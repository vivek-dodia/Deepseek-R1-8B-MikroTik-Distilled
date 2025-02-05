# Repository Information
Name: terraform-provider-mikrotik

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
	url = https://gitlab.com/ddelnano/terraform-provider-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "add-travis-ci-build"]
	remote = origin
	merge = refs/heads/add-travis-ci-build
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: .travis.yml
================================================
language: go
go:
- 1.11.x
- 1.12.x
script:
  - GO111MODULE=on go build
================================================

File: README.md
================================================
## Intro
This is an experiemental terraform provider for managing your Mikrotik's router's DNS. It allows you to create records via the routeos API.
## Examples
Creating a new DNS record
```terraform
provider "mikrotik" {
  host = "http://router:8728" # Or set MIKROTIK_HOST
  username = "username of api user" # Or set MIKROTIK_USER
  password = "xxxxxx" #  # Or set MIKROTIK_PASSWORD
}
resource "mikrotik_dns_record" "www" {
    name = "router"
    address = "192.168.88.1"
    ttl = 300
}
```
## Todo
- [ ] Add Travis test suite
- [ ] Add more rigorious Terraform tests
- [ ] Resource reading needs to be more robust so the terraform plan does not think it needs to recreate everything when really the state is fine.