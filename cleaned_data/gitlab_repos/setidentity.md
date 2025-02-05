# Repository Information
Name: setidentity

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
	url = https://gitlab.com/rachuna-net.pl/tools/ansibleroles/mikrotik/setidentity.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "develop"]
	remote = origin
	merge = refs/heads/develop
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: CHANGELOG.md
================================================
# 1.0.0
- Ustawienie nazwy routera
- Ustawienie rekordu DNS
================================================

File: main.yml
================================================
input_role_ansible_host:     "{{ ansible_host }}"
input_role_router_ip:        ""
================================================

File: main.yml
================================================
galaxy_info:
  author: Maciej Rachuna
  description: Set identity in mikrotik
  company: rachuna-net.pl
  license: BSD 3-Clause
  min_ansible_version: 2.9
  platforms:
  - name: RouterOs
    versions:
    - all
  galaxy_tags: [
    "system",
    "mikrotik",
    "identity",
  ]
dependencies: []
================================================

File: README.md
================================================
# setidentity
Ansible Role - Mikrotik - Set Identity
### Wymagania
```bash
apt-get install sshpass python3-pip
pip install paramiko
```
# Zmienne
Role Variables
--------------
Defaults role values:
```yaml
input_role_groups: []
input_role_users: []
```
# Przykładowy playbook
```yaml
- hosts: all
  gather_facts: yes
  tasks:
  - include_role:
      name: setidentity
    vars:
        input_role_ansible_host:              "{{ inventory_hostname }}"
        input_role_router_ip:                 "{{ ansible_host }}"
```
### CHANGELOG
[CHANGELOG](CHANGELOG.md)
## License
BSD 3-Clause
Author Information
------------------
### Maciej Rachuna
SysOps/DevOps
================================================

File: main.yml
================================================
- name: "[MikroTik] Set identity"
  routeros_command:
    commands:
      - /system identity set name="{{ input_role_ansible_host }}"
  register: set_identity_status
- name: "[MikroTik] Create dns record for router"
  routeros_command:
    commands:
    - :if ([/ip dns static find name={{ input_role_ansible_host }} ])
      do={
        /ip dns static set [ find name={{ input_role_ansible_host }} ]
        address={{ input_role_router_ip }}
        comment={{ input_role_ansible_host }}={{ input_role_ansible_host }}
        ttl=1d
      }
      else={
        /ip dns static add name={{ input_role_ansible_host }}
        address={{ input_role_router_ip }}
        comment={{ input_role_ansible_host }}
        ttl=1d
      }
  when:
    - input_role_router_ip != ""
    - input_role_ansible_host != ""