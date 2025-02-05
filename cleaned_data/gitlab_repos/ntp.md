# Repository Information
Name: ntp

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
	url = https://gitlab.com/rachuna-net.pl/tools/ansibleroles/mikrotik/ntp.git
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
- Configure ntp client
================================================

File: main.yml
================================================
input_role_client_servers:
  enabled: "yes"
  servers:
  - address: 162.159.200.123
    min_poll: 6
    max-poll: 10
    iburst: "yes"
    auth-key: none
    state: present
  - address: 162.159.200.1
    min_poll: 6
    max-poll: 10
    iburst: "yes"
    auth-key: none
    state: present
================================================

File: README.md
================================================
# ntp
Ansible Role - Mikrotik - Configure NTP Client
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
input_role_client_servers:
  enabled: "yes"
  servers:
  - address: 162.159.200.123
    min_poll: 6
    max-poll: 10
    iburst: "yes"
    auth-key: none
    state: present
  - address: 162.159.200.1
    min_poll: 6
    max-poll: 10
    iburst: "yes"
    auth-key: none
    state: present
```
# Przykładowy playbook
```yaml
- hosts: all
  gather_facts: yes
  tasks:
  - include_role:
      name: mikrotik_ntp
    vars:
      input_role_client_servers:
        enabled: "yes"
        servers:
        - address: 162.159.200.123
          min_poll: 6
          max-poll: 10
          iburst: "yes"
          auth-key: none
          state: present
        - address: 162.159.200.1
          min_poll: 6
          max-poll: 10
          iburst: "yes"
          auth-key: none
          state: present
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
- name: "[MikroTik] [NTP Client] Create/Update ntp servers"
  register: update_ntp_client_servers
  no_log: true
  routeros_command:
    commands:
    - :if ([/system ntp client servers find address={{ item.address }} ])
      do={
        /system ntp client servers set [find address={{ item.address }} ]
        comment="{{ item.comment | default('') }}"
        disabled={{ item.disabled | default ('no') }}
        {% if item.auth_key is defined %} auth-key={{ item.auth_key }}{% endif %}
        {% if item.iburst is defined %} iburst={{ item.iburst }}{% endif %}
        {% if item.min_poll is defined %} min-poll={{ item.min_poll }}{% endif %}
        {% if item.max_poll is defined %} max-poll={{ item.max_poll }}{% endif %}
      }
      else={
        /system ntp client servers add address={{ item.address }}
        comment="{{ item.comment | default('') }}"
        disabled={{ item.disabled | default ('no') }}
        {% if item.auth_key is defined %} auth-key={{ item.auth_key }}{% endif %}
        {% if item.iburst is defined %} iburst={{ item.iburst }}{% endif %}
        {% if item.min_poll is defined %} min-poll={{ item.min_poll }}{% endif %}
        {% if item.max_poll is defined %} max-poll={{ item.max_poll }}{% endif %}
      }
  loop: "{{ input_role_client_servers.servers }}"
  when:
    - item.state == "present"
- name: "[MikroTik] [NTP Client] Remove ntp servers"
  register: remove_ntp_client_servers
  no_log: true
  routeros_command:
    commands:
    - :if ([/system ntp client servers find address={{ item.address }} ])
      do={
        /system ntp client servers remove [find address={{ item.address }}]
      }
  loop: "{{ input_role_client_servers.servers }}"
  when:
    - item.state == "absent"
- name: "[MikroTik] [NTP Client] Enable ntp client servers"
  register: enable_ntp_enable_client_servers
  routeros_command:
    commands:
    - /system ntp client set enabled={{ input_role_client_servers.enabled }}
      {% if input_role_client_servers.mode is defined %} mode={{ input_role_client_servers.mode }}{% endif %}
      {% if input_role_client_servers.vrf is defined %} vrf={{ input_role_client_servers.vrf }}{% endif %}
- name: "[MikroTik] [NTP Client] Enable ntp client servers"
  register: enable_ntp_enable_client_servers
  debug:
    msg:
    - /system ntp client servers set enabled={{ input_role_client_servers.enabled }}
      {% if input_role_client_servers.mode is defined %} mode={{ input_role_client_servers.mode }}{% endif %}
      {% if input_role_client_servers.vrf is defined %} vrf={{ input_role_client_servers.vrf }}{% endif %}
- name: "[MikroTik] [Timezone] Set time-zone"
  register: enable_timezone_client_servers
  routeros_command:
    commands:
    - /system ntp client servers set enabled={{ input_role_client_servers.time_zone_name }}