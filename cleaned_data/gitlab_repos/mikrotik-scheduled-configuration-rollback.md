# Repository Information
Name: mikrotik-scheduled-configuration-rollback

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
	url = https://gitlab.com/mikrotik-ansible/mikrotik-scheduled-configuration-rollback.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: main.yml
================================================
mikrotik_scheduled_config_rollback:
  password_path: "credentials/"
  reload_in: 30m
  backup_download_path: "config_backups/"
================================================

File: example.md
================================================
## Configuration example:
```
mikrotik_scheduled_config_rollback:
  password_path: "credentials/" # Path to save files with passwords for backup files. Password files have timestamp suffix
  reload_in: 30m # Time to schedule reload in
  backup_download_path: "config_backups/" # Path to save downloaded backup files. The files have the same timestamp suffix as the password files related to them
```
## Create a task in the beginning of your site.yml to schedule reload on fail
```
- name: Schedule Reload
  gather_facts: yes # Required because I use ansible_date_time.iso8601_basic to create file names
  hosts: routeros
  tasks:
    - import_role:
        name: mikrotik-scheduled-configuration-rollback
  vars:
    mikrotik_rollback_backup_action: schedule # Flag to show that we schedule restore and make backup
```
## Create a task in the end of your site.yml to cancel reload
```
- name: Cancel Scheduled Reload
  gather_facts: yes # Required because I use ansible_date_time.iso8601_basic to create file names
  hosts: routeros
  tasks:
    - import_role:
        name: mikrotik-scheduled-configuration-rollback
  vars:
    mikrotik_rollback_backup_action: cancel # Flag to show that we are cancelling scheduled restore
```
================================================

File: LICENSE
================================================
BSD 3-Clause License
Copyright (c) 2019, Dmitriy Ermakov
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
================================================

File: README.md
================================================
# Mikrotik RouterOS Scheduled rollback-restore
Allows setting up planned reload and restore of previous configuration in case we made a configuration mistake.
================================================

File: main.yml
================================================
- name: Generate One-time configuration Backup password
  set_fact:
    mikrotik_temp_backup_password: "{{ lookup('password', mikrotik_scheduled_config_rollback['password_path'] + '/' + inventory_hostname + '__backup_password__' + ansible_date_time.iso8601_basic + '.txt  chars=ascii_letters,digits  length=63') }}"
    mikrotik_temp_backup_filename: "flash/mikrotik_rollback_backup_{{ ansible_date_time.iso8601_basic }}"
  when: mikrotik_rollback_backup_action == "schedule"
  tags: ["role::mikrotik::scheduled_restore"]
- name: Making Configuration Backup
  routeros_command:
    commands:
      - /system backup save encryption=aes-sha256 password={{ mikrotik_temp_backup_password }} name="{{ mikrotik_temp_backup_filename }}"
  register: mikrotik_make_backup_output
  failed_when: mikrotik_make_backup_output['stdout'] | join(';') is not search('Configuration backup saved')
  when: mikrotik_rollback_backup_action == "schedule"
  tags: ["role::mikrotik::scheduled_restore"]
- name: Download Configuration Backup
  command: scp -P {{ansible_port}} {{ansible_user}}@{{ansible_host}}:/{{ mikrotik_temp_backup_filename }}.backup {{ mikrotik_scheduled_config_rollback['backup_download_path'] }}/{{ inventory_hostname }}__{{ ansible_date_time.iso8601_basic }}.backup
  when: mikrotik_rollback_backup_action == "schedule"
  tags: ["role::mikrotik::scheduled_restore"]
- name: Setting Up Scheduled Configuration Rollback
  routeros_command:
    commands:
      - /system script remove scheduled_backup_restore_script
      - /system script add name="scheduled_backup_restore_script" source="/system backup load name={{ mikrotik_temp_backup_filename }} password={{ mikrotik_temp_backup_password }}"
      - /system scheduler remove mikrotik_scheduled_restore
      - /system scheduler add name="mikrotik_scheduled_restore" comment="Planned reboot and restore in case of configuration failure" disabled=no interval={{ mikrotik_scheduled_config_rollback['reload_in'] }} on-event="/system script run scheduled_backup_restore_script"
  register: mikrotik_rollback_backup_enabled_out
  failed_when: mikrotik_rollback_backup_enabled_out['stdout'] | join(';') is search('(error)|(invalid)')
  when: mikrotik_rollback_backup_action == "schedule"
  tags: ["role::mikrotik::scheduled_restore"]
- name: Cancel Scheduled Reboot-Restore
  routeros_command:
    commands:
      - /system scheduler remove mikrotik_scheduled_restore
      - /system script remove scheduled_backup_restore_script
      - /file remove {{ mikrotik_temp_backup_filename }}
  register: mikrotik_rollback_backup_cancel_out
  failed_when: mikrotik_rollback_backup_cancel_out['stdout'] | join(';') is search('(error)|(invalid)')
  when: mikrotik_rollback_backup_action == "cancel"
  tags: ["role::mikrotik::scheduled_restore"]