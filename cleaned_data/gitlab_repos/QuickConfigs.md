# Repository Information
Name: QuickConfigs

# Files

File: config
================================================
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://gitlab.com/ma24th/QuickConfigs.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: FUNDING.yml
================================================
# These are supported funding model platforms
github:  # Replace with up to 4 GitHub Sponsors-enabled usernames e.g., [user1, user2]
patreon: rootx # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']
================================================

File: .gitlab-ci.yml
================================================
stages:
    - build
    - test
build:
    stage: build
    script:
        - echo "Building"
        - mkdir build
        - touch build/info.txt
    artifacts:
        paths:
            - build/
test:
    stage: test
    script:
        - echo "Testing"
        - test -f "build/info.txt"
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
interface gi0/0
 ip add 1.0.0.1 255.255.255.252
 no shutdown
interface tun0
 ip add 10.0.12.1 255.255.255.252
 tunnel source 1.0.0.1
 tunnel destination 1.0.0.2
 tunnel mode gre ip
!-----------------------! 
interface tun0
 ip ospf 1 area 12
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
interface gi0/0
 ip add 1.0.0.2 255.255.255.252
 no shutdown
interface tun0
 ip add 10.0.12.2 255.255.255.252
 tunnel source 1.0.0.2
 tunnel destination 1.0.0.1
 tunnel mode gre ip
!-----------------------!
interface tun0
 ip ospf 1 area 12
================================================

File: EIGRP Config.txt
================================================
Basic EIGRP Config
!-----------------------!
int se0/0
 ip add 10.0.12.2 255.255.255.252
 no shut
int lo0
 ip add 192.168.0.1 255.255.255.0
Default Network
!-----------------------!
ip default-network 192.168.0.0
EIGRP
!-----------------------!
router eigrp 12
 no auto-summary
 network 10.0.12.0 0.0.0.255
 network 192.168.0.0 0.0.0.255
Verify
!-----------------------!
show version
show ip eigrp topology 192.168.0.0/24
show ip route 
================================================

File: EIGRP Config.txt
================================================
Basic EIGRP Config
!-----------------------!
int gi0/0
 ip add 10.0.12.1 255.255.255.252
 no shut
int se1/0
 ip add 1.0.0.1 255.255.255.252
 no shut
router eigrp 12
 no auto-summary 
 network 10.0.12.0 0.0.0.255
Default Route Next-Hop
!-----------------------!
ip route 0.0.0.0 0.0.0.0 1.0.0.2
router eigrp 12
 redistribute static metric 1000000 1 255 1 1500
Default Route Next-Hop
!-----------------------! 
ip route 0.0.0.0 0.0.0.0 serial 1/0
router eigrp 12
 network 0.0.0.0
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
router ospf 1
 router-id 0.0.0.1 
 network 10.0.12.0 0.0.0.255 area 21
 network 10.0.12.0 0.0.0.3 area 12
interface fa0/0
 ip address 10.0.12.1 255.255.255.252
 ip ospf network broadcast
 ip ospf 1 area 0
 ip ospf priority 0
 ip ospf hello-interval 10
 ip ospf dead-interval 90
 ip mtu 1500
 no shutdown
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
router ospf 1
 router-id 0.0.0.2 
 network 10.0.12.0 0.0.0.255 area 21
 network 10.0.12.0 0.0.0.3 area 12
interface fa0/0
 ip address 10.0.12.2 255.255.255.252
 ip ospf network broadcast
 ip ospf 1 area 0
 ip ospf priority 0
 ip ospf hello-interval 10
 ip ospf dead-interval 100
 ip mtu 1492
 no shutdown
int lo0
 ip add 2.2.2.2 255.255.255.255
 ip ospf 1 area 0
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
router ospf 1
 router-id 0.0.0.1 
interface se1/0
 ip address 172.16.0.1 255.255.255.248
 ip ospf network point-to-point
 no shutdown
 ip ospf 1 area 0
================================================

File: CR2 Config.txt
================================================
CR5
!-----------------------!
router ospf 1
 router-id 0.0.0.5 
interface se1/0
 ip address 172.16.0.5 255.255.255.248
 ip ospf network point-to-point
 no shutdown
 ip ospf 1 area 0
interface lo0
 ip add 5.5.5.5 255.255.255.0
 ip ospf network point-to-point
 ip ospf 1 area 0
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
router ospf 1
 router-id 0.0.0.1 
interface gi0/0
 ip address 10.0.0.1 255.255.255.0
 ip ospf network broadcast
 ip ospf 1 area 1234
 ip ospf priority 0
 no shutdown
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
router ospf 1
 router-id 0.0.0.2
interface gi0/0
 ip address 10.0.0.2 255.255.255.0
 ip ospf network broadcast
 ip ospf 1 area 1234
 ip ospf priority 0
 no shutdown
================================================

File: CR3 Config.txt
================================================
CR3
!-----------------------!
router ospf 1
 router-id 0.0.0.3 
interface gi0/0
 ip address 10.0.0.3 255.255.255.0
 ip ospf network broadcast
 ip ospf 1 area 1234
 ip ospf priority 1
 no shutdown
================================================

File: CR4 Config.txt
================================================
CR4
!-----------------------!
router ospf 1
 router-id 0.0.0.4 
interface gi0/0
 ip address 10.0.0.4 255.255.255.0
 ip ospf network broadcast
 ip ospf 1 area 1234
 ip ospf priority 1
 no shutdown
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
router ospf 1
 router-id 0.0.0.1 
interface gi0/0
 ip address 10.0.12.1 255.255.255.0
 ip ospf 1 area 0
 no shutdown
interface se1/0
 ip address 10.0.13.1 255.255.255.0
 ip ospf 1 area 13
 no shutdown
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
router ospf 1
 router-id 0.0.0.2
interface gi0/0
 ip address 10.0.12.2 255.255.255.0
 ip ospf 1 area 0
 no shutdown
================================================

File: CR3 Config.txt
================================================
CR3
!-----------------------!
router ospf 1
 router-id 0.0.0.3 
interface se1/0
 ip address 10.0.13.3 255.255.255.0
 ip ospf 1 area 13
 no shutdown
!-----------------------!
interface lo1
 ip address 3.3.3.1 255.255.255.255
interface lo2
 ip address 3.3.3.2 255.255.255.255
interface lo3
 ip address 3.3.3.3 255.255.255.255
interface lo4
 ip address 3.3.3.4 255.255.255.255
route-map Loopbacks permit 10
 match interface lo1
 set metric 1
route-map Loopbacks permit 20
 match interface lo2
 set metric 2
route-map Loopbacks permit 30
 match interface lo3
 set metric 3
route-map Loopbacks permit 40
 match interface lo4
 set metric 4
router ospf 1
 redistribute connected subnets metric-type 1 route-map Loopbacks
!-----------------------!
router ospf 1 
 summary-address 3.3.3.0 255.255.255.252
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
router ospf 1
 router-id 0.0.0.1 
interface gi0/0
 ip address 10.0.12.1 255.255.255.0
 ip ospf 1 area 0
 no shutdown
interface se1/0
 ip address 10.0.13.1 255.255.255.0
 ip ospf 1 area 13
 no shutdown
!-----------------------! 
router ospf 1 
 area 13 range 3.3.3.0 255.255.255.252
 area 13 range 3.3.3.0 255.255.255.252 cost 0
 area 13 range 3.3.3.0 255.255.255.252 not-advertise 
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
router ospf 1
 router-id 0.0.0.2
interface gi0/0
 ip address 10.0.12.2 255.255.255.0
 ip ospf 1 area 0
 no shutdown
================================================

File: CR3 Config.txt
================================================
CR3
!-----------------------!
router ospf 1
 router-id 0.0.0.3 
interface se1/0
 ip address 10.0.13.3 255.255.255.0
 ip ospf 1 area 13
 no shutdown
!-----------------------!
interface lo1
 ip address 3.3.3.1 255.255.255.255
 ip ospf cost 1
interface lo2
 ip address 3.3.3.2 255.255.255.255
 ip ospf cost 2
interface lo3
 ip address 3.3.3.3 255.255.255.255
 ip ospf cost 3
interface lo4
 ip address 3.3.3.4 255.255.255.255
 ip ospf cost 4
router ospf 1
 network 3.3.3.0 0.0.0.255 area 13
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
router ospf 1
 router-id 0.0.0.1 
interface gi0/0
 ip address 10.0.0.1 255.255.255.0
 ip ospf network non-broadcast
 ip ospf 1 area 0
 ip ospf priority 0
 no shutdown
router ospf 1
 neighbor 10.0.0.3
 neighbor 10.0.0.4
interface lo1
 ip add 1.1.1.1 255.255.255.255
 ip ospf 1 area 0
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
router ospf 1
 router-id 0.0.0.2
interface gi0/0
 ip address 10.0.0.2 255.255.255.0
 ip ospf network non-broadcast
 ip ospf 1 area 0
 ip ospf priority 0
 no shutdown
router ospf 1
 neighbor 10.0.0.3
 neighbor 10.0.0.4
interface lo1
 ip add 2.2.2.2 255.255.255.255
 ip ospf 1 area 0
================================================

File: CR3 Config.txt
================================================
CR3
!-----------------------!
router ospf 1
 router-id 0.0.0.3 
interface gi0/0
 ip address 10.0.0.3 255.255.255.0
 ip ospf network non-broadcast
 ip ospf 1 area 0
  ip ospf priority 254
 no shutdown
router ospf 1
 neighbor 10.0.0.1
 neighbor 10.0.0.2
 neighbor 10.0.0.4
================================================

File: CR4 Config.txt
================================================
CR4
!-----------------------!
router ospf 1
 router-id 0.0.0.4 
interface gi0/0
 ip address 10.0.0.4 255.255.255.0
 ip ospf network non-broadcast
 ip ospf 1 area 0
 ip ospf priority 255
 no shutdown
router ospf 1
 neighbor 10.0.0.1
 neighbor 10.0.0.2
 neighbor 10.0.0.3
================================================

File: book.txt
================================================
sh ip ospf interface br
	state f/c
sh ip ospf interface
	adjacency
	timers
	type
sh ip ospf neighbor 
	state
	prio
sh ip ospf database
	link-id -> router-id
	link count
sh ip ospf database router adv 0.0.0.1
	stub
	p2p
sh ip ospf database router adv 0.0.0.5
show ip ospf rib 
	*
	>
show ip ospf rib 5.5.5.5
	lsa/lsid/adv-rid
wireshark
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
router ospf 1
 router-id 0.0.0.1 
interface gi0/0
 ip address 10.0.0.1 255.255.255.0
 ip ospf network point-to-multipoint
 ip ospf 1 area 1234
 no shutdown
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
router ospf 1
 router-id 0.0.0.2
interface gi0/0
 ip address 10.0.0.2 255.255.255.0
 ip ospf network point-to-multipoint
 ip ospf 1 area 0
 no shutdown
interface lo1
 ip add 2.2.2.2 255.255.255.255
 ip ospf 1 area 0
================================================

File: CR3 Config.txt
================================================
CR3
!-----------------------!
router ospf 1
 router-id 0.0.0.3 
interface gi0/0
 ip address 10.0.0.3 255.255.255.0
 ip ospf network point-to-multipoint
 ip ospf 1 area 1234
 no shutdown
================================================

File: CR4 Config.txt
================================================
CR4
!-----------------------!
router ospf 1
 router-id 0.0.0.4 
interface gi0/0
 ip address 10.0.0.4 255.255.255.0
 ip ospf network point-to-multipoint
 ip ospf 1 area 1234
 no shutdown
================================================

File: book.txt
================================================
sh ip ospf interface br
	state f/c
sh ip ospf interface
	adjacency
	timers
	type
sh ip ospf neighbor 
	state
	prio
sh ip ospf database
	link-id -> router-id
	link count
sh ip ospf database router adv 0.0.0.1
	stub
	p2p
sh ip ospf database router adv 0.0.0.5
show ip ospf rib 
	*
	>
show ip ospf rib 5.5.5.5
	lsa/lsid/adv-rid
wireshark
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
router ospf 1
 router-id 0.0.0.1 
interface gi0/0
 ip address 10.0.0.1 255.255.255.0
 ip ospf network point-to-multipoint non-broadcast
 ip ospf 1 area 1234
 no shutdown
router ospf 1
 neighbor 10.0.0.2
 neighbor 10.0.0.3
 neighbor 10.0.0.4
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
router ospf 1
 router-id 0.0.0.2
interface gi0/0
 ip address 10.0.0.2 255.255.255.0
 ip ospf network point-to-multipoint non-broadcast
 ip ospf 1 area 1234
 no shutdown
router ospf 1
 neighbor 10.0.0.1
 neighbor 10.0.0.3
 neighbor 10.0.0.4
interface lo1
 ip add 2.2.2.2 255.255.255.255
 ip ospf 1 area 0
================================================

File: CR3 Config.txt
================================================
CR3
!-----------------------!
router ospf 1
 router-id 0.0.0.3 
interface gi0/0
 ip address 10.0.0.3 255.255.255.0
 ip ospf network point-to-multipoint non-broadcast
 ip ospf 1 area 1234
 no shutdown
router ospf 1
 neighbor 10.0.0.1
 neighbor 10.0.0.2
 neighbor 10.0.0.4
================================================

File: CR4 Config.txt
================================================
CR4
!-----------------------!
router ospf 1
 router-id 0.0.0.4 
interface gi0/0
 ip address 10.0.0.4 255.255.255.0
 ip ospf network point-to-multipoint non-broadcast
 ip ospf 1 area 1234
 no shutdown
router ospf 1
 neighbor 10.0.0.1
 neighbor 10.0.0.2
 neighbor 10.0.0.3
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
router ospf 1
 router-id 0.0.0.1 
interface se1/0
 ip address 10.0.12.1 255.255.255.0
 ip ospf network point-to-point
 no shutdown
 ip ospf 1 area 0
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
router ospf 1
 router-id 0.0.0.2 
interface se1/0
 ip address 10.0.12.2 255.255.255.0
 ip ospf network point-to-point
 no shutdown
 ip ospf 1 area 0
interface lo1
 ip add 2.2.2.2 255.255.255.0
 ip ospf network point-to-point
 ip ospf 1 area 0
================================================

File: PPPoE Client Config.txt
================================================
Cisco PPPoE Client
!-----------------------!
hostname CR2
interface gi0/0
  pppoe-client dial-pool-number 12
interface dialer 1
 dialer pool 12
 ip mtu 1492
 encapsulation ppp
 ip address negotiated
Authentication
!-----------------------!
interface dialer 1
 ppp pap sent-username CR2 password Pa$$w0rd
interface dialer 1
 ppp chap hostname CR2
 ppp chap password Pa$$w0rd
Routing 
!-----------------------!
ip route 0.0.0.0 0.0.0.0 1.0.0.10 
================================================

File: PPPoE Server Config.txt
================================================
PPPoE Server
!-----------------------!
hostname CR1
bba-group pppoe PPPOE
 virtual-template 1
interface gi0/0
 pppoe enable group PPPOE
 no shutdown
interface lo1
 ip address 1.0.0.10 255.255.255.255
interface virtual-template1
 encapsulation ppp
 ip unnumbered lo1
 ip mtu 1492
 peer default ip address pool IPCP
ip local pool IPCP 1.0.0.1
Authentication
!-----------------------!
interface virtual-template1
 ppp authentication pap
interface virtual-template1
 ppp authentication chap
username CR2 password Pa$$w0rd
Verification
!-----------------------!
debug ppp negotiation
who
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
key chain RIP
 key 1
  key-string cisco
interface fa0/0
 ip address 10.0.12.1 255.255.255.252
 mac-address 0011.1111.1111
 no shutdown
 ip rip authentication mode md5
 ip rip authentication key-chain RIP
interface lo0
 ip add 1.1.1.1 255.255.255.255
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 1.0.0.0 
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
key chain RIP
 key 1
  key-string cisco
interface fa0/0
 ip address 10.0.12.2 255.255.255.252
 mac-address 0022.2222.22
 no shutdown
 ip rip authentication mode text
 ip rip authentication key-chain RIP
interface lo0
 ip add 2.2.2.2 255.255.255.255
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 2.0.0.0
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
interface fa0/0
 ip address 10.0.12.1 255.255.255.252
 mac-address 0011.1111.1111
 no shutdown
router rip
 version 2
 no auto-summary
 network 10.0.0.0
Offset Filtering
!-----------------------! 
access-list 1 permit 2.2.2.0 0.0.0.3
router rip
 offset-list 1 in 16 fa0/0
 offset-list 0 in 16 fa0/0
Distribute Filtering
!-----------------------! 
ip prefix-list L1 deny 2.2.2.1/32
ip prefix-list L1 permit 0.0.0.0/0 le 32
router rip
 distribute-list prefix L1 in fa0/0
Distribute + Gateway
!-----------------------!
ip prefix-list L1 deny 2.2.2.1/32
ip prefix-list L1 permit 0.0.0.0/0 le 32
ip prefix-list CR2 permit 10.0.12.2/32
router rip
 distribute-list prefix L1 gateway CR2 in fa0/0
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
interface fa0/0
 ip address 10.0.12.2 255.255.255.252
 mac-address 0022.2222.22
 no shutdown
interface lo1
 ip add 2.2.2.1 255.255.255.255
interface lo2
 ip add 2.2.2.2 255.255.255.255
interface lo3
 ip add 2.2.2.3 255.255.255.255
interface lo4
 ip add 2.2.2.4 255.255.255.255
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 2.0.0.0
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
interface fa0/0
 ip address 10.0.12.1 255.255.255.252
 mac-address 0011.1111.1111
 no shutdown
interface lo0
 ip add 1.1.1.1 255.255.255.255
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 1.0.0.0 
 passive-interface default
 neighbor 10.0.12.2
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
interface fa0/0
 ip address 10.0.12.2 255.255.255.252
 mac-address 0022.2222.22
 no shutdown
interface lo0
 ip add 2.2.2.2 255.255.255.255
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 2.0.0.0
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
interface fa0/0
 ip address 10.0.12.1 255.255.255.0
 no shutdown
interface se1/0
 ip address 172.16.13.1 255.255.255.0
 ip ospf cost 1
 no shutdown 
router rip
 version 2
 no auto-summary
 network 10.0.0.0
router ospf 13
 router-id 0.0.0.1
 network 172.16.13.0 0.0.0.255 area 13
!-----------------------!
ip prefix-list L1 permit 3.3.3.1/32 
route-map LOOP permit 10
 match ip address prefix-list L1
router rip 
 redistribute ospf 13 metric 0
 redistribute ospf 13 metric transparent
 redistribute ospf 13 metric transparent route-map LOOP
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
interface fa0/0
 ip address 10.0.12.2 255.255.255.0
 no shutdown
router rip
 version 2
 no auto-summary
 network 10.0.0.0
================================================

File: CR3 Config.txt
================================================
CR3
!-----------------------!
interface se1/0
 ip address 172.16.13.3 255.255.255.0
 no shutdown
interface lo1
 ip add 3.3.3.1 255.255.255.255
interface lo2
 ip add 3.3.3.2 255.255.255.255
interface lo3
 ip add 3.3.3.3 255.255.255.255
route-map LOOP permit 10
 match interface lo1
 set metric 12
route-map LOOP permit 20
 match interface lo2
 set metric 13
route-map LOOP permit 30
 match interface lo3
 set metric 14
router ospf 13
 router-id 0.0.0.3
 network 172.16.13.0 0.0.0.255 area 13
 redistribute connected subnets metric-type 1 route-map LOOP
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
interface fa0/0
 ip address 10.0.12.1 255.255.255.0
 no shutdown
!
interface se1/0
 ip address 172.16.13.1 255.255.255.0
 no shutdown
!
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 172.16.0.0
route-map RIP permit 10
 set interface se1/0
router rip
 default-information originate route-map RIP
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
interface fa0/0
 ip address 10.0.12.2 255.255.255.0
 no shutdown
!
interface fa0/1
 ip address 192.168.23.2 255.255.255.0
 no shutdown
!
interface lo1
 ip add 2.2.2.1 255.255.255.255
interface lo2
 ip add 2.2.2.2 255.255.255.255
interface lo3
 ip add 2.2.2.3 255.255.255.255
!
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 192.168.23.0
 network 2.0.0.0
Summarization 
!-----------------------!
int fa0/0
 ip summary-address rip 2.2.2.0 255.255.255.248
!
int fa0/1
 ip summary-address rip 2.2.2.0 255.255.255.248
ip route 2.2.2.0 255.255.255.248 null0
================================================

File: CR3 Config.txt
================================================
CR3
!-----------------------!
interface fa0/1
 ip address 192.168.23.3 255.255.255.0
 no shutdown
!
interface se1/0
 ip address 172.16.13.3 255.255.255.0
 no shutdown
!
router rip
 version 2
 no auto-summary
 network 192.168.23.0
 network 172.16.0.0
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
interface fa0/0
 ip address 10.0.12.1 255.255.255.252
 mac-address 0011.1111.1111
 no shutdown
interface lo1
 ip add 1.1.1.1 255.255.255.255
router rip
 network 10.0.0.0
 network 1.0.0.0
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
interface fa0/0
 ip address 10.0.12.2 255.255.255.252
 mac-address 0022.2222.2222
 ip rip v2-broadcast 
 ip rip send version 1 2 
 no shutdown
! 
interface lo1
 ip add 2.2.2.1 255.255.255.255
! 
interface lo2
 ip add 2.2.2.2 255.255.255.255
! 
interface lo3
 ip add 2.2.2.3 255.255.255.255
!
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 2.0.0.0
 flash-update-threshold 20
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
int lo0 
 ip add 10.0.12.1 255.255.255.255  
! 
interface lo1
 ip add 1.1.1.1 255.255.255.255
! 
int virtual-template 12  
 ip unnumbered lo0 
 ip mtu 1492 
 encapsulation ppp 
 peer default ip address pool IPCP
!
ip local pool IPCP 10.0.12.2
!
bba-group pppoe PPPOE 
 virtual-template 12 
!
interface fa0/0
 pppoe enable group PPPOE
 mac-address 0011.1111.1111
 no shutdown
!
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 1.0.0.0
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
interface dialer1 
 ip address negotiated 
 ip mtu 1492 
 encapsulation ppp 
 dialer pool 12 
!
interface fa0/0
 mac-address 0022.2222.2222
 pppoe-client dial-pool-number 12
 no shutdown
! 
interface lo1
 ip add 2.2.2.2 255.255.255.255
!
router rip
 version 2
 no auto-summary
 network 10.0.0.0
 network 2.0.0.0
 no validate-update-source
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
ipv6 unicast-routing
!
interface se1/0
 encapsulation frame-relay
 no frame-relay inverse-arp
 no shutdown
!
int se1/0.123 multipoint
 no frame-relay inverse-arp
 frame-relay map ip 10.0.123.2 102 broadcast
 frame-relay map ip 10.0.123.3 103 broadcast
 frame-relay map ipv6 2001:123::2 102 
 frame-relay map ipv6 2001:123::3 103 
 frame-relay map ipv6 fe80::2 102 broadcast
 frame-relay map ipv6 fe80::3 103 broadcast
 ip address 10.0.123.1 255.255.255.0
 ip split-horizon
 ipv6 address fe80::1 link-local
 ipv6 address 2001:123::1/64
 ipv6 rip RIPng enable
interface lo1
 ip address 1.1.1.1 255.255.255.255
 ipv6 address 1::1/128
 ipv6 rip RIPng enable
ipv6 router rip RIPng 
 split-horizon 
 poison-reverse
router rip
 version 2
 no auto-summary
 network 1.0.0.0
 network 10.0.0.0
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
ipv6 unicast-routing
!
interface se1/0
 encapsulation frame-relay
 no frame-relay inverse-arp
 no shutdown
!
interface se1/0.123 point-to-point
 no frame-relay inverse-arp
 frame-relay interface-dlci 201 
 ip address 10.0.123.2 255.255.255.0
 ipv6 address fe80::2 link-local
 ipv6 address 2001:123::2/64
 ipv6 rip RIPng enable
 no shutdown
!
interface lo1
 ip address 2.2.2.2 255.255.255.255
 ipv6 address 2::2/128
 ipv6 rip RIPng enable
!
router rip
 version 2
 no auto-summary
 network 2.0.0.0
 network 10.0.0.0
================================================

File: CR3 Config.txt
================================================
CR3
!-----------------------!
ipv6 unicast-routing
!
interface se1/0
 encapsulation frame-relay
 no frame-relay inverse-arp
 no shutdown
!
interface se1/0.123 point-to-point
 no frame-relay inverse-arp
 frame-relay interface-dlci 301 
 ip address 10.0.123.3 255.255.255.0
 ipv6 address fe80::3 link-local
 ipv6 address 2001:123::3/64
 ipv6 rip RIPng enable
 no shutdown
!
interface lo1
 ip address 3.3.3.3 255.255.255.255
 ipv6 address 3::3/128
 ipv6 rip RIPng enable
!
router rip
 version 2
 no auto-summary
 network 3.0.0.0
 network 10.0.0.0
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
ipv6 unicast-routing
interface fa0/0
 ipv6 address fe80::1 link-local
 ipv6 address 2001:12::1/64
 ipv6 rip RIPng enable
interface lo1
 ipv6 address 1::1/128 
 ipv6 rip RIPng enable
!-----------------------!
show ipv6 protocols
show ipv6 interface fa0/0
show ipv6 rip 
show ipv6 rip database 
show ipv6 rip next-hops
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
ipv6 unicast-routing
interface fa0/0
 ipv6 address fe80::2 link-local
 ipv6 address 2001:12::2/64
 ipv6 rip RIPng enable
interface lo1
 ipv6 address 2::2/128 
 ipv6 rip RIPng enable
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
ipv6 unicast-routing
!
interface fa0/0
 ipv6 address fe80::1 link-local
 ipv6 rip RIPng enable
Filtering
!-----------------------!
ipv6 prefix-list L123 permit 2::/126 ge 128
ipv6 prefix-list L1 deny 2::1/128
ipv6 prefix-list L1 permit ::/0 le 128
ipv6 router rip RIPng
 distribute-list prefix-list L123 in
 distribute-list prefix-list L1 in fa0/0
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
ipv6 unicast-routing
interface fa0/0
 ipv6 address fe80::2 link-local
 ipv6 rip RIPng enable
interface lo1
 ipv6 address 2::1/128 
 ipv6 rip RIPng enable
interface lo2
 ipv6 address 2::2/128 
 ipv6 rip RIPng enable
interface lo3
 ipv6 address 2::3/128 
 ipv6 rip RIPng enable
interface lo4
 ipv6 address 2::4/128 
 ipv6 rip RIPng enable
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
ipv6 unicast-routing
interface fa0/0
 ipv6 address fe80::1 link-local
 ipv6 rip RIPng enable
 ipv6 rip RIPng metric-offset 4
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
ipv6 unicast-routing
interface fa0/0
 ipv6 address fe80::2 link-local
 ipv6 rip RIPng enable
interface lo1
 ipv6 address 2::2/128 
 ipv6 rip RIPng enable
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
ipv6 unicast-routing
ipv6 router ospf 13
 router-id 0.0.0.1
interface fa0/0
 ipv6 address fe80::1 link-local
 ipv6 address 2001:12::1/64
 ipv6 rip RIPng enable
 no shutdown
interface se1/0
 ipv6 address fe80::1 link-local
 ipv6 address 2001:13::1/64
 ipv6 ospf 13 area 0
 ipv6 ospf cost 1
 no shutdown 
ipv6 router rip RIPng
 redistribute ospf 13 
!-----------------------!
ipv6 prefix-list L1 permit 3::1/128 
ipv6 prefix-list L1 permit 2001:13::/64 
route-map LOOP permit 10
 match ipv6 address prefix-list L1
ipv6 router rip RIPng
 redistribute ospf 13 
 redistribute ospf 13 metric 1
 redistribute ospf 13 metric 1 route-map LOOP
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
ipv6 unicast-routing
interface fa0/0
 ipv6 address fe80::2 link-local
 ipv6 address 2001:12::2/64
 ipv6 rip RIPng enable
 no shutdown
================================================

File: CR3 Config.txt
================================================
CR3
!-----------------------!
ipv6 unicast-routing
interface se1/0
 ipv6 address fe80::3 link-local
 ipv6 address 2001:13::3/64
 ipv6 ospf 13 area 0
 ipv6 ospf cost 1
 no shutdown 
interface lo1
 ipv6 address 3::1/128
interface lo2
 ipv6 address 3::2/128
interface lo3
 ipv6 address 3::3/128
route-map LOOP permit 10
 match interface lo1
 set metric 12
route-map LOOP permit 20
 match interface lo2
 set metric 13
route-map LOOP permit 30
 match interface lo3
 set metric 14
ipv6 router ospf 13
 router-id 0.0.0.3
 redistribute connected metric-type 1 route-map LOOP
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
ipv6 unicast-routing
!
interface fa0/0
 ipv6 address fe80::1 link-local
 ipv6 rip RIPng enable
 no shutdown
!
interface se1/0
 ipv6 address fe80::1 link-local
 ipv6 rip RIPng enable
 no shutdown 
!
int lo1 
 ipv6 address 1::1/128
 ipv6 rip RIPng enable 
!-----------------------!
int fa0/0  
 ipv6 rip RIPng default-information only
 ipv6 rip RIPng default-information originate metric 4
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
ipv6 unicast-routing
!
interface fa0/0
 ipv6 address fe80::2 link-local
 ipv6 rip RIPng enable
 no shutdown
!
interface fa0/1
 ipv6 address fe80::2 link-local
 ipv6 rip RIPng enable
 no shutdown
!
interface lo1
 ipv6 address 2::1/128 
 ipv6 rip RIPng enable
interface lo2
 ipv6 address 2::2/128 
 ipv6 rip RIPng enable 
interface lo3
 ipv6 address 2::3/128 
 ipv6 rip RIPng enable
Summarization
!-----------------------!
int fa0/0
 ipv6 rip RIPng summary-address 2::/120
!
int fa0/1
 ipv6 rip RIPng summary-address 2::/120
! 
ipv6 route 2::/120 null0
================================================

File: CR3 Config.txt
================================================
CR3
!-----------------------!
ipv6 unicast-routing
!
interface fa0/1
 ipv6 address fe80::3 link-local
 ipv6 rip RIPng enable
 no shutdown
!
interface se1/0
 ipv6 address fe80::3 link-local
 ipv6 rip RIPng enable
 no shutdown 
!
int lo1 
 ipv6 address 3::3/128
 ipv6 rip RIPng enable 
================================================

File: CR1 Config.txt
================================================
CR1
!-----------------------!
ipv6 unicast-routing
interface fa0/0
 mac-address 0011.1111.1111
 ipv6 address fe80::1 link-local
 ipv6 rip RIPng enable
 no shutdown
ipv6 router rip RIPng 
 timers 30 180 0 120
================================================

File: CR2 Config.txt
================================================
CR2
!-----------------------!
ipv6 unicast-routing
interface fa0/0
 mac-address 0022.2222.2222
 ipv6 address fe80::1 link-local
 ipv6 rip RIPng enable
 no shutdown
interface lo1
 ipv6 address 2::1/128 
 ipv6 rip RIPng enable
interface lo2
 ipv6 address 2::2/128 
 ipv6 rip RIPng enable 
interface lo3
 ipv6 address 2::3/128 
 ipv6 rip RIPng enable
================================================

File: Config.txt
================================================
Basic SRX Config
==================================================
set system root-authentication encrypted-password "$1$4zHjLsyX$X61xzWZbSkPYer/d5M7zb1"
set system services telnet
set interfaces ge-0/0/0 unit 0 family inet address 2.0.0.1/24
set interfaces ge-0/0/1 unit 0 family inet address 10.0.0.1/24
set routing-options static route 0.0.0.0/0 next-hop 2.0.0.2
edit security zones security-zone trust
 delete
 set interfaces ge-0/0/1.0
edit security zones security-zone untrust 
 delete
 set interfaces ge-0/0/0.0 host-inbound-traffic system-services telnet
Junos Applications
==================================================
show configuration groups junos-defaults applications application
show configuration groups junos-defaults applications | match "icmp|ping" | display set
Allow Applications
==================================================
edit security policies from-zone untrust to-zone trust 
 set policy ALLOW_ADMIN match application junos-ping
 set policy ALLOW_ADMIN match application junos-telnet
 set policy ALLOW_ADMIN match application junos-ssh
 set policy ALLOW_ADMIN match application junos-https
 set policy ALLOW_ADMIN match source-address any
 set policy ALLOW_ADMIN match destination-address any
 set policy ALLOW_ADMIN then permit
insert policy ALLOW_ADMIN before policy default-deny
Define Application Sets
==================================================
set applications application TELNET protocol tcp
set applications application TELNET destination-port 2000
set applications application-set ADMIN_SET application junos-ssh
set applications application-set ADMIN_SET application junos-https
set applications application-set ADMIN_SET application junos-telnet
set applications application-set ADMIN_SET application junos-ping
set applications application-set ADMIN_SET application TELNET
edit security policies from-zone untrust to-zone trust 
 set policy ALLOW_ADMIN match application ADMIN_SET
 set policy ALLOW_ADMIN match source-address any
 set policy ALLOW_ADMIN match destination-address any
 set policy ALLOW_ADMIN then permit
insert policy ALLOW_ADMIN before policy default-deny
================================================

File: Windows, Linux & VPCS.txt
================================================
Windows IPv4 Network Adapter
==================================================
Remove-NetIPAddress -InterfaceAlias Loopback
New-NetIPAddress -InterfaceAlias Loopback –IPAddress 2.0.0.2 -PrefixLength 24
netsh interface ip set address "Loopback" static 2.0.0.2 255.255.255.0
Windows IPv4 Route
==================================================
route add 10.0.0.0 mask 255.255.255.0 2.0.0.1
Linux IPv4 Config & Route
==================================================
ifconfig eth0 10.0.0.10/24
route add -net 0.0.0.0 netmask 0.0.0.0 gw 10.0.0.1
VPCS IPv4 Config & Route
==================================================
ip 10.0.0.10/24 10.0.0.1 
================================================

File: Config.txt
================================================
set security ike proposal ike-prop-vpn-c0b054a9-1 authentication-method pre-shared-keys 
set security ike proposal ike-prop-vpn-c0b054a9-1 authentication-algorithm sha1
set security ike proposal ike-prop-vpn-c0b054a9-1 encryption-algorithm aes-128-cbc
set security ike proposal ike-prop-vpn-c0b054a9-1 lifetime-seconds 28800
set security ike proposal ike-prop-vpn-c0b054a9-1 dh-group group2
set security ike policy ike-pol-vpn-c0b054a9-1 mode main 
set security ike policy ike-pol-vpn-c0b054a9-1 proposals ike-prop-vpn-c0b054a9-1
set security ike policy ike-pol-vpn-c0b054a9-1 pre-shared-key ascii-text ullOfhXpV7fjUU0er8YXCNYdqGvIBucl
set security ike gateway gw-vpn-c0b054a9-1 ike-policy ike-pol-vpn-c0b054a9-1
QC -> set security ike gateway gw-vpn-c0b054a9-1 external-interface fe-0/0/0.0
set security ike gateway gw-vpn-c0b054a9-1 address 52.63.29.199
set security ike traceoptions file kmd
set security ike traceoptions file size 1024768
set security ike traceoptions file files 10
set security ike traceoptions flag all
set security ipsec proposal ipsec-prop-vpn-c0b054a9-1 protocol esp
set security ipsec proposal ipsec-prop-vpn-c0b054a9-1 authentication-algorithm hmac-sha1-96
set security ipsec proposal ipsec-prop-vpn-c0b054a9-1 encryption-algorithm aes-128-cbc
set security ipsec proposal ipsec-prop-vpn-c0b054a9-1 lifetime-seconds 3600
set security ipsec policy ipsec-pol-vpn-c0b054a9-1 perfect-forward-secrecy keys group2
set security ipsec policy ipsec-pol-vpn-c0b054a9-1 proposals ipsec-prop-vpn-c0b054a9-1
set security ipsec vpn vpn-c0b054a9-1 bind-interface st0.1
set security ipsec vpn vpn-c0b054a9-1 ike gateway gw-vpn-c0b054a9-1
set security ipsec vpn vpn-c0b054a9-1 ike ipsec-policy ipsec-pol-vpn-c0b054a9-1
set security ipsec vpn vpn-c0b054a9-1 df-bit clear 
set interfaces st0.1 family inet address 169.254.33.138/30
set interfaces st0.1 family inet mtu 1436
set security zones security-zone trust interfaces st0.1
set security zones security-zone trust host-inbound-traffic protocols bgp
set security flow tcp-mss ipsec-vpn mss 1387
set security ipsec vpn vpn-c0b054a9-1 vpn-monitor source-interface st0.1 
set security ipsec vpn vpn-c0b054a9-1 vpn-monitor destination-ip 169.254.33.137
QC -> set routing-options static route 172.31.0.0/16 next-hop st0.1
set security ike proposal ike-prop-vpn-c0b054a9-2 authentication-method pre-shared-keys 
set security ike proposal ike-prop-vpn-c0b054a9-2 authentication-algorithm sha1
set security ike proposal ike-prop-vpn-c0b054a9-2 encryption-algorithm aes-128-cbc
set security ike proposal ike-prop-vpn-c0b054a9-2 lifetime-seconds 28800
set security ike proposal ike-prop-vpn-c0b054a9-2 dh-group group2
set security ike policy ike-pol-vpn-c0b054a9-2 mode main 
set security ike policy ike-pol-vpn-c0b054a9-2 proposals ike-prop-vpn-c0b054a9-2
set security ike policy ike-pol-vpn-c0b054a9-2 pre-shared-key ascii-text dBO_6eIpSlctVmoqMDLSkY1JX1RhcHNt
set security ike gateway gw-vpn-c0b054a9-2 ike-policy ike-pol-vpn-c0b054a9-2
QC -> set security ike gateway gw-vpn-c0b054a9-2 external-interface fe-0/0/0.0
set security ike gateway gw-vpn-c0b054a9-2 address 52.63.117.182 
set security ipsec proposal ipsec-prop-vpn-c0b054a9-2 protocol esp
set security ipsec proposal ipsec-prop-vpn-c0b054a9-2 authentication-algorithm hmac-sha1-96
set security ipsec proposal ipsec-prop-vpn-c0b054a9-2 encryption-algorithm aes-128-cbc
set security ipsec proposal ipsec-prop-vpn-c0b054a9-2 lifetime-seconds 3600
set security ipsec policy ipsec-pol-vpn-c0b054a9-2 perfect-forward-secrecy keys group2
set security ipsec policy ipsec-pol-vpn-c0b054a9-2 proposals ipsec-prop-vpn-c0b054a9-2
set security ipsec vpn vpn-c0b054a9-2 bind-interface st0.2
set security ipsec vpn vpn-c0b054a9-2 ike gateway gw-vpn-c0b054a9-2
set security ipsec vpn vpn-c0b054a9-2 ike ipsec-policy ipsec-pol-vpn-c0b054a9-2
set security ipsec vpn vpn-c0b054a9-2 df-bit clear 
set security ike gateway gw-vpn-c0b054a9-2 dead-peer-detection
set interfaces st0.2 family inet address 169.254.32.50/30
set interfaces st0.2 family inet mtu 1436
set security zones security-zone trust interfaces st0.2
set security zones security-zone untrust host-inbound-traffic system-services ike
set security zones security-zone trust host-inbound-traffic protocols bgp
set security flow tcp-mss ipsec-vpn mss 1387
set security ipsec vpn vpn-c0b054a9-2 vpn-monitor source-interface st0.2 
set security ipsec vpn vpn-c0b054a9-2 vpn-monitor destination-ip 169.254.32.49
QC -> set routing-options static route 172.31.0.0/16 next-hop st0.2
==================================================
edit security policies
set from-zone trust to-zone trust policy ALLOW_ALL match source-address any
set from-zone trust to-zone trust policy ALLOW_ALL match destination-address any
set from-zone trust to-zone trust policy ALLOW_ALL match application any
set from-zone trust to-zone trust policy ALLOW_ALL then permit
================================================

File: vpn-c0b054a9.txt
================================================
# Amazon Web Services
# Virtual Private Cloud
#
# AWS utilizes unique identifiers to manipulate the configuration of 
# a VPN Connection. Each VPN Connection is assigned a VPN Connection Identifier
# and is associated with two other identifiers, namely the 
# Customer Gateway Identifier and the Virtual Private Gateway Identifier.
#
# Your VPN Connection ID  		    : vpn-c0b054a9
# Your Virtual Private Gateway ID           : vgw-d30032ce
# Your Customer Gateway ID 		    : cgw-f21e2cef
#
# This configuration consists of two tunnels. Both tunnels must be 
# configured on your Customer Gateway.
#
#
# --------------------------------------------------------------------------------
# IPSec Tunnel #1
# --------------------------------------------------------------------------------
# #1: Internet Key Exchange (IKE) Configuration
#
# A proposal is established for the supported IKE encryption, 
# authentication, Diffie-Hellman, and lifetime parameters.
#
set security ike proposal ike-prop-vpn-c0b054a9-1 authentication-method pre-shared-keys 
set security ike proposal ike-prop-vpn-c0b054a9-1 authentication-algorithm sha1
set security ike proposal ike-prop-vpn-c0b054a9-1 encryption-algorithm aes-128-cbc
set security ike proposal ike-prop-vpn-c0b054a9-1 lifetime-seconds 28800
set security ike proposal ike-prop-vpn-c0b054a9-1 dh-group group2
# An IKE policy is established to associate a Pre Shared Key with the  
# defined proposal.
#
set security ike policy ike-pol-vpn-c0b054a9-1 mode main 
set security ike policy ike-pol-vpn-c0b054a9-1 proposals ike-prop-vpn-c0b054a9-1
set security ike policy ike-pol-vpn-c0b054a9-1 pre-shared-key ascii-text ullOfhXpV7fjUU0er8YXCNYdqGvIBucl
# The IKE gateway is defined to be the Virtual Private Gateway. The gateway 
# configuration associates a local interface, remote IP address, and
# IKE policy.
#
# This example shows the outside of the tunnel as interface ge-0/0/0.0.
# This should be set to the interface that IP address 210.10.218.230 is
# associated with.
# This address is configured with the setup for your Customer Gateway.
#
# If the address changes, the Customer Gateway and VPN Connection must be recreated.
#
set security ike gateway gw-vpn-c0b054a9-1 ike-policy ike-pol-vpn-c0b054a9-1
set security ike gateway gw-vpn-c0b054a9-1 external-interface ge-0/0/0.0
set security ike gateway gw-vpn-c0b054a9-1 address 52.63.29.199
# Troubleshooting IKE connectivity can be aided by enabling IKE tracing.
# The configuration below will cause the router to log IKE messages to
# the 'kmd' log. Run 'show messages kmd' to retrieve these logs.
# set security ike traceoptions file kmd
# set security ike traceoptions file size 1024768
# set security ike traceoptions file files 10
# set security ike traceoptions flag all
# #2: IPSec Configuration
#
# The IPSec proposal defines the protocol, authentication, encryption, and
# lifetime parameters for our IPSec security association.
#
set security ipsec proposal ipsec-prop-vpn-c0b054a9-1 protocol esp
set security ipsec proposal ipsec-prop-vpn-c0b054a9-1 authentication-algorithm hmac-sha1-96
set security ipsec proposal ipsec-prop-vpn-c0b054a9-1 encryption-algorithm aes-128-cbc
set security ipsec proposal ipsec-prop-vpn-c0b054a9-1 lifetime-seconds 3600
# The IPSec policy incorporates the Diffie-Hellman group and the IPSec
# proposal.
#
set security ipsec policy ipsec-pol-vpn-c0b054a9-1 perfect-forward-secrecy keys group2
set security ipsec policy ipsec-pol-vpn-c0b054a9-1 proposals ipsec-prop-vpn-c0b054a9-1
# A security association is defined here. The IPSec Policy and IKE gateways
# are associated with a tunnel interface (st0.1).
# The tunnel interface ID is assumed; if other tunnels are defined on
# your router, you will need to specify a unique interface name 
# (for example, st0.10).
#
set security ipsec vpn vpn-c0b054a9-1 bind-interface st0.1
set security ipsec vpn vpn-c0b054a9-1 ike gateway gw-vpn-c0b054a9-1
set security ipsec vpn vpn-c0b054a9-1 ike ipsec-policy ipsec-pol-vpn-c0b054a9-1
set security ipsec vpn vpn-c0b054a9-1 df-bit clear 
# This option enables IPSec Dead Peer Detection, which causes periodic
# messages to be sent to ensure a Security Association remains operational.
#
set security ike gateway gw-vpn-c0b054a9-1 dead-peer-detection
# #3: Tunnel Interface Configuration
#
# The tunnel interface is configured with the internal IP address.
#
set interfaces st0.1 family inet address 169.254.33.138/30
set interfaces st0.1 family inet mtu 1436
set security zones security-zone trust interfaces st0.1
# The security zone protecting external interfaces of the router must be 
# configured to allow IKE traffic inbound.
#
set security zones security-zone untrust host-inbound-traffic system-services ike
# The security zone protecting internal interfaces (including the logical 
# tunnel interfaces) must be configured to allow BGP traffic inbound.
#
set security zones security-zone trust host-inbound-traffic protocols bgp
# This option causes the router to reduce the Maximum Segment Size of
# TCP packets to prevent packet fragmentation.
#
set security flow tcp-mss ipsec-vpn mss 1387
# --------------------------------------------------------------------------------
# #4: Static Route Configuration
#
# VPN monitoring is used in order to provide failover with multiple tunnels. If the primary tunnel fails, the redundant tunnel will automatically be used.
#
set security ipsec vpn vpn-c0b054a9-1 vpn-monitor source-interface st0.1 
set security ipsec vpn vpn-c0b054a9-1 vpn-monitor destination-ip 169.254.33.137
# Your Customer Gateway needs to set a static route for the prefix corresponding to your VPC on the tunnel.
# An example for a VPC with the prefix 10.0.0.0/16 is provided below
# set routing-options static route 10.0.0.0/16 next-hop st0.1
#
# --------------------------------------------------------------------------------
# IPSec Tunnel #2
# --------------------------------------------------------------------------------
# #1: Internet Key Exchange (IKE) Configuration
#
# A proposal is established for the supported IKE encryption, 
# authentication, Diffie-Hellman, and lifetime parameters.
#
set security ike proposal ike-prop-vpn-c0b054a9-2 authentication-method pre-shared-keys 
set security ike proposal ike-prop-vpn-c0b054a9-2 authentication-algorithm sha1
set security ike proposal ike-prop-vpn-c0b054a9-2 encryption-algorithm aes-128-cbc
set security ike proposal ike-prop-vpn-c0b054a9-2 lifetime-seconds 28800
set security ike proposal ike-prop-vpn-c0b054a9-2 dh-group group2
# An IKE policy is established to associate a Pre Shared Key with the  
# defined proposal.
#
set security ike policy ike-pol-vpn-c0b054a9-2 mode main 
set security ike policy ike-pol-vpn-c0b054a9-2 proposals ike-prop-vpn-c0b054a9-2
set security ike policy ike-pol-vpn-c0b054a9-2 pre-shared-key ascii-text dBO_6eIpSlctVmoqMDLSkY1JX1RhcHNt
# The IKE gateway is defined to be the Virtual Private Gateway. The gateway 
# configuration associates a local interface, remote IP address, and
# IKE policy.
#
# This example shows the outside of the tunnel as interface ge-0/0/0.0.
# This should be set to the interface that IP address 210.10.218.230 is
# associated with.
# This address is configured with the setup for your Customer Gateway.
#
# If the address changes, the Customer Gateway and VPN Connection must be recreated.
#
set security ike gateway gw-vpn-c0b054a9-2 ike-policy ike-pol-vpn-c0b054a9-2
set security ike gateway gw-vpn-c0b054a9-2 external-interface ge-0/0/0.0
set security ike gateway gw-vpn-c0b054a9-2 address 52.63.117.182
# Troubleshooting IKE connectivity can be aided by enabling IKE tracing.
# The configuration below will cause the router to log IKE messages to
# the 'kmd' log. Run 'show messages kmd' to retrieve these logs.
# set security ike traceoptions file kmd
# set security ike traceoptions file size 1024768
# set security ike traceoptions file files 10
# set security ike traceoptions flag all
# #2: IPSec Configuration
#
# The IPSec proposal defines the protocol, authentication, encryption, and
# lifetime parameters for our IPSec security association.
#
set security ipsec proposal ipsec-prop-vpn-c0b054a9-2 protocol esp
set security ipsec proposal ipsec-prop-vpn-c0b054a9-2 authentication-algorithm hmac-sha1-96
set security ipsec proposal ipsec-prop-vpn-c0b054a9-2 encryption-algorithm aes-128-cbc
set security ipsec proposal ipsec-prop-vpn-c0b054a9-2 lifetime-seconds 3600
# The IPSec policy incorporates the Diffie-Hellman group and the IPSec
# proposal.
#
set security ipsec policy ipsec-pol-vpn-c0b054a9-2 perfect-forward-secrecy keys group2
set security ipsec policy ipsec-pol-vpn-c0b054a9-2 proposals ipsec-prop-vpn-c0b054a9-2
# A security association is defined here. The IPSec Policy and IKE gateways
# are associated with a tunnel interface (st0.2).
# The tunnel interface ID is assumed; if other tunnels are defined on
# your router, you will need to specify a unique interface name 
# (for example, st0.10).
#
set security ipsec vpn vpn-c0b054a9-2 bind-interface st0.2
set security ipsec vpn vpn-c0b054a9-2 ike gateway gw-vpn-c0b054a9-2
set security ipsec vpn vpn-c0b054a9-2 ike ipsec-policy ipsec-pol-vpn-c0b054a9-2
set security ipsec vpn vpn-c0b054a9-2 df-bit clear 
# This option enables IPSec Dead Peer Detection, which causes periodic
# messages to be sent to ensure a Security Association remains operational.
#
set security ike gateway gw-vpn-c0b054a9-2 dead-peer-detection
# #3: Tunnel Interface Configuration
#
# The tunnel interface is configured with the internal IP address.
#
set interfaces st0.2 family inet address 169.254.32.50/30
set interfaces st0.2 family inet mtu 1436
set security zones security-zone trust interfaces st0.2
# The security zone protecting external interfaces of the router must be 
# configured to allow IKE traffic inbound.
#
set security zones security-zone untrust host-inbound-traffic system-services ike
# The security zone protecting internal interfaces (including the logical 
# tunnel interfaces) must be configured to allow BGP traffic inbound.
#
set security zones security-zone trust host-inbound-traffic protocols bgp
# This option causes the router to reduce the Maximum Segment Size of
# TCP packets to prevent packet fragmentation.
#
set security flow tcp-mss ipsec-vpn mss 1387
# --------------------------------------------------------------------------------
# #4: Static Route Configuration
#
# VPN monitoring is used in order to provide failover with multiple tunnels. If the primary tunnel fails, the redundant tunnel will automatically be used.
#
set security ipsec vpn vpn-c0b054a9-2 vpn-monitor source-interface st0.2 
set security ipsec vpn vpn-c0b054a9-2 vpn-monitor destination-ip 169.254.32.49
# Your Customer Gateway needs to set a static route for the prefix corresponding to your VPC on the tunnel.
# An example for a VPC with the prefix 10.0.0.0/16 is provided below
# set routing-options static route 10.0.0.0/16 next-hop st0.2
#
# Additional Notes and Questions
#  - Amazon Virtual Private Cloud Getting Started Guide: 
#       http://docs.amazonwebservices.com/AmazonVPC/latest/GettingStartedGuide
#  - Amazon Virtual Private Cloud Network Administrator Guide: 
#       http://docs.amazonwebservices.com/AmazonVPC/latest/NetworkAdminGuide
#  - XSL Version: 2009-07-15-1119716
================================================

File: Config.txt
================================================
set security ike proposal azure-proposal authentication-method pre-shared-keys
set security ike proposal azure-proposal authentication-algorithm sha1
set security ike proposal azure-proposal encryption-algorithm aes-256-cbc
set security ike proposal azure-proposal lifetime-seconds 28800
set security ike proposal azure-proposal dh-group group2
set security ike policy azure-policy mode main
set security ike policy azure-policy proposals azure-proposal
QC->set security ike policy azure-policy pre-shared-key ascii-text jovIDqrG21eKmkdRBr341H1dgoW0mCbu
set security ike gateway azure-gateway ike-policy azure-policy
QC->set security ike gateway azure-gateway address 40.X.X.X -> 13.70.91.29
set security ike gateway azure-gateway external-interface fe-0/0/0.0
QC->set security ike gateway azure-gateway version v2-only
set security ipsec proposal azure-ipsec-proposal protocol esp
set security ipsec proposal azure-ipsec-proposal authentication-algorithm hmac-sha1-96
set security ipsec proposal azure-ipsec-proposal encryption-algorithm aes-256-cbc
set security ipsec proposal azure-ipsec-proposal lifetime-seconds 3600
set security ipsec policy azure-vpn-policy proposals azure-ipsec-proposal
set security ipsec vpn azure-ipsec-vpn ike gateway azure-gateway
set security ipsec vpn azure-ipsec-vpn ike ipsec-policy azure-vpn-policy
QC->set security zones security-zone Internal interfaces vlan.1 -> fe-0/0/1.0 
set security zones security-zone Internal host-inbound-traffic system-services ike
set security zones security-zone Internal address-book address onprem-networks-1 192.168.1.0/24
set security zones security-zone Internet interfaces fe-0/0/0.0
set security zones security-zone Internet host-inbound-traffic system-services ike
QC->set security zones security-zone Internet address-book address azure-networks-1 10.0.0.0/16 -> 10.0.0.0/21
set security policies from-zone Internal to-zone Internet policy azure-security-Internal-to-Internet-0 match source-address onprem-networks-1
set security policies from-zone Internal to-zone Internet policy azure-security-Internal-to-Internet-0 match destination-address azure-networks-1
set security policies from-zone Internal to-zone Internet policy azure-security-Internal-to-Internet-0 match application any
set security policies from-zone Internal to-zone Internet policy azure-security-Internal-to-Internet-0 then permit
set security policies from-zone Internet to-zone Internal policy azure-security-Internet-to-Internal-0 match source-address azure-networks-1
set security policies from-zone Internet to-zone Internal policy azure-security-Internet-to-Internal-0 match destination-address onprem-networks-1
set security policies from-zone Internet to-zone Internal policy azure-security-Internet-to-Internal-0 match application any
set security policies from-zone Internet to-zone Internal policy azure-security-Internet-to-Internal-0 then permit
set interfaces st0 unit 0 family inet
set security zones security-zone Internet interfaces st0.0
set security ipsec vpn azure-ipsec-vpn bind-interface st0.0
QC->set routing-options static route 10.0.0.0/16 -> 10.0.0.0/21 next-hop st0.0
set security flow tcp-mss ipsec-vpn mss 1350
================================================

File: VpnDeviceScript.txt
================================================
set security ike proposal azure-proposal authentication-method pre-shared-keys
set security ike proposal azure-proposal authentication-algorithm sha1
set security ike proposal azure-proposal encryption-algorithm aes-256-cbc
set security ike proposal azure-proposal lifetime-seconds 28800
set security ike proposal azure-proposal dh-group group2
set security ike policy azure-policy mode main
set security ike policy azure-policy proposals azure-proposal
set security ike policy azure-policy pre-shared-key ascii-text jovIDqrG21eKmkdRBr341H1dgoW0mCbu
set security ike gateway azure-gateway ike-policy azure-policy
set security ike gateway azure-gateway address 13.70.91.29
set security ike gateway azure-gateway external-interface <NameOfYourOutsideInterface>
set security ipsec proposal azure-ipsec-proposal protocol esp
set security ipsec proposal azure-ipsec-proposal authentication-algorithm  hmac-sha1-96
set security ipsec proposal azure-ipsec-proposal encryption-algorithm aes-256-cbc
set security ipsec proposal azure-ipsec-proposal lifetime-seconds 3600
set security ipsec policy azure-vpn-policy proposals azure-ipsec-proposal
set security ipsec vpn azure-ipsec-vpn ike gateway azure-gateway
set security ipsec vpn azure-ipsec-vpn ike ipsec-policy azure-vpn-policy
set security zones security-zone trust interfaces <NameOfYourInsideInterface>
set security zones security-zone trust host-inbound-traffic system-services ike
set security zones security-zone trust address-book address onprem-networks-1 192.168.1.0/24
set security zones security-zone untrust interfaces <NameOfYourOutsideInterface>
set security zones security-zone untrust host-inbound-traffic system-services ike
set security zones security-zone untrust address-book address azure-networks-1 10.0.0.0/21
set security policies from-zone trust to-zone untrust policy azure-security-trust-to-untrust-0 match source-address onprem-networks-1
set security policies from-zone trust to-zone untrust policy azure-security-trust-to-untrust-0 match destination-address azure-networks-1
set security policies from-zone trust to-zone untrust policy azure-security-trust-to-untrust-0 match application any
set security policies from-zone trust to-zone untrust policy azure-security-trust-to-untrust-0 then permit tunnel ipsec-vpn azure-ipsec-vpn
set security policies from-zone trust to-zone untrust policy azure-security-trust-to-untrust-0 then permit tunnel pair-policy azure-security-untrust-to-trust-0
set security policies from-zone untrust to-zone trust policy azure-security-untrust-to-trust-0 match source-address azure-networks-1
set security policies from-zone untrust to-zone trust policy azure-security-untrust-to-trust-0 match destination-address onprem-networks-1
set security policies from-zone untrust to-zone trust policy azure-security-untrust-to-trust-0 match application any
set security policies from-zone untrust to-zone trust policy azure-security-untrust-to-trust-0 then permit tunnel ipsec-vpn azure-ipsec-vpn
set security policies from-zone untrust to-zone trust policy azure-security-untrust-to-trust-0 then permit tunnel pair-policy azure-security-trust-to-untrust-0
insert security policies from-zone trust to-zone untrust policy azure-security-trust-to-untrust-0 before policy 
set security flow tcp-mss ipsec-vpn mss 1350
================================================

File: Windows Firewall Rule.txt
================================================
Import-Module NetSecurity
New-NetFirewallRule -Name Allow_ICMP -DisplayName “Allow ICMPv4” -Protocol ICMPv4 -IcmpType 8 -Enabled True -Profile Any -Action Allow
|-----------------------------------------------------|
netsh advfirewall firewall add rule name="Allow ICMPv4" dir=in action=allow protocol=icmpv4
================================================

File: Routing Instance Config.txt
================================================
Routing Instance
!-----------------------!
set interfaces ge-0/0/1 unit 0 family inet address 172.16.0.1/24
set routing-instances RI instance-type virtual-router
set routing-instances RI interface ge-0/0/1.0
set routing-instances RI interface pp0.1
set routing-instances RI routing-options static route 0.0.0.0/0 next-hop pp0.1
set routing-instances RI system services dhcp-local-server group DHCP_POOL interface ge-0/0/1.0
set routing-instances RI access address-assignment pool DHCP_POOL family inet network 172.16.0.0/24
set routing-instances RI access address-assignment pool DHCP_POOL family inet range DHCP_RANGE low 172.16.0.10
set routing-instances RI access address-assignment pool DHCP_POOL family inet range DHCP_RANGE high 172.16.0.250
set routing-instances RI access address-assignment pool DHCP_POOL family inet dhcp-attributes maximum-lease-time 86400
set routing-instances RI access address-assignment pool DHCP_POOL family inet dhcp-attributes domain-name lab.local
set routing-instances RI access address-assignment pool DHCP_POOL family inet dhcp-attributes name-server 172.16.0.1
set routing-instances RI access address-assignment pool DHCP_POOL family inet dhcp-attributes router 172.16.0.1
Security & Firewall
!-----------------------!
edit security zones security-zone RI_UNTRUST
 set interfaces pp0.1 host-inbound-traffic system-services ping
edit security zones security-zone RI_TRUST
 set interfaces ge-0/0/1.0 host-inbound-traffic system-services all 
 set interfaces ge-0/0/1.0 host-inbound-traffic protocols all 
edit security policies from-zone RI_TRUST to-zone RI_UNTRUST 
 set policy 1 match source-address any
 set policy 1 match destination-address any
 set policy 1 match application any
 set policy 1 then permit
NAT
!-----------------------!
set security nat source rule-set RI_PAT from zone RI_TRUST
set security nat source rule-set RI_PAT to zone RI_UNTRUST
set security nat source rule-set RI_PAT rule 1 match source-address 0.0.0.0/0
set security nat source rule-set RI_PAT rule 1 then source-nat interface
================================================

File: Config.txt
================================================
Root setup (Pa$$w0rd)
==================================================
set system root-authentication encrypted-password "$1$pW.aob99$3CWqRk6.eOy5sRjnNqymk0"
Interfaces & Connectivity
==================================================
delete security zones security-zone untrust interfaces ge-0/0/0.0
edit security zones security-zone trust 
set interfaces ge-0/0/0.0 host-inbound-traffic system-services https
set interfaces ge-0/0/0.0 host-inbound-traffic system-services ssh
top
set interfaces ge-0/0/0.0 family inet address 10.0.0.1/24
Basic Configuration
==================================================
edit system services web-management
 delete
 set https system-generated-certificate port 443 interface ge-0/0/0.0
Help
==================================================
help apropos
help topic
Commit and Rollback
==================================================
commit check
commit confirmed
commit comment CHANGE_MADE
show | compare rollback 0
show | compare rollback 1
show system commit
show system rollback 0 compare 1
Output Filtering
==================================================
show | display set
show | match 
show | find 
show | save
================================================

File: Destination NAT Config.txt
================================================
Interfaces
!-----------------------!
set interfaces ge-0/0/1.0 family inet address 10.0.0.1/24
set interfaces ge-0/0/0.0 family inet address 1.0.0.1/30
Define Applications
!-----------------------!
set applications application RDP_TCP protocol tcp
set applications application RDP_TCP destination-port 3389
set applications application RDP_UDP protocol udp
set applications application RDP_UDP destination-port 3389
set security nat proxy-arp interface ge-0/0/0.0 address 1.0.0.10
1:1 Destination NAT
!-----------------------!
set security nat destination pool SERVER1_3389 address 10.0.0.100/32
set security nat destination pool SERVER1_3389 address port 3389
set security nat destination rule-set DNAT rule 1 match destination-address 1.0.0.10/32
set security nat destination rule-set DNAT rule 1 match destination-port 33890
set security nat destination rule-set DNAT rule 1 then destination-nat pool 100_3389
Security & Firewall
!-----------------------!
edit security zones
 set security-zone trust interfaces ge-0/0/1.0
 set security-zone trust host-inbound system-services all
 set security-zone trust host-inbound protocols all
 set security-zone trust address-book address SERVER1 10.0.0.100/32
 set security-zone untrust interfaces ge-0/0/0.0
 set security-zone untrust host-inbound system-services ping
edit security policies from-zone untrust to-zone trust
 set policy RDP_POLICY match source-address any
 set policy RDP_POLICY match destination-address SERVER1
 set policy RDP_POLICY match application RDP_TCP
 set policy RDP_POLICY match application RDP_UDP
 set policy RDP_POLICY then permit
================================================

File: DHCP Config.txt
================================================
Interfaces
!-----------------------!
set interfaces ge-0/0/1.0 family inet address 10.0.0.1/24
set interfaces ge-0/0/0.0 family inet address 1.0.0.1/30
DHCP
!-----------------------!
set system services dhcp-local-server group DHCP_POOL interface ge-0/0/1.0
set access address-assignment pool DHCP_POOL family inet network 10.0.0.0/24
set access address-assignment pool DHCP_POOL family inet range DHCP_RANGE low 10.0.0.10
set access address-assignment pool DHCP_POOL family inet range DHCP_RANGE high 10.0.0.250
set access address-assignment pool DHCP_POOL family inet dhcp-attributes maximum-lease-time 86400
set access address-assignment pool DHCP_POOL family inet dhcp-attributes domain-name lab.local
set access address-assignment pool DHCP_POOL family inet dhcp-attributes name-server 10.0.0.1
set access address-assignment pool DHCP_POOL family inet dhcp-attributes router 10.0.0.1
Security & Firewall
!-----------------------!
edit security zones
 set security-zone trust interfaces ge-0/0/1.0
 set security-zone trust host-inbound system-services all
 set security-zone trust host-inbound protocols all
 set security-zone untrust interfaces ge-0/0/0.0
 set security-zone untrust host-inbound system-services ping
================================================

File: Config.txt
================================================
Factory Default Configuration with Root
==================================================
load factory default
set system root-authentication plain-text-password
Factory Default Configuration without Root
==================================================
request system zeroize
Root Password Recovery
==================================================
boot -s 
recovery 
Configuration Management
==================================================
save /root/file1.conf
save /var/home/user/configurations/file2.conf
load override
================================================

File: Config.txt
================================================
Basic SRX Config
==================================================
set system services telnet
set interfaces ge-0/0/0 unit 0 family inet address 2.0.0.1/24
set interfaces ge-0/0/1 unit 0 family inet address 10.0.0.1/24
set routing-options static route 0.0.0.0/0 next-hop 2.0.0.2
Default Zone Assignment
==================================================
edit security zones security-zone untrust interfaces ge-0/0/0.0
 delete
 set host-inbound-traffic system-services ping
edit security zones security-zone trust
 set host-inbound-traffic system-services telnet
 set host-inbound-traffic system-services ssh
 set host-inbound-traffic system-services https
 set host-inbound-traffic system-services ping
 set interface ge-0/0/1
Enable HTTPS Management
==================================================
edit system services web-management 
 set https interface ge-0/0/0 system-generated-certificate
================================================

File: Windows, Linux & VPCS.txt
================================================
Windows IPv4 Network Adapter
==================================================
Remove-NetIPAddress -InterfaceAlias Loopback
New-NetIPAddress -InterfaceAlias Loopback –IPAddress 2.0.0.2 -PrefixLength 24
netsh interface ip set address "Loopback" static 2.0.0.2 255.255.255.0
Windows IPv4 Route
==================================================
route add 10.0.0.0 mask 255.255.255.0 2.0.0.1
Linux IPv4 Config & Route
==================================================
ifconfig eth0 10.0.0.10/24
route add -net 0.0.0.0 netmask 0.0.0.0 gw 10.0.0.1
VPCS IPv4 Config & Route
==================================================
ip 10.0.0.10/24 10.0.0.1 
================================================

File: IRB Config.txt
================================================
Global Mode
!-----------------------!
set protocols l2-learning global-mode switching
request system reboot
VLANs
!-----------------------!
set vlans VLAN10 vlan-id 10
set vlans VLAN10 l3-interface irb.10
delete interfaces ge-0/0/1.0
delete interfaces ge-0/0/2.0
delete interfaces ge-0/0/3.0
set interfaces ge-0/0/1.0 family ethernet-switching vlan members VLAN10
set interfaces ge-0/0/1.0 family ethernet-switching interface-mode access
set interfaces ge-0/0/2.0 family ethernet-switching vlan members VLAN10
set interfaces ge-0/0/2.0 family ethernet-switching interface-mode access
set interfaces ge-0/0/3.0 family ethernet-switching vlan members VLAN10
set interfaces ge-0/0/3.0 family ethernet-switching interface-mode access
IRB & WAN Interface
!-----------------------!
set interfaces ge-0/0/0.0 family inet address 1.0.0.1/30
set interface irb.10 family inet address 10.0.10.1/24
Security & Firewall
!-----------------------!
edit security zones
 set security-zone trust interfaces irb.10
 set security-zone trust host-inbound system-services all
 set security-zone trust host-inbound protocols all
 set security-zone untrust interfaces ge-0/0/0.0
 set security-zone untrust host-inbound system-services ping
Source NAT (PAT)
!-----------------------! 
set security nat source rule-set PAT from zone trust
set security nat source rule-set PAT to zone untrust
set security nat source rule-set PAT rule 1 match source-address 0.0.0.0/0
set security nat source rule-set PAT rule 1 then source-nat interface
Verify
!-----------------------!
================================================

File: Old vs New Config.txt
================================================
Old
!-----------------------!
set vlans VLAN10 vlan-id 10
set vlans VLAN10 l3-interface vlan.10
set interfaces ge-0/0/1.0 family ethernet-switching vlan members VLAN10
set interfaces ge-0/0/1.0 family ethernet-switching port-mode access
set interfaces ge-0/0/2.0 family ethernet-switching vlan members VLAN10
set interfaces ge-0/0/2.0 family ethernet-switching port-mode access
set interfaces ge-0/0/3.0 family ethernet-switching vlan members VLAN10
set interfaces ge-0/0/3.0 family ethernet-switching port-mode access
New
!-----------------------!
set protocols l2-learning global-mode switching
request system reboot
set vlans VLAN10 vlan-id 10
set vlans VLAN10 l3-interface irb.10
set interfaces ge-0/0/1.0 family ethernet-switching vlan members VLAN10
set interfaces ge-0/0/1.0 family ethernet-switching interface-mode access
set interfaces ge-0/0/2.0 family ethernet-switching vlan members VLAN10
set interfaces ge-0/0/2.0 family ethernet-switching interface-mode access
set interfaces ge-0/0/3.0 family ethernet-switching vlan members VLAN10
set interfaces ge-0/0/3.0 family ethernet-switching interface-mode access
================================================

File: Config.txt
================================================
LACP Link Aggregation
==================================================
set chassis aggregated-devices ethernet device-count 1
edit interfaces
 delete fe-0/0/1 unit 0
 delete fe-0/0/2 unit 0
 set fe-0/0/1 fastether-options 802.3ad ae0
 set fe-0/0/2 fastether-options 802.3ad ae0
 set ae0 unit 0 family inet address 10.0.12.2/30
 set ae0 aggregated-ether-options lacp active
edit security zones security-zone trust
 delete interfaces fe-0/0/1.0
 delete interfaces fe-0/0/2.0
 set interfaces ae0.0
================================================

File: Loopback Filter Config.txt
================================================
Interfaces
!-----------------------!
set interfaces ge-0/0/1.0 family inet address 10.0.0.1/24
set interfaces ge-0/0/0.0 family inet address 1.0.0.1/30
Management Filter #1
!-----------------------!
set policy-options prefix-list TRUSTED 10.0.0.0/24
edit firewall family inet filter MGMT
 set term DENY_TCP from source-address 0.0.0.0/0
 set term DENY_TCP from source-prefix-list TRUSTED except
 set term DENY_TCP from protocol tcp
 set term DENY_TCP from destination-port ssh
 set term DENY_TCP from destination-port https
 set term DENY_TCP then log
 set term DENY_TCP then discard
 set term DENY_UDP from source-address 0.0.0.0/0
 set term DENY_UDP from source-prefix-list TRUSTED except
 set term DENY_UDP from protocol udp
 set term DENY_UDP from destination-port snmp
 set term DENY_UDP then discard
 set term PERMIT_OTHER then accept
set interfaces lo0.0 family inet address 127.0.0.1/32
set interfaces lo0.0 family inet filter input MGMT
Security & Firewall
!-----------------------!
edit security zones
 set security-zone trust interfaces ge-0/0/1.0
 set security-zone trust host-inbound system-services all
 set security-zone trust host-inbound protocols all
 set security-zone untrust interfaces ge-0/0/0.0
 set security-zone untrust host-inbound system-services ping
Verify 
!-----------------------!
show firewall log
show firewall filter MGMT
================================================

File: Config.txt
================================================
Manual Time and Date
==================================================
set date 201605201900.00
Format = YYYYMMDDhhmm.ss
set date ntp 0.au.pool.ntp.org
NTP & Timezones
==================================================
set system ntp server 0.au.pool.ntp.org
set system ntp server 1.au.pool.ntp.org
set system ntp server 2.au.pool.ntp.org
set system ntp server 3.au.pool.ntp.org
set system time-zone GMT+10
set system time-zone Australia/Sydney
show system uptime
show ntp associations no-resolve
show ntp status
================================================

File: PPPoE Client Config.txt
================================================
PPPoE
!-----------------------!
delete interfaces ge-0/0/0.0
set interfaces ge-0/0/0.0 encapsulation ppp-over-ether
edit interfaces pp0.0
 set pppoe-options underlying-interface ge-0/0/0.0
 set pppoe-options idle-timeout 0
 set pppoe-options auto-reconnect 10
 set pppoe-options client
 set pppoe-options access-concentrator SRX1
 set family inet negotiate-address
 set family inet mtu 1492
PPPoE Authentication
!-----------------------!
edit interfaces pp0.0 
 set ppp-options pap local-name SRX2
 set ppp-options pap local-password Pa$$w0rd
 set ppp-options pap passive
 set ppp-options chap default-chap-secret Pa$$w0rd
 set ppp-options chap local-name SRX2
 set ppp-options chap passive
Routing & Security
!-----------------------!
edit security zones security-zone untrust 
 set host-inbound-traffic system-services ping 
 set interfaces pp0.0
set routing-options static route 0.0.0.0/0 next-hop pp0.0
Debug & Verify
!-----------------------!
set protocols ppp traceoptions file ppp
set protocols ppp traceoptions level all
set protocols ppp traceoptions flag all
set protocols pppoe traceoptions file pppoe
set protocols pppoe traceoptions level all
set protocols pppoe traceoptions flag all
show log pppoe
show log ppp
show ppp interface pp0 extensive
show pppoe statistics
show pppoe interfaces brief
show pppoe interfaces 
clear pppoe sessions 
clear pppoe statistics
================================================

File: PPPoE Server Config.txt
================================================
PPPoE
!-----------------------!
delete interfaces ge-0/0/0.0
set interfaces ge-0/0/0.0 encapsulation ppp-over-ether
edit interfaces pp0.0
 set pppoe-options underlying-interface ge-0/0/0.0
 set pppoe-options server
 set family inet mtu 1492
 set family inet address 1.0.0.10/32 destination 1.0.0.1
PPPoE Authentication
!-----------------------!
edit interfaces pp0.0
 set ppp-options pap local-name SRX2
 set ppp-options pap default-password Pa$$w0rd
 set ppp-options chap default-chap-secret Pa$$w0rd
 set ppp-options chap local-name SRX2
Routing & Security
!-----------------------!
edit security zones security-zone trust 
 set host-inbound-traffic system-services ping
 set interfaces pp0.0 
Debug & Verify
!-----------------------!
set protocols ppp traceoptions file ppp
set protocols ppp traceoptions level all
set protocols ppp traceoptions flag all
set protocols pppoe traceoptions file pppoe
set protocols pppoe traceoptions level all
set protocols pppoe traceoptions flag all
show log pppoe
show log ppp
show ppp interface pp0 extensive
show pppoe statistics
show pppoe interfaces brief
show pppoe interfaces 
clear pppoe sessions 
clear pppoe statistics
================================================

File: Policy-Based VPN Config.txt
================================================
Interfaces & Routing
!-----------------------!
set interfaces ge-0/0/0 unit 0 family inet address 1.0.0.1/24
set interfaces ge-0/0/1 unit 0 family inet address 172.16.0.1/24
set interfaces st0.0 family inet 
set routing-options static route 10.0.0.0/24 next-hop st0.0
set routing-options static route 0.0.0.0/0 next-hop 1.0.0.10
Policy-Based VPN
!-----------------------!
edit security 
 set ike proposal IKE authentication-method pre-shared-keys
 set ike proposal IKE dh-group group14
 set ike proposal IKE authentication-algorithm sha-256
 set ike proposal IKE encryption-algorithm aes-256-cbc
 set ike proposal IKE lifetime-seconds 86400
 set ike policy IKE_POLICY mode main
 set ike policy IKE_POLICY proposals IKE
 set ike policy IKE_POLICY pre-shared-key ascii-text Pa$$w0rd
 set ike gateway IKE_GATEWAY ike-policy IKE_POLICY
 set ike gateway IKE_GATEWAY address 2.0.0.1
 set ike gateway IKE_GATEWAY external-interface ge-0/0/0
 set ike gateway IKE_GATEWAY local-address 1.0.0.1 
 set ipsec proposal ESP protocol esp
 set ipsec proposal ESP authentication-algorithm hmac-md5-96
 set ipsec proposal ESP encryption-algorithm aes-128-cbc
 set ipsec proposal ESP lifetime-seconds 43200
 set ipsec policy ESP_POLICY proposals ESP
 set ipsec vpn ESP_VPN bind-interface st0.0 
 set ipsec vpn ESP_VPN ike gateway IKE_GATEWAY
 set ipsec vpn ESP_VPN ike ipsec-policy ESP_POLICY
 set ipsec vpn ESP_VPN establish-tunnels immediately
 set ipsec vpn ESP_VPN ike proxy-identity local 172.16.0.0/24
 set ipsec vpn ESP_VPN ike proxy-identity remote 10.0.0.0/24
 set ipsec vpn ESP_VPN ike proxy-identity service any
Security
!-----------------------!
edit security zones
 set security-zone trust interfaces ge-0/0/1.0
 set security-zone trust host-inbound system-services all
 set security-zone trust host-inbound protocols all
 set security-zone VPN interfaces st0.0
 set security-zone VPN host-inbound system-services all
 set security-zone VPN host-inbound protocols all
 set security-zone untrust interfaces ge-0/0/0.0
 set security-zone untrust host-inbound system-services ping
 set security-zone untrust host-inbound system-services ike
 set security-zone untrust host-inbound protocols esp
edit security policies from-zone trust to-zone VPN 
 set policy TRUST_TO_VPN match source-address any
 set policy TRUST_TO_VPN match destination-address any
 set policy TRUST_TO_VPN match application any
 set policy TRUST_TO_VPN then permit
edit security policies from-zone VPN to-zone trust
 set policy VPN_TO_TRUST match source-address any
 set policy VPN_TO_TRUST match destination-address any
 set policy VPN_TO_TRUST match application any
 set policy VPN_TO_TRUST then permit 
Verify
!-----------------------!
show security ike security-associations
show security ike security-associations detail
show security ipsec sa
show security ipsec sa detail
show security ipsec statistics
================================================

File: Route-Based VPN Config.txt
================================================
Interfaces & Routing
!-----------------------!
set interfaces ge-0/0/0 unit 0 family inet address 1.0.0.1/24
set interfaces ge-0/0/1 unit 0 family inet address 172.16.0.1/24
set interfaces st0.0 family inet address 12.0.0.1/30
set interfaces st0.0 family inet mtu 1400
set routing-options static route 10.0.0.0/24 next-hop 12.0.0.2
set routing-options static route 0.0.0.0/0 next-hop 1.0.0.10
Route-Based VPN
!-----------------------!
edit security 
 set ike proposal IKE authentication-method pre-shared-keys
 set ike proposal IKE dh-group group14
 set ike proposal IKE authentication-algorithm sha-256
 set ike proposal IKE encryption-algorithm aes-256-cbc
 set ike proposal IKE lifetime-seconds 86400
 set ike policy IKE_POLICY mode main
 set ike policy IKE_POLICY proposals IKE
 set ike policy IKE_POLICY pre-shared-key ascii-text Pa$$w0rd
 set ike gateway IKE_GATEWAY ike-policy IKE_POLICY
 set ike gateway IKE_GATEWAY address 2.0.0.1
 set ike gateway IKE_GATEWAY external-interface ge-0/0/0
 set ike gateway IKE_GATEWAY local-address 1.0.0.1 
 set ipsec proposal ESP protocol esp
 set ipsec proposal ESP authentication-algorithm hmac-md5-96
 set ipsec proposal ESP encryption-algorithm aes-128-cbc
 set ipsec proposal ESP lifetime-seconds 43200
 set ipsec policy ESP_POLICY proposals ESP
 set ipsec vpn ESP_VPN bind-interface st0.0 
 set ipsec vpn ESP_VPN ike gateway IKE_GATEWAY
 set ipsec vpn ESP_VPN ike ipsec-policy ESP_POLICY
 set ipsec vpn ESP_VPN establish-tunnels immediately
Security
!-----------------------!
edit security zones
 set security-zone trust interfaces ge-0/0/1.0
 set security-zone trust host-inbound system-services all
 set security-zone trust host-inbound protocols all
 set security-zone VPN interfaces st0.0
 set security-zone VPN host-inbound system-services all
 set security-zone VPN host-inbound protocols all
 set security-zone untrust interfaces ge-0/0/0.0
 set security-zone untrust host-inbound system-services ping
 set security-zone untrust host-inbound system-services ike
 set security-zone untrust host-inbound protocols esp
edit security policies from-zone trust to-zone VPN 
 set policy TRUST_TO_VPN match source-address any
 set policy TRUST_TO_VPN match destination-address any
 set policy TRUST_TO_VPN match application any
 set policy TRUST_TO_VPN then permit
edit security policies from-zone VPN to-zone trust
 set policy VPN_TO_TRUST match source-address any
 set policy VPN_TO_TRUST match destination-address any
 set policy VPN_TO_TRUST match application any
 set policy VPN_TO_TRUST then permit 
Verify
!-----------------------!
show security ike security-associations
show security ike security-associations detail
show security ipsec sa
show security ipsec sa detail
show security ipsec statistics
================================================

File: Source NAT Config.txt
================================================
Interfaces
!-----------------------!
set interfaces ge-0/0/1.0 family inet address 10.0.0.1/24
set interfaces ge-0/0/0.0 family inet address 1.0.0.1/30
Security & Firewall
!-----------------------!
edit security zones
 set security-zone trust interfaces ge-0/0/1.0
 set security-zone trust host-inbound system-services all
 set security-zone trust host-inbound protocols all
 set security-zone untrust interfaces ge-0/0/0.0
 set security-zone untrust host-inbound system-services ping
Source NAT (PAT)
!-----------------------! 
set security nat source rule-set PAT from zone trust
set security nat source rule-set PAT to zone untrust
set security nat source rule-set PAT rule 1 match source-address 0.0.0.0/0
set security nat source rule-set PAT rule 1 then source-nat interface
================================================

File: Config.txt
================================================
Syslog
==================================================
set system syslog user * any emergency
set system syslog file messages any any
set system syslog file messages authorization info
set system syslog file interactive-commands interactive-commands any
file show /var/log/messages | last | no-more
show log messages | last | no-more
file show /var/log/interactive-commands | last | no-more
show log messages | last | no-more
Custom File Logging
==================================================
set system syslog file AUTH authorization any
set system syslog file COMMANDS explicit-priority interactive-commands any
Console Logging (Does not mean Terminal)
==================================================
set system syslog console any any
set system syslog console any info
User Logging (Terminal)
==================================================
set system syslog user root any any 
set system syslog user * any info
Log to Syslog Server
==================================================
set system syslog host 2.0.0.2 any any
================================================

File: Config.txt
================================================
Root setup (Pa$$w0rd)
==================================================
set system root-authentication encrypted-password "$1$pW.aob99$3CWqRk6.eOy5sRjnNqymk0"
Interfaces & Connectivity
==================================================
delete security zones security-zone untrust interfaces ge-0/0/0.0
edit security zones security-zone trust 
set interfaces ge-0/0/0.0 host-inbound-traffic system-services https
set interfaces ge-0/0/0.0 host-inbound-traffic system-services ssh
top
set interfaces ge-0/0/0.0 family inet address 10.0.0.1/24
User Accounts
==================================================
edit system login
 set user bpin class super-user authentication encrypted-password "$1$pW.aob99$3CWqRk6.eOy5sRjnNqymk0"
 set user op class operator authentication encrypted-password "$1$pW.aob99$3CWqRk6.eOy5sRjnNqymk0"
 set user ro class read-only authentication encrypted-password "$1$pW.aob99$3CWqRk6.eOy5sRjnNqymk0"
Device Hardening
==================================================
edit system services web-management
 delete
 set https system-generated-certificate port 443 interface ge-0/0/0.0
edit system services ssh
 set root-login deny
 set protocol-version v2
 set connection-limit 3
 set rate-limit 3
 set max-sessions-per-connection 3
show log messages | match login
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2019 Mustafa Asaad [rootx]
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: DHCP Config.txt
================================================
/interface bridge
add name=BR-LAN
/interface bridge port
add bridge=BR-LAN interface=wlan0
/ip address
add address=192.168.1.1/24 interface=BR-LAN network=192.168.1.0
/ip pool
add name=dhcp_pool0 ranges=192.168.1.2-192.168.1.254
/ip dhcp-server network
add address=192.168.1.0/24 dns-server=192.168.1.1,1.1.1.1,8.8.8.8 gateway=\
    192.168.1.1
/ip dhcp-server
add address-pool=dhcp_pool0 disabled=no interface=BR-LAN name=dhcp1
================================================

File: README.md
================================================
# QuickConfigs
[![MIT license](https://img.shields.io/badge/LICENSE-MIT-blue)](https://opensource.org/licenses/MIT)
================================================

File: Configuration.txt
================================================
Add Wheezy Repository
!-------------------!
set system package repository wheezy components 'main contrib non-free'
set system package repository wheezy distribution wheezy 
set system package repository wheezy url http://http.us.debian.org/debian
#Update Sources
sudo apt-get update
#See installed packages
sudo dkpg -l
================================================

File: Config.txt
================================================
Firewall Zones
==================================================
edit zone-policy
 set zone WAN default-action drop
 set zone WAN from LAN firewall name LAN_TO_WAN
 set zone WAN from LOCAL firewall name LOCAL_TO_ALL
 set zone WAN interface eth0
 set zone LAN default-action drop
 set zone LAN from WAN firewall name WAN_TO_LAN
 set zone LAN from LOCAL firewall name LOCAL_TO_ALL
 set zone LAN interface eth1
 set zone LOCAL default-action drop
 set zone LOCAL from WAN firewall name WAN_TO_LOCAL
 set zone LOCAL from LAN firewall name LAN_TO_LOCAL
 set zone LOCAL local-zone
Firewall Rules
==================================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable 
edit firewall name WAN_TO_LOCAL
 set default-action drop
 set rule 1 action accept
 set rule 1 description NTP
 set rule 1 log disable
 set rule 1 state established enable
 set rule 1 state related enable 
 set rule 1 protocol udp
 set rule 1 source port 123
 set rule 2 source address 2.0.0.2
 set rule 2 action accept
 set rule 2 description DNS
 set rule 2 log disable
 set rule 2 state established enable
 set rule 2 state related enable 
 set rule 2 protocol tcp_udp
 set rule 2 source port 53
 set rule 2 source address 8.8.8.8
 set rule 3 action accept
 set rule 3 description DHCP
 set rule 3 log disable
 set rule 3 state established enable
 set rule 3 state related enable 
 set rule 3 protocol udp
 set rule 3 source port 67-68
 set rule 3 source address 2.0.0.2
 set rule 4 action accept
 set rule 4 description SSH
 set rule 4 destination port 9222
 set rule 4 log disable
 set rule 4 protocol tcp
 set rule 4 source address 100.0.0.1 
 set rule 5 action accept
 set rule 5 description HTTPS
 set rule 5 destination port 9443
 set rule 5 log disable
 set rule 5 protocol tcp
 set rule 5 source address 100.0.0.1 
 set rule 6 action accept
 set rule 6 description ICMP
 set rule 6 log disable
 set rule 6 protocol icmp
 set rule 6 state established enable
 set rule 6 state related enable 
edit firewall name LAN_TO_LOCAL
 set default-action accept
 set rule 1 action accept
 set rule 1 description SSH
 set rule 1 log disable
 set rule 1 protocol tcp
 set rule 1 destination port 9222
 set rule 1 source address 10.0.0.10
 set rule 2 action accept
 set rule 2 description HTTPS
 set rule 2 log disable
 set rule 2 protocol tcp
 set rule 2 destination port 9443 
 set rule 2 source address 10.0.0.10
 set rule 3 action drop
 set rule 3 description SSH
 set rule 3 log disable
 set rule 3 protocol tcp
 set rule 3 destination port 9222
 set rule 4 action drop
 set rule 4 description HTTPS
 set rule 4 log disable
 set rule 4 protocol tcp
 set rule 4 destination port 9443
set firewall name LAN_TO_WAN default-action accept
set firewall name LOCAL_TO_ALL default-action accept
Change Default Management Ports
==================================================
edit service
 set gui https-port 9443
 set ssh port 9222
Misc Options
==================================================
set service dns forwarding dhcp eth0
set service dns forwarding listen-on eth1
set system ntp server 2.0.0.2
================================================

File: Config.txt
================================================
Restore to Factory Defaults
==================================================
cp /opt/vyatta/etc/config.boot.default /config/config.boot
Configurations & Saving
==================================================
save
load config.boot
save alternateconfig.boot
load alternateconfig.boot
sudo -i
ls -l /config/
cat /config/config.boot
vi /config/config.boot
cat /config/alternateconfig.boot
vi /config/alternateconfig.boot
Edit Factory Default Configuration
==================================================
sudo -i
vi /opt/vyatta/etc/config.boot.default
================================================

File: Config.txt
================================================
Archival & Managing Commit
==================================================
edit system config-management 
 set commit-archive location tftp://192.168.1.99/
 set commit-revisions 5
set service telnet
commit comment ADDED_TELNET
commit confirm 5
Saving and Loading Running Configuration
==================================================
save
save tftp://192.168.1.99/config.txt 
load tftp://192.168.1.99/config.txt 
TFTP backup
==================================================
copy file running://config/config.boot to tftp://192.168.1.99/startup-config.txt
Viewing Commit Files
==================================================
show system commit
show system commit file 0 
show configuration
show system commit diff 0
Delete Commit History 
==================================================
delete file running://config/archive/config.boot.0.gz
Command History
==================================================
show history  
show history brief 
Using the Linux Shell
==================================================
sudo -i
ls -l /config/
ls -l /config/archive
cat /config/config.boot
================================================

File: Config.txt
================================================
Pre-Login Banner
==================================================
set system login banner pre-login "**********************************************************************\n\n\tThis system is for the use of authorized clients only.\n\tIndividuals using the computer network system without\n\tany authorization, or in excess of their authorization,\n\tare subject to having all their activity monitored and\n\trecorded by system personnel. To protect the environment\n\tfrom unauthorized use and to ensure the computer system\n\tis functioning properly, system technicians continously\n\tmonitor the network environment for unauthorized usage.\n\n\tUnauthorized access is a violation of criminal, civil,\n\tstate and federal laws.\n\n**********************************************************************\n\n"
Post-Login Banner
==================================================
set system login banner post-login "You are logged on to Edgerouter-X 5-Port with version v1.9.0\n"
================================================

File: Config.txt
================================================
HTTPS & SSH Rules
==========================================
edit firewall name MGMT
 set default-action drop
 set description 'Limit Management Access'
 set rule 1 action accept
 set rule 1 description SSH
 set rule 1 destination port 22
 set rule 1 log enable
 set rule 1 protocol tcp
 set rule 1 source address 10.0.0.11
 set rule 2 action accept
 set rule 2 description HTTPS
 set rule 2 destination port 443
 set rule 2 log enable
 set rule 2 protocol tcp
 set rule 2 source address 10.0.0.10
Apply to Interface
==========================================
edit interfaces ethernet eth1
 set description LAN
 set address 10.0.0.1/24
 set firewall local name MGMT
================================================

File: Config.txt
================================================
HTTPS & SSH Rules
==================================================
edit firewall name MGMT
 set default-action drop
 set description 'Limit Management Access'
 set rule 1 action accept
 set rule 1 description SSH
 set rule 1 destination port 22
 set rule 1 log enable
 set rule 1 protocol tcp
 set rule 1 source address 10.0.0.10
 set rule 2 action accept
 set rule 2 description HTTPS
 set rule 2 destination port 443
 set rule 2 log enable
 set rule 2 protocol tcp
 set rule 2 source address 10.0.0.11
Apply to Interface
==================================================
edit interfaces ethernet eth1
 set description LAN
 set address 10.0.0.1/24
 set firewall local name MGMT
================================================

File: Config.txt
================================================
Bonding interfaces
==================================================
edit interfaces bonding bond0
 set address 10.0.12.1/30
 set mode 802.3ad
set interfaces ethernet eth1 bond-group bond0
set interfaces ethernet eth2 bond-group bond0
show interfaces bonding  
show interfaces bonding brief
================================================

File: Config.txt
================================================
Bridge Interface
==================================================
edit interfaces
 set bridge br0 address 10.0.0.1/24
 set bridge br0 stp false
 set bridge br0 description BRIDGEDLAN
 set ethernet eth1 bridge-group bridge br0
 set ethernet eth1 description BRIDGEDLAN
 set ethernet eth2 bridge-group bridge br0
 set ethernet eth2 description BRIDGEDLAN
 set ethernet eth0 address 2.0.0.1/30
 set ethernet eth0 description WAN
DHCP Services
==================================================
edit service dhcp-server shared-network-name BRIDGEDLAN
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 dns-server 8.8.8.8
 set subnet 10.0.0.0/24 lease 28800
set service dns forwarding listen-on br0
set service dns forwarding name-server 8.8.8.8
================================================

File: Config.txt
================================================
Bridge Interface
==================================================
edit interfaces
 set bridge br0 address 10.0.0.1/24
 set bridge br0 stp false
 set bridge br0 description BRIDGEDLAN
 set ethernet eth1 bridge-group bridge br0
 set ethernet eth1 description BRIDGEDLAN
 set ethernet eth2 bridge-group bridge br0
 set ethernet eth2 description BRIDGEDLAN
 set ethernet eth0 address 2.0.0.1/30
 set ethernet eth0 description WAN
DHCP Services
==================================================
edit service dhcp-server shared-network-name BRIDGEDLAN
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 dns-server 8.8.8.8
 set subnet 10.0.0.0/24 lease 28800
set service dns forwarding listen-on br0
set service dns forwarding name-server 8.8.8.8
================================================

File: Configuration.txt
================================================
Basic WAN Limit Smart Queue QoS
|-----------------------------|
edit traffic-control smart-queue SHAPER
 set wan-interface eth0
 set upload rate 420kbit
 set download rate 5.2mbit
================================================

File: Configuration.txt
================================================
Traffic Analysis with DPI
|-----------------------|
set system traffic-analysis dpi enable
set system traffic-analysis export enable
Traffic Analysis without DPI
|--------------------------|
set system traffic-analysis dpi disable
set system traffic-analysis export enable
#Verify
show ubnt offload
https://www.youtube.com/c/+BenPin
================================================

File: Config.txt
================================================
Basic WAN_TO_LAN Rule
====================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable
Apply to Interface
====================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
 set firewall local name WAN_TO_LAN
Optional
====================================
edit service
 set gui listen-address 10.0.0.1
 set ssh listen-address 10.0.0.1 
================================================

File: Config.txt
================================================
Basic WAN_TO_LAN Rule
==================================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable
Apply to Interface
==================================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
 set firewall local name WAN_TO_LAN
Optional
==================================================
edit service
 set gui listen-address 10.0.0.1
 set gui https-port 9443
 set ssh listen-address 10.0.0.1 
 set ssh port 9222
================================================

File: Config.txt
================================================
Zones
==================================================
edit zone-policy
 set zone WAN default-action drop
 set zone WAN from LAN firewall name LAN_TO_ALL
 set zone WAN from LOCAL firewall name LOCAL_TO_ALL
 set zone WAN interface eth0
 set zone LAN default-action drop
 set zone LAN from WAN firewall name WAN_TO_LAN
 set zone LAN from LOCAL firewall name LOCAL_TO_ALL
 set zone LAN interface eth1
 set zone LOCAL default-action drop
 set zone LOCAL from WAN firewall name WAN_TO_LOCAL
 set zone LOCAL from LAN firewall name LAN_TO_ALL
 set zone LOCAL local-zone
Firewall Rules
==================================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable 
edit firewall name WAN_TO_LOCAL
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable
set firewall name LAN_TO_ALL default-action accept
set firewall name LOCAL_TO_ALL default-action accept
================================================

File: Config.txt
================================================
Zones
==================================================
edit zone-policy
 set zone WAN default-action drop
 set zone WAN from LAN firewall name LAN_TO_ALL
 set zone WAN from LOCAL firewall name LOCAL_TO_ALL
 set zone WAN interface eth0
 set zone LAN default-action drop
 set zone LAN from WAN firewall name WAN_TO_LAN
 set zone LAN from LOCAL firewall name LOCAL_TO_ALL
 set zone LAN interface eth1
 set zone LOCAL default-action drop
 set zone LOCAL from WAN firewall name WAN_TO_LOCAL
 set zone LOCAL from LAN firewall name LAN_TO_ALL
 set zone LOCAL local-zone
Firewall Rules
==================================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable 
edit firewall name WAN_TO_LOCAL
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable
set firewall name LAN_TO_ALL default-action accept
set firewall name LOCAL_TO_ALL default-action accept
================================================

File: Configuration.txt
================================================
Traffic Analysis with DPI
|-----------------------|
set system traffic-analysis dpi enable
set system traffic-analysis export enable
#Verify
show ubnt offload
Block Category & Allow Certain Apps
|---------------------------------|
#See which sites are grouped under 'adult websites' 
/usr/sbin/ubnt-dpi-util show-cat-apps TopSites-Adult
#If this list is empty, upgrade your firmware!
#See which category a specific site is grouped under
/usr/sbin/ubnt-dpi-util search-app pornhub.com
/usr/sbin/ubnt-dpi-util search-app penthouse
#Some adult websites are listed under Streaming-Media
#Combine Streaming-Media applications in a custom category
edit system traffic-analysis 
 set custom-category ADULT name hustlertube
 set custom-category ADULT name livejasmin.com
 set custom-category ADULT name porn.com
 set custom-category ADULT name pornhub.com
 set custom-category ADULT name redtube.com
 set custom-category ADULT name xhamster.com
 set custom-category ADULT name xnxx.com
 set custom-category ADULT name xtube
 set custom-category ADULT name xvideos.com
 set custom-category ADULT name youjizz
 set custom-category ADULT name youporn.com 
top 
#Drop rule for adult websites including custom category
edit firewall name BLOCK_ADULT
 set default-action accept
 set rule 10 description DROP_ADULT_SITES
 set rule 10 application category TopSites-Adult
 set rule 10 action drop 
 set rule 10 description DROP_ADULT_SITES
 set rule 20 application category ADULT
 set rule 20 action drop
top
#Apply to LAN interface
set interfaces switch switch0 firewall in name BLOCK_ADULT
commit
================================================

File: Configuration.txt
================================================
Capture with CLI
!---------------!
show interface ethernet eth0 capture
Capture with TCPdump
!-----------------------!
sudo tcpdump -i switch0 host <ip-address>
sudo tcpdump -i eth0 net <ip-network>/24 -w /home/ubnt/file.pcap -c 10
#Connect via WinSCP
#Copy over capture file
#Open in WireShark
================================================

File: Config.txt
================================================
Default Login
==================================================
Username: ubnt
Password: ubnt
Configuration Steps
==================================================
1. Associate interface with IP address
2. Create DHCP pool
3. Create reservations manually or 'Map Static IP'
Step 1
==================================================
set interfaces ethernet eth1 address 10.0.0.254/24 
Step 2
==================================================
edit service dhcp-server shared-network-name LOCAL 
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 default-router 10.0.0.254
 set subnet 10.0.0.0/24 dns-server 1.1.1.1
 set subnet 10.0.0.0/24 lease 28800
Step 3
==================================================
edit service dhcp-server shared-network-name LOCAL  
 set subnet 10.0.0.0/24 static-mapping XP ip-address 10.0.0.99
 set subnet 10.0.0.0/24 static-mapping XP mac-address '08:00:27:85:71:5e'
Helpful Commands
==================================================
show dhcp leases
show dhcp leases expired
show dhcp statistics
clear dhcp leases
clear dhcp lease ip 10.0.0.10
show configuration
show configuration commands
================================================

File: Config.txt
================================================
Default Login
==================================================
Username: ubnt
Password: ubnt
Configuration Steps
==================================================
1. Associate interface with IP address
2. Create DHCP pool
3. Create reservations manually or 'Map Static IP'
Step 1
==================================================
set interfaces ethernet eth1 address 10.0.0.254/24 
Step 2
==================================================
edit service dhcp-server shared-network-name LOCAL 
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 default-router 10.0.0.254
 set subnet 10.0.0.0/24 dns-server 1.1.1.1
 set subnet 10.0.0.0/24 lease 28800
Step 3
==================================================
edit service dhcp-server shared-network-name LOCAL  
 set subnet 10.0.0.0/24 static-mapping XP ip-address 10.0.0.99
 set subnet 10.0.0.0/24 static-mapping XP mac-address '08:00:27:85:71:5e'
Helpful Commands
==================================================
show dhcp leases
show dhcp leases expired
show dhcp statistics
clear dhcp leases
clear dhcp lease ip 10.0.0.10
show configuration
show configuration commands
================================================

File: Config.txt
================================================
Basics
==================================================
edit interfaces 
 set ethernet eth0 address dhcp
 set ethernet eth0 description WAN
 set ethernet eth1 address 10.0.0.1/24
 set ethernet eth1 description LAN
DHCP
==================================================
edit service dhcp-server shared-network-name LOCAL 
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 domain-name domain.local
 set subnet 10.0.0.0/24 lease 28800
Reservations
==================================================
edit service dhcp-server shared-network-name LOCAL  
 set subnet 10.0.0.0/24 static-mapping HOST1 ip-address 10.0.0.199
 set subnet 10.0.0.0/24 static-mapping HOST1 mac-address '08:00:27:85:71:5e'
Manual DNS (not needed if DNSMASQ is used)
==================================================
edit system static-host-mapping
 set host-name XP.domain.local inet 10.0.0.199
 set host-name XP.domain.local alias HOST1
DNSMASQ
==================================================
set interfaces ethernet eth0 dhcp-options name-server no-update
set system name-server 127.0.0.1
set system domain-name domain.local
set service dns forwarding name-server 8.8.8.8
set service dns forwarding name-server 8.8.4.4
set service dns forwarding listen-on eth1
set service dhcp-server use-dnsmasq enable
Verify
==================================================
show dhcp leases
show dhcp leases expired
show dhcp statistics
clear dhcp leases
clear dhcp lease ip 10.0.0.10
================================================

File: Config.txt
================================================
Basics
==================================================
edit interfaces 
 set ethernet eth0 address dhcp
 set ethernet eth0 description WAN
 set ethernet eth1 address 10.0.0.1/24
 set ethernet eth1 description LAN
DHCP
==================================================
edit service dhcp-server shared-network-name LOCAL 
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 domain-name domain.local
 set subnet 10.0.0.0/24 lease 28800
Reservations
==================================================
edit service dhcp-server shared-network-name LOCAL  
 set subnet 10.0.0.0/24 static-mapping HOST1 ip-address 10.0.0.199
 set subnet 10.0.0.0/24 static-mapping HOST1 mac-address '08:00:27:85:71:5e'
Manual DNS (not needed if DNSMASQ is used)
==================================================
edit system static-host-mapping
 set host-name XP.domain.local inet 10.0.0.199
 set host-name XP.domain.local alias HOST1
DNSMASQ
==================================================
set interfaces ethernet eth0 dhcp-options name-server no-update
set system name-server 127.0.0.1
set system domain-name domain.local
set service dns forwarding name-server 8.8.8.8
set service dns forwarding name-server 8.8.4.4
set service dns forwarding listen-on eth1
set service dhcp-server use-dnsmasq enable
Verify
==================================================
show dhcp leases
show dhcp leases expired
show dhcp statistics
clear dhcp leases
clear dhcp lease ip 10.0.0.10
================================================

File: Configuration.txt
================================================
WAN interfaces
!------------!
edit interfaces ethernet eth0 
 set pppoe 0 mtu 1492
 set pppoe 0 user-id ERX0
 set pppoe 0 password Pa$$w0rd
 set pppoe 0 name-server none
 set pppoe 0 default-route none
 set pppoe 0 firewall in name WAN_IN
 set pppoe 0 firewall local name WAN_LOCAL
top
edit interfaces ethernet eth1 
 set address dhcp
 set dhcp-options name-server no-update
 set dhcp-options default-route-distance 1
 set firewall in name WAN_IN
 set firewall local name WAN_LOCAL
set protocols static interface-route 0.0.0.0/0 next-hop-interface pppoe0
set system name-server 8.8.8.8
set firewall options mss-clamp mss 1452
Load-Balancing Defaults
!---------------------!
edit firewall group network-group PRIVATE_NETS
 set network 192.168.0.0/16
 set network 172.16.0.0/12
 set network 10.0.0.0/8
top 
edit firewall modify balance
 set rule 10 action modify
 set rule 10 description 'do NOT load balance lan to lan'
 set rule 10 destination group network-group PRIVATE_NETS
 set rule 10 modify table main
 set rule 20 action modify
 set rule 20 description 'do NOT load balance destination public address'
 set rule 20 destination group address-group ADDRv4_pppoe0
 set rule 20 modify table main
 set rule 30 action modify
 set rule 30 description 'do NOT load balance destination public address'
 set rule 30 destination group address-group ADDRv4_eth1
 set rule 30 modify table main
 set rule 70 action modify
 set rule 70 modify lb-group G
top
edit interfaces switch switch0 
 set address 192.168.1.1/24
 set firewall in modify balance
 set switch-port interface eth2
 set switch-port interface eth3
 set switch-port interface eth4
top 
edit load-balance group G
 set interface eth1
 set interface pppoe0
 set lb-local enable
edit service nat
 set rule 5000 description 'masquerade for WAN'
 set rule 5000 outbound-interface pppoe0
 set rule 5000 type masquerade
 set rule 5002 description 'masquerade for WAN 2'
 set rule 5002 outbound-interface eth1
 set rule 5002 type masquerade
top 
edit system conntrack 
 set expect-table-size 4096
 set hash-size 4096
 set table-size 32768
 set tcp half-open-connections 512
 set tcp loose enable
 set tcp max-retrans 3
top ; commit
Change Load-Balancing Defaults
!----------------------------!
edit load-balance group G
 set sticky dest-addr enable
 set interface pppoe0 route-test type ping target 8.8.8.8
 set interface pppoe0 route-test interval 5
 set interface pppoe0 route-test initial-delay 15
 set interface eth1 route-test type ping target 8.8.8.8 
 set interface eth1 route-test interval 5
 set interface eth1 route-test initial-delay 15
Influence Weighting
!-----------------!
edit load-balance group G 
 set interface pppoe0 weight 67
 set interface eth1 weight 33
Set one link to failover only
!---------------------------!
edit load-balance group G 
 set interface eth1 failover-only
Verify Load-Balancing
!-------------------!
show ip route
show load-balance status
show load-balance watchdog
show ip route table 201
show ip route table 202
================================================

File: Configuration Steps.txt
================================================
Configuration Steps Part #1
!-------------------------!
Power EdgeRouter-X using provided 12V power brick
Attach computer to Eth0 interface using standard (cat5e / cat6) UTP cable
Attach UAP-AC-LITE to Eth4 interface using standard (cat5e / cat6) UTP cable
Assign a static IP address to your PCs ethernet adapter
Open browser and navigate to http://192.168.1.1
Complete the basic wizard and reboot the device
Configuration Steps Part #2
!-------------------------!
After reboot, remove static IP address from your PCs ethernet adapter > DHCP
Unplug PC from Eth0 and re-attach to Eth1, Eth2 or Eth3 interface
Attach your Modem’s LAN interface to the ‘LAN’ port on the PoE-Injector
Attach the PoE-Injector ‘PoE’ port to the Eth0 interface of the EdgeRouter-X
Unplug the 12V power brick, the EdgeRouter will remain powered
Verify PCs IP address now given through DHCP
Open browser and navigate to http://192.168.1.1
Enable HWNAT Offloading through webpage or CLI
Reboot the EdgeRouter-X 
Enable passthrough PoE on the Eth4 interface, the UAP will now come online
Verify presence of UAP-AC-LITE using the ‘UBNT Device Discovery Tool’
Install controller on desired location and adopt UAP
================================================

File: Configuration.txt
================================================
Hardware Offloading
!-----------------!
configure
set system offload hwnat enable
commit
save 
exit
reboot
show ubnt offload
Reset to Factory Defaults
!-----------------------!
cp /opt/vyatta/etc/config.boot.default /config/config.boot
================================================

File: Configuration.txt
================================================
Passthrough PoE
!-------------!
edit interfaces ethernet eth4 
 set poe output pthru
 top ; commit
PoE Watchdog
!----------!
edit interfaces ethernet eth4 
 set poe watchdog address 192.168.1.x
 set poe watchdog failure-count 3
 set poe watchdog interval 15
 set poe watchdog off-delay 5
 set poe watchdog start-delay 300
 top ; commit
show interfaces ethernet poe watchdog
================================================

File: Config.txt
================================================
GUEST_TO_LAN Firewall Policy
==========================================
edit firewall group network-group LAN
 set network 192.168.0.0/16
 set network 172.16.0.0/12
 set network 10.0.0.0/8
edit firewall name GUEST_TO_LAN 
 set default-action accept
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
 set rule 2 action drop
 set rule 2 description "Network Group"
 set rule 2 log disable
 set rule 2 protocol all
 set rule 2 destination group network-group LAN
GUEST_TO_LOCAL Firewall Policy
==========================================
edit firewall name GUEST_TO_LOCAL
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
 set rule 2 action accept
 set rule 2 description DNS
 set rule 2 log disable
 set rule 2 protocol tcp_udp
 set rule 2 destination port 53
 set rule 3 action accept
 set rule 3 description DHCP
 set rule 3 log disable
 set rule 3 protocol udp
 set rule 3 destination port 67
Default WAN_TO_LAN Rule
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
 set firewall local name WAN_TO_LAN
edit interfaces ethernet eth2
 set address 172.16.0.1/24
 set firewall in name GUEST_TO_LAN 
 set firewall local name GUEST_TO_LOCAL
Misc Settings
==================================================
edit service dhcp-server shared-network-name GUEST 
 set subnet 172.16.0.0/24 default-router 172.16.0.1
 set subnet 172.16.0.0/24 start 172.16.0.10 stop 172.16.0.150
 set subnet 172.16.0.0/24 dns-server 172.16.0.1
 set subnet 172.16.0.0/24 lease 28800
edit service dhcp-server shared-network-name LAN 
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 lease 28800 
set service dns forwarding listen-on eth1
set service dns forwarding listen-on eth2
set service dns forwarding name-server 8.8.8.8
================================================

File: Config.txt
================================================
GUEST_TO_LAN Firewall Policy
==========================================
edit firewall group network-group LAN
 set network 192.168.0.0/16
 set network 172.16.0.0/12
 set network 10.0.0.0/8
edit firewall name GUEST_TO_LAN 
 set default-action accept
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
 set rule 2 action drop
 set rule 2 description "Network Group"
 set rule 2 log disable
 set rule 2 protocol all
 set rule 2 destination group network-group LAN
GUEST_TO_LOCAL Firewall Policy
==========================================
edit firewall name GUEST_TO_LOCAL
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
 set rule 2 action accept
 set rule 2 description DNS
 set rule 2 log disable
 set rule 2 protocol tcp_udp
 set rule 2 destination port 53
 set rule 3 action accept
 set rule 3 description DHCP
 set rule 3 log disable
 set rule 3 protocol udp
 set rule 3 destination port 67
Default WAN_TO_LAN Rule
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
 set firewall local name WAN_TO_LAN
edit interfaces ethernet eth2
 set address 172.16.0.1/24
 set firewall in name GUEST_TO_LAN 
 set firewall local name GUEST_TO_LOCAL
Misc Settings
==================================================
edit service dhcp-server shared-network-name GUEST 
 set subnet 172.16.0.0/24 default-router 172.16.0.1
 set subnet 172.16.0.0/24 start 172.16.0.10 stop 172.16.0.150
 set subnet 172.16.0.0/24 dns-server 172.16.0.1
 set subnet 172.16.0.0/24 lease 28800
edit service dhcp-server shared-network-name LAN 
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 lease 28800 
set service dns forwarding listen-on eth1
set service dns forwarding listen-on eth2
set service dns forwarding name-server 8.8.8.8
================================================

File: Config.txt
================================================
Virtual Interfaces (VIF)
==================================================
edit interfaces 
 set ethernet eth1 vif 10 address 10.0.0.1/24
 set ethernet eth1 vif 172 address 172.16.0.1/24
GUEST_TO_LAN Firewall Policy
==========================================
edit firewall group network-group LAN
 set network 192.168.0.0/16
 set network 172.16.0.0/12
 set network 10.0.0.0/8
edit firewall name GUEST_TO_LAN 
 set default-action accept
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
 set rule 2 action drop
 set rule 2 description "Network Group"
 set rule 2 log disable
 set rule 2 protocol all
 set rule 2 destination group network-group LAN
GUEST_TO_LOCAL Firewall Policy
==========================================
edit firewall name GUEST_TO_LOCAL
 set default-action drop
 set rule 1 action accept
 set rule 1 description DNS
 set rule 1 log disable
 set rule 1 protocol tcp_udp
 set rule 1 destination port 53
 set rule 2 action accept
 set rule 2 description DHCP
 set rule 2 log disable
 set rule 2 protocol udp
 set rule 2 destination port 67
 set rule 3 action accept
 set rule 3 description Established
 set rule 3 log disable
 set rule 3 protocol all
 set rule 3 state established enable
 set rule 3 state related enable 
Default WAN_TO_LAN Rule
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
edit interfaces ethernet eth1 vif 172
 set firewall in name GUEST_TO_LAN 
 set firewall local name GUEST_TO_LOCAL
Misc Settings
==================================================
edit service dhcp-server shared-network-name GUEST 
 set subnet 172.16.0.0/24 default-router 172.16.0.1
 set subnet 172.16.0.0/24 start 172.16.0.10 stop 172.16.0.150
 set subnet 172.16.0.0/24 dns-server 172.16.0.1
 set subnet 172.16.0.0/24 lease 28800
edit service dhcp-server shared-network-name LAN 
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 lease 28800 
set service dns forwarding listen-on eth1.10
set service dns forwarding listen-on eth1.172
set service dns forwarding name-server 8.8.8.8
================================================

File: Config.txt
================================================
Virtual Interfaces (VIF)
==================================================
edit interfaces 
 set ethernet eth1 vif 10 address 10.0.0.1/24
 set ethernet eth1 vif 172 address 172.16.0.1/24
GUEST_TO_LAN Firewall Policy
==========================================
edit firewall group network-group LAN
 set network 192.168.0.0/16
 set network 172.16.0.0/12
 set network 10.0.0.0/8
edit firewall name GUEST_TO_LAN 
 set default-action accept
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
 set rule 2 action drop
 set rule 2 description "Network Group"
 set rule 2 log disable
 set rule 2 protocol all
 set rule 2 destination group network-group LAN
GUEST_TO_LOCAL Firewall Policy
==========================================
edit firewall name GUEST_TO_LOCAL
 set default-action drop
 set rule 1 action accept
 set rule 1 description DNS
 set rule 1 log disable
 set rule 1 protocol tcp_udp
 set rule 1 destination port 53
 set rule 2 action accept
 set rule 2 description DHCP
 set rule 2 log disable
 set rule 2 protocol udp
 set rule 2 destination port 67
 set rule 3 action accept
 set rule 3 description Established
 set rule 3 log disable
 set rule 3 protocol all
 set rule 3 state established enable
 set rule 3 state related enable 
Default WAN_TO_LAN Rule
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
edit interfaces ethernet eth1 vif 172
 set firewall in name GUEST_TO_LAN 
 set firewall local name GUEST_TO_LOCAL
Misc Settings
==================================================
edit service dhcp-server shared-network-name GUEST 
 set subnet 172.16.0.0/24 default-router 172.16.0.1
 set subnet 172.16.0.0/24 start 172.16.0.10 stop 172.16.0.150
 set subnet 172.16.0.0/24 dns-server 172.16.0.1
 set subnet 172.16.0.0/24 lease 28800
edit service dhcp-server shared-network-name LAN 
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 lease 28800 
set service dns forwarding listen-on eth1.10
set service dns forwarding listen-on eth1.172
set service dns forwarding name-server 8.8.8.8
================================================

File: Config.txt
================================================
Default Login
==================================================
Username: ubnt
Password: ubnt
Configuration Steps
==================================================
1. Setup admin username and password
2. Configure default gateway (GW) and name servers (DNS) 
3. Configure optional system settings
4. Setup dynamic IP (DHCP) services and interfaces
5. Configure source NAT using masquerade (PAT)
6. Configure firewall
7. Associate IP addresses to WAN and LAN interfaces using DHCP or static addresses
8. Associate firewall zones with interfaces
Step 1, 2 & 3
==================================================
configure
edit system
 set gateway-address 2.0.0.2
 set host-name EdgeRouter
 set login user bpin level admin
 set login user bpin authentication plaintext-password Pa$$w0rd
 set name-server 8.8.8.8
 set name-server 8.8.4.4
 set time-zone Europe/Amsterdam
Step 4
==================================================
set interfaces ethernet eth1 address 2.0.0.1/30
edit service dhcp-server shared-network-name LOCAL 
 set subnet 192.168.1.0/24 start 192.168.1.10 stop 192.168.1.150
 set subnet 192.168.1.0/24 default-router 192.168.1.1
 set subnet 192.168.1.0/24 dns-server 192.168.1.1
Step 5
==================================================
edit service nat rule 5000
 set description "MASQUERADE"
 set log disable
 set outbound-interface eth1
 set protocol all
 set type masquerade
Step 6
==================================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
Step 7 & 8
================================================== 
edit interfaces ethernet eth1
 set firewall in name WAN_TO_LAN
 set firewall local name WAN_TO_LAN
================================================

File: Config.txt
================================================
Default Login
==================================================
Username: ubnt
Password: ubnt
Configuration Steps
==================================================
1. Setup admin username and password
2. Configure default gateway (GW) and name servers (DNS) 
3. Configure optional system settings
4. Setup dynamic IP (DHCP) services and interfaces
5. Configure source NAT using masquerade (PAT)
6. Configure firewall
7. Associate IP addresses to WAN and LAN interfaces using DHCP or static addresses
8. Associate firewall zones with interfaces
Step 1, 2 & 3
==================================================
configure
edit system
 set gateway-address 2.0.0.2
 set host-name EdgeRouter
 set login user bpin level admin
 set login user bpin authentication plaintext-password Pa$$w0rd
 set name-server 8.8.8.8
 set name-server 8.8.4.4
 set time-zone Europe/Amsterdam
 delete login user ubnt
Step 4
==================================================
set interfaces ethernet eth1 address 2.0.0.1/24 
edit service dhcp-server shared-network-name LOCAL 
 set subnet 192.168.1.0/24 start 192.168.1.11 stop 192.168.1.150
 set subnet 192.168.1.0/24 default-router 192.168.1.1
 set subnet 192.168.1.0/24 dns-server 8.8.8.8
 set subnet 192.168.1.0/24 dns-server 8.8.4.4
Step 5
==================================================
edit service nat rule 5000
 set description "MASQUERADE (PAT)"
 set log disable
 set outbound-interface eth1
 set protocol all
 set type masquerade
Step 6
==================================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable
Step 7 & 8
================================================== 
edit interfaces ethernet eth1
 set firewall in name WAN_TO_LAN
 set firewall local name WAN_TO_LAN
================================================

File: Config.txt
================================================
L2TP
==================================================
edit vpn
 set ipsec ipsec-interfaces interface eth0
 set ipsec nat-networks allowed-network 0.0.0.0/0
 set l2tp remote-access authentication mode local
 set l2tp remote-access authentication local-users username vpnbpin password Pa$$w0rd
 set l2tp remote-access client-ip-pool start 172.16.0.200
 set l2tp remote-access client-ip-pool stop 172.16.0.220
 set l2tp remote-access ipsec-settings authentication mode pre-shared-secret
 set l2tp remote-access ipsec-settings authentication pre-shared-secret Pa$$w0rd
 set l2tp remote-access ipsec-settings ike-lifetime 3600
 set l2tp remote-access outside-address 2.0.0.1
 set l2tp remote-access mtu 1450
Firewall Rule L2TP
==========================================
edit firewall name VPN
 set default-action drop
 set rule 1 action accept
 set rule 1 description IKE
 set rule 1 destination port 500
 set rule 1 log disable
 set rule 1 protocol udp
 set rule 1 source address 100.0.0.1
 set rule 2 action accept
 set rule 2 description L2TP
 set rule 2 destination port 1701
 set rule 2 log disable
 set rule 2 protocol udp
 set rule 2 source address 100.0.0.1
 set rule 3 action accept
 set rule 3 description ESP
 set rule 3 log disable
 set rule 3 protocol esp
 set rule 3 source address 100.0.0.1
 set rule 4 action accept
 set rule 4 description SSH
 set rule 4 destination port 22
 set rule 4 log disable
 set rule 4 protocol tcp
 set rule 4 source address 100.0.0.1
 set rule 5 action accept
 set rule 5 description HTTPS
 set rule 5 destination port 443
 set rule 5 log disable
 set rule 5 protocol tcp
 set rule 5 source address 100.0.0.1 
Default WAN_TO_LAN Rule
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable 
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
 set firewall local name VPN
Verify
==================================================
show vpn remote-access 
show vpn ipsec sa
show vpn log
================================================

File: EdgerouterL2TP.bat
================================================
rasdial Edgerouter vpnbpin Pa$$w0rd
route add 10.0.0.0 mask 255.255.255.0 0.0.0.0 IF 32
================================================

File: Windows Routes.txt
================================================
Windows L2TP Settings
==================================================
Allow these protocols -> MS-CHAP v2
Add route to Windows
==================================================
1. route print -4
2. determine PPTP vpn interface ID (32 in my case)
3. route add 10.0.0.0 mask 255.255.255.0 0.0.0.0 IF 32
Optionally create a batch (.bat) file
==================================================
rasdial Edgerouter vpnbpin Pa$$w0rd
route add 10.0.0.0 mask 255.255.255.0 0.0.0.0 IF 32
================================================

File: Configuration.txt
================================================
Default Credentials
!-----------------------!
Username : ubnt
Password : ubnt
Method #1 UniFi Discovery Utility
!-------------------------------!
#Install UniFi Discovery Utility on local PC
#Discover APs/devices
manage > set url to http://10.0.0.10:8080/inform
Method #2 SSH
!------------!
#Connect via SSH to UAP using terminal client
#Make sure the device is in a factory default state
#Make sure the device firmware is the same as the controller 
#USG SSH adoption
	mca-cli
	info
	set-inform http://10.0.0.10:8080/inform		 
#AP SSH adoption
	info
	set-inform http://10.0.0.10:8080/inform
#Device will go offline after adoption
#Run command again after adoption
set-inform
Method #3 DHCP Option 43
!----------------------!
#Connect to EdgeRouter/USG webpage
#Set the inform address in the unifi field of the dhcp-scope
#Connect via SSH to EdgeRouter/USG using terminal client
edit service dhcp-server shared-network-name LAN 
 set authoritative enable
 set subnet 192.168.1.0/24 default-router 192.168.1.254
 set subnet 192.168.1.0/24 dns-server 192.168.1.254
 set subnet 192.168.1.0/24 lease 86400
 set subnet 192.168.1.0/24 start 192.168.1.38 stop 192.168.1.243
 set subnet 192.168.1.0/24 unifi-controller 10.0.0.10
#Reboot UAP to aquire new DHCP settings
================================================

File: Config.txt
================================================
Configuration Commands
==================================================
configure
edit system
 set host-name Edgerouter
 set login user bpin level admin
 set login user bpin authentication plaintext-password Pa$$w0rd
 set name-server 8.8.8.8
 set name-server 8.8.4.4
 set time-zone Europe/Amsterdam
edit interfaces 
 set ethernet eth0 address 2.0.0.1/24 
 set ethernet eth0 description WAN  
 set ethernet eth1 address 10.0.0.1/24
 set ethernet eth1 description LAN  
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
================================================

File: Config.txt
================================================
LLDP & CDP
======================================
set service lldp
set service lldp legacy-protocols cdp
show lldp neighbors
================================================

File: Config.txt
================================================
Basic Configuration
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth0 description WAN
 set ethernet eth1 address 10.0.0.1/24
 set ethernet eth0 description LAN
Destination NAT Rules
==================================================
edit service nat
 set rule 1 description HTTP_100
 set rule 1 inside-address address 10.0.0.100
 set rule 1 inside-address port 80
 set rule 1 destination address 2.0.0.100
 set rule 1 destination port 80
 set rule 1 inbound-interface eth0
 set rule 1 log disable
 set rule 1 protocol tcp
 set rule 1 type destination
 set rule 2 description HTTP_1
 set rule 2 inside-address address 10.0.0.100
 set rule 2 inside-address port 80
 set rule 2 destination address 2.0.0.1
 set rule 2 destination port 80
 set rule 2 inbound-interface eth0
 set rule 2 log disable
 set rule 2 protocol tcp
 set rule 2 type destination
Assign Multiple IPs to External Interface
==================================================
edit interfaces ethernet eth0
 set address 2.0.0.100/24
================================================

File: Config.txt
================================================
Manual Time and Date
==================================================
Format = MMDDhhmmYYYY.ss
set date 0818hhmm2016.00
NTP & Timezones
==================================================
edit system 
 delete ntp server 0.ubnt.pool.ntp.org 
 delete ntp server 1.ubnt.pool.ntp.org 
 delete ntp server 2.ubnt.pool.ntp.org 
 delete ntp server 3.ubnt.pool.ntp.org 
 set ntp server nl.pool.ntp.org
 set time-zone Europe/Amsterdam
set date ntp
show date
show system uptime
show ntp nl.pool.ntp.org
show ntp
================================================

File: Config.txt
================================================
Manual Time and Date
=======================================
Format = MMDDhhmmYYYY.ss
set date 08271445082016.00
NTP & Timezones
=======================================
edit system 
 delete ntp server 0.ubnt.pool.ntp.org 
 delete ntp server 1.ubnt.pool.ntp.org 
 delete ntp server 2.ubnt.pool.ntp.org 
 delete ntp server 3.ubnt.pool.ntp.org 
 set ntp server nl.pool.ntp.org
 set time-zone Europe/Amsterdam
set date ntp
show date
show system uptime
show ntp nl.pool.ntp.org
show ntp
================================================

File: Config.txt
================================================
Hardware Offloading 
======================================
edit system offload
 set hwnat enable
 set ipsec enable
 set ipv4 forwarding enable
 set ipv4 gre enable
 set ipv6 forwarding enable
 set ipv6 gre enable
reboot
show ubnt offload 
================================================

File: Config.txt
================================================
OpenVPN Certificates
==================================================
sudo -i
cd /usr/lib/ssl/misc
./CA.sh -newca
	Passphrase				  = Pa$$w0rd
	countryName               = NL
	stateOrProvinceName       = QUICKCONFIGS
	organizationName          = QUICKCONFIGS
	organizationalUnitName    = QUICKCONFIGS
	commonName                = ROOT
cp demoCA/cacert.pem /config/auth
cp demoCA/private/cakey.pem /config/auth
./CA.sh -newreq
./CA.sh -sign
	countryName               = NL
	stateOrProvinceName       = QUICKCONFIGS
	localityName              = QUICKCONFIGS
	organizationName          = QUICKCONFIGS
	organizationalUnitName    = QUICKCONFIGS
	commonName                = SERVER
mv newcert.pem /config/auth/SERVER.pem
mv newkey.pem /config/auth/SERVER.key
openssl dhparam -out /config/auth/DH.pem -2 1024
./CA.sh -newreq
./CA.sh -sign
	countryName               = NL
	stateOrProvinceName       = QUICKCONFIGS
	localityName              = QUICKCONFIGS
	organizationName          = QUICKCONFIGS
	organizationalUnitName    = QUICKCONFIGS
	commonName                = CLIENT
mv newcert.pem /config/auth/CLIENT.pem
mv newkey.pem /config/auth/CLIENT.key
openssl rsa -in /config/auth/SERVER.key -out /config/auth/SERVER-NOPASS.key
openssl rsa -in /config/auth/CLIENT.key -out /config/auth/CLIENT-NOPASS.key
OpenVPN Interface
==================================================
edit interfaces openvpn vtun0
 set mode server
 set description OpenVPN
 set encryption aes256
 set hash sha256
 set server subnet 172.16.0.0/24
 set server push-route 10.0.0.0/24
 set server name-server 10.0.0.100
 set tls ca-cert-file /config/auth/cacert.pem
 set tls cert-file /config/auth/SERVER.pem
 set tls key-file /config/auth/SERVER-NOPASS.key
 set tls dh-file /config/auth/DH.pem
 set openvpn-option "--comp-lzo no"
Firewall Rule OpenVPN
==========================================
edit firewall name VPN
 set default-action drop
 set rule 1 action accept
 set rule 1 description OpenVPN
 set rule 1 destination port 1194
 set rule 1 log disable
 set rule 1 protocol udp
 set rule 1 source address 100.0.0.1
 set rule 2 action accept
 set rule 2 description SSH
 set rule 2 destination port 22
 set rule 2 log disable
 set rule 2 protocol tcp
 set rule 2 source address 100.0.0.1
 set rule 3 action accept
 set rule 3 description HTTPS
 set rule 3 destination port 443
 set rule 3 log disable
 set rule 3 protocol tcp
 set rule 3 source address 100.0.0.1
Default WAN_TO_LAN Rule
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
 set firewall local name VPN
Misc Settings
==================================================
set service dns forwarding listen-on vtun0
set service dns forwarding name-server 8.8.8.8
Verify
==================================================
show openvpn status server
================================================

File: edgerouter.ovpn
================================================
client
dev tun
proto udp
remote 2.0.0.1 1194
float
comp-lzo yes
push "comp-lzo yes"
resolv-retry infinite 
nobind
persist-key 
persist-tun 
verb 3
auth SHA256
cipher AES-256-CBC
ca cacert.pem 
cert CLIENT.pem
key CLIENT-NOPASS.key
================================================

File: Cisco & Juniper Config.txt
================================================
Cisco Config
============================================
interface gi0/0 
 ip address 10.0.13.3 255.255.255.0
 no shutdown
int lo1
 ip address 13.0.1.1 255.255.255.0
 ip ospf network point-to-point
int lo2
 ip address 13.0.2.1 255.255.255.0
 ip ospf network point-to-point
int lo3
 ip address 13.0.3.1 255.255.255.0
 ip ospf network point-to-point
router ospf 1
 router-id 3.3.3.3
 network 10.0.13.0 0.0.0.255 area 0
 network 13.0.0.0 0.0.3.255 area 0
 passive-interface default
 no passive-interface gi0/0
SRX Config
============================================
set interfaces fe-0/0/0 unit 0 family inet address 10.0.12.2/30
set routing-options router-id 2.2.2.2
edit protocols ospf area 0.0.0.0 
 set interface fe-0/0/0.0 interface-type p2p
edit security zones security-zone trust
 set interface fe-0/0/0.0
 set host-inbound-traffic protocols ospf
================================================

File: Config.txt
================================================
Enable Interfaces for OSPF
====================================
edit interfaces ethernet eth1
 set address 10.0.12.1/30
 set ip ospf network point-to-point
 set description TO_SRX
edit interfaces ethernet eth2
 set address 10.0.13.1/24
 set description TO_CISCO
Advertise Networks
====================================
edit protocols ospf
 set area 0 network 10.0.12.0/24
 set area 0 network 10.0.13.0/30
 set parameters router-id 1.1.1.1
 set passive-interface default
 set passive-interface-exclude eth1
 set passive-interface-exclude eth2
================================================

File: Cisco & Juniper Config.txt
================================================
Cisco Config
============================================
interface gi0/0 
 ip address 10.0.13.3 255.255.255.0
 no shutdown
int lo1
 ip address 13.0.1.1 255.255.255.0
 ip ospf network point-to-point
int lo2
 ip address 13.0.2.1 255.255.255.0
 ip ospf network point-to-point
int lo3
 ip address 13.0.3.1 255.255.255.0
 ip ospf network point-to-point
router ospf 1
 router-id 3.3.3.3
 network 10.0.13.0 0.0.0.255 area 0
 network 13.0.0.0 0.0.3.255 area 0
 passive-interface default
 no passive-interface gi0/0
SRX Config
============================================
set interfaces fe-0/0/0 unit 0 family inet address 10.0.12.2/30
set routing-options router-id 2.2.2.2
edit protocols ospf area 0.0.0.0 
 set interface fe-0/0/0.0 interface-type p2p
edit security zones security-zone trust
 set interface fe-0/0/0.0
 set host-inbound-traffic protocols ospf
================================================

File: Config.txt
================================================
Enable Interfaces for OSPF
====================================
edit interfaces ethernet eth1
 set address 10.0.12.1/30
 set ip ospf network point-to-point
 set description TO_SRX
edit interfaces ethernet eth2
 set address 10.0.13.1/24
 set description TO_CISCO
Advertise Networks
====================================
edit protocols ospf
 set area 0 network 10.0.12.0/24
 set area 0 network 10.0.13.0/30
 set parameters router-id 1.1.1.1
 set passive-interface default
 set passive-interface-exclude eth1
 set passive-interface-exclude eth2
================================================

File: Cisco & Juniper Config.txt
================================================
Cisco Config
============================================
interface gi0/0 
 ip address 10.0.13.3 255.255.255.0
 ip ospf network point-to-point
 no shutdown
int lo1
 ip address 13.0.1.1 255.255.255.0
 ip ospf network point-to-point
int lo2
 ip address 13.0.2.1 255.255.255.0
 ip ospf network point-to-point
int lo3
 ip address 13.0.3.1 255.255.255.0
 ip ospf network point-to-point
router ospf 1
 router-id 3.3.3.3
 network 10.0.13.0 0.0.0.255 area 0
 network 13.0.0.0 0.0.3.255 area 13
 passive-interface default
 no passive-interface gi0/0
SRX Config
============================================
set interfaces fe-0/0/0 unit 0 family inet address 10.0.12.2/30
set routing-options router-id 2.2.2.2
edit protocols ospf area 0.0.0.12
 set interface fe-0/0/0.0 interface-type p2p
edit security zones security-zone trust
 set interface fe-0/0/0.0
 set host-inbound-traffic protocols ospf
================================================

File: Config.txt
================================================
Enable Interfaces for OSPF
====================================
edit interfaces ethernet eth1
 set address 10.0.12.1/30
 set ip ospf network point-to-point
 set description TO_SRX
edit interfaces ethernet eth2
 set address 10.0.13.1/24
 set ip ospf network point-to-point
 set description TO_CISCO
Advertise Networks
====================================
edit protocols ospf
 set area 12 network 10.0.12.0/24
 set area 0 network 10.0.13.0/30
 set parameters router-id 1.1.1.1
 set passive-interface default
 set passive-interface-exclude eth1
 set passive-interface-exclude eth2
================================================

File: Cisco & Juniper Config.txt
================================================
Cisco Config
============================================
interface gi0/0 
 ip address 10.0.13.3 255.255.255.0
 ip ospf network point-to-point
 no shutdown
int lo1
 ip address 13.0.1.1 255.255.255.0
 ip ospf network point-to-point
int lo2
 ip address 13.0.2.1 255.255.255.0
 ip ospf network point-to-point
int lo3
 ip address 13.0.3.1 255.255.255.0
 ip ospf network point-to-point
router ospf 1
 router-id 3.3.3.3
 network 10.0.13.0 0.0.0.255 area 0
 network 13.0.0.0 0.0.3.255 area 13
 passive-interface default
 no passive-interface gi0/0
SRX Config
============================================
set interfaces fe-0/0/0 unit 0 family inet address 10.0.12.2/30
set routing-options router-id 2.2.2.2
edit protocols ospf area 0.0.0.12
 set interface fe-0/0/0.0 interface-type p2p
edit security zones security-zone trust
 set interface fe-0/0/0.0
 set host-inbound-traffic protocols ospf
================================================

File: Config.txt
================================================
Enable Interfaces for OSPF
====================================
edit interfaces ethernet eth1
 set address 10.0.12.1/30
 set ip ospf network point-to-point
 set description TO_SRX
edit interfaces ethernet eth2
 set address 10.0.13.1/24
 set ip ospf network point-to-point
 set description TO_CISCO
Advertise Networks
====================================
edit protocols ospf
 set area 12 network 10.0.12.0/24
 set area 0 network 10.0.13.0/30
 set parameters router-id 1.1.1.1
 set passive-interface default
 set passive-interface-exclude eth1
 set passive-interface-exclude eth2
================================================

File: Cisco & Juniper Config.txt
================================================
Cisco Config
============================================
interface gi0/0 
 ip address 10.0.13.3 255.255.255.0
 ip ospf message-digest-key 1 md5 ubnt
 ip ospf authentication message-digest
 no shutdown
int lo1
 ip address 13.0.1.1 255.255.255.0
 ip ospf network point-to-point
int lo2
 ip address 13.0.2.1 255.255.255.0
 ip ospf network point-to-point
int lo3
 ip address 13.0.3.1 255.255.255.0
 ip ospf network point-to-point
router ospf 1
 router-id 3.3.3.3
 network 10.0.13.0 0.0.0.255 area 0
 network 13.0.0.0 0.0.3.255 area 0
 passive-interface default
 no passive-interface gi0/0
SRX Config
============================================
set interfaces fe-0/0/0 unit 0 family inet address 10.0.12.2/30
set routing-options router-id 2.2.2.2
edit protocols ospf area 0.0.0.0 
 set interface fe-0/0/0.0 interface-type p2p
 set interface fe-0/0/0.0 authentication simple-password ubnt
edit security zones security-zone trust
 set interface fe-0/0/0.0
 set host-inbound-traffic protocols ospf
================================================

File: Config.txt
================================================
Enable Interfaces for OSPF
====================================
edit interfaces ethernet eth1
 set address 10.0.12.1/30
 set ip ospf network point-to-point
 set description TO_SRX
edit interfaces ethernet eth2
 set address 10.0.13.1/24
 set description TO_CISCO
Advertise Networks
====================================
edit protocols ospf
 set area 0 network 10.0.12.0/24
 set area 0 network 10.0.13.0/30
 set parameters router-id 1.1.1.1
 set passive-interface default
 set passive-interface-exclude eth1
 set passive-interface-exclude eth2
Interface Authentication
====================================
edit interfaces ethernet eth1 ip ospf
 set authentication plaintext-password ubnt
edit interfaces ethernet eth2 ip ospf
 set authentication md5 key-id 1 md5-key ubnt
Area Authentication
====================================
edit protocols ospf area 0
 set authentication md5
================================================

File: Cisco & Juniper Config.txt
================================================
Cisco Config
============================================
interface gi0/0 
 ip address 10.0.13.3 255.255.255.0
 ip ospf message-digest-key 1 md5 ubnt
 ip ospf authentication message-digest
 no shutdown
int lo1
 ip address 13.0.1.1 255.255.255.0
 ip ospf network point-to-point
int lo2
 ip address 13.0.2.1 255.255.255.0
 ip ospf network point-to-point
int lo3
 ip address 13.0.3.1 255.255.255.0
 ip ospf network point-to-point
router ospf 1
 router-id 3.3.3.3
 network 10.0.13.0 0.0.0.255 area 0
 network 13.0.0.0 0.0.3.255 area 0
 passive-interface default
 no passive-interface gi0/0
SRX Config
============================================
set interfaces fe-0/0/0 unit 0 family inet address 10.0.12.2/30
set routing-options router-id 2.2.2.2
edit protocols ospf area 0.0.0.0 
 set interface fe-0/0/0.0 interface-type p2p
 set interface fe-0/0/0.0 authentication simple-password ubnt
edit security zones security-zone trust
 set interface fe-0/0/0.0
 set host-inbound-traffic protocols ospf
================================================

File: Config.txt
================================================
Enable Interfaces for OSPF
====================================
edit interfaces ethernet eth1
 set address 10.0.12.1/30
 set ip ospf network point-to-point
 set description TO_SRX
edit interfaces ethernet eth2
 set address 10.0.13.1/24
 set description TO_CISCO
Advertise Networks
====================================
edit protocols ospf
 set area 0 network 10.0.12.0/24
 set area 0 network 10.0.13.0/30
 set parameters router-id 1.1.1.1
 set passive-interface default
 set passive-interface-exclude eth1
 set passive-interface-exclude eth2
Interface Authentication
====================================
edit interfaces ethernet eth1 ip ospf
 set authentication plaintext-password ubnt
edit interfaces ethernet eth2 ip ospf
 set authentication md5 key-id 1 md5-key ubnt
Area Authentication
====================================
edit protocols ospf area 0
 set authentication md5
================================================

File: Cisco & Juniper Config.txt
================================================
Cisco Config
============================================
interface gi0/0 
 ip address 10.0.13.3 255.255.255.0
 ip ospf network point-to-point
 no shutdown
router ospf 1
 router-id 3.3.3.3
 network 10.0.13.0 0.0.0.255 area 0
 passive-interface default
 no passive-interface gi0/0
SRX Config
============================================
set interfaces fe-0/0/0 unit 0 family inet address 10.0.12.2/30
set routing-options router-id 2.2.2.2
edit protocols ospf area 0.0.0.12
 set interface fe-0/0/0.0 interface-type p2p
edit security zones security-zone trust
 set interface fe-0/0/0.0
 set host-inbound-traffic protocols ospf
================================================

File: Config.txt
================================================
Enable Interfaces for OSPF
====================================
edit interfaces ethernet eth1
 set address 10.0.12.1/30
 set ip ospf network point-to-point
 set description TO_SRX
edit interfaces ethernet eth2
 set address 10.0.13.1/24
 set ip ospf network point-to-point
 set description TO_CISCO
Advertise Networks
====================================
edit protocols ospf
 set area 12 network 10.0.12.0/24
 set area 0 network 10.0.13.0/30
 set parameters router-id 1.1.1.1
 set passive-interface default
 set passive-interface-exclude eth1
 set passive-interface-exclude eth2
Redistribution
====================================
edit interfaces loopback lo
 set ip ospf network point-to-point
 set address 11.0.1.1/24
 set address 11.0.2.1/24
 set address 11.0.3.1/24
edit protocols ospf
 set redistribute connected metric-type 1
 set redistribute connected metric 4
================================================

File: Cisco & Juniper Config.txt
================================================
Cisco Config
============================================
interface gi0/0 
 ip address 10.0.13.3 255.255.255.0
 ip ospf network point-to-point
 no shutdown
router ospf 1
 router-id 3.3.3.3
 network 10.0.13.0 0.0.0.255 area 0
 passive-interface default
 no passive-interface gi0/0
SRX Config
============================================
set interfaces fe-0/0/0 unit 0 family inet address 10.0.12.2/30
set routing-options router-id 2.2.2.2
edit protocols ospf area 0.0.0.12
 set interface fe-0/0/0.0 interface-type p2p
edit security zones security-zone trust
 set interface fe-0/0/0.0
 set host-inbound-traffic protocols ospf
================================================

File: Config.txt
================================================
Enable Interfaces for OSPF
====================================
edit interfaces ethernet eth1
 set address 10.0.12.1/30
 set ip ospf network point-to-point
 set description TO_SRX
edit interfaces ethernet eth2
 set address 10.0.13.1/24
 set ip ospf network point-to-point
 set description TO_CISCO
Advertise Networks
====================================
edit protocols ospf
 set area 12 network 10.0.12.0/24
 set area 0 network 10.0.13.0/30
 set parameters router-id 1.1.1.1
 set passive-interface default
 set passive-interface-exclude eth1
 set passive-interface-exclude eth2
Redistribution
====================================
edit interfaces loopback lo
 set ip ospf network point-to-point
 set address 11.0.1.1/24
 set address 11.0.2.1/24
 set address 11.0.3.1/24
edit protocols ospf
 set redistribute connected metric-type 1
 set redistribute connected metric 4
================================================

File: Cisco & Juniper Config.txt
================================================
Cisco Config
============================================
interface gi0/0 
 ip address 10.0.13.3 255.255.255.0
 ip ospf network point-to-point
 no shutdown
router ospf 1
 router-id 3.3.3.3
 network 10.0.13.0 0.0.0.255 area 0
 passive-interface default
 no passive-interface gi0/0
SRX Config
============================================
set interfaces fe-0/0/0 unit 0 family inet address 10.0.12.2/30
set routing-options router-id 2.2.2.2
edit protocols ospf area 0.0.0.12
 set interface fe-0/0/0.0 interface-type p2p
edit security zones security-zone trust
 set interface fe-0/0/0.0
 set host-inbound-traffic protocols ospf
================================================

File: Config.txt
================================================
Route-Maps & Prefix-Lists
====================================
edit policy prefix-list LOOPBACKS
 set rule 1 prefix 11.0.0.0/22
 set rule 1 ge 24
 set rule 1 le 24
 set rule 1 action permit
edit policy route-map OSPF 
 set rule 1 match ip address prefix-list LOOPBACKS
 set rule 1 action permit
edit protocols ospf
 set redistribute connected route-map OSPF
 set redistribute connected metric-type 2
================================================

File: Cisco & Juniper Config.txt
================================================
Cisco Config
============================================
interface gi0/0 
 ip address 10.0.13.3 255.255.255.0
 ip ospf network point-to-point
 no shutdown
router ospf 1
 router-id 3.3.3.3
 network 10.0.13.0 0.0.0.255 area 0
 passive-interface default
 no passive-interface gi0/0
SRX Config
============================================
set interfaces fe-0/0/0 unit 0 family inet address 10.0.12.2/30
set routing-options router-id 2.2.2.2
edit protocols ospf area 0.0.0.12
 set interface fe-0/0/0.0 interface-type p2p
edit security zones security-zone trust
 set interface fe-0/0/0.0
 set host-inbound-traffic protocols ospf
================================================

File: Config.txt
================================================
Route-Maps & Prefix-Lists
====================================
edit policy prefix-list LOOPBACKS
 set rule 1 prefix 11.0.0.0/22
 set rule 1 ge 24
 set rule 1 le 24
 set rule 1 action permit
edit policy route-map OSPF 
 set rule 1 match ip address prefix-list LOOPBACKS
 set rule 1 action permit
edit protocols ospf
 set redistribute connected route-map OSPF
 set redistribute connected metric-type 2
================================================

File: Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VTI Interface
==================================================
set interfaces vti vti0 address 12.0.0.2/30 
set interfaces vti vti0 mtu 1400
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group FOO0 lifetime 28800 
 set ike-group FOO0 proposal 1 dh-group 14
 set ike-group FOO0 proposal 1 encryption aes128
 set ike-group FOO0 proposal 1 hash md5
 set esp-group FOO0 lifetime 3600
 set esp-group FOO0 proposal 1 encryption aes128
 set esp-group FOO0 proposal 1 hash md5
 set esp-group FOO0 mode tunnel
 set esp-group FOO0 pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group FOO0
 set vti bind vti0
 set vti esp-group FOO0
OSPF
==================================================
edit protocols ospf
 set parameters router-id 2.2.2.2
 set area 0 network 10.0.0.0/24
 set area 1 network 12.0.0.0/30
set interfaces vti vti0 ip ospf network point-to-point
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
show ip ospf neighbor
show ip ospf interface brief
show ip ospf database
================================================

File: Juniper VPN Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set fe-0/0/0 unit 0 family inet address 1.0.0.1/24
 set fe-0/0/1 unit 0 family inet address 172.16.0.1/24
set routing-options static route 0.0.0.0/0 next-hop 1.0.0.2
VTI Interface
================================================== 
edit interfaces
 set st0 unit 0 family inet mtu 1400
 set st0 unit 0 family inet address 12.0.0.1/30
VPN Tunnel
================================================
edit security 
 set ike proposal IKE authentication-method pre-shared-keys
 set ike proposal IKE dh-group group14
 set ike proposal IKE authentication-algorithm md5
 set ike proposal IKE encryption-algorithm aes-128-cbc
 set ike proposal IKE lifetime-seconds 28800
 set ike policy IKE_POLICY mode main
 set ike policy IKE_POLICY proposals IKE
 set ike policy IKE_POLICY pre-shared-key ascii-text Pa$$w0rd
 set ike gateway IKE_GATEWAY ike-policy IKE_POLICY
 set ike gateway IKE_GATEWAY address 2.0.0.1
 set ike gateway IKE_GATEWAY external-interface fe-0/0/0
 set ike gateway IKE_GATEWAY local-address 1.0.0.1
 set ipsec proposal ESP protocol esp
 set ipsec proposal ESP authentication-algorithm hmac-md5-96
 set ipsec proposal ESP encryption-algorithm aes-128-cbc
 set ipsec proposal ESP lifetime-seconds 3600
 set ipsec policy ESP_POLICY proposals ESP
 set ipsec vpn ESP_VPN bind-interface st0.0
 set ipsec vpn ESP_VPN ike gateway IKE_GATEWAY
 set ipsec vpn ESP_VPN ike ipsec-policy ESP_POLICY
 set ipsec vpn ESP_VPN establish-tunnels immediately
Security Settings
==================================================
set security zones security-zone trust interfaces st0.0
edit security policies from-zone trust to-zone trust 
 set policy trust-to-trust match source-address any
 set policy trust-to-trust match destination-address any
 set policy trust-to-trust match application any
 set policy trust-to-trust then permit
OSPF
==================================================
set routing-options router-id 1.1.1.1 
edit protocols ospf 
 set area 1 interface st0.0 interface-type p2p  
 set area 1 interface fe-0/0/1.0    
Verify 
==================================================
show security ike security-associations
show security ike security-associations detail
show security ipsec sa
show security ipsec sa detail
show security ipsec statistics
show ospf neighbor 
show ospf interface
show ospf database
================================================

File: Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VTI Interface
==================================================
set interfaces vti vti0 address 12.0.0.2/30 
set interfaces vti vti0 mtu 1400
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group IKE lifetime 28800 
 set ike-group IKE proposal 1 dh-group 14
 set ike-group IKE proposal 1 encryption aes128
 set ike-group IKE proposal 1 hash md5
 set esp-group ESP lifetime 3600
 set esp-group ESP proposal 1 encryption aes128
 set esp-group ESP proposal 1 hash md5
 set esp-group ESP mode tunnel
 set esp-group ESP pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set vti bind vti0
 set vti esp-group ESP
OSPF
==================================================
edit protocols ospf
 set parameters router-id 2.2.2.2
 set area 0 network 10.0.0.0/24
 set area 1 network 12.0.0.0/30
set interfaces vti vti0 ip ospf network point-to-point
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
show ip ospf neighbor
show ip ospf interface brief
show ip ospf database
================================================

File: Juniper VPN Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set fe-0/0/0 unit 0 family inet address 1.0.0.1/24
 set fe-0/0/1 unit 0 family inet address 172.16.0.1/24
set routing-options static route 0.0.0.0/0 next-hop 1.0.0.2
VTI Interface
================================================== 
edit interfaces
 set st0 unit 0 family inet mtu 1400
 set st0 unit 0 family inet address 12.0.0.1/30
VPN Tunnel
================================================
edit security 
 set ike proposal IKE authentication-method pre-shared-keys
 set ike proposal IKE dh-group group14
 set ike proposal IKE authentication-algorithm md5
 set ike proposal IKE encryption-algorithm aes-128-cbc
 set ike proposal IKE lifetime-seconds 28800
 set ike policy IKE_POLICY mode main
 set ike policy IKE_POLICY proposals IKE
 set ike policy IKE_POLICY pre-shared-key ascii-text Pa$$w0rd
 set ike gateway IKE_GATEWAY ike-policy IKE_POLICY
 set ike gateway IKE_GATEWAY address 2.0.0.1
 set ike gateway IKE_GATEWAY external-interface fe-0/0/0
 set ike gateway IKE_GATEWAY local-address 1.0.0.1
 set ipsec proposal ESP protocol esp
 set ipsec proposal ESP authentication-algorithm hmac-md5-96
 set ipsec proposal ESP encryption-algorithm aes-128-cbc
 set ipsec proposal ESP lifetime-seconds 3600
 set ipsec policy ESP_POLICY proposals ESP
 set ipsec vpn ESP_VPN bind-interface st0.0
 set ipsec vpn ESP_VPN ike gateway IKE_GATEWAY
 set ipsec vpn ESP_VPN ike ipsec-policy ESP_POLICY
 set ipsec vpn ESP_VPN establish-tunnels immediately
Security Settings
==================================================
set security zones security-zone trust interfaces st0.0
edit security policies from-zone trust to-zone trust 
 set policy trust-to-trust match source-address any
 set policy trust-to-trust match destination-address any
 set policy trust-to-trust match application any
 set policy trust-to-trust then permit
OSPF
==================================================
set routing-options router-id 1.1.1.1 
edit protocols ospf 
 set area 1 interface st0.0 interface-type p2p  
 set area 1 interface fe-0/0/1.0    
Verify 
==================================================
show security ike security-associations
show security ike security-associations detail
show security ipsec sa
show security ipsec sa detail
show security ipsec statistics
show ospf neighbor 
show ospf interface
show ospf database
================================================

File: Config.txt
================================================
PPTP
==================================================
edit vpn pptp remote-access 
 set authentication mode local
 set authentication local-users username vpnbpin password Pa$$w0rd
 set client-ip-pool start 172.16.0.200
 set client-ip-pool stop 172.16.0.220
 ;set dhcp-interface eth0
 set outside-address 2.0.0.1
 set mtu 1024
 set dns-servers server-1 10.0.0.100
 set dns-servers server-2 8.8.8.8
Firewall Rule PPTP
==========================================
edit firewall name VPN
 set default-action drop
 set rule 1 action accept
 set rule 1 description PPTP
 set rule 1 destination port 1723
 set rule 1 log disable
 set rule 1 protocol tcp
 set rule 1 source address 100.0.0.1
 set rule 2 action accept
 set rule 2 description GRE
 set rule 2 log disable
 set rule 2 protocol gre
 set rule 2 source address 100.0.0.1
 set rule 3 action accept
 set rule 3 description SSH
 set rule 3 destination port 22
 set rule 3 log disable
 set rule 3 protocol tcp
 set rule 3 source address 100.0.0.1
 set rule 4 action accept
 set rule 4 description HTTPS
 set rule 4 destination port 443
 set rule 4 log disable
 set rule 4 protocol tcp
 set rule 4 source address 100.0.0.1
Default WAN_TO_LAN Rule
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
 set firewall local name VPN
================================================

File: EdgerouterPPTP.bat
================================================
rasdial Edgerouter vpnbpin Pa$$w0rd
route add 10.0.0.0 mask 255.255.255.0 0.0.0.0 IF 32
================================================

File: Windows Routes.txt
================================================
Add route to Windows
==================================================
1. route print -4
2. determine PPTP vpn interface ID (32 in my case)
3. route add 10.0.0.0 mask 255.255.255.0 0.0.0.0 IF 32
Optionally create a batch (.bat) file
==================================================
rasdial Edgerouter vpnbpin Pa$$w0rd
route add 10.0.0.0 mask 255.255.255.0 0.0.0.0 IF 32
================================================

File: Config.txt
================================================
PPTP
==================================================
edit vpn pptp remote-access 
 set authentication mode local
 set authentication local-users username vpnbpin password Pa$$w0rd
 set client-ip-pool start 172.16.0.200
 set client-ip-pool stop 172.16.0.220
 ;set dhcp-interface eth0
 set outside-address 2.0.0.1
 set mtu 1024
 set dns-servers server-1 10.0.0.100
 set dns-servers server-2 8.8.8.8
Firewall Rule PPTP
==========================================
edit firewall name VPN
 set default-action drop
 set rule 1 action accept
 set rule 1 description PPTP
 set rule 1 destination port 1723
 set rule 1 log disable
 set rule 1 protocol tcp
 set rule 1 source address 100.0.0.1
 set rule 2 action accept
 set rule 2 description GRE
 set rule 2 log disable
 set rule 2 protocol gre
 set rule 2 source address 100.0.0.1
 set rule 3 action accept
 set rule 3 description SSH
 set rule 3 destination port 22
 set rule 3 log disable
 set rule 3 protocol tcp
 set rule 3 source address 100.0.0.1
 set rule 4 action accept
 set rule 4 description HTTPS
 set rule 4 destination port 443
 set rule 4 log disable
 set rule 4 protocol tcp
 set rule 4 source address 100.0.0.1
Default WAN_TO_LAN Rule
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
 set firewall local name VPN
================================================

File: EdgerouterPPTP.bat
================================================
rasdial Edgerouter vpnbpin Pa$$w0rd
route add 10.0.0.0 mask 255.255.255.0 0.0.0.0 IF 32
================================================

File: Windows Routes.txt
================================================
Add route to Windows
==================================================
1. route print -4
2. determine PPTP vpn interface ID (32 in my case)
3. route add 10.0.0.0 mask 255.255.255.0 0.0.0.0 IF 32
Optionally create a batch (.bat) file
==================================================
rasdial Edgerouter vpnbpin Pa$$w0rd
route add 10.0.0.0 mask 255.255.255.0 0.0.0.0 IF 32
================================================

File: Config.txt
================================================
Port Forwarding
==========================================
edit port-forward
 set auto-firewall disable
 set lan-interface eth1
 set wan-interface eth0
 set rule 1 description "80_TO_WEBSERVER"
 set rule 1 protocol tcp
 set rule 1 original-port 80
 set rule 1 forward-to address 10.0.0.100
 set rule 1 forward-to port 80
 set rule 2 description "8080_TO_WEBSERVER"
 set rule 2 protocol tcp
 set rule 2 original-port 8080
 set rule 2 forward-to address 10.0.0.100
 set rule 2 forward-to port 80
Firewall Entries
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description PortForward
 set rule 1 log disable
 set rule 1 protocol tcp
 set rule 1 destination port 80
 set rule 2 action accept
 set rule 2 description Established
 set rule 2 log disable
 set rule 2 protocol all
 set rule 2 state established enable
 set rule 2 state related enable 
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
================================================

File: Config.txt
================================================
Port Forwarding
==========================================
edit port-forward
 set auto-firewall disable
 set lan-interface eth1
 set wan-interface eth0
 set rule 1 description "80_TO_WEBSERVER"
 set rule 1 protocol tcp
 set rule 1 original-port 80
 set rule 1 forward-to address 10.0.0.100
 set rule 1 forward-to port 80
 set rule 2 description "8080_TO_WEBSERVER"
 set rule 2 protocol tcp
 set rule 2 original-port 8080
 set rule 2 forward-to address 10.0.0.100
 set rule 2 forward-to port 80
Firewall Entries
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description PortForward
 set rule 1 log disable
 set rule 1 protocol tcp
 set rule 1 destination port 80
 set rule 2 action accept
 set rule 2 description Established
 set rule 2 log disable
 set rule 2 protocol all
 set rule 2 state established enable
 set rule 2 state related enable 
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
================================================

File: Configuration.txt
================================================
Port Forwarding
!-------------!
edit port-forward
 set auto-firewall disable
 set hairpin-nat enable
 set lan-interface switch0
 set wan-interface eth0
 set rule 1 description IKE
 set rule 1 forward-to address 192.168.1.10
 set rule 1 forward-to port 500
 set rule 1 original-port 500
 set rule 1 protocol udp
 set rule 2 description ESP
 set rule 2 forward-to address 192.168.1.10
 set rule 2 forward-to port 4500
 set rule 2 original-port 4500
 set rule 2 protocol udp
top
Firewall Entries
!--------------!
edit firewall name WAN_IN
 set default-action drop
 set rule 10 action accept
 set rule 10 description 'Established'
 set rule 10 log disable
 set rule 10 protocol all
 set rule 10 state established enable
 set rule 10 state related enable 
 set rule 20 action drop
 set rule 20 description 'Invalid'
 set rule 20 log disable
 set rule 20 protocol all
 set rule 20 state invalid enable
 set rule 30 action accept
 set rule 30 description ESP
 set rule 30 log disable
 set rule 30 protocol udp
 set rule 30 destination port 4500
 set rule 40 action accept
 set rule 40 description IKE
 set rule 40 log disable
 set rule 40 protocol udp
 set rule 40 destination port 500 
top ; commit
Alternatively use Destination NAT
!-------------------------------!
edit service nat
 set rule 1 description IKE
 set rule 1 destination port 500
 set rule 1 inbound-interface eth0
 set rule 1 inside-address address 192.168.1.10
 set rule 1 inside-address port 500
 set rule 1 log disable
 set rule 1 protocol udp
 set rule 1 type destination
 set rule 2 description ESP
 set rule 2 destination port 4500
 set rule 2 inbound-interface eth0
 set rule 2 inside-address address 192.168.1.10
 set rule 2 inside-address port 4500
 set rule 2 log disable
 set rule 2 protocol udp
 set rule 2 type destination
Verify L2TP
!---------!
sudo tcpdump -i eth0 -n udp dst port 4500 or port 500 or port 1701
show nat statistics
show nat rules 
#Zenmap for Windows
nmap -sU -p 500 <your-wan-ipaddress>
nmap -sU -p 4500 <your-wan-ipaddress>
================================================

File: Config.txt
================================================
Port Mirroring
===========================================
edit interfaces
 set ethernet eth1 address 10.0.0.1/24
 set ethernet eth1 description SOURCE
 set ethernet eth1 mirror eth0
 set ethernet eth0 description DESTINATION
================================================

File: Config.txt
================================================
Port Mirroring
===========================================
edit interfaces
 set ethernet eth1 address 10.0.0.1/24
 set ethernet eth1 description SOURCE
 set ethernet eth1 mirror eth0
 set ethernet eth0 description DESTINATION
================================================

File: Configuration.txt
================================================
PPPoE Client
!----------!
edit interfaces ethernet eth0 
 set pppoe 0 mtu 1492
 set pppoe 0 user-id ERX0
 set pppoe 0 password Pa$$w0rd
 set pppoe 0 name-server none
 set pppoe 0 default-route none
 set pppoe 0 firewall in name WAN_IN
 set pppoe 0 firewall local name WAN_LOCAL
set protocols static interface-route 0.0.0.0/0 next-hop-interface pppoe0
set system name-server 8.8.8.8
set system name-server 8.8.4.4
set firewall options mss-clamp mss 1452
Verify PPPoE Connection
!----------------------!
show interfaces pppoe pppoe0 log
clear interfaces connection pppoe0
connect interface pppoe0
================================================

File: Cisco VPN Config.txt
================================================
Default Interfaces
==================================================
interface gi0/0
 ip address 1.0.0.1 255.255.255.0
 no shutdown
interface gi1/0
 ip address 172.16.0.1 255.255.255.0
 no shutdown
ip route 0.0.0.0 0.0.0.0 1.0.0.2
Crypto VPN
================================================
crypto isakmp policy 10
 encr aes
 hash md5
 authentication pre-share
 group 14
 lifetime 28800
crypto isakmp key Pa$$w0rd address 2.0.0.1        
crypto ipsec transform-set TS esp-aes esp-md5-hmac 
 mode tunnel
crypto ipsec profile IPSEC
 set transform-set TS  
 set security-association lifetime seconds 3600
VTI Interface
================================================== 
interface tun0
 ip add 12.0.0.1 255.255.255.252
 ip mtu 1400
 tunnel source 1.0.0.1
 tunnel destination 2.0.0.1
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile IPSEC
RIP
==================================================
router rip
 version 2
 no auto-summary
 network 12.0.0.0 
 network 172.16.0.0 
 neighbor 12.0.0.2
Verify 
==================================================
show crypto isakmp sa
show crypto ipsec sa
show crypto engine connections active
debug crypto isakmp
================================================

File: Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VTI Interface
==================================================
set interfaces vti vti0 address 12.0.0.2/30 
set interfaces vti vti0 mtu 1400
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group FOO0 lifetime 28800 
 set ike-group FOO0 proposal 1 dh-group 14
 set ike-group FOO0 proposal 1 encryption aes128
 set ike-group FOO0 proposal 1 hash md5
 set esp-group FOO0 lifetime 3600
 set esp-group FOO0 proposal 1 encryption aes128
 set esp-group FOO0 proposal 1 hash md5
 set esp-group FOO0 mode tunnel
 set esp-group FOO0 pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set vti bind vti0
 set vti esp-group FOO0
RIP
==================================================
edit protocols rip
 set interface vti0
 set network 10.0.0.0/24
 set neighbor 12.0.0.1
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Cisco VPN Config.txt
================================================
Default Interfaces
==================================================
interface gi0/0
 ip address 1.0.0.1 255.255.255.0
 no shutdown
interface gi1/0
 ip address 172.16.0.1 255.255.255.0
 no shutdown
ip route 0.0.0.0 0.0.0.0 1.0.0.2
Crypto VPN
================================================
crypto isakmp policy 10
 encr aes
 hash md5
 authentication pre-share
 group 14
 lifetime 28800
crypto isakmp key Pa$$w0rd address 2.0.0.1        
crypto ipsec transform-set TS esp-aes esp-md5-hmac 
 mode tunnel
crypto ipsec profile IPSEC
 set transform-set TS  
 set security-association lifetime seconds 3600
VTI Interface
================================================== 
interface tun0
 ip add 12.0.0.1 255.255.255.252
 ip mtu 1400
 tunnel source 1.0.0.1
 tunnel destination 2.0.0.1
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile IPSEC
RIP
==================================================
router rip
 version 2
 no auto-summary
 network 12.0.0.0 
 network 172.16.0.0 
 neighbor 12.0.0.2
Verify 
==================================================
show crypto isakmp sa
show crypto ipsec sa
show crypto engine connections active
debug crypto isakmp
show ip protocols
show ip rip database
================================================

File: Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VTI Interface
==================================================
set interfaces vti vti0 address 12.0.0.2/30 
set interfaces vti vti0 mtu 1400
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group IKE lifetime 28800 
 set ike-group IKE proposal 1 dh-group 14
 set ike-group IKE proposal 1 encryption aes128
 set ike-group IKE proposal 1 hash md5
 set esp-group ESP lifetime 3600
 set esp-group ESP proposal 1 encryption aes128
 set esp-group ESP proposal 1 hash md5
 set esp-group ESP mode tunnel
 set esp-group ESP pfs disable
edit site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set vti bind vti0
 set vti esp-group ESP
RIP
==================================================
edit protocols rip
 set interface vti0
 set network 10.0.0.0/24
 set neighbor 12.0.0.1
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
show ip rip interface 
show ip rip
================================================

File: Configuration.txt
================================================
Create Basic Script
!-----------------!
sudo vi /config/scripts/dhcp
#!/bin/bash
run=/opt/vyatta/bin/vyatta-op-cmd-wrapper
$run release dhcp interface eth0
$run renew dhcp interface eth0
/bin/sleep 10
$run show interfaces
$run ping www.youtube.com
#Make script executable
chmod +x /config/scripts/dhcp
#Verify script
cat /config/scripts/dhcp
#Run script
/config/scripts/dhcp
================================================

File: Configuration.txt
================================================
Site-to-Site IPsec VPN
|--------------------|
edit vpn ipsec 
 set auto-firewall-nat-exclude enable
 set ike-group FOO0 lifetime 86400 
 set ike-group FOO0 proposal 1 dh-group 14
 set ike-group FOO0 proposal 1 encryption aes256
 set ike-group FOO0 proposal 1 hash sha256
 set ike-group FOO0 dead-peer-detection action restart
 set ike-group FOO0 dead-peer-detection interval 30
 set ike-group FOO0 dead-peer-detection timeout 120
 set esp-group FOO0 lifetime 43200
 set esp-group FOO0 proposal 1 encryption aes128
 set esp-group FOO0 proposal 1 hash md5
 set esp-group FOO0 mode tunnel
 set esp-group FOO0 pfs disable
edit vpn ipsec site-to-site peer 2.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type respond
 set local-address 1.0.0.1
 set ike-group FOO0
 set tunnel 1 esp-group FOO0
 set tunnel 1 local prefix 192.168.1.0/24
 set tunnel 1 remote prefix 10.0.0.0/24
Verify IPsec Tunnel
|-----------------|
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
sudo ipsec statusall
#Logs
show vpn log
#Reset connection
clear vpn ipsec-peer 2.0.0.1
sudo ipsec restart
#Verify StrongSwan
cat /etc/ipsec.conf 
Linux StrongSwan VPN
|------------------|
sudo apt-get install strongswan
sudo nano /etc/ipsec.conf
conn peer-1.0.0.1-tunnel-1
        left=1.0.0.1
        right=2.0.0.1
        leftsubnet=192.168.1.0/24
        rightsubnet=10.0.0.0/24
        ike=aes256-sha256-modp2048!
        keyexchange=ikev1
        aggressive=no
        ikelifetime=86400s
        dpddelay=30s
        dpdtimeout=120s
        dpdaction=restart
        esp=aes128-md5!
        keylife=43200s
        rekeymargin=540s
        type=tunnel
        compress=no
        authby=secret
        auto=route
        keyingtries=1
sudo nano /etc/ipsec.secrets
	2.0.0.1 1.0.0.1 : PSK "Pa$$w0rd"
#Enable routing between interfaces
echo 1 > /proc/sys/net/ipv4/ip_forward
Verify IPsec Tunnel
|-----------------|
sudo ipsec statusall
grep -a charon /var/log/auth.log
#Reset connection
sudo ipsec restart
================================================

File: Cisco VPN Config.txt
================================================
Interfaces
==================================================
interface gi0/0
 ip address 1.0.0.1 255.255.255.0
 no shutdown
interface gi1/0
 ip address 172.16.0.1 255.255.255.0
 no shutdown
ip route 0.0.0.0 0.0.0.0 1.0.0.2
Crypto Map VPN
================================================
crypto isakmp policy 10
 encr aes
 hash md5
 authentication pre-share
 group 14
 lifetime 28800
crypto isakmp key Pa$$w0rd address 2.0.0.1        
crypto ipsec transform-set TS esp-aes esp-md5-hmac 
 mode tunnel
crypto map CMAP 10 ipsec-isakmp 
 set peer 2.0.0.1
 set transform-set TS 
 match address VPN
 set security-association lifetime seconds 3600
ip access-list extended VPN 
 permit ip 172.16.0.0 0.0.0.255 10.0.0.0 0.0.0.255
int g0/0 
 crypto map CMAP
Verify 
==================================================
show crypto isakmp sa
show crypto ipsec sa
show crypto engine connections active
debug crypto isakmp
================================================

File: Config.txt
================================================
Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group FOO0 lifetime 28800 
 set ike-group FOO0 proposal 1 dh-group 14
 set ike-group FOO0 proposal 1 encryption aes128
 set ike-group FOO0 proposal 1 hash md5
 set esp-group FOO0 lifetime 3600
 set esp-group FOO0 proposal 1 encryption aes128
 set esp-group FOO0 proposal 1 hash md5
 set esp-group FOO0 mode tunnel
 set esp-group FOO0 pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group FOO0
 set tunnel 1 esp-group FOO0
 set tunnel 1 local prefix 10.0.0.0/24
 set tunnel 1 remote prefix 172.16.0.0/24
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Cisco VPN Config.txt
================================================
Interfaces
==================================================
interface gi0/0
 ip address 1.0.0.1 255.255.255.0
 no shutdown
interface gi1/0
 ip address 172.16.0.1 255.255.255.0
 no shutdown
ip route 0.0.0.0 0.0.0.0 1.0.0.2
Crypto Map VPN
================================================
crypto isakmp policy 10
 encr aes
 hash md5
 authentication pre-share
 group 14
 lifetime 28800
crypto isakmp key Pa$$w0rd address 2.0.0.1        
crypto ipsec transform-set TS esp-aes esp-md5-hmac 
 mode tunnel
crypto map CMAP 10 ipsec-isakmp 
 set peer 2.0.0.1
 set transform-set TS 
 match address VPN
 set security-association lifetime seconds 3600
ip access-list extended VPN 
 permit ip 172.16.0.0 0.0.0.255 10.0.0.0 0.0.0.255
int g0/0 
 crypto map CMAP
Verify 
==================================================
show crypto isakmp sa
show crypto ipsec sa
show crypto engine connections active
debug crypto isakmp
================================================

File: Config.txt
================================================
Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group IKE lifetime 28800 
 set ike-group IKE proposal 1 dh-group 14
 set ike-group IKE proposal 1 encryption aes128
 set ike-group IKE proposal 1 hash md5
 set esp-group ESP lifetime 3600
 set esp-group ESP proposal 1 encryption aes128
 set esp-group ESP proposal 1 hash md5
 set esp-group ESP mode tunnel
 set esp-group ESP pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set tunnel 1 esp-group ESP
 set tunnel 1 local prefix 10.0.0.0/24
 set tunnel 1 remote prefix 172.16.0.0/24
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Cisco VPN Config.txt
================================================
Interfaces
==================================================
interface gi0/0
 ip address 1.0.0.1 255.255.255.0
 no shutdown
interface gi1/0
 ip address 172.16.0.1 255.255.255.0
 no shutdown
ip route 0.0.0.0 0.0.0.0 1.0.0.2
Crypto Map VPN
================================================
crypto isakmp policy 10
 encr aes 
 hash md5
 authentication pre-share
 group 14
 lifetime 28800
crypto isakmp key Pa$$w0rd address 2.0.0.1        
crypto ipsec transform-set TS esp-aes esp-md5-hmac 
 mode tunnel
crypto map CMAP 10 ipsec-isakmp 
 set peer 2.0.0.1
 set transform-set TS 
 match address VPN
 set security-association lifetime seconds 3600
ip access-list extended VPN 
 permit ip 172.16.0.0 0.0.0.255 10.0.0.0 0.0.0.255
int g0/0 
 crypto map CMAP
Verify 
==================================================
show crypto isakmp sa
show crypto ipsec sa
show crypto engine connections active
debug crypto isakmp
================================================

File: Config.txt
================================================
Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group FOO0 lifetime 28800 
 set ike-group FOO0 proposal 1 dh-group 14
 set ike-group FOO0 proposal 1 encryption aes128
 set ike-group FOO0 proposal 1 hash md5
 set esp-group FOO0 lifetime 3600
 set esp-group FOO0 proposal 1 encryption aes128
 set esp-group FOO0 proposal 1 hash md5
 set esp-group FOO0 mode tunnel
 set esp-group FOO0 pfs disable
 set auto-firewall-nat-exclude enable 
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group FOO0
 set tunnel 1 esp-group FOO0
 set tunnel 1 local prefix 10.0.0.0/24
 set tunnel 1 remote prefix 172.16.0.0/24
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Cisco VPN Config.txt
================================================
Interfaces
==================================================
interface gi0/0
 ip address 1.0.0.1 255.255.255.0
 no shutdown
interface gi1/0
 ip address 172.16.0.1 255.255.255.0
 no shutdown
ip route 0.0.0.0 0.0.0.0 1.0.0.2
Crypto Map VPN
================================================
crypto isakmp policy 10
 encr aes
 hash md5
 authentication pre-share
 group 14
 lifetime 28800
crypto isakmp key Pa$$w0rd address 2.0.0.1        
crypto ipsec transform-set TS esp-aes esp-md5-hmac 
 mode tunnel
crypto map CMAP 10 ipsec-isakmp 
 set peer 2.0.0.1
 set transform-set TS 
 match address VPN
 set security-association lifetime seconds 3600
ip access-list extended VPN 
 permit ip 172.16.0.0 0.0.0.255 10.0.0.0 0.0.0.255
int g0/0 
 crypto map CMAP
Verify 
==================================================
show crypto isakmp sa
show crypto ipsec sa
show crypto engine connections active
debug crypto isakmp
================================================

File: Config.txt
================================================
Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group IKE lifetime 28800 
 set ike-group IKE proposal 1 dh-group 14
 set ike-group IKE proposal 1 encryption aes128
 set ike-group IKE proposal 1 hash md5
 set esp-group ESP lifetime 3600
 set esp-group ESP proposal 1 encryption aes128
 set esp-group ESP proposal 1 hash md5
 set esp-group ESP mode tunnel
 set esp-group ESP pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set tunnel 1 esp-group ESP
 set tunnel 1 local prefix 10.0.0.0/24
 set tunnel 1 remote prefix 172.16.0.0/24
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Config.txt
================================================
Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group FOO0 lifetime 28800 
 set ike-group FOO0 proposal 1 dh-group 14
 set ike-group FOO0 proposal 1 encryption aes128
 set ike-group FOO0 proposal 1 hash md5
 set esp-group FOO0 lifetime 3600
 set esp-group FOO0 proposal 1 encryption aes128
 set esp-group FOO0 proposal 1 hash md5
 set esp-group FOO0 mode tunnel
 set esp-group FOO0 pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group FOO0
 set tunnel 1 esp-group FOO0
 set tunnel 1 local prefix 10.0.0.0/24
 set tunnel 1 remote prefix 172.16.0.0/24
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Juniper VPN Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set fe-0/0/0 unit 0 family inet address 1.0.0.1/24
 set fe-0/0/1 unit 0 family inet address 172.16.0.1/24
set routing-options static route 0.0.0.0/0 next-hop 1.0.0.2
VTI Interfaces
==================================================
set interfaces st0.0 family inet 
set routing-options static route 10.0.0.0/24 next-hop st0.0
VPN Tunnel
================================================
edit security 
 set ike proposal IKE authentication-method pre-shared-keys
 set ike proposal IKE dh-group group14
 set ike proposal IKE authentication-algorithm md5
 set ike proposal IKE encryption-algorithm aes-128-cbc
 set ike proposal IKE lifetime-seconds 28800
 set ike policy IKE_POLICY mode main
 set ike policy IKE_POLICY proposals IKE
 set ike policy IKE_POLICY pre-shared-key ascii-text Pa$$w0rd
 set ike gateway IKE_GATEWAY ike-policy IKE_POLICY
 set ike gateway IKE_GATEWAY address 2.0.0.1
 set ike gateway IKE_GATEWAY external-interface fe-0/0/0
 set ike gateway IKE_GATEWAY local-address 1.0.0.1 
 set ipsec proposal ESP protocol esp
 set ipsec proposal ESP authentication-algorithm hmac-md5-96
 set ipsec proposal ESP encryption-algorithm aes-128-cbc
 set ipsec proposal ESP lifetime-seconds 3600
 set ipsec policy ESP_POLICY proposals ESP
 set ipsec vpn ESP_VPN bind-interface st0.0 
 set ipsec vpn ESP_VPN ike gateway IKE_GATEWAY
 set ipsec vpn ESP_VPN ike ipsec-policy ESP_POLICY
 set ipsec vpn ESP_VPN establish-tunnels immediately
 set ipsec vpn ESP_VPN ike proxy-identity local 172.16.0.0/24
 set ipsec vpn ESP_VPN ike proxy-identity remote 10.0.0.0/24
 set ipsec vpn ESP_VPN ike proxy-identity service any
Security Settings
==================================================
set security zones security-zone trust interfaces st0.0
edit security policies from-zone trust to-zone trust 
 set policy trust-to-trust match source-address any
 set policy trust-to-trust match destination-address any
 set policy trust-to-trust match application any
 set policy trust-to-trust then permit
Verify 
==================================================
show security ike security-associations
show security ike security-associations detail
show security ipsec sa
show security ipsec sa detail
show security ipsec statistics
================================================

File: Config.txt
================================================
Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group IKE lifetime 28800 
 set ike-group IKE proposal 1 dh-group 14
 set ike-group IKE proposal 1 encryption aes128
 set ike-group IKE proposal 1 hash md5
 set esp-group ESP lifetime 3600
 set esp-group ESP proposal 1 encryption aes128
 set esp-group ESP proposal 1 hash md5
 set esp-group ESP mode tunnel
 set esp-group ESP pfs disable
edit site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set tunnel 1 esp-group ESP
 set tunnel 1 local prefix 10.0.0.0/24
 set tunnel 1 remote prefix 172.16.0.0/24
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Juniper VPN Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set fe-0/0/0 unit 0 family inet address 1.0.0.1/24
 set fe-0/0/1 unit 0 family inet address 172.16.0.1/24
set routing-options static route 0.0.0.0/0 next-hop 1.0.0.2
VTI Interfaces
==================================================
set interfaces st0.0 family inet 
set routing-options static route 10.0.0.0/24 next-hop st0.0
VPN Tunnel
================================================
edit security 
 set ike proposal IKE authentication-method pre-shared-keys
 set ike proposal IKE dh-group group14
 set ike proposal IKE authentication-algorithm md5
 set ike proposal IKE encryption-algorithm aes-128-cbc
 set ike proposal IKE lifetime-seconds 28800
 set ike policy IKE_POLICY mode main
 set ike policy IKE_POLICY proposals IKE
 set ike policy IKE_POLICY pre-shared-key ascii-text Pa$$w0rd
 set ike gateway IKE_GATEWAY ike-policy IKE_POLICY
 set ike gateway IKE_GATEWAY address 2.0.0.1
 set ike gateway IKE_GATEWAY external-interface fe-0/0/0
 set ike gateway IKE_GATEWAY local-address 1.0.0.1 
 set ipsec proposal ESP protocol esp
 set ipsec proposal ESP authentication-algorithm hmac-md5-96
 set ipsec proposal ESP encryption-algorithm aes-128-cbc
 set ipsec proposal ESP lifetime-seconds 3600
 set ipsec policy ESP_POLICY proposals ESP
 set ipsec vpn ESP_VPN bind-interface st0.0 
 set ipsec vpn ESP_VPN ike gateway IKE_GATEWAY
 set ipsec vpn ESP_VPN ike ipsec-policy ESP_POLICY
 set ipsec vpn ESP_VPN establish-tunnels immediately
 set ipsec vpn ESP_VPN ike proxy-identity local 172.16.0.0/24
 set ipsec vpn ESP_VPN ike proxy-identity remote 10.0.0.0/24
 set ipsec vpn ESP_VPN ike proxy-identity service any
Security Settings
==================================================
set security zones security-zone trust interfaces st0.0
edit security policies from-zone trust to-zone trust 
 set policy trust-to-trust match source-address any
 set policy trust-to-trust match destination-address any
 set policy trust-to-trust match application any
 set policy trust-to-trust then permit
Verify 
==================================================
show security ike security-associations
show security ike security-associations detail
show security ipsec sa
show security ipsec sa detail
show security ipsec statistics
================================================

File: Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VTI Interface
==================================================
set interfaces vti vti0 address 12.0.0.2/30 
set interfaces vti vti0 mtu 1400
edit protocols static 
 set route 172.16.0.0/24 next-hop 12.0.0.1 
 set interface-route 172.16.0.0/24 next-hop-interface vti0
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group FOO0 lifetime 28800 
 set ike-group FOO0 proposal 1 dh-group 14
 set ike-group FOO0 proposal 1 encryption aes128
 set ike-group FOO0 proposal 1 hash md5
 set esp-group FOO0 lifetime 3600
 set esp-group FOO0 proposal 1 encryption aes128
 set esp-group FOO0 proposal 1 hash md5
 set esp-group FOO0 mode tunnel
 set esp-group FOO0 pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set vti bind vti0
 set vti esp-group FOO0
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Juniper VPN Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set fe-0/0/0 unit 0 family inet address 1.0.0.1/24
 set fe-0/0/1 unit 0 family inet address 172.16.0.1/24
set routing-options static route 0.0.0.0/0 next-hop 1.0.0.2
VTI Interface
================================================== 
edit interfaces
 set st0 unit 0 family inet mtu 1400
 set st0 unit 0 family inet address 12.0.0.1/30
set routing-options static route 10.0.0.0/24 next-hop 12.0.0.2
VPN Tunnel
================================================
edit security ike
 set ike proposal IKE authentication-method pre-shared-keys
 set ike proposal IKE dh-group group14
 set ike proposal IKE authentication-algorithm md5
 set ike proposal IKE encryption-algorithm aes-128-cbc
 set ike proposal IKE lifetime-seconds 28800
 set ike policy IKE_POLICY mode main
 set ike policy IKE_POLICY proposals IKE
 set ike policy IKE_POLICY pre-shared-key ascii-text Pa$$w0rd
 set ike gateway IKE_GATEWAY ike-policy IKE_POLICY
 set ike gateway IKE_GATEWAY address 2.0.0.1
 set ike gateway IKE_GATEWAY external-interface fe-0/0/0
 set ike gateway IKE_GATEWAY local-address 1.0.0.1
 set ipsec proposal ESP protocol esp
 set ipsec proposal ESP authentication-algorithm hmac-md5-96
 set ipsec proposal ESP encryption-algorithm aes-128-cbc
 set ipsec proposal ESP lifetime-seconds 3600
 set ipsec policy ESP_POLICY proposals ESP
 set ipsec vpn ESP_VPN bind-interface st0.0
 set ipsec vpn ESP_VPN ike gateway IKE_GATEWAY
 set ipsec vpn ESP_VPN ike ipsec-policy ESP_POLICY
 set ipsec vpn ESP_VPN establish-tunnels immediately
Security Settings
==================================================
set security zones security-zone trust interfaces st0.0
edit security policies from-zone trust to-zone trust 
 set policy trust-to-trust match source-address any
 set policy trust-to-trust match destination-address any
 set policy trust-to-trust match application any
 set policy trust-to-trust then permit
Verify 
==================================================
show security ike security-associations
show security ike security-associations detail
show security ipsec sa
show security ipsec sa detail
show security ipsec statistics
================================================

File: Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VTI Interface
==================================================
set interfaces vti vti0 address 12.0.0.2/30 
set interfaces vti vti0 mtu 1400
edit protocols static 
 set route 172.16.0.0/24 next-hop 12.0.0.1 
 set interface-route 172.16.0.0/24 next-hop-interface vti0
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group IKE lifetime 28800 
 set ike-group IKE proposal 1 dh-group 14
 set ike-group IKE proposal 1 encryption aes128
 set ike-group IKE proposal 1 hash md5
 set esp-group ESP lifetime 3600
 set esp-group ESP proposal 1 encryption aes128
 set esp-group ESP proposal 1 hash md5
 set esp-group ESP mode tunnel
 set esp-group ESP pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set vti bind vti0
 set vti esp-group ESP
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Juniper VPN Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set fe-0/0/0 unit 0 family inet address 1.0.0.1/24
 set fe-0/0/1 unit 0 family inet address 172.16.0.1/24
set routing-options static route 0.0.0.0/0 next-hop 1.0.0.2
VTI Interface
================================================== 
edit interfaces
 set st0 unit 0 family inet mtu 1400
 set st0 unit 0 family inet address 12.0.0.1/30
set routing-options static route 10.0.0.0/24 next-hop 12.0.0.2
VPN Tunnel
================================================
edit security 
 set ike proposal IKE authentication-method pre-shared-keys
 set ike proposal IKE dh-group group14
 set ike proposal IKE authentication-algorithm md5
 set ike proposal IKE encryption-algorithm aes-128-cbc
 set ike proposal IKE lifetime-seconds 28800
 set ike policy IKE_POLICY mode main
 set ike policy IKE_POLICY proposals IKE
 set ike policy IKE_POLICY pre-shared-key ascii-text Pa$$w0rd
 set ike gateway IKE_GATEWAY ike-policy IKE_POLICY
 set ike gateway IKE_GATEWAY address 2.0.0.1
 set ike gateway IKE_GATEWAY external-interface fe-0/0/0
 set ike gateway IKE_GATEWAY local-address 1.0.0.1
 set ipsec proposal ESP protocol esp
 set ipsec proposal ESP authentication-algorithm hmac-md5-96
 set ipsec proposal ESP encryption-algorithm aes-128-cbc
 set ipsec proposal ESP lifetime-seconds 3600
 set ipsec policy ESP_POLICY proposals ESP
 set ipsec vpn ESP_VPN bind-interface st0.0
 set ipsec vpn ESP_VPN ike gateway IKE_GATEWAY
 set ipsec vpn ESP_VPN ike ipsec-policy ESP_POLICY
 set ipsec vpn ESP_VPN establish-tunnels immediately
Security Settings
==================================================
set security zones security-zone trust interfaces st0.0
edit security policies from-zone trust to-zone trust 
 set policy trust-to-trust match source-address any
 set policy trust-to-trust match destination-address any
 set policy trust-to-trust match application any
 set policy trust-to-trust then permit
Verify 
==================================================
show security ike security-associations
show security ike security-associations detail
show security ipsec sa
show security ipsec sa detail
show security ipsec statistics
================================================

File: Cisco VPN Config.txt
================================================
Default Interfaces
==================================================
interface gi0/0
 ip address 1.0.0.1 255.255.255.0
 no shutdown
interface gi1/0
 ip address 172.16.0.1 255.255.255.0
 no shutdown
ip route 0.0.0.0 0.0.0.0 1.0.0.2
Crypto VPN
================================================
crypto isakmp policy 10
 encr aes
 hash md5
 authentication pre-share
 group 14
 lifetime 28800
crypto isakmp key Pa$$w0rd address 2.0.0.1        
crypto ipsec transform-set TS esp-aes esp-md5-hmac 
 mode tunnel
crypto ipsec profile IPSEC
 set transform-set TS  
 set security-association lifetime seconds 3600
VTI Interface
================================================== 
interface tun0
 ip add 12.0.0.1 255.255.255.252
 ip mtu 1400
 tunnel source 1.0.0.1
 tunnel destination 2.0.0.1
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile IPSEC
ip route 10.0.0.0 255.255.255.0 12.0.0.2
Verify 
==================================================
show crypto isakmp sa
show crypto ipsec sa
show crypto engine connections active
debug crypto isakmp
================================================

File: Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VTI Interface
==================================================
set interfaces vti vti0 address 12.0.0.2/30 
set interfaces vti vti0 mtu 1400
edit protocols static 
 set route 172.16.0.0/24 next-hop 12.0.0.1 
 set interface-route 172.16.0.0/24 next-hop-interface vti0
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group FOO0 lifetime 28800 
 set ike-group FOO0 proposal 1 dh-group 14
 set ike-group FOO0 proposal 1 encryption aes128
 set ike-group FOO0 proposal 1 hash md5
 set esp-group FOO0 lifetime 3600
 set esp-group FOO0 proposal 1 encryption aes128
 set esp-group FOO0 proposal 1 hash md5
 set esp-group FOO0 mode tunnel
 set esp-group FOO0 pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set vti bind vti0
 set vti esp-group FOO0
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Cisco VPN Config.txt
================================================
Default Interfaces
==================================================
interface gi0/0
 ip address 1.0.0.1 255.255.255.0
 no shutdown
interface gi1/0
 ip address 172.16.0.1 255.255.255.0
 no shutdown
ip route 0.0.0.0 0.0.0.0 1.0.0.2
Crypto VPN
================================================
crypto isakmp policy 10
 encr aes
 hash md5
 authentication pre-share
 group 14
 lifetime 28800
crypto isakmp key Pa$$w0rd address 2.0.0.1        
crypto ipsec transform-set TS esp-aes esp-md5-hmac 
 mode tunnel
crypto ipsec profile IPSEC
 set transform-set TS  
 set security-association lifetime seconds 3600
VTI Interface
================================================== 
interface tun0
 ip add 12.0.0.1 255.255.255.252
 ip mtu 1400
 tunnel source 1.0.0.1
 tunnel destination 2.0.0.1
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile IPSEC
ip route 10.0.0.0 255.255.255.0 12.0.0.2
Verify 
==================================================
show crypto isakmp sa
show crypto ipsec sa
show crypto engine connections active
debug crypto isakmp
================================================

File: Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VTI Interface
==================================================
set interfaces vti vti0 address 12.0.0.2/30 
set interfaces vti vti0 mtu 1400
edit protocols static 
 set route 172.16.0.0/24 next-hop 12.0.0.1 
 set interface-route 172.16.0.0/24 next-hop-interface vti0
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group IKE lifetime 28800 
 set ike-group IKE proposal 1 dh-group 14
 set ike-group IKE proposal 1 encryption aes128
 set ike-group IKE proposal 1 hash md5
 set esp-group ESP lifetime 3600
 set esp-group ESP proposal 1 encryption aes128
 set esp-group ESP proposal 1 hash md5
 set esp-group ESP mode tunnel
 set esp-group ESP pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set vti bind vti0
 set vti esp-group ESP
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VTI Interface
==================================================
set interfaces vti vti0 address 12.0.0.2/30 
set interfaces vti vti0 mtu 1400
edit protocols static 
 set route 172.16.0.0/24 next-hop 12.0.0.1 
 set interface-route 172.16.0.0/24 next-hop-interface vti0
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group FOO0 lifetime 28800 
 set ike-group FOO0 proposal 1 dh-group 14
 set ike-group FOO0 proposal 1 encryption aes128
 set ike-group FOO0 proposal 1 hash md5
 set esp-group FOO0 lifetime 3600
 set esp-group FOO0 proposal 1 encryption aes128
 set esp-group FOO0 proposal 1 hash md5
 set esp-group FOO0 mode tunnel
 set esp-group FOO0 pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set vti bind vti0
 set vti esp-group FOO0
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Juniper VPN Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set fe-0/0/0 unit 0 family inet address 1.0.0.1/24
 set fe-0/0/1 unit 0 family inet address 172.16.0.1/24
set routing-options static route 0.0.0.0/0 next-hop 1.0.0.2
VTI Interface
================================================== 
edit interfaces
 set st0 unit 0 family inet mtu 1400
 set st0 unit 0 family inet address 12.0.0.1/30
set routing-options static route 10.0.0.0/24 next-hop 12.0.0.2
VPN Tunnel
================================================
edit security
 set ike proposal IKE authentication-method pre-shared-keys
 set ike proposal IKE dh-group group14
 set ike proposal IKE authentication-algorithm md5
 set ike proposal IKE encryption-algorithm aes-128-cbc
 set ike proposal IKE lifetime-seconds 28800
 set ike policy IKE_POLICY mode main
 set ike policy IKE_POLICY proposals IKE
 set ike policy IKE_POLICY pre-shared-key ascii-text Pa$$w0rd
 set ike gateway IKE_GATEWAY ike-policy IKE_POLICY
 set ike gateway IKE_GATEWAY address 2.0.0.1
 set ike gateway IKE_GATEWAY external-interface fe-0/0/0
 set ike gateway IKE_GATEWAY local-address 1.0.0.1
 set ipsec proposal ESP protocol esp
 set ipsec proposal ESP authentication-algorithm hmac-md5-96
 set ipsec proposal ESP encryption-algorithm aes-128-cbc
 set ipsec proposal ESP lifetime-seconds 3600
 set ipsec policy ESP_POLICY proposals ESP
 set ipsec vpn ESP_VPN bind-interface st0.0
 set ipsec vpn ESP_VPN ike gateway IKE_GATEWAY
 set ipsec vpn ESP_VPN ike ipsec-policy ESP_POLICY
 set ipsec vpn ESP_VPN establish-tunnels immediately
Security Settings
==================================================
set security zones security-zone trust interfaces st0.0
edit security policies from-zone trust to-zone trust 
 set policy trust-to-trust match source-address any
 set policy trust-to-trust match destination-address any
 set policy trust-to-trust match application any
 set policy trust-to-trust then permit
Verify 
==================================================
show security ike security-associations
show security ike security-associations detail
show security ipsec sa
show security ipsec sa detail
show security ipsec statistics
================================================

File: Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
set protocols static route 0.0.0.0/0 next-hop 2.0.0.2 
VTI Interface
==================================================
set interfaces vti vti0 address 12.0.0.2/30 
set interfaces vti vti0 mtu 1400
edit protocols static 
 set route 172.16.0.0/24 next-hop 12.0.0.1 
 set interface-route 172.16.0.0/24 next-hop-interface vti0
VPN Tunnel
==================================================
edit vpn ipsec 
 set ike-group IKE lifetime 28800 
 set ike-group IKE proposal 1 dh-group 14
 set ike-group IKE proposal 1 encryption aes128
 set ike-group IKE proposal 1 hash md5
 set esp-group ESP lifetime 3600
 set esp-group ESP proposal 1 encryption aes128
 set esp-group ESP proposal 1 hash md5
 set esp-group ESP mode tunnel
 set esp-group ESP pfs disable
edit vpn ipsec site-to-site peer 1.0.0.1
 set authentication mode pre-shared-secret 
 set authentication pre-shared-secret Pa$$w0rd
 set description IPsecVPN
 set connection-type initiate
 set local-address 2.0.0.1
 set ike-group IKE
 set vti bind vti0
 set vti esp-group ESP
Verify 
==================================================
show vpn log
show vpn ipsec policy 
show vpn ipsec status
show vpn ipsec sa
================================================

File: Juniper VPN Config.txt
================================================
Default Interfaces
==================================================
edit interfaces
 set fe-0/0/0 unit 0 family inet address 1.0.0.1/24
 set fe-0/0/1 unit 0 family inet address 172.16.0.1/24
set routing-options static route 0.0.0.0/0 next-hop 1.0.0.2
VTI Interface
================================================== 
edit interfaces
 set st0 unit 0 family inet mtu 1400
 set st0 unit 0 family inet address 12.0.0.1/30
edit routing-options  
 set static route 10.0.0.0/24 next-hop 12.0.0.2
VPN Tunnel
================================================
edit security 
 set ike proposal IKE authentication-method pre-shared-keys
 set ike proposal IKE dh-group group14
 set ike proposal IKE authentication-algorithm md5
 set ike proposal IKE encryption-algorithm aes-128-cbc
 set ike proposal IKE lifetime-seconds 28800
 set ike policy IKE_POLICY mode main
 set ike policy IKE_POLICY proposals IKE
 set ike policy IKE_POLICY pre-shared-key ascii-text Pa$$w0rd
 set ike gateway IKE_GATEWAY ike-policy IKE_POLICY
 set ike gateway IKE_GATEWAY address 2.0.0.1
 set ike gateway IKE_GATEWAY external-interface fe-0/0/0
 set ike gateway IKE_GATEWAY local-address 1.0.0.1
 set ipsec proposal ESP protocol esp
 set ipsec proposal ESP authentication-algorithm hmac-md5-96
 set ipsec proposal ESP encryption-algorithm aes-128-cbc
 set ipsec proposal ESP lifetime-seconds 3600
 set ipsec policy ESP_POLICY proposals ESP
 set ipsec vpn ESP_VPN bind-interface st0.0
 set ipsec vpn ESP_VPN ike gateway IKE_GATEWAY
 set ipsec vpn ESP_VPN ike ipsec-policy ESP_POLICY
 set ipsec vpn ESP_VPN establish-tunnels immediately
Security Settings
==================================================
set security zones security-zone trust interfaces st0.0
edit security policies from-zone trust to-zone trust 
 set policy trust-to-trust match source-address any
 set policy trust-to-trust match destination-address any
 set policy trust-to-trust match application any
 set policy trust-to-trust then permit
Verify 
==================================================
show security ike security-associations
show security ike security-associations detail
show security ipsec sa
show security ipsec sa detail
show security ipsec statistics
================================================

File: Config.txt
================================================
SNMPv2c
==================================================
edit service snmp
 set community ABCDE12345ABCDE client 10.0.0.10
 set community ABCDE12345ABCDE authorization ro
 set listen-address 10.0.0.1 port 161
================================================

File: Config.txt
================================================
SNMPv3 AuthPriv (Authentication & Encryption)
==================================================
edit service snmp
 set listen-address 10.0.0.1 port 161
 set v3 view VIEW oid 1
 set v3 group SNMP view VIEW
 set v3 group SNMP mode ro
 set v3 group SNMP seclevel priv
 set v3 user USER group SNMP
 set v3 user USER mode ro
 set v3 user USER auth plaintext-key Pa$$w0rd
 set v3 user USER auth type sha
 set v3 user USER privacy plaintext-key Pa$$w0rd
 set v3 user USER privacy type aes
================================================

File: Config.txt
================================================
Port Address Translation (Masquerade)
=====================================
edit service nat rule 5000
 set description MASQUERADE
 set log disable
 set outbound-interface eth0
 set protocol all
 set source address 10.0.0.0/24
 set type masquerade
================================================

File: Config.txt
================================================
Port Address Translation (Masquerade)
=====================================
edit service nat rule 5000
 set description MASQUERADE
 set log disable
 set outbound-interface eth0
 set protocol all
 set source address 10.0.0.0/24
 set type masquerade
================================================

File: Configuration.txt
================================================
iPerf3 Server (Receiver)
!---------------------!
-s = Run in server mode
-p = Port (5201 by default)
-f = Format
	 k - Kbits
	 m - Mbits
	 K - Kytes
	 M - MBytes
#Run default	 
iperf3 -s -f m
#Listen on port 5555
iperf3 -s -p 5555 -f m
iPerf3 Client (Sender)
!-------------------!
-c = Run in client mode and specify remote ip
-p = Port (5201 by default)
-f = Format
	 k - Kbits
	 m - Mbits
	 K - Kytes
	 M - MBytes
-P = Number of parallel streams (TCP only)
-u = Test with UDP instead of TCP
-i = Interval (1 second is default)
-t = Testing time (default is 10)
#Run default
iperf3 -c 192.168.1.1 -f m
#Run 5 parallel streams on port 5555
iperf3 -c 192.168.1.1 -f m -p 5555 -P 5
#Run UDP for 10 seconds with 2 second interval
iPerf3 -c 192.168.1.1 -f m -u -i 2 -t 10
Dual Bidirectional Test (iPerf2 only)
!-----------------------!
#First install iPerf2
#Add the Wheezy Debian repositories
set system package repository wheezy components 'main contrib non-free'
set system package repository wheezy distribution wheezy 
set system package repository wheezy url http://http.us.debian.org/debian
sudo apt-get install iperf
#Server
iperf -s -f m -i 1
#Client
iperf -c 192.168.1.1 -f m -i 1 -d
================================================

File: Configuration.txt
================================================
iPerf3 Server (Receiver)
!---------------------!
-s = Run in server mode
-p = Port (5201 by default)
-f = Format
	 k - Kbits
	 m - Mbits
	 K - Kytes
	 M - MBytes
#Run default	 
iperf3 -s -f m
#Listen on port 5555
iperf3 -s -p 5555 -f m
iPerf3 Client (Sender)
!-------------------!
-c = Run in client mode and specify remote ip
-p = Port (5201 by default)
-f = Format
	 k - Kbits
	 m - Mbits
	 K - Kytes
	 M - MBytes
-P = Number of parallel streams (TCP only)
-u = Test with UDP instead of TCP
-i = Interval (1 second is default)
-t = Testing time (default is 10)
#Run default
iperf3 -c 192.168.1.1 -f m
#Run 5 parallel streams on port 5555
iperf3 -c 192.168.1.1 -f m -p 5555 -P 5
#Run UDP for 10 seconds with 2 second interval
iPerf3 -c 192.168.1.1 -f m -u -i 2 -t 10
================================================

File: Config.txt
================================================
Add Speedtest Script
!------------------!
sudo su
curl -O /config/scripts/ https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
#Make script executable
chmod +x speedtest.py
#Move script
mv speedtest.py /config/scripts
#Run script
/config/scripts/speedtest.py
================================================

File: Config.txt
================================================
Disable SSH Password Authentication
====================================
edit service ssh 
 set disable-password-authentication
Load RSA Public Key
==================================== 
loadkey bpin ~/PASS.pub
loadkey bpin ~/NOPASS.pub
================================================

File: Config.txt
================================================
Port Address Translation (Masquerade)
=====================================
edit service nat rule 5000
 set description MASQUERADE
 set log disable
 set outbound-interface eth0
 set protocol all
 set source address 10.0.0.0/24
 set type masquerade
Static 1:1 Source NAT
==================================================
edit service nat rule 5001
 set description STATIC
 set log disable
 set outbound-interface eth0
 set protocol all
 set outside-address address 2.0.0.100/32
 set source address 10.0.0.100/32
 set type source
================================================

File: Config.txt
================================================
Port Address Translation (Masquerade)
=====================================
edit service nat rule 5000
 set description MASQUERADE
 set log disable
 set outbound-interface eth0
 set protocol all
 set source address 10.0.0.0/24
 set type masquerade
Static 1:1 Source NAT
==================================================
edit service nat rule 5001
 set description STATIC
 set log disable
 set outbound-interface eth0
 set protocol all
 set outside-address address 2.0.0.100/32
 set source address 10.0.0.100/32
 set type source
================================================

File: Config.txt
================================================
Default Logging
==================================================
edit system syslog
 delete global facility protocols 
 set global facility all level debug
show log | no-more
cat /var/log/messages
sudo -i
ls -l /var/log/
Custom File Logging
==================================================
Stored in /var/log/user
edit system syslog
 set file AUTH facility auth level debug
 set file ALL facility all level debug
show log file AUTH 
cat /var/log/user/AUTH
Remote Syslog Logging	  
==================================================
edit system syslog
  set host 192.168.1.99 facility all level debug
================================================

File: Configuration.txt
================================================
Traffic Analysis with DPI
|-----------------------|
set system traffic-analysis dpi enable
set system traffic-analysis export enable
#Verify
show ubnt offload
Block Category
|-------------|
#See which sites are grouped under 'social networks' 
/usr/sbin/ubnt-dpi-util show-cat-apps Social-Network
#See which category a specific site is grouped under
/usr/sbin/ubnt-dpi-util search-app facebook
/usr/sbin/ubnt-dpi-util search-app twitter
#View all categories via CLI
set firewall name WAN_LOCAL rule 10 application category ?
#View all categories via GUI
Firewall Policies > WAN_LOCAL Actions > Advanced > Application
#Drop rule for social networks
edit firewall name SOCIAL_NETWORK
 set default-action accept
 set rule 10 description DROP_SOCIAL_SITES
 set rule 10 application category Social-Network
 set rule 10 action drop
top
#Apply to LAN interface
set interfaces switch switch0 firewall in name SOCIAL_NETWORK
commit
Block Custom Categories
|---------------------|
#Combine existing applications in a custom category
edit system traffic-analysis 
 set custom-category BLOCKED_SITES name Facebook
 set custom-category BLOCKED_SITES name Twitter
top 
#Drop rule for custom category
edit firewall name SOCIAL_NETWORK
 set default-action accept
 set rule 10 description DROP_BLOCKED_SITES 
 set rule 10 application category BLOCKED_SITES
 set rule 10 action drop
top
#Apply to LAN interface
set interfaces switch switch0 firewall in name BLOCKED_SITES
commit
Block Category & Allow Certain Apps
|---------------------------------|
#Combine existing applications in a custom category
edit system traffic-analysis 
 set custom-category ALLOWED_SITES name linkedin
 set custom-category ALLOWED_SITES name yammer
top 
#Drop rule for custom category
edit firewall name SOCIAL_NETWORK
 set default-action accept
 set rule 10 description ALLOWED_SOCIAL_SITES
 set rule 10 application category ALLOWED_SITES
 set rule 10 action accept 
 set rule 20 description DROP_SOCIAL_SITES
 set rule 20 application category Social-Network
 set rule 20 action drop
top
#Apply to LAN interface
set interfaces switch switch0 firewall in name SOCIAL_NETWORK
commit
================================================

File: Configuration.txt
================================================
Temporary Management Connection (Optional)
!----------------------------------------!
delete interfaces switch switch0 switch-port interface eth3
set interfaces ethernet eth3 address 172.16.0.1/24
#On PC, configure static IP:
Address	: 172.16.0.10
Mask	: 255.255.255.0
Gateway	: -
#Patch into Eth3 and navigate to:
https://172.16.0.1
VIF & PVID Interfaces
!-------------------!
edit interfaces switch switch0
 delete address 192.168.1.1/24
 set vif 1 address 192.168.1.1/24
 set vif 10 address 10.0.0.1/24
 set switch-port interface eth1 vlan pvid 1
 set switch-port interface eth2 vlan pvid 1
 set switch-port interface eth4 vlan pvid 1
 set switch-port interface eth4 vlan vid 10
 set switch-port vlan-aware enable
 set mtu 1500
 top 
set interfaces ethernet eth4 poe output pthru  
#After config you can patch back into Eth1  
#Set PC back to DHCP and remove Eth3 config
delete interfaces ethernet eth3 address 172.16.0.1/24
set interfaces switch switch0 switch-port interface eth3 vlan pvid 1
GUEST_TO_LAN Firewall Policy
!--------------------------!
edit firewall group network-group LAN
 set network 192.168.0.0/16
 set network 172.16.0.0/12
 set network 10.0.0.0/8
top 
edit firewall name GUEST_TO_LAN 
 set default-action accept
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
 set rule 2 action drop
 set rule 2 description LAN_RANGES
 set rule 2 log disable
 set rule 2 protocol all
 set rule 2 destination group network-group LAN
GUEST_TO_LOCAL Firewall Policy
!----------------------------!
edit firewall name GUEST_TO_LOCAL
 set default-action drop
 set rule 1 action accept
 set rule 1 description DNS
 set rule 1 log disable
 set rule 1 protocol tcp_udp
 set rule 1 destination port 53
 set rule 2 action accept
 set rule 2 description DHCP
 set rule 2 log disable
 set rule 2 protocol udp
 set rule 2 destination port 67
 set rule 3 action accept
 set rule 3 description Established
 set rule 3 log disable
 set rule 3 protocol all
 set rule 3 state established enable
 set rule 3 state related enable 
WAN_TO_LAN Firewall Policy
!------------------------!
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
Apply Policies to Interfaces 
!--------------------------!
edit interfaces switch switch0 
 set vif 10 firewall in name GUEST_TO_LAN 
 set vif 10 firewall local name GUEST_TO_LOCAL
DHCP Settings
!-----------!
edit service dhcp-server shared-network-name GUEST 
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.50
 set subnet 10.0.0.0/24 lease 86400
edit service dhcp-server shared-network-name LAN 
 set subnet 192.168.1.0/24 default-router 192.168.1.1
 set subnet 192.168.1.0/24 dns-server 192.168.1.1
 set subnet 192.168.1.0/24 start 192.168.1.38 stop 192.168.1.243
 set subnet 192.168.1.0/24 lease 86400
DNS Forwarding
!------------!
edit service dns
 set forwarding listen-on switch0.1
 set forwarding listen-on switch0.10
 set forwarding cache-size 150
 set forwarding name-server 8.8.8.8
UniFi Configuration
!-----------------!
#Either use startup wizard (after install) or configure WLANs manually
Settings > Wireless Networks > WLAN Group Default > Create New WLAN
Name/SSID : GUEST 
Security  : Open or WPA
Policy    : Check or Uncheck 'Apply Guest Policies'
VLAN	  : Use VLAN with VLAN-id 10
#If you want the EdgeRouter to handle the policies (firewall rules), uncheck this
#If you leave this checked, then you don't need the GUEST_TO_LAN and GUEST_TO_LOCAL policies above
Name/SSID : LAN 
Security  : WPA
VLAN	  : No VLAN-id
#Management traffic from UAPs is always untagged
#In this case untagged traffic is put in VLAN 1 using the PVID (Native VLAN)
#(Optional) Disable DHCP server on Controller
Settings > Networks > LAN > Uncheck 'Enable DHCP Server' (USG)
================================================

File: Configuration.txt
================================================
AWS Launch Instance
!------------------!
1. Services > Compute EC2 > Launch Instance
   Ubuntu Server 16.04 LTS (HVM), SSD Volume Type
2. General Purpose > t2-micro (Free tier eligible)
3. Add storage (30 GB)
4. Review and Launch
5. Security Groups >  Edit security groups
TCP-22		SSH
TCP-8080	UAP > controller communication
TCP-8443	Controller GUI / API
TCP-8880	HTTP portal redirect
TCP-8843	HTTPS portal redirect
UDP-3478 	STUN
Allow the above from either:
   Anywhere 
   Custom range 
   My IP
6. Launch Instance
   Create a new key pair or use exisiting
   Download key pair
7. Assign Elastic IP (static)
   Services > Network & security > Elastic IPs
   Allocate new address > VPC
   Associate address > link to Ubuntu Server Instance
7. Connect to server using SSH and your key pair
   Use public DNS provided by AWS > description of Instance
   Add public key to SSH client of your choice
   Username in case of Ubuntu Server is ubuntu
   No password needed
Ubuntu Server Installation
!------------------------!
apt-get install apt-transport-https
Verify Ubuntu Installation
!------------------------!
#Verify networking
#Verify ntp & timezones
timedatectl status
timedatectl set-timezone Europe/Amsterdam
#Verify sudoers / root
cut -d: -f1 /etc/passwd
#Update & upgrade
apt-get update
apt-get upgrade
UniFi Installation
!----------------!
nano /etc/apt/sources.list
#UniFi
deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti
tail /etc/apt/sources.list
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50
apt-get update
apt-get install unifi
Verify UniFi Installation
!-----------------------!
systemctl status unifi
https://amazonpublicdns....:8443
(Optional) Disable UniFi Update
!-----------------------!
apt-mark hold unifi
dpkg -l | grep unifi
apt-mark unhold unifi
Layer 3 (L3) Device Adoption
!--------------------------!
Install UniFi Discovery Utility on local PC
Discover APs/devices
manage > set url to http://aws-elastic-ip:8080/inform
	     set username/password to ubnt/ubnt
See my 'Layer 3 Device Adoption Methods' video/config file for other options
(Optional) Install Webmin
!-----------------------!
nano /etc/apt/sources.list
#Webmin
deb http://download.webmin.com/download/repository sarge contrib
deb http://webmin.mirror.somersettechsolutions.co.uk/repository sarge contrib
wget http://www.webmin.com/jcameron-key.asc
apt-key add jcameron-key.asc
apt-get update
apt-get install webmin
Optional (Verify Webmin)
!-----------------------!
systemctl status webmin
https://192.168.1.199:10000
================================================

File: Configuration.txt
================================================
Ubuntu Image & Login
!------------------!
https://wiki.ubuntu.com/ARM/RaspberryPi
ubuntu-16.04-preinstalled-server-armhf+raspi3.img.xz 
Username: ubuntu
Password: ubuntu
Ubuntu Installation
!-----------------!
adduser unifiadmin
visudo
unifiadmin    ALL=(ALL) ALL
nano /etc/ssh/sshd_config
PermitRootLogin no
UseDNS no
nano /etc/network/interfaces
auto eth0
iface eth0 inet static
    address 192.168.1.10
    netmask 255.255.255.0
    gateway 192.168.1.254
    dns-nameservers 192.168.1.254
echo UniFiController > /etc/hostname
nano /etc/hosts
127.0.1.1 UniFiController
reboot
userdel ubuntu
Verify Debian Installation
!------------------------!
Verify networking 
Verify ntp & timezones > timedatectl status
Verify sudoers / root
Update & upgrade
UniFi Installation
!----------------!
apt-get install apt-transport-https
nano /etc/apt/sources.list
#UniFi
deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti
tail /etc/apt/sources.list
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50
apt-get update
apt-get install unifi
Verify UniFi Installation
!-----------------------!
systemctl status unifi
https://192.168.1.10:8443
apt-get install nmap
nmap localhost
(Optional) Disable UniFi Update
!-----------------------!
apt-mark hold unifi
dpkg -l | grep unifi
apt-mark unhold unifi
Disable Default MongoDB Instance
!------------------------------|
systemctl stop unifi
service mongodb stop
echo 'ENABLE_MONGODB=no' | sudo tee -a /etc/mongodb.conf > /dev/null
Install Java 8 JDK Instance
!--------------------------
java -version
add-apt-repository ppa:webupd8team/java
apt-get update
apt-get install oracle-java8-installer
apt-get install oracle-java8-set-default
update-alternatives --config java
java -version
nano /etc/init.d/unifi
uncomment # set_java_home () {
...
}
JAVA_HOME=/usr/lib/jvm/java-8-oracle
reboot
(Optional) Rotate Log Files
!-------------------------!
apt-get install logrotate
nano /etc/logrotate.d/unifi
/var/log/unifi/*.log {
    rotate 5
    weekly
    missingok
    notifempty
    compress
    delaycompress
    copytruncate
}
(Optional) Install Webmin
!-----------------------!
nano /etc/apt/sources.list
#Webmin
deb http://download.webmin.com/download/repository sarge contrib
deb http://webmin.mirror.somersettechsolutions.co.uk/repository sarge contrib
wget http://www.webmin.com/jcameron-key.asc
apt-key add jcameron-key.asc
apt-get update
apt-get install webmin
Optional (Verify Webmin)
!-----------------------!
systemctl status webmin
https://192.168.1.10:10000
================================================

File: Configuration.txt
================================================
Ubuntu Image & Login
!------------------!
https://www.ubuntu.com/download/server
ubuntu-16.04.1-server-amd64.iso
#Make sure to install openssh-server package
apt-get install openssh-server
Ubuntu Installation
!-----------------!
adduser unifiadmin
visudo
unifiadmin    ALL=(ALL) ALL
nano /etc/ssh/sshd_config
PermitRootLogin no
UseDNS no
echo UniFiController > /etc/hostname
nano /etc/hosts
127.0.1.1 UniFiController
Ubuntu Networking
!-----------------------!
nano /etc/network/interfaces
auto ens33
iface ens33 inet static
    address 192.168.1.10
    netmask 255.255.255.0
    gateway 192.168.1.254
    dns-nameservers 192.168.1.254
reboot
#(Optional) change interface names
nano /etc/network/interfaces
auto eth0
iface eth0 inet static
    address 192.168.1.10
    netmask 255.255.255.0
    gateway 192.168.1.254
    dns-nameservers 192.168.1.254
nano /etc/default/grub 
GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0"
update-grub
Verify Debian Installation
!------------------------!
#Verify networking
#Verify ntp & timezones
timedatectl status
timedatectl set-timezone Europe/Amsterdam
#Verify sudoers / root
cut -d: -f1 /etc/passwd
#Update & upgrade
apt-get update
apt-get upgrade
UniFi Installation
!----------------!
apt-get install apt-transport-https
nano /etc/apt/sources.list
#UniFi
deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti
tail /etc/apt/sources.list
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50
apt-get update
apt-get install unifi
Verify UniFi Installation
!-----------------------!
systemctl status unifi
https://192.168.1.10:8443
apt-get install nmap
nmap localhost
(Optional) Disable UniFi Update
!-----------------------!
apt-mark hold unifi
dpkg -l | grep unifi
apt-mark unhold unifi
(Optional) Install Webmin
!-----------------------!
nano /etc/apt/sources.list
#Webmin
deb http://download.webmin.com/download/repository sarge contrib
deb http://webmin.mirror.somersettechsolutions.co.uk/repository sarge contrib
wget http://www.webmin.com/jcameron-key.asc
apt-key add jcameron-key.asc
apt-get update
apt-get install webmin
Optional (Verify Webmin)
!-----------------------!
systemctl status webmin
https://192.168.1.10:10000
================================================

File: Configuration.txt
================================================
Windows & UniFi Installation
!--------------------------!
#Set static IP address
#Install Java 8 RE
Default installation directory:
	%userprofile%\Ubiquiti UniFi
(optional) Move UniFi location:
	C:\Ubiquiti UniFi
Option #1 Run on System Startup
!-----------------------------!	
#Create a local admin account for UniFi (recommended)
#Open administrative command prompt (or use Control Panel)
	net user /add unifiadmin *
	net localgroup administrators unifiadmin /add
#Create a scheduled task
Task Scheduler > Create Basic Task
Name:		UniFiBoot
Trigger:	When the computer starts
Action:		Start a program
Program/script:
"%PROGRAMDATA%\Oracle\Java\javapath\javaw.exe"
Arguments:
C:\Ubiquiti UniFi\lib\ace.jar" ui
#This argument assumes that you moved the install location to C:\Ubiquiti UniFi
#Go to task properties
General  : Change user account to other local admin
General  : Run whether user is logged on or not
General  : Run with the highest privileges
Settings : Run task as soon as possible after a scheduled start is missed
Settings : If task fails, restart every: ... minutes/times
Option #2 Run UniFi as a Service
!------------------------------!
#Disable the scheduled task if created above
#Open administrative command prompt
	cd C:\Ubiquiti UniFi 
	java -jar lib\ace.jar installsvc
#These arguments assume that you moved the install location to C:\Ubiquiti UniFi
#Change service parameters
Start > run > services.msc
Service: 		UniFi Controller
Startup type: 	Automatic (should be default)
Log on:			Change user account to other local admin
#Reboot to start the service
Windows Firewall 
!--------------!
Option #1 Disable firewall
Option #2 Leave default UniFi/Java firewall rules as is
Option #3 Delete default firewall rules and create your own
#Option 3
Import-Module NetSecurity
Remove-NetFirewallRule -DisplayName "UniFi DB Server"
Remove-NetFirewallRule -DisplayName "Java (TM) Runtime Environment"
New-NetFirewallRule -Name UniFiUDP -DisplayName UniFiUDP –LocalPort 3478,10001 -Protocol UDP -Profile Any -Direction Inbound -Action Allow
New-NetFirewallRule -Name UniFiTCP -DisplayName UniFiTCP –LocalPort 8080,8880,8443,8843,27117 -Protocol TCP -Profile Any -Direction Inbound -Action Allow
New-NetFirewallRule -Name AllowICMPv4 -DisplayName AllowICMPv4 -Protocol ICMPv4 -IcmpType 8 -Enabled True -Profile Any -Action Allow
Firewall Ports
!------------!
TCP-8080	UAP > controller communication
TCP-8443	Controller GUI / API
TCP-8880	HTTP portal redirect
TCP-8843	HTTPS portal redirect
UDP-3478 	STUN
UDP-10001	UBNT Discovery
================================================

File: Configuration.txt
================================================
Method #1 Download Firmware from Ubiquiti
!---------------------------------------!
#Connect via SSH to UAP using terminal client
upgrade http://dl.ubnt.com/unifi/firmware/<modelnr>/firmware<version>.bin
Method #2 Download Firmware from Controller
!-----------------------------------------!
#Connect via SSH to UAP using terminal client
#The local path on Linux-based controllers is /usr/lib/unifi/dl/firmware/...
upgrade http://aws-elastic-ip:8080/dl/firmware/<modelnr>/firmware<version>.bin
#Change the <modelnr> value depending on your UniFi Model:
BZ2	 	 = UAP, UAP-LR, UAP-OD, UAP-OD5 
U2HSR	 = UAP-Outdoor+
U2IW	 = UAP-InWall
U2Sv2	 = UAP-v2, UAP-LR-v2
U7E	 	 = UAP-AC, UAP-AC v2, UAP-AC-OD
U7P	 	 = UAP-Pro
U7PG2	 = UAP-AC-Lite/AC-LR/AC-Pro/AC-EDU/AC-M/AC-M-PRO/AC-IW
UGW3	 = USG
UGW4	 = USG-Pro-4
US24P250 = US (all current models, with the exception of the US-16-XG)
USXG	 = US-16-XG
Method #3 Upload the Firmware from a local device
!-----------------------------------------------!
#Download the firmware to local PC
https://www.ubnt.com/download/unifi/
#Rename the firmware file to fwupdate.bin
#Connect via SCP to UAP using WinSCP
#Place the file into /tmp/
#Path on UAP is /tmp/fwupdate.bin
#Connect via SSH to UAP using terminal client and run:
syswrapper.sh upgrade2 &
================================================

File: Configuration.txt
================================================
UniFi Re-Installation / Upgrade
!-----------------------------!
#This part assumes that you have already installed UniFi v4 Stable
nano /etc/apt/sources.list
#This should be in the sources list:
#UniFi v4 Stable
deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti
#Uncomment/remove above and add:
#UniFi v5 
deb http://www.ubnt.com/downloads/unifi/debian unifi5 ubiquiti
tail /etc/apt/sources.list
#This key should already be added if you have installed UniFi v4 Stable
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50
apt-get update
#If you have previously disabled the UniFi update (hold), unhold the package:
apt-mark unhold unifi
#Verify the unhold (should be ii, not hi)
dpkg -l | grep unifi
#Stop the UniFi service
service unifi stop
apt-get upgrade
reboot
Verify UniFi Installation
!-----------------------!
systemctl status unifi
https://192.168.1.10:8443
apt-get install nmap
nmap localhost
#nmap should show
8080/tcp open  http-proxy
8443/tcp open  https-alt
#After upgrade you can put the UniFi package on hold again
apt-mark hold unifi
================================================

File: Config.txt
================================================
System Management
==================================================
edit service
 set telnet port 23
 set telnet listen-address 10.0.0.1
 set gui https-port 8443
User Management
==================================================
edit system login 
 set user bpin level operator 
 set user bpin authentication plaintext-password Pa$$w0rd
 delete system login user ubnt
Root Account 
================================================== 
sudo -i
edit system login
 set user root authentication plaintext-password Pa$$w0rd
set service telnet allow-root 
Limit Access
==================================================
edit firewall name MGMT
 set default-action drop
 set rule 1 action accept
 set rule 1 destination port 23
 set rule 1 log disable
 set rule 1 protocol tcp
 set rule 1 source address 10.0.0.99/32
set interfaces ethernet eth1 firewall local name MGMT
================================================

File: Configuration.txt
================================================
Temporary Management Connection
!-----------------------------!
delete interfaces switch switch0 switch-port interface eth2
set interfaces ethernet eth2 address 172.16.0.1/24
#On PC, configure static IP:
Address	: 172.16.0.10
Mask	: 255.255.255.0
Gateway	: -
#Patch into Eth2 and navigate to:
https://172.16.0.1
Switch0 Modification
!------------------!
edit interfaces switch switch0
 delete address 192.168.1.1/24
 set vif 1 address 192.168.1.1/24
 set vif 10 address 10.0.0.1/24
 set switch-port interface eth3 vlan pvid 10
 set switch-port interface eth4 vlan pvid 1
 set switch-port vlan-aware enable
 set mtu 1500
 top ; commit
#On PC, change adapter back to DHCP
#Patch into Eth3 and navigate to:
https://10.0.0.1
delete interfaces ethernet eth2 address 172.16.0.1/24
edit interfaces switch switch0 
 set switch-port interface eth1 vlan pvid 1 or 10
 set switch-port interface eth2 vlan pvid 1 or 10
 top ; commit
Misc Settings
!-----------!
set service dns forwarding listen-on switch0.1
set service dns forwarding listen-on switch0.10
set service dns forwarding name-server 8.8.8.8
edit service dhcp-server shared-network-name LAN 
 set subnet 192.168.1.0/24 default-router 192.168.1.1
 set subnet 192.168.1.0/24 dns-server 192.168.1.1
 set subnet 192.168.1.0/24 lease 86400
 set subnet 192.168.1.0/24 start 192.168.1.38 stop 192.168.1.243
edit service dhcp-server shared-network-name VLAN10 
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 lease 86400
 set subnet 10.0.0.0/24 start 10.0.0.38 stop 10.0.0.243
================================================

File: Config.txt
================================================
Switch Interface
=============================================
edit interfaces switch switch0
 set vif 10 address 10.0.0.1/24
 set vif 172 address 172.16.0.1/24
 set switch-port interface eth1 vlan vid 10
 set switch-port interface eth1 vlan vid 172
 set switch-port interface eth2 vlan pvid 10
 set switch-port interface eth3 vlan pvid 172
 set switch-port vlan-aware enable
 set mtu 1500
================================================

File: Config.txt
================================================
Switch Interface
=============================================
edit interfaces switch switch0
 set vif 10 address 10.0.0.1/24
 set vif 172 address 172.16.0.1/24
 set switch-port interface eth1 vlan vid 10
 set switch-port interface eth1 vlan vid 172
 set switch-port interface eth2 vlan pvid 10
 set switch-port interface eth3 vlan pvid 172
 set switch-port vlan-aware enable
 set mtu 1500
================================================

File: Config.txt
================================================
Virtual Interfaces (VIF)
==================================================
edit interfaces 
 set ethernet eth1 vif 10 address 10.0.0.1/24
 set ethernet eth1 vif 172 address 172.16.0.1/24
Misc Settings
==================================================
set service dns forwarding listen-on eth1.10
set service dns forwarding listen-on eth1.172
set service dns forwarding name-server 8.8.8.8
edit service dhcp-server shared-network-name 10_LAN 
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 lease 28800
edit service dhcp-server shared-network-name 172_LAN 
 set subnet 172.16.0.0/24 default-router 172.16.0.1
 set subnet 172.16.0.0/24 start 172.16.0.10 stop 172.16.0.150
 set subnet 172.16.0.0/24 dns-server 172.16.0.1
 set subnet 172.16.0.0/24 lease 28800 
================================================

File: Config.txt
================================================
Virtual Interfaces (VIF)
==================================================
edit interfaces 
 set ethernet eth1 vif 10 address 10.0.0.1/24
 set ethernet eth1 vif 172 address 172.16.0.1/24
Misc Settings
==================================================
set service dns forwarding listen-on eth1.10
set service dns forwarding listen-on eth1.172
set service dns forwarding name-server 8.8.8.8
edit service dhcp-server shared-network-name 10_LAN 
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 lease 28800
edit service dhcp-server shared-network-name 172_LAN 
 set subnet 172.16.0.0/24 default-router 172.16.0.1
 set subnet 172.16.0.0/24 start 172.16.0.10 stop 172.16.0.150
 set subnet 172.16.0.0/24 dns-server 172.16.0.1
 set subnet 172.16.0.0/24 lease 28800 
================================================

File: Cisco VRRP Config.txt
================================================
VRRP
===============================
int g1/0
 ip add 10.0.0.2 255.255.255.0
 description LAN
 no shutdown
 vrrp 12 preempt
 vrrp 12 priority 100
 vrrp 12 ip 10.0.0.254 
 vrrp 12 authentication Pa$$w0rd
================================================

File: Config.txt
================================================
VRRP
=============================================
edit interfaces ethernet eth1
 set address 10.0.0.1/24
 set description LAN
 edit vrrp vrrp-group 12 
  set priority 100
  set preempt true
  set authentication type plaintext-password
  set authentication password Pa$$w0rd
  set virtual-address 10.0.0.254/24
Verify
=============================================
show vrrp
show vrrp summary
clear vrrp master interface eth1 group 12
================================================

File: Juniper VRRP Config.txt
================================================
VRRP
===============================================
edit interfaces fe-0/0/1.0
 set description LAN
 edit family inet address 10.0.0.2/24
  set vrrp-group 12 preempt
  set vrrp-group 12 priority 100
  set vrrp-group 12 authentication-type simple
  set vrrp-group 12 authentication-key Pa$$w0rd
  set vrrp-group 12 virtual-address 10.0.0.254 
Verify
===============================================
show vrrp
show vrrp extensive
show vrrp summary 
================================================

File: Cisco VRRP Config.txt
================================================
VRRP
===============================
int g1/0
 ip add 10.0.0.2 255.255.255.0
 description LAN
 no shutdown
 vrrp 12 preempt
 vrrp 12 priority 100
 vrrp 12 ip 10.0.0.254 
 vrrp 12 authentication Pa$$w0rd
================================================

File: Config.txt
================================================
VRRP
=============================================
edit interfaces ethernet eth1
 set address 10.0.0.1/24
 set description LAN
 edit vrrp vrrp-group 12 
  set priority 100
  set preempt true
  set authentication type plaintext-password
  set authentication password Pa$$w0rd
  set virtual-address 10.0.0.254/24
Verify
=============================================
show vrrp
show vrrp summary
clear vrrp master interface eth1 group 12
================================================

File: Juniper VRRP Config.txt
================================================
VRRP
===============================================
edit interfaces fe-0/0/1.0
 set description LAN
 edit family inet address 10.0.0.2/24
  set vrrp-group 12 preempt
  set vrrp-group 12 priority 100
  set vrrp-group 12 authentication-type simple
  set vrrp-group 12 authentication-key Pa$$w0rd
  set vrrp-group 12 virtual-address 10.0.0.254 
Verify
===============================================
show vrrp
show vrrp extensive
show vrrp summary 
================================================

File: Config.txt
================================================
Default WAN_TO_LAN Rule
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable
WAN Management Filter
==========================================
edit firewall name MGMT
 set default-action drop
 set description 'Limit Management Access'
 set rule 1 action accept
 set rule 1 description SSH_9222
 set rule 1 destination port 9222
 set rule 1 log disable
 set rule 1 protocol tcp
 set rule 1 source address 100.0.0.1
 set rule 2 action accept
 set rule 2 description HTTPS_9443
 set rule 2 destination port 9443
 set rule 2 log disable
 set rule 2 protocol tcp
 set rule 2 source address 100.0.0.1
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
 set firewall local name MGMT
edit service
 set gui listen-address 2.0.0.1
 set gui listen-address 10.0.0.1
 set gui https-port 9443
 set ssh listen-address 2.0.0.1
 set gui listen-address 10.0.0.1
 set ssh port 9222
================================================

File: Config.txt
================================================
Default WAN_TO_LAN Rule
==========================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable
WAN Management Filter
==========================================
edit firewall name MGMT
 set default-action drop
 set description 'Limit Management Access'
 set rule 1 action accept
 set rule 1 description SSH_9222
 set rule 1 destination port 9222
 set rule 1 log disable
 set rule 1 protocol tcp
 set rule 1 source address 100.0.0.1
 set rule 2 action accept
 set rule 2 description HTTPS_9443
 set rule 2 destination port 9443
 set rule 2 log disable
 set rule 2 protocol tcp
 set rule 2 source address 100.0.0.1
Apply to Interface 
==========================================
edit interfaces ethernet eth0
 set firewall in name WAN_TO_LAN
 set firewall local name MGMT
edit service
 set gui listen-address 2.0.0.1
 set gui listen-address 10.0.0.1
 set gui https-port 9443
 set ssh listen-address 2.0.0.1
 set gui listen-address 10.0.0.1
 set ssh port 9222
================================================

File: Config.txt
================================================
Interfaces
==================================================
edit interfaces 
 set ethernet eth0 address 2.0.0.1/24
 set ethernet eth1 address 10.0.0.1/24
 set ethernet eth2 address 172.16.0.1/24
Zone Policies
==================================================
edit zone-policy
 set zone WAN default-action drop
 set zone WAN from LAN firewall name LAN_TO_ALL
 set zone WAN from LOCAL firewall name LOCAL_TO_ALL
 set zone WAN from GUEST firewall name GUEST_TO_WAN
 set zone WAN interface eth0
 set zone LAN default-action drop
 set zone LAN from WAN firewall name WAN_TO_ALL
 set zone LAN from LOCAL firewall name LOCAL_TO_ALL
 set zone LAN from GUEST firewall name GUEST_TO_LAN
 set zone LAN interface eth1
 set zone GUEST default-action drop
 set zone GUEST from WAN firewall name WAN_TO_ALL
 set zone GUEST from LOCAL firewall name LOCAL_TO_ALL
 set zone GUEST from LAN firewall name LAN_TO_ALL
 set zone GUEST interface eth2
 set zone LOCAL default-action drop
 set zone LOCAL from WAN firewall name WAN_TO_ALL
 set zone LOCAL from LAN firewall name LAN_TO_ALL
 set zone LOCAL from GUEST firewall name GUEST_TO_LOCAL
 set zone LOCAL local-zone 
GUEST Firewall Policy
==========================================
edit firewall name GUEST_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
edit firewall name GUEST_TO_LOCAL
 set default-action drop
 set rule 1 action accept
 set rule 1 description DNS
 set rule 1 log disable
 set rule 1 protocol tcp_udp
 set rule 1 destination port 53
 set rule 2 action accept
 set rule 2 description DHCP
 set rule 2 log disable
 set rule 2 protocol udp
 set rule 2 destination port 67
 set rule 3 action accept
 set rule 3 description Established
 set rule 3 log disable
 set rule 3 protocol all
 set rule 3 state established enable
 set rule 3 state related enable
set firewall name GUEST_TO_WAN default-action accept
Other Firewall Rules
==================================================
edit firewall name WAN_TO_ALL
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable 
set firewall name LAN_TO_ALL default-action accept
set firewall name LOCAL_TO_ALL default-action accept
Misc Settings
==================================================
set service dns forwarding listen-on eth1
set service dns forwarding listen-on eth2
set service dns forwarding name-server 8.8.8.8
edit service dhcp-server shared-network-name LAN 
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 lease 28800
edit service dhcp-server shared-network-name GUEST 
 set subnet 172.16.0.0/24 default-router 172.16.0.1
 set subnet 172.16.0.0/24 start 172.16.0.10 stop 172.16.0.150
 set subnet 172.16.0.0/24 dns-server 172.16.0.1
 set subnet 172.16.0.0/24 lease 28800 
================================================

File: Config.txt
================================================
Zones
==================================================
edit zone-policy
 set zone WAN default-action drop
 set zone WAN from LAN firewall name LAN_TO_ALL
 set zone WAN from LOCAL firewall name LOCAL_TO_ALL
 set zone WAN interface eth0
 set zone LAN default-action drop
 set zone LAN from WAN firewall name WAN_TO_LAN
 set zone LAN from LOCAL firewall name LOCAL_TO_ALL
 set zone LAN interface eth1
 set zone LOCAL default-action drop
 set zone LOCAL from WAN firewall name WAN_TO_LOCAL
 set zone LOCAL from LAN firewall name LAN_TO_ALL
 set zone LOCAL local-zone
Firewall Rules
==================================================
edit firewall name WAN_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable 
edit firewall name WAN_TO_LOCAL
 set default-action drop
 set description 'Limit Management Access'
 set rule 1 action accept
 set rule 1 description SSH
 set rule 1 destination port 22
 set rule 1 log disable
 set rule 1 protocol tcp
 set rule 1 source address 100.0.0.1 
 set rule 2 action accept
 set rule 2 description HTTPS
 set rule 2 destination port 443
 set rule 2 log disable
 set rule 2 protocol tcp
 set rule 2 source address 100.0.0.1
 set rule 3 action accept
 set rule 3 description Established
 set rule 3 log disable
 set rule 3 protocol all
 set rule 3 state established enable
 set rule 3 state invalid disable
 set rule 3 state new disable
 set rule 3 state related enable
set firewall name LAN_TO_ALL default-action accept
set firewall name LOCAL_TO_ALL default-action accept
================================================

File: Config.txt
================================================
Virtual Interfaces (VIF)
==================================================
edit interfaces 
 set ethernet eth1 vif 10 address 10.0.0.1/24
 set ethernet eth1 vif 172 address 172.16.0.1/24
Zone Policies
==================================================
edit zone-policy
 set zone WAN default-action drop
 set zone WAN from LAN firewall name LAN_TO_ALL
 set zone WAN from LOCAL firewall name LOCAL_TO_ALL
 set zone WAN from GUEST firewall name GUEST_TO_WAN
 set zone WAN interface eth0
 set zone LAN default-action drop
 set zone LAN from WAN firewall name WAN_TO_ALL
 set zone LAN from LOCAL firewall name LOCAL_TO_ALL
 set zone LAN from GUEST firewall name GUEST_TO_LAN
 set zone LAN interface eth1.10
 set zone GUEST default-action drop
 set zone GUEST from WAN firewall name WAN_TO_ALL
 set zone GUEST from LOCAL firewall name LOCAL_TO_ALL
 set zone GUEST from LAN firewall name LAN_TO_ALL
 set zone GUEST interface eth1.172
 set zone LOCAL default-action drop
 set zone LOCAL from WAN firewall name WAN_TO_ALL
 set zone LOCAL from LAN firewall name LAN_TO_ALL
 set zone LOCAL from GUEST firewall name GUEST_TO_LOCAL
 set zone LOCAL local-zone 
GUEST Firewall Policy
==========================================
edit firewall name GUEST_TO_LAN 
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state related enable
edit firewall name GUEST_TO_LOCAL
 set default-action drop
 set rule 1 action accept
 set rule 1 description DNS
 set rule 1 log disable
 set rule 1 protocol tcp_udp
 set rule 1 destination port 53
 set rule 2 action accept
 set rule 2 description DHCP
 set rule 2 log disable
 set rule 2 protocol udp
 set rule 2 destination port 67
 set rule 3 action accept
 set rule 3 description Established
 set rule 3 log disable
 set rule 3 protocol all
 set rule 3 state established enable
 set rule 3 state related enable
set firewall name GUEST_TO_WAN default-action accept
Other Firewall Rules
==================================================
edit firewall name WAN_TO_ALL
 set default-action drop
 set rule 1 action accept
 set rule 1 description Established
 set rule 1 log disable
 set rule 1 protocol all
 set rule 1 state established enable
 set rule 1 state invalid disable
 set rule 1 state new disable
 set rule 1 state related enable 
set firewall name LAN_TO_ALL default-action accept
set firewall name LOCAL_TO_ALL default-action accept
Misc Settings
==================================================
set service dns forwarding listen-on eth1.10
set service dns forwarding listen-on eth1.172
set service dns forwarding name-server 8.8.8.8
edit service dhcp-server shared-network-name LAN 
 set subnet 10.0.0.0/24 default-router 10.0.0.1
 set subnet 10.0.0.0/24 start 10.0.0.10 stop 10.0.0.150
 set subnet 10.0.0.0/24 dns-server 10.0.0.1
 set subnet 10.0.0.0/24 lease 28800
edit service dhcp-server shared-network-name GUEST 
 set subnet 172.16.0.0/24 default-router 172.16.0.1
 set subnet 172.16.0.0/24 start 172.16.0.10 stop 172.16.0.150
 set subnet 172.16.0.0/24 dns-server 172.16.0.1
 set subnet 172.16.0.0/24 lease 28800