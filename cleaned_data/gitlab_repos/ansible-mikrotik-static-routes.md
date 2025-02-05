# Repository Information
Name: ansible-mikrotik-static-routes

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
	url = https://gitlab.com/mikrotik-ansible/ansible-mikrotik-static-routes.git
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
mikrotik_static_routes: []
mikrotik_static_routes_remove_old_routes: false
================================================

File: routes.md
================================================
---
Configuration sample.
Values must be RouterOS valid parameters for routes (/ip route).
Be careful: the role only sets defined variables.
If you set a variable, apply configuration and then
you undefine the variable - no any config changes will be done.
The value will remain the same as the last defined variable.
```
# if true _ deletes All STATIC routes from routing table
mikrotik_static_routes_remove_old_routes: false
#
# dst_address, gateway and comment are REQUIRED attributes
#
mikrotik_static_routes:
  - dst_address: "10.8.1.0/24"
    gateway:
      - "10.8.0.1"
    comment: "comment 1"
    bgp_as_path:
    bgp_atomic_aggregate:
    bgp_communities:
    bgp_local_pref:
    bgp_med:
    bgp_origin:
    bgp_prepend:
    check_gateway:
    # copy_from:  _ might be done in future
    disabled:
    distance:
    pref_src:
    route_tag:
    routing_mark:
    scope:
    target_scope:
    type:
  - dst_address: "10.8.2.0/24"
    gateway:
      - "10.8.0.1"
    comment: "comment 1"
    bgp_as_path:
    bgp_atomic_aggregate:
    bgp_communities:
    bgp_local_pref:
    bgp_med:
    bgp_origin:
    bgp_prepend:
    check_gateway:
    # copy_from:  _ might be done in future
    disabled:
    distance:
    pref_src:
    route_tag:
    routing_mark:
    scope:
    target_scope:
    type:
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
  description: Mikrotik static routing setup
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
    - routing
dependencies: []
  # List your role dependencies here, one per line. Be sure to remove the '[]' above,
  # if you add dependencies to this list.
================================================

File: README.md
================================================
# Mikrotik RouterOS users and SSH public keys management
Allows adding and deleting static routes for Mikrotik RouterOS
Big thanks to Martin Dulin for his role https://github.com/mikrotik-ansible/mikrotik-firewall.
His role gave me an idea how solve RouterOS configuration tasks.
================================================

File: main.yml
================================================
---
  - name: Generate static-routes_list-{{inventory_hostname}}.rsc to check and add user
    template: src=static-routes.rsc.j2 dest={{role_path}}/files/tmp/static-routes_list-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Send static-routes_list-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/static-routes_list-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/static-routes_list-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Delete temporary static-routes_list-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/static-routes_list-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost
  - name: Run static-routes_list-{{inventory_hostname}}.rsc on router
    routeros_command:
      commands:  "/import static-routes_list-{{inventory_hostname}}.rsc"
    tags: mikrotik_firewall_services
    register: static_routes_list_out
    failed_when: static_routes_list_out['stdout_lines'][0][-1] is not search('Script file loaded and executed successfully')
  - name: Remove static-routes_list-{{inventory_hostname}}.rsc from router
    routeros_command:
      commands:  "/file remove static-routes_list-{{inventory_hostname}}.rsc"
    register: static_routes_file_delete_out
    failed_when: static_routes_file_delete_out['stdout_lines'][0][-1] is search('no such item')
================================================