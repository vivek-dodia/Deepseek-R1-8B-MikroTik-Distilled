# Repository Information
Name: ansible-mikrotik

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
	url = https://gitlab.com/alxndro.plo/ansible-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2017 Wynand Booysen
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: mikrotik-backup-config.yml
================================================
---
# An Ansible Playbook to backup the Mikrotik device's configuration to both script and backup file
# Version 1 - 07/01/2017
#
# ansible.cfg
# [paramiko_connection]
# pty=False
#
- name: Mikrotik Backup Device Configuration
  hosts: mikrotik
  vars:
    ftpserver_var: speedtest.tele2.net
    ftpuser_var: anonymous
    ftppass_var: 
  connection: paramiko
  user: admin
  gather_facts: no
  tasks:
   - name: Performing backup of Mikrotik to local storage
     raw: /system backup save name {{inventory_hostname}}
   - name: Exporting current configuration to text
     raw: /export file={{inventory_hostname}}
   - name: FTP backup file
     raw: /tool fetch address={{ftpserver_var}} src-path={{inventory_hostname}}.backup user={{ftpuser_var}} mode=ftp dst-path=/upload/{{inventory_hostname}}.backup upload=yes
   - name: FTP export config
     raw: /tool fetch address={{ftpserver_var}} src-path={{inventory_hostname}}.rsc user={{ftpuser_var}} mode=ftp dst-path=/upload/{{inventory_hostname}}.rsc upload=yes
================================================

File: mikrotik-update-default-snmp.yml
================================================
---
# An Ansible Playbook to update (Lockdown) the default SNMP community 'public' which cannot be deleted
# Version 1 - 07/01/2017
#
# ansible.cfg
# [paramiko_connection]
# pty=False
#
- name: Mikrotik Update Default SNMP community
  hosts: mikrotik
  vars:
    address_var: x.x.x.x/32
    community_var: COMMUNITYNAME
  connection: paramiko
  user: admin
  gather_facts: no
  tasks:
   - name: Updating default SNMP community 'public'
     raw: /snmp community set [ find default=yes ] addresses={{address_var}} name={{community_var}}
================================================

File: mikrotik-update-ros-from-mikrotik-servers.yml
================================================
---
# An Ansible Playbook to mass update the ROS version on MikroTik routers
# Version 1 - 08/01/2017
#
- name: Mikrotik ROS Update
  hosts: mikrotik
# serial: 1 # executes one host at a time
  connection: paramiko
  user: admin
  gather_facts: no
  tasks:
   - name: Check if updates required
     raw: /system package update check-for-updates
     register: updatecheck
   - name: Run package updates and reboot if needed
     when: updatecheck.stdout.find('System is already up to date') == -1
     raw: /system package update download
     register: download
     until: download.stdout.find('please reboot router') > -1
     retries: 3
     delay: 60
   - name: Reboot the Router if the download is successful
     when: (updatecheck.stdout.find('System is already up to date') == -1) and (download.stdout.find('please reboot router') > -1)
     raw: /system reboot
     register: reboot
     async: 0
     poll: 0
================================================

File: README.md
================================================
# ansible-mikrotik
Ansible Playbooks for Mikrotik Devices