# Repository Information
Name: bak-ros

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
	url = https://gitlab.com/elektro-potkan/bak-ros.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: bakRouterOS
================================================
#!/bin/bash
# retrieve data
DATA=`\
	eval "$1 '/system package print where disabled=no; / export terse'" \
	| tr --delete "\r" \
`
# search for packages end
BREAK=`echo "$DATA" \
	| grep --line-number --max-count=1 '^$' \
	| cut --delimiter=':' --fields=1 \
`
OS_LINE=`expr $BREAK + 1`
PKGS_END=`expr $BREAK - 1`
EXPORT_BEGIN=`expr $BREAK + 3`
# extract the RouterOS version
OS=`echo "$DATA" \
	| head --lines="$OS_LINE" \
	| tail --lines=1 \
	| cut --delimiter=' ' --fields=5- \
	| while read line; do echo "# $line"; done \
`
# process packages
PKGS=`echo "$DATA" \
	| head --lines="$PKGS_END" \
	| tail --lines=+3 \
	| cut --delimiter=' ' --fields=5 \
	| sort \
	| while read line; do echo "# - $line"; done \
`
# get the main export
MAIN=`echo "$DATA" \
	| tail --lines="+$EXPORT_BEGIN"
`
# replace line-breaks made by active CAPsMAN
MAIN=`echo "$MAIN" \
	|perl -0pe 's/^\/interface wireless\n# managed by CAPsMAN(\n# .*)*\nset/\/interface wireless set/gm' \
	|perl -0pe 's/^\/interface wireless cap\n# \nset/\/interface wireless cap set/m' \
`
# remove unnecessary lines
MAIN=`echo "$MAIN" \
	|perl -0pe 's/^\/interface wireless set \[ find default-name=wlan[0-9] \]( disabled=no)? ssid=MikroTik\n//gm' \
	|perl -0pe 's/^\/interface wireless security-profiles set \[ find default=yes \] supplicant-identity=MikroTik\n//m' \
`
# output
printf "%s\n" \
	"$OS" \
	"$PKGS" \
	"$MAIN"
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2022 Elektro-potkan
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

File: README.md
================================================
RouterOS Backup script
======================
Bash scripts for back-up of MikroTik RouterOS devices configuration.
Usage
-----
```bash
echo 'Exporting MyRouter...'
bakRouterOS 'ssh 10.0.0.1' > my_router.rsc
echo 'Exporting MyGW...'
bakRouterOS 'ssh admin@192.168.63.2 -p 4321' > my_gw.rsc
echo 'Exporting MyOtherRouter...'
bakRouterOS 'ssh -o PubkeyAcceptedKeyTypes=+ssh-rsa 123.145.167.189 -p 12345' > my_other_router.rsc
```
Since the `bakRouterOS` script was rewritten to output the export into stdout
(as that allows piping it into another filters, etc.),
there is no automatic echo of the `Exporting ... filename` line.
If You want it back, a simple function might be enough:
```bash
function echoSave {
	echo "Exporting... $1"
	cat > "$1"
}
bakRouterOS 'ssh 10.0.0.1' |echoSave my_router.rsc
bakRouterOS 'ssh admin@192.168.63.2 -p 4321' |echoSave my_gw.rsc
bakRouterOS 'ssh -o PubkeyAcceptedKeyTypes=+ssh-rsa 123.145.167.189 -p 12345' \
	|echoSave my_other_router.rsc
```
### RB4011
When exporting the configuration from RB4011 devices, there are lines like
`/interface ethernet switch port set 0 default-vlan-id=0`.
They are usually there, even when the router is reset into default config.
To remove them, pipe the export through `cleanRB4011` script:
```bash
echo 'Exporting MyRB4011...'
bakRouterOS 'ssh admin@192.168.63.2 -p 4321' \
	|cleanRB4011 \
	> my_rb4011.rsc
```
Author
------
Elektro-potkan <git@elektro-potkan.cz>
Info
----
### Versioning
This project uses [Semantic Versioning 2.0.0 (semver.org)](https://semver.org).
License
-------
This program is licensed under the MIT License.
See file [LICENSE](LICENSE).