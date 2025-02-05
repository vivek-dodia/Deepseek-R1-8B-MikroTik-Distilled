# Repository Information
Name: ansible-mikrotik-l2tp-client

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
	url = https://gitlab.com/mikrotik-ansible/ansible-mikrotik-l2tp-client.git
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
mikrotik_l2tp_client_delete_old_profiles: no
mikrotik_l2tp_client_delete_old_connections: no
mikrotik_l2tp_client:
  delete_configs_on_target_router: yes
================================================

File: l2tp-example.md
================================================
---
Example configuration.
Use it as a reference.
Be careful: the role only sets defined variables.
If you set a variable, apply configuration and then
you undefine the variable - no any config changes will be done.
The value will remain the same as the last defined variable.
```
mikrotik_l2tp_client_delete_old_profiles: <yes|no> # if 'yes' - delete ALL existing PPP profiles. Deletes even profiles which are not used by L2TP but used by other PPP connections.
mikrotik_l2tp_client_delete_old_connections: <yes|no> # if 'yes' - delete ALL existing L2TP client connections
mikrotik_l2tp_client:
  profiles:
    - name: profile 1 # Required. name of new profile.
      address_list: list1 # name of an address list to add address of interface to
      comment: comment 1 # Required. comment to add to a profile
      idle_timeout: 3600 # Specifies the amount of time after which the link will be terminated if there are no activity present. Timeout is not set by default
      interface_list: int_list 1 #name of an interface list to add the client to
      on_up: script1 # name of a script to start on interface up
      remote_address: 10.8.0.1 # Assigns an individual address to the PPP. Tunnel address or name of the pool from which address is assigned to remote ppp interface.
      use_encryption: <yes | no | default | require> # Set encryption. Must be quoted
      wins_server: 10.8.0.1 # Windows Internet Naming Service server
      bridge: bridge1 # Name of the bridge interface to which ppp interface will be added as slave port. Both tunnel end point (server and client) must be in bridge in order to make this work.
      #bridge_port_priority:  # No documentation on wiki.mikrotik.com.
      copy_from: 0 # Item number to copy settings from. Not recommended for usage because of unpredictability of numbering
      incoming_filter: chain_inc_1 #Firewall chain name for incoming packets
      local_address: 10.8.0.10 # Tunnel address or name of the pool from which address is assigned to ppp interface locally.
      only_one: <yes|no> # Allow only one connection at a time
      #queue_type: #  No documentation on wiki.mikrotik.com.
      session_timeout: 1d # The maximum time the connection can stay up
      use_mpls: <yes | no | default | require> # Must be quoted. Specifies whether to allow MPLS over L2TP
      #bridge_horizon: #  No documentation on wiki.mikrotik.com.
      change_tcp_mss: <yes|no> # Change or not TCP protocol's Maximum Segment Size
      dns_server: 10.0.0.11 # IP address of the DNS server that is supplied to ppp clients
      #insert_queue_before: #  No documentation on wiki.mikrotik.com.
      on_down: script_down_1 # script to run on interface down
      outgoing_filter: chain_out_1 # Firewall chain name for outgoing packets
      # Rate limitation in form of rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold]
      # [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]
      # from the point of view of the router (so "rx" is client upload, and "tx" is client download).
      # All rates are measured in bits per second, unless followed by optional 'k' suffix (kilobits per second)
      # or 'M' suffix (megabits per second).
      # If tx-rate is not specified, rx-rate serves as tx-rate too.
      # The same applies for tx-burst-rate, tx-burst-threshold and tx-burst-time.
      # If both rx-burst-threshold and tx-burst-threshold are not specified
      # (but burst-rate is specified), rx-rate and tx-rate are used as burst thresholds.
      # If both rx-burst-time and tx-burst-time are not specified, 1s is used as default.
      # Priority takes values 1..8, where 1 implies the highest priority, but 8 - the lowest.
      # If rx-rate-min and tx-rate-min are not specified rx-rate and tx-rate values are used.
      # The rx-rate-min and tx-rate-min values can not exceed rx-rate and tx-rate values.
      rate_limit: 1000M
      use_compression: <yes|no> # Specifies whether to use data compression or not.
      #use_upnp: #  No documentation on wiki.mikrotik.com.
  connections:
    - name: l2tp-out-1 # required argument
      user: user_1 # Required. L2TP auth user
      connect_to: 10.7.0.1 # Required. The IP address of the L2TP server to connect to
      comment: my connection # Required. Comment to add to connection
      add_default_route: <yes|no> # Whether to use server which this client is connected to as its default gateway
      #allow_fast_path: <yes|no> #  No documentation on wiki.mikrotik.com. Could be the setting to enable FastPath processing
      copy_from:  0 # Item number to copy settings from. Not recommended for usage because of unpredictability of numbering
      dial_on_demand: <yes|no> # Enable/disable dial on demand
      use_ipsec: <yes|no> # Enables IPsec encryption with default settings in PSK mode.
      ipsec_secret: password # Secret to use with "use_ipsec" in PSK mode. Be careful to use only RouterOS supported symbols.
      max_mru: 1500 # Maximum Receive Unit. Max packet size that PPP interface will be able to receive without packet fragmentation.
      mrru: <disabled | integer> # Maximum packet size that can be received on the link. If a packet is bigger than tunnel MTU, it will be split into multiple packets, allowing full size IP or Ethernet packets to be sent over the tunnel.
      password: password # L2TP auth password. Be careful to use only RouterOS supported symbols.
      allow: pap,chap,mschap1,mschap2 # must be quoted. The authentication method to allow for the client
      default_route_distance: 10 # Distance to set to created default route if "add_default_route" is enabled
      disabled: <yes|no> # Required. if the connection is disabled
      keepalive_timeout: 10 # PPP keepalive timeout in seconds.
      max_mtu: 1500 # Maximum Transmission Unit. Max packet size that PPP interface will be able to send without packet fragmentation.
      profile: "profile 1" # name of PPP profile to use for the connection.
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
  description: Mikrotik L2TP client setup
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
    - l2tp
dependencies: []
  # List your role dependencies here, one per line. Be sure to remove the '[]' above,
  # if you add dependencies to this list.
================================================

File: README.md
================================================
# Mikrotik L2TP client configurator.
A Role allows configuraiton of Mikrotik RouterOS L2TP client interface with Ansible.
The role creates PPP profiles and L2TP client interfaces.
Examples of usage with comments are in docs/
Big thanks to Martin Dulin for his role https://github.com/mikrotik-ansible/mikrotik-firewall.
His role gave me an idea how solve RouterOS configuration tasks.
================================================

File: main.yml
================================================
---
  - name: Generate l2tp-client-{{inventory_hostname}}.rsc to check and add user
    template: src=l2tp-client.rsc.j2 dest={{role_path}}/files/tmp/l2tp-client-{{inventory_hostname}}.rsc
    delegate_to: localhost
    tags: ["role::mikrotik::L2TP_client", "role::mikrotik::L2TP_client::generate_script_local"]
  - name: Send l2tp-client-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/l2tp-client-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/l2tp-client-{{inventory_hostname}}.rsc
    delegate_to: localhost
    tags: ["role::mikrotik::L2TP_client"]
  - name: Delete temporary l2tp-client-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/l2tp-client-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost
    tags: ["role::mikrotik::L2TP_client"]
  - name: Run l2tp-client-{{inventory_hostname}}.rsc on router
    routeros_command:
      commands:  "/import l2tp-client-{{inventory_hostname}}.rsc"
    register: mikrotik_l2tp_client_out
    failed_when: mikrotik_l2tp_client_out['stdout_lines'][0][-1] is not search('Script file loaded and executed successfully')
    tags: ["role::mikrotik::L2TP_client"]
  - name: Remove l2tp-client-{{inventory_hostname}}.rsc from router
    routeros_command:
      commands:  "/file remove l2tp-client-{{inventory_hostname}}.rsc"
    register: mikrotik_l2tp_client_out_delete_out
    failed_when: mikrotik_l2tp_client_out_delete_out['stdout_lines'][0][-1] is search('no such item')
    when: mikrotik_l2tp_client.delete_configs_on_target_router
    tags: ["role::mikrotik::L2TP_client"]
================================================