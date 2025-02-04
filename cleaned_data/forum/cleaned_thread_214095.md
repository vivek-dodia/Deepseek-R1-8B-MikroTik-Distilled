# Thread Information
Title: Thread-214095
Section: RouterOS
Thread ID: 214095

# Discussion

## Initial Question
Hi, allI'm having a big problem configuring an IPSec Site to Site tunnel. I don't know why, but I can't configure the tunnel between the 2 MTs correctly, I went through more than a dozen instructions and nothing works as it should. I received information that MT I have some problems with this configuration. Please help me how to configure Mikrotik devices correctly. The diagram belowIn my case there is a big problem with connecting 2 MT together. The ping works, but only one way, host A to Host B.Please help Me guys. ---

## Response 1
Could you consider exporting your configurations to check what is already set? ---

## Response 2
probably a NAT problemon office1/ip ro add dst-address=192.168.10.0/24 gateway=172.10.20.1 pref-src=192.168.20.1/ip fi na add action=accept chain=srcnat dst-address=192.168.10.0/24on office2/ip ro add dst-address=192.168.10.0/24 gateway=172.10.30.1 pref-src=192.168.30.1/ip fi na add action=accept chain=srcnat dst-address=192.168.10.0/24on hq/ip ro add dst-address=192.168.20.0/24 gateway=172.10.10.1 pref-src=192.168.10.1/ip ro add dst-address=192.168.30.0/24 gateway=172.10.10.1 pref-src=192.168.10.1/ip fi na add action=accept chain=srcnat dst-address=192.168.20.0/24/ip fi na add action=accept chain=srcnat dst-address=192.168.30.0/24 ---