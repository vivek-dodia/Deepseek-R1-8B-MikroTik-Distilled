# Repository Information
Name: block

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
	url = https://gitlab.com/mrehak/block.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: README.md
================================================
The block.pl script can watch suricata output eve.json file and update the IP address list on Mikrotik router. It is designed as a trivial IDS system.
You have to configure suricata system first. Than, you have to configure Mikrotik router to block IPs on the list. It is written basically for FreeBSD system but it could be easilly adoped to any other UNIX system.
================================================