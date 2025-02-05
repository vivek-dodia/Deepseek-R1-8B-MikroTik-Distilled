# Repository Information
Name: mikrotik-tunnel

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
	url = https://gitlab.com/public503/mikrotik-tunnel.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: cron.sh
================================================
sleep 10
cd /mikrotik-tunnel/home;   sudo bash ./loop > ./log 2>&1 &
cd /mikrotik-tunnel/radius; sudo bash ./loop > ./log 2>&1 &
================================================

File: install.txt
================================================
# put in /etc/rc.local
sudo bash /mikrotik-tunnel/cron.sh
================================================