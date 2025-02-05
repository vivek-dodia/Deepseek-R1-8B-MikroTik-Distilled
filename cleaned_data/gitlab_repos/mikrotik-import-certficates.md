# Repository Information
Name: mikrotik-import-certficates

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
	url = https://gitlab.com/mikrotik-ansible/mikrotik-import-certficates.git
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
mikrotik_tls_certificates:
  delete_all_certificates: no
  delete_configs_on_target_router: yes
  certificates: []
  crls: []
================================================

File: certificates.md
================================================
# Certificate import example
The role allows control over imported certificates and private keys
if delete_all_certificates us true - deletes all CRLs, public and private keys.
Example usage:
```
mikrotik_tls_certificates:
  delete_all_certificates: <yes|no> # if true - deletes ALL certificates and CRLs
  delete_configs_on_target_router: <yes|no> # if true - deletes keys and configs from target router
  certificates:
    - name: certificate 1 # Required. Name for a certificate
      public_key_source_path: path_1 # Required. path on control PC to copy from
      private_key_source_path: path_2 # Default - empty. path on control PC to copy from. If not set - not import any private key.
      private_key_password: password # Password to decrypt private key
      trusted: <yes|no> # Required. Set trusted or not
  crls:
    - url: "http://example.com/crl.pem" # path to download CRL from
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
# Mikrotik certificates configuration.
A Role allows configuraiton (import and deleting) of Mikrotik RouterOS TLS certificates using Ansible.
Examples of usage with comments are in docs/
Big thanks to Martin Dulin for his role https://github.com/mikrotik-ansible/mikrotik-firewall.
His role gave me an idea how solve RouterOS configuration tasks.
================================================

File: main.yml
================================================
---
  - name: Generate certificates template certificates-{{inventory_hostname}}.rsc to import certificates
    template: src=certificates.rsc.j2 dest={{role_path}}/files/tmp/certificates-{{inventory_hostname}}.rsc
    delegate_to: localhost
    tags: ["role::mikrotik::certificates", "role::mikrotik::certificates::upload_only"]
  - name: Send public keys to router
    command: scp -P {{ansible_port}} "{{ item['public_key_source_path'] }}" {{ansible_user}}@{{ansible_host}}:"/Ansible_pki_{{ item['name'] }}.crt"
    delegate_to: localhost
    loop: "{{ mikrotik_tls_certificates['certificates'] }}"
    tags: ["role::mikrotik::certificates", "role::mikrotik::certificates::upload_only"]
  - name: Send private keys to router
    command: scp -P {{ansible_port}} "{{ item['private_key_source_path'] }}" {{ansible_user}}@{{ansible_host}}:"/Ansible_pki_{{ item['name'] }}.pem"
    delegate_to: localhost
    when: "'private_key_source_path' in item.keys()"
    loop: "{{ mikrotik_tls_certificates['certificates'] }}"
    tags: ["role::mikrotik::certificates", "role::mikrotik::certificates::upload_only"]
  - name: Send certificates-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/certificates-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/certificates-{{inventory_hostname}}.rsc
    delegate_to: localhost
    tags: ["role::mikrotik::certificates", "role::mikrotik::certificates::upload_only"]
  - name: Delete temporary certificates-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/certificates-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost
    tags: ["role::mikrotik::certificates", "role::mikrotik::certificates::upload_only"]
  - name: Run certificates-{{inventory_hostname}}.rsc on router
    routeros_command:
      commands:  "/import certificates-{{inventory_hostname}}.rsc"
    register: mikrotik_certificates_out
    failed_when: mikrotik_certificates_out['stdout_lines'][0][-1] is not search('Script file loaded and executed successfully')
    tags: ["role::mikrotik::certificates"]
  - name: Remove certificates-{{inventory_hostname}}.rsc from router
    routeros_command:
      commands:  "/file remove certificates-{{inventory_hostname}}.rsc"
    register: mikrotik_certificates_out_delete_out
    failed_when: mikrotik_certificates_out_delete_out['stdout_lines'][0][-1] is search('no such item')
    when: mikrotik_tls_certificates.delete_configs_on_target_router
    tags: ["role::mikrotik::certificates"]
  - name: Remove public and private key files from router
    routeros_command:
      commands:  /file remove [/file find name~"Ansible_pki_{{ item['name'] }}."]
    register: mikrotik_public_keys_out_delete_out
    loop: "{{ mikrotik_tls_certificates['certificates'] }}"
    failed_when: mikrotik_public_keys_out_delete_out['stdout'][0] is search('no such item')
    when: mikrotik_tls_certificates.delete_configs_on_target_router
    tags: ["role::mikrotik::certificates"]
================================================