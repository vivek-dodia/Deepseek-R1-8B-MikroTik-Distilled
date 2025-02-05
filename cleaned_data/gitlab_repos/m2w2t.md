# Repository Information
Name: m2w2t

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
	url = https://gitlab.com/billbuchan/m2w2t.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: host1.sh
================================================
# So here's a shell script that sets our five environment variables
# for each host, and then switches the terraform workspace
# Please don't try and hit my router.
# set the IP address or hostname of the router
export TF_VAR_host=192.168.0.10
export MIKROTIK_HOST=http://$TF_VAR_host
# the username that terraform should use to log in
export MIKROTIK_USER=admin
# and it's password
export MIKROTIK_PASSWORD=youneedtochangethis
# We'll use the insecure methods as we're using http
# instead of https
export MIKROTIK_INSECURE=true
# Now switch terraform workspace so that each host gets it's
# own workspace, and therefore state file.
terraform workspace select "$TF_VAR_host" || terraform workspace new "$TF_VAR_host"
================================================

File: LICENSE
================================================
MIT No Attribution
Copyright 2024 Bill Buchan
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so.
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
# Make Mikrotik go write with Terraform (m2w2t)
## Description
This is an exercise in making Terraform play nice with Mikrotik routers, and therefore aid large scale Mikrotik management.
## Installation
Please
- Install terraform
- Clone this locally
- Read the presentations
- Update the host.sh file with your own config
- run the host.sh file
- edit the main.tf file to reflect your own environment
- edit the variables.tf file to reflect your own enviornment
- then run 'terraform init'
- and then run 'terraform plan' to see what changes it'll make
- If you're feeling brave, run 'terraform apply'...
## Usage
This was developed in order to demonstrate how to use Terraform to control a large Mikrotik fleet.
## Support
There is none. 
## Authors and acknowledgment
I'm Bill Buchan
- Founder, Director and tea-lady for Marykirk.com - a WISP/FISP based in Aberdeenshire, Scotland
- A long-term enterprise and government IT consultant, specalising in security
## License
This is MIT Licensed. Fill yer boots. See attached license file.
## Version
#### 1.0
- Released September 2024 for the UK WISPA conference in Edinburgh.
================================================