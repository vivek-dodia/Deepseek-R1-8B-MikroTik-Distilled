# Thread Information
Title: Thread-214086
Section: RouterOS
Thread ID: 214086

# Discussion

## Initial Question
HiI´ve reading a lot of threads here at the forum about the /29 IPs delivered from the ISP, but I am still confuce and not having my config properly done.The ISP delivered the /29 Public IP´s by a /31 Upstream link (this ls the internal ISP Link)What I am trying to do is:1 - ISP UPstream xxx.xxx.xxx.18/31 to MT1 xxx.xxx.xxx.19/31 (In order to stablish the ISP Upstream link. this currently works)2 -Then, having other MT2 Router connected to WAN 2 with xxx.xxx.xxx.51/29 as Public IP (is in here where I am missing something as Theres no Internet access in here)been MT1 the GW for MT2/ interface bridgeadd name=WanBridge/interface ethernetset [ find default-name=ether1 ] name=Wan1set [ find default-name=ether2 ] name=Wan2set [ find default-name=ether3 ] name=Wan3set [ find default-name=ether3 ] name=Wan4/interface bridge portadd bridge=WanBridge ingress-filtering=no interface=Wan1 \add bridge=WanBridge ingress-filtering=no interface=Wan2 \add bridge=WanBridge ingress-filtering=no interface=Wan3 \add bridge=WanBridge ingress-filtering=no interface=Wan4 \/ip addressadd address=xxx.xxx.xxx.19/31 interface=WanBridge network=xxx.xxx.xxx.18add address=xxx.xxx.xxx.56/29 interface=WanBridge network=xxx.xxx.xxx.50/ip routeadd disabled=no distance=1 dst-address=0.0.0.0/0 gateway=xxx.xxx.xxx.18 \routing-table=main scope=30 suppress-hw-offload=no target-scope=10 ---

## Response 1
What version of ROS do you use as /31 works since 7.18beta? ---

## Response 2
Currently ROS V7.17 at both Routers ---