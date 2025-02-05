# Repository Information
Name: playbooks

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
	url = https://gitlab.com/projects20xx/network/mikrotik/playbooks.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: firewaleth1.yml
================================================
---
- hosts: test
  gather_facts: no
  connection: network_cli
  tasks:
    - name: Delete Firewall
      routeros_command:
       commands:
         - /system script run addresslist
         - /ip firewall mangle remove [find comment=Teamviewer]
         - /ip firewall mangle remove [find comment=Youtube]
         - /ip firewall filter remove [find chain=input]
#         - /ip firewall filter remove [find chain=output]
         - /ip firewall filter remove [find chain=forward]
         - /ip firewall layer7-protocol remove [find name=teamviewer]
         - /ip firewall layer7-protocol remove [find name=teamviewer1]
         - /system script remove [find name=addresslist]
         - /tool netwatch remove [find comment="VPNallowAny"]     
    - name: Add script Address-list
      routeros_command:
       commands: /system script add name=addresslist owner=administrator source="ip firewall address-list\r\ \n:foreach i in=[find (list=rabota) or (list=rdp) or (list=socialnetwork) or (list=znakomstva) or (list=ammyy)or (list=allowmikrotik) or (list=videohost)] do={\r\ \n:do {\r\ \nremove \$i;\r\ \n} on-error={ :put \"OK adresslist\"};\r\ \n}"
    - name: Add Firewall
      routeros_command:
       commands:
         - /system script run addresslist 
         - /ip firewall layer7-protocol add name=teamviewer regexp="^(post|get) /d(out|in).aspx\\\?.*client=dyngate"
         - /ip firewall layer7-protocol add name=teamviewer1 regexp="^\\x17"
#         - /ip firewall layer7-protocol add name=anydesk regexp="^.+(ammyy|anydesk).*\$"
         - /ip firewall mangle add action=mark-connection chain=prerouting comment=Youtube connection-mark=no-mark new-connection-mark=youtube-conn passthrough=yes protocol=tcp tls-host=*youtube.com
         - /ip firewall mangle add action=mark-packet chain=prerouting comment=Youtube connection-mark=youtube-conn new-packet-mark=youtube-packet passthrough=yes
         - /ip firewall mangle add action=mark-connection chain=prerouting comment=Teamviewer new-connection-mark=tiamviewer-conn passthrough=yes protocol=tcp tls-host=*teamviewer.com
         - /ip firewall mangle add action=mark-packet chain=prerouting comment=Teamviewer connection-mark=tiamviewer-conn new-packet-mark=teamviewer-packet passthrough=yes
         - /ip firewall service-port set sip disabled=no
         - /ip firewall address-list add address=10.10.0.0/24 list=allowmikrotik
         - /ip firewall address-list add address=10.10.99.0/24 list=allowmikrotik
         - /ip firewall address-list add address=10.10.97.0/24 list=allowmikrotik
         - /ip firewall address-list add address=vk.com list=socialnetwork
         - /ip firewall address-list add address=ok.ru list=socialnetwork
         - /ip firewall address-list add address=instagram.com list=socialnetwork
         - /ip firewall address-list add address=facebook.com list=socialnetwork
         - /ip firewall address-list add address=ru-ru.facebook.com list=socialnetwork
         - /ip firewall address-list add address=twitter.com list=socialnetwork
         - /ip firewall address-list add address=linkedin.com list=socialnetwork
         - /ip firewall address-list add address=pinterest.com list=socialnetwork
         - /ip firewall address-list add address=pinterest.ru list=socialnetwork
         - /ip firewall address-list add address=tumblr.com list=socialnetwork
         - /ip firewall address-list add address=flickr.com list=socialnetwork
         - /ip firewall address-list add address=myspace.com list=socialnetwork
         - /ip firewall address-list add address=meetup.com list=socialnetwork
         - /ip firewall address-list add address=tagged.com list=socialnetwork
         - /ip firewall address-list add address=ask.fm list=socialnetwork
         - /ip firewall address-list add address=meetme.com list=socialnetwork
         - /ip firewall address-list add address=classmates.com list=socialnetwork
         - /ip firewall address-list add address=loveplanet.ru list=znakomstva
         - /ip firewall address-list add address=mamba.ru list=znakomstva
         - /ip firewall address-list add address=mylove.ru list=znakomstva
         - /ip firewall address-list add address=badoo.com list=znakomstva
         - /ip firewall address-list add address=24open.ru list=znakomstva
         - /ip firewall address-list add address=dating.ru list=znakomstva
         - /ip firewall address-list add address=fotostrana.ru list=znakomstva
         - /ip firewall address-list add address=tabor.ru list=znakomstva
         - /ip firewall address-list add address=znakomstva.ru list=znakomstva
         - /ip firewall address-list add address=maybe.ru list=znakomstva
         - /ip firewall address-list add address=hh.ru list=rabota
         - /ip firewall address-list add address=superjob.ru list=rabota
         - /ip firewall address-list add address=avito.ru list=rabota
         - /ip firewall address-list add address=moscow.hh.ru list=rabota
         - /ip firewall address-list add address=job.ru list=rabota
         - /ip firewall address-list add address=rabota.ru list=rabota
         - /ip firewall address-list add address=zarplata.ru list=rabota
         - /ip firewall address-list add address=rabota.mail.ru list=rabota
         - /ip firewall address-list add address=vakant.ru list=rabota
         - /ip firewall address-list add address=gorodrabot.ru list=rabota
         - /ip firewall address-list add address=rosrabota.ru list=rabota
         - /ip firewall address-list add address=jobmarket.ru list=rabota
         - /ip firewall address-list add address=career.ru list=rabota
         - /ip firewall address-list add address=trud.com list=rabota
         - /ip firewall address-list add address=trudbox.com list=rabota
         - /ip firewall address-list add address=job-mo.ru list=rabota
         - /ip firewall address-list add address=job.ws list=rabota
         - /ip firewall address-list add address=jobinmoscow.ru list=rabota
         - /ip firewall address-list add address=careerist.ru list=rabota
         - /ip firewall address-list add address=adzuna.ru list=rabota
         - /ip firewall address-list add address=jobijoba.ru list=rabota
         - /ip firewall address-list add address=vimeo.com list=videohost
         - /ip firewall address-list add address=rutube.ru list=videohost
         - /ip firewall address-list add address=ivi.ru list=videohost
         - /ip firewall address-list add address=video.mail.ru list=videohost
         - /ip firewall address-list add address=smotri.com list=videohost
         - /ip firewall address-list add address=teamviewer.com list=rdp
         - /ip firewall address-list add address=ammyy.com list=rdp
         - /ip firewall address-list add address=anydesk.com list=rdp
         - /ip firewall address-list add address=relays.net.anydesk.com list=rdp
         - /ip firewall address-list add address=21.111.200.64 list=ammyy
         - /ip firewall address-list add address=23.105.254.132 list=ammyy
         - /ip firewall address-list add address=136.243.18.81 list=ammyy
         - /ip firewall address-list add address=24.111.200.64 list=ammyy
         - /ip firewall address-list add address=rl.ammyy.com list=ammyy
#         - /interface list add name=LAN
#         - /interface list add name=WAN
#         - /ip firewall filter add action=accept chain=input dst-port=1701,500,4500 protocol=udp comment="l2tpports"
         - /ip firewall filter add action=accept chain=input connection-state=established,related,untracked comment="Allowestablished"
         - /ip firewall filter add action=drop chain=input dst-port=8291 protocol=tcp src-address-list=!allowmikrotik comment="Drop Winbox"
         - /ip firewall filter add action=drop chain=input dst-port=53 in-interface-list=WAN protocol=udp comment="DNSudp"
         - /ip firewall filter add action=drop chain=input dst-port=53 in-interface-list=WAN protocol=tcp comment="DNStcp"
         - /ip firewall filter add action=drop chain=input connection-state=invalid comment="Invalid"
         - /ip firewall filter add action=drop chain=input in-interface-list=WAN comment="DropWAN"
         - /ip firewall filter add action=reject chain=forward comment="Block rabota" dst-address-list=rabota dst-port=80,443 protocol=tcp reject-with=tcp-reset
         - /ip firewall filter add action=reject chain=forward comment="Block Socialnetwork" dst-address-list=socialnetwork dst-port=80,443 protocol=tcp reject-with=tcp-reset
         - /ip firewall filter add action=reject chain=forward comment="Block znakomstva" dst-address-list=znakomstva dst-port=80,443 protocol=tcp reject-with=tcp-reset
         - /ip firewall filter add action=reject chain=forward comment="Block videohost" dst-address-list=videohost dst-port=80,443 protocol=tcp reject-with=tcp-reset
         - /ip firewall filter add action=reject chain=forward comment="Mail Google" content=mail.google.com dst-port=80,443 protocol=tcp reject-with=tcp-reset
         - /ip firewall filter add action=reject chain=forward comment="Mail Yandex" content=mail.yandex.ru dst-port=80,443 protocol=tcp reject-with=tcp-reset
         - /ip firewall filter add action=reject chain=forward comment="Mail rambler" content=mail.rambler.ru dst-port=80,443 protocol=tcp reject-with=tcp-reset
         - /ip firewall filter add action=reject chain=forward comment="Mail Mail" content=e.mail.ru dst-port=80,443 protocol=tcp reject-with=tcp-reset
         - /ip firewall filter add action=reject chain=forward comment="Drop Youtube" packet-mark=youtube-packet dst-port=80,443 protocol=tcp reject-with=tcp-reset
         - /ip firewall filter add action=reject chain=forward comment="Youtube" content=youtube.com dst-port=80,443 protocol=tcp reject-with=tcp-reset
         - /ip firewall filter add action=drop chain=forward comment="Teamviewer Site" packet-mark=teamviewer-packet
         - /ip firewall filter add action=drop chain=forward comment="Teamviewer" content=teamviewer.com
         - /ip firewall filter add action=drop chain=forward comment="Drop Tiamviewer" layer7-protocol=teamviewer
         - /ip firewall filter add action=drop chain=forward comment="Drop Tiamviewer" layer7-protocol=teamviewer1
         - /ip firewall filter add action=drop chain=forward comment="Drop Tiamviewer Anydesk" dst-address-list=rdp
         - /ip firewall filter add action=drop chain=forward comment="Drop AmmyyAdmin" dst-address-list=ammyy
         - /ip firewall filter add action=drop chain=forward comment="Teamviewer" dst-port=5938 protocol=tcp
         - /ip firewall filter add action=drop chain=forward comment="Teamviewer" dst-port=5938 protocol=udp
         - /ip firewall filter add action=accept chain=forward comment="Established,related" connection-state=established,related
         - /ip firewall filter add action=drop chain=forward comment="Invalid" connection-state=invalid
         - /ip firewall filter add action=drop chain=forward comment="Drop all from WAN not DSTNATed " connection-nat-state=!dstnat connection-state=new in-interface-list=WAN
         - /ip service set winbox address=0.0.0.0/0
         - /ip service set ssh address=10.10.0.0/16
         - /ip neighbor discovery-settings set discover-interface-list=LAN
         - /tool mac-server mac-winbox set allowed-interface-list=LAN
         - /tool mac-server set allowed-interface-list=LAN
#         - /interface list member add interface=bridge-local list=LAN
#         - /interface list member add interface=forsage-vpn  list=LAN
#         - /interface list member add interface=ether1 list=WAN 
         - /ip service disable telnet
         - /ip service disable api
         - /ip service disable api-ssl
         - /ip service disable ftp
         - /tool netwatch add comment=VPNallowAny down-script="/ip firewall filter set [find comment=\"Drop Tiamviewer Anydesk\"] disabled=yes\r\ \n/ip firewall connection remove [find]" host=10.10.10.1 interval=5m timeout=500ms up-script="/ip firewall filter set [find comment=\"Drop Tiamviewer Anydesk\"] disabled=no\r\ \n/ip firewall connection remove [find]"
================================================

File: mikrotik_eth1_dev1
================================================
---
- hosts: localhost
  serial: 1
  connection: local
  gather_facts: yes
  vars:
  - ssh_user: admin
  - vpn_address: 
  - ansible_user: 
  - ansible_password: 
  vars_prompt:
  - name: info
    prompt: "Проводной интернет. Порт eth1 получение ip адреса динамическое, прошивка обновлена ver 7.x Для продолжения нажмите Enter, выйти CTRL+Z"
    private: no 
  - name: ssh_ip
    prompt: "Введите ip адрес устройства"
    private: no
  - name: identity
    prompt: "Введите имя филиала (пример: Yantar)"
    private: no
  - name: dhcp
    prompt: "Введите ip адрес 3 октета(пример: 10.168.102):"
    private: no
  - name: l2tpuser
    prompt: "Введите логин l2tp vpn:"
    private: no
  - name: l2tppass
    prompt: "Введите пароль для l2tp vpn:"
    private: yes
  - name: ipseckey
    prompt: "Введите ipsec ключ:"
    private: yes
  tasks:
  - name: "generate script from template"
    action: template src=/home/ansible/ansible/mikrotik/template/mikrotiketh1ver3.j2 dest=/home/ansible/ansible/mikrotik/template_config/mikrotiketh1ver3_{{identity}}.rsc backup=no
    tags: generate
  - name: "copy script on device"
    action: "command scp -oStrictHostKeyChecking=no /home/ansible/ansible/mikrotik/template_config/mikrotiketh1ver3_{{identity}}.rsc {{ssh_user}}@{{ssh_ip}}:"
    tags: import
  - name: "Import script on the client"
    action: command ssh -oStrictHostKeyChecking=no {{ssh_user}}@{{ssh_ip}} "/import mikrotiketh1ver3_{{identity}}.rsc"
  - name: "Pause 3 sec"
    local_action: pause seconds=3
  - name: "copy sshkey on device"
    action: "command scp -oStrictHostKeyChecking=no /home/ansible/.ssh/id_rsa.pub  {{ssh_user}}@{{ssh_ip}}:" 
  - name: "Pause 2 seconds"
    local_action: pause seconds=2
  - name: "import key user on mikrotik"
    action: command ssh -oStrictHostKeyChecking=no {{ssh_user}}@{{ssh_ip}} "user ssh-keys import user=ansible public-key-file=id_rsa.pub"
  - name: "pause 1 seconds"
    local_action: pause seconds=1
  - name: "Remove import file"
    action: command ssh -oStrictHostKeyChecking=no {{ssh_user}}@{{ssh_ip}} "/file remove mikrotiketh1ver3_{{identity}}.rsc"
================================================

File: mikrotik_lte_dev
================================================
---
- hosts: localhost
  serial: 1
  connection: local
  gather_facts: yes
  vars:
  - ssh_user: admin
  - vpn_address: 
  - ansible_user:
  - ansible_password: 
  vars_prompt:
  - name: info
    prompt: "Для модемов версии stick интерфейс lte1. Убедитесь что модем вставлен, прошивка обновлена ver 7.x Для продолжения нажмите Enter, выйти CTRL+Z"
    private: no 
  - name: ssh_ip
    prompt: "Введите ip адрес устройства"
    private: no
  - name: identity
    prompt: "Введите имя филиала (пример: Yantar)"
    private: no
  - name: dhcp
    prompt: "Введите ip адрес 3 октета(пример: 10.168.102):"
    private: no
  - name: l2tpuser
    prompt: "Введите логин l2tp vpn:"
    private: no
  - name: l2tppass
    prompt: "Введите пароль для l2tp vpn:"
    private: yes
  - name: ipseckey
    prompt: "Введите ipsec ключ:"
    private: yes
  tasks:
  - name: "generate script from template"
    action: template src=/home/ansible/ansible/mikrotik/template/mikrotikltever3.j2 dest=/home/ansible/ansible/mikrotik/template_config/mikrotikltever3_{{identity}}.rsc backup=no
    tags: generate
  - name: "copy script on device"
    action: "command scp -oStrictHostKeyChecking=no /home/ansible/ansible/mikrotik/template_config/mikrotikltever3_{{identity}}.rsc {{ssh_user}}@{{ssh_ip}}:"
    tags: import
  - name: "Import script on the client"
    action: command ssh -oStrictHostKeyChecking=no {{ssh_user}}@{{ssh_ip}} "/import mikrotikltever3_{{identity}}.rsc"
  - name: "Pause 3 sec"
    local_action: pause seconds=3
  - name: "copy sshkey on device"
    action: "command scp -oStrictHostKeyChecking=no /home/ansible/.ssh/id_rsa.pub  {{ssh_user}}@{{ssh_ip}}:" 
  - name: "Pause 2 seconds"
    local_action: pause seconds=2
  - name: "import key user on mikrotik"
    action: command ssh -oStrictHostKeyChecking=no {{ssh_user}}@{{ssh_ip}} "user ssh-keys import user=ansible public-key-file=id_rsa.pub"
  - name: "pause 1 seconds"
    local_action: pause seconds=1
  - name: "Remove import file"
    action: command ssh -oStrictHostKeyChecking=no {{ssh_user}}@{{ssh_ip}} "/file remove mikrotikltever3_{{identity}}.rsc"
================================================

File: sendsshkey.yml
================================================
--- 
- hosts: localhost
  serial: 1
  connection: local
  gather_facts: yes
  vars:
  - ssh_user: ansible
  - ssh_ip: 10.10.10.102
#  - hosts: routers
  tasks:
#  - name: "delete old key"
#    action: command ssh -oStrictHostKeyChecking=no {{ssh_user}}@{{ssh_ip}} "user ssh-keys remove numbers=0"
  - name: "copy sshkey on device"
    action: "command scp -oStrictHostKeyChecking=no /home/ansible/.ssh/id_rsa.pub  {{ssh_user}}@{{ssh_ip}}:"
  - name: "import key user on mikrotik"
    action: command ssh -oStrictHostKeyChecking=no {{ssh_user}}@{{ssh_ip}} "user ssh-keys import user=ansible public-key-file=id_rsa.pub"
  - name: "delete public key"
    action: command ssh -oStrictHostKeyChecking=no {{ssh_user}}@{{ssh_ip}} "file remove id_rsa.pub"
================================================

File: user.yaml
================================================
--- 
- hosts: krivsk
  gather_facts: no
  connection: network_cli
  tasks:
    - name: Add users
      routeros_command:
       commands:
#          - /user remove [find name=ivanov]
#          - /user group set set write policy="reboot,read,write,test,winbox,web,sniff,romon,tikapp,!local,!telnet,!ssh,!ftp,!policy,!password,!sensitive,!api,!dude"
          - /user add group=full name=administrator password= address=10.10.0.0/16
================================================

File: mikrotiketh1ver3.j2
================================================
/system identity set name={{identity}}
/interface bridge add name=bridge-local
/interface bridge port add interface=ether2 bridge=bridge-local
/interface bridge port add interface=ether3 bridge=bridge-local
/interface bridge port add interface=ether4 bridge=bridge-local
#/interface bridge port add interface=ether5 bridge=bridge-local 
/ip address add address="{{dhcp}}.254/24" interface=bridge-local comment=LAN
/ip pool add name=dhcppool ranges={{dhcp}}.1-{{dhcp}}.253
/ip dhcp-server add name=dhcp interface=bridge-local lease-time=12h address-pool=dhcppool disabled=no
/ip dhcp-server network  add address={{dhcp}}.0/24 gateway={{dhcp}}.254 dns-server={{dhcp}}.254,8.8.8.8 domain=365-cloud.local comment=dhcp-local
/ip service disable telnet
/ip service disable api
/ip service disable api-ssl
/ip service disable ftp
/ip service set www address={{dhcp}}.0/24,10.10.0.0/16
/ip service set ssh address=10.10.0.0/16
/ip service set winbox address=0.0.0.0/0
/interface list add name=LAN
/interface list add name=WAN
/ip neighbor discovery-settings set discover-interface-list=LAN
/tool mac-server mac-winbox set allowed-interface-list=LAN
/tool mac-server set allowed-interface-list=LAN
/interface l2tp-client add name=cloud-vpn user={{l2tpuser}} password={{l2tppass}} allow=mschap2 connect-to={{vpn_address}} ipsec-secret={{ipseckey}} use-ipsec=yes disabled=no comment=Vpn
/ip route add distance=1 dst-address=10.10.0.0/16 gateway=cloud-vpn comment=ofisroute
/ip dhcp-client add interface=ether1 add-default-route=yes use-peer-dns=yes use-peer-ntp=yes disabled=no comment=WAN
/ip firewall nat add action=masquerade chain=srcnat out-interface-list=WAN comment=WAN   
/ip dns set allow-remote-requests=yes
/system clock set time-zone-name=Europe/Moscow time-zone-autodetect=no 
/user
add group=full name={{ansible_user}} password={{ansible_password}} address=10.10.0.0/16
/system script remove [find name=addresslist]
#ver 6.42
/system script
add name=addresslist owner=administrator policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/\
    ip firewall address-list\r\
    \n:foreach i in=[find (list=rabota) or (list=rdp) or (list=socialnetwork) \
    or (list=znakomstva) or (list=videohost)or (list=ammyy)] do={\r\
    \n  :do {\r\
    \n      remove \$i;\r\
    \n  } on-error={ :put \"OK addresslist\"};\r\
    \n }"
/system script run addresslist 
/ip firewall layer7-protocol
add name=teamviewer regexp="^(post|get) /d(out|in).aspx\\\?.*client=dyngate"
add name=teamviewer1 regexp="^\\x17"
/ip firewall mangle
add action=mark-connection chain=prerouting comment=Youtube connection-mark=no-mark new-connection-mark=youtube-conn passthrough=yes protocol=tcp tls-host=*youtube.com
add action=mark-packet chain=prerouting comment=Youtube connection-mark=youtube-conn new-packet-mark=youtube-packet passthrough=yes
add action=mark-connection chain=prerouting comment=Teamviewer new-connection-mark=tiamviewer-conn passthrough=yes protocol=tcp tls-host=*teamviewer.com
add action=mark-packet chain=prerouting comment=Teamviewer connection-mark=tiamviewer-conn new-packet-mark=teamviewer-packet passthrough=yes
/ip firewall service-port set sip disabled=yes
/ip firewall address-list
add address=10.10.0.0/24 list=allowmikrotik
add address=10.10.99.0/24 list=allowmikrotik
add address=10.10.97.0/24 list=allowmikrotik
add address=10.10.1.0/24 list=allowmikrotik
add address=vk.com list=socialnetwork
add address=ok.ru list=socialnetwork
add address=instagram.com list=socialnetwork
add address=facebook.com list=socialnetwork
add address=ru-ru.facebook.com list=socialnetwork
add address=twitter.com list=socialnetwork
add address=linkedin.com list=socialnetwork
add address=pinterest.com list=socialnetwork
add address=pinterest.ru list=socialnetwork
add address=tumblr.com list=socialnetwork
add address=flickr.com list=socialnetwork
add address=myspace.com list=socialnetwork
add address=meetup.com list=socialnetwork
add address=tagged.com list=socialnetwork
add address=ask.fm list=socialnetwork
add address=meetme.com list=socialnetwork
add address=classmates.com list=socialnetwork
add address=loveplanet.ru list=znakomstva
add address=mamba.ru list=znakomstva
add address=mylove.ru list=znakomstva
add address=badoo.com list=znakomstva
add address=24open.ru list=znakomstva
add address=dating.ru list=znakomstva
add address=fotostrana.ru list=znakomstva
add address=tabor.ru list=znakomstva
add address=znakomstva.ru list=znakomstva
add address=maybe.ru list=znakomstva
add address=hh.ru list=rabota
add address=superjob.ru list=rabota
add address=avito.ru list=rabota
add address=moscow.hh.ru list=rabota
add address=job.ru list=rabota
add address=rabota.ru list=rabota
add address=zarplata.ru list=rabota
add address=rabota.mail.ru list=rabota
add address=vakant.ru list=rabota
add address=gorodrabot.ru list=rabota
add address=rosrabota.ru list=rabota
add address=jobmarket.ru list=rabota
add address=career.ru list=rabota
add address=trud.com list=rabota
add address=trudbox.com list=rabota
add address=job-mo.ru list=rabota
add address=job.ws list=rabota
add address=jobinmoscow.ru list=rabota
add address=careerist.ru list=rabota
add address=adzuna.ru list=rabota
add address=jobijoba.ru list=rabota
add address=vimeo.com list=videohost
add address=rutube.ru list=videohost
add address=ivi.ru list=videohost
add address=video.mail.ru list=videohost
add address=smotri.com list=videohost
add address=teamviewer.com list=rdp
add address=ammyy.com list=rdp
add address=anydesk.com list=rdp
add address=relays.net.anydesk.com list=rdp
add address=21.111.200.64 list=ammyy
add address=23.105.254.132 list=ammyy
add address=136.243.18.81 list=ammyy
add address=24.111.200.64 list=ammyy
add address=rl.ammyy.com list=ammyy
add address=194.54.15.25 comment=Sberbank list=kassa-allowed-ip-dst
add address=194.54.14.89 comment=Sberbank list=kassa-allowed-ip-dst
add address=194.54.14.162 comment=Sberbank list=kassa-allowed-ip-dst
add address=91.213.144.29 comment=OFD list=kassa-allowed-ip-dst
add address=10.10.143.242 comment=K4 list=kassy-ip-src
add address=10.10.0.0/16 comment=Local list=kassa-allowed-ip-dst
add address=edge.365-cloud.ru comment=edge list=kassa-allowed-ip-dst
add address=kitchen.365-cloud.ru comment=kitchen list=kassa-allowed-ip-dst
add address=esm.365-cloud.ru comment=esm list=kassa-allowed-ip-dst
add address=ntp.ubuntu.com comment=ntp list=kassa-allowed-ip-dst
add address=docker.io comment="DOCKER HUB" list=kassa-allowed-ip-dst
add address=registry-1.docker.io list=kassa-allowed-ip-dst
add address=production.cloudflare.docker.com list=kassa-allowed-ip-dst
add address=ru.archive.ubuntu.com comment=Ubuntu-Update list=kassa-allowed-ip-dst
add address=security.ubuntu.com comment=Ubuntu-Update list=kassa-allowed-ip-dst
add address=kkt.sbis.ru comment=OFD list=kassa-allowed-ip-dst
#/ip firewall filter add action=accept chain=input dst-port=1701,500,4500 protocol=udp comment="l2tpports"
/ip firewall filter add action=accept chain=input connection-state=established,related,untracked comment="Allowestablished"
/ip firewall filter add action=drop chain=input dst-port=8291 protocol=tcp src-address-list=!allowmikrotik comment="Drop Winbox"
/ip firewall filter add action=drop chain=input dst-port=53 in-interface-list=WAN protocol=udp comment="DNSudp"
/ip firewall filter add action=drop chain=input dst-port=53 in-interface-list=WAN protocol=tcp comment="DNStcp"
/ip firewall filter add action=drop chain=input connection-state=invalid comment="Invalid"
/ip firewall filter add action=drop chain=input in-interface-list=WAN comment="DropWAN"
/ip firewall filter
add action=reject chain=forward comment="Block rabota" dst-address-list=rabota dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Block Socialnetwork" dst-address-list=socialnetwork dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Block znakomstva" dst-address-list=znakomstva dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Block videohost" dst-address-list=videohost dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Mail Google" content=mail.google.com dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Mail Yandex" content=mail.yandex.ru dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Mail rambler" content=mail.rambler.ru dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Mail Mail" content=e.mail.ru dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Drop Youtube" packet-mark=youtube-packet dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Youtube" content=youtube.com dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=drop chain=forward comment="Teamviewer Site" packet-mark=teamviewer-packet
add action=drop chain=forward comment="Teamviewer" content=teamviewer.com
add action=drop chain=forward comment="Drop Tiamviewer" layer7-protocol=teamviewer
add action=drop chain=forward comment="Drop Tiamviewer" layer7-protocol=teamviewer1
add action=drop chain=forward comment="Drop Tiamviewer Anydesk" dst-address-list=rdp
add action=drop chain=forward comment="Drop AmmyyAdmin" dst-address-list=ammyy
add action=drop chain=forward comment="Teamviewer" dst-port=5938 protocol=tcp
add action=drop chain=forward comment="Teamviewer" dst-port=5938 protocol=udp
add action=drop chain=forward comment=Kassy dst-address-list=!kassa-allowed-ip-dst log-prefix=kassy src-address-list=kassy-ip-src
add action=accept chain=forward comment="Established,related" connection-state=established,related
add action=drop chain=forward comment="Invalid" connection-state=invalid
add action=drop chain=forward comment="Drop all from WAN not DSTNATed " connection-nat-state=!dstnat connection-state=new in-interface-list=WAN
/interface list member add interface=bridge-local list=LAN
/interface list member add interface=cloud-vpn  list=LAN
/interface list member add interface=ether1 list=WAN
/tool netwatch add comment=VPNallowAny down-script="/ip firewall filter set [find comment=\"Drop Tiamviewer Anydesk\"] disabled=yes\r\ \n/ip firewall connection remove [find]" host=10.10.10.1 interval=5m timeout=500ms up-script="/ip firewall filter set [find comment=\"Drop Tiamviewer Anydesk\"] disabled=no\r\ \n/ip firewall connection remove [find]"
================================================

File: mikrotikltever3.j2
================================================
/system identity set name={{identity}}
/interface bridge add name=bridge-local
#/interface bridge port add interface=ether1 bridge=bridge-local
/interface bridge port add interface=ether2 bridge=bridge-local
/interface bridge port add interface=ether3 bridge=bridge-local
/interface bridge port add interface=ether4 bridge=bridge-local
#/interface bridge port add interface=ether5 bridge=bridge-local 
/ip address add address="{{dhcp}}.254/24" interface=bridge-local comment=LAN
/ip pool add name=dhcppool ranges={{dhcp}}.1-{{dhcp}}.253
/ip dhcp-server add name=dhcp interface=bridge-local lease-time=12h address-pool=dhcppool disabled=no
/ip dhcp-server network  add address={{dhcp}}.0/24 gateway={{dhcp}}.254 dns-server={{dhcp}}.254,8.8.8.8 domain=365-cloud.local comment=dhcp-local
/ip service disable telnet
/ip service disable api
/ip service disable api-ssl
/ip service disable ftp
/ip service set www address={{dhcp}}.0/24,10.10.0.0/16
/ip service set ssh address=10.10.0.0/16
/ip service set winbox address=0.0.0.0/0
/interface list add name=LAN
/interface list add name=WAN
/ip neighbor discovery-settings set discover-interface-list=LAN
/tool mac-server mac-winbox set allowed-interface-list=LAN
/tool mac-server set allowed-interface-list=LAN
/interface l2tp-client add name=cloud-vpn user={{l2tpuser}} password={{l2tppass}} allow=mschap2 connect-to={{vpn_address}} ipsec-secret={{ipseckey}} use-ipsec=yes disabled=no comment=Vpn
/ip route add distance=1 dst-address=10.10.0.0/16 gateway=cloud-vpn comment=ofisroute
#/ip dhcp-client remove [find interface=lte1]
#/ip dhcp-client add interface=lte1 add-default-route=yes use-peer-dns=yes use-peer-ntp=yes disabled=yes comment=Clientlte1
#/ip dhcp-client add interface=ether1 add-default-route=yes use-peer-dns=yes use-peer-ntp=yes disabled=no comment=WAN
/ip firewall nat add action=masquerade chain=srcnat out-interface-list=WAN comment=WAN   
/ip dns set allow-remote-requests=yes
/system clock set time-zone-name=Europe/Moscow time-zone-autodetect=no 
/user
add group=full name={{ansible_user}} password={{ansible_password}} address=10.10.0.0/16
/system script remove [find name=addresslist]
#ver 6.42
/system script
add name=addresslist owner=administrator policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/\
    ip firewall address-list\r\
    \n:foreach i in=[find (list=rabota) or (list=rdp) or (list=socialnetwork) \
    or (list=znakomstva) or (list=videohost)or (list=ammyy)] do={\r\
    \n  :do {\r\
    \n      remove \$i;\r\
    \n  } on-error={ :put \"OK addresslist\"};\r\
    \n }"
/system script run addresslist 
/ip firewall layer7-protocol
add name=teamviewer regexp="^(post|get) /d(out|in).aspx\\\?.*client=dyngate"
add name=teamviewer1 regexp="^\\x17"
/ip firewall mangle
add action=mark-connection chain=prerouting comment=Youtube connection-mark=no-mark new-connection-mark=youtube-conn passthrough=yes protocol=tcp tls-host=*youtube.com
add action=mark-packet chain=prerouting comment=Youtube connection-mark=youtube-conn new-packet-mark=youtube-packet passthrough=yes
add action=mark-connection chain=prerouting comment=Teamviewer new-connection-mark=tiamviewer-conn passthrough=yes protocol=tcp tls-host=*teamviewer.com
add action=mark-packet chain=prerouting comment=Teamviewer connection-mark=tiamviewer-conn new-packet-mark=teamviewer-packet passthrough=yes
/ip firewall service-port set sip disabled=yes
/ip firewall address-list
add address=10.10.0.0/24 list=allowmikrotik
add address=10.10.99.0/24 list=allowmikrotik
add address=10.10.97.0/24 list=allowmikrotik
add address=10.10.1.0/24 list=allowmikrotik
add address=vk.com list=socialnetwork
add address=ok.ru list=socialnetwork
add address=instagram.com list=socialnetwork
add address=facebook.com list=socialnetwork
add address=ru-ru.facebook.com list=socialnetwork
add address=twitter.com list=socialnetwork
add address=linkedin.com list=socialnetwork
add address=pinterest.com list=socialnetwork
add address=pinterest.ru list=socialnetwork
add address=tumblr.com list=socialnetwork
add address=flickr.com list=socialnetwork
add address=myspace.com list=socialnetwork
add address=meetup.com list=socialnetwork
add address=tagged.com list=socialnetwork
add address=ask.fm list=socialnetwork
add address=meetme.com list=socialnetwork
add address=classmates.com list=socialnetwork
add address=loveplanet.ru list=znakomstva
add address=mamba.ru list=znakomstva
add address=mylove.ru list=znakomstva
add address=badoo.com list=znakomstva
add address=24open.ru list=znakomstva
add address=dating.ru list=znakomstva
add address=fotostrana.ru list=znakomstva
add address=tabor.ru list=znakomstva
add address=znakomstva.ru list=znakomstva
add address=maybe.ru list=znakomstva
add address=hh.ru list=rabota
add address=superjob.ru list=rabota
add address=avito.ru list=rabota
add address=moscow.hh.ru list=rabota
add address=job.ru list=rabota
add address=rabota.ru list=rabota
add address=zarplata.ru list=rabota
add address=rabota.mail.ru list=rabota
add address=vakant.ru list=rabota
add address=gorodrabot.ru list=rabota
add address=rosrabota.ru list=rabota
add address=jobmarket.ru list=rabota
add address=career.ru list=rabota
add address=trud.com list=rabota
add address=trudbox.com list=rabota
add address=job-mo.ru list=rabota
add address=job.ws list=rabota
add address=jobinmoscow.ru list=rabota
add address=careerist.ru list=rabota
add address=adzuna.ru list=rabota
add address=jobijoba.ru list=rabota
add address=vimeo.com list=videohost
add address=rutube.ru list=videohost
add address=ivi.ru list=videohost
add address=video.mail.ru list=videohost
add address=smotri.com list=videohost
add address=teamviewer.com list=rdp
add address=ammyy.com list=rdp
add address=anydesk.com list=rdp
add address=relays.net.anydesk.com list=rdp
add address=21.111.200.64 list=ammyy
add address=23.105.254.132 list=ammyy
add address=136.243.18.81 list=ammyy
add address=24.111.200.64 list=ammyy
add address=rl.ammyy.com list=ammyy
add address=194.54.15.25 comment=Sberbank list=kassa-allowed-ip-dst
add address=194.54.14.89 comment=Sberbank list=kassa-allowed-ip-dst
add address=194.54.14.162 comment=Sberbank list=kassa-allowed-ip-dst
add address=91.213.144.29 comment=OFD list=kassa-allowed-ip-dst
add address=10.10.143.242 comment=K4 list=kassy-ip-src
add address=10.10.0.0/16 comment=Local list=kassa-allowed-ip-dst
add address=edge.365-cloud.ru comment=edge list=kassa-allowed-ip-dst
add address=kitchen.365-cloud.ru comment=kitchen list=kassa-allowed-ip-dst
add address=esm.365-cloud.ru comment=esm list=kassa-allowed-ip-dst
add address=ntp.ubuntu.com comment=ntp list=kassa-allowed-ip-dst
add address=docker.io comment="DOCKER HUB" list=kassa-allowed-ip-dst
add address=registry-1.docker.io list=kassa-allowed-ip-dst
add address=production.cloudflare.docker.com list=kassa-allowed-ip-dst
add address=ru.archive.ubuntu.com comment=Ubuntu-Update list=kassa-allowed-ip-dst
add address=security.ubuntu.com comment=Ubuntu-Update list=kassa-allowed-ip-dst
add address=kkt.sbis.ru comment=OFD list=kassa-allowed-ip-dst
#/ip firewall filter add action=accept chain=input dst-port=1701,500,4500 protocol=udp comment="l2tpports"
/ip firewall filter add action=accept chain=input connection-state=established,related,untracked comment="Allowestablished"
/ip firewall filter add action=drop chain=input dst-port=8291 protocol=tcp src-address-list=!allowmikrotik comment="Drop Winbox"
/ip firewall filter add action=drop chain=input dst-port=53 in-interface-list=WAN protocol=udp comment="DNSudp"
/ip firewall filter add action=drop chain=input dst-port=53 in-interface-list=WAN protocol=tcp comment="DNStcp"
/ip firewall filter add action=drop chain=input connection-state=invalid comment="Invalid"
/ip firewall filter add action=drop chain=input in-interface-list=WAN comment="DropWAN"
/ip firewall filter
add action=reject chain=forward comment="Block rabota" dst-address-list=rabota dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Block Socialnetwork" dst-address-list=socialnetwork dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Block znakomstva" dst-address-list=znakomstva dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Block videohost" dst-address-list=videohost dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Mail Google" content=mail.google.com dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Mail Yandex" content=mail.yandex.ru dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Mail rambler" content=mail.rambler.ru dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Mail Mail" content=e.mail.ru dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Drop Youtube" packet-mark=youtube-packet dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=reject chain=forward comment="Youtube" content=youtube.com dst-port=80,443 protocol=tcp reject-with=tcp-reset
add action=drop chain=forward comment="Teamviewer Site" packet-mark=teamviewer-packet
add action=drop chain=forward comment="Teamviewer" content=teamviewer.com
add action=drop chain=forward comment="Drop Tiamviewer" layer7-protocol=teamviewer
add action=drop chain=forward comment="Drop Tiamviewer" layer7-protocol=teamviewer1
add action=drop chain=forward comment="Drop Tiamviewer Anydesk" dst-address-list=rdp
add action=drop chain=forward comment="Drop AmmyyAdmin" dst-address-list=ammyy
add action=drop chain=forward comment="Teamviewer" dst-port=5938 protocol=tcp
add action=drop chain=forward comment="Teamviewer" dst-port=5938 protocol=udp
add action=drop chain=forward comment=Kassy dst-address-list=!kassa-allowed-ip-dst log-prefix=kassy src-address-list=kassy-ip-src
add action=accept chain=forward comment="Established,related" connection-state=established,related
add action=drop chain=forward comment="Invalid" connection-state=invalid
add action=drop chain=forward comment="Drop all from WAN not DSTNATed " connection-nat-state=!dstnat connection-state=new in-interface-list=WAN
/interface list member add interface=bridge-local list=LAN
/interface list member add interface=cloud-vpn  list=LAN
/interface list member add interface=ether1 list=WAN
/interface list member add interface=lte1 list=WAN
/tool netwatch add comment=VPNallowAny down-script="/ip firewall filter set [find comment=\"Drop Tiamviewer Anydesk\"] disabled=yes\r\ \n/ip firewall connection remove [find]" host=10.10.10.1 interval=5m timeout=500ms up-script="/ip firewall filter set [find comment=\"Drop Tiamviewer Anydesk\"] disabled=no\r\ \n/ip firewall connection remove [find]"
================================================

File: 1.rsc
================================================
1