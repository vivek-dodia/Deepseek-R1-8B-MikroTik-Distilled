# Repository Information
Name: cert.pl-hole-for-mikrotik

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
	url = https://gitlab.com/joystick-security/mikrotik/cert.pl-hole-for-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: install-cert.pl-hole-for-mikrotik-dns.md
================================================
## Install cert.pl-hole-for-mikrotik-dns
download install-dns.rsc
```
/tool fetch url="https://gitlab.com/joystick-security/mikrotik/cert.pl-hole-for-mikrotik/-/raw/main/install-dns.rsc" mode=https
```
run script in terminal
```
/import file-name=install-dns.rsc
```
**Auto update is included in the installation script** -> [install-dns.rsc](https://gitlab.com/joystick-security/mikrotik/cert.pl-hole-for-mikrotik/-/raw/main/install-dns.rsc)
**Important**
[cert.pl-hole-for-mikrotik-dns.rsc](https://gitlab.com/joystick-security/mikrotik/cert.pl-hole-for-mikrotik/-/raw/main/cert.pl-hole-for-mikrotik-dns.rsc) is is generated and uploaded to this repository daily before 2:00 AM (**UTC+0**).
| Scheduler |
| ------ |
cert.pl-hole-for-mikrotik-download starts at 02:05 AM (router time).
cert.pl-hole-for-mikrotik-autoupdate starts at 02:10 AM (router time).
================================================

File: install-cert.pl-hole-for-mikrotik.md
================================================
## Install cert.pl-hole-for-mikrotik
download install.rsc
```
/tool fetch url="https://gitlab.com/joystick-security/mikrotik/cert.pl-hole-for-mikrotik/-/raw/main/install.rsc" mode=https
```
run script in terminal
```
/import file-name=install.rsc
```
**Auto update is included in the installation script** -> [install.rsc](https://gitlab.com/joystick-security/mikrotik/cert.pl-hole-for-mikrotik/-/raw/main/install.rsc)
**Important**
[cert.pl-hole-for-mikrotik.rsc](https://gitlab.com/joystick-security/mikrotik/cert.pl-hole-for-mikrotik/-/raw/main/cert.pl-hole-for-mikrotik.rsc) is is generated and uploaded to this repository daily before 2:00 AM (**UTC+0**).
| Scheduler |
| ------ |
cert.pl-hole-for-mikrotik-download starts at 02:05 AM (router time).
cert.pl-hole-for-mikrotik-autoupdate starts at 02:10 AM (router time).
================================================

File: install-dns.rsc
================================================
/system script 
add name="cert.pl-hole-for-mikrotik-dns-download" source={/tool fetch url="https://gitlab.com/joystick-security/mikrotik/cert.pl-hole-for-mikrotik/-/raw/main/cert.pl-hole-for-mikrotik-dns.rsc" mode=https}
add name="cert.pl-hole-for-mikrotik-dns-autoupdate" source={/ip dns static
:foreach i in=[find comment=cert.pl-hole-for-mikrotik-dns] do={
  :do {
      remove $i;
  } on-error={ :put "cannot be deleted"};
 };
/import file-name=cert.pl-hole-for-mikrotik-dns.rsc;
/file remove cert.pl-hole-for-mikrotik-dns.rsc}
/system scheduler 
add interval=24h name="cert.pl-hole-for-mikrotik-dns-download" start-time=02:05:00 on-event=cert.pl-hole-for-mikrotik-dns-download
add interval=24h name="cert.pl-hole-for-mikrotik-dns-autoupdate" start-time=02:10:00 on-event=cert.pl-hole-for-mikrotik-dns-autoupdate
================================================

File: install.rsc
================================================
/system script 
add name="cert.pl-hole-for-mikrotik-download" source={/tool fetch url="https://gitlab.com/joystick-security/mikrotik/cert.pl-hole-for-mikrotik/-/raw/main/cert.pl-hole-for-mikrotik.rsc" mode=https}
add name="cert.pl-hole-for-mikrotik-autoupdate" source={/ip firewall address-list
:foreach i in=[find list=cert.pl-hole-for-mikrotik] do={
  :do {
      remove $i;
  } on-error={ :put "cannot be deleted"};
 };
/import file-name=cert.pl-hole-for-mikrotik.rsc;
/file remove cert.pl-hole-for-mikrotik.rsc}
/system scheduler 
add interval=24h name="cert.pl-hole-for-mikrotik-download" start-time=02:05:00 on-event=cert.pl-hole-for-mikrotik-download
add interval=24h name="cert.pl-hole-for-mikrotik-autoupdate" start-time=02:10:00 on-event=cert.pl-hole-for-mikrotik-autoupdate
/ip firewall filter
add chain=forward dst-address-list="cert.pl-hole-for-mikrotik" action=drop log=yes log-prefix="cert.pl-hole-for-mikrotik"
================================================

File: README.md
================================================
# CERT.pl hole for mikrotik
> https://cert.pl/en/posts/2020/03/malicious_domains/
Original .rsc list is truncated to 4096 bytes. I decided to generate a complete list based on https://hole.cert.pl/domains/domains.txt <br /><br />
In the cert.pl-hole-for-mikrotik.rsc file, I especially add FQDN to the firewall address-list. Because MikroTik can transform FQDN into IP addresses dynamically. So if a malicious website changes IP address and FQDN remains unchanged it will protect us again. It's also a plus if the malicious site has multiple A records. <br />
[Install version with FQDN](https://gitlab.com/joystick-security/mikrotik/cert.pl-hole-for-mikrotik/-/blob/main/install-cert.pl-hole-for-mikrotik.md)
The version with static DNS records, which is the most accurate. <br />
For this option to work we need to make sure that **DoH/DoT is disabled in the web browser.** <br />
[Install version with DNS](https://gitlab.com/joystick-security/mikrotik/cert.pl-hole-for-mikrotik/-/blob/main/install-cert.pl-hole-for-mikrotik-dns.md)
**I recommend a minimum of 512MB RAM on the router.**