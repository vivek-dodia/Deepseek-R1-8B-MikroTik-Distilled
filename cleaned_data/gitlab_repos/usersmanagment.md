# Repository Information
Name: usersmanagment

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
	url = https://gitlab.com/rachuna-net.pl/tools/ansibleroles/mikrotik/usersmanagment.git
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
- Zarządzanie grupami użytkowników
- Zarządzanie użytkownikami
================================================

File: main.yml
================================================
input_role_groups: []
input_role_users:  []
#### Example Configuration
#
# input_role_groups:
#   ansible:
#     name: ansible
#     policy:
#     - "sensitive"
#     - "ssh"
#     - "ftp"
#     - "reboot"
#     - "read"
#     - "write"
#     - "policy"
#     - "password"
#     - "web"
#     - "api"
#     - "!rest-api"
#     - "romon"
#     - "sniff"
#     - "!local"
#     - "!winbox"
#     - "test"
#     - "!telnet"
#     state: present
#
# input_role_users:
#   ansible:
#     name: "{{ lookup('hashi_vault', 'secret=secrets/rnp/internal/mikrotik:ansible_username')}}"
#     group: "ansible-accounts"
#     comment: Technical Account
#     state: present
#     address:
#     - 10.1.0.0/24
#     - 10.0.0.0/24
#     - 10.2.0.0/24
#     - 10.3.0.0/24
#     - 192.168.88.0/24
#     password: "{{ lookup('hashi_vault', 'secret=secrets/rnp/internal/mikrotik:ansible_password')}}"
#     ss_publickey: ""
================================================

File: main.yml
================================================
galaxy_info:
  author: Maciej Rachuna
  description: Users managment on mikrotik
  company: rachuna-net.pl
  license: BSD 3-Clause
  min_ansible_version: "2.10"
  platforms:
  - name: RouterOs
    versions:
    - all
  galaxy_tags: [
    "system",
    "mikrotik",
    "backup",
  ]
dependencies: []
================================================

File: README.md
================================================
# usersmanagment
Ansible Role - Mikrotik - Users Managment
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
      name: rnp-tools-ansibleroles-mikrotik-usersmanagment
    vars:
      input_role_groups:
        ansible:
          name: ansible
          policy:
          - "sensitive"
          - "ssh"
          - "ftp"
          - "reboot"
          - "read"
          - "write"
          - "policy"
          - "password"
          - "web"
          - "api"
          - "!rest-api"
          - "romon"
          - "sniff"
          - "!local"
          - "!winbox"
          - "test"
          - "!telnet"
          state: present
      input_role_users:
        ansible:
          name: ansible
          group: full
          comment: Technical Account
          state: present
          address:
            - 0.0.0.0/24
          password: "(vault)"
          ss_publickey: ""
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

File: configure_groups.yml
================================================
- name: "[Groups] Create/Update {{ group_item.value.name }} group"
  register: group_status
  routeros_command:
    commands:
    - :if ([/user group find name="{{ group_item.value.name }}"] != "")
      do={
        /user group set [ find name="{{ group_item.value.name }}"]
        policy="{{ group_item.value.policy | join(',') }}"
        comment="{{ group_item.value.comment |default('') }}"
      }
      else={
        /user group add name="{{ group_item.value.name }}"
        policy="{{ group_item.value.policy | join(',') }}"
        comment="{{ group_item.value.comment |default('') }}"
      }
  when: group_item.value.state == "present"
- name: "[Groups] Remove {{ group_item.value.name }} group"
  register: remove_group_status
  routeros_command:
    commands:
      - :if ([/user group find name="{{ group_item.value.name }}"] != "")
        do={
          /user group remove [ find name="{{ group_item.value.name }}"]
        }
  when: group_item.value.state == "absent"
================================================

File: configure_users.yml
================================================
- name: "[Users] Create/Update {{ user_item.value.name }} user"
  register: user_status
  routeros_command:
    commands:
    - :if ([/user find name="{{ user_item.value.name }}"] != "")
      do={
        /user set [ find name="{{ user_item.value.name }}"]
        group="{{ user_item.value.group }}"
        comment="{{ user_item.value.comment |default('') }}"
        address="{{ user_item.value.address | join(',') }}"
        disabled={{ user_item.value.disabled  | default('no') }}
        {% if user_item.value.password is defined %}password="{{ user_item.value.password }}"{% endif %}
      }
      else={
        /user add name="{{ user_item.value.name }}"
        group="{{ user_item.value.group }}"
        comment="{{ user_item.value.comment |default('') }}"
        address="{{ user_item.value.address | join(',') }}"
        disabled="{{ user_item.value.disabled | default('no') }}"
        password="{{ user_item.value.password | default('') }}"
      }
  when: user_item.value.state == "present"
- name: "[Users] Remove {{ user_item.value.name }} user"
  register: user_status
  routeros_command:
    commands:
    - :if ([/user find name="{{ user_item.value.name }}"] != "")
      do={
        /user remove [ find name="{{ user_item.value.name }}"]
      }
  when: user_item.value.state == "absent"
- name: "[Users] Add/Update ssh key for {{ user_item.value.name }} user"
  routeros_command:
    commands:
    - /file print file={{ user_item.value.name }}.pub
    - :delay 2
    - /file set {{ user_item.value.name }}.pub.txt contents="{{ user_item.value.ssh_publickey }}"
    - /user/ssh-keys/remove numbers=[/user/ssh-keys/find user="{{ user_item.value.name }}"]
    - /user ssh-keys import public-key-file="{{ user_item.value.name }}.pub.txt" user="{{ user_item.value.name }}" }
    - :if ([/file/find name="{{ user_item.value.name }}.pub.txt"] !="")
      do={ /file/remove {{ user_item.value.name }}.pub.txt }
  when:
    - user_item.value.state == "present"
    - user_item.value.ssh_publickey is defined
    - user_item.value.ssh_publickey != ""
================================================

File: main.yml
================================================
- include: setup_role.yml
- include: configure_groups.yml
  no_log: true
  loop: "{{ lookup('dict', var_role_groups) }}"
  loop_control:
    loop_var: group_item
  when:
    - var_role_groups is defined
    - group_item.key != "default"
- include: configure_users.yml
  no_log: true
  loop: "{{ lookup('dict', var_role_users) }}"
  loop_control:
    loop_var: user_item
  when:
    - var_role_users is defined
    - user_item.key != "default"
================================================

File: setup_role.yml
================================================
- name: "[Setup] Set variables"
  set_fact:
    var_role_groups: "{{ input_role_groups | combine({'default': '' }) }}"
    var_role_users: "{{ input_role_users | combine({'default': '' }) }}"