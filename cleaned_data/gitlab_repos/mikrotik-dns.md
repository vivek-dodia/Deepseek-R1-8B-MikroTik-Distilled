# Repository Information
Name: mikrotik-dns

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
	url = https://gitlab.com/mikrotik-ansible/mikrotik-dns.git
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
mikrotik_dns:
  delete_dns_script_on_target_router: true
  servers: []
  allow-remote-requests: no
  max-udp-packet-size: 4096
  query-server-timeout: 2s
  query-total-timeout: 10s
  max-concurrent-queries: 100
  max-concurrent-tcp-sessions: 20
  cache-size: "2048KiB"
  cache-max-ttl: "1w"
  static_records: []
================================================

File: example.yml
================================================
# DNS config example
```
mikrotik_dns:
  servers:
    - 8.8.8.8
    - 8.8.4.4
  allow-remote-requests: no # Default: no. Specifies whether to allow network requests
  max-udp-packet-size: 4096 # Default: 4096.  Maximum size of allowed UDP packet.
  query-server-timeout: 2s # Default: 2s.  Specifies how long to wait for query response from one server
  query-total-timeout: 10s # Default: 10s.  Specifies how long to wait for query response in total. Note that this setting must be configured taking into account query-server-timeout and number of used DNS server.
  max-concurrent-queries: 100 # Default: 100.  Specifies how much concurrent queries are allowed
  max-concurrent-tcp-sessions: 20 # Default: 20.  Specifies how much concurrent TCP sessions are allowed
  cache-size: "2048KiB" # Default: 2048Kib.  Specifies the size of DNS cache in KiB
  cache-max-ttl: "1w" # Default: 1w.  Maximum time-to-live for cache records. In other words, cache records will expire unconditionally after cache-max-ttl time. Shorter TTL received from DNS servers are respected.
  static_records: # List of static records to add to router
    - name: rec1 # Default: none. DNS name to be resolved to a given IP address. Either name or regexp could be set.
      regexp: reg1 # Default: none. Regex match to be resolved to a given IP address. Either name or regexp could be set.
      address: 10.8.0.1 # Required. IP address to resolve domain name with.
      comment: 'record 1' # Required. Description of a record
      disabled: no # Default: no. If the record is active
      ttl: 10h # Default: 1w. Time to live for the record
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
# Mikrotik DNS configuration.
A Role allows configuraiton of Mikrotik RouterOS DNS client and server using Ansible.
Examples of usage with comments are in docs/
Big thanks to Martin Dulin for his role https://github.com/mikrotik-ansible/mikrotik-firewall.
His role gave me an idea how solve RouterOS configuration tasks.
================================================

File: main.yml
================================================
---
  - name: Generate DNS template DNS-{{inventory_hostname}}.rsc to import DNS
    template: src=dns.rsc.j2 dest={{role_path}}/files/tmp/DNS-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Send DNS-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/DNS-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/DNS-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Delete temporary DNS-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/DNS-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost
  - name: Run DNS-{{inventory_hostname}}.rsc on router
    routeros_command:
      commands:  "/import DNS-{{inventory_hostname}}.rsc"
    tags: mikrotik_DNS
    register: mikrotik_DNS_out
    failed_when: mikrotik_DNS_out['stdout_lines'][0][-1] is not search('Script file loaded and executed successfully')
  - name: Remove DNS-{{inventory_hostname}}.rsc from router
    routeros_command:
      commands:  "/file remove DNS-{{inventory_hostname}}.rsc"
    register: mikrotik_DNS_out_delete_out
    failed_when: mikrotik_DNS_out_delete_out['stdout_lines'][0][-1] is search('no such item')
    when: mikrotik_dns.delete_dns_script_on_target_router | default(true)
================================================