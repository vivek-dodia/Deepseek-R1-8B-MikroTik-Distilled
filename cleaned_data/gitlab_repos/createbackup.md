# Repository Information
Name: createbackup

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
	url = https://gitlab.com/rachuna-net.pl/tools/ansibleroles/mikrotik/createbackup.git
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
- PUtworzenie roli do wykonywania backupu
================================================

File: main.yml
================================================
input_role_localhost_os_distribution:  ubuntu"
input_role_install_tools:              true
input_role_ansible_host:               "{{ ansible_host }}"
input_role_destination_path:           "/tmp/test"
input_role_ansible_user:               "{{ ansible_user }}"
input_role_ansible_password:           "{{ ansible_ssh_pass }}"
================================================

File: main.yml
================================================
galaxy_info:
  author: Maciej Rachuna
  description: Create configuration mikrotik
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
# createbackup
Ansible Role - Mikrotik - Create backup
![Overwiew](docs/createBackup.png)
### Wymagania
```bash
apt-get install sshpass python3-pip
pip install paramiko
```
# Zmienne
default:
```yaml
input_role_localhost_os_distribution: "ubuntu"
input_role_ansible_host:             "{{ ansible_host }}"
input_role_destination_path:          "/tmp/test"
input_role_ansible_user:              "{{ ansible_user }}"
input_role_ansible_password:          "{{ ansible_ssh_pass }}"
```
Zmienne wewnętrzne:
```yaml
var_role_backup_filename:      "{{ input_role_ansible_host }}.{{ lookup('pipe','date +%Y%m%d') }}.backup"
var_role_backup_filename_rsc:  "{{ input_role_ansible_host }}.{{ lookup('pipe','date +%Y%m%d') }}.rsc"
```
# Przykładowy playbook
```yaml
- hosts: all
  gather_facts: yes
  tasks:
  - include_role:
      name: createbackup
    vars:
      input_role_install_tools:              true
      input_role_localhost_os_distribution:  "{{ ansible_distribution }}"
      input_role_ansible_host:               "{{ ansible_host }}"
      input_role_destination_path:           "/tmp/test"
      input_role_ansible_user:               "{{ ansible_user }}"
      input_role_ansible_password:           "{{ ansible_ssh_pass }}"
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

File: create_backup_on_mikrotik.yml
================================================
- name: "[MikroTik] Create backup of Mikrotik to local storage"
  routeros_command:
    commands:
      - /system backup save name="{{ var_role_backup_filename }}"
      - /export file="{{ var_role_backup_filename_rsc }}"
  register: create_backup_stdout
================================================

File: create_infrastructure_directories_on_localhost.yml
================================================
- name: "[localhost] Create backup {{ input_role_destination_path }}/backup on localhost"
  become: true
  delegate_to: localhost
  file:
    path: "{{ input_role_destination_path }}/backup"
    state: directory
    owner: "{{ lookup('env', 'USER') }}"
    group: "{{ lookup('env', 'USER') }}"
  register: backup_directory_status
- name: "[localhost] Create backup {{ input_role_destination_path }}/rsc on localhost"
  become: true
  delegate_to: localhost
  file:
    path: "{{ input_role_destination_path }}/rsc"
    state: directory
    owner: "{{ lookup('env', 'USER') }}"
    group: "{{ lookup('env', 'USER') }}"
  register: rsc_directory_status
================================================

File: download_backup.yml
================================================
- name: "[localhost] Download backup"
  become: true
  action: command sshpass -p "{{ input_role_ansible_password }}" sftp {{ input_role_ansible_user }}@{{ input_role_ansible_host }}:{{ var_role_backup_filename }} {{ input_role_destination_path }}/backup
- name: "[localhost] Download configuration"
  become: true
  action: command sshpass -p "{{ input_role_ansible_password }}" sftp {{ input_role_ansible_user }}@{{ input_role_ansible_host }}:{{ var_role_backup_filename_rsc }} {{ input_role_destination_path }}/rsc
================================================

File: install_tools.yml
================================================
- name: "[Ubuntu] Install tools"
  delegate_to: localhost
  apt:
    pkg:
    - sshpass
  when: input_role_localhost_os_distribution == "Ubuntu"
================================================

File: main.yml
================================================
- become: true
  delegate_to: localhost
  include: install_tools.yml
  when: input_role_install_tools is true
- include: create_infrastructure_directories_on_localhost.yml
- include: create_backup_on_mikrotik.yml
- include: download_backup.yml
================================================

File: main.yml
================================================
var_role_backup_filename:      "{{ input_role_ansible_host }}.{{ lookup('pipe','date +%Y%m%d') }}.backup"
var_role_backup_filename_rsc:  "{{ input_role_ansible_host }}.{{ lookup('pipe','date +%Y%m%d') }}.rsc"