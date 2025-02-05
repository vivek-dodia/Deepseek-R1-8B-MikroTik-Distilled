# Repository Information
Name: ansible-mikrotik-exporter

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
	url = https://gitlab.com/chokoreetoz/ansible-mikrotik-exporter.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2019
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
================================================

File: main.yml
================================================
---
- name: Playbook Mikrotik-exporter
  remote_user: root
  hosts: all
  roles:
    - { role: install}
================================================

File: README.md
================================================
Ansible Installer for Mikrotik-exporter
=========
## Description
An installer for Prometheus Exporter for Mikrotik devices. Can be configured to collect metrics from a single device or multiple devices. Single device monitoring can be configured all on the command line. Multiple devices require a configuration file. A user will be required that has read-only access to the device configuration via the API.
## Reference
Please read the readme on https://github.com/nshttpd/mikrotik-exporter
Ansible role to install mikrotik-exporter
Requirements
------------
Install this exporter on the same prometheus server
Role Variables
--------------
```YAML
# process_exporter version to be installed
mikrotik_exporter_version: latest
# process_exporter config file path
mikrotik_exporter_config_file: /etc/mikrotik_exporter.yml
# process_exporter listen address
mikrotik_exporter_web_listen_address: 0.0.0.0:9436
```
## Config File
After install, you have to change the configuration file. Config file, placed in the ``` /etc/mikrotik_exporter.yml ```
Dependencies
------------
None
How to install Playbook
----------------
```
ansible-playbook -i hosts --limit=dockerbuild.daffakidz.com main.yml
```
# NOTE
After install you have to update the configuration ``` /etc/mikrotik_exporter.yml ```
================================================

File: main.yml
================================================
---
# Mikrotik_exporter version to be installed
mikrotik_exporter_version: latest
# mikrotik_exporter config file path
mikrotik_exporter_config_file: /etc/mikrotik_exporter.yml
# mikrotik_exporter listen address
mikrotik_exporter_web_listen_address: 0.0.0.0:9436
# mikrotik_exporter systemd file service
mikrotik_exporter_systemd_file: /etc/systemd/system/mikrotik_exporter.service
================================================

File: main.yml
================================================
---
- name: restart mikrotik_exporter
  systemd:
    name: mikrotik_exporter
    state: restarted
    daemon_reload: true
================================================

File: main.yml
================================================
---
dependencies: []
galaxy_info:
  role_name: mikrotik-exporter
  author: Hendry Yoga Priyanto
  description: Ansible role to install mikrotik-exporter
  company: Jagoanhosting
  license: MIT
  min_ansible_version: 2.7
  platforms:
    - name: EL
      versions:
        - 7
    - name: Debian
      versions:
        - stretch
  galaxy_tags: []
================================================

File: molecule.yml
================================================
---
dependency:
  name: galaxy
driver:
  name: docker
lint:
  name: yamllint
platforms:
  - name: instance
    image: "geerlingguy/docker-${MOLECULE_DISTRO:-centos7}-ansible:latest"
    command: ${MOLECULE_DOCKER_COMMAND:-""}
    volumes:
      - /sys/fs/cgroup:/sys/fs/cgroup:ro
    privileged: true
    pre_build_image: true
provisioner:
  name: ansible
  lint:
    name: ansible-lint
  playbooks:
    converge: ${MOLECULE_PLAYBOOK:-playbook.yml}
scenario:
  name: default
verifier:
  name: testinfra
  lint:
    name: flake8
================================================

File: playbook.yml
================================================
---
- name: Converge
  hosts: all
  vars:
    mikrotik_exporter_process_names:
      - comm:
        - bash
      - name: "{% raw %}{{ .ExeFull }}:{{ .Matches.Cfgfile }}{% endraw %}"
        exe:
        - /usr/bin/mikrotik-exporter
        cmdline:
        - -config.path\\s+(?P<Cfgfile>\\S+)
  roles:
    - role: jagoanhosting.mikrotik-exporter
================================================

File: test_default.py
================================================
import os
import testinfra.utils.ansible_runner
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
def test_config_file(host):
    f = host.file('/etc/mikrotik_exporter.yml')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
def test_socket(host):
    s = host.socket("tcp://127.0.0.1:9256")
    assert s.is_listening
================================================

File: main.yml
================================================
---
- name: Gather variables for each operating system
  include_vars: "{{ item }}"
  with_first_found:
    - "{{ ansible_distribution_file_variety | lower }}.yml"
    - "{{ ansible_distribution | lower }}.yml"
    - "{{ ansible_os_family | lower }}.yml"
- name: Install dependencies
  package:
    name: "{{ item }}"
    state: present
  register: _install_dep_packages
  until: _install_dep_packages is success
  retries: 5
  delay: 2
  with_items: "{{ node_exporter_dependencies }}"
- name: Git clone mikrotik_exporter
  git:
    repo: 'https://github.com/nshttpd/mikrotik-exporter'
    dest: '/tmp/mikrotik-exporter'
    force: yes
- name: Copy BGP collector from template
  template:
    src: bgp_collector.go.j2
    dest: /tmp/mikrotik-exporter/collector/bgp_collector.go
    owner: root
    group: root
    mode: 0644
- name: compile mikrotik exporter source
  command: 'make'
  args:
    chdir: /tmp/mikrotik-exporter
  retries: 5
  delay: 5
- name: build mikrotik exporter source
  command: 'go build'
  args:
    chdir: /tmp/mikrotik-exporter
  delay: 5
- name: Create /usr/local/bin
  file:
    path: /usr/local/bin
    state: directory
    mode: 0755
- name: Propagate mikrotik_exporter binary
  copy:
    src: "/tmp/mikrotik-exporter/mikrotik-exporter"
    dest: "/usr/local/bin/mikrotik_exporter"
    mode: 0755
    owner: root
    group: root
    remote_src: yes
- name: Configure mikrotik_exporter
  template:
    src: mikrotik_exporter.yml.j2
    dest: "{{ mikrotik_exporter_config_file }}"
    mode: 0644
- name: Copy the mikrotik Exporter systemd service file
  template:
    src: mikrotik_exporter.service.j2
    dest: "{{ mikrotik_exporter_systemd_file }}"
    owner: root
    group: root
    mode: 0644
  notify: restart mikrotik_exporter
- name: Start & enable Process Exporter
  systemd:
    name: mikrotik_exporter
    state: started
    enabled: true
    daemon_reload: true
================================================

File: mikrotik_exporter.service.j2
================================================
#
# This file is managed remotely, all changes will be lost
#
[Unit]
Description=Prometheus Mikrotik Exporter
After=network-online.target
[Service]
Type=simple
ExecStart=/usr/local/bin/mikrotik_exporter \
    -config-file=/etc/mikrotik_exporter.yml \
SyslogIdentifier=mikrotik_exporter
Restart=always
[Install]
WantedBy=multi-user.target
================================================

File: mikrotik_exporter.yml.j2
================================================
# list perangkat yang dimonitor
devices:
  - name: router1name
    address: 10.10.10.2
    user: prometheus #your router username
    password: passwordok #your router password
features:
  bgp: true
#  dhcp: true
#  dhcpv6: true
#  dhcpl: true
#  routes: true
#  pools: true
#  optics: true
#  wlansta: true
#  wlanif: true
#  ipsec: true
  monitor: true
================================================

File: clearlinux.yml
================================================
---
node_exporter_dependencies:
  - git
  - gcc
  - go
================================================

File: debian.yml
================================================
---
node_exporter_dependencies: []
================================================

File: main.yml
================================================
---
go_arch_map:
  i386: '386'
  x86_64: 'amd64'
  aarch64: 'arm64'
  armv7l: 'armv7'
  armv6l: 'armv6'
go_arch: "{{ go_arch_map[ansible_architecture] | default(ansible_architecture) }}"
================================================

File: redhat.yml
================================================
---
node_exporter_dependencies:
  - git
  - gcc
  - go
================================================

File: suse.yml
================================================
---
node_exporter_dependencies: []