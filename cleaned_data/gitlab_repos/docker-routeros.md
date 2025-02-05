# Repository Information
Name: docker-routeros

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
	url = https://gitlab.com/audy018/docker-routeros.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
================================================

File: description
================================================
Unnamed repository; edit this file 'description' to name the repository.
================================================

File: FUNDING.yml
================================================
# These are supported funding model platforms
patreon: efreelancer # Replace with a single Patreon username
================================================

File: cron.sh
================================================
#!/usr/bin/env bash
# Cron fix
cd "$(dirname $0)"
function getTarballs
{
    curl https://mikrotik.com/download/archive -o - 2>/dev/null | \
        grep -o '<a href=['"'"'"][^"'"'"']*['"'"'"]' | \
        sed -e 's/^<a href=["'"'"']//' -e 's/["'"'"']$//' | \
        grep -i vdi | \
        sed 's:.*/::' | \
        sort -V
    curl https://mikrotik.com/download -o - 2>/dev/null | \
        grep -o '<a href=['"'"'"][^"'"'"']*['"'"'"]' | \
        sed -e 's/^<a href=["'"'"']//' -e 's/["'"'"']$//' | \
        grep -i vdi | \
        sed 's:.*/::' | \
        sort -V
}
function getTag
{
    echo "$1" | sed -r 's/chr\-(.*)\.vdi/\1/gi'
}
function checkTag
{
    git rev-list "$1" 2>/dev/null
}
getTarballs | while read line; do
    tag=`getTag "$line"`
    echo ">>> $line >>> $tag"
    if [ "x$(checkTag "$tag")" == "x" ]
        then
            url="https://download.mikrotik.com/routeros/$tag/chr-$tag.vdi"
            if curl --output /dev/null --silent --head --fail "$url"; then
                echo ">>> URL exists: $url"
                sed -r "s/(ROUTEROS_VERSON=\")(.*)(\")/\1$tag\3/g" -i Dockerfile
                git commit -m "Release of RouterOS changed to $tag" -a
                git push
                git tag "$tag"
                git push --tags
            else
                echo ">>> URL don't exist: $url"
            fi
        else
            echo ">>> Tag $tag has been already created"
    fi
done
================================================

File: docker-compose.yml
================================================
version: "3"
services:
  routeros-6-42:
    image: evilfreelancer/docker-routeros:6.42.12
    restart: unless-stopped
    cap_add:
      - NET_ADMIN
    devices:
      - /dev/net/tun
    ports:
      - "12222:22"
      - "12223:23"
      - "18728:8728"
      - "18729:8729"
  routeros-6-45:
    image: evilfreelancer/docker-routeros:6.46.5
    build:
      context: .
    restart: unless-stopped
    cap_add:
      - NET_ADMIN
    devices:
      - /dev/net/tun
    ports:
      - "22222:22"
      - "22223:23"
      - "7777:80"
      - "8728:8728"
      - "8729:8729"
      - "28728:8728"
      - "28729:8729"
================================================

File: Dockerfile
================================================
FROM alpine:3.11
# For access via VNC
EXPOSE 5900
# Default ports of RouterOS
EXPOSE 21 22 23 80 443 8291 8728 8729
# Different VPN services
EXPOSE 50 51 500/udp 4500/udp 1194/tcp 1194/udp 1701 1723
# Change work dir (it will also create this folder if is not exist)
WORKDIR /routeros
# Install dependencies
RUN set -xe \
 && apk add --no-cache --update \
    netcat-openbsd qemu-x86_64 qemu-system-x86_64 \
    busybox-extras iproute2 iputils \
    bridge-utils iptables jq bash python3
# Environments which may be change
ENV ROUTEROS_VERSON="6.46.5"
ENV ROUTEROS_IMAGE="chr-$ROUTEROS_VERSON.vdi"
ENV ROUTEROS_PATH="https://download.mikrotik.com/routeros/$ROUTEROS_VERSON/$ROUTEROS_IMAGE"
# Download VDI image from remote site
RUN wget "$ROUTEROS_PATH" -O "/routeros/$ROUTEROS_IMAGE"
# Copy script to routeros folder
ADD ["./scripts", "/routeros"]
ENTRYPOINT ["/routeros/entrypoint.sh"]
================================================

File: LICENSE
================================================
MIT License
Copyright (c) 2018 Paul Rock
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

File: README.md
================================================
# Mikrotik RouterOS in Docker
This extrasmall image was created for tests purpose only, for example on
this project based unit testing of [routeros-api-php](https://github.com/EvilFreelancer/routeros-api-php) library.
If you need fully functional "RouterOS in Docker" for production usage
look at [VR Network Lab](https://github.com/plajjan/vrnetlab) project.
## How to use
### Create your own `Dockerfile`
List of all available tags is [here](https://hub.docker.com/r/evilfreelancer/docker-routeros/tags/),
`latest` will be used by default.
```dockerfile
FROM evilfreelancer/docker-routeros
ADD ["your-scripts.sh", "/"]
RUN /your-scripts.sh
```
### Use image from docker hub
```bash
docker pull evilfreelancer/docker-routeros
docker run -d -p 2222:22 -p 8728:8728 -p 8729:8729 -p 5900:5900 -ti evilfreelancer/docker-routeros
```
### Use in docker-compose.yml
Example is [here](docker-compose.yml).
```yml
version: "3"
services:
  routeros-6-42:
    image: evilfreelancer/docker-routeros:6.42.12
    restart: unless-stopped
    cap_add:
      - NET_ADMIN
    devices:
      - /dev/net/tun
    ports:
      - "12222:22"
      - "12223:23"
      - "18728:8728"
      - "18729:8729"
  routeros-6-44:
    image: evilfreelancer/docker-routeros:6.46.5
    restart: unless-stopped
    cap_add:
      - NET_ADMIN
    devices:
      - /dev/net/tun
    ports:
      - "22222:22"
      - "22223:23"
      - "28728:8728"
      - "28729:8729"
```
### Build from sources
For this you need download project and build everything from scratch:
```bash
git clone https://github.com/EvilFreelancer/docker-routeros.git
cd docker-routeros
docker build . --tag ros
docker run -d -p 2222:22 -p 8728:8728 -p 8729:8729 -p 5900:5900 -ti ros
```
Now you can connect to your RouterOS container via VNC protocol
(on localhost 5900 port) and via SSH (on localhost 2222 port).
## List of exposed ports
| Description | Ports |
|-------------|-------|
| Defaults    | 21, 22, 23, 80, 443, 8291, 8728, 8729 |
| IPSec       | 50, 51, 500/udp, 4500/udp |
| OpenVPN     | 1194/tcp, 1194/udp |
| L2TP        | 1701 |
| PPTP        | 1723 |
## Links
* https://github.com/joshkunz/qemu-docker
* https://github.com/ennweb/docker-kvm
================================================

File: entrypoint.sh
================================================
#!/usr/bin/env bash
# A bridge of this name will be created to host the TAP interface created for
# the VM
QEMU_BRIDGE='qemubr0'
# DHCPD must have an IP address to run, but that address doesn't have to
# be valid. This is the dummy address dhcpd is configured to use.
DUMMY_DHCPD_IP='10.0.0.1'
# These scripts configure/deconfigure the VM interface on the bridge.
QEMU_IFUP='/routeros/qemu-ifup'
QEMU_IFDOWN='/routeros/qemu-ifdown'
# The name of the dhcpd config file we make
DHCPD_CONF_FILE='/routeros/dhcpd.conf'
function default_intf() {
    ip -json route show | jq -r '.[] | select(.dst == "default") | .dev'
}
# First step, we run the things that need to happen before we start mucking
# with the interfaces. We start by generating the DHCPD config file based
# on our current address/routes. We "steal" the container's IP, and lease
# it to the VM once it starts up.
/routeros/generate-dhcpd-conf.py $QEMU_BRIDGE > $DHCPD_CONF_FILE
default_dev=`default_intf`
# Now we start modifying the networking configuration. First we clear out
# the IP address of the default device (will also have the side-effect of
# removing the default route)
ip addr flush dev $default_dev
# Next, we create our bridge, and add our container interface to it.
ip link add $QEMU_BRIDGE type bridge
ip link set dev $default_dev master $QEMU_BRIDGE
# Then, we toggle the interface and the bridge to make sure everything is up
# and running.
ip link set dev $default_dev up
ip link set dev $QEMU_BRIDGE up
# Finally, start our DHCPD server
udhcpd -I $DUMMY_DHCPD_IP -f $DHCPD_CONF_FILE &
# And run the VM! A brief explanation of the options here:
# -enable-kvm: Use KVM for this VM (much faster for our case).
# -nographic: disable SDL graphics.
# -serial mon:stdio: use "monitored stdio" as our serial output.
# -nic: Use a TAP interface with our custom up/down scripts.
# -drive: The VM image we're booting.
exec qemu-system-x86_64 \
    -nographic -serial mon:stdio \
    -vnc 0.0.0.0:0 \
    -m 256 \
    -nic tap,id=qemu0,script=$QEMU_IFUP,downscript=$QEMU_IFDOWN \
    "$@" \
    -hda $ROUTEROS_IMAGE
================================================

File: entrypoint_with_four_interfaces.sh
================================================
#!/bin/sh
qemu-system-x86_64 \
    -vnc 0.0.0.0:0 \
    -m 256 \
    -hda $ROUTEROS_IMAGE \
    -device e1000,netdev=net0 \
    -netdev user,id=net0,hostfwd=tcp::21-:21,hostfwd=tcp::22-:22,hostfwd=tcp::23-:23,hostfwd=tcp::80-:80,hostfwd=tcp::443-:443,hostfwd=tcp::8291-:8291,hostfwd=tcp::8728-:8728,hostfwd=tcp::8729-:8729 \
    -device e1000,netdev=net1 \
    -netdev user,id=net1 \
    -device e1000,netdev=net2 \
    -netdev user,id=net2 \
    -device e1000,netdev=net3 \
    -netdev user,id=net3
================================================

File: generate-dhcpd-conf.py
================================================
#!/usr/bin/env python3
import argparse
import ipaddress
import json
import re
import socket
import subprocess
from typing import List, Iterable
DEFAULT_ROUTE = 'default'
DEFAULT_DNS_IPS = ('8.8.8.8', '8.8.4.4')
DHCP_CONF_TEMPLATE = """
start {host_addr}
end   {host_addr}
# avoid dhcpd complaining that we have
# too many addresses
maxleases 1
interface {dhcp_intf}
option dns      {dns}
option router   {gateway}
option subnet   {subnet}
option hostname {hostname}
"""
def default_route(routes):
    """Returns the host's default route"""
    for route in routes:
        if route['dst'] == DEFAULT_ROUTE:
            return route
    raise ValueError('no default route')
def addr_of(addrs, dev : str) -> ipaddress.IPv4Interface:
    """Finds and returns the IP address of `dev`"""
    for addr in addrs:
        if addr['ifname'] != dev:
            continue
        info = addr['addr_info'][0]
        return ipaddress.IPv4Interface((info['local'], info['prefixlen']))
    raise ValueError('dev {0} not found'.format(dev))
def generate_conf(intf_name : str, dns : Iterable[str]) -> str:
    """Generates a dhcpd config. `intf_name` is the interface to listen on."""
    with subprocess.Popen(['ip', '-json', 'route'], stdout=subprocess.PIPE) as proc:
        routes = json.load(proc.stdout)
    with subprocess.Popen(['ip', '-json', 'addr'], stdout=subprocess.PIPE) as proc:
        addrs = json.load(proc.stdout)
    droute = default_route(routes)
    host_addr = addr_of(addrs, droute['dev'])
    return DHCP_CONF_TEMPLATE.format(
        dhcp_intf = intf_name,
        dns = ' '.join(dns),
        gateway = droute['gateway'],
        host_addr = host_addr.ip,
        hostname = socket.gethostname(),
        subnet = host_addr.network.netmask,
    )
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('intf_name')
    parser.add_argument('dns_ips', nargs='*')
    args = parser.parse_args()
    dns_ips = args.dns_ips
    if not dns_ips:
        dns_ips = DEFAULT_DNS_IPS
    print(generate_conf(args.intf_name, dns_ips))
================================================