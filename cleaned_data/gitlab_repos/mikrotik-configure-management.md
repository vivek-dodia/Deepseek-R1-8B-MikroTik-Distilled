# Repository Information
Name: mikrotik-configure-management

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
	url = https://gitlab.com/mikrotik-ansible/mikrotik-configure-management.git
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
mikrotik_management:
  #hostname: null
  telnet:
    available_from_addresses: []
    disabled: yes
    port: 23
  ftp:
    available_from_addresses: []
    disabled: yes
    port: 21
  www:
    available_from_addresses: []
    disabled: yes
    port: 80
  www-ssl:
    available_from_addresses: []
    disabled: yes
    port: 443
    certificate: ""
  ssh:
    available_from_addresses: []
    disabled: no
    port: 22
  api:
    available_from_addresses: []
    disabled: yes
    port: 8728
  winbox:
    available_from_addresses: []
    disabled: yes
    port: 8291
  api-ssl:
    available_from_addresses: []
    disabled: yes
    port: 8729
    certificate: ""
  snmp:
    credentials_dir: 'credentials/'
    enabled: no
    contact: ""
    location: ""
    engine-id: ""
    trap-target: ""
    trap-community: ""
    trap-version: 1
    trap-generators: temp-exception
    communities: []
================================================

File: example.md
================================================
# Example of management configuration
```
mikrotik_management:
  hostname: host1 # hostname to set for the router. Default is inventory_hostname
  telnet:
    available_from_addresses: [] # Default: []. Addresses to allow connection from.
    disabled: yes # Default: yes.
    port: 23 # Default 23. TCP port for the service.
  ftp:
    available_from_addresses: []
    disabled: yes # Default: yes.
    port: 21
  www:
    available_from_addresses: []
    disabled: yes # Default: yes.
    port: 80
  www-ssl:
    available_from_addresses: []
    disabled: yes # Default: yes.
    port: 443
    certificate: "" # TLS certificate from /certificate to use for the service
  ssh:
    available_from_addresses: []
    disabled: no # Default: no.
    port: 22
  api:
    available_from_addresses: []
    disabled: yes # Default: yes.
    port: 8728
  winbox:
    available_from_addresses: []
    disabled: yes # Default: yes.
    port: 8291
  api-ssl:
    available_from_addresses: []
    disabled: yes # Default: yes.
    port: 8729
    certificate: ""
  snmp: # Global SNMP configuration
    credentials_dir: (string) # Place to save new auto generated default snmp community name
    enabled: no # Default: no. Status of SNMP
    contact: admin@example.com # Default: none. SNMP contact info
    location: office 1 # Default: none. SNMP location
    engine-id: engine 1 # Default: none.
    trap-target:
      - 10.8.0.1 # Default: none. List of trap targets
    trap-community: public # Default: random string which is equal to "default" SNMP community name.  Must exists in RouterOS config or error.
    trap-version: 1  # Default: 1.
    trap-generators: temp-exception  # Default: temp-exception.
    communities: # SNMP communities
      - name: public  # Required
        addresses: # list of addresses to allow connection from
          - 10.8.0.1
        write-access: no # Default: no. Allow/Disallow write access
        read-access: no # Default: no. Allow/Disallow read access
        authentication-protocol: MD5  # Default: MD5.
        encryption-protocol: "DES"  # Default: DES.
        encryption-password: "" # Default: none.
        authentication-password: "" # Default: none.
        security: none # Default: none.
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
# Mikrotik management configuration.
A Role allows configuraiton of Mikrotik RouterOS management (/ip services, /snmp, /system identity) using Ansible.
Examples of usage with comments are in docs/
Big thanks to Martin Dulin for his role https://github.com/mikrotik-ansible/mikrotik-firewall.
His role gave me an idea how solve RouterOS configuration tasks.
================================================

File: main.yml
================================================
---
  - name: Generate management template management-{{inventory_hostname}}.rsc to import management
    template: src=management_full.rsc.j2 dest={{role_path}}/files/tmp/management-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Send management-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/management-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/management-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Delete temporary management-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/management-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost
  - name: Run management-{{inventory_hostname}}.rsc on router
    routeros_command:
      commands:  "/import management-{{inventory_hostname}}.rsc"
    tags: mikrotik_management
    register: mikrotik_management_out
    failed_when: mikrotik_management_out['stdout_lines'][0][-1] is not search('Script file loaded and executed successfully')
  - name: Remove management-{{inventory_hostname}}.rsc from router
    routeros_command:
      commands:  "/file remove management-{{inventory_hostname}}.rsc"
    register: mikrotik_management_out_delete_out
    failed_when: mikrotik_management_out_delete_out['stdout_lines'][0][-1] is search('no such item')
    when: mikrotik_management.delete_management_script_on_target_router | default(true)
================================================