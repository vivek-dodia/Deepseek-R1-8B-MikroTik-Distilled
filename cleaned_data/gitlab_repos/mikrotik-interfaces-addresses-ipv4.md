# Repository Information
Name: mikrotik-interfaces-addresses-ipv4

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
	url = https://gitlab.com/mikrotik-ansible/mikrotik-interfaces-addresses-ipv4.git
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
mikrotik_interfaces_addresses_ipv4:
  delete_all_addresses: false
  delete_all_dhcp_clients: false
  delete_addresses_on_target_router: true
  static_addresses: []
  dhcp_clients: []
================================================

File: example.md
================================================
mikrotik_interfaces_addresses_ipv4:
  delete_all_addresses: false # If true - deletes ALL static IPv4 addresses
  delete_all_dhcp_clients: false # If true - deletes ALL DHCP clients
  delete_addresses_on_target_router: true # If true - deletes import-script on the target router
  static_addresses:
    - comment: (string) # Required. Description of the address
      disabled: (yes|no) # Required. If the address is disabled
      address: (ipv4 address with prefix length) # Required. IPv4 address. Must be in form 10.8.0.1/24
      interface: (string) # Required. Name of interface to bind the address to.
  dhcp_clients:
    - interface: (string) # Required. name of an interface to bind DHCP client to
      comment: (string) # Required. Description of a client
      disabled: (yes|no) # Required. Whether to disable DHCP client.
      add-default-route: (yes | no | special-classless) # Default: yes. Whether to install default route in routing table received from dhcp server. By default RouterOS client complies to RFC and ignores option 3 if classless option 121 is received. To force client not to ignore option 3 set special-classless. This parameter is available in v6rc12+. yes - adds classless route if received, if not then add default route (old behavior). special-classless - adds both classless route if received and default route (MS style)
      dhcp-options: (string) # Default: None. DHCP options to send to DHCP server. Default list is: clientid, clientid_duid, hostname. List, separated by comma.
      script: (string) # Default: None. Script to run on receiveing IPv4 address from DHCP server.
      use-peer-ntp: (yes|no) # Default: yes. Whether to accept the NTP server settings from DHCP server.
      default-route-distance: (number) # Default: 1. Sets default route distance for a route received from DHCP server.
      use-peer-dns: (yes|no) # Default: yes. Whether to accept the DNS server settings from DHCP server.
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
# Mikrotik interfaces addresses configuration.
# Warning! The role deletes ALL undefined IPv4 addresses. You must be carefull to not loose control over your device!
A Role allows configuraiton of Mikrotik RouterOS Interfaces addresses IPv4 only.
Role allows setup of IPv4 static addresses and DHCP client.
Examples of usage with comments are in docs/
Big thanks to Martin Dulin for his role https://github.com/mikrotik-ansible/mikrotik-firewall.
His role gave me an idea how solve RouterOS configuration tasks.
================================================

File: main.yml
================================================
---
  - name: Generate addresses template addresses-{{inventory_hostname}}.rsc to import addresses
    template: src=addresses_full.rsc.j2 dest={{role_path}}/files/tmp/addresses-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Send addresses-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/addresses-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/addresses-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Delete temporary addresses-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/addresses-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost
  - name: Run addresses-{{inventory_hostname}}.rsc on router
    routeros_command:
      commands:  "/import addresses-{{inventory_hostname}}.rsc"
    tags: mikrotik_addresses
    register: mikrotik_addresses_out
    failed_when: mikrotik_addresses_out['stdout_lines'][0][-1] is not search('Script file loaded and executed successfully')
  - name: Remove addresses-{{inventory_hostname}}.rsc from router
    routeros_command:
      commands:  "/file remove addresses-{{inventory_hostname}}.rsc"
    register: mikrotik_addresses_out_delete_out
    failed_when: mikrotik_addresses_out_delete_out['stdout_lines'][0][-1] is search('no such item')
    when: mikrotik_interfaces_addresses_ipv4.delete_addresses_on_target_router
================================================