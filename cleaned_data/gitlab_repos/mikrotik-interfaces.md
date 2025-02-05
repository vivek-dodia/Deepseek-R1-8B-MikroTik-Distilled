# Repository Information
Name: mikrotik-interfaces

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
	url = https://gitlab.com/mikrotik-ansible/mikrotik-interfaces.git
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
mikrotik_interfaces:
  reset_ethernet_interfaces: false
  delete_all_vlan_interfaces: false
  delete_all_bridge_interfaces: false
  ethernets: []
  vlans: []
  bridges: []
================================================

File: example.md
================================================
# Example
Use example below to configure tour device
```
mikrotik_interfaces:
  reset_ethernet_interfaces: false
  delete_all_vlan_interfaces: false
  delete_interfaces_on_target_router: true
  ethernets:
    - comment: (string) # Required. Descriptive name of an item
      default-name: (string) # Required. Default (hardware) name of an interface - used for matching.
      disabled: (yes|no) # Required. if true - interface is disabled.
      name: (string) # Default: None. Name of an interface.
      advertise: (string) # Default: "10M-half,10M-full,100M-half,100M-full,1000M-full". List of ethernet modes to advertise, separated by comma.
      arp: (disabled | enabled | proxy-arp | reply-only) # Default: enabled. Address Resolution Protocol mode: disabled - the interface will not use ARP; enabled - the interface will use ARP; proxy-arp - the interface will use the ARP proxy feature; reply-only - the interface will only reply to requests originated from matching IP address/MAC address combinations which are entered as static entries in the ARP table. No dynamic entries will be automatically stored in the ARP table. Therefore for communications to be successful, a valid static entry must already exist.
      arp-timeout: (auto|time) # Default: auto. ARP timeout.
      auto-negotiation: (yes | no) # Default: yes. When enabled, the interface "advertises" its maximum capabilities to achieve the best connection possible. Note1: Auto-negotiation should not be disabled on one end only, otherwise Ethernet Interfaces may not work properly. Note2: Gigabit link cannot work with auto-negotiation disabled.
      tx-flow-control: (on | off | auto) # Default: off. When set to on, port will send pause frames when specific buffer usage thresholds is met. auto is the same as on except when auto-negotiation=yes flow control status is resolved by taking into account what other end advertises. Feature is supported on AR724x, AR9xxx, QCA9xxx CPU ports, all CCR ports and all Atheros switch chip ports.
      rx-flow-control: (on | off | auto) # Default: off. When set to on, port will process received pause frames and suspend transmission if required. auto is the same as on except when auto-negotiation=yes flow control status is resolved by taking into account what other end advertises. Feature is supported on AR724x, AR9xxx, QCA9xxx CPU ports, all CCR ports and all Atheros switch chip ports.
      full-duplex: (yes | no) # Default: yes. Defines whether the transmission of data appears in two directions simultaneously
      # Not implemented. mac-address: (MAC) # Default: None. Media Access Control number of an interface.
      mdix-enable: (yes | no) # Default: yes. Whether the MDI/X auto cross over cable correction feature is enabled for the port: (Hardware specific, e.g. ether1 on RB500 can be set to yes/no. Fixed to 'yes' on other hardware.)
      mtu: (integer [0..65536]) # Default: 1500. Layer3 Maximum transmission unit
      # Not implemented. orig-mac-address: (MAC) # Default: None. Not documented.
      speed: (10Mbps | 10Gbps | 100Mbps | 1Gbps) # Default: None. Sets interface data transmission speed which takes effect only when auto-negotiation is disabled.
      loop-protect: (yes|no|default) # Default: default. Sets loop protection status.
      loop-protect-disable-time: (time) # Default: 5m. Sets time for which the interface will be disabled on loop detection
      loop-protect-send-interval: (time) # Default: 5s. Sets interval between loop checks.
  vlans:
    - name: (string) # Required. Interface name
      comment: (string) # Required. Descriptive comment of interface
      disabled: (yes|no) # Required. if true - interface is disabled.
      interface: (name) # Required. Name of physical interface on top of which VLAN will work
      vlan-id: (integer: 1..4095) # Default: 1. Virtual LAN identifier or tag that is used to distinguish VLANs. Must be equal for all computers that belong to the same VLAN.
      arp: (disabled | enabled | proxy-arp | reply-only) # Default: enabled. Address Resolution Protocol mode
      arp-timeout: (auto|time) # Default: auto. ARP protocol timeout.
      mtu: (integer) # Default: 1500. Layer3 Maximum transmission unit
      use-service-tag: (yes | no) # Default: no. 802.1ad compatible Service Tag
  bridges:
    - name: (string) # Required. Unique name of a bridge interface
      comment: (string) # Required. Descriptive name of the bridge interface
      member-ports:
        - interface: (string) # Required. Name of physical or logical interface to add to the bridge
          comment: (string) # Required. Description of the member interface
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
# Mikrotik Ethernet interfaces configuration.
A Role allows configuraiton of Mikrotik RouterOS Ethernet interfaces and vlans.
Examples of usage with comments are in docs/
Big thanks to Martin Dulin for his role https://github.com/mikrotik-ansible/mikrotik-firewall.
His role gave me an idea how solve RouterOS configuration tasks.
================================================

File: main.yml
================================================
---
  - name: Generate interfaces template interfaces-{{inventory_hostname}}.rsc to import interfaces
    template: src=interfaces_full.rsc.j2 dest={{role_path}}/files/tmp/interfaces-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Send interfaces-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/interfaces-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/interfaces-{{inventory_hostname}}.rsc
    delegate_to: localhost
  - name: Delete temporary interfaces-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/interfaces-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost
  - name: Run interfaces-{{inventory_hostname}}.rsc on router
    routeros_command:
      commands:  "/import interfaces-{{inventory_hostname}}.rsc"
    tags: mikrotik_interfaces
    register: mikrotik_interfaces_out
    failed_when: mikrotik_interfaces_out['stdout_lines'][0][-1] is not search('Script file loaded and executed successfully')
  - name: Remove interfaces-{{inventory_hostname}}.rsc from router
    routeros_command:
      commands:  "/file remove interfaces-{{inventory_hostname}}.rsc"
    register: mikrotik_interfaces_out_delete_out
    failed_when: mikrotik_interfaces_out_delete_out['stdout_lines'][0][-1] is search('no such item')
================================================

File: ToDo.txt
================================================
Add all fields for Mikrotik Bridge interfaces