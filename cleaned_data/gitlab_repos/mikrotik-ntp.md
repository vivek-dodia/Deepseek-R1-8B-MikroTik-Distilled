# Repository Information
Name: mikrotik-ntp

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
	url = https://gitlab.com/mikrotik-ansible/mikrotik-ntp.git
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
mikrotik_ntp:
  enabled: yes
  primary-ntp: 0.0.0.0
  secondary-ntp: 0.0.0.0
  server-dns-names:
    - 0.pool.ntp.org
    - 1.pool.ntp.org
    - 2.pool.ntp.org
================================================

File: example.md
================================================
Example usage:
```
mikrotik_ntp:
  enabled: yes # Sets NTP client to enabled/disabled state
  primary-ntp: 0.0.0.0 # Primary NTP server IP. Could be set to 0.0.0.0 or omitted if you prefer using DNS names
  secondary-ntp: 0.0.0.0 # Secondary NTP server IP.  Could be set to 0.0.0.0 or omitted if you prefer using DNS names
  server-dns-names: # List of DNS names of NTP servers. Required configured DNS client on Mikrotik RouterOS
    - 0.pool.ntp.org
    - 1.pool.ntp.org
    - 2.pool.ntp.org
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
# Mikrotik NTP client configuration.
A Role allows configuraiton of Mikrotik RouterOS NTP client.
Examples of usage with comments are in docs/
================================================

File: main.yml
================================================
- name: Configure NTP client
  routeros_command:
    commands:
      - /system ntp client set enabled="{{ mikrotik_ntp['enabled'] | default(true) | bool | ternary('yes', 'no') }}"
      - /system ntp client set primary-ntp="{{ mikrotik_ntp['primary-ntp'] | default('0.0.0.0') }}"
      - /system ntp client set secondary-ntp="{{ mikrotik_ntp['secondary-ntp'] | default('0.0.0.0') }}"
      - /system ntp client set server-dns-names="{{ mikrotik_ntp['server-dns-names'] | default(['0.pool.ntp.org', '1.pool.ntp.org', '2.pool.ntp.org']) | join(',') }}"
  register: mikrotik_ntp_set_out
  failed_when: mikrotik_ntp_set_out['stdout'] | join(';') is search('invalid|error|bad')