# Repository Information
Name: mikrotik-routeros-backup

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
	url = https://gitlab.com/automate-check-point/mikrotik-routeros-backup.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: backup.sh
================================================
#!/bin/bash
source ../Secrets/mtik.creds
echo "***Backing up Mikrotik devices***"
ansible-playbook mtik.backup.yml
================================================

File: mtik.backup.yml
================================================
---
- name: Playbook to backup configs on Vyos VMs based on Ansible inventory
  connection: network_cli
  hosts: device_roles_mikrotik-switch
  gather_facts: False
  vars:
    backup_dir: "../Backups/MTik/"
    ansible_user: "{{ lookup('env','ansible_u') }}"
    ansible_password: "{{ lookup('env','ansible_p') }}"
  tasks:
   - name: Export
     ansible.builtin.shell: >-
                sshpass -p '{{ ansible_password }}' ssh -o StrictHostKeyChecking=no  {{ ansible_user }}@{{ ansible_host }} /export 
     register: export
     delegate_to: localhost
   - name: Backup
     ansible.builtin.copy:
       content: "{{ export.stdout }}"
       dest: "{{ backup_dir }}/{{ inventory_hostname }}_config.{{ lookup('pipe', 'date +%d-%m-%Y@%H:%M') }}"
     when: export is defined
     delegate_to: localhost