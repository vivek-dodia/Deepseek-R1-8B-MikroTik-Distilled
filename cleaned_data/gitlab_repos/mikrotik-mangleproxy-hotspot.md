# Repository Information
Name: mikrotik-mangleproxy-hotspot

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
	url = https://gitlab.com/ekohendratno/mikrotik-mangleproxy-hotspot.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: config.src
================================================
/ip firewall mangle
add action=mark-connection chain=prerouting disabled=no dst-address-type=!local hotspot=auth in-interface=bridge1 new-connection-mark=WAN_conn passthrough=yes per-connection-classifier=both-addresses-and-ports:1/0
================================================

File: README.md
================================================
# mikrotik-mangleproxy-hotspot
================================================