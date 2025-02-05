# Repository Information
Name: mikrotik-conf

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
	url = https://gitlab.com/zbox-mirror/mikrotik-conf.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: mirror.yml
================================================
name: "Mirror"
on:
  - push
env:
  OWNER: "${{ github.repository_owner }}-mirror"
  USER_AGENT: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
jobs:
  # ------------------------------------------------------------------------------------------------------------------ #
  # GitHub.
  # ------------------------------------------------------------------------------------------------------------------ #
  mirror_github:
    runs-on: ubuntu-latest
    name: "GitHub"
    env:
      DOMAIN: "${{ github.server_url }}"
    steps:
      - name: "Get repository name"
        shell: bash
        run: |
          echo "REPO_NAME=$( echo '${{ github.repository }}' | awk -F '/' '{ print $2 }' )" >> $GITHUB_ENV
      - name: "Create repository"
        shell: bash
        run: |
          http="$( curl -s -o '/dev/null' -I -w '%{http_code}' -A '${{ env.USER_AGENT }}' '${{ github.server_url }}/${{ env.OWNER }}/${{ env.REPO_NAME }}' )"
          if [[ "${http}" -ne 200 ]]; then
            curl -X POST \
            -H 'Authorization: Bearer ${{ secrets.BOT_GITHUB_TOKEN }}' \
            -H 'Accept: application/vnd.github+json' \
            -A '${{ env.USER_AGENT }}' \
            '${{ github.api_url }}/orgs/${{ env.OWNER }}/repos' \
            -d '{"name":"${{ env.REPO_NAME }}","private":false,"has_issues":false,"has_projects":false,"has_wiki":false}'
          fi
      - name: "Mirror repository"
        uses: ghastore/mirror@main
        with:
          src_repo: "${{ github.server_url }}/${{ github.repository }}.git"
          src_user: "${{ secrets.BOT_GITHUB_NAME }}"
          src_token: "${{ secrets.BOT_GITHUB_TOKEN }}"
          dst_repo: "${{ env.DOMAIN }}/${{ env.OWNER }}/${{ env.REPO_NAME }}.git"
          dst_user: "${{ secrets.BOT_GITHUB_NAME }}"
          dst_token: "${{ secrets.BOT_GITHUB_TOKEN }}"
  # ------------------------------------------------------------------------------------------------------------------ #
  # GitLab.
  # ------------------------------------------------------------------------------------------------------------------ #
  mirror_gitlab:
    runs-on: ubuntu-latest
    name: "GitLab"
    env:
      DOMAIN: "https://gitlab.com"
      VERSION: "v4"
      NSID: '57669711'
    steps:
      - name: "Get repository name"
        shell: bash
        run: |
          echo "REPO_NAME=$( echo '${{ github.repository }}' | awk -F '/' '{ print $2 }' )" >> $GITHUB_ENV
      - name: "Create repository"
        shell: bash
        run: |
          http="$( curl -s -o '/dev/null' -I -w '%{http_code}' -A '${{ env.USER_AGENT }}' '${{ env.DOMAIN }}/${{ env.OWNER }}/${{ env.REPO_NAME }}' )"
          if [[ "${http}" -ne 200 ]]; then
            curl -X POST \
            -H 'Authorization: Bearer ${{ secrets.BOT_GITLAB_TOKEN }}' \
            -H 'Content-Type: application/json' \
            -A '${{ env.USER_AGENT }}' \
            '${{ env.DOMAIN }}/api/${{ env.VERSION }}/projects' \
            -d '{"name":"${{ env.REPO_NAME }}","path":"${{ env.REPO_NAME }}","namespace_id":"${{ env.NSID }}","visibility":"public","issues_access_level":"disabled","wiki_access_level":"disabled"}'
          fi
      - name: "Mirror repository"
        uses: ghastore/mirror@main
        with:
          src_repo: "${{ github.server_url }}/${{ github.repository }}.git"
          src_user: "${{ secrets.BOT_GITHUB_NAME }}"
          src_token: "${{ secrets.BOT_GITHUB_TOKEN }}"
          dst_repo: "${{ env.DOMAIN }}/${{ env.OWNER }}/${{ env.REPO_NAME }}.git"
          dst_user: "${{ secrets.BOT_GITLAB_NAME }}"
          dst_token: "${{ secrets.BOT_GITLAB_TOKEN }}"
  # ------------------------------------------------------------------------------------------------------------------ #
  # Codeberg.
  # ------------------------------------------------------------------------------------------------------------------ #
  mirror_codeberg:
    runs-on: ubuntu-latest
    name: "Codeberg"
    env:
      DOMAIN: "https://codeberg.org"
      VERSION: "v1"
    steps:
      - name: "Get repository name"
        shell: bash
        run: |
          echo "REPO_NAME=$( echo '${{ github.repository }}' | awk -F '/' '{ print $2 }' )" >> $GITHUB_ENV
      - name: "Create repository"
        shell: bash
        run: |
          http="$( curl -s -o '/dev/null' -I -w '%{http_code}' -A '${{ env.USER_AGENT }}' '${{ env.DOMAIN }}/${{ env.OWNER }}/${{ env.REPO_NAME }}' )"
          if [[ "${http}" -ne 200 ]]; then
            curl -X POST \
            -H 'Authorization: token ${{ secrets.BOT_CODEBERG_TOKEN }}' \
            -H 'Accept: application/json' \
            -H 'Content-Type: application/json' \
            -A '${{ env.USER_AGENT }}' \
            '${{ env.DOMAIN }}/api/${{ env.VERSION }}/orgs/${{ env.OWNER }}/repos' \
            -d '{"name":"${{ env.REPO_NAME }}"}'
          fi
      - name: "Mirror repository"
        uses: ghastore/mirror@main
        with:
          src_repo: "${{ github.server_url }}/${{ github.repository }}.git"
          src_user: "${{ secrets.BOT_GITHUB_NAME }}"
          src_token: "${{ secrets.BOT_GITHUB_TOKEN }}"
          dst_repo: "${{ env.DOMAIN }}/${{ env.OWNER }}/${{ env.REPO_NAME }}.git"
          dst_user: "${{ secrets.BOT_CODEBERG_NAME }}"
          dst_token: "${{ secrets.BOT_CODEBERG_TOKEN }}"
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2022 zBox Development Platform
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

File: rb2011.00.rsc
================================================
# DEFAULT COMMANDS:
# /tool fetch url="https://raw.githubusercontent.com/zbox/mikrotik-conf/main/rb2011.00.rsc" dst-path="ros.rb2011.00.rsc"
# /tool fetch url="https://curl.se/ca/cacert.pem" dst-path="ros.cacert.pem"
# /system reset-configuration no-defaults=yes skip-backup=yes run-after-reset="ros.rb2011.00.rsc"
# /certificate import file-name="ros.cacert.pem" passphrase="" name="ROS"
/interface bridge
add name=bridge1
/interface list
add name=WAN
add name=LAN
/ip pool
add name=dhcp ranges=10.0.250.1-10.0.255.254
/ip dhcp-server
add address-pool=dhcp interface=bridge1 name=dhcp1
/interface bridge port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
add bridge=bridge1 interface=ether6
add bridge=bridge1 interface=ether7
add bridge=bridge1 interface=ether8
add bridge=bridge1 interface=ether9
add bridge=bridge1 interface=ether10
/ipv6 settings
set disable-ipv6=yes
/interface list member
add interface=ether1 list=WAN
add interface=bridge1 list=LAN
/ip address
add address=10.0.0.1/16 interface=bridge1 network=10.0.0.0
/ip dhcp-client
add interface=ether1
/ip dhcp-server network
add address=10.0.0.0/16 dns-server=10.0.0.1,1.1.1.1,1.0.0.1 domain=home.lan gateway=10.0.0.1 ntp-server=10.0.0.1
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip dns static
add address=10.0.0.1 name=gw.lan comment="LAN Gateway"
/ip firewall filter
add action=accept chain=input connection-state=established,related,untracked comment="[ACCEPT] Established, Related, Untracked"
add action=drop chain=input connection-state=invalid comment="[DROP] Invalid"
add action=accept chain=input protocol=icmp comment="[ACCEPT] ICMP"
add action=accept chain=input dst-port=9090,22022 protocol=tcp comment="[ROS] WinBox and SSH"
add action=drop chain=input in-interface-list=!LAN comment="[DROP] All not coming from LAN"
add action=accept chain=forward ipsec-policy=in,ipsec comment="[ACCEPT] In IPsec policy"
add action=accept chain=forward ipsec-policy=out,ipsec comment="[ACCEPT] Out IPsec policy"
add action=fasttrack-connection chain=forward connection-state=established,related comment="[ROS] FastTrack"
add action=accept chain=forward connection-state=established,related,untracked comment="[ROS] FastTrack"
add action=drop chain=forward connection-state=invalid comment="[DROP] Invalid"
add action=drop chain=forward connection-nat-state=!dstnat connection-state=new in-interface-list=WAN comment="[DROP] All from WAN not DSTNATed"
/ip firewall nat
add action=masquerade chain=srcnat out-interface-list=WAN
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set ssh port=22022
set api disabled=yes
set winbox port=9090
set api-ssl disabled=yes
/lcd
set enabled=no
/system clock
set time-zone-name=Europe/Moscow
/system identity
set name="GW-RB2011"
/system ntp client
set enabled=yes
/system ntp server
set enabled=yes manycast=yes multicast=yes
/system ntp client servers
add address=time.cloudflare.com
/tool bandwidth-server
set enabled=no
/tool mac-server
set allowed-interface-list=none
/tool mac-server ping
set enabled=no
/user
set [find name="admin"] password="qwerty1209"
================================================

File: rb2011.01.rsc
================================================
# DEFAULT COMMANDS:
# /tool fetch url="https://raw.githubusercontent.com/zbox/mikrotik-conf/main/rb2011.01.rsc" dst-path="ros.rb2011.01.rsc"
# /tool fetch url="https://curl.se/ca/cacert.pem" dst-path="ros.cacert.pem"
# /system reset-configuration no-defaults=yes skip-backup=yes run-after-reset="ros.rb2011.01.rsc"
# /certificate import file-name="ros.cacert.pem" passphrase="" name="ROS"
/interface bridge
add name=bridge1
/interface ethernet
set [ find default-name=ether1 ] mac-address=3C:97:0E:42:21:ED
/interface list
add name=WAN
add name=LAN
/ip pool
add name=dhcp ranges=10.0.250.1-10.0.255.254
/ip dhcp-server
add address-pool=dhcp interface=bridge1 name=dhcp1
/interface bridge port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
add bridge=bridge1 interface=ether6
add bridge=bridge1 interface=ether7
add bridge=bridge1 interface=ether8
add bridge=bridge1 interface=ether9
add bridge=bridge1 interface=ether10
/ipv6 settings
set disable-ipv6=yes
/interface list member
add interface=ether1 list=WAN
add interface=bridge1 list=LAN
/ip address
add address=10.0.0.1/16 interface=bridge1 network=10.0.0.0
/ip dhcp-client
add interface=ether1
/ip dhcp-server lease
add address=10.0.1.1 mac-address=14:EB:B6:B3:28:90 comment="TL-SG1024DE-01"
add address=10.0.2.1 mac-address=14:EB:B6:63:C6:09 comment="TL-SG108E-01"
add address=10.0.2.2 mac-address=B4:B0:24:92:E4:60 comment="TL-SG108E-02"
add address=10.0.3.1 mac-address=50:FF:20:79:B6:38 comment="KN-3510-01"
add address=10.0.5.1 mac-address=14:DA:E9:B3:A6:F5 comment="PVE-CRAFT"
add address=10.0.5.2 mac-address=AA:0D:0D:85:9A:A3 comment="PVE-CRAFT-01"
add address=10.0.5.3 mac-address=96:AD:F4:C8:12:2C comment="PVE-CRAFT-02"
/ip dhcp-server network
add address=10.0.0.0/16 dns-server=10.0.0.1,1.1.1.1,1.0.0.1 domain=home.lan gateway=10.0.0.1 ntp-server=10.0.0.1
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip dns static
add address=10.0.0.1 name=gw01.lan comment="LAN Gateway 01"
/ip firewall filter
add action=accept chain=input connection-state=established,related,untracked comment="[ACCEPT] Established, Related, Untracked"
add action=drop chain=input connection-state=invalid comment="[DROP] Invalid"
add action=accept chain=input protocol=icmp comment="[ACCEPT] ICMP"
add action=accept chain=input dst-port=9090,22022 protocol=tcp comment="[ROS] WinBox and SSH"
add action=drop chain=input in-interface-list=!LAN comment="[DROP] All not coming from LAN"
add action=accept chain=forward ipsec-policy=in,ipsec comment="[ACCEPT] In IPsec policy"
add action=accept chain=forward ipsec-policy=out,ipsec comment="[ACCEPT] Out IPsec policy"
add action=fasttrack-connection chain=forward connection-state=established,related comment="[ROS] FastTrack"
add action=accept chain=forward connection-state=established,related,untracked comment="[ROS] FastTrack"
add action=drop chain=forward connection-state=invalid comment="[DROP] Invalid"
add action=drop chain=forward connection-nat-state=!dstnat connection-state=new in-interface-list=WAN comment="[DROP] All from WAN not DSTNATed"
/ip firewall nat
add action=masquerade chain=srcnat out-interface-list=WAN
add action=dst-nat chain=dstnat dst-port=60511 protocol=tcp to-addresses=10.0.5.1 to-ports=8006 comment="PVE-CRAFT / ProxMox"
add action=dst-nat chain=dstnat dst-port=60521 protocol=tcp to-addresses=10.0.5.2 to-ports=22122 comment="PVE-CRAFT / 01 / SSH"
add action=dst-nat chain=dstnat dst-port=60522 protocol=tcp to-addresses=10.0.5.2 to-ports=8384 comment="PVE-CRAFT / 01 / Syncthing"
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set ssh port=22022
set api disabled=yes
set winbox port=9090
set api-ssl disabled=yes
/lcd
set enabled=no
/system clock
set time-zone-name=Europe/Moscow
/system identity
set name="GW-01"
/system ntp client
set enabled=yes
/system ntp server
set enabled=yes manycast=yes multicast=yes
/system ntp client servers
add address=time.cloudflare.com
/tool bandwidth-server
set enabled=no
/tool mac-server
set allowed-interface-list=none
/tool mac-server ping
set enabled=no
/user
set [find name="admin"] password="qwerty1209"
================================================

File: rb941.00.rsc
================================================
# DEFAULT COMMANDS:
# /tool fetch url="https://raw.githubusercontent.com/zbox/mikrotik-conf/main/rb941.00.rsc" dst-path="ros.rb941.00.rsc"
# /tool fetch url="https://curl.se/ca/cacert.pem" dst-path="ros.cacert.pem"
# /system reset-configuration no-defaults=yes skip-backup=yes run-after-reset="ros.rb941.00.rsc"
# /certificate import file-name="ros.cacert.pem" passphrase="" name="ROS"
/interface bridge
add name=bridge1
/interface list
add name=WAN
add name=LAN
/interface wireless security-profiles
add authentication-types=wpa2-psk mode=dynamic-keys name=security supplicant-identity="" wpa2-pre-shared-key="wifi-rb941"
/interface wireless
set [ find default-name="wlan1" ] band=2ghz-b/g/n channel-width=20/40mhz-XX country=russia4 disabled=no installation=indoor mode=ap-bridge security-profile=security ssid="GW-RB941" wps-mode=disabled
/ip pool
add name=dhcp ranges=192.168.88.10-192.168.88.254
/ip dhcp-server
add address-pool=dhcp interface=bridge1 name=dhcp1
/interface bridge port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=wlan1
/ipv6 settings
set disable-ipv6=yes
/interface list member
add interface=ether1 list=WAN
add interface=bridge1 list=LAN
/ip address
add address=192.168.88.1/24 interface=bridge1 network=192.168.88.0
/ip dhcp-client
add interface=ether1
/ip dhcp-server network
add address=192.168.88.0/24 dns-server=192.168.88.1,1.1.1.1,1.0.0.1 domain=home.lan gateway=192.168.88.1 ntp-server=192.168.88.1
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip dns static
add address=192.168.88.1 name=gw.lan comment="LAN Gateway"
/ip firewall filter
add action=accept chain=input connection-state=established,related,untracked comment="[ACCEPT] Established, Related, Untracked"
add action=drop chain=input connection-state=invalid comment="[DROP] Invalid"
add action=accept chain=input protocol=icmp comment="[ACCEPT] ICMP"
add action=accept chain=input dst-port=9090,22022 protocol=tcp comment="[ROS] WinBox and SSH"
add action=drop chain=input in-interface-list=!LAN comment="[DROP] All not coming from LAN"
add action=accept chain=forward ipsec-policy=in,ipsec comment="[ACCEPT] In IPsec policy"
add action=accept chain=forward ipsec-policy=out,ipsec comment="[ACCEPT] Out IPsec policy"
add action=fasttrack-connection chain=forward connection-state=established,related comment="[ROS] FastTrack"
add action=accept chain=forward connection-state=established,related,untracked comment="[ROS] FastTrack"
add action=drop chain=forward connection-state=invalid comment="[DROP] Invalid"
add action=drop chain=forward connection-nat-state=!dstnat connection-state=new in-interface-list=WAN comment="[DROP] All from WAN not DSTNATed"
/ip firewall nat
add action=masquerade chain=srcnat out-interface-list=WAN
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set ssh port=22022
set api disabled=yes
set winbox port=9090
set api-ssl disabled=yes
/system clock
set time-zone-name=Europe/Moscow
/system identity
set name="GW-RB941"
/system ntp client
set enabled=yes
/system ntp server
set enabled=yes manycast=yes multicast=yes
/system ntp client servers
add address=time.cloudflare.com
/tool bandwidth-server
set enabled=no
/tool mac-server
set allowed-interface-list=none
/tool mac-server ping
set enabled=no
/user
set [find name="admin"] password="qwerty1209"
================================================

File: README.md
================================================
# mikrotik-conf