# Repository Information
Name: generate-mac-address-mikrotik

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
	url = https://gitlab.com/pradha/generate-mac-address-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: README.md
================================================
# Generate MAC Address Mikrotik
This script can update your mikrotik with random mac address  
================================================

File: script
================================================
:local hash ([/certificate scep-server otp generate minutes-valid=0 as-value]->"password");
:log warning $hash
:local mac1 [:pick $hash 0 2]
:local mac2 [:pick $hash 2 4]
:local mac3 [:pick $hash 4 6]
:local mac4 [:pick $hash 6 8]
:local mac5 [:pick $hash 8 10]
:local mac6 [:pick $hash 10 12]
:local macAddr "$mac1:$mac2:$mac3:$mac4:$mac5:$mac6"
:log info $macAddr
/interface ethernet set <your ather name> mac-address=$macAddr