# Repository Information
Name: ansible-mikrotik-users

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
	url = https://gitlab.com/mikrotik-ansible/ansible-mikrotik-users.git
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
mikrotik_users: []
================================================

File: users.md
================================================
---
Create users as in an example below.
Be careful: the role only sets defined variables.
If you set a variable, apply configuration and then
you undefine the variable - no any config changes will be done.
The value will remain the same as the last defined variable.
```
mikrotik_users:
  credentials_dir: 'credentials/'
  user_list:
    - name: u1 # login
      group: full # routeros group
      comment: u1 user # comment
      password: Pa$$word! # set password. Better use ansible-vault
      disabled: false # is user active
    - name: u2
      group: read
      comment: u2 user
      password: Pa$$word!
      address: 192.168.57.0/24 # allowed to login address list
      disabled: false
    - name: u3
      group: full
      comment: u3 user
      disabled: false
      # if password is not set it will be generated and put to {{credentials_dir}} + '/' + {{inventory_hostname}} + '__' + {{user.name}} + '__password.txt
      # the credentials_dir must exist or task fails
    - name: admin
      group: full
      comment: Admin user
      disabled: false
      password: Pa$$word!
      # paths to ssh public kery files
      pubkeys:
        - "{{playbook_dir}}/host_vars/vault/files/ssh_keys/admin1.pub"
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

File: main.yml
================================================
galaxy_info:
  author: Dmitriy Ermakov <demonihin@gmail.com
  description: Mikrotik users and SSH keys setup
  license: MIT
  min_ansible_version: 2.7
  platforms:
    - name: RouterOS
      versions:
        - all
  categories:
    - networking
  galaxy_tags:
    - networking
    - mikrotik
    - routeros
    - users
    - ssh-keys
dependencies: []
  # List your role dependencies here, one per line. Be sure to remove the '[]' above,
  # if you add dependencies to this list.
================================================

File: README.md
================================================
---
# Mikrotik RouterOS user management with Ansible.
Look for examples in "docs" folder.
Big thanks to Martin Dulin for his role https://github.com/mikrotik-ansible/mikrotik-firewall.
His role gave me an idea how solve RouterOS configuration tasks.
================================================

File: main.yml
================================================
---
  - name: Generate users_list-{{inventory_hostname}}.rsc to check and add user
    template: src=users.rsc.j2 dest={{role_path}}/files/tmp/users_list-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Send users_list-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/users_list-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/users_list-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Send ssh public keys for users
    command: scp -P {{ansible_port}} {{ item.1 }} {{ansible_user}}@{{ansible_host}}:/{{item.0.name}}-{{ index }}-pubkey.pub
    delegate_to: localhost
    loop: "{{ mikrotik_users['user_list'] | subelements('pubkeys', skip_missing=True) }}"
    loop_control:
      index_var: index
  - name: Delete temporary users_list-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/users_list-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost
  - name: Run users_list-{{inventory_hostname}}.rsc on router
    routeros_command:
      commands:  "/import users_list-{{inventory_hostname}}.rsc"
    tags: mikrotik_firewall_services
    register: users_list_out
    failed_when: users_list_out['stdout_lines'][0][-1] is not search('Script file loaded and executed successfully')
  - name: Remove users_list-{{inventory_hostname}}.rsc from router
    routeros_command:
      commands:  "/file remove users_list-{{inventory_hostname}}.rsc"
    register: users_file_delete_out
    failed_when: users_file_delete_out['stdout_lines'][0][-1] is search('no such item')
================================================