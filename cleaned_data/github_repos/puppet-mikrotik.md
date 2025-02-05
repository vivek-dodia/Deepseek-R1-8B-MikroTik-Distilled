# Repository Information
Name: puppet-mikrotik

# Directory Structure
Directory structure:
└── github_repos/puppet-mikrotik/
    │   ├── config
    │   ├── description
    │   ├── HEAD
    │   ├── hooks/
    │   │   ├── applypatch-msg.sample
    │   │   ├── commit-msg.sample
    │   │   ├── fsmonitor-watchman.sample
    │   │   ├── post-update.sample
    │   │   ├── pre-applypatch.sample
    │   │   ├── pre-commit.sample
    │   │   ├── pre-merge-commit.sample
    │   │   ├── pre-push.sample
    │   │   ├── pre-rebase.sample
    │   │   ├── pre-receive.sample
    │   │   ├── prepare-commit-msg.sample
    │   │   ├── push-to-checkout.sample
    │   │   └── update.sample
    │   ├── index
    │   ├── info/
    │   │   └── exclude
    │   ├── logs/
    │   │   ├── HEAD
    │   │   └── refs/
    │   │       ├── heads/
    │   │       │   └── master
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-55fb4c2a20e7dd0122c5b5d68ba872588a9ebbed.idx
    │   │       └── pack-55fb4c2a20e7dd0122c5b5d68ba872588a9ebbed.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── .project
    ├── files/
    │   ├── mtik-4.0.4.gem
    │   └── mtik-4.1.2.gem
    ├── Gemfile
    ├── lib/
    │   └── puppet/
    │       ├── feature/
    │       │   ├── mtik.rb
    │       │   └── net_scp.rb
    │       ├── provider/
    │       │   ├── mikrotik_address_list/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_api.rb
    │       │   ├── mikrotik_bgp_aggregate/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_bgp_instance/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_bgp_instance_vrf/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_bgp_network/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_bgp_peer/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_certificate/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_dhcpv6_client/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_dhcpv6_server/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_dhcp_server/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_dhcp_server_network/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_dns/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_file/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_firewall_rule/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_graph_interface/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_graph_queue/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_graph_resource/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_bgp_vpls/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_bond/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_bridge/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_bridge_msti/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_bridge_msti_port/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_bridge_port/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_bridge_settings/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_bridge_vlan/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_eoip/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_ethernet/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_gre/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_list/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_ppp/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_pppoe_server/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_ppp_server_binding/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_te/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_vlan/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_interface_vrrp/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipsec_group/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipsec_identity/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipsec_mode_config/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipsec_peer/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipsec_policy/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipsec_profile/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipsec_proposal/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipv6_address/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipv6_address_list/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipv6_firewall_rule/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipv6_nd_interface/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipv6_pool/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipv6_route/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ipv6_settings/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ip_address/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ip_hotspot/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ip_hotspot_profile/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ip_pool/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ip_route/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ip_route_rule/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ip_route_vrf/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ip_service/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ip_settings/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_logging_action/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_logging_rule/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_mpls_ldp/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_mpls_ldp_interface/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_mpls_te_interface/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_mpls_te_path/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ospfv3_area/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ospfv3_instance/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ospfv3_interface/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ospf_area/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ospf_area_range/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ospf_instance/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ospf_interface/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ospf_network/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ospf_nmba_neighbor/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_package/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ppp_aaa/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ppp_profile/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ppp_secret/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_ppp_server/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_radius_server/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_romon/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_romon_port/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_routing_filter/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_schedule/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_script/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_snmp/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_snmp_community/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_system/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_tool_email/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_tool_netwatch/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_upgrade/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_upgrade_source/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_user/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_user_aaa/
    │       │   │   └── mikrotik_api.rb
    │       │   ├── mikrotik_user_group/
    │       │   │   └── mikrotik_api.rb
    │       │   └── mikrotik_user_sshkey/
    │       │       └── mikrotik_api.rb
    │       ├── type/
    │       │   ├── mikrotik_address_list.rb
    │       │   ├── mikrotik_bgp_aggregate.rb
    │       │   ├── mikrotik_bgp_instance.rb
    │       │   ├── mikrotik_bgp_instance_vrf.rb
    │       │   ├── mikrotik_bgp_network.rb
    │       │   ├── mikrotik_bgp_peer.rb
    │       │   ├── mikrotik_certificate.rb
    │       │   ├── mikrotik_dhcpv6_client.rb
    │       │   ├── mikrotik_dhcpv6_server.rb
    │       │   ├── mikrotik_dhcp_server.rb
    │       │   ├── mikrotik_dhcp_server_network.rb
    │       │   ├── mikrotik_dns.rb
    │       │   ├── mikrotik_file.rb
    │       │   ├── mikrotik_firewall_rule.rb
    │       │   ├── mikrotik_graph_interface.rb
    │       │   ├── mikrotik_graph_queue.rb
    │       │   ├── mikrotik_graph_resource.rb
    │       │   ├── mikrotik_interface_bgp_vpls.rb
    │       │   ├── mikrotik_interface_bond.rb
    │       │   ├── mikrotik_interface_bridge.rb
    │       │   ├── mikrotik_interface_bridge_msti.rb
    │       │   ├── mikrotik_interface_bridge_msti_port.rb
    │       │   ├── mikrotik_interface_bridge_port.rb
    │       │   ├── mikrotik_interface_bridge_settings.rb
    │       │   ├── mikrotik_interface_bridge_vlan.rb
    │       │   ├── mikrotik_interface_eoip.rb
    │       │   ├── mikrotik_interface_ethernet.rb
    │       │   ├── mikrotik_interface_gre.rb
    │       │   ├── mikrotik_interface_list.rb
    │       │   ├── mikrotik_interface_ppp.rb
    │       │   ├── mikrotik_interface_pppoe_server.rb
    │       │   ├── mikrotik_interface_ppp_server_binding.rb
    │       │   ├── mikrotik_interface_te.rb
    │       │   ├── mikrotik_interface_vlan.rb
    │       │   ├── mikrotik_interface_vrrp.rb
    │       │   ├── mikrotik_ipsec_group.rb
    │       │   ├── mikrotik_ipsec_identity.rb
    │       │   ├── mikrotik_ipsec_mode_config.rb
    │       │   ├── mikrotik_ipsec_peer.rb
    │       │   ├── mikrotik_ipsec_policy.rb
    │       │   ├── mikrotik_ipsec_profile.rb
    │       │   ├── mikrotik_ipsec_proposal.rb
    │       │   ├── mikrotik_ipv6_address.rb
    │       │   ├── mikrotik_ipv6_address_list.rb
    │       │   ├── mikrotik_ipv6_firewall_rule.rb
    │       │   ├── mikrotik_ipv6_nd_interface.rb
    │       │   ├── mikrotik_ipv6_pool.rb
    │       │   ├── mikrotik_ipv6_route.rb
    │       │   ├── mikrotik_ipv6_settings.rb
    │       │   ├── mikrotik_ip_address.rb
    │       │   ├── mikrotik_ip_hotspot.rb
    │       │   ├── mikrotik_ip_hotspot_profile.rb
    │       │   ├── mikrotik_ip_pool.rb
    │       │   ├── mikrotik_ip_route.rb
    │       │   ├── mikrotik_ip_route_rule.rb
    │       │   ├── mikrotik_ip_route_vrf.rb
    │       │   ├── mikrotik_ip_service.rb
    │       │   ├── mikrotik_ip_settings.rb
    │       │   ├── mikrotik_logging_action.rb
    │       │   ├── mikrotik_logging_rule.rb
    │       │   ├── mikrotik_mpls_ldp.rb
    │       │   ├── mikrotik_mpls_ldp_interface.rb
    │       │   ├── mikrotik_mpls_te_interface.rb
    │       │   ├── mikrotik_mpls_te_path.rb
    │       │   ├── mikrotik_ospfv3_area.rb
    │       │   ├── mikrotik_ospfv3_instance.rb
    │       │   ├── mikrotik_ospfv3_interface.rb
    │       │   ├── mikrotik_ospf_area.rb
    │       │   ├── mikrotik_ospf_area_range.rb
    │       │   ├── mikrotik_ospf_instance.rb
    │       │   ├── mikrotik_ospf_interface.rb
    │       │   ├── mikrotik_ospf_network.rb
    │       │   ├── mikrotik_ospf_nmba_neighbor.rb
    │       │   ├── mikrotik_package.rb
    │       │   ├── mikrotik_ppp_aaa.rb
    │       │   ├── mikrotik_ppp_profile.rb
    │       │   ├── mikrotik_ppp_secret.rb
    │       │   ├── mikrotik_ppp_server.rb
    │       │   ├── mikrotik_radius_server.rb
    │       │   ├── mikrotik_romon.rb
    │       │   ├── mikrotik_romon_port.rb
    │       │   ├── mikrotik_routing_filter.rb
    │       │   ├── mikrotik_schedule.rb
    │       │   ├── mikrotik_script.rb
    │       │   ├── mikrotik_snmp.rb
    │       │   ├── mikrotik_snmp_community.rb
    │       │   ├── mikrotik_system.rb
    │       │   ├── mikrotik_tool_email.rb
    │       │   ├── mikrotik_tool_netwatch.rb
    │       │   ├── mikrotik_upgrade.rb
    │       │   ├── mikrotik_upgrade_source.rb
    │       │   ├── mikrotik_user.rb
    │       │   ├── mikrotik_user_aaa.rb
    │       │   ├── mikrotik_user_group.rb
    │       │   └── mikrotik_user_sshkey.rb
    │       └── util/
    │           └── network_device/
    │               ├── mikrotik/
    │               │   ├── device.rb
    │               │   └── facts.rb
    │               ├── mikrotik.rb
    │               └── transport/
    │                   └── mikrotik.rb
    ├── LICENSE
    ├── manifests/
    │   └── init.pp
    ├── metadata.json
    ├── Rakefile
    ├── README.md
    ├── spec/
    │   ├── acceptance/
    │   │   ├── .gitignore
    │   │   ├── address_list_spec.rb
    │   │   ├── bridge_spec.rb
    │   │   ├── dns_spec.rb
    │   │   ├── interface_spec.rb
    │   │   ├── ipv6_firewall_spec.rb
    │   │   ├── ipv6_spec.rb
    │   │   ├── ip_address_spec.rb
    │   │   ├── ip_firewall_spec.rb
    │   │   ├── ip_hotspot_spec.rb
    │   │   ├── ip_service_spec.rb
    │   │   ├── logging_spec.rb
    │   │   ├── mpls_spec.rb
    │   │   ├── mpls_te_spec.rb
    │   │   ├── nodesets/
    │   │   │   └── default.yml
    │   │   ├── ppp_spec.rb
    │   │   ├── radius_spec.rb
    │   │   ├── romon_spec.rb
    │   │   ├── route_spec.rb
    │   │   ├── routing_bgp_spec.rb
    │   │   ├── routing_ospf_spec.rb
    │   │   ├── settings_spec.rb
    │   │   ├── snmp_spec.rb
    │   │   ├── system_spec.rb
    │   │   ├── tools_spec.rb
    │   │   ├── tool_graph_spec.rb
    │   │   ├── upgrade_spec.rb
    │   │   └── user_spec.rb
    │   ├── fixtures/
    │   │   ├── .gitignore
    │   │   ├── testnodes.example.yaml
    │   │   └── upgrade_source.example.yaml
    │   ├── spec_helper_acceptance.rb
    │   └── support/
    │       ├── changing_device_run.rb
    │       ├── empty_device_run.rb
    │       ├── faulty_device_run.rb
    │       ├── idempotent_device_run.rb
    │       ├── idempotent_device_run_after_failures.rb
    │       ├── idempotent_manifest.rb
    │       └── testnodes.rb
    └── vagrant/
        ├── .gitignore
        └── Vagrantfile


# Content
File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/Lavaburn/puppet-mikrotik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master


File: /.git\description
Unnamed repository; edit this file 'description' to name the repository.


File: /.git\HEAD
ref: refs/heads/master


File: /.git\hooks\applypatch-msg.sample
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:


File: /.git\hooks\commit-msg.sample
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}


File: /.git\hooks\fsmonitor-watchman.sample
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
File: /.git\hooks\post-update.sample
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info


File: /.git\hooks\pre-applypatch.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:


File: /.git\hooks\pre-commit.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --


File: /.git\hooks\pre-merge-commit.sample
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:


File: /.git\hooks\pre-push.sample
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0


File: /.git\hooks\pre-rebase.sample
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END


File: /.git\hooks\pre-receive.sample
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi


File: /.git\hooks\prepare-commit-msg.sample
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi


File: /.git\hooks\push-to-checkout.sample
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi


File: /.git\hooks\update.sample
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0


File: /.git\info\exclude
File: /.git\logs\HEAD
0000000000000000000000000000000000000000 c0def79d13daa1d1bb408948358ffd9bf7054888 vivek-dodia <vivek.dodia@icloud.com> 1738606032 -0500	clone: from https://github.com/Lavaburn/puppet-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 c0def79d13daa1d1bb408948358ffd9bf7054888 vivek-dodia <vivek.dodia@icloud.com> 1738606032 -0500	clone: from https://github.com/Lavaburn/puppet-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 c0def79d13daa1d1bb408948358ffd9bf7054888 vivek-dodia <vivek.dodia@icloud.com> 1738606032 -0500	clone: from https://github.com/Lavaburn/puppet-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
d5acfc7556454c02e8414f8025e0424d169bb880 refs/remotes/origin/bugfix_require
9d86fcf0a3fc69cb987a1c953ac48575276e8a69 refs/remotes/origin/main
c0def79d13daa1d1bb408948358ffd9bf7054888 refs/remotes/origin/master
970613d513fb1bf2ceae4143d8b7d13c96a3ec75 refs/remotes/origin/puppet6
f29363c9c2c21b4fabcd780e74c9a6bc376724e1 refs/remotes/origin/v7


File: /.git\refs\heads\master
c0def79d13daa1d1bb408948358ffd9bf7054888


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
/.vagrant/
/.bundle/
/bin/
/log/
/Gemfile.lock


File: /.project
<?xml version="1.0" encoding="UTF-8"?>
<projectDescription>
	<name>puppet-mikrotik</name>
	<comment></comment>
	<projects>
	</projects>
	<buildSpec>
		<buildCommand>
			<name>org.eclipse.xtext.ui.shared.xtextBuilder</name>
			<arguments>
			</arguments>
		</buildCommand>
	</buildSpec>
	<natures>
		<nature>com.puppetlabs.geppetto.pp.dsl.ui.puppetNature</nature>
		<nature>org.eclipse.xtext.ui.shared.xtextNature</nature>
	</natures>
</projectDescription>


File: /Gemfile
source "https://rubygems.org"

group :test do
  gem 'puppet', ENV['PUPPET_VERSION'] || '~> 6.2.0'  
  gem 'puppetlabs_spec_helper', '~> 2.13.1'
end

group :acceptance do
  # Ruby 2.4.5
  gem 'beaker', '~> 4.5.0'
  gem 'beaker-puppet', '~> 1.16.0'
  gem 'beaker-puppet_install_helper', '~> 0.9.7'    
  gem 'beaker-rspec', '~> 6.2.4'
  gem 'beaker-vagrant', '~> 0.6.2'
  gem 'vagrant-wrapper', '~> 2.0.3'  
end


File: /lib\puppet\feature\mtik.rb
require 'puppet/util/feature'

Puppet.features.add(:mtik, :libs => ["mtik"])


File: /lib\puppet\feature\net_scp.rb
require 'puppet/util/feature'

Puppet.features.add(:net_scp, :libs => ["net/scp"])


File: /lib\puppet\provider\mikrotik_address_list\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_address_list).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
    
    sorted_addresses = {}
    address_list_entries = get_all("/ip/firewall/address-list")
    address_list_entries.each do |entry|
      list = entry["list"]
      address = entry["address"]
      
      if !sorted_addresses.key?(list)
        sorted_addresses[list] = []
      end
      
      sorted_addresses[list].push(address)      
    end
    
    sorted_addresses.each do |list, addresses|
      instances << addressList(list, addresses)
    end
    
    instances
  end
  
  def self.addressList(list, addresses)
      new(
        :ensure    => :present,
        :name      => list,
        :addresses => addresses
      )
  end

  def flush
    Puppet.debug("Flushing Address List #{resource[:name]}")
      
    params = {}
    params["list"] = resource[:name]
    
    #Puppet.debug("Params (= Lookup): #{params.inspect}")
   
    list_flush("/ip/firewall/address-list", params, params, :addresses,  "address")
  end
  
  def list_flush(path, params, lookup, list_name, entry_name)  
    Puppet.debug("list_flush(#{path}, #{params.inspect}, #{lookup.inspect}, #{list_name.inspect}, #{entry_name.inspect})")
    
    # create
    if @property_flush[:ensure] == :present
      Puppet.debug("Creating #{path}")
      
      resource[list_name].each do |entry|
        params2 = params.merge({entry_name => entry})
        result = Puppet::Provider::Mikrotik_Api::add(path, params2)
      end
    end
  
    # destroy
    if @property_flush[:ensure] == :absent
      Puppet.debug("Deleting #{path}")
      
      id_list = Puppet::Provider::Mikrotik_Api::lookup_id(path, lookup)
      id_list.each do |id|
        id_lookup = { ".id" => id } 
        result = Puppet::Provider::Mikrotik_Api::remove(path, id_lookup)
      end      
    end      
    
    # update
    if @property_flush.empty?
      Puppet.debug("Updating #{path}")
      
      # Create
      (@property_hash[list_name] - @original_values[list_name]).each do |item|
        params2 = params.merge({entry_name => item})
        result = Puppet::Provider::Mikrotik_Api::add(path, params2)
      end
      
      # Delete
      (@original_values[list_name] - @property_hash[list_name]).each do |item|
        lookup2 = lookup.merge({entry_name => item})
        id_list = Puppet::Provider::Mikrotik_Api::lookup_id(path, lookup2)
        id_list.each do |id|
          id_lookup = { ".id" => id } 
          result = Puppet::Provider::Mikrotik_Api::remove(path, id_lookup)        
        end
      end
    end    
  end
end

File: /lib\puppet\provider\mikrotik_api.rb
require_relative '../util/network_device/mikrotik'
require_relative '../util/network_device/transport/mikrotik'

class Puppet::Provider::Mikrotik_Api < Puppet::Provider
  def self.prefetch(resources)
    nodes = instances
    resources.keys.each do |name|
      if provider = nodes.find { |node| node.name == name }
        resources[name].provider = provider
      end
    end
  end

  def self.transport
    if Puppet::Util::NetworkDevice.current
      # we are in `puppet device`
      Puppet::Util::NetworkDevice.current.transport
    else
      # we are in `puppet resource`
      Puppet::Util::NetworkDevice::Transport::Mikrotik.new(Facter.value(:url))
    end
  end

  def self.connection
    transport.connection
  end
  
  def self.get_all(path)
    Puppet.debug("Retrieving Config #{path}")
    
    objects = connection.get_reply("#{path}/getall")
    
    result = []
    objects.each do |object| 
      #Puppet.debug("Object: #{object}")        
      
      if object.key?('!re')
        result << object.reject { |k, v| ['!re', '.tag'].include? k  }
      end
    end
    result
  end

  def self.set(path, params_hash)
    Puppet.debug("Storing Config #{path}: #{params_hash.inspect}")
    
    params = []
    params << params_hash.collect { |k,v| "=#{k}=#{v}" }
    #Puppet.debug("Params: #{params.inspect}")
    
    result = connection.get_reply("#{path}/set", *params)    # .id => ?.id ???
    Puppet.debug("Set Result: #{result}")
    result.each do |res|
      if res.key?('!trap')
        raise "Error while setting #{path}: #{res['message']}"
      end
    end
  end
  
  def self.add(path, params_hash)
    Puppet.debug("Creating Config #{path}: #{params_hash.inspect}")
    
    params = []
    params << params_hash.collect { |k,v| "=#{k}=#{v}" }
    #Puppet.debug("Params: #{params}")
    
    result = connection.get_reply("#{path}/add", *params)    
    Puppet.debug("Add Result: #{result}")
    result.each do |res|
      if res.key?('!trap')
        raise "Error while adding #{path}: #{res['message']}"
      end
    end
  end

  def self.remove(path, params_hash)
    Puppet.debug("Removing Config #{path}: #{params_hash.inspect}")
    
    params = []
    params << params_hash.collect { |k,v| "=#{k}=#{v}" }
    
    result = connection.get_reply("#{path}/remove", *params)

    Puppet.debug("Remove Result: #{result}")  
    result.each do |res|
      if res.key?('!trap')
        raise "Error while removing #{path}: #{res['message']}"
      end
    end
  end

  def self.move(path, params_hash)
    Puppet.debug("Moving Config #{path}: #{params_hash.inspect}")
    
    params = []
    params << params_hash.collect { |k,v| "=#{k}=#{v}" }
    
    result = connection.get_reply("#{path}/move", *params)
    Puppet.debug("Move Result: #{result}")
    result.each do |res|
      if res.key?('!trap')
        raise "Error while moving #{path}: #{res['message']}"
      end
    end
  end
  
  def self.enable(path, params_hash)
    Puppet.debug("Enabling #{path}: #{params_hash.inspect}")

    params = []
    params << params_hash.collect { |k,v| "=#{k}=#{v}" }
    #Puppet.debug("Params: #{params.inspect}")
    
    result = connection.get_reply("#{path}/enable", *params)    # .id => ?.id ???
    Puppet.debug("Set Result: #{result}")
    result.each do |res|
      if res.key?('!trap')
        raise "Error while setting #{path}: #{res['message']}"
      end
    end
  end

  def self.disable(path, params_hash)
    Puppet.debug("Disabling #{path}: #{params_hash.inspect}")

    params = []
    params << params_hash.collect { |k,v| "=#{k}=#{v}" }
    #Puppet.debug("Params: #{params.inspect}")
    
    result = connection.get_reply("#{path}/disable", *params)    # .id => ?.id ???
    Puppet.debug("Set Result: #{result}")
    result.each do |res|
      if res.key?('!trap')
        raise "Error while setting #{path}: #{res['message']}"
      end
    end
  end

  def self.command(path, params_hash = {})
    Puppet.debug("Running Command: #{path}: #{params_hash.inspect}")

    params = []
    params << params_hash.collect { |k,v| "=#{k}=#{v}" }
      
    result = connection.get_reply(path, *params)
    Puppet.debug("Command Result: #{result}")
    result.each do |res|
      if res.key?('!trap')
        raise "Error while running command #{path}: #{res['message']}"
      end
    end
  end
  
  def initialize(value = {})
    super(value)
    
    if value.is_a? Hash
      @original_values = value.clone
    else
      @original_values = {}
    end
    
    @property_flush = {}
  end
  
  def exists?
    [:present, :enabled, :disabled].include?(@property_hash[:ensure]) 
  end
  
  def create
    @property_flush[:ensure] = :present
  end
  
  def destroy        
    @property_flush[:ensure] = :absent
  end
  
  def simple_flush(path, params, lookup)  
    #Puppet.debug("simple_flush(#{path}, #{params.inspect}, #{lookup.inspect})")
    
    # create
    if @property_flush[:ensure] == :present and @original_values.empty?
      Puppet.debug("Creating #{path}")
      
      result = Puppet::Provider::Mikrotik_Api::add(path, params)
    end
  
    # destroy
    if @property_flush[:ensure] == :absent
      Puppet.debug("Deleting #{path}")
      
      id_list = Puppet::Provider::Mikrotik_Api::lookup_id(path, lookup)
      id_list.each do |id|
        id_lookup = { ".id" => id } 
        result = Puppet::Provider::Mikrotik_Api::remove(path, id_lookup)
      end      
    end      
    
    # update
    if ! @original_values.empty?
      Puppet.debug("Updating #{path}")
        
      id_list = Puppet::Provider::Mikrotik_Api::lookup_id(path, lookup)
      id_list.each do |id|
        params = params.merge({ ".id" => id })
        result = Puppet::Provider::Mikrotik_Api::set(path, params)
      end
    end    
  end
  
  def self.lookup_id(path, lookup)
    id_list = []
      
    query_words = lookup.collect { |k,v| "?#{k}=#{v}" }
    
    objects = connection.get_reply("#{path}/getall", *query_words)      
    objects.each do |object| 
      if object.key?('!re')
        id_list << object[".id"]
      end
    end      
    #Puppet.debug("ID list for #{path} with #{lookup.inspect}: #{id_list.inspect}")
      
    id_list
  end
  
  # Different ensure options can be stored in "state"
  def setState(state)
    @property_hash[:state] = state
  end  
  
  def getState
    return :absent if @property_hash[:state].nil?
    
    @property_hash[:state]
  end  
  
  def self.convertStringToBool(str)
    result = str == 'true'?true:false
    result
  end
  
  def self.convertBoolToYesNo(str)
    result = str.to_s == 'true' ? "yes" : "no"
    result
  end
  
  def self.convertYesNoToBool(str)
    result = str == 'yes'?true:false
    result
  end
end

File: /lib\puppet\provider\mikrotik_bgp_aggregate\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_bgp_aggregate).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    bgp_aggregates = Puppet::Provider::Mikrotik_Api::get_all("/routing/bgp/aggregate")
    aggregates = bgp_aggregates.collect { |bgp_aggregate| bgpAggregate(bgp_aggregate) }    
    aggregates
  end
  
  def self.bgpAggregate(data)     
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end   

    new(
      :ensure             => :present,
      :state              => state,
      :name               => data['prefix'],
      :instance           => data['instance'],
      :summary_only       => data['summary-only'],
      :inherit_attributes => data['inherit-attributes'],
      :include_igp        => data['include-igp'],
      :attribute_filter   => data['attribute-filter'],
      :suppress_filter    => data['suppress-filter'],
      :advertise_filter   => data['advertise-filter']
    )
  end

  def flush
    Puppet.info("Flushing BGP Aggregate #{resource[:name]}")
    
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end

    params["prefix"] = resource[:name]
    params["instance"] = resource[:instance]

    params["attribute-filter"] = resource[:attribute_filter] if ! resource[:attribute_filter].nil?
    params["suppress-filter"] = resource[:suppress_filter] if ! resource[:suppress_filter].nil?
    params["advertise-filter"] = resource[:advertise_filter] if ! resource[:advertise_filter].nil?

    params["summary-only"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:summary_only]) if ! resource[:summary_only].nil?
    params["inherit-attributes"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:inherit_attributes]) if ! resource[:inherit_attributes].nil?
    params["include-igp"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:include_igp]) if ! resource[:include_igp].nil?

    lookup = {}
    lookup["prefix"] = resource[:name]

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/bgp/aggregate", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_bgp_instance\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_bgp_instance).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    bgp_instances = Puppet::Provider::Mikrotik_Api::get_all("/routing/bgp/instance")
    instances = bgp_instances.collect { |bgp_instance| bgpInstance(bgp_instance) }    
    instances
  end
  
  def self.bgpInstance(data)        
    new(
      :ensure                      => :present,
      :name                        => data['name'],
      :as                          => data['as'],
      :router_id                   => data['router-id'],
      :redistribute_connected      => data['redistribute-connected'].to_sym,
      :redistribute_static         => data['redistribute-static'].to_sym,
      :redistribute_ospf           => data['redistribute-ospf'].to_sym,
      :redistribute_bgp            => data['redistribute-other-bgp'].to_sym,
      :out_filter                  => data['out-filter'],
      :client_to_client_reflection => data['client-to-client-reflection'].to_sym,
      :routing_table               => data['routing-table']
    )
  end

  def flush
    Puppet.info("Flushing BGP Instance #{resource[:name]}")
    
    params = {}
    params["name"] = resource[:name]
    params["as"] = resource[:as] if ! resource[:as].nil?
    params["router-id"] = resource[:router_id] if ! resource[:router_id].nil?
    params["redistribute-connected"] = resource[:redistribute_connected] if ! resource[:redistribute_connected].nil?
    params["redistribute-static"] = resource[:redistribute_static] if ! resource[:redistribute_static].nil?
    params["redistribute-ospf"] = resource[:redistribute_ospf] if ! resource[:redistribute_ospf].nil?
    params["redistribute-other-bgp"] = resource[:redistribute_bgp] if ! resource[:redistribute_bgp].nil?
    params["out-filter"] = resource[:out_filter] if ! resource[:out_filter].nil?
    params["client-to-client-reflection"] = resource[:client_to_client_reflection] if ! resource[:client_to_client_reflection].nil?
    params["routing-table"] = resource[:routing_table] if ! resource[:routing_table].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/bgp/instance", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_bgp_instance_vrf\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_bgp_instance_vrf).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik

  mk_resource_methods

  def self.instances
    bgp_vrfs = Puppet::Provider::Mikrotik_Api::get_all("/routing/bgp/instance/vrf")
    vrfs = bgp_vrfs.collect { |bgp_vrf| bgpVRF(bgp_vrf) }    
    vrfs
  end

  def self.bgpVRF(data)  
    # Puppet.debug("Data: #{data.inspect}")
     
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end

    new(
      :ensure                 => :present,
      :state                  => state,
      :name                   => data['routing-mark'],
      :instance               => data['instance'],
      :redistribute_connected => data['redistribute-connected'].to_sym,
      :redistribute_static    => data['redistribute-static'].to_sym,
      :redistribute_rip       => data['redistribute-rip'].to_sym,
      :redistribute_ospf      => data['redistribute-ospf'].to_sym,
      :redistribute_bgp       => data['redistribute-other-bgp'].to_sym,
      :in_filter              => data['in-filter'],
      :out_filter             => data['out-filter']
    )
  end

  def flush
    Puppet.info("Flushing BGP Instance VRF #{resource[:name]}")

    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end

    params["routing-mark"] = resource[:name]
    params["instance"] = resource[:instance]
    params["redistribute-connected"] = resource[:redistribute_connected] if ! resource[:redistribute_connected].nil?
    params["redistribute-static"] = resource[:redistribute_static] if ! resource[:redistribute_static].nil?
    params["redistribute-rip"] = resource[:redistribute_rip] if ! resource[:redistribute_rip].nil?
    params["redistribute-ospf"] = resource[:redistribute_ospf] if ! resource[:redistribute_ospf].nil?
    params["redistribute-other-bgp"] = resource[:redistribute_bgp] if ! resource[:redistribute_bgp].nil?
    params["in-filter"] = resource[:in_filter] if ! resource[:in_filter].nil?
    params["out-filter"] = resource[:out_filter] if ! resource[:out_filter].nil?

    lookup = {}
    lookup["routing-mark"] = resource[:name]
    lookup["instance"] = resource[:instance]

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/bgp/instance/vrf", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_bgp_network\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_bgp_network).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    bgp_networks = Puppet::Provider::Mikrotik_Api::get_all("/routing/bgp/network")
    networks = bgp_networks.collect { |bgp_network| bgpNetwork(bgp_network) }    
    networks
  end
  
  def self.bgpNetwork(data)     
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end   
    
    new(
      :ensure      => :present,
      :state       => state,
      :name        => data['network'],
      :synchronize => data['synchronize']
    )
  end

  def flush
    Puppet.info("Flushing BGP Network #{resource[:name]}")
    
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["network"] = resource[:name]
    params["synchronize"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:synchronize]) if ! resource[:synchronize].nil?

    lookup = {}
    lookup["network"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/bgp/network", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_bgp_peer\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_bgp_peer).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    bgp_peers = Puppet::Provider::Mikrotik_Api::get_all("/routing/bgp/peer")
    instances = bgp_peers.collect { |bgp_peer| bgpPeer(bgp_peer) }    
    instances
  end
  
  def self.bgpPeer(data) 
#    Puppet.debug("BGP Peer: #{data.inspect}")
      
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end   
    
    new(
      :ensure                   => :present,
      :state                    => state,
      :name                     => data['name'],
      :instance                 => data['instance'],
      :peer_address             => data['remote-address'],          
      :peer_port                => data['remote-port'],
      :peer_as                  => data['remote-as'],
      :tcp_md5_key              => data['tcp-md5-key'],
      :nexthop_choice           => data['nexthop-choice'],
      :multihop                 => data['multihop'],
      :route_reflect            => data['route-reflect'],
      :hold_time                => data['hold-time'],
      :keepalive_time           => data['keepalive-time'],
      :ttl                      => data['ttl'],
      :max_prefix_limit         => data['max-prefix-limit'],
      :max_prefix_restart_time  => data['max-prefix-restart-time'],
      :in_filter                => data['in-filter'],
      :out_filter               => data['out-filter'],      
      :allow_as_in              => data['allow-as-in'],
      :remove_private_as        => data['remove-private-as'],
      :as_override              => data['as-override'],
      :default_originate        => data['default-originate'],
      :passive                  => data['passive'],
      :use_bfd                  => data['use-bfd'],
      :address_families         => data['address-families'].split(','),
      :source                   => data['update-source'],
      :comment                  => data['comment']
    )
  end

  def flush
    Puppet.debug("Flushing BGP Peer #{resource[:name]}")

    params = {}
    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end

    params["name"] = resource[:name]
    params["instance"] = resource[:instance] if ! resource[:instance].nil?
    params["remote-address"] = resource[:peer_address] if ! resource[:peer_address].nil?
    params["remote-port"] = resource[:peer_port] if ! resource[:peer_port].nil?
    params["remote-as"] = resource[:peer_as] if ! resource[:peer_as].nil?
    params["tcp-md5-key"] = resource[:tcp_md5_key] if ! resource[:tcp_md5_key].nil?
    params["nexthop-choice"] = resource[:nexthop_choice] if ! resource[:nexthop_choice].nil?
    params["multihop"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:multihop]) if ! resource[:multihop].nil?
    params["route-reflect"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:route_reflect]) if ! resource[:route_reflect].nil?
    params["hold-time"] = resource[:hold_time] if ! resource[:hold_time].nil?
    params["keepalive-time"] = resource[:keepalive_time] if ! resource[:keepalive_time].nil?
    params["ttl"] = resource[:ttl] if ! resource[:ttl].nil?
    params["max-prefix-limit"] = resource[:max_prefix_limit] if ! resource[:max_prefix_limit].nil?
    params["max-prefix-restart-time"] = resource[:max_prefix_restart_time] if ! resource[:max_prefix_restart_time].nil?
    params["in-filter"] = resource[:in_filter] if ! resource[:in_filter].nil?
    params["out-filter"] = resource[:out_filter] if ! resource[:out_filter].nil?
    params["allow-as-in"] = resource[:allow_as_in] if ! resource[:allow_as_in].nil?
    params["remove-private-as"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:remove_private_as]) if ! resource[:remove_private_as].nil?
    params["as-override"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:as_override]) if ! resource[:as_override].nil?
    params["default-originate"] = resource[:default_originate] if ! resource[:default_originate].nil?
    params["passive"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:passive]) if ! resource[:passive].nil?
    params["use-bfd"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:use_bfd]) if ! resource[:use_bfd].nil?
    params["address-families"] = resource[:address_families].join(',') if ! resource[:address_families].nil?    
    params["update-source"] = resource[:source] if ! resource[:source].nil?
    params["comment"] = resource[:comment] if ! resource[:comment].nil?
    
    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/bgp/peer", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_certificate\mikrotik_api.rb
require_relative '../mikrotik_api'
require 'openssl'

Puppet::Type.type(:mikrotik_certificate).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  confine :feature => :net_scp

  mk_resource_methods

  def self.instances
    certs = Puppet::Provider::Mikrotik_Api::get_all("/certificate")
    certs.map {|data| cert(data) }
  end

  CERTNAME_REGEX = /^(.*)\.crt_(\d)+$/

  def self.cert(data)
    md = data['name'].match(CERTNAME_REGEX)
    if md
      rname = md.captures[0]
      rnum  = md.captures[1]
    else
      rname = data['name']
      rnum  = 0
    end
    new(
      ensure: :present,
      name: rname,
      fingerprint: data['fingerprint'],
      has_private_key: data['private-key'],
      number: rnum,
    )
  end

  def flush
    cert_filename = "#{resource[:name]}.crt"
    upload_data(resource[:certificate], cert_filename)
    self.class.import('file-name' => cert_filename)
    cleanup(cert_filename)

    if !resource[:private_key].nil?
      key_filename = "#{resource[:name]}.key"
      upload_data(resource[:private_key],key_filename)
      if resource[:private_key_passphrase]
        self.class.import('file-name': key_filename, passphrase: resource[:private_key_passphrase])
      else
        self.class.import('file-name': key_filename)
      end
      cleanup(key_filename)
    end
  end


  def self.import(params_hash)
    Puppet.debug("Importing certificate: #{params_hash.inspect}")
    
    params = []
    params << params_hash.collect { |k,v| "=#{k}=#{v}" }
    
    result = connection.get_reply("/certificate/import", *params)
    Puppet.debug("Import Result: #{result}")
    result.each do |res|
      if res.key?('!trap')
        raise "Error while importing certificate: #{res['message']}"
      end
    end
  end

  def upload_data(data,filename)
    Puppet.debug("Uploading data to file #{filename}")
    c = self.class.transport.connection
    data = StringIO.new(data)
    path = filename
    Net::SCP.upload!(c.host,c.user,data,path,ssh: {password: c.pass})
    sleep(5)
  end

  def cleanup(filename)
    Puppet.debug("Deleting #{filename}")
    self.class.remove('/file',{ numbers: filename })    
  end

end

File: /lib\puppet\provider\mikrotik_dhcpv6_client\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_dhcpv6_client).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    servers = Puppet::Provider::Mikrotik_Api::get_all("/ipv6/dhcp-client")
    servers.each do |server|
      object = dhcpClient(server)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end
  
  def self.dhcpClient(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    request = data['request'].split(',')
        
    new(
      :ensure             => :present,
      :state              => state,
      :name               => data['interface'],
      :request_address    => (request.include?("address")?'true':'false'),# TODO: verify string boolean ?,
      :request_prefix     => (request.include?("prefix")?'true':'false'),# TODO: verify string boolean ?,
      :pool_name          => data['pool-name'],
      :pool_prefix_length => data['pool-prefix-length'],
      :prefix_hint        => data['prefix-hint'],
      :use_peer_dns       => data['use-peer-dns'],
      :add_default_route  => data['add-default-route']
    )
  end

  def flush
    Puppet.debug("Flushing DHCPv6 Client #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    if !resource[:request_address].nil? || !resource[:request_prefix].nil?
      request = []
      request.push("address") if resource[:request_address]
      request.push("prefix")  if resource[:request_prefix]
      params["request"] = request.join(',')
    end
      
    params["interface"] = resource[:name]    
    params["pool-name"] = resource[:pool_name] if !resource[:pool_name].nil?
    params["pool-prefix-length"] = resource[:pool_prefix_length] if !resource[:pool_prefix_length].nil?
    params["prefix-hint"] = resource[:prefix_hint] if !resource[:prefix_hint].nil?
    params["use-peer-dns"] = resource[:use_peer_dns] if !resource[:use_peer_dns].nil?
    params["add-default-route"] = resource[:add_default_route] if !resource[:add_default_route].nil?

    lookup = {}
    lookup["interface"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ipv6/dhcp-client", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_dhcpv6_server\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_dhcpv6_server).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    servers = Puppet::Provider::Mikrotik_Api::get_all("/ipv6/dhcp-server")
    servers.each do |server|
      object = dhcpServer(server)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end
  
  def self.dhcpServer(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
        
    new(
      :ensure       => :present,
      :state        => state,
      :name         => data['name'],
      :interface    => data['interface'],
      :lease_time   => data['lease-time'],
      :address_pool => data['address-pool']
    )
  end

  def flush
    Puppet.debug("Flushing DHCPv6 Server #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["name"] = resource[:name]
    params["interface"] = resource[:interface] if !resource[:interface].nil?
    params["lease-time"] = resource[:lease_time] if !resource[:lease_time].nil?
    params["address-pool"] = resource[:address_pool] if !resource[:address_pool].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ipv6/dhcp-server", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_dhcp_server\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_dhcp_server).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    servers = Puppet::Provider::Mikrotik_Api::get_all("/ip/dhcp-server")
    servers.each do |server|
      object = dhcpServer(server)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end
  
  def self.dhcpServer(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
        
    new(
      :ensure           => :present,
      :state            => state,
      :name             => data['name'],
      :interface        => data['interface'],
      :relay            => data['relay'],
      :lease_time       => data['lease-time'],
      :bootp_lease_time => data['bootp-lease-time'],
      :address_pool     => data['address-pool'],
      :src_address      => data['src-address'],
      :delay_threshold  => data['delay-threshold'],
      :authoritative    => data['authoritative'],
      :bootp_support    => data['bootp-support'],
      :lease_script     => data['lease-script'],
      :add_arp          => (data['add-arp'].nil? ? :false : data['add-arp']),
      :always_broadcast => (data['always-broadcast'].nil? ? :false : data['always-broadcast']),
      :use_radius       => (data['use-radius'].nil? ? :false : data['use-radius'])
    )
  end

  def flush
    Puppet.debug("Flushing DHCP Server #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["name"] = resource[:name]
    params["interface"] = resource[:interface] if !resource[:interface].nil?
    params["relay"] = resource[:relay] if !resource[:relay].nil?
    params["lease-time"] = resource[:lease_time] if !resource[:lease_time].nil?
    params["bootp-lease-time"] = resource[:bootp_lease_time] if !resource[:bootp_lease_time].nil?
    params["address-pool"] = resource[:address_pool] if !resource[:address_pool].nil?
    params["src-address"] = resource[:src_address] if !resource[:src_address].nil?
    params["delay-threshold"] = resource[:delay_threshold] if !resource[:delay_threshold].nil?
    params["authoritative"] = resource[:authoritative] if !resource[:authoritative].nil?
    params["bootp-support"] = resource[:bootp_support] if !resource[:bootp_support].nil?
    params["lease-script"] = resource[:lease_script] if !resource[:lease_script].nil?
      
    params["add-arp"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:add_arp]) if ! resource[:add_arp].nil?
    params["always-broadcast"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:always_broadcast]) if ! resource[:always_broadcast].nil?
    params["use-radius"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:use_radius]) if ! resource[:use_radius].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/dhcp-server", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_dhcp_server_network\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_dhcp_server_network).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    networks = Puppet::Provider::Mikrotik_Api::get_all("/ip/dhcp-server/network")
    networks.each do |network|
      object = dhcpServerNetwork(network)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end
  
  def self.dhcpServerNetwork(data)
    new(
      :ensure           => :present,
      :name             => data['address'],
      :gateways         => data['gateway'].nil? ? nil : data['gateway'].split(','),
      :netmask          => data['netmask'],
      :dns_servers      => data['dns-server'].nil? ? nil : data['dns-server'].split(','),
      :domain           => data['domain'],
      :wins_servers     => data['wins-server'].nil? ? nil : data['wins-server'].split(','),
      :ntp_servers      => data['ntp-server'].nil? ? nil : data['ntp-server'].split(','),
      :caps_managers    => data['caps-manager'].nil? ? nil : data['caps-manager'].split(','),
      :next_server      => data['next-server'],
      :boot_file_name   => data['boot-file-name'],
      :dhcp_options     => data['dhcp-option'].nil? ? nil : data['dhcp-option'].split(','),
      :dhcp_option_sets => data['dhcp-option-set'].nil? ? nil : data['dhcp-option-set'].split(',')
    )
  end

  def flush
    Puppet.debug("Flushing DHCP Server Network #{resource[:name]}")
      
    params = {}
    params["address"] = resource[:name]
    params["gateway"] = resource[:gateways].join(',') if !resource[:gateways].nil?
    params["netmask"] = resource[:netmask] if !resource[:netmask].nil?
    params["dns-server"] = resource[:dns_servers].join(',') if !resource[:dns_servers].nil?
    params["domain"] = resource[:domain] if !resource[:domain].nil?
    params["wins-server"] = resource[:wins_servers].join(',') if !resource[:wins_servers].nil?
    params["ntp-server"] = resource[:ntp_servers].join(',') if !resource[:ntp_servers].nil?
    params["caps-manager"] = resource[:caps_managers].join(',') if !resource[:caps_managers].nil?
    params["next-server"] = resource[:next_server] if !resource[:next_server].nil?
    params["boot-file-name"] = resource[:boot_file_name] if !resource[:boot_file_name].nil?
    params["dhcp-option"] = resource[:dhcp_options].join(',') if !resource[:dhcp_options].nil?
    params["dhcp-option-set"] = resource[:dhcp_option_sets].join(',') if !resource[:dhcp_option_sets].nil?

    lookup = {}
    lookup["address"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/dhcp-server/network", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_dns\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_dns).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
      
    dns = Puppet::Provider::Mikrotik_Api::get_all("/ip/dns")
    dns.each do |data|
      object = dnsSettings(data)
      if object != nil
        instances << object
      end
    end

    instances
  end
  
  def self.dnsSettings(data)
    new(
      :name                  => 'dns',
      :servers               => data['servers'].split(','),
      :allow_remote_requests => data['allow-remote-requests']
    )
  end

  def flush
    Puppet.debug("Flushing DNS")
    
    if (@property_hash[:name] != 'dns') 
      raise "There is only one set of DNS settings. Title (name) should be -dns-"
    end
    
    update = {}
    update["servers"] = @property_hash[:servers].join(",")
    update["allow-remote-requests"] = @property_hash[:allow_remote_requests].to_s
    
    result = Puppet::Provider::Mikrotik_Api::set("/ip/dns", update)
  end
end

File: /lib\puppet\provider\mikrotik_file\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_file).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  confine :feature => :net_scp

  mk_resource_methods

  def self.instances
    files = Puppet::Provider::Mikrotik_Api::get_all("/file")
    files.map {|data| file(data)}
  end

  def self.file(data)
    new(
      ensure: :present, 
      name: data['name'],
      content: data['contents'],
    )
  end

  def flush
    if resource[:ensure] == :present
      c = self.class.transport.connection
      data = StringIO.new(resource['content'])
      path = resource['name']
      Net::SCP.upload!(c.host,c.user,data,path,ssh: {password: c.pass})
    else
      Puppet::Provider::Mikrotik_Api::remove("/file", {'numbers' => resource['name']})
    end
  end

end

File: /lib\puppet\provider\mikrotik_firewall_rule\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_firewall_rule).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []

    filter_rules = get_all("/ip/firewall/filter")
    filter_rules.each do |rule|
      object = firewallRule(rule, 'filter', filter_rules)
      if object != nil
        instances << object
      end
    end

    nat_rules = get_all("/ip/firewall/nat")
    nat_rules.each do |rule|
      object = firewallRule(rule, 'nat', nat_rules)
      if object != nil
        instances << object
      end
    end

    mangle_rules = get_all("/ip/firewall/mangle")
    mangle_rules.each do |rule|
      object = firewallRule(rule, 'mangle', mangle_rules)
      if object != nil
        instances << object
      end      
    end

    instances
  end
  
  def self.firewallRule(rule, table, all_rules)
    if rule['comment'] != nil  
      if rule['disabled'] == 'true'
        state = :disabled
      else
        state = :enabled
      end

      chain_order = getChainOrder(rule['.id'], rule['chain'], all_rules)

      new(
        :ensure                    => :present,
        :state                     => state,
        :name                      => rule['comment'],
        :table                     => table,
        # General
        :chain                     => rule['chain'],
        :chain_order               => chain_order.to_s,
        :src_address               => rule['src-address'],
        :dst_address               => rule['dst-address'],
        :protocol                  => rule['protocol'],
        :src_port                  => rule['src-port'],
        :dst_port                  => rule['dst-port'],
        :port                      => rule['port'],
        :p2p                       => rule['p2p'],
        :in_interface              => rule['in-interface'],
        :out_interface             => rule['out-interface'],
        :in_interface_list         => rule['in-interface-list'],
        :out_interface_list        => rule['out-interface-list'],
        :packet_mark               => rule['packet-mark'],
        :connection_mark           => rule['connection-mark'],
        :routing_mark              => rule['routing-mark'],
        :routing_table             => rule['routing-table'],
        :connection_type           => rule['connection-type'],
        :connection_state          => rule['connection-state'],
        :connection_nat_state      => rule['connection-nat-state'],
        # Advanced
        :src_address_list          => rule['src-address-list'],
        :dst_address_list          => rule['dst-address-list'],
        :layer7_protocol           => rule['layer7-protocol'],
        :content                   => rule['content'],
        :connection_bytes          => rule['connection-bytes'],
        :connection_rate           => rule['connection-rate'],
        :per_connection_classifier => rule['per-connection-classifier'],
        :src_mac_address           => rule['src-mac-address'],
        :in_bridge_port            => rule['in-bridge-port'],
        :out_bridge_port           => rule['out-bridge-port'],
        :in_bridge_port_list       => rule['in-bridge-port-list'],
        :out_bridge_port_list      => rule['out-bridge-port-list'],
        :ipsec_policy              => rule['ipsec-policy'],
        :tls_host                  => rule['tls-host'],
        :ingress_priority          => rule['ingress-priority'],
        :priority                  => rule['priority'],
        :dscp                      => rule['dscp'],
        :tcp_mss                   => rule['tcp-mss'],
        :packet_size               => rule['packet-size'],
        :random                    => rule['random'],
        :tcp_flags                 => rule['tcp-flags'],      
        :ipv4_options              => rule['ipv4-options'],
        :ttl                       => rule['ttl'],
        # Extra  
        :connection_limit          => rule['connection-limit'],
        :limit                     => rule['limit'],
        :dst_limit                 => rule['dst-limit'],
        :nth                       => rule['nth'],
        :time                      => rule['time'],
        :src_address_type          => rule['src-address-type'],
        :dst_address_type          => rule['dst-address-type'],
        :psd                       => rule['psd'],
        :hotspot                   => rule['hotspot'],
        :fragment                  => rule['fragment'],      
        # Action    
        :action                    => rule['action'],
        :log                       => rule['log'],
        :log_prefix                => rule['log-prefix'],
        :jump_target               => rule['jump-target'],
        :address_list              => rule['address-list'],
        :address_list_timeout      => rule['address-list-timeout'],
        :reject_with               => rule['reject-with'],
        :to_addresses              => rule['to-addresses'],
        :to_ports                  => rule['to-ports'],
        :new_connection_mark       => rule['new-connection-mark'],
        :new_dscp                  => rule['new-dscp'],
        :new_mss                   => rule['new-mss'],
        :new_packet_mark           => rule['new-packet-mark'],
        :new_priority              => rule['new-priority'],
        :new_routing_mark          => rule['new-routing-mark'],
        :new_ttl                   => rule['new-ttl'],
        :route_dst                 => rule['route-dst'],
        :sniff_id                  => rule['sniff-id'],
        :sniff_target              => rule['sniff-target'],
        :sniff_target_port         => rule['sniff-target-port']
      )
    end
  end

  def flush
    Puppet.debug("Flushing Firewall Rule #{resource[:name]}")

    if @property_flush[:ensure] == :absent
      if @property_hash[:table].nil?
        raise "Table is always a required parameter."
      end
      table = @property_hash[:table]
    else
      if resource[:table].nil? or resource[:chain].nil?
        raise "Table and Chain are required parameters."
      end
      table = resource[:table]
    end
    
    params = {}
        
    if @property_hash[:state] == :disabled
      params["disabled"] = true
    elsif @property_hash[:state] == :enabled
      params["disabled"] = false
    end

    if !resource[:chain_order].nil?
      table_rules = Puppet::Provider::Mikrotik_Api::get_all("/ip/firewall/#{table}")
      ids = self.class.getChainIds(resource[:chain], table_rules)
      
      if @property_flush[:ensure] == :present
        unless resource[:chain_order] > ids.length
          rule_id_after = ids[resource[:chain_order].to_i - 1]# index starts at 0, order starts at 1
          params["place-before"] = rule_id_after
        end
      end
    end

    params["comment"] = resource[:name]
    # General
    params["chain"] = resource[:chain] if ! resource[:chain].nil?   
    params["src-address"] = resource[:src_address] if ! resource[:src_address].nil?   
    params["dst-address"] = resource[:dst_address] if ! resource[:dst_address].nil?   
    params["protocol"] = resource[:protocol] if ! resource[:protocol].nil?  
    params["src-port"] = resource[:src_port] if ! resource[:src_port].nil?  
    params["dst-port"] = resource[:dst_port] if ! resource[:dst_port].nil?  
    params["port"] = resource[:port] if ! resource[:port].nil?  
    params["p2p"] = resource[:p2p] if ! resource[:p2p].nil?        
    params["in-interface"] = resource[:in_interface] if ! resource[:in_interface].nil?  
    params["out-interface"] = resource[:out_interface] if ! resource[:out_interface].nil?  
    params["in-interface-list"] = resource[:in_interface_list] if ! resource[:in_interface_list].nil?  
    params["out-interface-list"] = resource[:out_interface_list] if ! resource[:out_interface_list].nil?  
    params["packet-mark"] = resource[:packet_mark] if ! resource[:packet_mark].nil?  
    params["connection-mark"] = resource[:connection_mark] if ! resource[:connection_mark].nil?  
    params["routing-mark"] = resource[:routing_mark] if ! resource[:routing_mark].nil?  
    params["routing-table"] = resource[:routing_table] if ! resource[:routing_table].nil?  
    params["connection-type"] = resource[:connection_type] if ! resource[:connection_type].nil?  
    params["connection-state"] = resource[:connection_state] if ! resource[:connection_state].nil?  
    params["connection-nat-state"] = resource[:connection_nat_state] if ! resource[:connection_nat_state].nil?
    # Advanced
    params["src-address-list"] = resource[:src_address_list] if ! resource[:src_address_list].nil?
    params["dst-address-list"] = resource[:dst_address_list] if ! resource[:dst_address_list].nil?
    params["layer7-protocol"] = resource[:layer7_protocol] if ! resource[:layer7_protocol].nil?
    params["content"] = resource[:content] if ! resource[:content].nil?
    params["connection-bytes"] = resource[:connection_bytes] if ! resource[:connection_bytes].nil?
    params["connection-rate"] = resource[:connection_rate] if ! resource[:connection_rate].nil?
    params["per-connection-classifier"] = resource[:per_connection_classifier] if ! resource[:per_connection_classifier].nil?
    params["src-mac-address"] = resource[:src_mac_address] if ! resource[:src_mac_address].nil?
    params["in-bridge-port"] = resource[:in_bridge_port] if ! resource[:in_bridge_port].nil?
    params["out-bridge-port"] = resource[:out_bridge_port] if ! resource[:out_bridge_port].nil?
    params["in-bridge-port-list"] = resource[:in_bridge_port_list] if ! resource[:in_bridge_port_list].nil?
    params["out-bridge-port-list"] = resource[:out_bridge_port_list] if ! resource[:out_bridge_port_list].nil?
    params["ipsec-policy"] = resource[:ipsec_policy] if ! resource[:ipsec_policy].nil?
    params["tls-host"] = resource[:tls_host] if ! resource[:tls_host].nil?  
    params["ingress-priority"] = resource[:ingress_priority] if ! resource[:ingress_priority].nil?
    params["priority"] = resource[:priority] if ! resource[:priority].nil?
    params["dscp"] = resource[:dscp] if ! resource[:dscp].nil?
    params["tcp-mss"] = resource[:tcp_mss] if ! resource[:tcp_mss].nil?
    params["packet-size"] = resource[:packet_size] if ! resource[:packet_size].nil?
    params["random"] = resource[:random] if ! resource[:random].nil?
    params["tcp-flags"] = resource[:tcp_flags] if ! resource[:tcp_flags].nil?  
    params["ipv4-options"] = resource[:ipv4_options] if ! resource[:ipv4_options].nil?
    params["ttl"] = resource[:ttl] if ! resource[:ttl].nil?
    # Extra
    params["connection-limit"] = resource[:connection_limit] if ! resource[:connection_limit].nil?
    params["limit"] = resource[:limit] if ! resource[:limit].nil?
    params["dst-limit"] = resource[:dst_limit] if ! resource[:dst_limit].nil?
    params["nth"] = resource[:nth] if ! resource[:nth].nil?
    params["time"] = resource[:time] if ! resource[:time].nil?
    params["src-address-type"] = resource[:src_address_type] if ! resource[:src_address_type].nil?
    params["dst-address-type"] = resource[:dst_address_type] if ! resource[:dst_address_type].nil?
    params["psd"] = resource[:psd] if ! resource[:psd].nil?
    params["hotspot"] = resource[:hotspot] if ! resource[:hotspot].nil?
    params["fragment"] = resource[:fragment] if ! resource[:fragment].nil?  
    # Action
    params["action"] = resource[:action] if ! resource[:action].nil?   
    params["log"] = resource[:log] if ! resource[:log].nil?
    params["log-prefix"] = resource[:log_prefix] if ! resource[:log_prefix].nil?
    params["jump-target"] = resource[:jump_target] if ! resource[:jump_target].nil?
    params["address-list"] = resource[:address_list] if ! resource[:address_list].nil?
    params["address-list-timeout"] = resource[:address_list_timeout] if ! resource[:address_list_timeout].nil?
    params["reject-with"] = resource[:reject_with] if ! resource[:reject_with].nil?
    params["to-addresses"] = resource[:to_addresses] if ! resource[:to_addresses].nil?
    params["to-ports"] = resource[:to_ports] if ! resource[:to_ports].nil?
    params["new-connection-mark"] = resource[:new_connection_mark] if ! resource[:new_connection_mark].nil?
    params["new-dscp"] = resource[:new_dscp] if ! resource[:new_dscp].nil?
    params["new-mss"] = resource[:new_mss] if ! resource[:new_mss].nil?
    params["new-packet-mark"] = resource[:new_packet_mark] if ! resource[:new_packet_mark].nil?
    params["new-priority"] = resource[:new_priority] if ! resource[:new_priority].nil?      
    params["new-routing-mark"] = resource[:new_routing_mark] if ! resource[:new_routing_mark].nil?
    params["new-ttl"] = resource[:new_ttl] if ! resource[:new_ttl].nil?
    params["route-dst"] = resource[:route_dst] if ! resource[:route_dst].nil?
    params["sniff-id"] = resource[:sniff_id] if ! resource[:sniff_id].nil?
    params["sniff-target"] = resource[:sniff_target] if ! resource[:sniff_target].nil?
    params["sniff-target-port"] = resource[:sniff_target_port] if ! resource[:sniff_target_port].nil?
      
    lookup = { "comment" => resource[:name] }
    
    Puppet.debug("Rule: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/firewall/#{table}", params, lookup)
      
    if !resource[:chain_order].nil?
      if @property_flush.empty?
        id_list = Puppet::Provider::Mikrotik_Api::lookup_id("/ip/firewall/#{table}", lookup)
        id_list.each do |id|
          chain_order = self.class.getChainOrder(id, resource[:chain], table_rules)
          if resource[:chain_order].to_i != chain_order
            self.class.moveRule(id, table, resource[:chain], chain_order, resource[:chain_order].to_i, table_rules)
          end
        end
      end
    end
  end
    
  def self.getChainOrder(lookup_id, lookup_chain, table_rules)    
    ids = getChainIds(lookup_chain, table_rules)
    
    chain_order = 1
    ids.each do |id|
      if id == lookup_id
         return chain_order
      end        
     
      chain_order = chain_order + 1
    end
  end
  
  def self.getChainIds(lookup_chain, table_rules)
    ids = table_rules.collect do |rule|
      if rule['chain'] == lookup_chain
        rule['.id']
      end
    end
    
    ids.compact
  end
    
  def self.moveRule(rule_id, table, lookup_chain, old_chain_order, new_chain_order, table_rules)
    Puppet.debug("Moving rule #{rule_id} from position #{old_chain_order} to position #{new_chain_order} in chain #{lookup_chain} on table #{table}.")
    
    if new_chain_order == old_chain_order
      return
    end
  
    if new_chain_order > old_chain_order
      lookup_order = new_chain_order + 1
    else
      lookup_order = new_chain_order
    end
  
    destination = nil
    chain_pos = 0
  
    table_rules.each do |rule|
      if rule['chain'] == lookup_chain
        chain_pos = chain_pos + 1         
      end
      
      if chain_pos == new_chain_order
        destination = rule['.id']  
      end
      
      if chain_pos == lookup_order
        destination = rule['.id']   
        break
      end
    end
  
    if rule_id == destination
      return
    end
  
    move_params = {}
    move_params["numbers"] = rule_id
    move_params["destination"] = destination if destination != nil
    result = Puppet::Provider::Mikrotik_Api::move("/ip/firewall/#{table}", move_params)
  end
end

File: /lib\puppet\provider\mikrotik_graph_interface\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_graph_interface).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/tool/graphing/interface")
    instances = interfaces.collect { |interface| toolGraphInterface(interface) }    
    instances
  end
  
  def self.toolGraphInterface(data)
      new(
        :ensure        => :present,
        :name          => data['interface'],
        :allow         => data['allow-address'],
        :store_on_disk => data['store-on-disk']
      )
  end

  def flush
    Puppet.debug("Flushing Tool Graph Interface #{resource[:name]}")
      
    params = {}
    params["interface"] = resource[:name]
    params["allow-address"] = resource[:allow] if ! resource[:allow].nil?
    params["store-on-disk"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:store_on_disk]) if ! resource[:store_on_disk].nil?

    lookup = {}
    lookup["interface"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/tool/graphing/interface", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_graph_queue\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_graph_queue).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/tool/graphing/queue")
    instances = interfaces.collect { |interface| toolGraphQueue(interface) }    
    instances
  end
  
  def self.toolGraphQueue(data)
      new(
        :ensure        => :present,
        :name          => data['simple-queue'],
        :allow         => data['allow-address'],
        :store_on_disk => data['store-on-disk'],
        :allow_target  => data['allow-target']
      )
  end

  def flush
    Puppet.debug("Flushing Tool Graph Queue #{resource[:name]}")
      
    params = {}
    params["simple-queue"] = resource[:name]
    params["allow-address"] = resource[:allow] if ! resource[:allow].nil?
    params["store-on-disk"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:store_on_disk]) if ! resource[:store_on_disk].nil?
    params["allow-target"] = resource[:allow_target] if ! resource[:allow_target].nil?

    lookup = {}
    lookup["simple-queue"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/tool/graphing/queue", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_graph_resource\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_graph_resource).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    resources = Puppet::Provider::Mikrotik_Api::get_all("/tool/graphing/resource")
    instances = resources.collect { |resource| toolGraphResource(resource) }    
    instances
  end
  
  def self.toolGraphResource(data)
      new(
        :ensure        => :present,
        :name          => 'resource',
        :allow         => data['allow-address'],
        :store_on_disk => data['store-on-disk']
      )
  end

  def flush
    Puppet.debug("Flushing Tool Graph Resource #{resource[:name]}")
      
    params = {}
    params["allow-address"] = resource[:allow] if ! resource[:allow].nil?
    params["store-on-disk"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:store_on_disk]) if ! resource[:store_on_disk].nil?

    lookup = {}
    lookup["allow-address"] = @original_values[:allow]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/tool/graphing/resource", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_interface_bgp_vpls\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_bgp_vpls).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/interface/vpls/bgp-vpls")
    instances = interfaces.collect { |interface| interface(interface) }    
    instances
  end
  
  def self.interface(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure               => :present,
      :state                => state,
      :name                 => data['name'],
      :route_distinguisher  => data['route-distinguisher'],
      :import_route_targets => data['import-route-targets'].split(','),
      :export_route_targets => data['export-route-targets'].split(','),
      :site_id              => data['site-id'],
      :bridge               => data['bridge'],
      :bridge_cost          => data['bridge-cost'],
      :bridge_horizon       => data['bridge-horizon'],
      :control_word         => data['control-word'],
      :pw_mtu               => data['pw-mtu'],
      :pw_type              => data['pw-type']
    )
  end

  def flush
    Puppet.debug("Flushing BGP VPLS Interface #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["name"] = resource[:name]
    params["route-distinguisher"] = resource[:route_distinguisher] if ! resource[:route_distinguisher].nil?
    params["import-route-targets"] = resource[:import_route_targets].join(',') if ! resource[:import_route_targets].nil?
    params["export-route-targets"] = resource[:export_route_targets].join(',') if ! resource[:export_route_targets].nil?
    params["site-id"] = resource[:site_id] if ! resource[:site_id].nil?
    params["bridge"] = resource[:bridge] if ! resource[:bridge].nil?
    params["bridge-cost"] = resource[:bridge_cost] if ! resource[:bridge_cost].nil?
    params["bridge-horizon"] = resource[:bridge_horizon] if ! resource[:bridge_horizon].nil?
    params["control-word"] = resource[:control_word] if ! resource[:control_word].nil?
    params["pw-mtu"] = resource[:pw_mtu] if ! resource[:pw_mtu].nil?
    params["pw-type"] = resource[:pw_type] if ! resource[:pw_type].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/vpls/bgp-vpls", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_bond\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_bond).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/interface/bonding")
    instances = interfaces.collect { |interface| interface(interface) }    
    instances
  end
  
  def self.interface(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure               => :present,
      :state                => state,
      :name                 => data['name'],
      :mtu                  => data['mtu'],
      :arp                  => data['arp'],
      :arp_timeout          => data['arp-timeout'],
      :slaves               => data['slaves'].split(','),
      :mode                 => data['mode'],
      :link_monitoring      => data['link-monitoring'],
      :transmit_hash_policy => data['transmit-hash-policy'],
      :primary              => data['primary']
    )
  end

  def flush
    Puppet.debug("Flushing Bonded Interface #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["name"] = resource[:name]
    params["mtu"] = resource[:mtu] if ! resource[:mtu].nil?
    params["arp"] = resource[:arp] if ! resource[:arp].nil?
    params["arp-timeout"] = resource[:arp_timeout] if ! resource[:arp_timeout].nil?
    params["slaves"] = resource[:slaves].join(',') if ! resource[:slaves].nil?
    params["mode"] = resource[:mode] if ! resource[:mode].nil?
    params["link-monitoring"] = resource[:link_monitoring] if ! resource[:link_monitoring].nil?
    params["transmit-hash-policy"] = resource[:transmit_hash_policy] if ! resource[:transmit_hash_policy].nil?
    params["primary"] = resource[:primary] if ! resource[:primary].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/bonding", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_bridge\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_bridge).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/interface/bridge")
    instances = interfaces.collect { |interface| interface(interface) }    
    instances
  end
  
  def self.interface(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure            => :present,
      :state             => state,
      :name              => data['name'],
      :mtu               => data['mtu'],
      :arp               => data['arp'],
      :arp_timeout       => data['arp-timeout'],
      :admin_mac         => data['admin-mac'],
      :igmp_snooping     => (data['igmp-snooping'].nil? ? :false : data['igmp-snooping']),
      :dhcp_snooping     => (data['dhcp-snooping'].nil? ? :false : data['dhcp-snooping']),
      :fast_forward      => (data['fast-forward'].nil? ? :false : data['fast-forward']),
      :protocol_mode     => data['protocol-mode'],
      :priority          => data['priority'],
      :region_name       => data['region-name'],
      :region_revision   => data['region-revision'],
      :vlan_filtering    => (data['vlan-filtering'].nil? ? :false : data['vlan-filtering']),
      :pvid              => data['pvid'],
      :ether_type        => data['ether-type'],
      :frame_types       => data['frame-types'],
      :ingress_filtering => (data['ingress-filtering'].nil? ? :false : data['ingress-filtering']),
      :comment           => data['comment']
    )
  end

  def flush
    Puppet.debug("Flushing Bridge #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["name"] = resource[:name]
    params["mtu"] = resource[:mtu] if ! resource[:mtu].nil?
    params["arp"] = resource[:arp] if ! resource[:arp].nil?
    params["arp-timeout"] = resource[:arp_timeout] if ! resource[:arp_timeout].nil?
    params["admin-mac"] = resource[:admin_mac] if ! resource[:admin_mac].nil?    
    params["igmp-snooping"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:igmp_snooping]) if ! resource[:igmp_snooping].nil?
    params["dhcp-snooping"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:dhcp_snooping]) if ! resource[:dhcp_snooping].nil?
    params["fast-forward"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:fast_forward]) if ! resource[:fast_forward].nil?
    params["protocol-mode"] = resource[:protocol_mode] if ! resource[:protocol_mode].nil?
    params["priority"] = resource[:priority] if ! resource[:priority].nil?
    params["region-name"] = resource[:region_name] if ! resource[:region_name].nil?      
    params["region-revision"] = resource[:region_revision] if ! resource[:region_revision].nil?
    params["vlan-filtering"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:vlan_filtering]) if ! resource[:vlan_filtering].nil?
    params["pvid"] = resource[:pvid] if ! resource[:pvid].nil?      
    params["ether-type"] = resource[:ether_type] if ! resource[:ether_type].nil?
    params["frame-types"] = resource[:frame_types] if ! resource[:frame_types].nil?
    params["ingress-filtering"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:ingress_filtering]) if ! resource[:ingress_filtering].nil?
    params["comment"] = resource[:comment] if ! resource[:comment].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/bridge", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_bridge_msti\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_bridge_msti).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    msti_list = Puppet::Provider::Mikrotik_Api::get_all("/interface/bridge/msti")
    instances = msti_list.collect { |msti| msti(msti) }    
    instances
  end
  
  def self.msti(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure       => :present,
      :state        => state,
      :name         => data['comment'],
      :bridge       => data['bridge'],
      :identifier   => data['identifier'],
      :priority     => data['priority'],
      :vlan_mapping => data['vlan-mapping'].split(',')
    )
  end

  def flush
    Puppet.debug("Flushing Bridge MSTI #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["comment"]      = resource[:name]
    params["bridge"]       = resource[:bridge]      
    params["identifier"]   = resource[:identifier]
    params["priority"]     = resource[:priority] if ! resource[:priority].nil?
    params["vlan-mapping"] = resource[:vlan_mapping].join(',') if ! resource[:vlan_mapping].nil?    

    lookup = {}
    lookup["comment"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/bridge/msti", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_bridge_msti_port\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_bridge_msti_port).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    ports = Puppet::Provider::Mikrotik_Api::get_all("/interface/bridge/port/mst-override")
    instances = ports.collect { |port| override(port) unless port['dynamic'] == "yes" }    
    instances
  end
  
  def self.override(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end

    if data['comment'].nil?
      name = data['interface'] + " on " + data['identifier']
    else
      name = data['comment']
    end
        
    new(
      :ensure             => :present,
      :state              => state,
      :name               => name,
      :interface          => data['interface'],
      :identifier         => data['identifier'],
      :priority           => data['priority'],
      :internal_path_cost => data['internal-path-cost']
    )
  end

  def flush
    Puppet.debug("Flushing Bridge Port MST Override #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["comment"]             = resource[:name]
    params["interface"]           = resource[:interface]      
    params["identifier"]          = resource[:identifier]
    params["priority"]            = resource[:priority] if ! resource[:priority].nil?
    params["internal-path-cost"]  = resource[:internal_path_cost] if ! resource[:internal_path_cost].nil?

    lookup = {}
    lookup["comment"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/bridge/port/mst-override", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_interface_bridge_port\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_bridge_port).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/interface/bridge/port")
    instances = interfaces.collect { |interface| interface(interface) }    
    instances
  end
  
  def self.interface(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure             => :present,
      :state              => state,
      :name               => data['interface'],
      :bridge             => data['bridge'],
      :horizon            => data['horizon'],   
      :priority           => data['priority'],
      :path_cost          => data['path-cost'],  
      :internal_path_cost => data['internal-path-cost'],  
      :pvid               => data['pvid'],     
      :frame_types        => data['frame-types'],
      :ingress_filtering  => (data['ingress-filtering'].nil? ? :false : data['ingress-filtering']),
      :tag_stacking       => (data['tag-stacking'].nil? ? :false : data['tag-stacking']),
      :comment            => data['comment']
    )
  end

  def flush
    Puppet.debug("Flushing Bridge Port #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["interface"] = resource[:name]
    params["bridge"] = resource[:bridge]
    params["horizon"] = resource[:horizon] if ! resource[:horizon].nil?
    params["priority"] = resource[:priority] if ! resource[:priority].nil?
    params["path-cost"] = resource[:path_cost] if ! resource[:path_cost].nil?
    params["internal-path-cost"] = resource[:internal_path_cost] if ! resource[:internal_path_cost].nil?
    params["pvid"] = resource[:pvid] if ! resource[:pvid].nil?      
    params["frame-types"] = resource[:frame_types] if ! resource[:frame_types].nil?
    params["ingress-filtering"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:ingress_filtering]) if ! resource[:ingress_filtering].nil?
    params["tag-stacking"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:tag_stacking]) if ! resource[:tag_stacking].nil?
    params["comment"] = resource[:comment] if ! resource[:comment].nil?

    lookup = {}
    lookup["interface"] = resource[:name]
    # ? lookup["bridge"] = resource[:bridge]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/bridge/port", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_bridge_settings\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_bridge_settings).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
      
    bridge_settings = Puppet::Provider::Mikrotik_Api::get_all("/interface/bridge/settings")
    bridge_settings.each do |data|
      object = bridgeSettings(data)
      if object != nil
        instances << object
      end
    end

    instances
  end
  
  def self.bridgeSettings(data)
    Puppet.debug("Bridge Settings: #{data}")  # TODO: REMOVE !
    
    new(
      :name                      => 'bridge',
      :allow_fast_path           => data['allow-fast-path'],
      :use_ip_firewall           => data['use-ip-firewall'],
      :use_ip_firewall_for_pppoe => data['use-ip-firewall-for-pppoe'],
      :use_ip_firewall_for_vlan  => data['use-ip-firewall-for-vlan']
    )
  end

  def flush
    Puppet.debug("Flushing Bridge Settings")
    
    if (@property_hash[:name] != 'bridge') 
      raise "There is only one set of Bridge settings. Title (name) should be -bridge-"
    end
    
    update = {}
    update["allow-fast-path"] = resource[:allow_fast_path] if ! resource[:allow_fast_path].nil?
    update["use-ip-firewall"] = resource[:use_ip_firewall] if ! resource[:use_ip_firewall].nil?
    update["use-ip-firewall-for-pppoe"] = resource[:use_ip_firewall_for_pppoe] if ! resource[:use_ip_firewall_for_pppoe].nil?
    update["use-ip-firewall-for-vlan"] = resource[:use_ip_firewall_for_vlan] if ! resource[:use_ip_firewall_for_vlan].nil?
    
    result = Puppet::Provider::Mikrotik_Api::set("/interface/bridge/settings", update)
  end
end

File: /lib\puppet\provider\mikrotik_interface_bridge_vlan\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_bridge_vlan).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    vlans = Puppet::Provider::Mikrotik_Api::get_all("/interface/bridge/vlan")
    instances = vlans.collect { |vlan| vlan(vlan) unless vlan['dynamic'] == "yes" }    
    instances
  end
  
  def self.vlan(data)    
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end

    if data['comment'].nil?
      name = data['vlan-ids'] + " on " + data['bridge']
    else
      name = data['comment']
    end

    new(
      :ensure    => :present,
      :state     => state,
      :name      => name,
      :bridge    => data['bridge'],
      :vlan_ids  => data['vlan-ids'].split(','),
      :tagged    => data['tagged'].split(','),
      :untagged  => data['untagged'].split(',')
    )
  end

  def flush
    Puppet.debug("Flushing Bridge VLAN #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["comment"]  = resource[:name]
    params["bridge"]   = resource[:bridge]      
    params["vlan-ids"] = resource[:vlan_ids].join(',') if ! resource[:vlan_ids].nil?    
    params["tagged"]   = resource[:tagged].join(',')   if ! resource[:tagged].nil?    
    params["untagged"] = resource[:untagged].join(',') if ! resource[:untagged].nil?    

    lookup = {}
    lookup["comment"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/bridge/vlan", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_eoip\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_eoip).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/interface/eoip")
    instances = interfaces.collect { |interface| interface(interface) }    
    instances
  end
  
  def self.interface(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure          => :present,
      :state           => state,
      :name            => data['name'],
      :mtu             => data['mtu'],
      :admin_mac       => data['admin-mac'],
      :arp             => data['arp'],
      :arp_timeout     => data['arp-timeout'],
      :local_address   => data['local-address'],
      :remote_address  => data['remote-address'],
      :tunnel_id       => data['tunnel-id'],
      :ipsec_secret    => data['ipsec-secret'],
      :keepalive       => data['keepalive'],
      :dscp            => data['dscp'],
      :dont_fragment   => data['dont-fragment'],
      :clamp_tcp_mss   => data['clamp-tcp-mss'],
      :allow_fast_path => data['allow-fast-path']
    )
  end

  def flush
    Puppet.debug("Flushing EoIP Interface #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["name"] = resource[:name]
    params["mtu"] = resource[:mtu] if ! resource[:mtu].nil?
    params["admin-mac"] = resource[:admin_mac] if ! resource[:admin_mac].nil?
    params["arp"] = resource[:arp] if ! resource[:arp].nil?
    params["arp-timeout"] = resource[:arp_timeout] if ! resource[:arp_timeout].nil?
    params["local-address"] = resource[:local_address] if ! resource[:local_address].nil?
    params["remote-address"] = resource[:remote_address] if ! resource[:remote_address].nil?
    params["tunnel-id"] = resource[:tunnel_id] if ! resource[:tunnel_id].nil?      
    params["ipsec-secret"] = resource[:ipsec_secret] if ! resource[:ipsec_secret].nil?
    params["keepalive"] = resource[:keepalive] if ! resource[:keepalive].nil?
    params["dscp"] = resource[:dscp] if ! resource[:dscp].nil?
    params["dont-fragment"] = resource[:dont_fragment] if ! resource[:dont_fragment].nil?
    params["clamp-tcp-mss"] = resource[:clamp_tcp_mss] if ! resource[:clamp_tcp_mss].nil?
    params["allow-fast-path"] = resource[:allow_fast_path] if ! resource[:allow_fast_path].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/eoip", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_ethernet\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_ethernet).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/interface/ethernet")
    instances = interfaces.collect { |interface| interface(interface) }    
    instances
  end
  
  def self.interface(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure           => :present,
      :state            => state,
      :name             => data['default-name'],
      :alias            => data['name'],
      :mtu              => data['mtu'],
      :arp              => data['arp'],
      :arp_timeout      => data['arp_timeout'],
      :auto_negotiation => data['auto_negotiation'],
      :advertise        => data['advertise'].split(',')
    )
  end

  def flush
    Puppet.debug("Flushing Ethernet Interface #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
    #  params["disabled"] = 'yes'
      Puppet.debug("DISABLE Ethernet Interface #{resource[:name]}")
    elsif @property_hash[:state] == :enabled
    #  params["disabled"] = 'no'
      Puppet.debug("ENABLE Ethernet Interface #{resource[:name]}")
    end
    
    params["name"] = resource[:alias] if ! resource[:alias].nil?
    params["mtu"] = resource[:mtu] if ! resource[:mtu].nil?
    params["arp"] = resource[:arp] if ! resource[:arp].nil?
    params["arp-timeout"] = resource[:arp_timeout] if ! resource[:arp_timeout].nil?
    params["auto-negotiation"] = resource[:auto_negotiation] if ! resource[:auto_negotiation].nil?
    params["advertise"] = resource[:advertise].join(',') if ! resource[:advertise].nil?

    lookup = {}
    lookup["default-name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/ethernet", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_gre\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_gre).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/interface/gre")
    instances = interfaces.collect { |interface| interface(interface) }    
    instances
  end
  
  def self.interface(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure          => :present,
      :state           => state,
      :name            => data['name'],
      :mtu             => data['mtu'],
      :local_address   => data['local-address'],
      :remote_address  => data['remote-address'],
      :ipsec_secret    => data['ipsec-secret'],
      :keepalive       => data['keepalive'],
      :dscp            => data['dscp'],
      :dont_fragment   => data['dont-fragment'],
      :clamp_tcp_mss   => data['clamp-tcp-mss'],
      :allow_fast_path => data['allow-fast-path']
    )
  end

  def flush
    Puppet.debug("Flushing GRE Interface #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["name"] = resource[:name]
    params["mtu"] = resource[:mtu] if ! resource[:mtu].nil?
    params["local-address"] = resource[:local_address] if ! resource[:local_address].nil?
    params["remote-address"] = resource[:remote_address] if ! resource[:remote_address].nil?
    params["ipsec-secret"] = resource[:ipsec_secret] if ! resource[:ipsec_secret].nil?
    params["keepalive"] = resource[:keepalive] if ! resource[:keepalive].nil?
    params["dscp"] = resource[:dscp] if ! resource[:dscp].nil?
    params["dont-fragment"] = resource[:dont_fragment] if ! resource[:dont_fragment].nil?
    params["clamp-tcp-mss"] = resource[:clamp_tcp_mss] if ! resource[:clamp_tcp_mss].nil?
    params["allow-fast-path"] = resource[:allow_fast_path] if ! resource[:allow_fast_path].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/gre", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_list\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_list).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interface_members = {}
    
    members = get_all("/interface/list/member")
    members.each do |member|
      list_name = member["list"]
      unless interface_members.key?(list_name)
        interface_members[list_name] = []
      end
      interface_members[list_name] << member["interface"]
    end
    
    lists = Puppet::Provider::Mikrotik_Api::get_all("/interface/list")
    instances = lists.collect do |list| 
      list_name = list['name']
      interface_members[list_name] = [] unless interface_members.key?(list_name)

      interface_list(list_name, interface_members[list_name],list)
    end
    
    instances
  end
  
  def self.interface_list(name, members,details)
    new(
      :ensure  => :present,
      :name    => name,
      :members => members,
      :include => details['include'].split(','),
      :exclude => details['exclude'].split(',')
    )
  end
  
  def flush
    Puppet.debug("Flushing Interface List #{resource[:name]}")    
      
    list_params = {}
    list_params["name"] = resource[:name]
    list_params["include"] = resource[:include].join(',') if !resource[:include].nil?
    list_params["exclude"] = resource[:exclude].join(',') if !resource[:exclude].nil?

    members_params = {}
    members_params["list"] = resource[:name]
    
    list_flush("/interface/list", list_params, :members, "/interface/list/member", members_params, :interface)
  end
  
  def list_flush(list_path, list_params, members_param_name, members_path, members_params, member_param_name)  
    Puppet.debug("list_flush(#{list_path}, #{list_params.inspect}, #{members_param_name}, #{members_path}, #{members_params.inspect}, #{member_param_name})")

    # CREATE
    if @property_flush[:ensure] == :present
      Puppet.debug("Creating #{list_path}")
  
      # create list
      result = Puppet::Provider::Mikrotik_Api::add(list_path, list_params)
      
      # create members
      if resource[:manage_members]
        resource[members_param_name].each do |item|
          Puppet.debug("Create member #{item} in #{members_path}")
      
          params2 = members_params.merge({member_param_name => item})
          result = Puppet::Provider::Mikrotik_Api::add(members_path, params2)
        end
      end
    end
  
    # DESTROY
    if @property_flush[:ensure] == :absent
      Puppet.debug("Deleting #{list_path}")

      # remove members (and save the orphans)
      # TODO: deleting an interface also creates an orphan      
      id_list = Puppet::Provider::Mikrotik_Api::lookup_id(members_path, members_params)
      id_list.each do |id|
        id_lookup = { ".id" => id } 
        result = Puppet::Provider::Mikrotik_Api::remove(members_path, id_lookup)
      end
      
      # remove list
      id_list = Puppet::Provider::Mikrotik_Api::lookup_id(list_path, list_params)
      id_list.each do |id|
        id_lookup = { ".id" => id } 
        result = Puppet::Provider::Mikrotik_Api::remove(list_path, id_lookup)
      end
    end
    
    # UPDATE
    if @property_flush.empty?
      Puppet.debug("Updating #{members_path}")
      
      if resource[:manage_members]
        # Create members
        (@property_hash[members_param_name] - @original_values[members_param_name]).each do |item|
          Puppet.debug("Create member #{item} in #{members_path}")
      
          params2 = members_params.merge({member_param_name => item})
          result = Puppet::Provider::Mikrotik_Api::add(members_path, params2)
        end
        
        # Delete members
        (@original_values[members_param_name] - @property_hash[members_param_name]).each do |item|
          Puppet.debug("Delete member #{item} in #{members_path}")

          lookup2 = members_params.merge({member_param_name => item})
          id_list = Puppet::Provider::Mikrotik_Api::lookup_id(members_path, lookup2)
          id_list.each do |id|
            id_lookup = { ".id" => id } 
            result = Puppet::Provider::Mikrotik_Api::remove(members_path, id_lookup)        
          end
        end
      end
    end    
  end 
end

File: /lib\puppet\provider\mikrotik_interface_ppp\mikrotik_api.rb
require_relative '../mikrotik_api'
Puppet::Type.type(:mikrotik_interface_ppp).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  mk_resource_methods
  def self.instances    
    instances = []
    ovpn = Puppet::Provider::Mikrotik_Api::get_all("/interface/ovpn-client")
    ovpn.each { |client|
      instances << pppClient('ovpn_client', client)
    }
    instances
  end

  def self.pppClient(type,data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    authentication = data['authentication'] || data['auth'] 
    cert = data['certificate'] == 'none' ? nil : data['certificate']

    new(
      :ensure            => :present,
      :state             => state,
      :name              => data['name'],
      :ppp_type          => type,
      :max_mtu           => data['max-mtu'],
      :mac_address       => data['mac-address'],
      :connect_to        => data['connect-to'],
      :port              => data['port'],
      :mode              => data['mode'],
      :user              => data['user'],
      :password          => data['password'],
      :profile           => data['profile'],
      :certificate       => cert,
      :add_default_route => data['add_default_route'],
      :authentication    => authentication,
      :cipher            => data['cipher']
    )
  end


  def flush
    Puppet.debug("Flushing PPP Client #{resource[:name]}")
    params = {}
    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end

    attributes = %i{name max_mtu mac_address connect_to port mode user password profile certificate cipher add_default_route}
    attributes.each do |attrib|
      param_name = attrib.to_s.tr('_','-')
      params[param_name] = resource[attrib] unless resource[attrib].nil?  
    end

    auth_key = resource[:ppp_type] == 'ovpn_client' ? 'auth' : 'authentication'
    params[auth_key] = resource[:authentication] if ! resource[:authentication].nil?

    interface_type = resource[:ppp_type].to_s.tr('_','-')

    lookup = {}
    lookup["name"] = resource[:name]
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")
    simple_flush("/interface/#{interface_type}", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_pppoe_server\mikrotik_api.rb
require_relative '../mikrotik_api'
Puppet::Type.type(:mikrotik_interface_pppoe_server).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  mk_resource_methods
  def self.instances    
    instances = []
    servers = Puppet::Provider::Mikrotik_Api::get_all("/interface/pppoe-server/server")
    servers.each { |server|
      instances << pppoeServer(server)
    }
    instances
  end

  def self.pppoeServer(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end

    new(
      :ensure               => :present,
      :state                => state,
      :name                 => data['service-name'],
      :interface            => data['interface'],
      :max_mtu              => data['max-mtu'],
      :max_mru              => data['max-mru'],
      :mrru                 => data['mrru'],
      :authentication       => data['authentication'].split(','),
      :keepalive            => data['keepalive-timeout'],
      :one_session_per_host => data['one-session-per-host'],
      :max_sessions         => data['max-sessions'],
      :pado_delay           => data['pado-delay'],
      :default_profile      => data['default-profile']
    )
  end

  def flush
    Puppet.debug("Flushing PPPoE Server #{resource[:name]}")
    params = {}
    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["service-name"] = resource[:name]
    params["interface"] = resource[:interface]
      
    params["max-mtu"] = resource[:max_mtu] if !resource[:max_mtu].nil?
    params["max-mru"] = resource[:max_mru] if !resource[:max_mru].nil?
    params["mrru"] = resource[:mrru] if !resource[:mrru].nil?

    params["authentication"] = resource[:authentication].join(',') if !resource[:authentication].nil?
      
    params["keepalive-timeout"] = resource[:keepalive] if !resource[:keepalive].nil?
    params["one-session-per-host"] = resource[:one_session_per_host] if !resource[:one_session_per_host].nil?
    params["max-sessions"] = resource[:max_sessions] if !resource[:max_sessions].nil?
    params["pado-delay"] = resource[:pado_delay] if !resource[:pado_delay].nil?
    params["default-profile"] = resource[:default_profile] if !resource[:default_profile].nil?

    lookup = {"service-name" => resource[:name]}
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")
    simple_flush("/interface/pppoe-server/server", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_interface_ppp_server_binding\mikrotik_api.rb
require_relative '../mikrotik_api'
Puppet::Type.type(:mikrotik_interface_ppp_server_binding).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  mk_resource_methods
  def self.instances    
    instances = []
    ovpn = Puppet::Provider::Mikrotik_Api::get_all("/interface/ovpn-server")
    ovpn.each { |client|
      instances << pppServerBinding('ovpn', client)
    }
    instances
  end

  def self.pppServerBinding(type,data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end

    new(
      :ensure   => :present,
      :state    => state,
      :name     => data['name'],
      :ppp_type => type,
      :user     => data['user'],
      :comment  => data['comment'],
    )
  end


  def flush
    Puppet.debug("Flushing PPP Server Binding #{resource[:name]}")
    params = {}
    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end

    attributes = [:name, :user, :comment]
    attributes.each do |attrib|
      params[attrib] = resource[attrib] unless resource[attrib].nil?  
    end

    interface_type = "#{resource[:ppp_type]}-server"

    lookup = {"name" => resource[:name]}
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")
    simple_flush("/interface/#{interface_type}", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_te\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_te).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/interface/traffic-eng")
    instances = interfaces.collect { |interface| teInterface(interface) }    
    instances
  end

  def self.teInterface(data)    
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :name                           => data['name'],
      :ensure                         => :present,
      :state                          => state,
      :mtu                            => data['mtu'],
      :from_address                   => data['from-address'],
      :to_address                     => data['to-address'],
      :bandwidth                      => data['bandwidth'],
      :primary_path                   => data['primary-path'],
      :secondary_paths                => data['secondary-paths'].split(','),
      :record_route                   => (data['record-route'].nil? ? :false : data['record-route']),
      :bandwidth_limit                => data['bandwidth-limit'],
      :auto_bandwidth_range           => data['auto-bandwidth-range'],
      :auto_bandwidth_reserve         => data['auto-bandwidth-reserve'],
      :auto_bandwidth_avg_interval    => data['auto-bandwidth-avg-interval'],
      :auto_bandwidth_update_interval => data['auto-bandwidth-update-interval'],
      :primary_retry_interval         => data['primary-retry-interval'],
      :setup_priority                 => data['setup-priority'],
      :holding_priority               => data['holding-priority'],
      :reoptimize_interval            => data['reoptimize-interval']
    )
  end

  def flush 
    Puppet.debug("Flushing MPLS TE Interface #{resource[:name]}")

    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end

    params["name"] = resource[:name]
    params["mtu"] = resource[:mtu] if ! resource[:mtu].nil?  

    params["from-address"] = resource[:from_address] if ! resource[:from_address].nil?
    params["to-address"] = resource[:to_address] if ! resource[:to_address].nil?
    params["bandwidth"] = resource[:bandwidth] if ! resource[:bandwidth].nil?
    params["primary-path"] = resource[:primary_path] if ! resource[:primary_path].nil?
    params["secondary-paths"] = resource[:secondary_paths].join(',') if ! resource[:secondary_paths].nil?
    params["record-route"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:record_route]) if ! resource[:record_route].nil?     
    params["bandwidth-limit"] = resource[:bandwidth_limit] if ! resource[:bandwidth_limit].nil?
    params["auto-bandwidth-range"] = resource[:auto_bandwidth_range] if ! resource[:auto_bandwidth_range].nil?
    params["auto-bandwidth-reserve"] = resource[:auto_bandwidth_reserve] if ! resource[:auto_bandwidth_reserve].nil?
    params["auto-bandwidth-avg-interval"] = resource[:auto_bandwidth_avg_interval] if ! resource[:auto_bandwidth_avg_interval].nil?
    params["auto-bandwidth-update-interval"] = resource[:auto_bandwidth_update_interval] if ! resource[:auto_bandwidth_update_interval].nil?
    params["primary-retry-interval"] = resource[:primary_retry_interval] if ! resource[:primary_retry_interval].nil?
    params["setup-priority"] = resource[:setup_priority] if ! resource[:setup_priority].nil?
    params["holding-priority"] = resource[:holding_priority] if ! resource[:holding_priority].nil?
    params["reoptimize-interval"] = resource[:reoptimize_interval] if ! resource[:reoptimize_interval].nil?

    lookup = {}
    lookup["name"] = resource[:name]

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/traffic-eng", params, lookup)
  end
end

File: /lib\puppet\provider\mikrotik_interface_vlan\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_vlan).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/interface/vlan")
    instances = interfaces.collect { |interface| interface(interface) }    
    instances
  end
  
  def self.interface(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure          => :present,
      :state           => state,
      :name            => data['name'],
      :mtu             => data['mtu'],
      :arp             => data['arp'],
      :arp_timeout     => data['arp-timeout'],
      :vlan_id         => data['vlan-id'],
      :interface       => data['interface'],
      :use_service_tag => data['use-service-tag']
    )
  end

  def flush
    Puppet.debug("Flushing VLAN Interface #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["name"] = resource[:name]
    params["mtu"] = resource[:mtu] if ! resource[:mtu].nil?
    params["arp"] = resource[:arp] if ! resource[:arp].nil?
    params["arp-timeout"] = resource[:arp_timeout] if ! resource[:arp_timeout].nil?
    params["vlan-id"] = resource[:vlan_id] if ! resource[:vlan_id].nil?
    params["interface"] = resource[:interface] if ! resource[:interface].nil?
    params["use-service-tag"] = resource[:use_service_tag] if ! resource[:use_service_tag].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/vlan", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_interface_vrrp\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_interface_vrrp).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/interface/vrrp")
    instances = interfaces.collect { |interface| interface(interface) }    
    instances
  end
  
  def self.interface(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure          => :present,
      :state           => state,
      :name            => data['name'],
      :mtu             => data['mtu'],
      :arp             => data['arp'],
      :arp_timeout     => data['arp-timeout'],
      :interface       => data['interface'],
      :vrid            => data['vrid'],
      :priority        => data['priority'],
      :interval        => data['interval'],
      :preemption_mode => data['preemption-mode'],
      :authentication  => data['authentication'],
      :password        => data['password'],
      :version         => data['version'],
      :v3_protocol     => data['v3-protocol'],
      :on_master       => data['on-master'],
      :on_backup       => data['on-backup']
    )
  end

  def flush
    Puppet.debug("Flushing VRRP Interface #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["name"] = resource[:name]
    params["mtu"] = resource[:mtu] if ! resource[:mtu].nil?
    params["arp"] = resource[:arp] if ! resource[:arp].nil?
    params["arp-timeout"] = resource[:arp_timeout] if ! resource[:arp_timeout].nil?
    params["interface"] = resource[:interface] if ! resource[:interface].nil?
    params["vrid"] = resource[:vrid] if ! resource[:vrid].nil?
    params["priority"] = resource[:priority] if ! resource[:priority].nil?
    params["interval"] = resource[:interval] if ! resource[:interval].nil?
    params["preemption-mode"] = resource[:preemption_mode] if ! resource[:preemption_mode].nil?      
    params["authentication"] = resource[:authentication] if ! resource[:authentication].nil?
    params["password"] = resource[:password] if ! resource[:password].nil?
    params["version"] = resource[:version] if ! resource[:version].nil?
    params["v3-protocol"] = resource[:v3_protocol] if ! resource[:v3_protocol].nil?
    params["on-master"] = resource[:on_master] if ! resource[:on_master].nil?
    params["on-backup"] = resource[:on_backup] if ! resource[:on_backup].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/interface/vrrp", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_ipsec_group\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipsec_group).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik

  mk_resource_methods

  def self.instances
    groups = Puppet::Provider::Mikrotik_Api::get_all("/ip/ipsec/policy/group")
    instances = scripts.collect { |group| ipsecGroup(group) }
    instances
  end

  def self.ipsecGroup(data)
    new(
      :ensure   => :present,
      :name     => data['name'],
    )
  end

  def flush
    Puppet.info("Flushing Group #{resource[:name]}")

    params = { "name" => resource[:name] }
    lookup = { "name" => resource[:name] }

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/ipsec/policy/group", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_ipsec_identity\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipsec_identity).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik

  mk_resource_methods

  def self.instances
    instances = []

    identities = Puppet::Provider::Mikrotik_Api::get_all("/ip/ipsec/identity")
    identities.each do |identity|
      object = ipsecIdentity(identity)
      if object != nil
        instances << object
      end
    end

    instances
  end

  def self.ipsecIdentity(data)
    if data['comment'] != nil
      if data['disabled'] == "true"
        state = :disabled
      else
        state = :enabled
      end

      if data['eap-methods']
        eap_methods = data['eap-methods'].split(',').map {|mthd| mthd[4..-1] }
      end

      new(
        :ensure                => :present,
        :state                 => state,
        :name                  => data['comment'],
        :auth_method           => data['auth-method'],
        :certificate           => data['certificate'],
        :eap_methods           => eap_methods,
        :generate_policy       => data['generate-policy'],
        :key                   => data['key'],
        :match_by              => data['match-by'],
        :mode_config           => data['mode-config'],
        :my_id                 => data['my-id'],
        :notrack_chain         => data['notrack-chain'],
        :password              => data['password'],
        :policy_template_group => data['policy-template-group'] || 'default',
        :remote_certificate    => data['remote-certificate'],
        :remote_id             => data['remote-id'],
        :remote_key            => data['remote-key'],
        :secret                => data['secret'],
        :peer                  => data['peer'],
      )
    end
  end

  def flush
    Puppet.debug("Flushing IPSec Identity #{resource[:name]}")

    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end

    params["comment"] = resource[:name]
    params["auth-method"] = resource[:auth_method]
    params["certificate"] = resource[:certificate]
    params["eap-methods"] = resource[:eap_methods].map {|mthd| "eap-#{mthd}" }.join(',') unless resource[:eap_methods].nil?
    params["generate-policy"] = resource[:generate_policy]
    params['key'] = resource[:key]
    params['match-by'] = resource[:match_by]
    params["mode-config"] = resource[:mode_config]
    params["my-id"] = resource[:my_id]
    params['notrack-chain'] = resource[:notrack_chain]
    params['password'] = resource[:password]
    params['policy-template-group'] = resource[:policy_template_group]
    params['remote-certificate'] = resource[:remote_certificate]
    params['remote-id'] = resource[:remote_id]
    params['remote-key'] = resource[:remote_key]
    params['secret'] = resource[:secret]
    params['username'] = resource[:username]
    params['peer'] = resource[:peer]
    params.compact!

    lookup = { "comment" => resource[:name] }

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/ipsec/identity", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_ipsec_mode_config\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipsec_mode_config).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik

  mk_resource_methods

  def self.instances
    instances = []

    modes = Puppet::Provider::Mikrotik_Api::get_all("/ip/ipsec/mode-config")
    modes.each do |mode|
      object = ipsecModeConfig(mode)
      if object != nil
        instances << object
      end
    end

    instances
  end

  def self.ipsecModeConfig(data)
    new(
      :ensure                => :present,
      :name                  => data['name'],
      :comment               => data['comment'],
      :address_pool          => data['address-pool'],
      :address_prefix_length => data['address-prefix-length'],
      :split_include         => data['split-include'].nil? ? nil : data['split-include'].split(','),
      :static_dns            => data['static-dns'].nil? ? nil : data['static-dns'].split(','),
      :system_dns            => data['system-dns'],
    )
  end

  def flush
    Puppet.debug("Flushing IPSec Mode Config #{resource[:name]}")

    params = {
      "name"                  => resource[:name],
      "comment"               => resource[:comment],
      "address-pool"          => resource[:address_pool],
      "address-prefix-length" => resource[:address_prefix_length],
      "split-include"         => resource[:split_include].nil? ? nil : resource[:split_include].join(','),
      "static-dns"            => resource[:static_dns].nil? ? nil : resource[:static_dns].join(','),
      "system-dns"            => resource[:system_dns],
    }.compact

    lookup = { "name" => resource[:name] }

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/ipsec/mode-config", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_ipsec_peer\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipsec_peer).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik

  mk_resource_methods

  def self.instances
    instances = []

    peers = Puppet::Provider::Mikrotik_Api::get_all("/ip/ipsec/peer")
    peers.each do |peer|
      object = ipsecPeer(peer)
      if object != nil
        instances << object
      end
    end

    instances
  end

  def self.ipsecPeer(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end

    new(
      :ensure                => :present,
      :state                 => state,
      :name                  => data['name'],
      :comment               => data['comment'],
      :address               => data['address'],
      :exchange_mode         => data['exchange-mode'],
      :local_address         => data['local-address'],
      :passive               => data['passive'],
      :port                  => data['port'],
      :profile               => data['profile'],
      :send_initial_contact  => data['send-initial-contact'],
    )
  end

  def flush
    Puppet.debug("Flushing IPSec Peer #{resource[:name]}")

    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end

    params["name"] = resource[:name]
    params["comment"] = resource[:comment]
    params["address"] = resource[:address]
    params["exchange-mode"] = resource[:exchange_mode]
    params["local-address"] = resource[:local_address]
    params['passive'] = resource[:passive]
    params['port'] = resource[:port]
    params['send-initial-contact'] = resource[:send_initial_contact]
    params['profile'] = resource[:profile]
    params.compact!

    lookup = { "name" => resource[:name] }

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/ipsec/peer", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_ipsec_policy\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipsec_policy).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik

  mk_resource_methods

  def self.instances
    instances = []
    policies = Puppet::Provider::Mikrotik_Api::get_all("/ip/ipsec/policy")
    policies.each do |policy|
      object = ipsecPolicy(policy)
      if object != nil
        instances << object
      end
    end
    instances
  end

  def self.prefetch(resources)
    nodes = instances
    resources.keys.each do |name|
      if provider = nodes.find { |node| node.name == name }
        resources[name].provider = provider
      end
    end
  end

  def self.ipsecPolicy(data)
    if data['comment'] != nil
      if data['disabled'] == "true"
        state = :disabled
      else
        state = :enabled
      end

      new(
        :ensure               => :present,
        :state                => state,
        :name                 => data['comment'],
        :action               => data['action'],
        :dst_address          => data['dst-address'],
        :dst_port             => data['dst-port'],
        :group                => data['group'],
        :ipsec_protocols      => data['ipsec-protocols'],
        :level                => data['level'],
        :proposal             => data['proposal'],
        :protocol             => data['protocol'],
        :src_address          => data['src-address'],
        :src_port             => data['src-port'],
        :template             => data['template'],
        :tunnel               => data['tunnel'],
        :peer                 => data['peer'],
      )
    end
  end

  def flush
    Puppet.debug("Flushing IPSec Policy #{resource[:name]}")

    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end

    params["comment"] = resource[:name]
    params["action"] = resource[:action]
    params["dst-address"] = resource[:dst_address]
    params["dst-port"] = resource[:dst_port]
    params["group"] = resource[:group]
    params["ipsec-protocols"] = resource[:ipsec_protocols]
    params["level"] = resource[:level]
    params["proposal"] = resource[:proposal]
    params["protocol"] = resource[:protocol]
    params["src-address"] = resource[:src_address]
    params["src-port"] = resource[:src_port]
    params["template"] = resource[:template]
    params["tunnel"] = resource[:tunnel]
    params["peer"] = resource[:peer]
    params.compact!

    lookup = { "comment" => resource[:name] }

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/ipsec/policy", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_ipsec_profile\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipsec_profile).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik

  mk_resource_methods

  def self.instances
    instances = []

    profiles = Puppet::Provider::Mikrotik_Api::get_all("/ip/ipsec/profile")
    profiles.each do |profile|
      object = ipsecProfile(profile)
      if object != nil
        instances << object
      end
    end

    instances
  end

  def self.ipsecProfile(data)
    new(
      :ensure                => :present,
      :name                  => data['name'],
      :dh_group              => data['dh-group'].nil? ? nil : data['dh-group'].split(','),
      :dpd_interval          => data['dpd-interval'],
      :dpd_maximum_failures  => data['dpd-maximum-failures'],
      :enc_algorithm         => data['enc-algorithm'].nil? ? nil : data['enc-algorithm'].split(','),
      :hash_algorithm        => data['hash-algorithm'],
      :lifebytes             => data['lifebytes'],
      :lifetime              => data['lifetime'],
      :nat_traversal         => data['nat-traversal'],
      :prf_algorithm         => data['prf-algorithm'] || 'auto',
      :proposal_check        => data['proposal-check'],
    )
  end

  def flush
    Puppet.debug("Flushing IPSec Profile #{resource[:name]}")

    params = {}

    params["name"] = resource[:name]
    params["dh-group"] = resource[:dh_group].join(',') unless resource[:dh_group].nil?
    params["dpd-interval"] = resource[:dpd_interval]
    params["dpd-maximum-failures"] = resource[:dpd_maximum_failures]
    params["enc-algorithm"] = resource[:enc_algorithm].join(',') unless resource[:enc_algorithm].nil?
    params["hash-algorithm"] = resource[:hash_algorithm]
    params["lifebytes"] = resource[:lifebytes]
    params["lifetime"] = resource[:lifetime]
    params['nat-traversal'] = resource[:nat_traversal]
    params['prf-algorithm'] = resource[:prf_algorithm]
    params['proposal-check'] = resource[:proposal_check]
    params.compact!

    lookup = { "name" => resource[:name] }

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/ipsec/profile", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_ipsec_proposal\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipsec_proposal).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    proposals = Puppet::Provider::Mikrotik_Api::get_all("/ip/ipsec/proposal")
    proposals.each do |proposal|
      object = ipsecProposal(proposal)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end
  
  def self.ipsecProposal(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end

    new(
      :ensure          => :present,
      :state           => state,
      :name            => data['name'],
      :comment         => data['comment'],
      :auth_algorithms => data['auth-algorithms'].nil? ? nil : data['auth-algorithms'].split(','),
      :enc_algorithms  => data['enc-algorithms'].nil? ? nil : data['enc-algorithms'].split(','),
      :lifetime        => data['lifetime'],
      :pfs_group       => data['pfs-group'],
    )
  end

  def flush
    Puppet.debug("Flushing IPSec Proposal #{resource[:name]}")

    if @property_hash[:state] == :disabled
      disabled = 'yes'
    elsif @property_hash[:state] == :enabled
      disabled = 'no'
    end
      
    params = {
      "name"                  => resource[:name],
      "comment"               => resource[:comment],
      "disabled"              => disabled,
      "auth-algorithms"       => resource[:auth_algorithms].nil? ? nil : resource[:auth_algorithms].join(','),
      "enc-algorithms"        => resource[:enc_algorithms].nil? ? nil : resource[:enc_algorithms].join(','),
      "lifetime"              => resource[:lifetime],
      "pfs-group"             => resource[:pfs_group],
    }.compact

    lookup = { "name" => resource[:name] }
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/ipsec/proposal", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ipv6_address\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipv6_address).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    addresses = Puppet::Provider::Mikrotik_Api::get_all("/ipv6/address")
    instances = addresses.collect { |address| ipAddress(address) }    
    instances
  end
  
  def self.ipAddress(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end

    if data['eui-64']
      address = data['address']
      # TODO: remove last 4 octets
    else
      address = data['address']
    end   
    
    new(
      :ensure    => :present,
      :state     => state,
      :name      => address,
      :interface => data['interface'],
      :advertise => data['advertise'],
      :eui64     => data['eui-64'],
      :from_pool => data['from-pool']
    )
  end

  def flush
    Puppet.debug("Flushing IPv6 Address #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["address"]   = resource[:name]
    params["interface"] = resource[:interface]
    params["advertise"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:advertise]) if ! resource[:advertise].nil?
    params["eui-64"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:eui64]) if ! resource[:eui64].nil?
    params["from-pool"] = resource[:from_pool] if ! resource[:from_pool].nil?

    lookup = {}
    lookup["address"] = resource[:address]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ipv6/address", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ipv6_address_list\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipv6_address_list).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
    
    sorted_addresses = {}
    address_list_entries = get_all("/ipv6/firewall/address-list")
    address_list_entries.each do |entry|
      list = entry["list"]
      address = entry["address"]
      
      if !sorted_addresses.key?(list)
        sorted_addresses[list] = []
      end
      
      sorted_addresses[list].push(address)      
    end
    
    sorted_addresses.each do |list, addresses|
      instances << addressList(list, addresses)
    end
    
    instances
  end
  
  def self.addressList(list, addresses)
      new(
        :ensure    => :present,
        :name      => list,
        :addresses => addresses
      )
  end

  def flush
    Puppet.debug("Flushing IPv6 Address List #{resource[:name]}")
      
    params = {}
    params["list"] = resource[:name]
    
    #Puppet.debug("Params (= Lookup): #{params.inspect}")
   
    list_flush("/ipv6/firewall/address-list", params, params, :addresses,  "address")
  end
  
  def list_flush(path, params, lookup, list_name, entry_name)  
    Puppet.debug("list_flush(#{path}, #{params.inspect}, #{lookup.inspect}, #{list_name.inspect}, #{entry_name.inspect})")
    
    # create
    if @property_flush[:ensure] == :present
      Puppet.debug("Creating #{path}")
      
      resource[list_name].each do |entry|
        params2 = params.merge({entry_name => entry})
        result = Puppet::Provider::Mikrotik_Api::add(path, params2)
      end
    end
  
    # destroy
    if @property_flush[:ensure] == :absent
      Puppet.debug("Deleting #{path}")
      
      id_list = Puppet::Provider::Mikrotik_Api::lookup_id(path, lookup)
      id_list.each do |id|
        id_lookup = { ".id" => id } 
        result = Puppet::Provider::Mikrotik_Api::remove(path, id_lookup)
      end      
    end      
    
    # update
    if @property_flush.empty?
      Puppet.debug("Updating #{path}")
      
      # Create
      (@property_hash[list_name] - @original_values[list_name]).each do |item|
        params2 = params.merge({entry_name => item})
        result = Puppet::Provider::Mikrotik_Api::add(path, params2)
      end
      
      # Delete
      (@original_values[list_name] - @property_hash[list_name]).each do |item|
        lookup2 = lookup.merge({entry_name => item})
        id_list = Puppet::Provider::Mikrotik_Api::lookup_id(path, lookup2)
        id_list.each do |id|
          id_lookup = { ".id" => id } 
          result = Puppet::Provider::Mikrotik_Api::remove(path, id_lookup)        
        end
      end
    end    
  end
end

File: /lib\puppet\provider\mikrotik_ipv6_firewall_rule\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipv6_firewall_rule).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []

    filter_rules = get_all("/ipv6/firewall/filter")
    filter_rules.each do |rule|
      object = firewallRule(rule, 'filter', filter_rules)
      if object != nil
        instances << object
      end
    end

#    nat_rules = get_all("/ipv6/firewall/nat")
#    nat_rules.each do |rule|
#      object = firewallRule(rule, 'nat', nat_rules)
#      if object != nil
#        instances << object
#      end
#    end

    mangle_rules = get_all("/ipv6/firewall/mangle")
    mangle_rules.each do |rule|
      object = firewallRule(rule, 'mangle', mangle_rules)
      if object != nil
        instances << object
      end      
    end

    instances
  end
  
  def self.firewallRule(rule, table, all_rules)
    if rule['comment'] != nil  
      if rule['disabled'] == 'true'
        state = :disabled
      else
        state = :enabled
      end

      chain_order = getChainOrder(rule['.id'], rule['chain'], all_rules)

      new(
        :ensure                    => :present,
        :state                     => state,
        :name                      => rule['comment'],
        :table                     => table,
        # General
        :chain                     => rule['chain'],
        :chain_order               => chain_order.to_s,
        :src_address               => rule['src-address'],
        :dst_address               => rule['dst-address'],
        :protocol                  => rule['protocol'],
        :src_port                  => rule['src-port'],
        :dst_port                  => rule['dst-port'],
        :port                      => rule['port'],
#        :p2p                       => rule['p2p'],
        :in_interface              => rule['in-interface'],
        :out_interface             => rule['out-interface'],
        :in_interface_list         => rule['in-interface-list'],
        :out_interface_list        => rule['out-interface-list'],
        :packet_mark               => rule['packet-mark'],
        :connection_mark           => rule['connection-mark'],
#        :routing_mark              => rule['routing-mark'],
#        :routing_table             => rule['routing-table'],
        :connection_type           => rule['connection-type'],
        :connection_state          => rule['connection-state'],
#        :connection_nat_state      => rule['connection-nat-state'],
        # Advanced
        :src_address_list          => rule['src-address-list'],
        :dst_address_list          => rule['dst-address-list'],
#        :layer7_protocol           => rule['layer7-protocol'],
        :content                   => rule['content'],
        :connection_bytes          => rule['connection-bytes'],
        :connection_rate           => rule['connection-rate'],
        :per_connection_classifier => rule['per-connection-classifier'],
        :src_mac_address           => rule['src-mac-address'],
        :in_bridge_port            => rule['in-bridge-port'],
        :out_bridge_port           => rule['out-bridge-port'],
        :in_bridge_port_list       => rule['in-bridge-port-list'],
        :out_bridge_port_list      => rule['out-bridge-port-list'],
        :ipsec_policy              => rule['ipsec-policy'],
        :ingress_priority          => rule['ingress-priority'],
        :priority                  => rule['priority'],
        :dscp                      => rule['dscp'],
        :tcp_mss                   => rule['tcp-mss'],
        :packet_size               => rule['packet-size'],
        :random                    => rule['random'],
        :tcp_flags                 => rule['tcp-flags'],      
#        :ipv4_options              => rule['ipv4-options'],
#        :ttl                       => rule['ttl'],
        # ICMP OPTIONS ?
        # Extra  
        :connection_limit          => rule['connection-limit'],
        :limit                     => rule['limit'],
        :dst_limit                 => rule['dst-limit'],
        :nth                       => rule['nth'],
        :time                      => rule['time'],
        :src_address_type          => rule['src-address-type'],
        :dst_address_type          => rule['dst-address-type'],
        # HEADERS ?
        # HOP LIMIT ?
#        :psd                       => rule['psd'],
#        :hotspot                   => rule['hotspot'],
#        :fragment                  => rule['fragment'],      
        # Action    
        :action                    => rule['action'],
        :log                       => rule['log'],
        :log_prefix                => rule['log-prefix'],
        :jump_target               => rule['jump-target'],
        :address_list              => rule['address-list'],
        :address_list_timeout      => rule['address-list-timeout'],
        :reject_with               => rule['reject-with'],
#        :to_addresses              => rule['to-addresses'],
#        :to_ports                  => rule['to-ports'],
        :new_connection_mark       => rule['new-connection-mark'],
        :new_dscp                  => rule['new-dscp'],
        :new_mss                   => rule['new-mss'],
        :new_packet_mark           => rule['new-packet-mark']
#        :new_priority              => rule['new-priority'],
#        :new_routing_mark          => rule['new-routing-mark'],
        # NEW HOP LIMIT ?
#        :new_ttl                   => rule['new-ttl'],
#        :route_dst                 => rule['route-dst'],
#        :sniff_id                  => rule['sniff-id'],
#        :sniff_target              => rule['sniff-target'],
#        :sniff_target_port         => rule['sniff-target-port']
      )
    end
  end

  def flush
    Puppet.debug("Flushing Firewall Rule #{resource[:name]}")

    if @property_flush[:ensure] == :absent
      if @property_hash[:table].nil?
        raise "Table is always a required parameter."
      end
      table = @property_hash[:table]
    else
      if resource[:table].nil? or resource[:chain].nil?
        raise "Table and Chain are required parameters."
      end
      table = resource[:table]
    end
    
    params = {}
        
    if @property_hash[:state] == :disabled
      params["disabled"] = true
    elsif @property_hash[:state] == :enabled
      params["disabled"] = false
    end

    if !resource[:chain_order].nil?
      table_rules = Puppet::Provider::Mikrotik_Api::get_all("/ipv6/firewall/#{table}")
      ids = self.class.getChainIds(resource[:chain], table_rules)
      
      if @property_flush[:ensure] == :present
        unless resource[:chain_order] > ids.length
          rule_id_after = ids[resource[:chain_order].to_i - 1]# index starts at 0, order starts at 1
          params["place-before"] = rule_id_after
        end
      end
    end

    params["comment"] = resource[:name]
    # General
    params["chain"] = resource[:chain] if ! resource[:chain].nil?   
    params["src-address"] = resource[:src_address] if ! resource[:src_address].nil?   
    params["dst-address"] = resource[:dst_address] if ! resource[:dst_address].nil?   
    params["protocol"] = resource[:protocol] if ! resource[:protocol].nil?  
    params["src-port"] = resource[:src_port] if ! resource[:src_port].nil?  
    params["dst-port"] = resource[:dst_port] if ! resource[:dst_port].nil?  
    params["port"] = resource[:port] if ! resource[:port].nil?  
#    params["p2p"] = resource[:p2p] if ! resource[:p2p].nil?        
    params["in-interface"] = resource[:in_interface] if ! resource[:in_interface].nil?  
    params["out-interface"] = resource[:out_interface] if ! resource[:out_interface].nil?  
    params["in-interface-list"] = resource[:in_interface_list] if ! resource[:in_interface_list].nil?  
    params["out-interface-list"] = resource[:out_interface_list] if ! resource[:out_interface_list].nil?  
    params["packet-mark"] = resource[:packet_mark] if ! resource[:packet_mark].nil?  
    params["connection-mark"] = resource[:connection_mark] if ! resource[:connection_mark].nil?  
#    params["routing-mark"] = resource[:routing_mark] if ! resource[:routing_mark].nil?  
#    params["routing-table"] = resource[:routing_table] if ! resource[:routing_table].nil?  
    params["connection-type"] = resource[:connection_type] if ! resource[:connection_type].nil?  
    params["connection-state"] = resource[:connection_state] if ! resource[:connection_state].nil?  
#    params["connection-nat-state"] = resource[:connection_nat_state] if ! resource[:connection_nat_state].nil?
    # Advanced
    params["src-address-list"] = resource[:src_address_list] if ! resource[:src_address_list].nil?
    params["dst-address-list"] = resource[:dst_address_list] if ! resource[:dst_address_list].nil?
#    params["layer7-protocol"] = resource[:layer7_protocol] if ! resource[:layer7_protocol].nil?
    params["content"] = resource[:content] if ! resource[:content].nil?
    params["connection-bytes"] = resource[:connection_bytes] if ! resource[:connection_bytes].nil?
    params["connection-rate"] = resource[:connection_rate] if ! resource[:connection_rate].nil?
    params["per-connection-classifier"] = resource[:per_connection_classifier] if ! resource[:per_connection_classifier].nil?
    params["src-mac-address"] = resource[:src_mac_address] if ! resource[:src_mac_address].nil?
    params["in-bridge-port"] = resource[:in_bridge_port] if ! resource[:in_bridge_port].nil?
    params["out-bridge-port"] = resource[:out_bridge_port] if ! resource[:out_bridge_port].nil?
    params["in-bridge-port-list"] = resource[:in_bridge_port_list] if ! resource[:in_bridge_port_list].nil?
    params["out-bridge-port-list"] = resource[:out_bridge_port_list] if ! resource[:out_bridge_port_list].nil?
    params["ipsec-policy"] = resource[:ipsec_policy] if ! resource[:ipsec_policy].nil?
    params["ingress-priority"] = resource[:ingress_priority] if ! resource[:ingress_priority].nil?
    params["priority"] = resource[:priority] if ! resource[:priority].nil?
    params["dscp"] = resource[:dscp] if ! resource[:dscp].nil?
    params["tcp-mss"] = resource[:tcp_mss] if ! resource[:tcp_mss].nil?
    params["packet-size"] = resource[:packet_size] if ! resource[:packet_size].nil?
    params["random"] = resource[:random] if ! resource[:random].nil?
    params["tcp-flags"] = resource[:tcp_flags] if ! resource[:tcp_flags].nil?  
#    params["ipv4-options"] = resource[:ipv4_options] if ! resource[:ipv4_options].nil?
#    params["ttl"] = resource[:ttl] if ! resource[:ttl].nil?
    # Extra
    params["connection-limit"] = resource[:connection_limit] if ! resource[:connection_limit].nil?
    params["limit"] = resource[:limit] if ! resource[:limit].nil?
    params["dst-limit"] = resource[:dst_limit] if ! resource[:dst_limit].nil?
    params["nth"] = resource[:nth] if ! resource[:nth].nil?
    params["time"] = resource[:time] if ! resource[:time].nil?
    params["src-address-type"] = resource[:src_address_type] if ! resource[:src_address_type].nil?
    params["dst-address-type"] = resource[:dst_address_type] if ! resource[:dst_address_type].nil?
#    params["psd"] = resource[:psd] if ! resource[:psd].nil?
#    params["hotspot"] = resource[:hotspot] if ! resource[:hotspot].nil?
#    params["fragment"] = resource[:fragment] if ! resource[:fragment].nil?  
    # Action
    params["action"] = resource[:action] if ! resource[:action].nil?   
    params["log"] = resource[:log] if ! resource[:log].nil?
    params["log-prefix"] = resource[:log_prefix] if ! resource[:log_prefix].nil?
    params["jump-target"] = resource[:jump_target] if ! resource[:jump_target].nil?
    params["address-list"] = resource[:address_list] if ! resource[:address_list].nil?
    params["address-list-timeout"] = resource[:address_list_timeout] if ! resource[:address_list_timeout].nil?
    params["reject-with"] = resource[:reject_with] if ! resource[:reject_with].nil?
#    params["to-addresses"] = resource[:to_addresses] if ! resource[:to_addresses].nil?
#    params["to-ports"] = resource[:to_ports] if ! resource[:to_ports].nil?
    params["new-connection-mark"] = resource[:new_connection_mark] if ! resource[:new_connection_mark].nil?
    params["new-dscp"] = resource[:new_dscp] if ! resource[:new_dscp].nil?
    params["new-mss"] = resource[:new_mss] if ! resource[:new_mss].nil?
    params["new-packet-mark"] = resource[:new_packet_mark] if ! resource[:new_packet_mark].nil?
#    params["new-priority"] = resource[:new_priority] if ! resource[:new_priority].nil?      
#    params["new-routing-mark"] = resource[:new_routing_mark] if ! resource[:new_routing_mark].nil?
#    params["new-ttl"] = resource[:new_ttl] if ! resource[:new_ttl].nil?
#    params["route-dst"] = resource[:route_dst] if ! resource[:route_dst].nil?
#    params["sniff-id"] = resource[:sniff_id] if ! resource[:sniff_id].nil?
#    params["sniff-target"] = resource[:sniff_target] if ! resource[:sniff_target].nil?
#    params["sniff-target-port"] = resource[:sniff_target_port] if ! resource[:sniff_target_port].nil?
      
    lookup = { "comment" => resource[:name] }
    
    Puppet.debug("Rule: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ipv6/firewall/#{table}", params, lookup)
      
    if !resource[:chain_order].nil?
      if @property_flush.empty?
        id_list = Puppet::Provider::Mikrotik_Api::lookup_id("/ipv6/firewall/#{table}", lookup)
        id_list.each do |id|
          chain_order = self.class.getChainOrder(id, resource[:chain], table_rules)
          if resource[:chain_order].to_i != chain_order
            self.class.moveRule(id, table, resource[:chain], chain_order, resource[:chain_order].to_i, table_rules)
          end
        end
      end
    end
  end
    
  def self.getChainOrder(lookup_id, lookup_chain, table_rules)    
    ids = getChainIds(lookup_chain, table_rules)
    
    chain_order = 1
    ids.each do |id|
      if id == lookup_id
         return chain_order
      end        
     
      chain_order = chain_order + 1
    end
  end
  
  def self.getChainIds(lookup_chain, table_rules)
    ids = table_rules.collect do |rule|
      if rule['chain'] == lookup_chain
        rule['.id']
      end
    end
    
    ids.compact
  end
    
  def self.moveRule(rule_id, table, lookup_chain, old_chain_order, new_chain_order, table_rules)
    Puppet.debug("Moving rule #{rule_id} from position #{old_chain_order} to position #{new_chain_order} in chain #{lookup_chain} on table #{table}.")
    
    if new_chain_order == old_chain_order
      return
    end
  
    if new_chain_order > old_chain_order
      lookup_order = new_chain_order + 1
    else
      lookup_order = new_chain_order
    end
  
    destination = nil
    chain_pos = 0
  
    table_rules.each do |rule|
      if rule['chain'] == lookup_chain
        chain_pos = chain_pos + 1         
      end
      
      if chain_pos == new_chain_order
        destination = rule['.id']  
      end
      
      if chain_pos == lookup_order
        destination = rule['.id']   
        break
      end
    end
  
    if rule_id == destination
      return
    end
  
    move_params = {}
    move_params["numbers"] = rule_id
    move_params["destination"] = destination if destination != nil
    result = Puppet::Provider::Mikrotik_Api::move("/ipv6/firewall/#{table}", move_params)
  end
end

File: /lib\puppet\provider\mikrotik_ipv6_nd_interface\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipv6_nd_interface).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/ipv6/nd")
    instances = interfaces.collect { |interface| ndInterface(interface) }    
    instances
  end
  
  def self.ndInterface(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end

    new(
      :ensure                 => :present,
      :state                  => state,
      :name                   => data['interface'],
      :ra_interval            => data['ra-interval'],
      :ra_delay               => data['ra-delay'],
      :mtu                    => data['mtu'],
      :reachable_time         => data['reachable-time'],
      :retransmit_interval    => data['retransmit-interval'],
      :ra_lifetime            => data['ra-lifetime'],
      :hop_limit              => data['hop-limit'],
      :advertise_mac          => data['advertise-mac-address'],         # BOOLEAN
      :advertise_dns          => data['advertise-dns'],                 # BOOLEAN
      :managed_address_config => data['managed-address-configuration'], # BOOLEAN
      :other_config           => data['other-configuration']            # BOOLEAN
    )
  end

  def flush
    Puppet.debug("Flushing IPv6 Address #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["interface"]   = resource[:name]
    params["ra-interval"] = resource[:ra_interval] if ! resource[:ra_interval].nil?
    params["ra-delay"] = resource[:ra_delay] if ! resource[:ra_delay].nil?
    params["mtu"] = resource[:mtu] if ! resource[:mtu].nil?
    params["reachable-time"] = resource[:reachable_time] if ! resource[:reachable_time].nil?
    params["retransmit-interval"] = resource[:retransmit_interval] if ! resource[:retransmit_interval].nil?
    params["ra-lifetime"] = resource[:ra_lifetime] if ! resource[:ra_lifetime].nil?
    params["hop-limit"] = resource[:hop_limit] if ! resource[:hop_limit].nil?
    params["advertise-mac-address"] = resource[:advertise_mac] if ! resource[:advertise_mac].nil?
    params["advertise-dns"] = resource[:advertise_dns] if ! resource[:advertise_dns].nil?
    params["managed-address-configuration"] = resource[:managed_address_config] if ! resource[:managed_address_config].nil?
    params["other-configuration"] = resource[:other_config] if ! resource[:other_config].nil?
    #    params["xxx-xxx"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:xxx_xxx]) if ! resource[:xxx_xxx].nil?
      
    lookup = {}
    lookup["interface"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ipv6/nd", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ipv6_pool\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipv6_pool).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik

  mk_resource_methods

  def self.instances   
    instances = []

    pools = Puppet::Provider::Mikrotik_Api::get_all("/ipv6/pool")
    pools.each do |pool|
      object = ipPool(pool)
      if object != nil        
        instances << object
      end
    end

    instances
  end

  def self.ipPool(data)
    new(
      :ensure        => :present,
      :name          => data['name'],
      :prefix        => data['prefix'], 
      :prefix_length => data['prefix-length']
    )
  end

  def flush
    Puppet.debug("Flushing IPv6 Pool #{resource[:name]}")

    params = {}
    params["name"] = resource[:name]
    params["prefix"] = resource[:prefix] if !resource[:prefix].nil?
    params["prefix-length"] = resource[:prefix_length] if !resource[:prefix_length].nil?

    lookup = {}
    lookup["name"] = resource[:name]

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ipv6/pool", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_ipv6_route\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipv6_route).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    routes = Puppet::Provider::Mikrotik_Api::get_all("/ipv6/route")
    routes.each do |route|
      object = ipRoute(route)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end
  
  def self.ipRoute(data)
    if data['comment'] != nil
      if data['disabled'] == "true"
        state = :disabled
      else
        state = :enabled
      end
      
      new(
        :ensure               => :present,
        :state                => state,
        :name                 => data['comment'],
        :dst_address          => data['dst-address'], 
        :gateway              => data['gateway'],
        :check_gateway        => data['check-gateway'],
        :type                 => data['type'],
        :distance             => data['distance'],
        :scope                => data['scope'],
        :target_scope         => data['target-scope'],
        :bgp_as_path          => data['bgp-as-path'],   
        :bgp_local_pref       => data['bgp-local-pref'],
        :bgp_prepend          => data['bgp-prepend'],
        :bgp_med              => data['bgp-med'],
        :bgp_atomic_aggregate => data['bgp-atomic-aggregate'],
        :bgp_origin           => data['bgp-origin'],
        :route_tag            => data['route-tag'],
        :bgp_communities      => data['bgp-communities']
      )
    end
  end

  def flush
    Puppet.debug("Flushing IPv6 Route #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["comment"] = resource[:name]
    params["dst-address"] = resource[:dst_address]
    Puppet.info("IPv6 DST Address = Params: #{params["dst-address"].inspect}")
    params["gateway"] = resource[:gateway] if !resource[:gateway].nil?
    params["check-gateway"] = resource[:check_gateway] if !resource[:check_gateway].nil?
    params["type"] = resource[:type] if !resource[:type].nil?
    params["distance"] = resource[:distance] if !resource[:distance].nil?
    params["scope"] = resource[:scope] if !resource[:scope].nil?
    params["target-scope"] = resource[:target_scope] if !resource[:target_scope].nil?
    params["bgp-as-path"] = resource[:bgp_as_path] if !resource[:bgp_as_path].nil?
    params["bgp-local-pref"] = resource[:bgp_local_pref] if !resource[:bgp_local_pref].nil?
    params["bgp-prepend"] = resource[:bgp_prepend] if !resource[:bgp_prepend].nil?
    params["bgp-med"] = resource[:bgp_med] if !resource[:bgp_med].nil?
    params["bgp-atomic-aggregate"] = resource[:bgp_atomic_aggregate] if !resource[:bgp_atomic_aggregate].nil?
    params["bgp-origin"] = resource[:bgp_origin] if !resource[:bgp_origin].nil?
    params["route-tag"] = resource[:route_tag] if !resource[:route_tag].nil?
    params["bgp-communities"] = resource[:bgp_communities] if !resource[:bgp_communities].nil?

    lookup = {}
    lookup["comment"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ipv6/route", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ipv6_settings\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ipv6_settings).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
      
    ip_settings = Puppet::Provider::Mikrotik_Api::get_all("/ipv6/settings")
    ip_settings.each do |data|
      object = ipSettings(data)
      if object != nil
        instances << object
      end
    end

    instances
  end
  
  def self.ipSettings(data)
    new(
      :name                         => 'ipv6',
      :forward                      => data['forward'],
      :accept_redirects             => (data['accept-redirects'] == "yes-if-forwarding-disabled"?'true':'false'),# TODO: verify string boolean ?
      :accept_router_advertisements => data['accept-router-advertisements'],
      :max_neighbor_entries         => data['max-neighbor-entries']
    )
  end

  def flush
    Puppet.debug("Flushing IPv6 Settings")
    
    if (@property_hash[:name] != 'ipv6') 
      raise "There is only one set of IP settings. Title (name) should be -ipv6-"
    end
    
    update = {}
    update["forward"] = resource[:forward] if ! resource[:forward].nil?
    if !resource[:accept_redirects].nil? 
      if resource[:accept_redirects] == :true    # TODO: verify types (string/bool)
        update["accept-redirects"] = "yes-if-forwarding-disabled"
      else
        update["accept-redirects"] = "no"
      end
    end
    update["accept-router-advertisements"] = resource[:accept_router_advertisements] if ! resource[:accept_router_advertisements].nil?
    update["max-neighbor-entries"] = resource[:max_neighbor_entries] if ! resource[:max_neighbor_entries].nil?
    
    result = Puppet::Provider::Mikrotik_Api::set("/ipv6/settings", update)
  end
end


File: /lib\puppet\provider\mikrotik_ip_address\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ip_address).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    addresses = Puppet::Provider::Mikrotik_Api::get_all("/ip/address")
    instances = addresses.collect { |address| ipAddress(address) }    
    instances
  end
  
  def self.ipAddress(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure     => :present,
      :state      => state,
      :name       => data['address'],
      :interface  => data['interface']
    )
  end

  def flush
    Puppet.debug("Flushing IP Address #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["address"]   = resource[:name]
    params["interface"] = resource[:interface]

    lookup = {}
    lookup["address"] = resource[:address]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/address", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ip_hotspot\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ip_hotspot).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    servers = Puppet::Provider::Mikrotik_Api::get_all("/ip/hotspot")
    servers.each do |server|
      object = hsServer(server)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end

  def self.hsServer(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
        
    new(
      :ensure            => :present,
      :state             => state,
      :name              => data['name'],
      :address_pool      => data['address-pool'],
      :addresses_per_mac => data['addresses-per-mac'],
      :idle_timeout      => data['idle-timeout'],
      :interface         => data['interface'],
      :keepalive_timeout => data['keepalive-timeout'],
      :login_timeout     => data['login-timeout'],
      :profile           => data['profile']
    )
  end

  def flush
    Puppet.debug("Flushing Hotspot Server #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["name"] = resource[:name]
    params["address-pool"] = resource[:address_pool] if !resource[:address_pool].nil?
    params["addresses-per-mac"] = resource[:addresses_per_mac] if !resource[:addresses_per_mac].nil?
    params["idle-timeout"] = resource[:idle_timeout] if !resource[:idle_timeout].nil?
    params["interface"] = resource[:interface] if !resource[:interface].nil?
    params["keepalive-timeout"] = resource[:keepalive_timeout] if !resource[:keepalive_timeout].nil?
    params["login-timeout"] = resource[:login_timeout] if !resource[:login_timeout].nil?
    params["profile"] = resource[:profile] if !resource[:profile].nil?
      
    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/hotspot", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ip_hotspot_profile\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ip_hotspot_profile).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    profiles = Puppet::Provider::Mikrotik_Api::get_all("/ip/hotspot/profile")
    profiles.each do |profile|
      object = hsProfile(profile)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end
  
  def self.hsProfile(data)
    new(
      :ensure                => :present,
      :name                  => data['name'],
      :dns_name              => data['dns-name'],
      :hotspot_address       => data['hotspot-address'],
      :html_directory        => data['html-directory'],
      # html-directory-override
      :http_cookie_lifetime  => data['http-cookie-lifetime'],
      #  http-proxy
      :login_by              => data['login-by'].split(','),
      # mac-auth-mode
      # mac-auth-password
      :nas_port_type         => data['nas-port-type'],
      :radius_accounting     => (data['radius-accounting'].nil? ? :false : data['radius-accounting']),
      :radius_default_domain => data['radius-default-domain'],
      :radius_interim_update => data['radius-interim-update'],
      :radius_location_id    => data['radius-location-id'],
      :radius_location_name  => data['radius-location-name'],
      # radius-mac-format
      # rate-limit
      # smtp-server
      :split_user_domain     => (data['split-user-domain'].nil? ? :false : data['split-user-domain']),
      #ssl-certificate
      :trial_uptime_limit    => data['trial-uptime-limit'],
      :trial_uptime_reset    => data['trial-uptime-reset'],
      :trial_user_profile    => data['trial-user-profile'],
      :use_radius            => (data['use-radius'].nil? ? :false : data['use-radius'])
    )
  end

  def flush
    Puppet.debug("Flushing Hotspot Profile #{resource[:name]}")
      
    params = {}

    params["name"] = resource[:name]
    params["dns-name"] = resource[:dns_name] if !resource[:dns_name].nil?
    params["hotspot-address"] = resource[:hotspot_address] if !resource[:hotspot_address].nil?
    params["html-directory"] = resource[:html_directory] if !resource[:html_directory].nil?
    params["http-cookie-lifetime"] = resource[:http_cookie_lifetime] if !resource[:http_cookie_lifetime].nil?
    params["nas-port-type"] = resource[:nas_port_type] if !resource[:nas_port_type].nil?
    params["radius-default-domain"] = resource[:radius_default_domain] if !resource[:radius_default_domain].nil?
    params["radius-interim-update"] = resource[:radius_interim_update] if !resource[:radius_interim_update].nil?
    params["radius-location-id"] = resource[:radius_location_id] if !resource[:radius_location_id].nil?
    params["radius-location-name"] = resource[:radius_location_name] if !resource[:radius_location_name].nil?
    params["trial_uptime_limit"] = resource[:trial_uptime_limit] if !resource[:trial_uptime_limit].nil?
    params["trial_uptime_reset"] = resource[:trial_uptime_reset] if !resource[:trial_uptime_reset].nil?
    params["trial_user_profile"] = resource[:trial_user_profile] if !resource[:trial_user_profile].nil?

    params["login-by"] = resource[:login_by].join(',') if ! resource[:login_by].nil?
    
    params["radius-accounting"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:radius_accounting]) if ! resource[:radius_accounting].nil?
    params["split-user-domain"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:split_user_domain]) if ! resource[:split_user_domain].nil?
    params["use-radius"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:use_radius]) if ! resource[:use_radius].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/hotspot/profile", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ip_pool\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ip_pool).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    pools = Puppet::Provider::Mikrotik_Api::get_all("/ip/pool")
    pools.each do |pool|
      object = ipPool(pool)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end
  
  def self.ipPool(data)
    new(
      :ensure    => :present,
      :name      => data['name'],
      :ranges    => data['ranges'].split(','), 
      :next_pool => data['next-pool']
    )
  end

  def flush
    Puppet.debug("Flushing IP Pool #{resource[:name]}")
      
    params = {}
    params["name"] = resource[:name]
    params["ranges"] = resource[:ranges].join(',') if !resource[:ranges].nil?
    params["next-pool"] = resource[:next_pool] if !resource[:next_pool].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/pool", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ip_route\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ip_route).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    routes = Puppet::Provider::Mikrotik_Api::get_all("/ip/route")
    routes.each do |route|
      object = ipRoute(route)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end
  
  def self.ipRoute(data)
    if data['comment'] != nil
      if data['disabled'] == "true"
        state = :disabled
      else
        state = :enabled
      end
      
      new(
        :ensure               => :present,
        :state                => state,
        :name                 => data['comment'],
        :dst_address          => data['dst-address'], 
        :gateway              => data['gateway'],
        :check_gateway        => data['check-gateway'],
        :type                 => data['type'],
        :distance             => data['distance'],
        :scope                => data['scope'],
        :target_scope         => data['target-scope'],
        :routing_mark         => data['routing-mark'],
        :pref_src             => data['pref-src'],
        :bgp_as_path          => data['bgp-as-path'],   
        :bgp_local_pref       => data['bgp-local-pref'],
        :bgp_prepend          => data['bgp-prepend'],
        :bgp_med              => data['bgp-med'],
        :bgp_atomic_aggregate => data['bgp-atomic-aggregate'],
        :bgp_origin           => data['bgp-origin'],
        :route_tag            => data['route-tag'],
        :bgp_communities      => data['bgp-communities']
      )
    end
  end

  def flush
    Puppet.debug("Flushing IP Route #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["comment"] = resource[:name]
    params["dst-address"] = resource[:dst_address]
    params["gateway"] = resource[:gateway] if !resource[:gateway].nil?
    params["check-gateway"] = resource[:check_gateway] if !resource[:check_gateway].nil?
    params["type"] = resource[:type] if !resource[:type].nil?
    params["distance"] = resource[:distance] if !resource[:distance].nil?
    params["scope"] = resource[:scope] if !resource[:scope].nil?
    params["target-scope"] = resource[:target_scope] if !resource[:target_scope].nil?
    params["routing-mark"] = resource[:routing_mark] if !resource[:routing_mark].nil?
    params["pref-src"] = resource[:pref_src] if !resource[:pref_src].nil?
    params["bgp-as-path"] = resource[:bgp_as_path] if !resource[:bgp_as_path].nil?
    params["bgp-local-pref"] = resource[:bgp_local_pref] if !resource[:bgp_local_pref].nil?
    params["bgp-prepend"] = resource[:bgp_prepend] if !resource[:bgp_prepend].nil?
    params["bgp-med"] = resource[:bgp_med] if !resource[:bgp_med].nil?
    params["bgp-atomic-aggregate"] = resource[:bgp_atomic_aggregate] if !resource[:bgp_atomic_aggregate].nil?
    params["bgp-origin"] = resource[:bgp_origin] if !resource[:bgp_origin].nil?
    params["route-tag"] = resource[:route_tag] if !resource[:route_tag].nil?
    params["bgp-communities"] = resource[:bgp_communities] if !resource[:bgp_communities].nil?

    lookup = {}
    lookup["comment"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/route", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ip_route_rule\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ip_route_rule).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    rules = Puppet::Provider::Mikrotik_Api::get_all("/ip/route/rule")
    rules.each do |rule|
      object = ipRule(rule)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end
  
  def self.ipRule(data)
    if data['comment'] != nil
      if data['disabled'] == "true"
        state = :disabled
      else
        state = :enabled
      end
      
      new(
        :ensure       => :present,
        :state        => state,
        :name         => data['comment'],
        :src_address  => data['src-address'],
        :dst_address  => data['dst-address'],
        :routing_mark => data['routing-mark'],
        :interface    => data['interface'],
        :action       => data['action'],
        :table        => data['table']
      )
    end
  end

  def flush
    Puppet.debug("Flushing IP Route Rule #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["comment"] = resource[:name]
    params["src-address"] = resource[:src_address] if !resource[:src_address].nil?
    params["dst-address"] = resource[:dst_address] if !resource[:dst_address].nil?
    params["routing-mark"] = resource[:routing_mark] if !resource[:routing_mark].nil?
    params["interface"] = resource[:interface] if !resource[:interface].nil?
    params["action"] = resource[:action] if !resource[:action].nil?
    params["table"] = resource[:table] if !resource[:table].nil?

    lookup = {}
    lookup["comment"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/route/rule", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ip_route_vrf\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ip_route_vrf).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    tables = Puppet::Provider::Mikrotik_Api::get_all("/ip/route/vrf")
    tables.each do |table|
      object = vrf(table)
      if object != nil        
        instances << object
      end
    end
    
    instances
  end
  
  def self.vrf(data)
    if data['routing-mark'] != nil
      if data['disabled'] == "true"
        state = :disabled
      else
        state = :enabled
      end
      
      new(
        :ensure               => :present,
        :state                => state,
        :name                 => data['routing-mark'],
        :interfaces           => data['interfaces'].nil? ? nil : data['interfaces'].split(','),
        :route_distinguisher  => data['route-distinguisher'],
        :import_route_targets => data['import-route-targets'].nil? ? nil : data['import-route-targets'].split(','),
        :export_route_targets => data['export-route-targets'].nil? ? nil : data['export-route-targets'].split(',')
      )
    end
  end

  def flush
    Puppet.debug("Flushing IP Route VRF #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["routing-mark"] = resource[:name]
    params["interfaces"] = resource[:interfaces].join(',') if !resource[:interfaces].nil?
    params["route-distinguisher"] = resource[:route_distinguisher] if !resource[:route_distinguisher].nil?
    params["import-route-targets"] = resource[:import_route_targets].join(',') if !resource[:import_route_targets].nil?
    params["export-route-targets"] = resource[:export_route_targets].join(',') if !resource[:export_route_targets].nil?

    lookup = {}
    lookup["routing-mark"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ip/route/vrf", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ip_service\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ip_service).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
    
    services = get_all("/ip/service")
    instances = services.collect { |service| ipService(service) }
    
    instances
  end
  
  def self.ipService(service)
    #Puppet.debug("IP Service: #{service.inspect}")
    
    if service['disabled'] == 'true'
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure    => :present,
      :state     => state,
      :name      => service['name'],
      :port      => service['port'],
      :addresses => service['address'].split(',')
    )
  end

  def flush
    Puppet.debug("Flushing IP Service #{resource[:name]}")
    
    path = '/ip/service'
    
    params = {}
        
    if @property_hash[:state] == :disabled
      params["disabled"] = true
    elsif @property_hash[:state] == :enabled
      params["disabled"] = false
    end
    
    params["port"] = resource[:port] if ! resource[:port].nil?   
    if ! resource[:addresses].nil?
      params["address"] = resource[:addresses].join(',')
    end
             
    lookup = { "name" => resource[:name] }
    
    id_list = Puppet::Provider::Mikrotik_Api::lookup_id(path, lookup)
    id_list.each do |id|
      params = params.merge({ ".id" => id })
      result = Puppet::Provider::Mikrotik_Api::set(path, params)
    end
  end  
end

File: /lib\puppet\provider\mikrotik_ip_settings\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ip_settings).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
      
    ip_settings = Puppet::Provider::Mikrotik_Api::get_all("/ip/settings")
    ip_settings.each do |data|
      object = ipSettings(data)
      if object != nil
        instances << object
      end
    end

    instances
  end
  
  def self.ipSettings(data)
    new(
      :name      => 'ip',
      :rp_filter => data['rp-filter']
    )
  end

  def flush
    Puppet.debug("Flushing IP Settings")
    
    if (@property_hash[:name] != 'ip') 
      raise "There is only one set of IP settings. Title (name) should be -ip-"
    end
    
    update = {}
    update["rp-filter"] = resource[:rp_filter] if ! resource[:rp_filter].nil?
    
    result = Puppet::Provider::Mikrotik_Api::set("/ip/settings", update)
  end
end

File: /lib\puppet\provider\mikrotik_logging_action\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_logging_action).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances      
    actions = get_all("/system/logging/action")
    instances = actions.collect { |action| loggingAction(action) }
  end
  
  def self.loggingAction(action)
    new(
      :ensure          => :present,
      :name            => action['name'],
      :target          => action['target'],
      :remote          => action['remote'],
      :remote_port     => action['remote-port'],
      :src_address     => action['src-address'],
      :bsd_syslog      => action['bsd-syslog'],
      :syslog_facility => action['syslog-facility'],
      :syslog_severity => action['syslog-severity']
    )
  end

  def flush
    Puppet.debug("Flushing Logging Action #{resource[:name]}")

    if @property_flush[:ensure] == :present
      if resource[:target].nil?
        raise "Target is a required parameter."
      end
    end

    params = {}
    params["name"] = resource[:name]
    params["target"] = resource[:target]
    if (resource[:target] == :remote)
      params["remote"] = resource[:remote] if ! resource[:remote].nil?
      params["remote-port"] = resource[:remote_port] if ! resource[:remote_port].nil?
      params["src-address"] = resource[:src_address] if ! resource[:src_address].nil?      
      if ! resource[:bsd_syslog].nil?
        params["bsd-syslog"] = resource[:bsd_syslog]?"yes":"no"        
      end
      params["syslog_-facility"] = resource[:syslog_facility] if ! resource[:syslog_facility].nil?
      params["syslog-severity"] = resource[:syslog_severity] if ! resource[:syslog_severity].nil?
    end
    
    lookup = { "name" => resource[:name] }
    
    Puppet.debug("Rule: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/system/logging/action", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_logging_rule\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_logging_rule).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    rules = get_all("/system/logging")
    instances = rules.collect { |rule| loggingRule(rule) }
  end
  
  def self.loggingRule(rule)
    topics = rule['topics'].split(',')
    name = topics.join('_') + "_" + rule['action']
    
    new(
      :ensure => :present,
      :name   => name,
      :topics => topics,
      :action => rule['action']
    )
  end

  def flush
    Puppet.debug("Flushing Logging Rule #{resource[:name]}")
    
    if resource[:topics].nil? or resource[:action].nil?
      raise "topics and action are required parameters."
    end      
    
    params = {}
    params["topics"] = resource[:topics].join(',')
    params["action"] = resource[:action] 
    
    lookup = { 
      "topics" => resource[:topics].join(','),
      "action" => resource[:action]
    }
    
    Puppet.debug("Rule: #{params.inspect} - Lookup: #{lookup.inspect}")
      
    simple_flush("/system/logging", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_mpls_ldp\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_mpls_ldp).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
      
    ldp = Puppet::Provider::Mikrotik_Api::get_all("/mpls/ldp")
    ldp.each do |data|
      object = mplsLdp(data)
      if object != nil
        instances << object
      end
    end

    instances
  end
  
  def self.mplsLdp(data)
    if data['enabled'] == "true"
      state = :enabled
    else
      state = :disabled
    end
    
    new(
      :name                         => 'ldp',
      :ensure                       => :present,
      :state                        => state,
      :lsr_id                       => data['lsr-id'],
      :transport_address            => data['transport-address'],
      :path_vector_limit            => data['path-vector-limit'],
      :hop_limit                    => data['hop-limit'],
      :loop_detect                  => data['loop-detect'],
      :use_explicit_null            => data['use-explicit-null'],
      :distribute_for_default_route => data['distribute-for-default-route']
    )
  end

  def flush
    Puppet.debug("Flushing MPLS LDP")
    
    if (@property_hash[:name] != 'ldp') 
      raise "There is only one set of MPLS LDP settings. Title (name) should be -ldp-"
    end
    
    update = {}

    if @property_hash[:state] == :disabled
      update["enabled"] = 'no'
    elsif @property_hash[:state] == :enabled
      update["enabled"] = 'yes'
    end
    
    update["lsr-id"] = resource[:lsr_id] if ! resource[:lsr_id].nil?
    update["transport-address"] = resource[:transport_address] if ! resource[:transport_address].nil?
    update["path-vector-limit"] = resource[:path_vector_limit] if ! resource[:path_vector_limit].nil?
    update["hop-limit"] = resource[:hop_limit] if ! resource[:hop_limit].nil?
    update["loop-detect"] = resource[:loop_detect] if ! resource[:loop_detect].nil?
    update["use-explicit-null"] = resource[:use_explicit_null] if ! resource[:use_explicit_null].nil?
    update["distribute-for-default-route"] = resource[:distribute_for_default_route] if ! resource[:distribute_for_default_route].nil?
    
    result = Puppet::Provider::Mikrotik_Api::set("/mpls/ldp", update)
  end
end

File: /lib\puppet\provider\mikrotik_mpls_ldp_interface\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_mpls_ldp_interface).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
      
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/mpls/ldp/interface")
    interfaces.each do |interface|
      object = mplsLdpInterface(interface)
      if object != nil
        instances << object
      end
    end

    instances
  end
  
  def self.mplsLdpInterface(data)    
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :name                     => data['interface'],
      :ensure                   => :present,
      :state                    => state,
      :hello_interval           => data['hello-interval'],
      :hold_time                => data['hold-time'],
      :transport_address        => data['transport-address'],
      :accept_dynamic_neighbors => data['accept-dynamic-neighbors']
    )
  end

  def flush 
    Puppet.debug("Flushing MPLS LDP Interface #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["interface"] = resource[:name]
    params["hello-interval"] = resource[:hello_interval] if ! resource[:hello_interval].nil?
    params["hold-time"] = resource[:hold_time] if ! resource[:hold_time].nil?
    params["transport-address"] = resource[:transport_address] if ! resource[:transport_address].nil?
    params["accept-dynamic-neighbors"] = resource[:accept_dynamic_neighbors] if ! resource[:accept_dynamic_neighbors].nil?

    lookup = {}
    lookup["interface"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/mpls/ldp/interface", params, lookup)
  end
end

File: /lib\puppet\provider\mikrotik_mpls_te_interface\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_mpls_te_interface).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/mpls/traffic-eng/interface")
    instances = interfaces.collect { |interface| teInterface(interface) }    
    instances
  end

  def self.teInterface(data)    
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :name         => data['interface'],
      :ensure       => :present,
      :state        => state,
      :bandwidth    => data['bandwidth'],
      :k_factor     => data['k-factor'],
      :refresh_time => data['refresh-time']
    )
  end

  def flush 
    Puppet.debug("Flushing MPLS TE Interface #{resource[:name]}")

    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end

    params["interface"]     = resource[:name]
    params["bandwidth"]     = resource[:bandwidth]    if ! resource[:bandwidth].nil?
    params["k-factor"]      = resource[:k_factor]     if ! resource[:k_factor].nil?
    params["refresh-time"]  = resource[:refresh_time] if ! resource[:refresh_time].nil?

    lookup = {}
    lookup["interface"] = resource[:name]

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/mpls/traffic-eng/interface", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_mpls_te_path\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_mpls_te_path).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    paths = Puppet::Provider::Mikrotik_Api::get_all("/mpls/traffic-eng/tunnel-path")
    instances = paths.collect { |path| tunnelPath(path) }    
    instances
  end

  def self.tunnelPath(data)    
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :name         => data['name'],
      :ensure       => :present,
      :state        => state,
      :use_cspf     => (data['use-cspf'].nil?     ? :false : data['use-cspf']),
      :record_route => (data['record-route'].nil? ? :false : data['record-route']),
      :hops         => data['hops'].split(',')
    )
  end

  def flush 
    Puppet.debug("Flushing MPLS TE Tunnel Path #{resource[:name]}")
      
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["name"] = resource[:name]
    params["use-cspf"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:use_cspf]) if ! resource[:use_cspf].nil?
    params["record-route"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:record_route]) if ! resource[:record_route].nil?
    params["hops"] = resource[:hops].join(',') if ! resource[:hops].nil?  

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/mpls/traffic-eng/tunnel-path", params, lookup)
  end
end

File: /lib\puppet\provider\mikrotik_ospfv3_area\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ospfv3_area).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    ospf_areas = Puppet::Provider::Mikrotik_Api::get_all("/routing/ospf-v3/area")
    instances = ospf_areas.collect { |ospf_area| ospfArea(ospf_area) }    
    instances
  end
  
  def self.ospfArea(data)
      new(
        :ensure    => :present,
        :name      => data['name'],
        :area_id   => data['area-id'],
        :instance  => data['instance'],
        :area_type => data['type']
      )
  end

  def flush
    Puppet.debug("Flushing OSPFv3 Area #{resource[:name]}")
      
    params = {}
    params["name"] = resource[:name]
    params["area-id"] = resource[:area_id] if ! resource[:area_id].nil?
    params["instance"] = resource[:instance] if ! resource[:instance].nil?
    params["type"] = resource[:area_type] if ! resource[:area_type].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/ospf-v3/area", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ospfv3_instance\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ospfv3_instance).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    ospf_instances = Puppet::Provider::Mikrotik_Api::get_all("/routing/ospf-v3/instance")
    instances = ospf_instances.collect { |ospf_instance| ospfInstance(ospf_instance) }    
    instances
  end
  
  def self.ospfInstance(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure                 => :present,
      :state                  => state,
      :name                   => data['name'],
      :router_id              => data['router-id'],
      :distribute_default     => data['distribute-default'],
      :redistribute_connected => data['redistribute-connected'],
      :redistribute_static    => data['redistribute-static'],
      :redistribute_ospf      => data['redistribute-other-ospf'],
      :redistribute_bgp       => data['redistribute-bgp'],
      :redistribute_rip       => data['redistribute-rip'],
      :metric_default         => data['metric-default'],
      :metric_connected       => data['metric-connected'],
      :metric_static          => data['metric-static'],
      :metric_ospf            => data['metric-other-ospf'],
      :metric_bgp             => data['metric-bgp'],
      :metric_rip             => data['metric-rip']
    )
  end

  def flush
    Puppet.debug("Flushing OSPFv3 Instance #{resource[:name]}")
      
    params = {}
      
    if @property_hash[:state] == :disabled
      params["disabled"] = true
    elsif @property_hash[:state] == :enabled
      params["disabled"] = false
    end

    params["name"] = resource[:name]
    params["router-id"] = resource[:router_id] if ! resource[:router_id].nil?
    params["distribute-default"] = resource[:distribute_default] if ! resource[:distribute_default].nil?
    params["redistribute-connected"] = resource[:redistribute_connected] if ! resource[:redistribute_connected].nil?
    params["redistribute-static"] = resource[:redistribute_static] if ! resource[:redistribute_static].nil?
    params["redistribute-other-ospf"] = resource[:redistribute_ospf] if ! resource[:redistribute_ospf].nil?
    params["redistribute-bgp"] = resource[:redistribute_bgp] if ! resource[:redistribute_bgp].nil?
    params["redistribute-rip"] = resource[:redistribute_rip] if ! resource[:redistribute_rip].nil?
    params["metric-default"] = resource[:metric_default] if ! resource[:metric_default].nil?
    params["metric-connected"] = resource[:metric_connected] if ! resource[:metric_connected].nil?
    params["metric-static"] = resource[:metric_static] if ! resource[:metric_static].nil?
    params["metric-bgp"] = resource[:metric_bgp] if ! resource[:metric_bgp].nil?
    params["metric-other-ospf"] = resource[:metric_ospf] if ! resource[:metric_ospf].nil?
    params["metric-rip"] = resource[:metric_rip] if ! resource[:metric_rip].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/ospf-v3/instance", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ospfv3_interface\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ospfv3_interface).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    ospf_interfaces = Puppet::Provider::Mikrotik_Api::get_all("/routing/ospf-v3/interface")
    instances = ospf_interfaces.collect { |ospf_interface| ospfInterface(ospf_interface) }    
    instances
  end

  def self.ospfInterface(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure       => :present,
      :state        => state,
      :name         => data['interface'],
      :area         => data['area'],
      :cost         => data['cost'],
      :priority     => data['priority'],
      :network_type => data['network-type'],
      :passive      => data['passive'],
      :use_bfd      => data['use-bfd']
    )
  end

  def flush
    Puppet.debug("Flushing OSPFv3 Interface #{resource[:name]}")
      
    params = {}
    if @property_hash[:state] == :disabled
      params["disabled"] = true
    elsif @property_hash[:state] == :enabled
      params["disabled"] = false
    end
    
    params["interface"] = resource[:name]
    params["area"] = resource[:area] if ! resource[:area].nil?
    params["cost"] = resource[:cost] if ! resource[:cost].nil?
    params["priority"] = resource[:priority] if ! resource[:priority].nil?
    params["network-type"] = resource[:network_type] if ! resource[:network_type].nil?
    params["passive"] = resource[:passive] if ! resource[:passive].nil?
    params["use-bfd"] = resource[:use_bfd] if ! resource[:use_bfd].nil?

    lookup = {}
    lookup["interface"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/ospf-v3/interface", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ospf_area\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ospf_area).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    ospf_areas = Puppet::Provider::Mikrotik_Api::get_all("/routing/ospf/area")
    instances = ospf_areas.collect { |ospf_area| ospfArea(ospf_area) }    
    instances
  end
  
  def self.ospfArea(data)
      new(
        :ensure    => :present,
        :name      => data['name'],
        :area_id   => data['area-id'],
        :instance  => data['instance'],
        :area_type => data['type']
      )
  end

  def flush
    Puppet.debug("Flushing OSPF Area #{resource[:name]}")
      
    params = {}
    params["name"] = resource[:name]
    params["area-id"] = resource[:area_id] if ! resource[:area_id].nil?
    params["instance"] = resource[:instance] if ! resource[:instance].nil?
    params["type"] = resource[:area_type] if ! resource[:area_type].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/ospf/area", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ospf_area_range\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ospf_area_range).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    ospf_area_ranges = Puppet::Provider::Mikrotik_Api::get_all("/routing/ospf/area/range")
    instances = ospf_area_ranges.collect { |ospf_area_range| ospfAreaRange(ospf_area_range) }    
    instances
  end
  
  def self.ospfAreaRange(data)
      new(
        :ensure    => :present,
        :name      => data['range'],
        :area      => data['area'],
        :cost      => data['cost'],
        :advertise => data['advertise'],
        :comment   => data['comment']
      )
  end

  def flush
    Puppet.debug("Flushing OSPF Area Range #{resource[:name]}/#{resource[:area]}")

    params = {}
    params["range"]     = resource[:name]
    params["area"]      = resource[:area]
    params["cost"]      = resource[:cost]
    params["advertise"] = resource[:advertise]
    params["comment"]   = resource[:comment] if ! resource[:comment].nil?

    lookup = {
      "range" => resource[:name],
      "area"  => resource[:area]
    }
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/ospf/area/range", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ospf_instance\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ospf_instance).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    ospf_instances = Puppet::Provider::Mikrotik_Api::get_all("/routing/ospf/instance")
    instances = ospf_instances.collect { |ospf_instance| ospfInstance(ospf_instance) }    
    instances
  end
  
  def self.ospfInstance(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure                 => :present,
      :state                  => state,
      :name                   => data['name'],
      :router_id              => data['router-id'],
      :distribute_default     => data['distribute-default'],
      :redistribute_connected => data['redistribute-connected'],
      :redistribute_static    => data['redistribute-static'],
      :redistribute_ospf      => data['redistribute-other-ospf'],
      :redistribute_bgp       => data['redistribute-bgp'],
      :redistribute_rip       => data['redistribute-rip'],
      :in_filter              => data['in-filter'],
      :out_filter             => data['out-filter'],
      :metric_default         => data['metric-default'],
      :metric_connected       => data['metric-connected'],
      :metric_static          => data['metric-static'],
      :metric_ospf            => data['metric-other-ospf'],
      :metric_bgp             => data['metric-bgp'],
      :metric_rip             => data['metric-rip'],
      :mpls_te_area           => data['mpls-te-area'],
      :mpls_te_router_id      => data['mpls-te-router-id'],
      :routing_table          => data['routing-table']
    )
  end

  def flush
    Puppet.debug("Flushing OSPF Instance #{resource[:name]}")
      
    params = {}
      
    if @property_hash[:state] == :disabled
      params["disabled"] = true
    elsif @property_hash[:state] == :enabled
      params["disabled"] = false
    end

    params["name"] = resource[:name]
    params["router-id"] = resource[:router_id] if ! resource[:router_id].nil?
    params["distribute-default"] = resource[:distribute_default] if ! resource[:distribute_default].nil?
    params["redistribute-connected"] = resource[:redistribute_connected] if ! resource[:redistribute_connected].nil?
    params["redistribute-static"] = resource[:redistribute_static] if ! resource[:redistribute_static].nil?
    params["redistribute-other-ospf"] = resource[:redistribute_ospf] if ! resource[:redistribute_ospf].nil?
    params["redistribute-bgp"] = resource[:redistribute_bgp] if ! resource[:redistribute_bgp].nil?
    params["redistribute-rip"] = resource[:redistribute_rip] if ! resource[:redistribute_rip].nil?
    params["in-filter"] = resource[:in_filter] if ! resource[:in_filter].nil?
    params["out-filter"] = resource[:out_filter] if ! resource[:out_filter].nil?
    params["metric-default"] = resource[:metric_default] if ! resource[:metric_default].nil?
    params["metric-connected"] = resource[:metric_connected] if ! resource[:metric_connected].nil?
    params["metric-static"] = resource[:metric_static] if ! resource[:metric_static].nil?
    params["metric-bgp"] = resource[:metric_bgp] if ! resource[:metric_bgp].nil?
    params["metric-other-ospf"] = resource[:metric_ospf] if ! resource[:metric_ospf].nil?
    params["metric-rip"] = resource[:metric_rip] if ! resource[:metric_rip].nil?
    params["mpls-te-area"] = resource[:mpls_te_area] if ! resource[:mpls_te_area].nil?
    params["mpls-te-router-id"] = resource[:mpls_te_router_id] if ! resource[:mpls_te_router_id].nil?
    params["routing-table"] = resource[:routing_table] if ! resource[:routing_table].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/ospf/instance", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ospf_interface\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ospf_interface).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    ospf_interfaces = Puppet::Provider::Mikrotik_Api::get_all("/routing/ospf/interface")
    instances = ospf_interfaces.reject {|data| data['dynamic'] == 'true' }.collect { |ospf_interface| ospfInterface(ospf_interface) }
    instances
  end

  def self.ospfInterface(data)
      new(
        :ensure                 => :present,
        :name                   => data['interface'],
        :cost                   => data['cost'],
        :priority               => data['priority'],
        :authentication         => data['authentication'],
        :authentication_key     => data['authentication-key'],          
        :authentication_key_id  => data['authentication-key-id'],
        :network_type           => data['network-type'],
        :passive                => data['passive'],
        :use_bfd                => data['use-bfd']
      )
  end

  def flush
    Puppet.debug("Flushing OSPF Interface #{resource[:name]}")
      
    params = {}
    params["interface"] = resource[:name]
    params["cost"] = resource[:cost] if ! resource[:cost].nil?
    params["priority"] = resource[:priority] if ! resource[:priority].nil?
    params["authentication"] = resource[:authentication] if ! resource[:authentication].nil?
    params["authentication-key"] = resource[:authentication_key] if ! resource[:authentication_key].nil?
    params["authentication-key-id"] = resource[:authentication_key_id] if ! resource[:authentication_key_id].nil?
    params["network-type"] = resource[:network_type] if ! resource[:network_type].nil?
    params["passive"] = resource[:passive] if ! resource[:passive].nil?
    params["use-bfd"] = resource[:use_bfd] if ! resource[:use_bfd].nil?

    lookup = {}
    lookup["interface"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/ospf/interface", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ospf_network\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ospf_network).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    ospf_networks = Puppet::Provider::Mikrotik_Api::get_all("/routing/ospf/network")
    instances = ospf_networks.collect { |ospf_network| ospfNetwork(ospf_network) }    
    instances
  end
  
  def self.ospfNetwork(data)
      new(
        :ensure  => :present,
        :name    => data['network'],
        :area    => data['area'],
        :comment => data['comment'],
      )
  end

  def flush
    Puppet.debug("Flushing OSPF Network #{resource[:name]}")
      
    params = {}
    params["network"] = resource[:name]
    params["area"] = resource[:area] if ! resource[:area].nil?
    params["comment"] = resource[:comment] if ! resource[:comment].nil?

    lookup = {}
    lookup["network"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/ospf/network", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ospf_nmba_neighbor\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ospf_nmba_neighbor).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    ospf_neighbors = Puppet::Provider::Mikrotik_Api::get_all("/routing/ospf/nbma-neighbor")
    instances = ospf_neighbors.collect { |ospf_neighbor| ospfNeighbor(ospf_neighbor) }    
    instances
  end
  
  def self.ospfNeighbor(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure        => :present,
      :state         => state,
      :name          => data['address'],
      :instance      => data['instance'],
      :poll_interval => data['poll-interval'],
      :priority      => data['priority']
    )
  end

  def flush
    Puppet.debug("Flushing OSPF NMBA Neighbor #{resource[:name]}")
      
    params = {}
      
    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["address"] = resource[:name]
    params["instance"] = resource[:instance] if ! resource[:instance].nil?
    params["poll-interval"] = resource[:poll_interval] if ! resource[:poll_interval].nil?
    params["priority"] = resource[:priority] if ! resource[:priority].nil?

    lookup = {}
    lookup["address"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/routing/ospf/nbma-neighbor", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_package\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_package).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods
  
  def self.instances    
    packages = Puppet::Provider::Mikrotik_Api::get_all("/system/package")
    instances = packages.collect { |package| getPackage(package) }
    instances    
  end
  
  def self.getPackage(package)    
    if package['disabled'] == "true" and package['scheduled'] == ""
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure => :present,
      :state  => state,
      :name   => package['name']
    )
  end

  def flush
    lookup = {}
    lookup["name"] = resource[:name]

    id_list = Puppet::Provider::Mikrotik_Api::lookup_id("/system/package", lookup)
    id_list.each do |id|
      params = { ".id" => id }
      
      if @property_hash[:state] == :disabled
        Puppet.debug("Disabling Package #{resource[:name]}")
  
        result = Puppet::Provider::Mikrotik_Api::disable("/system/package", params)        
      elsif @property_hash[:state] == :enabled
        Puppet.debug("Enabling Package #{resource[:name]}")

        result = Puppet::Provider::Mikrotik_Api::enable("/system/package", params)
      end
    end

    # Reboot
    reboot(resource[:force_reboot])
  end

  def reboot(force)
    if (force)
      Puppet.info("Rebooting device to install package")
      Puppet::Provider::Mikrotik_Api::command("/system/reboot")
      sleep(60)
    else
      Puppet.warning( "Package enabling requires rebooting the device. Puppet is not allowed to reboot device without 'force_reboot => true'.")
    end
  end
end


File: /lib\puppet\provider\mikrotik_ppp_aaa\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ppp_aaa).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
      
    aaa = Puppet::Provider::Mikrotik_Api::get_all("/ppp/aaa")
    aaa.each do |data|
      object = pppAAASettings(data)
      if object != nil
        instances << object
      end
    end

    instances
  end
  
  def self.pppAAASettings(data)        
    new(
      :name           => 'aaa',
      :use_radius     => data['use-radius'],
      :accounting     => data['accounting'],
      :interim_update => data['interim-update']
    )
  end

  def flush
    Puppet.debug("Flushing PPP AAA")
    
    if (@property_hash[:name] != 'aaa') 
      raise "There is only one set of PPP AAA settings. Title (name) should be -aaa-"
    end
    
    update = {}
    update["use-radius"]     = (resource[:use_radius].to_s) if ! resource[:use_radius].nil?
    update["accounting"]     = (resource[:accounting].to_s) if ! resource[:accounting].nil?
    update["interim-update"] = resource[:interim_update] if ! resource[:interim_update].nil?
    
    result = Puppet::Provider::Mikrotik_Api::set("/ppp/aaa", update)
  end
end


File: /lib\puppet\provider\mikrotik_ppp_profile\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ppp_profile).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    profiles = Puppet::Provider::Mikrotik_Api::get_all("/ppp/profile")
    instances = profiles.collect { |profile| pppProfile(profile) }    
    instances
  end
  
  def self.pppProfile(data)    
    new(
      :ensure               => :present,
      :name                 => data['name'],
      :local_address        => data['local-address'],
      :remote_address       => data['remote-address'],
      :bridge               => data['bridge'],
      :bridge_path_cost     => data['bridge-path-cost'],
      :bridge_port_priority => data['bridge-port-priority'],
      :incoming_filter      => data['incoming-filter'],
      :outgoing_filter      => data['outgoing-filter'],        
      :address_list         => data['address-list'],
      :interface_list       => data['interface-list'],
      :dns_server           => data['dns-server'],    
      :wins_server          => data['wins-server'],
      :change_tcp_mss       => data['change-tcp-mss'],
      :use_upnp             => data['use-upnp'],
      :use_mpls             => data['use-mpls'],
      :use_compression      => data['use-compression'],
      :use_encryption       => data['use-encryption'],
      :session_timeout      => data['session-timeout'],
      :idle_timeout         => data['idle-timeout'],
      :rate_limit           => data['rate-limit'],
      :insert_queue_before  => data['insert-queue-before'],
      :parent_queue         => data['parent-queue'],
      :queue_type           => data['queue-type'],
      :only_one             => data['only-one'],
      :on_up                => data['on-up'],
      :on_down              => data['on-down']
    )
  end

  def flush
    Puppet.debug("Flushing PPP profile #{resource[:name]}")
      
    params = {}
    params["name"] = resource[:name]
    params["local-address"] = resource[:local_address] if ! resource[:local_address].nil?
    params["remote-address"] = resource[:remote_address] if ! resource[:remote_address].nil?
    params["bridge"] = resource[:bridge] if ! resource[:bridge].nil?      
    params["bridge-path-cost"] = resource[:bridge_path_cost] if ! resource[:bridge_path_cost].nil?
    params["bridge-port-priority"] = resource[:bridge_port_priority] if ! resource[:bridge_port_priority].nil?
    params["incoming-filter"] = resource[:incoming_filter] if ! resource[:incoming_filter].nil?
    params["outgoing-filter"] = resource[:outgoing_filter] if ! resource[:outgoing_filter].nil?
    params["address-list"] = resource[:address_list] if ! resource[:address_list].nil?
    params["interface-list"] = resource[:interface_list] if ! resource[:interface_list].nil?
    params["dns-server"] = resource[:dns_server] if ! resource[:dns_server].nil?
    params["wins-server"] = resource[:wins_server] if ! resource[:wins_server].nil?
    params["change-tcp-mss"] = resource[:change_tcp_mss] if ! resource[:change_tcp_mss].nil?
    params["use-upnp"] = resource[:use_upnp] if ! resource[:use_upnp].nil?
    params["use-mpls"] = resource[:use_mpls] if ! resource[:use_mpls].nil?
    params["use-compression"] = resource[:use_compression] if ! resource[:use_compression].nil?
    params["use-encryption"] = resource[:use_encryption] if ! resource[:use_encryption].nil?
    params["session-timeout"] = resource[:session_timeout] if ! resource[:session_timeout].nil?
    params["idle-timeout"] = resource[:idle_timeout] if ! resource[:idle_timeout].nil?
    params["rate-limit"] = resource[:rate_limit] if ! resource[:rate_limit].nil?
    params["insert-queue-before"] = resource[:insert_queue_before] if ! resource[:insert_queue_before].nil?
    params["parent-queue"] = resource[:parent_queue] if ! resource[:parent_queue].nil?
    params["queue-type"] = resource[:queue_type] if ! resource[:queue_type].nil?      
    params["only-one"] = resource[:only_one] if ! resource[:only_one].nil?
    params["on-up"] = resource[:on_up] if ! resource[:on_up].nil?
    params["on-down"] = resource[:on_down] if ! resource[:on_down].nil?
      
    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ppp/profile", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_ppp_secret\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ppp_secret).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik

  mk_resource_methods

  def self.instances
    secrets = Puppet::Provider::Mikrotik_Api::get_all("/ppp/secret")
    instances = secrets.collect { |secret| secretObject(secret) }
    instances
  end

  def self.secretObject(data)
    routes = data['routes'].nil? ? nil : data['routes'].split(',')

    if data['disabled'] == 'true'
      state = :disabled
    else
      state = :enabled
    end

    new(
      :ensure           => :present,
      :state            => state,
      :name             => data['name'],
      :password         => data['password'],
      :service          => data['service'],
      :caller_id        => data['caller-id'],
      :profile          => data['profile'],
      :local_address    => data['local-address'],
      :remote_address   => data['remote-address'],
      :routes           => routes,
      :limit_bytes_in   => data['limit-bytes-in'],
      :limit_bytes_out  => data['limit-bytes-out']
    )
  end

  def flush
    Puppet.debug("Flushing PPP Secret #{resource[:name]}")

    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = true
    elsif @property_hash[:state] == :enabled
      params["disabled"] = false
    end

    params["name"] = resource[:name]
    params["password"] = resource[:password] if ! resource[:password].nil?
    params["service"] = resource[:service] if ! resource[:service].nil?
    params["caller-id"] = resource[:caller_id] if ! resource[:caller_id].nil?
    params["profile"] = resource[:profile] if ! resource[:profile].nil?
    params["local-address"] = resource[:local_address] if ! resource[:local_address].nil?
    params["remote-address"] = resource[:remote_address] if ! resource[:remote_address].nil?
    params["routes"] = resource[:routes].join(',') if ! resource[:routes].nil?
    params["limit-bytes-in"] = resource[:limit_bytes_in] if ! resource[:limit_bytes_in].nil?
    params["limit-bytes-out"] = resource[:limit_bytes_out] if ! resource[:limit_bytes_out].nil?

    lookup = {}
    lookup["name"] = resource[:name]

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/ppp/secret", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_ppp_server\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_ppp_server).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik

  mk_resource_methods

  def self.instances    
    instances = []

    pptp = Puppet::Provider::Mikrotik_Api::get_all("/interface/pptp-server/server")
    pptp.each { |server| 
      instances << pppServer('pptp', server)
    }

    l2tp = Puppet::Provider::Mikrotik_Api::get_all("/interface/l2tp-server/server")
    l2tp.each { |server|
      instances << pppServer('l2tp', server)
    }

    ovpn = Puppet::Provider::Mikrotik_Api::get_all("/interface/ovpn-server/server")
    ovpn.each { |server|
      instances << pppServer('ovpn', server)
    }

    instances
  end

  def self.pppServer(type, data)
    if data['enabled'] == 'true'
      state = :enabled
    else
      state = :disabled
    end

    auth_data = data['authentication'] || data['auth'] 
    authentication = auth_data.nil? ? nil : auth_data.split(',')
    cipher = data['cipher'].nil? ? nil : data['cipher'].split(',')
    cert = (data['certificate'] == '*0' ? nil : data['certificate'])

    new(
      :ensure                     => :present,
      :name                       => type,
      :state                      => state,
      :max_mtu                    => data['max-mtu'],
      :max_mru                    => data['max-mru'],     
      :mode                       => data['mode'],     
      :mrru                       => data['mrru'],
      :netmask                    => data['netmask'],
      :mac_address                => data['mac-address'],
      :authentication             => authentication,
      :cipher                     => cipher,
      :certificate                => cert,
      :port                       => data['port'],
      :require_client_certificate => data['require-client-certificate'],
      :keepalive_timeout          => data['keepalive-timeout'],
      :default_profile            => data['default-profile'],
      :max_sessions               => data['max-sessions'],
      :use_ipsec                  => data['use-ipsec'],
      :ipsec_secret               => data['ipsec-secret'],
      :allow_fastpath             => data['allow-fastpath'],  
    )
  end

  def flush
    Puppet.debug("Flushing PPP Server #{resource[:name]}")
    
    unless %{pptp l2tp ovpn}.include?(@property_hash[:name])
      raise "PPP server should be of type PPTP or L2TP or OVPN"
    end
      
    auth_key =  case @property_hash[:name]
                when 'pptp', 'l2tp'
                  'authentication'
                when 'ovpn'
                  'auth'
                else
                  'authentication'
                end

    params = {}
    
    if @property_hash[:state] == :disabled
      params["enabled"] = false
    elsif @property_hash[:state] == :enabled
      params["enabled"] = true
    end
      
    params["max-mtu"] = resource[:max_mtu] if ! resource[:max_mtu].nil?
    params["max-mru"] = resource[:max_mru] if ! resource[:max_mru].nil?
    params["mode"] = resource[:mode] if ! resource[:mode].nil?
    params["mrru"] = resource[:mrru] if ! resource[:mrru].nil?
    params[auth_key] = resource[:authentication].join(',') if ! resource[:authentication].nil?
    params["cipher"] = resource[:cipher].join(',') if ! resource[:cipher].nil?
    params["netmask"] = resource[:netmask] if ! resource[:netmask].nil?
    params["mac-address"] = resource[:mac_address] if ! resource[:mac_address].nil?
    params["certificate"] = resource[:certificate] if ! resource[:certificate].nil?
    params["require-client-certificate"] = resource[:require_client_certificate] if ! resource[:require_client_certificate].nil?
    params["port"] = resource[:port] if ! resource[:port].nil?
    params["keepalive-timeout"] = resource[:keepalive_timeout] if ! resource[:keepalive_timeout].nil?
    params["default-profile"] = resource[:default_profile] if ! resource[:default_profile].nil?
    params["max-sessions"] = resource[:max_sessions] if ! resource[:max_sessions].nil?
    params["use-ipsec"] = resource[:use_ipsec] if ! resource[:use_ipsec].nil?
    params["ipsec-secret"] = resource[:ipsec_secret] if ! resource[:ipsec_secret].nil?
    params["allow-fastpath"] = resource[:allow_fastpath] if ! resource[:allow_fastpath].nil?
    
    Puppet.debug("PPP Server: #{resource[:name]} - Params: #{params.inspect}")

    if (@property_hash[:name] == 'pptp') 
      result = Puppet::Provider::Mikrotik_Api::set("/interface/pptp-server/server", params)
    end
    if (@property_hash[:name] == 'l2tp') 
      result = Puppet::Provider::Mikrotik_Api::set("/interface/l2tp-server/server", params)
    end
    if (@property_hash[:name] == 'ovpn')
      result = Puppet::Provider::Mikrotik_Api::set("/interface/ovpn-server/server", params)
    end
  end  
end


File: /lib\puppet\provider\mikrotik_radius_server\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_radius_server).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik

  mk_resource_methods

  def self.instances
    servers = Puppet::Provider::Mikrotik_Api::get_all("/radius")

    instances = []
    servers.each { |server|
      obj = radiusServer(server)
      if obj != nil
        instances << obj
      end
    }
    instances
  end

  def self.radiusServer(data)
    if ! data['comment'].nil?
      services = data['service'].split(',')
      
      new(
        :ensure            => :present,
        :name              => data['comment'],
        :address           => data['address'],
        :services          => services,
        :called_id         => data['called-id'],
        :domain            => data['domain'],
        :secret            => data['secret'],
        :auth_port         => data['authentication-port'],
        :acct_port         => data['accounting-port'],
        :timeout           => data['timeout'],
        :accounting_backup => data['accounting-backup'],
        :realm             => data['realm'],
        :src_address       => data['src-address']
      )
    end
  end

  def flush
    Puppet.debug("Flushing RADIUS Server #{resource[:name]}")
      
    params = {}
    params["comment"] = resource[:name]
    params["address"] = resource[:address] if ! resource[:address].nil?
    if ! resource[:services].nil?
      params["service"] = resource[:services].join(',')
    end
    # TODO
    params["called-id"] = resource[:called_id] if ! resource[:called_id].nil?
    params["domain"] = resource[:domain] if ! resource[:domain].nil?
    params["secret"] = resource[:secret] if ! resource[:secret].nil?
    params["authentication-port"] = resource[:auth_port] if ! resource[:auth_port].nil?
    params["accounting-port"] = resource[:acct_port] if ! resource[:acct_port].nil?

    params["timeout"] = resource[:timeout] if ! resource[:timeout].nil?
    params["accounting-backup"] = resource[:accounting_backup] if ! resource[:accounting_backup].nil?
    params["realm"] = resource[:realm] if ! resource[:realm].nil?
    params["src-address"] = resource[:src_address] if ! resource[:src_address].nil?

    lookup = {}
    lookup["comment"] = resource[:name]

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/radius", params, lookup)
  end
end


File: /lib\puppet\provider\mikrotik_romon\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_romon).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances      
    romon = Puppet::Provider::Mikrotik_Api::get_all("/tool/romon")  
    instances = romon.collect { |data| romonSettings(data) }
    instances
  end
  
  def self.romonSettings(data)
    if data['enabled'] == "false"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure  => :present,
      :state   => state,
      :name    => 'romon',
      :id      => data['id'],
      :secrets => data['secrets'].split(',')
    )
  end

  def flush
    Puppet.debug("Flushing RoMON")
    
    if (@property_hash[:name] != 'romon') 
      raise "There is only one set of RoMON settings. Title (name) should be -romon-"
    end

    update = {}
      
    if @property_hash[:state] == :disabled
      update["enabled"] = false
    elsif @property_hash[:state] == :enabled
      update["enabled"] = true
    end 
    
    update["id"] = resource[:id] if ! resource[:id].nil?
    update["secrets"] = resource[:secrets].join(',') if ! resource[:secrets].nil?

    result = Puppet::Provider::Mikrotik_Api::set("/tool/romon", update)
  end
end


File: /lib\puppet\provider\mikrotik_romon_port\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_romon_port).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    interfaces = Puppet::Provider::Mikrotik_Api::get_all("/tool/romon/port")
    networks = interfaces.collect { |interface| romonPort(interface) }
    networks
  end
  
  def self.romonPort(data)     
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end   
    
    new(
      :ensure   => :present,
      :state    => state,
      :name     => data['interface'],
      :forbid   => data['forbid'],# TODO
      :secrets  => data['secrets'].split(','),
      :cost     => data['cost']
    )
  end

  def flush
    Puppet.info("Flushing RoMON Port #{resource[:name]}")
    
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
    
    params["interface"] = resource[:name]
    params["forbid"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:forbid]) if ! resource[:forbid].nil?
    params["secrets"] = resource[:secrets].join(',') if ! resource[:secrets].nil?
    params["cost"] = resource[:cost]

    lookup = {}
    lookup["interface"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/tool/romon/port", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_routing_filter\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_routing_filter).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances   
    instances = []
      
    filters = Puppet::Provider::Mikrotik_Api::get_all("/routing/filter")
    filters.each do |filter|
      object = routingFilter(filter, filters)
      if object != nil
        instances << object
      end
    end
    
    instances
  end

  def self.routingFilter(data, all_filters)
    if data['comment'] != nil
      #Puppet.debug("Routing filter: #{data.inspect}")

      if data['disabled'] == "true"
        state = :disabled
      else
        state = :enabled
      end

      chain_order = getChainOrder(data['.id'], data['chain'], all_filters)
      
      new(
        :ensure                 => :present,
        :state                  => state,
        :name                   => data['comment'],
        :chain                  => data['chain'],
        :chain_order            => chain_order.to_s,
        :prefix                 => data['prefix'],
        :prefix_length          => data['prefix-length'],
        :match_chain            => data['match-chain'],
        :protocols              => data['protocol'].nil? ? nil : data['protocol'].split(','),
        :distance               => data['distance'],
        :scope                  => data['scope'],
        :target_scope           => data['target-scope'],
        :pref_src               => data['pref-src'],
        :routing_mark           => data['routing-mark'],
        :route_comment          => data['route-comment'],
        :route_tag              => data['route-tag'],
        :route_targets          => data['route-target'].nil? ? nil : data['route-target'].split(','),
        :sites_of_origin        => data['site-of-origin'].nil? ? nil : data['site-of-origin'].split(','),
        :address_families       => data['address-family'].nil? ? nil : data['address-family'].split(','),
        :ospf_type              => data['ospf-type'],
        :invert_match           => data['invert-match'],
        :bgp_as_path            => data['bgp-as-path'],
        :bgp_as_path_length     => data['bgp-as-path-length'],
        :bgp_weight             => data['bgp-weight'],
        :bgp_local_pref         => data['bgp-local-pref'],
        :bgp_med                => data['bgp-med'],
        :bgp_atomic_aggregate   => data['bgp-atomic-aggregate'],
        :bgp_origins            => data['bgp-origin'].nil? ? nil : data['bgp-origin'].split(','),
        :locally_originated_bgp => data['locally-originated-bgp'],
        :bgp_communities        => data['bgp-communities'].nil? ? nil : data['bgp-communities'].split(','),
        :action                 => data['action'],
        :jump_target            => data['jump-target'],
        :set_distance           => data['set-distance'],
        :set_scope              => data['set-scope'],
        :set_target_scope       => data['set-target-scope'],
        :set_pref_src           => data['set-pref-src'],
        :set_in_nexthops        => data['set-in-nexthop'].nil? ? nil : data['set-in-nexthop'].split(','),
        :set_in_nexthops_direct => data['set-in-nexthop-direct'].nil? ? nil : data['set-in-nexthop-direct'].split(','),
        :set_out_nexthop        => data['set-out-nexthop'],
        :set_routing_mark       => data['set-routing-mark'],
        :set_route_comment      => data['set-route-comment'],
        :set_check_gateway      => data['set-check-gateway'],
        :set_disabled           => data['set-disabled'],
        :set_type               => data['set-type'],
        :set_route_tag          => data['set-route-tag'],
        :set_use_te_nexthop     => data['set-use-te-nexthop'],
        :set_route_targets      => data['set-route-target'].nil? ? nil : data['set-route-target'].split(','),
        :append_route_targets   => data['append-route-target'].nil? ? nil : data['append-route-target'].split(','),
        :set_site_of_origin     => data['set-site-of-origin'].nil? ? nil : data['set-site-of-origin'].split(','),
        :set_bgp_weight         => data['set-bgp-weight'],
        :set_bgp_local_pref     => data['set-bgp-local-pref'],
        :set_bgp_prepend        => data['set-bgp-prepend'],
        :set_bgp_prepend_path   => data['set-bgp-prepend-path'].nil? ? nil : data['set-bgp-prepend-path'].split(','),
        :set_bgp_med            => data['set-bgp-med'],
        :set_bgp_communities    => data['set-bgp-communities'].nil? ? nil : data['set-bgp-communities'].split(','),
        :append_bgp_communities => data['append-bgp-communities'].nil? ? nil : data['append-bgp-communities'].split(',')
      )
    end
  end

  def flush
    Puppet.debug("Flushing routing filter #{resource[:name]}")

    unless @property_flush[:ensure] == :absent
      if resource[:chain].nil?
        raise "Chain is a required parameter."
      end
    end

    params = {}      

    if @property_hash[:state] == :disabled
      params["disabled"] = true
    elsif @property_hash[:state] == :enabled
      params["disabled"] = false
    end
    
    if !resource[:chain_order].nil?
      all_filters = Puppet::Provider::Mikrotik_Api::get_all("/routing/filter")
      ids = self.class.getChainIds(resource[:chain], all_filters)
      
      if @property_flush[:ensure] == :present
        unless resource[:chain_order] > ids.length          
          filter_id_after = ids[resource[:chain_order].to_i - 1]# index starts at 0, order starts at 1
          params["place-before"] = filter_id_after
        end
      end
    end
      
    params["comment"] = resource[:name]
    params["chain"] = resource[:chain]    
    params["prefix"] = resource[:prefix] if !resource[:prefix].nil?
    params["prefix-length"] = resource[:prefix_length] if !resource[:prefix_length].nil?
    params["match-chain"] = resource[:match_chain] if !resource[:match_chain].nil?
    params["protocol"] = resource[:protocols].join(',') if !resource[:protocols].nil?      
    params["distance"] = resource[:distance] if !resource[:distance].nil?
    params["scope"] = resource[:scope] if !resource[:scope].nil?
    params["target-scope"] = resource[:target_scope] if !resource[:target_scope].nil?
    params["pref-src"] = resource[:pref_src] if !resource[:pref_src].nil?
    params["routing-mark"] = resource[:routing_mark] if !resource[:routing_mark].nil?
    params["route-comment"] = resource[:route_comment] if !resource[:route_comment].nil?
    params["route-tag"] = resource[:route_tag] if !resource[:route_tag].nil?
    params["route-target"] = resource[:route_targets].join(',') if !resource[:route_targets].nil?
    params["site-of-origin"] = resource[:sites_of_origin].join(',') if !resource[:sites_of_origin].nil?
    params["address-family"] = resource[:address_families].join(',') if !resource[:address_families].nil?
    params["ospf-type"] = resource[:ospf_type] if !resource[:ospf_type].nil?
    params["invert-match"] = resource[:invert_match] if !resource[:invert_match].nil?
    params["bgp-as-path"] = resource[:bgp_as_path] if !resource[:bgp_as_path].nil?
    params["bgp-as-path-length"] = resource[:bgp_as_path_length] if !resource[:bgp_as_path_length].nil?
    params["bgp-weight"] = resource[:bgp_weight] if !resource[:bgp_weight].nil?
    params["bgp-local-pref"] = resource[:bgp_local_pref] if !resource[:bgp_local_pref].nil?
    params["bgp-med"] = resource[:bgp_med] if !resource[:bgp_med].nil?
    params["bgp-atomic-aggregate"] = resource[:bgp_atomic_aggregate] if !resource[:bgp_atomic_aggregate].nil?
    params["bgp-origin"] = resource[:bgp_origins].join(',') if !resource[:bgp_origins].nil?
    params["locally-originated-bgp"] = resource[:locally_originated_bgp] if !resource[:locally_originated_bgp].nil?
    params["bgp-communities"] = resource[:bgp_communities].join(',') if !resource[:bgp_communities].nil?
    params["action"] = resource[:action] if !resource[:action].nil?
    params["jump-target"] = resource[:jump_target] if !resource[:jump_target].nil?
    params["set-distance"] = resource[:set_distance] if !resource[:set_distance].nil?
    params["set-scope"] = resource[:set_scope] if !resource[:set_scope].nil?
    params["set-target-scope"] = resource[:set_target_scope] if !resource[:set_target_scope].nil?
    params["set-pref-src"] = resource[:set_pref_src] if !resource[:set_pref_src].nil?
    params["set-in-nexthop"] = resource[:set_in_nexthops].join(',') if !resource[:set_in_nexthops].nil?
    params["set-in-nexthop-direct"] = resource[:set_in_nexthops_direct].join(',') if !resource[:set_in_nexthops_direct].nil?
    params["set-out-nexthop"] = resource[:set_out_nexthop] if !resource[:set_out_nexthop].nil?
    params["set-routing-mark"] = resource[:set_routing_mark] if !resource[:set_routing_mark].nil?
    params["set-route-comment"] = resource[:set_route_comment] if !resource[:set_route_comment].nil?
    params["set-check-gateway"] = resource[:set_check_gateway] if !resource[:set_check_gateway].nil?
    params["set-disabled"] = resource[:set_disabled] if !resource[:set_disabled].nil?
    params["set-type"] = resource[:set_type] if !resource[:set_type].nil?
    params["set-route-tag"] = resource[:set_route_tag] if !resource[:set_route_tag].nil?
    params["set-use-te-nexthop"] = resource[:set_use_te_nexthop] if !resource[:set_use_te_nexthop].nil?
    params["set-route-targets"] = resource[:set_route_targets].join(',') if !resource[:set_route_targets].nil?
    params["append-route-targets"] = resource[:append_route_targets].join(',') if !resource[:append_route_targets].nil?
    params["set-site-of-origin"] = resource[:set_site_of_origin].join(',') if !resource[:set_site_of_origin].nil?
    params["set-bgp-weight"] = resource[:set_bgp_weight] if !resource[:set_bgp_weight].nil?
    params["set-bgp-local-pref"] = resource[:set_bgp_local_pref] if !resource[:set_bgp_local_pref].nil?
    params["set-bgp-prepend"] = resource[:set_bgp_prepend] if !resource[:set_bgp_prepend].nil?
    params["set-bgp-prepend-path"] = resource[:set_bgp_prepend_path].join(',') if !resource[:set_bgp_prepend_path].nil?
    params["set-bgp-med"] = resource[:set_bgp_med] if !resource[:set_bgp_med].nil?
    params["set-bgp-communities"] = resource[:set_bgp_communities].join(',') if !resource[:set_bgp_communities].nil?
    params["append-bgp-communities"] = resource[:append_bgp_communities].join(',') if !resource[:append_bgp_communities].nil?

    lookup = {}
    lookup["comment"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")
    
    simple_flush("/routing/filter", params, lookup)
        
    if !resource[:chain_order].nil?
      if @property_flush.empty?
        id_list = Puppet::Provider::Mikrotik_Api::lookup_id("/routing/filter", lookup)
        id_list.each do |id|
          chain_order = self.class.getChainOrder(id, resource[:chain], all_filters)
          if resource[:chain_order].to_i != chain_order
            self.class.moveFilter(id, resource[:chain], chain_order, resource[:chain_order].to_i, all_filters)
          end
        end
      end
    end
  end
    
  def self.getChainOrder(lookup_id, lookup_chain, all_filters)    
    ids = getChainIds(lookup_chain, all_filters)
    
    chain_order = 1
    ids.each do |id|
      if id == lookup_id
         return chain_order
      end        
     
      chain_order = chain_order + 1
    end
  end
  
  def self.getChainIds(lookup_chain, all_filters)
    ids = all_filters.collect do |filter|
      if filter['chain'] == lookup_chain
         filter['.id']
      end
    end
    
    ids.compact
  end
    
  def self.moveFilter(filter_id, lookup_chain, old_chain_order, new_chain_order, all_filters)
    Puppet.debug("Moving filter #{filter_id} from position #{old_chain_order} to position #{new_chain_order} in chain #{lookup_chain}.")
    
    if new_chain_order == old_chain_order
      return
    end

    if new_chain_order > old_chain_order
      lookup_order = new_chain_order + 1
    else
      lookup_order = new_chain_order
    end

    destination = nil
    chain_pos = 0

    all_filters.each do |filter|
      if filter['chain'] == lookup_chain
        chain_pos = chain_pos + 1         
      end
      
      if chain_pos == new_chain_order
        destination = filter['.id']  
      end
      
      if chain_pos == lookup_order
        destination = filter['.id']   
        break
      end
    end

    if filter_id == destination
      return
    end

    move_params = {}
    move_params["numbers"] = filter_id
    move_params["destination"] = destination if destination != nil
    result = Puppet::Provider::Mikrotik_Api::move("/routing/filter", move_params)
  end
end


File: /lib\puppet\provider\mikrotik_schedule\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_schedule).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    schedules = Puppet::Provider::Mikrotik_Api::get_all("/system/scheduler")
    instances = schedules.collect { |schedule| systemSchedule(schedule) }    
    instances
  end
  
  def self.systemSchedule(data)            
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure     => :present,
      :state      => state,
      :name       => data['name'],
      :start_date => data['start-date'],
      :start_time => data['start-time'],
      :interval   => data['interval'],
      :policies   => data['policy'].split(','), 
      :on_event   => data['on-event']
    )
  end

  def flush
    Puppet.debug("Flushing Scheduler #{resource[:name]}")
    
    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end
      
    params["name"] = resource[:name]
    params["start-date"] = resource[:start_date] if ! resource[:start_date].nil?
    params["start-time"] = resource[:start_time] if ! resource[:start_time].nil?
    params["interval"] = resource[:interval] if ! resource[:interval].nil?      
    params["policy"] = resource[:policies].join(',') if ! resource[:policies].nil?
    params["on-event"] = resource[:on_event] if ! resource[:on_event].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/system/scheduler", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_script\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_script).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    scripts = Puppet::Provider::Mikrotik_Api::get_all("/system/script")
    instances = scripts.collect { |script| systemScript(script) }    
    instances
  end
  
  def self.systemScript(data)        
    new(
      :ensure   => :present,
      :name     => data['name'],
      :policies => data['policy'].split(','),  
      :source   => data['source']
    )
  end

  def flush
    Puppet.info("Flushing Script #{resource[:name]}")
    
    params = {}
    params["name"] = resource[:name]
    params["policy"] = resource[:policies].join(',') if ! resource[:policies].nil?
    params["source"] = resource[:source] if ! resource[:source].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/system/script", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_snmp\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_snmp).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances      
    snmp = Puppet::Provider::Mikrotik_Api::get_all("/snmp")  
    instances = snmp.collect { |data| snmpSettings(data) }
    instances
  end
  
  def self.snmpSettings(data)
    if data['enabled'] == "false"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure          => :present,
      :state           => state,
      :name            => 'snmp',
      :contact         => data['contact'],
      :location        => data['location'],
      :trap_version    => data['trap-version'],
      :trap_community  => data['trap-community'],
      :trap_generators => data['trap-generators'].split(','),
      :trap_targets    => data['trap-target'].split(',')
    )
  end

  def flush
    Puppet.debug("Flushing SNMP")
    
    if (@property_hash[:name] != 'snmp') 
      raise "There is only one set of SNMP settings. Title (name) should be -snmp-"
    end

    update = {}
      
    if @property_hash[:state] == :disabled
      update["enabled"] = false
    elsif @property_hash[:state] == :enabled
      update["enabled"] = true
    end 
    
    update["contact"] = resource[:contact] if ! resource[:contact].nil?
    update["location"] = resource[:location] if ! resource[:location].nil?
    update["trap-version"] = resource[:trap_version] if ! resource[:trap_version].nil?
    update["trap-community"] = resource[:trap_community] if ! resource[:trap_community].nil?
    update["trap-generators"] = resource[:trap_generators].join(',') if ! resource[:trap_generators].nil?
    update["trap-target"] = resource[:trap_targets].join(',') if ! resource[:trap_targets].nil?

    result = Puppet::Provider::Mikrotik_Api::set("/snmp", update)
  end
end


File: /lib\puppet\provider\mikrotik_snmp_community\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_snmp_community).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    communities = Puppet::Provider::Mikrotik_Api::get_all("/snmp/community")
    Puppet.debug("/snmp/community: #{communities.inspect}")
    instances = communities.collect { |community| snmpCommunity(community) }
    
    instances
  end
  
  def self.snmpCommunity(data)
    addresses = data['addresses'].nil? ? nil : data['addresses'].split(',')
    
    new(
      :ensure       => :present,
      :name         => data['name'],
      :read_access  => data['read-access'],
      :write_access => data['write-access'],
      :addresses    => addresses
    )
  end

  def flush
    Puppet.debug("Flushing SNMP Community #{resource[:name]}")
      
    params = {}
    params["name"] = resource[:name]
    params["read-access"] = resource[:read_access] if ! resource[:read_access].nil?
    params["write-access"] = resource[:write_access] if ! resource[:write_access].nil?
    params["addresses"] = resource[:addresses].join(',') if ! resource[:addresses].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/snmp/community", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_system\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_system).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    system_identity_name = ""
    system_clock_timzeone = ""
    ntp_client_data = []
    
    identity = Puppet::Provider::Mikrotik_Api::get_all("/system/identity")
    identity.each do |data|
      system_identity_name = data['name']
    end

    clock = Puppet::Provider::Mikrotik_Api::get_all("/system/clock")
    clock.each do |data|
      system_clock_timzeone = data['time-zone-name']
    end

    ntp_client = Puppet::Provider::Mikrotik_Api::get_all("/system/ntp/client")
    ntp_client.each do |data|
      ntp_client_data = data
    end
    
    system = new(
      :name          => 'system',
      :identity      => system_identity_name,
      :timezone      => system_clock_timzeone,
      :ntp_enabled   => ntp_client_data['enabled'],
      :ntp_primary   => ntp_client_data['primary-ntp'],
      :ntp_secondary => ntp_client_data['secondary-ntp']
    )
    instances = [system]
    
    instances
  end
  
  def flush
    Puppet.debug("Flushing System Settings")
    
    if (@property_hash[:name] != 'system') 
      raise "There is only one set of System settings. Title (name) should be -system-"
    end
    
    identity = {}
    identity["name"] = resource[:identity] if ! resource[:identity].nil?
    result = Puppet::Provider::Mikrotik_Api::set("/system/identity", identity)

    clock = {}
    clock["time-zone-name"] = resource[:timezone] if ! resource[:timezone].nil?
    result = Puppet::Provider::Mikrotik_Api::set("/system/clock", clock)
    
    ntp_client = {}
    ntp_client["enabled"] = resource[:ntp_enabled] if ! resource[:ntp_enabled].nil?
    ntp_client["primary-ntp"] = resource[:ntp_primary] if ! resource[:ntp_primary].nil?
    ntp_client["secondary-ntp"] = resource[:ntp_secondary] if ! resource[:ntp_secondary].nil?

    result = Puppet::Provider::Mikrotik_Api::set("/system/ntp/client", ntp_client)
  end
end


File: /lib\puppet\provider\mikrotik_tool_email\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_tool_email).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
      
    email = Puppet::Provider::Mikrotik_Api::get_all("/tool/e-mail")
    email.each do |data|
      object = toolEmail(data)
      if object != nil
        instances << object
      end
    end

    instances
  end
  
  def self.toolEmail(data)
    new(
      :name            => 'email',
      :server          => data['address'],
      :port            => data['port'],
      :username        => data['user'],
      :password        => data['password'],
      :from_address    => data['from'],
      :enable_starttls => convertYesNoToBool(data['start-tls']).to_s
    )
  end

  def flush
    Puppet.debug("Flushing Tool E-mail")
    
    if (@property_hash[:name] != 'email') 
      raise "There is only one set of E-Mail Tool settings. Title (name) should be -email-"
    end
    
    update = {}
    update["address"] = resource[:server] if ! resource[:server].nil?
    update["port"] = resource[:port] if ! resource[:port].nil?
    update["user"] = resource[:username] if ! resource[:username].nil?
    update["password"] = resource[:password] if ! resource[:password].nil?
    update["from"] = resource[:from_address] if ! resource[:from_address].nil?
    update["start-tls"] = Puppet::Provider::Mikrotik_Api::convertBoolToYesNo(resource[:enable_starttls]) if ! resource[:enable_starttls].nil?
    
    result = Puppet::Provider::Mikrotik_Api::set("/tool/e-mail", update)
  end
end

File: /lib\puppet\provider\mikrotik_tool_netwatch\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_tool_netwatch).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    watches = Puppet::Provider::Mikrotik_Api::get_all("/tool/netwatch")
    instances = watches.collect { |watch| netwatchCheck(watch) }    
    instances
  end
  
  def self.netwatchCheck(data)
    if data['disabled'] == "true"
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure      => :present,
      :state       => state,
      :name        => data['host'],
      :interval    => data['interval'],
      :timeout     => data['timeout'],
      :down_script => data['down-script'],
      :up_script   => data['up-script'],
      :comment     => data['comment']        
    )
  end

  def flush
    Puppet.debug("Flushing Netwatch check #{resource[:name]}")

    params = {}

    if @property_hash[:state] == :disabled
      params["disabled"] = 'yes'
    elsif @property_hash[:state] == :enabled
      params["disabled"] = 'no'
    end

    params["host"]   = resource[:name]
    params["interval"] = resource[:interval] if ! resource[:interval].nil?
    params["timeout"] = resource[:timeout] if ! resource[:timeout].nil?
    params["down-script"] = resource[:down_script] if ! resource[:down_script].nil?
    params["up-script"] = resource[:up_script] if ! resource[:up_script].nil?
    params["comment"] = resource[:comment] if ! resource[:comment].nil?

    lookup = {}
    lookup["host"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/tool/netwatch", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_upgrade\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_upgrade).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods
  
  def exists?
    [:present, :installed, :downloaded].include?(@property_hash[:ensure]) 
  end
  
  def self.instances
    Puppet::Provider::Mikrotik_Api::command("/system/upgrade/refresh")
    
    sleep(10)
    
    packages = Puppet::Provider::Mikrotik_Api::get_all("/system/upgrade")
    # Puppet.debug("/system/upgrade: #{packages.inspect}")

    instances = packages.collect { |package| 
      if package['name'] =~ /routeros-.*/
        getPackage(package)  
      end
    }
    instances    
  end
  
  def self.getPackage(package)
    new(
      :ensure => :present,
      :name   => package['version'],
      :state  => package['status'].to_sym
    )
  end

  def flush
    Puppet.debug("Upgrading Firmware to #{resource[:name]}")

    # Standard features that won't work here
    if @property_flush[:ensure] == :present and @original_values.empty?
      raise "Firmware #{resource[:name]} is not available from auto upgrade source!"      
    end
    
    if @property_flush[:ensure] == :absent
        raise "It is not possible to remove firmware from auto upgrade sources!"      
    end

    # Download Only
    if @property_hash[:state] == :downloaded
      if @original_values[:state] == :installed
        Puppet.debug("Get State: "+getState)
        Puppet.warning("Firmware #{resource[:name]} is already installed!")
     end         
      
      if @original_values[:state] == :available
        download(resource[:name])        
      end  
    end
    
    # Reboot
    if @property_hash[:state] == :installed
      if @original_values[:state] == :available
        download(resource[:name])        
        reboot(resource[:force_reboot])
      end

      if @original_values[:state] == :downloaded
        reboot(resource[:force_reboot])
      end
    end
  end

  def download(version)
    Puppet.info("Downloading firmware #{version}")
    
    packages = Puppet::Provider::Mikrotik_Api::get_all("/system/upgrade")
    packages.each { |package| 
      if package['name'] =~ /routeros-.*/ and package['version'] == version    
        params = {}
        params[".id"] = package['.id']
            
        Puppet::Provider::Mikrotik_Api::command("/system/upgrade/download", params)
          
        downloading(version)
      end
    }
  end
  
  def downloading(version)
    downloading = true
    
    while (downloading) do
      downloading = false
      
      packages = Puppet::Provider::Mikrotik_Api::get_all("/system/upgrade")
      packages.each { |package| 
        if package['name'] =~ /routeros-.*/ and package['version'] == version
          if package['status'] == 'downloading'
            Puppet.debug("Firmware download is #{package['completed']}% completed. Sleeping for 5 seconds")  
                      
            downloading = true
            
            sleep(5)
          end
        end
      }
    end
  end
  
  def reboot(force)
    if (force)
      Puppet.info("Rebooting device to install firmware")

      Puppet::Provider::Mikrotik_Api::command("/system/reboot")
      sleep(60)
    else
      Puppet.warning( "Firmware installation requires rebooting the device. Puppet is not allowed to reboot device without 'force_reboot => true'.")
    end
  end
end

File: /lib\puppet\provider\mikrotik_upgrade_source\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_upgrade_source).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    sources = Puppet::Provider::Mikrotik_Api::get_all("/system/upgrade/upgrade-package-source")
    #Puppet.debug("/system/upgrade/upgrade-package-source: #{sources.inspect}")
    instances = sources.collect { |source| upgradeSource(source) }
    
    instances
  end
  
  def self.upgradeSource(source)    
    new(
      :ensure   => :present,
      :name     => source['address'],
      :username => source['user']
    )
  end

  def flush
    #Puppet.debug("Flushing Upgrade Source #{resource[:name]}")
      
    params = {}
    params["address"] = resource[:name]
    params["user"] = resource[:username] if ! resource[:username].nil?

    # Password can not be managed once created !
    if @property_flush[:ensure] == :present
      params["password"] = resource[:password] if ! resource[:password].nil?
    end
    
    lookup = {}
    lookup["address"] = resource[:name]
    
    #Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/system/upgrade/upgrade-package-source", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_user\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_user).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    users = Puppet::Provider::Mikrotik_Api::get_all("/user")
    instances = users.collect { |user| userObject(user) }    
    instances
  end
  
  def self.userObject(data)
    addresses = data['address'].nil? ? nil : data['address'].split(',')

    if data['disabled'] == 'true'
      state = :disabled
    else
      state = :enabled
    end
    
    new(
      :ensure    => :present,
      :state     => state,
      :name      => data['name'],
      :group     => data['group'],
      :addresses => addresses
    )
  end

  def flush
    Puppet.debug("Flushing User #{resource[:name]}")
      
    params = {}
        
    if @property_hash[:state] == :disabled
      params["disabled"] = true
    elsif @property_hash[:state] == :enabled
      params["disabled"] = false
    end
    
    params["name"] = resource[:name]
    params["group"] = resource[:group] if ! resource[:group].nil?
    params["address"] = resource[:addresses].join(',') if ! resource[:addresses].nil?
    params["password"] = resource[:password] if ! resource[:password].nil?
      
    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/user", params, lookup)
  end  
end


File: /lib\puppet\provider\mikrotik_user_aaa\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_user_aaa).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    instances = []
      
    aaa = Puppet::Provider::Mikrotik_Api::get_all("/user/aaa")
    aaa.each do |data|
      object = userAAASettings(data)
      if object != nil
        instances << object
      end
    end

    instances
  end
  
  def self.userAAASettings(data)        
    new(
      :name           => 'aaa',
      :use_radius     => data['use-radius'],
      :accounting     => data['accounting'],
      :interim_update => data['interim-update'],
      :default_group  => data['default-group'],
      :exclude_groups => data['exclude-groups'].split(',')
    )
  end

  def flush
    Puppet.debug("Flushing User AAA")
    
    if (@property_hash[:name] != 'aaa') 
      raise "There is only one set of User AAA settings. Title (name) should be -aaa-"
    end
    
    update = {}
    update["use-radius"]     = (resource[:use_radius].to_s) if ! resource[:use_radius].nil?
    update["accounting"]     = (resource[:accounting].to_s) if ! resource[:accounting].nil?
    update["interim-update"] = resource[:interim_update] if ! resource[:interim_update].nil?
    update["default-group"]  = resource[:default_group] if ! resource[:default_group].nil?
    update["exclude-groups"] = resource[:exclude_groups].join(",") if ! resource[:exclude_groups].nil?
    
    result = Puppet::Provider::Mikrotik_Api::set("/user/aaa", update)
  end
end


File: /lib\puppet\provider\mikrotik_user_group\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_user_group).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances    
    user_groups = Puppet::Provider::Mikrotik_Api::get_all("/user/group")
    instances = user_groups.collect { |user_group| userGroup(user_group) }    
    instances
  end
  
  def self.userGroup(data)
    fullpolicy = data['policy'].split(',')
    policy = fullpolicy.delete_if { |permission| permission.start_with?('!') }
    
    new(
      :ensure => :present,
      :name   => data['name'],
      :skin   => data['skin'],
      :policy => policy
    )
  end

  def flush
    Puppet.debug("Flushing User Group #{resource[:name]}")
      
    params = {}
    params["name"] = resource[:name]
    params["skin"] = resource[:skin] if ! resource[:skin].nil?
    params["policy"] = resource[:policy].join(',') if ! resource[:policy].nil?

    lookup = {}
    lookup["name"] = resource[:name]
    
    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    simple_flush("/user/group", params, lookup)
  end  
end

File: /lib\puppet\provider\mikrotik_user_sshkey\mikrotik_api.rb
require_relative '../mikrotik_api'

Puppet::Type.type(:mikrotik_user_sshkey).provide(:mikrotik_api, :parent => Puppet::Provider::Mikrotik_Api) do
  confine :feature => :mtik
  
  mk_resource_methods

  def self.instances
    ssh_keys = Puppet::Provider::Mikrotik_Api::get_all("/user/ssh-keys")
    instances = ssh_keys.collect { |ssh_key| sshKey(ssh_key) }
    instances
  end

  def self.sshKey(data)
    new(
      :ensure => :present,
      :name   => data['name']
    )
  end

  def flush
    Puppet.debug("Flushing User SSH Key #{resource[:name]}")

    params = {}
    params["user"] = resource[:name]
    params["public-key-file"] = 'TODO'

    lookup = {}
    lookup["name"] = resource[:name]

    Puppet.debug("Params: #{params.inspect} - Lookup: #{lookup.inspect}")

    # TODO - transfer file and import...
  end  
end


File: /lib\puppet\type\mikrotik_address_list.rb
Puppet::Type.newtype(:mikrotik_address_list) do  
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end

  newparam(:name) do
    desc 'The address list name'
    isnamevar
  end

  newproperty(:addresses, :array_matching => :all) do
    desc 'The IP addresses assigned to the list'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
end


File: /lib\puppet\type\mikrotik_bgp_aggregate.rb
Puppet::Type.newtype(:mikrotik_bgp_aggregate) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Network (CIDR IP) to aggregate'
    isnamevar
  end
  
  newproperty(:instance) do
    desc 'The BGP Instance (AS).'
  end

  newproperty(:summary_only) do
    desc 'Whether to supress smaller networks that belong to this aggregate.'
    newvalues(true, false)
  end
    
  newproperty(:inherit_attributes) do
    desc 'Whether the aggregate should use attributes from aggregated networks.'
    newvalues(true, false)
  end

  newproperty(:include_igp) do
    desc 'Whether to include IGP networks.'
    newvalues(true, false)
  end
  
  newproperty(:attribute_filter) do
    desc 'Routing filters to use for setting attributes.'
  end
  
  newproperty(:suppress_filter) do
    desc 'Routing filters to use for supressing routes.'
  end

  newproperty(:advertise_filter) do
    desc 'Routing filters to use for advertisements.'
  end  
end


File: /lib\puppet\type\mikrotik_bgp_instance.rb
Puppet::Type.newtype(:mikrotik_bgp_instance) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'BGP Instance name'
    isnamevar
  end
  
  newproperty(:as) do
    desc 'The Autonomous System (AS) Number.'
  end

  newproperty(:router_id) do
    desc 'The Router ID.'
  end
    
  newproperty(:redistribute_connected) do
    desc 'Whether to redistribute connected routes to BGP.'
    newvalues(true, false)
  end

  newproperty(:redistribute_static) do
    desc 'Whether to redistribute static routes to BGP.'
    newvalues(true, false)
  end
  
  newproperty(:redistribute_ospf) do
    desc 'Whether to redistribute OSPF routes to BGP.'
    newvalues(true, false)
  end
  
  newproperty(:redistribute_bgp) do
    desc 'Whether to redistribute BGP routes from other instances to BGP.'
    newvalues(true, false)
  end

  newproperty(:out_filter) do
    desc 'The output filter applying to all peers on this instance.'
  end

  newproperty(:client_to_client_reflection) do
    desc 'Whether to enable Client-to-Client Reflection.'
    newvalues(true, false)
  end

  newproperty(:routing_table) do
    desc 'The routing table this instance belongs to.'
  end
end


File: /lib\puppet\type\mikrotik_bgp_instance_vrf.rb
Puppet::Type.newtype(:mikrotik_bgp_instance_vrf) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
    
  newparam(:name) do
    desc 'The routing mark / VRF to inject into the instance.'
    isnamevar
  end

  newparam(:instance) do
    desc 'BGP Instance name'
  end
  
  newproperty(:redistribute_connected) do
    desc 'Whether to redistribute connected routes to the instance.'
    newvalues(true, false)
  end

  newproperty(:redistribute_static) do
    desc 'Whether to redistribute static routes to the instance.'
    newvalues(true, false)
  end

  newproperty(:redistribute_rip) do
    desc 'Whether to redistribute RIP routes to the instance.'
    newvalues(true, false)
  end
  
  newproperty(:redistribute_ospf) do
    desc 'Whether to redistribute OSPF routes to the instance.'
    newvalues(true, false)
  end
  
  newproperty(:redistribute_bgp) do
    desc 'Whether to redistribute BGP routes from other instances to the instance.'
    newvalues(true, false)
  end

  newproperty(:in_filter) do
    desc 'The input filter applying to the injection.'
  end
  
  newproperty(:out_filter) do
    desc 'The output filter applying to the injection.'
  end
end


File: /lib\puppet\type\mikrotik_bgp_network.rb
Puppet::Type.newtype(:mikrotik_bgp_network) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Network (CIDR IP)'
    isnamevar
  end
  
  newproperty(:synchronize) do
    desc 'Whether to synchronize the advertisement with IGP protocols.'
    newvalues(true, false)
  end
end


File: /lib\puppet\type\mikrotik_bgp_peer.rb
Puppet::Type.newtype(:mikrotik_bgp_peer) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  

  newparam(:name) do
    desc 'BGP Peer name'
    isnamevar
  end

  newproperty(:instance) do
    desc 'The BGP Instance this peer belongs to.'
  end

  newproperty(:peer_address) do
    desc 'The Peer Remote Address (IP).'
  end

  newproperty(:peer_port) do
    desc 'TCP port to connect to.'
  end

  newproperty(:peer_as) do
    desc 'The Peer Autonomous System Number (ASN).'
  end

  newproperty(:tcp_md5_key) do
    desc 'The MD5 hash for securing the session.'
  end

  newproperty(:nexthop_choice) do
    desc 'Whether to change nexthop on advertisements.'
    newvalues('default', 'force-self', 'propagate')
  end

  newproperty(:multihop) do
    desc 'Whether to allow multiple hops between peers.'
    newvalues(true, false)
  end

  newproperty(:route_reflect) do
    desc 'Whether to act as a Reflector for this peer.'
    newvalues(true, false)
  end

  newproperty(:hold_time) do
    desc 'The time (seconds) to hold the session up once keepalive exceeded.'
  end

  newproperty(:keepalive_time) do
    desc 'The time (seconds) to keep the session alive.'
  end

  newproperty(:ttl) do
    desc 'The max. number of hop0 (TTL) to reach the peer in.'
  end

  newproperty(:max_prefix_limit) do
    desc 'The maximum number of prefixes to accept from the peer.'
  end

  newproperty(:max_prefix_restart_time) do
    desc 'Minimum time after which peer can reestablish session if max prefix limit was exceeded.'
  end

  newproperty(:in_filter) do
    desc 'The input filter that applies to this peer.'
  end

  newproperty(:out_filter) do
    desc 'The output filter that applies to this peer.'
  end

  newproperty(:allow_as_in) do
    desc 'The maximum number of times my own ASN can appear in the AS Path.'
  end

  newproperty(:remove_private_as) do
    desc 'Whether to remove private ASNs when advertising to peer.'
    newvalues(true, false)
  end

  newproperty(:as_override) do
    desc 'Whether to replace peer ASN with own ASN.'
    newvalues(true, false)
  end

  newproperty(:default_originate) do
    desc 'Specifies how to distribute default route.'
    newvalues('never', 'if-installed', 'always')
  end

  newproperty(:passive) do
    desc 'Do not connect to the peer, only accept incoming connection.'
    newvalues(true, false)
  end

  newproperty(:use_bfd) do
    desc 'Whether to use BFD to break a faulty session faster.'
    newvalues(true, false)
  end

  newproperty(:address_families, :array_matching => :all) do
    desc 'The address families to exchange routing information for [ip, ipv6, l2vpn, vpn4, l2vpn-cisco].'
  end

  newproperty(:source) do
    desc 'The Source IP/Interface that connections should be seen from.'
  end

  newproperty(:comment) do
    desc 'Comment about the peer.'
  end
end


File: /lib\puppet\type\mikrotik_certificate.rb
require 'openssl'

Puppet::Type.newtype(:mikrotik_certificate) do
  apply_to_all

  ensurable do
    defaultvalues
    defaultto(:present)
  end

  newparam(:name) do
    desc 'name of the certificate'
    isnamevar
  end

  newparam(:certificate) do
    desc 'certificate file'
    isrequired
  end

  newparam(:private_key) do
    desc 'private key file'
  end

  newparam(:private_key_passphrase) do
    desc 'private key password'
  end

  newproperty(:fingerprint) do
    desc 'certificate fingerprint'
    defaultto do
      cert = OpenSSL::X509::Certificate.new(resource[:certificate])
      OpenSSL::Digest::SHA256.hexdigest(cert.to_der)
    end
  end

  newproperty(:has_private_key) do
    desc 'does this cert have an associated key?'
  end

  newparam(:number) do
    desc 'number assigned to each cert when multiple are in the same file'
    defaultto(0) 
  end
 
end

File: /lib\puppet\type\mikrotik_dhcpv6_client.rb
Puppet::Type.newtype(:mikrotik_dhcpv6_client) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Interface to listen on for DHCPv6 packets'
    isnamevar
  end

  newproperty(:request_address) do
    desc 'Whether to request IPv6 address from DHCP server.'
    newvalues(true, false)
  end
  
  newproperty(:request_prefix) do
    desc 'Whether to request IPv6 prefix from DHCP server.'
    newvalues(true, false)
  end
  
  newproperty(:pool_name) do
    desc 'Name of Pool to be created on receiving prefix.'
  end

  newproperty(:pool_prefix_length) do
    desc 'Prefix size for pool to be created on receiving prefix.'
  end
  
  newproperty(:prefix_hint) do
    desc 'Prefix Hint (?)'
  end
  
  newproperty(:use_peer_dns) do
    desc 'Whether to use DNS provided by DHCP server.'
    newvalues(true, false)
  end

  newproperty(:add_default_route) do
    desc 'Whether to use default route provided by DHCP server.'
    newvalues(true, false)
  end
end


File: /lib\puppet\type\mikrotik_dhcpv6_server.rb
Puppet::Type.newtype(:mikrotik_dhcpv6_server) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Name of the DHCPv6 server instance'
    isnamevar
  end

  newproperty(:interface) do
    desc 'Interface to attach the DHCPv6 server to'
  end  
    
  newproperty(:lease_time) do
    desc 'Lease time for IPv6 leases'
  end
    
  newproperty(:address_pool) do
    desc 'IPv6 address pool to lease addresses from'
  end
end


File: /lib\puppet\type\mikrotik_dhcp_server.rb
Puppet::Type.newtype(:mikrotik_dhcp_server) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Name of the DHCP server instance'
    isnamevar
  end

  newproperty(:interface) do
    desc 'Interface to attach the DHCP server to'
  end  
  
  newproperty(:relay) do
    desc 'DHCP relay address'
  end
  
  newproperty(:lease_time) do
    desc 'Lease time for IP leases'
  end
  
  newproperty(:bootp_lease_time) do
    desc 'Lease time for BOOTP protocol'
  end
  
  newproperty(:address_pool) do
    desc 'IP address pool to lease addresses from'
  end
  
  newproperty(:src_address) do
    desc 'Source address of the DHCP responses'
  end
  
  newproperty(:delay_threshold) do
    desc 'Wait x time before replying to a request'
  end
  
  newproperty(:authoritative) do
    desc 'Whether/When to make the DHCP server authorative'
    newvalues('no', 'yes', 'after-2sec-delay', 'after-10sec-delay')
  end
  
  newproperty(:bootp_support) do
    desc 'Whether to enable BOOTP support'
    newvalues('none', 'static', 'dynamic')
  end
  
  newproperty(:lease_script) do
    desc 'Script to run on IP lease'
  end
  
  newproperty(:add_arp) do
    desc 'Whether to add dynamic ARP entry on lease'
    newvalues(true, false)
  end
  
  newproperty(:always_broadcast) do
    desc 'Whether to enable always broadcast (?)'
    newvalues(true, false)
  end
  
  newproperty(:use_radius) do
    desc 'Whether to use RADIUS server for IP lease authorization/accounting'
    newvalues(true, false)
  end
    
  # Not defined in winbox:
    #  conflict-detection -- 
    #  insert-queue-before -- 
    #  use-framed-as-classless -- 
end


File: /lib\puppet\type\mikrotik_dhcp_server_network.rb
Puppet::Type.newtype(:mikrotik_dhcp_server_network) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:address) do
    desc 'Network address (CIDR subnet) in use by a DHCP server instance'
    isnamevar
  end

  newproperty(:gateways, :array_matching => :all) do
    desc 'Default Gateways to advertise when leasing IP'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:netmask) do
    desc 'Netmask to use for IP lease (?)'
  end
  
  newproperty(:dns_servers, :array_matching => :all) do
    desc 'DNS servers to advertise when leasing IP'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:domain) do
    desc 'Domain name to advertise when leasing IP'
  end

  newproperty(:wins_servers, :array_matching => :all) do
    desc 'WINS servers to advertise when leasing IP'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:ntp_servers, :array_matching => :all) do
    desc 'NTP servers to advertise when leasing IP'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:caps_managers, :array_matching => :all) do
    desc 'CAPS managers to advertise when leasing IP'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:next_server) do
    desc 'IP of the next DHCP server to use'
  end

  newproperty(:boot_file_name) do
    desc 'File name to use for BOOTP protocol'
  end
  
  newproperty(:dhcp_options, :array_matching => :all) do
    desc 'Extra DHCP options to advertise when leasing IP'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:dhcp_option_sets, :array_matching => :all) do
    desc 'Option set to use for advertising extra DHCP options'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
end


File: /lib\puppet\type\mikrotik_dns.rb
Puppet::Type.newtype(:mikrotik_dns) do
  apply_to_all
  
  # Only 1 set of settings that is always enabled. NOT ensurable 
  
  newparam(:name) do
    desc 'Name should be -dns-'
    isnamevar
  end

  newproperty(:servers, :array_matching => :all) do
    desc 'The DNS servers that the router will use to lookup names.'
  end
  
  newproperty(:allow_remote_requests) do
    desc 'Whether to allow incoming DNS requests (not router-local).'
    newvalues(true, false)
  end
end


File: /lib\puppet\type\mikrotik_file.rb
Puppet::Type.newtype(:mikrotik_file) do
  apply_to_all

  ensurable do
    defaultvalues
    defaultto(:present)
  end

  newparam(:name) do
    desc 'Path to file'
    isnamevar
  end

  newproperty(:content) do
    desc 'Contents of file'
  end

end

File: /lib\puppet\type\mikrotik_firewall_rule.rb
Puppet::Type.newtype(:mikrotik_firewall_rule) do
  apply_to_all
  
  ensurable do
    newvalue(:present) do
      provider.create
    end

    newvalue(:absent) do
      provider.destroy
    end

    newvalue(:enabled) do
      provider.create
      provider.setState(:enabled)
    end

    newvalue(:disabled) do
      provider.create
      provider.setState(:disabled)
    end

    defaultto :present
    
    def retrieve
      provider.getState
    end

    def insync?(is)
      @should.each { |should| 
        case should
        when :present
          return (provider.getState != :absent)
        when :absent
          return (provider.getState == :absent)
        when :enabled
          return (provider.getState == :enabled)
        when :disabled
          return (provider.getState == :disabled)
        end
      }
    end
  end

  newparam(:name) do
    desc 'The unique identifier for the rule'
    isnamevar
  end

  newparam(:table) do
    desc 'The table to which the rule applies (filter,nat,mangle)'
  end
  
  # General
  newproperty(:chain) do
    desc 'The chain to which the rule applies (input,output,filter,src-nat,...)'
  end

  newproperty(:chain_order) do
    desc 'Order number inside the chain (starts at 1).'
  end

  newproperty(:src_address) do  # src-address
    desc 'Source address with mask'
  end
  
  newproperty(:dst_address) do  # dst-address
    desc 'Destination address with mask'
  end

  newproperty(:protocol) do  # protocol
    desc 'Protocol name or number'
  end

  newproperty(:src_port) do  # src-port
    desc 'Source-port number'
  end

  newproperty(:dst_port) do  # dst-port
    desc 'Destination port number or range'
  end

  newproperty(:port) do  # port
    desc 'Source Or Destination port number or range'
  end
  
  newproperty(:p2p) do  # p2p
    desc 'P2P program to match'
  end  

  newproperty(:in_interface) do  # in-interface
    desc 'Interface the packet has entered the router through'
  end

  newproperty(:out_interface) do  # out-interface
    desc 'Interface the packet has leaved the router through'
  end

  newproperty(:in_interface_list) do  # in-interface-list
    desc 'Interface List the packet has entered the router through'
  end

  newproperty(:out_interface_list) do  # out-interface-list
    desc 'Interface List the packet has leaved the router through'
  end

  newproperty(:packet_mark) do  # packet-mark
    desc 'Matches packets marked via mangle facility with particular packet mark'
  end

  newproperty(:connection_mark) do  # connection-mark
    desc 'Matches packets marked via mangle facility with particular connection mark'
  end

  newproperty(:routing_mark) do  # routing-mark
    desc 'Matches packets marked by mangle facility with particular routing mark'
  end

  newproperty(:routing_table) do  # routing-table
    desc 'Matches packets on particular routing table'
  end

  newproperty(:connection_type) do  # connection-type
    desc 'Match packets with given connection type'
  end

  newproperty(:connection_state) do  # connection-state
    desc 'Interprets the connection tracking analysis data for a particular packet'
  end

  newproperty(:connection_nat_state) do  # connection-nat-state
    desc 'Interprets the NAT connection tracking analysis data for a particular packet'
  end

  # Advanced
  newproperty(:src_address_list) do  # src-address-list
    desc 'Matches source address of a packet against user-defined address list'
  end
  
  newproperty(:dst_address_list) do  # dst-address-list
    desc 'Destination address list name in which packet place'
  end
  
  newproperty(:layer7_protocol) do  # layer7-protocol
    desc 'TODO'
  end
  
  newproperty(:content) do  # content
    desc 'The text packets should contain in order to match the rule'
  end
  
  newproperty(:connection_bytes) do  # connection-bytes
    desc 'Match packets with given bytes or byte range'
  end
  
  newproperty(:connection_rate) do  # connection-rate
    desc 'TODO'
  end
  
  newproperty(:per_connection_classifier) do  # per-connection-classifier
    desc 'TODO'
  end
  
  newproperty(:src_mac_address) do  # src-mac-address
    desc 'Source MAC address'
  end
  
  newproperty(:in_bridge_port) do  # in-bridge-port
    desc 'TODO'
  end
  
  newproperty(:out_bridge_port) do  # out-bridge-port
    desc 'Matches the bridge port physical output device added to a bridge device'
  end
  
  newproperty(:in_bridge_port_list) do  # in-bridge-port-list
    desc 'TODO'
  end
  
  newproperty(:out_bridge_port_list) do  # out-bridge-port-list
    desc 'TODO'
  end
  
  newproperty(:ipsec_policy) do  # ipsec-policy
    desc 'TODO'
  end

  newproperty(:tls_host) do  # tls-host
    desc 'TODO'
  end
    
  newproperty(:ingress_priority) do  # ingress-priority
    desc 'TODO'
  end
  
  newproperty(:priority) do  # priority
    desc 'TODO'
  end
  
  newproperty(:dscp) do  # dscp
    desc 'TODO'
  end
  
  newproperty(:tcp_mss) do  # tcp-mss
    desc 'TCP Maximum Segment Size value'
  end
  
  newproperty(:packet_size) do  # packet-size
    desc 'Packet size or range in bytes'
  end
  
  newproperty(:random) do  # random
    desc 'Match packets randomly with given propability'
  end
  
  newproperty(:tcp_flags) do  # tcp-flags
    desc 'TCP flags to match'
  end
  
  newproperty(:ipv4_options) do  # ipv4-options
    desc 'Match ipv4 header options'
  end
  
  newproperty(:ttl) do  # ttl
    desc 'TODO'
  end
  
  # Extra  
  newproperty(:connection_limit) do  # connection-limit
    desc 'Restrict connection limit per address or address block'
  end
  
  newproperty(:limit) do  # limit
    desc 'Setup burst, how many times to use it in during time interval measured in seconds'
  end
  
  newproperty(:dst_limit) do  # dst-limit
    desc 'Packet limitation per time with burst to dst-address, dst-port or src-address'
  end
  
  newproperty(:nth) do  # nth
    desc 'Match nth packets received by the rule'
  end
  
  newproperty(:time) do  # time
    desc 'Packet arrival time and date or locally generated packets departure time and date'
  end
  
  newproperty(:src_address_type) do  # src-address-type
    desc 'Source IP address type'
  end
  
  newproperty(:dst_address_type) do  # dst-address-type
    desc 'Destination address type'
  end
  
  newproperty(:psd) do  # psd
    desc 'Detect TCP un UDP scans'
  end
  
  newproperty(:hotspot) do  # hotspot
    desc 'Matches packets received from clients against various Hot-Spot'
  end
  
  newproperty(:fragment) do  # fragment
    desc 'TODO'
  end
      
  # Action    
  newproperty(:action) do
    desc 'Action to undertake if the packet matches the rule'
  end
  
  newproperty(:log) do  # log
    desc 'TODO'
  end
  
  newproperty(:log_prefix) do  # log-prefix
    desc 'Creates all logs with specific prefix'
  end
  
  newproperty(:jump_target) do  # jump-target
    desc 'Name of the target chain, if the action=jump is used'
  end

  newproperty(:address_list) do  # address-list
    desc 'Address list in which marked address put'
  end
  
  newproperty(:address_list_timeout) do  # address-list-timeout
    desc 'Time interval after which address remove from address list'
  end
  
  newproperty(:reject_with) do  # reject-with
    desc 'Alters the reply packet of reject action'
  end
  
  newproperty(:to_addresses) do  # to-addresses
    desc 'Address or address range to replace original address of an IP packet with'
  end
  
  newproperty(:to_ports) do  # to-ports
    desc 'Port or port range to replace original port of an IP packet with'
  end
  
  newproperty(:new_connection_mark) do  # new-connection-mark
    desc 'Specify the new value of the connection mark to be used in conjunction with action=mark-connection'
  end
  
  newproperty(:new_dscp) do  # new-dscp
    desc 'TODO'
  end
  
  newproperty(:new_mss) do  # new-mss
    desc 'Specify MSS value to be used in conjunction with action=change-mss'
  end
  
  newproperty(:new_packet_mark) do  # new-packet-mark
    desc 'Specify the new value of the packet mark to be used in conjunction with action=mark-packet'
  end
  
  newproperty(:new_priority) do  # new-priority
    desc 'TODO'
  end
  
  newproperty(:new_routing_mark) do  # new-routing-mark
    desc 'Specify the new value of the routing mark used in conjunction with action=mark-routing'
  end
  
  newproperty(:new_ttl) do  # new-ttl
    desc 'Specify the new TTL field value used in conjunction with action=change-ttl'
  end
  
  newproperty(:route_dst) do  # route-dst
    desc 'TODO'
  end
  
  newproperty(:sniff_id) do  # sniff-id
    desc 'TODO'
  end
  
  newproperty(:sniff_target) do  # sniff-target
    desc 'TODO'
  end
  
  newproperty(:sniff_target_port) do  # sniff-target-port
    desc 'TODO'
  end
end


File: /lib\puppet\type\mikrotik_graph_interface.rb
Puppet::Type.newtype(:mikrotik_graph_interface) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'The interface name (or "all")'
    isnamevar
  end
  
  newproperty(:allow) do
    desc 'The IP/Subnet to allow access to the graphs.'
    defaultto '0.0.0.0/0'
  end

  newproperty(:store_on_disk) do
    desc 'Whether to store the graphs on disk.'
    newvalues(true, false)
    defaultto true    
  end
end


File: /lib\puppet\type\mikrotik_graph_queue.rb
Puppet::Type.newtype(:mikrotik_graph_queue) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'The simple queue name (or "all")'
    isnamevar
  end
  
  newproperty(:allow) do
    desc 'The IP/Subnet to allow access to the graphs.'
    defaultto '0.0.0.0/0'
  end

  newproperty(:store_on_disk) do
    desc 'Whether to store the graphs on disk.'
    newvalues(true, false)
    defaultto true    
  end

  newproperty(:allow_target) do
    desc 'Whether to allow access to web graphing from IP range specified in target-address parameter'
    newvalues(true, false)
    defaultto true    
  end
end


File: /lib\puppet\type\mikrotik_graph_resource.rb
Puppet::Type.newtype(:mikrotik_graph_resource) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
    
  newparam(:name) do
    desc 'Name should be -resource-'
    isnamevar
  end
  
  newproperty(:allow) do
    desc 'The IP/Subnet to allow access to the graphs.'
    defaultto '0.0.0.0/0'
  end

  newproperty(:store_on_disk) do
    desc 'Whether to store the graphs on disk.'
    newvalues(true, false)
    defaultto true    
  end
end


File: /lib\puppet\type\mikrotik_interface_bgp_vpls.rb
Puppet::Type.newtype(:mikrotik_interface_bgp_vpls) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Interface name'
    isnamevar
  end

  newproperty(:route_distinguisher) do
    desc 'Route Distinguisher (X:Y) [eg. ASN:IP]'
  end
  
  newproperty(:import_route_targets, :array_matching => :all) do
    desc 'Import Route Targets (X:Y) [eg. ASN:IP]'
  end
  
  newproperty(:export_route_targets, :array_matching => :all) do
    desc 'Export Route Targets (X:Y) [eg. ASN:IP]'
  end

  newproperty(:site_id) do
    desc 'Site ID (unique per peering)'
  end

  newproperty(:bridge) do
    desc 'Bridge to attach VPLS tunnels to'
  end

  newproperty(:bridge_cost) do
    desc 'Port cost on the bridge'
  end

  newproperty(:bridge_horizon) do
    desc 'Port horizon on the bridge'
  end
  
  newproperty(:control_word) do
    desc 'Whether to use control word'
    newvalues(true, false)
  end

  newproperty(:pw_mtu) do
    desc 'MTU for the Pseudowire'
  end
  
  newproperty(:pw_type) do
    desc 'Type of the Pseudowire'
    newvalues(:vpls, 'raw ethernet', 'tagged ethernet')
  end
end


File: /lib\puppet\type\mikrotik_interface_bond.rb
Puppet::Type.newtype(:mikrotik_interface_bond) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'The bonding interface name'
    isnamevar
  end
  
  newproperty(:mtu) do
    desc 'Maximum Transmit Unit'
  end

  newproperty(:arp) do
    desc 'Address Resolution Protocol to use'
    newvalues('enabled', 'disabled', 'proxy-arp', 'reply-only')
  end

  newproperty(:arp_timeout) do
    desc 'Address Resolution Protocol Timeout'
  end

  newproperty(:slaves, :array_matching => :all) do
    desc 'Interfaces that are used in bonding'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:mode) do
    desc 'Interface bonding mode'
    newvalues('802.3ad', 'active-backup', 'balance-alb', 'balance-rr', 'balance-tlb', 'balance-xor', 'broadcast')
  end
  
  newproperty(:link_monitoring) do
    desc 'Method for monitoring the link'
    newvalues('arp', 'mii', 'none')
  end
  
  newproperty(:transmit_hash_policy) do
    desc 'Transmit Hash Policy'
    newvalues('layer-2', 'layer-2-and-3', 'layer-3-and-4')
  end
  
  newproperty(:primary) do
    desc 'Slave that will be used in active-backup mode as active link'
  end
  
  # Not frequently used settings:
  ## min-links -- 
  ## down-delay -- Time period the interface is disabled  if a link failure has been detected
  ## up-delay -- Time period the interface is disabled if a link has been brought up
  ## lacp-rate -- Link Aggregation Control Protocol rate specifies how often to exchange with LACPDUs between bonding peer
  ## mii-interval -- Time in milliseconds for monitoring mii-type link
  ## arp-interval -- Time in milliseconds for monitoring ARP requests
  ## arp-ip-targets -- IP addresses for monitoring
end


File: /lib\puppet\type\mikrotik_interface_bridge.rb
Puppet::Type.newtype(:mikrotik_interface_bridge) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'The bridge name'
    isnamevar
  end

  newproperty(:mtu) do
    desc 'Maximum Transmit Unit'
  end

  newproperty(:arp) do
    desc 'Address Resolution Protocol to use'
    newvalues('enabled', 'disabled', 'proxy-arp', 'reply-only')
  end

  newproperty(:arp_timeout) do
    desc 'Address Resolution Protocol Timeout'
  end

  newproperty(:admin_mac) do
    desc 'The administrative MAC address'
  end

  newproperty(:igmp_snooping) do
    desc 'Whether to enable IGMP snooping'
    newvalues(true, false)
  end

  newproperty(:dhcp_snooping) do
    desc 'Whether to enable DHCP snooping'
    newvalues(true, false)
  end

  newproperty(:fast_forward) do
    desc 'Whether to enable FastPath/Hardware Acceleration'
    newvalues(true, false)
  end

  # STP
  newproperty(:protocol_mode) do
    desc 'Bridge protection mode: none, STP, RSTP, MSTP'
    newvalues('none', 'stp', 'rstp', 'mstp')
  end
  
  newproperty(:priority) do
    desc 'Bridge interface priority: hexidecimal, defaults to 0x8000'
  end
  
  # MSTP
  newproperty(:region_name) do
    desc 'MSTP Region Name'
  end

  newproperty(:region_revision) do
    desc 'MSTP Region Revision'
  end
  
  # VLAN 
  newproperty(:vlan_filtering) do
    desc 'Whether to enable VLAN filtering'
    newvalues(true, false)
  end

  newproperty(:pvid) do
    desc 'Bridge VLAN ID (untagged)'
  end

  newproperty(:ether_type) do
    desc 'Bridge Ether Type'
    newvalues('0x8100', '0x88a8', '0x9100')
  end
  
  newproperty(:frame_types) do
    desc 'Allow Frame Types'
    newvalues('admit-all', 'admit-only-untagged-and-priority-tagged', 'admit-only-vlan-tagged')
  end
  
  newproperty(:ingress_filtering) do
    desc 'Whether to enable ingress filtering'
    newvalues(true, false)
  end
  
  newproperty(:comment) do
    desc 'Comments'
  end
  
  # Less frequently used options:  
  
  ##  ageing-time -- Time the information about host will be kept in the the data base
  ##  auto-mac --   
  
  # STP  
  ##  max-message-age -- Time to remember Hello messages received from other bridges
  ##  forward-delay -- Time which is spent in listening/learning state
  ##  transmit-hold-count -- 
  ##  max-hops --
  
  # DHCP snooping 
  ##  add-dhcp-option82 -- 
  
  # IGMP snooping
  ##  igmp-version -- 
  ##  multicast-router -- 
  ##  multicast-querier -- 
  ##  startup-query-count -- 
  ##  last-member-query-count -- 
  ##  last-member-interval -- 
  ##  membership-interval -- 
  ##  querier-interval -- 
  ##  query-interval -- 
  ##  query-response-interval -
  ##  startup-query-interval -- 
end


File: /lib\puppet\type\mikrotik_interface_bridge_msti.rb
Puppet::Type.newtype(:mikrotik_interface_bridge_msti) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'Unique name for MST Instance'
    isnamevar
  end

  newproperty(:bridge) do
    desc 'The bridge on which the MST Instance should run.'
  end
  
  newproperty(:identifier) do
    desc 'The MST Instance identifier (1-32).'
  end

  newproperty(:priority) do
    desc 'The bridge priority within the MST Instance.'
  end
  
  newproperty(:vlan_mapping, :array_matching => :all) do
    desc 'List of VLANs'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
end


File: /lib\puppet\type\mikrotik_interface_bridge_msti_port.rb
Puppet::Type.newtype(:mikrotik_interface_bridge_msti_port) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'Unique name for Port MST Override'
    isnamevar
  end
  
  newproperty(:interface) do
    desc 'The interface to apply this config.'
  end
  
  newproperty(:identifier) do
    desc 'The MST Instance identifier (1-32).'
  end

  newproperty(:priority) do
    desc 'The port priority within the MST Instance. Default: 0x80 (hex)'
  end
  
  newproperty(:internal_path_cost) do
    desc 'The port cost within the MST Instance. Default: 10'
  end
end


File: /lib\puppet\type\mikrotik_interface_bridge_port.rb
Puppet::Type.newtype(:mikrotik_interface_bridge_port) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:interface) do
    desc 'Name of the interface'
    isnamevar
  end

  newproperty(:bridge) do
    desc 'The bridge interface the respective interface is grouped in'
  end

  newproperty(:horizon) do
    desc 'The bridge horizon (ports with equal value do not exchange packets)'
  end
  
  # STP
  newproperty(:priority) do
    desc 'The port priority in STP (or between domains in MSTP). Default: 0x80 (hex)'
  end
  
  newproperty(:path_cost) do
    desc 'The path cost in STP (or between domains in MSTP). Default: 10'
  end
  
  newproperty(:internal_path_cost) do
    desc 'The path cost in the MSTP domain. Default: 10'
  end

  # VLAN 
  newproperty(:pvid) do
    desc 'Port VLAN ID (untagged)'
  end
  
  newproperty(:frame_types) do
    desc 'Allow Frame Types'
    newvalues('admit-all', 'admit-only-untagged-and-priority-tagged', 'admit-only-vlan-tagged')
  end

  newproperty(:ingress_filtering) do
    desc 'Whether to enable ingress filtering'
    newvalues(true, false)
  end

  newproperty(:tag_stacking) do
    desc 'Whether to enable tag stacking'
    newvalues(true, false)
  end
  
  newproperty(:comment) do
    desc 'Comments'
  end

  # Less frequently used options:

  ##  learn -- 
  ##  unknown-unicast-flood -- 
  ##  unknown-multicast-flood -- 
  ##  broadcast-flood -- 
  ##  trusted -- 
  ##  hw -- 
  ##  multicast-router -- 
  ##  fast-leave -- 

  # STP
  ##  edge -- 
  ##  point-to-point -- 
  ##  auto-isolate -- 
  ##  restricted-role -- 
  ##  restricted-tcn -- 
  ##  bpdu-guard -- 
end


File: /lib\puppet\type\mikrotik_interface_bridge_settings.rb
Puppet::Type.newtype(:mikrotik_interface_bridge_settings) do
  apply_to_all
  
  # Only 1 set of settings that is always enabled. NOT ensurable 
  
  newparam(:name) do
    desc 'Name should be -bridge-'
    isnamevar
  end

  newproperty(:allow_fast_path) do
    desc 'Whether to allow Fast Path'
    newvalues(true, false)
  end
  
  newproperty(:use_ip_firewall) do
    desc 'Whether to use IP Firewall for bridged traffic'
    newvalues(true, false)
  end
  
  newproperty(:use_ip_firewall_for_pppoe) do
    desc 'Whether to use IP Firewall for PPPoE encapsulated traffic on the bridge [DANGER!]'
    newvalues(true, false)
  end
  
  newproperty(:use_ip_firewall_for_vlan) do
    desc 'Whether to use IP Firewall for VLAN encapsulated traffic on the bridge'
    newvalues(true, false)
  end
end


File: /lib\puppet\type\mikrotik_interface_bridge_vlan.rb
Puppet::Type.newtype(:mikrotik_interface_bridge_vlan) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Unique name of VLAN group on bridge'
    isnamevar
  end

  newproperty(:bridge) do
    desc 'The bridge interface that the VLANs should be configured on.'
  end
  
  newproperty(:vlan_ids, :array_matching => :all) do
    desc 'List of VLANs'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end

  newproperty(:tagged, :array_matching => :all) do
    desc 'List of interfaces where VLANs are tagged'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end

  newproperty(:untagged, :array_matching => :all) do
    desc 'List of interfaces where VLANs are untagged'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
end


File: /lib\puppet\type\mikrotik_interface_eoip.rb
Puppet::Type.newtype(:mikrotik_interface_eoip) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'The EoIP tunnel name'
    isnamevar
  end

  newproperty(:mtu) do
    desc 'Maximum Transmit Unit'
  end

  newproperty(:admin_mac) do
    desc 'The MAC address for this side of the tunnel'
  end  
  
  newproperty(:arp) do
    desc 'Address Resolution Protocol to use'
    newvalues('enabled', 'disabled', 'proxy-arp', 'reply-only')
  end

  newproperty(:arp_timeout) do
    desc 'Address Resolution Protocol Timeout'
  end
  
  newproperty(:local_address) do
    desc 'IP Address for this side of the tunnel'
  end
  
  newproperty(:remote_address) do
    desc 'IP Address for the remote side of the tunnel'
  end
  
  newproperty(:tunnel_id) do
    desc 'Unique ID for this tunnel'
  end
  
  newproperty(:ipsec_secret) do
    desc 'Shared secret if IPSEC encryption is being used'
  end
  
  newproperty(:keepalive) do
    desc 'Time to keep the tunnel alive if no traffic is seen'
  end

  newproperty(:dscp) do
    desc 'The DSCP value (QoS)'
  end

  newproperty(:dont_fragment) do
    desc 'Whether to allow packet fragmentation in the tunnel'
    newvalues('inherit', 'no')
  end

  newproperty(:clamp_tcp_mss) do
    desc 'Whether to clamp the TCP MSS (?)'
    newvalues(false, true)
    defaultto true
  end

  newproperty(:allow_fast_path) do
    desc 'Whether to allow Fast Path Routing'
    newvalues(false, true)
    defaultto true
  end

  # Not frequently used settings:
  ## loop-protect -- 
  ## loop-protect-disable-time -- 
  ## loop-protect-send-interval -- 
end


File: /lib\puppet\type\mikrotik_interface_ethernet.rb
Puppet::Type.newtype(:mikrotik_interface_ethernet) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'The original ethernet name (auto detected, not changeable)'
    isnamevar
  end
  
  newproperty(:alias) do
    desc 'The actual interface name'
  end

  newproperty(:mtu) do
    desc 'Maximum Transmit Unit'
  end
  
  newproperty(:arp) do
    desc 'Address Resolution Protocol to use'
    newvalues('enabled', 'disabled', 'proxy-arp', 'reply-only')
  end

  newproperty(:arp_timeout) do
    desc 'Address Resolution Protocol Timeout'
  end
  
  newproperty(:auto_negotiation) do
    desc 'When enabled the interface "advertises" the maximum capabilities to achieve the best connection possible'
  end

  newproperty(:advertise, :array_matching => :all) do
    desc 'Speed and duplex mode to advertise'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end

  # Not frequently used settings:
  ## loop-protect -- 
  ## loop-protect-disable-time -- 
  ## loop-protect-send-interval --  
end


File: /lib\puppet\type\mikrotik_interface_gre.rb
Puppet::Type.newtype(:mikrotik_interface_gre) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end

    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }  
    end
  end
  
  newparam(:name) do
    desc 'The GRE tunnel name'
    isnamevar
  end

  newproperty(:mtu) do
    desc 'Maximum Transmit Unit'
  end

  newproperty(:local_address) do
    desc 'IP Address for this side of the tunnel'
  end

  newproperty(:remote_address) do
    desc 'IP Address for the remote side of the tunnel'
  end

  newproperty(:ipsec_secret) do
    desc 'Shared secret if IPSEC encryption is being used'
  end

  newproperty(:keepalive) do
    desc 'Time to keep the tunnel alive if no traffic is seen'
  end

  newproperty(:dscp) do
    desc 'The DSCP value (QoS)'
  end

  newproperty(:dont_fragment) do
    desc 'Whether to allow packet fragmentation in the tunnel'
    newvalues('inherit', 'no')
  end

  newproperty(:clamp_tcp_mss) do
    desc 'Whether to clamp the TCP MSS (?)'
    newvalues(false, true)
    defaultto true
  end

  newproperty(:allow_fast_path) do
    desc 'Whether to allow Fast Path Routing'
    newvalues(false, true)
    defaultto true
  end
end


File: /lib\puppet\type\mikrotik_interface_list.rb
require 'puppet/property/boolean'

Puppet::Type.newtype(:mikrotik_interface_list) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end

  newparam(:name) do
    desc 'The name of the interfaces list'
    isnamevar
  end
  
  newparam(:manage_members, boolean: true, parent: Puppet::Property::Boolean) do
    defaultto true
  end

  newproperty(:members, :array_matching => :all) do
    desc 'Interfaces that belong to this list'
    
    def insync?(is)
      if !resource.manage_members?
        true
      elsif is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end

  newproperty(:include, :array_matching => :all) do
    desc 'Other interface lists whose members are included in this list'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end

  newproperty(:exclude, :array_matching => :all) do
    desc 'Other interface lists whose members are excluded from this list'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end

end


File: /lib\puppet\type\mikrotik_interface_ppp.rb
Puppet::Type.newtype(:mikrotik_interface_ppp) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create if retrieve == :absent
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'The interface name'
    isnamevar
  end

  newproperty(:ppp_type) do
    desc 'only ovpn_client supported so far'
    defaultto 'ovpn_client'
  end

  newproperty(:max_mtu) do
    desc 'Maximum Transmission Unit'
  end

  newproperty(:mac_address) do
    desc '(OVPN) MAC address of the interface (normally auto-generated)'
  end

  newproperty(:connect_to) do
    desc '(OVPN) The remote address to connect to'
  end

  newproperty(:port) do
    desc '(OVPN) The port the server is listening on'
    defaultto '1194'
  end

  newproperty(:mode) do
    desc '(OVPN) IP (tunnel) mode or Ethernet (bridge/tap) mode'
    newvalue(:ip)
    newvalue(:ethernet)
  end

  newproperty(:user) do
    desc 'The username to connect as'
  end

  newproperty(:password) do
    desc 'The password to connect with'
  end

  newproperty(:profile) do
    desc 'The profile to use'
  end

  autorequire(:mikrotik_ppp_profile) do
    self[:profile]
  end

  newproperty(:certificate) do
    desc '(OVPN) name of Certificate file'
  end

  newproperty(:add_default_route) do
    newvalue(:true)
    newvalue(:false)
  end

  newproperty(:authentication) do
    desc 'Authentication algorithm'
  end

  newproperty(:cipher) do
    desc '(OVPN) Cipher algorithm'
  end

end


File: /lib\puppet\type\mikrotik_interface_pppoe_server.rb
Puppet::Type.newtype(:mikrotik_interface_pppoe_server) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'The PPPoE Service name (service-name)'
    isnamevar
  end

  newproperty(:interface) do
    desc 'The interface on which to set up the service'
  end
  
  newproperty(:max_mtu) do
    desc 'Maximum Transmit Unit'
  end

  newproperty(:max_mru) do
    desc 'Maximum Receive Unit'
  end
  
  newproperty(:mrru) do
    desc 'MRRU'
  end
  
  newproperty(:keepalive) do
    desc 'Time to keep the tunnel alive if no traffic is seen'
  end
  
  newproperty(:default_profile) do
    desc 'The default user profile'
  end  
  
  newproperty(:one_session_per_host) do
    desc 'One session per host'
    newvalues(false, true)
  end
  
  newproperty(:max_sessions) do
    desc 'The maximum number of sessions on this service'
  end
  
  newproperty(:pado_delay) do
    desc 'PADO delay in ms'
  end
  
  newproperty(:authentication, :array_matching => :all) do
    desc 'List of authentication methods (pap, chap, mschap1/2)'
        
    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
end


File: /lib\puppet\type\mikrotik_interface_ppp_server_binding.rb
Puppet::Type.newtype(:mikrotik_interface_ppp_server_binding) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create if retrieve == :absent
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'The interface name'
    isnamevar
  end

  newproperty(:ppp_type) do
    desc 'only ovpn supported so far'
    defaultto 'ovpn'
  end

  newproperty(:user) do
    desc 'The username to connect as'
  end

  newproperty(:comment) do
    desc 'A comment'
  end

end


File: /lib\puppet\type\mikrotik_interface_te.rb
Puppet::Type.newtype(:mikrotik_interface_te) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Interface name'
    isnamevar
  end

  newproperty(:mtu) do
    desc 'Interface MTU (L3)'
  end
  
  newproperty(:from_address) do
    desc 'Establish Tunnel from this IP'
  end
  
  newproperty(:to_address) do
    desc 'Establish Tunnel to this IP'
  end

  newproperty(:bandwidth) do
    desc 'Bandwidth that the tunnel reserves by default'
  end

  newproperty(:primary_path) do
    desc 'MPLS-TE Tunnel path to use primarily'
  end

  newproperty(:secondary_paths, :array_matching => :all) do
    desc 'MPLS-TE Tunnel paths to fail over on'

# DO NOT SORT !
#    def insync?(is)
#      if is.is_a?(Array) and @should.is_a?(Array)
#        is.sort == @should.sort
#      else
#        is == @should
#      end
#    end
  end
  
  # TE
  newproperty(:record_route) do
    desc 'Whether to record route'
    newvalues(true, false)
  end
  
  # Bandwidth
  newproperty(:bandwidth_limit) do
    desc 'Actual bandwidth limit to enforce (%)'
  end
  
  newproperty(:auto_bandwidth_range) do
    desc 'Minimum and Maximum Bandwidth to reserve. Firmat: min-max'
  end
  
  newproperty(:auto_bandwidth_reserve) do
    desc 'Additional bandwidth to reserve (%)'
  end

  newproperty(:auto_bandwidth_avg_interval) do
    desc 'Interval at which to average bandwidth used for automatic bandwidth.'
  end
  
  newproperty(:auto_bandwidth_update_interval) do
    desc 'Interval at which to update automatic bandwidth.'
  end

  # TE
  newproperty(:primary_retry_interval) do
    desc 'Interval at which to return from secondary to primary path.'
  end
  newproperty(:setup_priority) do
    desc 'Priority (0-7) for bandwidth reservation to set up new tunnel.'
  end
  newproperty(:holding_priority) do
    desc 'Priority (0-7) for bandwidth reservation for running tunnel.'
  end
  newproperty(:reoptimize_interval) do
    desc 'Interval at which to calculate most optimal CSPF route.'
  end

  # Less frequently used options:
  ## disable-running-check -- 
  ## affinity-include-all -- 
  ## affinity-include-any -- 
  ## affinity-exclude -- 
  ## comment -- Not visible on Winbox?
end


File: /lib\puppet\type\mikrotik_interface_vlan.rb
Puppet::Type.newtype(:mikrotik_interface_vlan) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'The name of the VLAN (802.1q) interface'
    isnamevar
  end

  newproperty(:mtu) do
    desc 'Maximum Transmit Unit'
  end

  newproperty(:arp) do
    desc 'Address Resolution Protocol to use'
    newvalues('enabled', 'disabled', 'proxy-arp', 'reply-only')
  end

  newproperty(:arp_timeout) do
    desc 'Address Resolution Protocol Timeout'
  end
  
  newproperty(:vlan_id) do
    desc 'VLAN tag that is used to distinguish VLANs'
  end

  newproperty(:interface) do
    desc 'Physical interface to the network where are VLANs'
  end

  newproperty(:use_service_tag) do
    desc 'Whether to use VLAN Service Tag'
    newvalues(false, true)
    defaultto false
  end
end


File: /lib\puppet\type\mikrotik_interface_vrrp.rb
Puppet::Type.newtype(:mikrotik_interface_vrrp) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'The VRRP interface name'
    isnamevar
  end

  newproperty(:mtu) do
    desc 'Maximum Transmit Unit'
  end

  newproperty(:arp) do
    desc 'Address Resolution Protocol to use'
    newvalues('enabled', 'disabled', 'proxy-arp', 'reply-only')
  end

  newproperty(:arp_timeout) do
    desc 'Address Resolution Protocol Timeout'
  end

  newproperty(:interface) do
    desc 'Interface to attach VRRP address to. Interface should have IP set in same subnet (?)'
  end
  
  newproperty(:vrid) do
    desc 'Unique ID'
  end
  
  newproperty(:priority) do
    desc 'Priority of this peer'
  end
  
  newproperty(:interval) do
    desc 'Interval (seconds) for peer communication'
  end
  
  newproperty(:preemption_mode) do
    desc 'Whether to enable preemption for peer communication'
    newvalues(true, false)
    defaultto true
  end
  
  newproperty(:authentication) do
    desc 'Authentication mode to use for peer communication'
    newvalues('none', 'simple', 'ah')
    defaultto 'none'
  end
  
  newproperty(:password) do
    desc 'Password to use when authentication is enabled'
  end
  
  newproperty(:version) do
    desc 'Version of VRRP Protocol'
    newvalues(2, 3)
    defaultto 3
  end
  
  newproperty(:v3_protocol ) do
    desc 'IP version'
    newvalues('ipv4', 'ipv6')
    defaultto 'ipv4'
  end

  newproperty(:on_master) do
    desc 'Script to run when interface becomes Master'
  end

  newproperty(:on_backup) do
    desc 'Script to run when interface becomes Backup'
  end
end


File: /lib\puppet\type\mikrotik_ipsec_group.rb
require 'puppet/property/boolean'

Puppet::Type.newtype(:mikrotik_ipsec_group) do
  apply_to_all

  ensurable

  newparam(:name) do
    desc 'Policy template group name'
    isnamevar
    validate do |value|
      if value == 'default'
        raise ArgumentError, "the default IPSec policy template group is managed automatically by RouterOS"
      end
    end
  end
end


File: /lib\puppet\type\mikrotik_ipsec_identity.rb
require 'puppet/property/boolean'

Puppet::Type.newtype(:mikrotik_ipsec_identity) do
  apply_to_all

  ensurable do
    defaultto :present

    newvalue(:present) do
      provider.create
    end

    newvalue(:absent) do
      provider.destroy
    end

    newvalue(:enabled) do
      provider.setState(:enabled)
    end

    newvalue(:disabled) do
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end

    def insync?(is)
      @should.each { |should|
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled
            return (provider.getState == :enabled)
          when :disabled
            return (provider.getState == :disabled)
        end
      }
    end
  end

  newparam(:name) do
    desc 'The unique identifier for this identity'
    isnamevar
  end

  newproperty(:auth_method) do
    desc 'The authentication method to use.'
    newvalues(*%w{digital-signature eap eap-radius pre-shared-key pre-shared-key-xauth rsa-key rsa-signature-hybrid})
  end

  newproperty(:certificate) do
    desc 'Name of an installed certificate to use for signing packets.'
  end

  newproperty(:eap_methods, :array_matching => :all) do
    newvalues(:mschapv2, :peap, :tls, :ttls)
  end

  newproperty(:generate_policy) do
    desc 'Whether this identity is allowed to dynamically generate a policy from a policy-template-group if no existing policy matches'
    newvalues(*%w{no port-override port-strict})
  end

  newproperty(:key) do
    desc 'name of the private key to use from the installed IPSec Keys. Only applicable if auth_method is rsa-key.'
  end

  newproperty(:match_by) do
    newvalues(:certificate, :remote_id)
  end

  newproperty(:mode_config) do
  end

  newproperty(:my_id) do
  end

  newproperty(:notrack_chain) do
  end

  newproperty(:password) do
  end

  newproperty(:peer) do
  end

  newproperty(:policy_template_group) do
  end

  newproperty(:remote_certificate) do
  end

  newproperty(:remote_id) do
  end

  newproperty(:remote_key) do
  end

  newproperty(:secret) do
  end

  newproperty(:username) do
  end

  autorequire(:mikrotik_certificate) { self[:certificate] }
  autorequire(:mikrotik_ipsec_mode_config) { self[:mode_config] }
  autorequire(:mikrotik_ipsec_peer) { self[:peer] }
  autorequire(:mikrotik_ipsec_group) { self[:policy_template_group] }
end


File: /lib\puppet\type\mikrotik_ipsec_mode_config.rb
require 'puppet/property/boolean'

Puppet::Type.newtype(:mikrotik_ipsec_mode_config) do
  apply_to_all

  ensurable

  newparam(:name) do
    desc 'Mode Config description'
    isnamevar
  end

  newproperty(:address_pool) do
  end

  newproperty(:address_prefix_length) do
  end

  newproperty(:comment) do
  end

  newproperty(:split_include, :array_matching => :all) do
  end

  newproperty(:static_dns, :array_matching => :all) do
  end

  newproperty(:system_dns, boolean: true, parent: Puppet::Property::Boolean) do
  end
end


File: /lib\puppet\type\mikrotik_ipsec_peer.rb
require 'puppet/property/boolean'

Puppet::Type.newtype(:mikrotik_ipsec_peer) do
  apply_to_all

  ensurable do
    defaultto :present

    newvalue(:present) do
      provider.create
    end

    newvalue(:absent) do
      provider.destroy
    end

    newvalue(:enabled) do
      provider.setState(:enabled)
    end

    newvalue(:disabled) do
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end

    def insync?(is)
      @should.each { |should|
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled
            return (provider.getState == :enabled)
          when :disabled
            return (provider.getState == :disabled)
        end
      }
    end
  end

  newparam(:name) do
    desc 'Peer description'
    isnamevar
  end

  newproperty(:address) do
    desc 'Address'
  end

  newproperty(:exchange_mode) do
    newvalues(*%w{aggresive base ike2 main})
  end

  newproperty(:local_address) do
  end

  newproperty(:passive, boolean: true, parent: Puppet::Property::Boolean) do
    defaultto true
  end

  newproperty(:port) do
  end

  newproperty(:send_initial_contact, boolean: true, parent: Puppet::Property::Boolean) do
    defaultto false
  end

  newproperty(:profile) do
  end

  newproperty(:comment) do
  end

  autorequire(:mikrotik_ipsec_profile) { self[:profile] }
end


File: /lib\puppet\type\mikrotik_ipsec_policy.rb
require 'puppet/property/boolean'

Puppet::Type.newtype(:mikrotik_ipsec_policy) do
  apply_to_all

  ensurable do
    defaultto :present

    newvalue(:present) do
      provider.create
    end

    newvalue(:absent) do
      provider.destroy
    end

    newvalue(:enabled) do
      provider.setState(:enabled)
    end

    newvalue(:disabled) do
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end

    def insync?(is)
      @should.each { |should|
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled
            return (provider.getState == :enabled)
          when :disabled
            return (provider.getState == :disabled)
        end
      }
    end
  end

  newparam(:name) do
    desc 'Policy description'
    isnamevar
  end

  newproperty(:src_address) do
    desc 'Source Address'
  end

  newproperty(:src_port) do
    desc 'Source port'
  end

  newproperty(:dst_address) do
    desc 'Destination Address'
  end

  newproperty(:dst_port) do
    desc 'Destination Port'
  end

  newproperty(:protocol) do
    desc "The IP packet protocol to match"
    newvalues(*%w{
      all dccp ddp egp encap etherip ggp gre hmp icmp icmpv6 idpr-cmtp igmp ipencap ipip ipsec-ah ipsec-esp ipv6 ipv6-frag ipv6-nonxt
      ipv6-opts ipv6-route iso-tp4 l2tp ospf pim pup rdp rspf rsvp sctp st tcp udp udp-lite vmtp vrrp xns-idp xtp
    })
  end

  newproperty(:template, boolean: true, parent: Puppet::Property::Boolean) do
    desc 'Whether this is a policy template or a peer-specific policy. Templates use only the following properties: group, src_address, dst_address, protocol, proposal'
    defaultto true
  end

  newproperty(:group) do
    desc 'The template group that includes this policy template'
    validate do |value|
      if value && !resource[:template]
        raise ArgumentError, "only policy templates can belong to template groups"
      end
    end
  end

  newproperty(:action) do
    desc 'Specifies what to do with the packet matched by the policy.'
    newvalues(:encrypt,:discard,:none)
  end

  newproperty(:ipsec_protocols) do
    newvalues(:esp,:ah)
  end

  newproperty(:peer) do
    desc 'the peer this policy applies to, if this is not a template'
    validate do |value|
      if value && resource[:template]
        raise ArgumentError, "do not specify a peer for a policy template"
      end
    end
  end

  newproperty(:proposal) do
    desc 'the IPSec proposal to use'
  end

  newproperty(:level) do
    newvalues(:require,:unique,:use)
  end

  newproperty(:tunnel, boolean: true, parent: Puppet::Property::Boolean) do
  end

  autorequire(:mikrotik_ipsec_peer) { self[:peer] }
  autorequire(:mikrotik_ipsec_proposal) { self[:proposal] }
  autorequire(:mikrotik_ipsec_group) { self[:group] }
end


File: /lib\puppet\type\mikrotik_ipsec_profile.rb
require 'puppet/property/boolean'

Puppet::Type.newtype(:mikrotik_ipsec_profile) do
  apply_to_all

  ensurable

  newparam(:name) do
    desc 'Profile description'
    isnamevar
  end

  newproperty(:dh_group, :array_matching => :all) do
    newvalues(*%w{ec2n155 ec2n185 ecp256 ecp384 ecp521 modp768 modp1024 modp1536 modp2048 modp3072 modp4096 modp6144 modp8192})
  end

  newproperty(:dpd_interval) do
  end

  newproperty(:dpd_maximum_failures) do
  end

  newproperty(:enc_algorithm, :array_matching => :all) do
    newvalues(*%w{3des aes-128 aes-192 aes-256 blowfish camellia-128 camellia-192 camellia-256 des})
  end

  newproperty(:hash_algorithm) do
    newvalues(:md5, :sha1, :sha256, :sha384, :sha512)
  end

  newproperty(:lifebytes) do
  end

  newproperty(:lifetime) do
  end

  newproperty(:nat_traversal, boolean: true, parent: Puppet::Property::Boolean) do
  end

  newproperty(:prf_algorithm) do
    newvalues(:auto, :sha1, :sha256, :sha384, :sha512)
    defaultto :auto
  end

  newproperty(:proposal_check) do
    newvalues(:claim,:exact,:obey,:strict)
  end
end


File: /lib\puppet\type\mikrotik_ipsec_proposal.rb
Puppet::Type.newtype(:mikrotik_ipsec_proposal) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'Proposal name'
    isnamevar
  end

  newproperty(:auth_algorithms, array_matching: :all) do
    newvalues(:md5,:null,:sha1,:sha256,:sha512)
  end

  newproperty(:comment) do
  end

  newproperty(:enc_algorithms, array_matching: :all) do
    newvalues(*%w{
      3des des
      aes-128-cbc aes-128-ctr aes-128-gcm
      aes-192-cbc aes-192-ctr aes-192-gcm
      aes-256-cbc aes-256-ctr aes-256-gcm
      blowfish twofish
      camellia-128 camellia-192 camellia-256
      null
    })
  end
  
  newproperty(:lifetime) do
  end

  newproperty(:pfs_group) do
  end
end


File: /lib\puppet\type\mikrotik_ipv6_address.rb
Puppet::Type.newtype(:mikrotik_ipv6_address) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:address) do
    desc 'IP Address (CIDR notation)'
    isnamevar
  end
  
  newproperty(:interface) do
    desc 'Interface to attach the IP address on.'
  end
  
  newproperty(:advertise) do
    desc 'Whether to advertise (RA) the network.'
    newvalues(true, false)
  end
  
  newproperty(:eui64) do
    desc 'Whether to set up full address using MAC address.'
    newvalues(true, false)
  end
  
  newproperty(:from_pool) do
    desc 'The DHCP pool to use a network from.'
  end
end


File: /lib\puppet\type\mikrotik_ipv6_address_list.rb
Puppet::Type.newtype(:mikrotik_ipv6_address_list) do  
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end

  newparam(:name) do
    desc 'The address list name'
    isnamevar
  end

  newproperty(:addresses, :array_matching => :all) do
    desc 'The IP addresses assigned to the list'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
end


File: /lib\puppet\type\mikrotik_ipv6_firewall_rule.rb
Puppet::Type.newtype(:mikrotik_ipv6_firewall_rule) do
  apply_to_all
  
  ensurable do
    newvalue(:present) do
      provider.create
    end

    newvalue(:absent) do
      provider.destroy
    end

    newvalue(:enabled) do
      provider.create
      provider.setState(:enabled)
    end

    newvalue(:disabled) do
      provider.create
      provider.setState(:disabled)
    end

    defaultto :present
    
    def retrieve
      provider.getState
    end

    def insync?(is)
      @should.each { |should| 
        case should
        when :present
          return (provider.getState != :absent)
        when :absent
          return (provider.getState == :absent)
        when :enabled
          return (provider.getState == :enabled)
        when :disabled
          return (provider.getState == :disabled)
        end
      }
    end
  end

  newparam(:name) do
    desc 'The unique identifier for the rule'
    isnamevar
  end

  newparam(:table) do
    desc 'The table to which the rule applies (filter,mangle)'
  end
  
  # General
  newproperty(:chain) do
    desc 'The chain to which the rule applies (input,output,filter,prerouting,...)'
  end

  newproperty(:chain_order) do
    desc 'Order number inside the chain (starts at 1).'
  end

  newproperty(:src_address) do  # src-address
    desc 'Source address with mask'
  end
  
  newproperty(:dst_address) do  # dst-address
    desc 'Destination address with mask'
  end

  newproperty(:protocol) do  # protocol
    desc 'Protocol name or number'
  end

  newproperty(:src_port) do  # src-port
    desc 'Source-port number'
  end

  newproperty(:dst_port) do  # dst-port
    desc 'Destination port number or range'
  end

  newproperty(:port) do  # port
    desc 'Source Or Destination port number or range'
  end
  
#  newproperty(:p2p) do  # p2p
#    desc 'P2P program to match'
#  end  

  newproperty(:in_interface) do  # in-interface
    desc 'Interface the packet has entered the router through'
  end

  newproperty(:out_interface) do  # out-interface
    desc 'Interface the packet has leaved the router through'
  end

  newproperty(:in_interface_list) do  # in-interface-list
    desc 'Interface List the packet has entered the router through'
  end

  newproperty(:out_interface_list) do  # out-interface-list
    desc 'Interface List the packet has leaved the router through'
  end

  newproperty(:packet_mark) do  # packet-mark
    desc 'Matches packets marked via mangle facility with particular packet mark'
  end

  newproperty(:connection_mark) do  # connection-mark
    desc 'Matches packets marked via mangle facility with particular connection mark'
  end

#  newproperty(:routing_mark) do  # routing-mark
#    desc 'Matches packets marked by mangle facility with particular routing mark'
#  end
#
#  newproperty(:routing_table) do  # routing-table
#    desc 'Matches packets on particular routing table'
#  end

  newproperty(:connection_type) do  # connection-type
    desc 'Match packets with given connection type'
  end

  newproperty(:connection_state) do  # connection-state
    desc 'Interprets the connection tracking analysis data for a particular packet'
  end

#  newproperty(:connection_nat_state) do  # connection-nat-state
#    desc 'Interprets the NAT connection tracking analysis data for a particular packet'
#  end

  # Advanced
  newproperty(:src_address_list) do  # src-address-list
    desc 'Matches source address of a packet against user-defined address list'
  end
  
  newproperty(:dst_address_list) do  # dst-address-list
    desc 'Destination address list name in which packet place'
  end
  
#  newproperty(:layer7_protocol) do  # layer7-protocol
#    desc 'TODO'
#  end
  
  newproperty(:content) do  # content
    desc 'The text packets should contain in order to match the rule'
  end
  
  newproperty(:connection_bytes) do  # connection-bytes
    desc 'Match packets with given bytes or byte range'
  end
  
  newproperty(:connection_rate) do  # connection-rate
    desc 'TODO'
  end
  
  newproperty(:per_connection_classifier) do  # per-connection-classifier
    desc 'TODO'
  end
  
  newproperty(:src_mac_address) do  # src-mac-address
    desc 'Source MAC address'
  end
  
  newproperty(:in_bridge_port) do  # in-bridge-port
    desc 'TODO'
  end
  
  newproperty(:out_bridge_port) do  # out-bridge-port
    desc 'Matches the bridge port physical output device added to a bridge device'
  end
  
  newproperty(:in_bridge_port_list) do  # in-bridge-port-list
    desc 'TODO'
  end
  
  newproperty(:out_bridge_port_list) do  # out-bridge-port-list
    desc 'TODO'
  end
  
  newproperty(:ipsec_policy) do  # ipsec-policy
    desc 'TODO'
  end
  
  newproperty(:ingress_priority) do  # ingress-priority
    desc 'TODO'
  end
  
  newproperty(:priority) do  # priority
    desc 'TODO'
  end
  
  newproperty(:dscp) do  # dscp
    desc 'TODO'
  end
  
  newproperty(:tcp_mss) do  # tcp-mss
    desc 'TCP Maximum Segment Size value'
  end
  
  newproperty(:packet_size) do  # packet-size
    desc 'Packet size or range in bytes'
  end
  
  newproperty(:random) do  # random
    desc 'Match packets randomly with given propability'
  end
  
  newproperty(:tcp_flags) do  # tcp-flags
    desc 'TCP flags to match'
  end
  
#  newproperty(:ipv4_options) do  # ipv4-options
#    desc 'Match ipv4 header options'
#  end
#  
#  newproperty(:ttl) do  # ttl
#    desc 'TODO'
#  end
  
  # Extra  
  newproperty(:connection_limit) do  # connection-limit
    desc 'Restrict connection limit per address or address block'
  end
  
  newproperty(:limit) do  # limit
    desc 'Setup burst, how many times to use it in during time interval measured in seconds'
  end
  
  newproperty(:dst_limit) do  # dst-limit
    desc 'Packet limitation per time with burst to dst-address, dst-port or src-address'
  end
  
  newproperty(:nth) do  # nth
    desc 'Match nth packets received by the rule'
  end
  
  newproperty(:time) do  # time
    desc 'Packet arrival time and date or locally generated packets departure time and date'
  end
  
  newproperty(:src_address_type) do  # src-address-type
    desc 'Source IP address type'
  end
  
  newproperty(:dst_address_type) do  # dst-address-type
    desc 'Destination address type'
  end
  
#  newproperty(:psd) do  # psd
#    desc 'Detect TCP un UDP scans'
#  end
#  
#  newproperty(:hotspot) do  # hotspot
#    desc 'Matches packets received from clients against various Hot-Spot'
#  end
#  
#  newproperty(:fragment) do  # fragment
#    desc 'TODO'
#  end
      
  # Action    
  newproperty(:action) do
    desc 'Action to undertake if the packet matches the rule'
  end
  
  newproperty(:log) do  # log
    desc 'TODO'
  end
  
  newproperty(:log_prefix) do  # log-prefix
    desc 'Creates all logs with specific prefix'
  end
  
  newproperty(:jump_target) do  # jump-target
    desc 'Name of the target chain, if the action=jump is used'
  end

  newproperty(:address_list) do  # address-list
    desc 'Address list in which marked address put'
  end
  
  newproperty(:address_list_timeout) do  # address-list-timeout
    desc 'Time interval after which address remove from address list'
  end
  
  newproperty(:reject_with) do  # reject-with
    desc 'Alters the reply packet of reject action'
  end
  
#  newproperty(:to_addresses) do  # to-addresses
#    desc 'Address or address range to replace original address of an IP packet with'
#  end
#  
#  newproperty(:to_ports) do  # to-ports
#    desc 'Port or port range to replace original port of an IP packet with'
#  end

  newproperty(:new_connection_mark) do  # new-connection-mark
    desc 'Specify the new value of the connection mark to be used in conjunction with action=mark-connection'
  end
  
  newproperty(:new_dscp) do  # new-dscp
    desc 'TODO'
  end
  
  newproperty(:new_mss) do  # new-mss
    desc 'Specify MSS value to be used in conjunction with action=change-mss'
  end
  
  newproperty(:new_packet_mark) do  # new-packet-mark
    desc 'Specify the new value of the packet mark to be used in conjunction with action=mark-packet'
  end
  
#  newproperty(:new_priority) do  # new-priority
#    desc 'TODO'
#  end
#  
#  newproperty(:new_routing_mark) do  # new-routing-mark
#    desc 'Specify the new value of the routing mark used in conjunction with action=mark-routing'
#  end
#  
#  newproperty(:new_ttl) do  # new-ttl
#    desc 'Specify the new TTL field value used in conjunction with action=change-ttl'
#  end
#  
#  newproperty(:route_dst) do  # route-dst
#    desc 'TODO'
#  end
#  
#  newproperty(:sniff_id) do  # sniff-id
#    desc 'TODO'
#  end
#  
#  newproperty(:sniff_target) do  # sniff-target
#    desc 'TODO'
#  end
#  
#  newproperty(:sniff_target_port) do  # sniff-target-port
#    desc 'TODO'
#  end
  
  # TODO: headers, hop-limit, icmp-options
end


File: /lib\puppet\type\mikrotik_ipv6_nd_interface.rb
Puppet::Type.newtype(:mikrotik_ipv6_nd_interface) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:interface) do
    desc 'Interface to run Neighbor Discovery on'
    isnamevar
  end
  
  newproperty(:ra_interval) do  # ra-interval
    desc 'Interval (s) for Router Advertisements.'
  end
  
  newproperty(:ra_delay) do  # ra-delay
    desc 'Delay (s) for Router Advertisements.'
  end

  newproperty(:mtu) do
    desc 'MTU.'
  end

  newproperty(:reachable_time) do  # reachable-time
    desc 'Reachable Time (s).'
  end

  newproperty(:retransmit_interval) do  # retransmit-interval
    desc 'Retransmit Interval (s).'
  end

  newproperty(:ra_lifetime) do  # ra-lifetime
    desc 'RA Lifetime.'
  end

  newproperty(:hop_limit) do  # hop-limit
    desc 'Hop Limit.'
  end
  
  newproperty(:advertise_mac) do  # advertise-mac-address
    desc 'Whether to advertise DNS in the RA'
    newvalues(true, false)
  end

  newproperty(:advertise_dns) do  # advertise-dns
    desc 'Whether to advertise DNS in the RA'
    newvalues(true, false)
  end
  
  newproperty(:managed_address_config) do  # managed-address-configuration
    desc 'Whether to advertise DNS in the RA'
    newvalues(true, false)
  end
  
  newproperty(:other_config) do  # other-configuration
    desc 'Whether to advertise DNS in the RA'
    newvalues(true, false)
  end
end


File: /lib\puppet\type\mikrotik_ipv6_pool.rb
Puppet::Type.newtype(:mikrotik_ipv6_pool) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'IPv6 pool name'
    isnamevar
  end

  newproperty(:prefix) do
    desc 'IPv6 Prefix (parent subnet)'
  end
  
  newproperty(:prefix_length) do
    desc 'Prefix Length to allocate from pool. Default = 64'
  end
end


File: /lib\puppet\type\mikrotik_ipv6_route.rb
Puppet::Type.newtype(:mikrotik_ipv6_route) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled
            return (provider.getState == :enabled)
          when :disabled
            return (provider.getState == :disabled)
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Route description'
    isnamevar
  end

  newproperty(:dst_address) do
    desc 'Destination address'
  end
  
  newproperty(:gateway) do
    desc 'Gateway address'
  end

  newproperty(:check_gateway) do
    desc 'Whether to check nexthop with ARP or Ping request.'
    newvalues(:ping)
  end

  newproperty(:type) do
    desc 'Route type'
    newvalues('unicast', 'unreachable')
  end

  newproperty(:distance) do
    desc 'Administrative distance of the route'
  end

  newproperty(:scope) do
    desc 'Route Scope'
  end

  newproperty(:target_scope) do
    desc 'Target Route Scope'
  end

  newproperty(:bgp_as_path) do
    desc 'AS Path for BGP (advertisement ?)'
  end

  newproperty(:bgp_local_pref) do
    desc 'Local Preference for BGP (advertisement ?)'
  end

  newproperty(:bgp_prepend) do
    desc 'Prepend for BGP (advertisement ?)'
  end

  newproperty(:bgp_med) do
    desc 'MED for BGP (advertisement ?)'
  end

  newproperty(:bgp_atomic_aggregate) do
    desc 'Atomic Aggregate for BGP (advertisement ?)'
  end

  newproperty(:bgp_origin) do
    desc 'Origin for BGP (advertisement ?)'
  end

  newproperty(:route_tag) do
    desc 'Route Tag (?)'
  end

  newproperty(:bgp_communities) do
    desc 'BGP Communities for BGP (advertisement ?)'
  end  
end


File: /lib\puppet\type\mikrotik_ipv6_settings.rb
Puppet::Type.newtype(:mikrotik_ipv6_settings) do
  apply_to_all
  
  # Only 1 set of settings that is always enabled. NOT ensurable 
  
  newparam(:name) do
    desc 'Name should be -ipv6-'
    isnamevar
  end

  newproperty(:forward) do
    desc 'Whether to enable IPv6 Forwarding.'
    newvalues(true, false)
  end
  
  newproperty(:accept_redirects) do
    desc 'Whether to accept redirects.'
    newvalues(true, false)
  end

  newproperty(:accept_router_advertisements) do
    desc 'Whether to accept RAs.'
    newvalues('no', 'yes', 'yes-if-forwarding-disabled')
  end

  newproperty(:max_neighbor_entries) do
    desc 'Maximum neighbors. Default: 8192'
  end
end


File: /lib\puppet\type\mikrotik_ip_address.rb
Puppet::Type.newtype(:mikrotik_ip_address) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:address) do
    desc 'IP Address (CIDR notation)'
    isnamevar
  end
  
  newproperty(:interface) do
    desc 'Interface to attach the IP address on.'
  end

  # Not used much?
  #broadcast netmask network
end


File: /lib\puppet\type\mikrotik_ip_hotspot.rb
Puppet::Type.newtype(:mikrotik_ip_hotspot) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'The Hotspot Server name'
    isnamevar
  end
  
  newproperty(:address_pool) do
    desc 'IP address pool name'
  end
  
  newproperty(:addresses_per_mac) do
    desc 'Maximum count of IP addresses for one MAC address'
  end
  
  newproperty(:idle_timeout) do
    desc 'Maximal period of inactivity for unauthorized clients'
  end
  
  newproperty(:interface) do
    desc 'Interface to run HotSpot service on'
  end
  
  newproperty(:keepalive_timeout) do
    desc 'Keepalive timeout for unauthorized clients'
  end

  newproperty(:login_timeout) do
    desc 'Login timeout when authenticating'
  end

  newproperty(:profile) do
    desc 'Configuration for hotspot server'
  end  
end


File: /lib\puppet\type\mikrotik_ip_hotspot_profile.rb
Puppet::Type.newtype(:mikrotik_ip_hotspot_profile) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'The Hotspot Profile name'
    isnamevar
  end
  
  newproperty(:dns_name) do
    desc 'DNS name of the HotSpot server'
  end
  
  newproperty(:hotspot_address) do
    desc 'IP address for HotSpot service'
  end
  
  newproperty(:html_directory) do
    desc 'Name of the directory, which stores the HTML servlet pages'
  end
  
  newproperty(:http_cookie_lifetime) do
    desc 'Validity time of HTTP cookies'
  end
  
  newproperty(:login_by, :array_matching => :all) do
    desc 'Authentication method to use'
  
    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:nas_port_type) do
    desc 'NAS Port Type ID (RADIUS)'
  end
  
  newproperty(:radius_accounting) do
    desc 'Enable or disable accounting'
    newvalues(true, false)
  end
  
  newproperty(:radius_default_domain) do
    desc 'When using split domain, set this domain if none set'
  end

  newproperty(:radius_interim_update) do
    desc 'Interim-Update time interval'
  end
  
  newproperty(:radius_location_id) do
    desc 'RADIUS Location ID'
  end
  
  newproperty(:radius_location_name) do
    desc 'RADIUS Location Name'
  end
  
  newproperty(:split_user_domain) do
    desc 'Whether to split username from domain name with user@domain or domain\user'
  end
  
  newproperty(:trial_uptime_limit) do
    desc 'Maximum uptime in trial mode'
  end
  
  newproperty(:trial_uptime_reset) do
    desc 'When to reset user from using trial again'
  end
  
  newproperty(:trial_user_profile) do
    desc 'User Profile to apply to trial user.'
  end
  
  newproperty(:use_radius) do
    desc 'Use RADIUS for AAA'
    newvalues(true, false)
  end
end


File: /lib\puppet\type\mikrotik_ip_pool.rb
Puppet::Type.newtype(:mikrotik_ip_pool) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'IP pool name'
    isnamevar
  end

  newproperty(:ranges, :array_matching => :all) do
    desc 'IP ranges with addresses that belong to pool'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:next_pool) do
    desc 'Next IP pool to use if current pool is fully used.'
  end
end


File: /lib\puppet\type\mikrotik_ip_route.rb
Puppet::Type.newtype(:mikrotik_ip_route) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled
            return (provider.getState == :enabled)
          when :disabled
            return (provider.getState == :disabled)
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Route description'
    isnamevar
  end

  newproperty(:dst_address) do
    desc 'Destination address'
  end
  
  newproperty(:gateway) do
    desc 'Gateway address'
  end

  newproperty(:check_gateway) do
    desc 'Whether to check nexthop with ARP or Ping request.'
    newvalues(:arp, :ping)
  end

  newproperty(:type) do
    desc 'Route type'
    newvalues('unicast', 'blackhole', 'prohibit', 'unreachable')
  end

  newproperty(:distance) do
    desc 'Administrative distance of the route'
  end

  newproperty(:scope) do
    desc 'Route Scope'
  end

  newproperty(:target_scope) do
    desc 'Target Route Scope'
  end

  newproperty(:routing_mark) do
    desc 'Routing table this route belong in'
  end

  newproperty(:pref_src) do
    desc 'Preferred Source for the route'
  end

  newproperty(:bgp_as_path) do
    desc 'AS Path for BGP (advertisement ?)'
  end

  newproperty(:bgp_local_pref) do
    desc 'Local Preference for BGP (advertisement ?)'
  end

  newproperty(:bgp_prepend) do
    desc 'Prepend for BGP (advertisement ?)'
  end

  newproperty(:bgp_med) do
    desc 'MED for BGP (advertisement ?)'
  end

  newproperty(:bgp_atomic_aggregate) do
    desc 'Atomic Aggregate for BGP (advertisement ?)'
  end

  newproperty(:bgp_origin) do
    desc 'Origin for BGP (advertisement ?)'
  end

  newproperty(:route_tag) do
    desc 'Route Tag (?)'
  end

  newproperty(:bgp_communities) do
    desc 'BGP Communities for BGP (advertisement ?)'
  end
  
  # Not in Winbox:
    # vrf_interface
end


File: /lib\puppet\type\mikrotik_ip_route_rule.rb
Puppet::Type.newtype(:mikrotik_ip_route_rule) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Rule description'
    isnamevar
  end

  newproperty(:src_address) do
    desc 'Source Address'
  end

  newproperty(:dst_address) do
    desc 'Destination Address'
  end

  newproperty(:routing_mark) do
    desc 'Routing mark set by firewall mangle'
  end

  newproperty(:interface) do
    desc 'Interface of incoming traffic'
  end

  newproperty(:action) do
    desc 'Action to take with selected traffic'
    newvalues(:lookup, :drop, :unreachable)
  end

  newproperty(:table) do
    desc 'Table to lookup routes in if action == "lookup"'
  end
  
#  newproperty(:sequence) do
#    desc 'Ordering of the rule'
#  end
end


File: /lib\puppet\type\mikrotik_ip_route_vrf.rb
Puppet::Type.newtype(:mikrotik_ip_route_vrf) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:routing_mark) do
    desc 'Routing Mark/Table Name'
    isnamevar
  end
  
  newproperty(:interfaces, :array_matching => :all) do
    desc 'Interfaces to attach to VRF'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:route_distinguisher) do
    desc 'Route Destinguisher (BGP/MPLS ?)'
  end
  
  newproperty(:import_route_targets, :array_matching => :all) do
    desc 'Import Route Targets (BGP/MPLS ?)'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:export_route_targets, :array_matching => :all) do
    desc 'Export Route Targets (BGP/MPLS ?)'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  # Not in Winbox:
    # bgp-nexthop
end


File: /lib\puppet\type\mikrotik_ip_service.rb
Puppet::Type.newtype(:mikrotik_ip_service) do
  apply_to_all
  
  ensurable do
    defaultto :present

    newvalue(:present)
    
    newvalue(:enabled) do
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return true
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'The IP service name'
    isnamevar
  end

  newproperty(:port) do
    desc 'The port on which the service is listening'
  end

  newproperty(:addresses, :array_matching => :all) do
    desc 'The IP addresses assigned to the list'
    
    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
end


File: /lib\puppet\type\mikrotik_ip_settings.rb
Puppet::Type.newtype(:mikrotik_ip_settings) do
  apply_to_all
  
  # Only 1 set of settings that is always enabled. NOT ensurable 
  
  newparam(:name) do
    desc 'Name should be -ip-'
    isnamevar
  end

  newproperty(:rp_filter) do
    desc 'Setting for filtering Reverse Path. Can be -no-,-loose- or -strict-.'
    newvalues(:loose, :no, :strict)
  end
end


File: /lib\puppet\type\mikrotik_logging_action.rb
Puppet::Type.newtype(:mikrotik_logging_action) do
  apply_to_all

  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'Logging action name'
    isnamevar
  end
  
  newproperty(:target) do
    desc 'The log target (type)'
    newvalues(:memory, :disk, :echo, :remote, :email)
    defaultto :remote
  end
  
  newproperty(:remote) do
    desc 'The hostname of the remote syslog server.'
  end
  
  newproperty(:remote_port) do
    desc 'The port of the remote syslog server.'
  end
  
  newproperty(:src_address) do
    desc 'The source IP that should be used in the remote syslog connection.'
  end
  
  newproperty(:bsd_syslog) do
    desc 'Whether to format the logs in BSD Syslog format'
    newvalues(true, false)
  end
  
  newproperty(:syslog_facility) do
    desc 'BSD Syslog Facility'
  end

  newproperty(:syslog_severity) do
    desc 'BSD Syslog Severity'
  end
    
  # 'memory':
    # memory-lines
    # memory-stop-on-full
  # 'disk':
    # disk-file-name
    # disk-lines-per-file
    # disk-file-count
    # disk-stop-on-full
  # 'echo':
    # remember
  # 'email':
    # email-to
    # email-start-tls
end


File: /lib\puppet\type\mikrotik_logging_rule.rb
Puppet::Type.newtype(:mikrotik_logging_rule) do
  apply_to_all

  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'Mikrotik does not have a title ID for this object. Restricted to topic1,topic2_action'
    isnamevar
  end
  
  newproperty(:topics, :array_matching => :all) do
    desc 'The topics that will be filtered by this rule.'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort   
      else
        is == @should
      end
    end    
  end
  
  newproperty(:action) do
    desc 'The action that the logs will be sent to.'
  end
  
  newproperty(:prefix) do
    desc 'Prefix the logs by this string.'
  end
end


File: /lib\puppet\type\mikrotik_mpls_ldp.rb
Puppet::Type.newtype(:mikrotik_mpls_ldp) do
  apply_to_all
  
  ensurable do
    defaultto :present

    newvalue(:present)
        
    newvalue(:enabled) do
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return true
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Name should be -ldp-'
    isnamevar
  end

  newproperty(:lsr_id) do
    desc 'MPLS LSR ID'
  end

  newproperty(:transport_address) do
    desc 'Transport address for LDP'
  end

  newproperty(:path_vector_limit) do
    desc 'Path Vector Limit'
  end

  newproperty(:hop_limit) do
    desc 'Hop Limit'
  end

  newproperty(:loop_detect) do
    desc 'Whether to enable loop detect.'
  end

  newproperty(:use_explicit_null) do
    desc 'Whether to enable use of explicit null.'
  end

  newproperty(:distribute_for_default_route) do
    desc 'Whether to enable distribution of default route.'
  end
end


File: /lib\puppet\type\mikrotik_mpls_ldp_interface.rb
Puppet::Type.newtype(:mikrotik_mpls_ldp_interface) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Interface name'
    isnamevar
  end

  newproperty(:hello_interval) do
    desc 'MPLS Interface Hello Interval'
    #defaultto "5s"
  end
  
  newproperty(:hold_time) do
    desc 'MPLS Interface Hold Time'
    #defaultto "15s"
  end

  newproperty(:transport_address) do
    desc 'Transport address for LDP'
  end

  newproperty(:accept_dynamic_neighbors) do
    desc 'Whether to accept dynamic neighbors (Default = true)'
    newvalues(true, false)
    defaultto true
  end
end


File: /lib\puppet\type\mikrotik_mpls_te_interface.rb
Puppet::Type.newtype(:mikrotik_mpls_te_interface) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Interface name'
    isnamevar
  end

  newproperty(:bandwidth) do
    desc 'Interface Bandwidth'
  end

  newproperty(:k_factor) do
    desc 'Value used to calculate RSVP timeout.'
  end
  
  newproperty(:refresh_time) do
    desc 'Interval in which RSVP Path messages are sent out.'
  end
  
  # Less frequently used options:
  ## resource-class -- 
  ## use-udp -- 
  ## blockade-k-factor -- 
  ## te-metric -- 
  ## igp-flood-period -- 
  ## up-flood-thresholds -- 
  ## down-flood-thresholds -- 
  
  ## comment -- Not visible on Winbox?
end


File: /lib\puppet\type\mikrotik_mpls_te_path.rb
Puppet::Type.newtype(:mikrotik_mpls_te_path) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'Path name'
    isnamevar
  end

  newproperty(:use_cspf) do
    desc 'Whether to use dynamic OSPF paths. Default: true'   # Winbox behaviour does not match console/api
    newvalues(true, false)
  end
  
  newproperty(:record_route) do
    desc 'Whether to record route'
    newvalues(true, false)
  end

  newproperty(:hops, :array_matching => :all) do
    desc 'List of static hops. Format: IP:loose/strict'
        
    # DO NOT SORT !
    #    def insync?(is)
    #      if is.is_a?(Array) and @should.is_a?(Array)
    #        is.sort == @should.sort
    #      else
    #        is == @should
    #      end
    #    end
  end
  
  # Less frequently used options:
  ## affinity-include-all -- 
  ## affinity-include-any -- 
  ## affinity-exclude -- 
  ## reoptimize-interval -- Used by CSPF 

  ## comment -- Not visible on Winbox?
end


File: /lib\puppet\type\mikrotik_ospfv3_area.rb
Puppet::Type.newtype(:mikrotik_ospfv3_area) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'OSPFv3 Area Name'
    isnamevar
  end
  
  newproperty(:area_id) do
    desc 'The OSPFv3 Area ID (IP).'
  end
  
  newproperty(:instance) do
    desc 'The OSPFv3 instance this area belongs to.'
  end

  newproperty(:area_type) do
    desc 'The type of the OSPFv3 Area.'
    newvalues('default', 'stub', 'nssa')
  end
end


File: /lib\puppet\type\mikrotik_ospfv3_instance.rb
Puppet::Type.newtype(:mikrotik_ospfv3_instance) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }
    end
  end
  
  newparam(:name) do
    desc 'OSPFv3 Instance name'
    isnamevar
  end

  newproperty(:router_id) do
    desc 'The Router ID.'
  end
  
  newproperty(:distribute_default) do
    desc 'Whether to redistribute default routes to OSPF.'
    newvalues('never', 'if-installed-as-type-1', 'if-installed-as-type-2', 'always-as-type-1', 'always-as-type-2')
  end
    
  newproperty(:redistribute_connected) do
    desc 'Whether to redistribute connected routes to OSPF.'
    newvalues('no', 'as-type-1', 'as-type-2')
  end

  newproperty(:redistribute_static) do
    desc 'Whether to redistribute static routes to OSPF.'
    newvalues('no', 'as-type-1', 'as-type-2')
  end
  
  newproperty(:redistribute_ospf) do
    desc 'Whether to redistribute OSPF routes from other instances to OSPF.'
    newvalues('no', 'as-type-1', 'as-type-2')
  end
  
  newproperty(:redistribute_bgp) do
    desc 'Whether to redistribute BGP routes to OSPF.'
    newvalues('no', 'as-type-1', 'as-type-2')
  end
  
  newproperty(:redistribute_rip) do
    desc 'Whether to redistribute RIP routes to OSPF.'
    newvalues('no', 'as-type-1', 'as-type-2')
  end

  newproperty(:metric_default) do
    desc 'The metric to use when redistributing default routes on this instance.'
  end

  newproperty(:metric_connected) do
    desc 'The metric to use when redistributing connected routes on this instance.'
  end

  newproperty(:metric_static) do
    desc 'The metric to use when redistributing static routes on this instance.'
  end

  newproperty(:metric_bgp) do
    desc 'The metric to use when redistributing BGP routes on this instance.'
  end

  newproperty(:metric_ospf) do
    desc 'The metric to use when redistributing OSPF routes from other instances on this instance.'
  end
  
  newproperty(:metric_rip) do
    desc 'The metric to use when redistributing RIP routes on this instance.'
  end
end


File: /lib\puppet\type\mikrotik_ospfv3_interface.rb
Puppet::Type.newtype(:mikrotik_ospfv3_interface) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }
    end
  end
  
  newparam(:name) do
    desc 'OSPFv3 Interface'
    isnamevar
  end

  newproperty(:area) do
    desc 'The OSPFv3 area to assign the interface to.'
  end  
  
  newproperty(:cost) do
    desc 'The Cost of the OSPFv3 interface.'
  end
  
  newproperty(:priority) do
    desc 'The Priority of the OSPF interface.'
  end
    
  newproperty(:network_type) do # network-type
    desc 'The network type (default, broadcast, nbma, point-to-point, ptmp)'
    newvalues(:default, :broadcast, :nbma, 'point-to-point', :ptmp)
    defaultto :broadcast
  end
  
  newproperty(:passive) do
    desc 'Whether the interface is passive (not participating in OSPF)'
    newvalues(false, true)
    defaultto false
  end
  
  newproperty(:use_bfd) do # use-bfd
    desc 'Whether to enable BFD on the interface for the OSPF process'
    newvalues(false, true)
    defaultto false
  end
end


File: /lib\puppet\type\mikrotik_ospf_area.rb
Puppet::Type.newtype(:mikrotik_ospf_area) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'OSPF Area Name'
    isnamevar
  end
  
  newproperty(:area_id) do
    desc 'The OSPF Area ID (IP).'
  end
  
  newproperty(:instance) do
    desc 'The OSPF instance this area belongs to.'
  end

  newproperty(:area_type) do
    desc 'The type of the OSPF Area.'
    newvalues('default', 'stub', 'nssa')
  end
end


File: /lib\puppet\type\mikrotik_ospf_area_range.rb
require 'puppet/property/boolean'

Puppet::Type.newtype(:mikrotik_ospf_area_range) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'the network prefix of this range'
    isnamevar
  end
  
  newparam(:area) do
    desc 'The OSPF area associated with this range (name, not id)'
    isnamevar
  end
  
  newproperty(:cost) do
    desc "The cost of the summary LSA this range will create. 'calculated' will use the largest cost of all routes in the range" 
    newvalues(/^\d+$/,:calculated)
    defaultto :calculated
  end

  newproperty(:advertise, boolean: true, parent: Puppet::Property::Boolean) do
    desc 'Whether to create the summary LSA and advertise it to adjacent areas'
    defaultto true
  end

  newproperty(:comment) do
    desc "A comment describing this area range"
  end

  autorequire(:mikrotik_ospf_area) { self[:area] }

  # the actual 'title' of the resource is just the 'range' parameter;
  # the 'area' parameter must be set explicitly, not as part of the title.
  # This is exactly how the official 'package' resource works.
  def self.title_patterns
    [ [ /(.*)/, [ [:name] ] ] ]
  end
end


File: /lib\puppet\type\mikrotik_ospf_instance.rb
Puppet::Type.newtype(:mikrotik_ospf_instance) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }
    end
  end
  
  newparam(:name) do
    desc 'OSPF Instance name'
    isnamevar
  end

  newproperty(:router_id) do
    desc 'The Router ID.'
  end
  
  newproperty(:distribute_default) do
    desc 'Whether to redistribute default routes to OSPF.'
    newvalues('never', 'if-installed-as-type-1', 'if-installed-as-type-2', 'always-as-type-1', 'always-as-type-2')
  end
    
  newproperty(:redistribute_connected) do
    desc 'Whether to redistribute connected routes to OSPF.'
    newvalues('no', 'as-type-1', 'as-type-2')
  end

  newproperty(:redistribute_static) do
    desc 'Whether to redistribute static routes to OSPF.'
    newvalues('no', 'as-type-1', 'as-type-2')
  end
  
  newproperty(:redistribute_ospf) do
    desc 'Whether to redistribute OSPF routes from other instances to OSPF.'
    newvalues('no', 'as-type-1', 'as-type-2')
  end
  
  newproperty(:redistribute_bgp) do
    desc 'Whether to redistribute BGP routes to OSPF.'
    newvalues('no', 'as-type-1', 'as-type-2')
  end
  
  newproperty(:redistribute_rip) do
    desc 'Whether to redistribute RIP routes to OSPF.'
    newvalues('no', 'as-type-1', 'as-type-2')
  end

  newproperty(:in_filter) do
    desc 'The input filter applying on this instance.'
  end

  newproperty(:out_filter) do
    desc 'The output filter applying on this instance.'
  end

  newproperty(:metric_default) do
    desc 'The metric to use when redistributing default routes on this instance.'
  end

  newproperty(:metric_connected) do
    desc 'The metric to use when redistributing connected routes on this instance.'
  end

  newproperty(:metric_static) do
    desc 'The metric to use when redistributing static routes on this instance.'
  end

  newproperty(:metric_bgp) do
    desc 'The metric to use when redistributing BGP routes on this instance.'
  end

  newproperty(:metric_ospf) do
    desc 'The metric to use when redistributing OSPF routes from other instances on this instance.'
  end
  
  newproperty(:metric_rip) do
    desc 'The metric to use when redistributing RIP routes on this instance.'
  end

  newproperty(:mpls_te_area) do
    desc 'MPLS Traffic Engineering Area ID'
  end
  
  newproperty(:mpls_te_router_id) do
    desc 'MPLS Traffic Engineering Router ID'
  end
  
  newproperty(:routing_table) do
    desc 'Routing Table to receive and install routes from/to'
  end
end


File: /lib\puppet\type\mikrotik_ospf_interface.rb
Puppet::Type.newtype(:mikrotik_ospf_interface) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'OSPF Interface'
    isnamevar
  end
  
  newproperty(:cost) do
    desc 'The Cost of the OSPF interface.'
  end
  
  newproperty(:priority) do
    desc 'The Priority of the OSPF interface.'
  end
  
  newproperty(:authentication) do
    desc 'The authentication type (none, simple, md5)'
    newvalues(:none, :simple, :md5)
    defaultto :none
  end
  
  newproperty(:authentication_key) do # authentication-key
    desc 'The key used for authentication.'
  end
  
  newproperty(:authentication_key_id) do # authentication-key-id
    desc 'Key ID used to calculate message digest (MD5 authentication). Common for all routers in area.'
  end
  
  newproperty(:network_type) do # network-type
    desc 'The network type (default, broadcast, nbma, point-to-point, ptmp)'
    newvalues(:default, :broadcast, :nbma, 'point-to-point', :ptmp)
    defaultto :broadcast
  end
  
  newproperty(:passive) do
    desc 'Whether the interface is passive (not participating in OSPF)'
    newvalues(false, true)
    defaultto false
  end
  
  newproperty(:use_bfd) do # use-bfd
    desc 'Whether to enable BFD on the interface for the OSPF process'
    newvalues(false, true)
    defaultto false
  end
end


File: /lib\puppet\type\mikrotik_ospf_network.rb
Puppet::Type.newtype(:mikrotik_ospf_network) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'OSPF Network (Subnet)'
    isnamevar
  end
  
  newproperty(:area) do
    desc 'The OSPF Area this network belongs to.'
  end

  newproperty(:comment) do
    desc 'A comment that describes this network'
  end
end


File: /lib\puppet\type\mikrotik_ospf_nmba_neighbor.rb
Puppet::Type.newtype(:mikrotik_ospf_nmba_neighbor) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Neighbor Address'
    isnamevar
  end
  
  newproperty(:instance) do
    desc 'The OSPF Instance this neighbor belongs to.'
  end
  
  newproperty(:poll_interval) do
    desc 'The interval at which the neighbor should be polled (Defaults to 2 minutes)'
  end
  
  newproperty(:priority) do
    desc 'The OSPF priority used when the neighbor is down'
  end
end


File: /lib\puppet\type\mikrotik_package.rb
Puppet::Type.newtype(:mikrotik_package) do
  apply_to_all

  ensurable do
    defaultto :enabled

    newvalue(:enabled) do
      provider.setState(:enabled)  
    end

    newvalue(:disabled) do
      provider.setState(:disabled) 
    end

    def retrieve
      provider.getState
    end

    def insync?(is)
      @should.each { |should|               
        return (provider.getState == should)
      }
    end
  end

  newparam(:name) do
    desc 'Package Name'
    isnamevar
  end

  newparam(:force_reboot) do
    desc 'Whether to reboot after downloading package'
    newvalues(true, false)
  end
end


File: /lib\puppet\type\mikrotik_ppp_aaa.rb
Puppet::Type.newtype(:mikrotik_ppp_aaa) do
  apply_to_all
  
  # Only 1 set of settings that is always enabled. NOT ensurable 
  
  newparam(:name) do
    desc 'Name should be -aaa-'
    isnamevar
  end

  newproperty(:use_radius) do
    desc 'Whether to enable RADIUS for user authentication.'
    newvalues(true, false)
  end
  
  newproperty(:accounting) do
    desc 'Whether to enable RADIUS accounting.'
    newvalues(true, false)
  end
  
  newproperty(:interim_update) do
    desc 'The time period between RADIUS accounting updates.'
  end  
end


File: /lib\puppet\type\mikrotik_ppp_profile.rb
Puppet::Type.newtype(:mikrotik_ppp_profile) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'PPP profile name'
    isnamevar
  end

  newproperty(:local_address) do
    desc 'The local address to use for PPP session'
  end  
  
  newproperty(:remote_address) do
    desc 'The remote address (or IP pool) to use for PPP session'
  end  

  newproperty(:bridge) do
    desc 'The bridge to assign the PPP session to'
  end  
  
  newproperty(:bridge_path_cost ) do
    desc 'The path cost for the session when assigned to a bridge'
  end  
  
  newproperty(:bridge_port_priority) do
    desc 'The port priority for the session when assigned to a bridge'
  end  
  
  newproperty(:incoming_filter) do
    desc 'The filter to use for incoming connections'
  end  
  
  newproperty(:outgoing_filter) do
    desc 'The filter to use for outgoing connections'
  end  
  
  newproperty(:address_list) do
    desc 'Address list to add active sessions on'
  end

  newproperty(:interface_list) do
    desc 'Interface list to add active sessions on'
  end

  newproperty(:dns_server) do
    desc 'DNS Server to assign to the PPP client'
  end  
  
  newproperty(:wins_server) do
    desc 'WINS Server to assign to the PPP client'
  end  

  newproperty(:change_tcp_mss) do
    desc 'Whether to change TCP MSS'
    newvalues(:yes, :no, :default)
  end  
  
  newproperty(:use_upnp) do
    desc 'Whether to use uPnP'
    newvalues(:yes, :no, :default)
  end  

  newproperty(:use_mpls) do
    desc 'Whether to use MPLS'
    newvalues(:yes, :no, :required, :default)
  end
  
  newproperty(:use_compression) do
    desc 'Whether to use compression'
    newvalues(:yes, :no, :default)
  end
  
  newproperty(:use_encryption) do
    desc 'Whether to use encryption'
    newvalues(:yes, :no, :required, :default)
  end
  
  newproperty(:session_timeout) do
    desc 'The maximum time the connection can stay up'
  end  

  newproperty(:idle_timeout) do
    desc 'The time limit when the link will be terminated if there is no activity'
  end  

  newproperty(:rate_limit) do
    desc 'Data rate limitations for the client'
  end  

  newproperty(:only_one) do
    desc 'Whether to allow only one session per user'
    defaultto :default
    newvalues(:yes, :no, :default)
  end

  newproperty(:insert_queue_before) do
    desc 'Add queue for session and insert before'
  end 

  newproperty(:parent_queue) do
    desc 'Attach queue for session to parent queue'
  end  

  newproperty(:queue_type) do
    desc 'Set type for queue for session'
  end

  newproperty(:on_up) do
    desc 'Action to perform on up'
  end  

  newproperty(:on_down) do
    desc 'Action to perform on down'
  end  
end


File: /lib\puppet\type\mikrotik_ppp_secret.rb
Puppet::Type.newtype(:mikrotik_ppp_secret) do
  apply_to_all

  ensurable do
    newvalue(:present) do
      provider.create
    end

    newvalue(:absent) do
      provider.destroy
    end

    newvalue(:enabled) do
      provider.create
      provider.setState(:enabled)
    end

    newvalue(:disabled) do
      provider.create
      provider.setState(:disabled)
    end

    defaultto :enabled

    def retrieve
      provider.getState
    end

    def insync?(is)
      @should.each { |should|
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled
            return (provider.getState == :enabled)
          when :disabled
            return (provider.getState == :disabled)
        end
      }
    end
  end

  newparam(:name) do
    desc 'Name of the user'
    isnamevar
  end

  newproperty(:password) do
    desc 'User password'
  end

  newproperty(:service) do
    desc 'Specifies service that will use this user'
  end

  newproperty(:caller_id) do
    desc 'Sets IP address for PPTP, L2TP or MAC address for PPPoE'
  end

  newproperty(:profile) do
    desc 'Profile name for the user'
  end

  newproperty(:local_address) do
    desc 'Assigns an individual address to the PPP-server'
  end

  newproperty(:remote_address) do
    desc 'Assigns an individual address to the PPP-client'
  end

  newproperty(:routes, :array_matching => :all) do
    desc 'Routes that appear on the server when the client is connected'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end

  newproperty(:limit_bytes_in) do
    desc 'Maximum amount of bytes user can transmit'
  end

  newproperty(:limit_bytes_out) do
    desc 'Maximum amount of bytes user can receive'
  end
end


File: /lib\puppet\type\mikrotik_ppp_server.rb
Puppet::Type.newtype(:mikrotik_ppp_server) do
  apply_to_all
  
  ensurable do
    newvalue(:present)

    newvalue(:enabled) do
      provider.setState(:enabled)
    end

    newvalue(:disabled) do
      provider.setState(:disabled)
    end

    defaultto :present
    
    def retrieve
      provider.getState
    end

    def insync?(is)
      @should.each { |should|
        case should
          when :present
            return true
          when :enabled
            return (provider.getState == :enabled)
          when :disabled
            return (provider.getState == :disabled)
        end
      }
    end
  end

  newparam(:name) do
    desc 'Name should be -pptp- or -l2tp-'
    isnamevar
  end

  newproperty(:max_mtu) do
    desc 'Maximum Transmission Unit'
  end
  
  newproperty(:max_mru) do
    desc 'Maximum Receive Unit'
  end
  
  newproperty(:mrru) do
    desc 'Maximum Receive Reconstructed Unit'
  end
  
  newproperty(:authentication, :array_matching => :all) do
    desc 'Authentication algorithms'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
 
  newproperty(:keepalive_timeout) do
    desc 'Time after which an inactive session should be disconnected'
  end
  
  newproperty(:default_profile) do
    desc 'Default profile to use'
  end
  
  # L2TP Only  
  newproperty(:max_sessions) do
    desc '(L2TP) The maximum number of sessions allowed on the server'
  end

  newproperty(:use_ipsec) do
    desc '(L2TP) Whether to use IPSEC encryption'
  end
  
  newproperty(:ipsec_secret) do
    desc '(L2TP) IPSEC Secret'
  end
  
  newproperty(:allow_fastpath) do
    desc '(L2TP) Whether to allow Fast Path'
  end

  #OVPN Only
  newproperty(:port) do
    desc '(OVPN) Port to run the server on'
  end

  newproperty(:mode) do
    desc '(OVPN) IP (tunnel) mode or Ethernet (bridge/tap) mode'
    newvalue(:ip)
    newvalue(:ethernet)
  end

  newproperty(:netmask) do
    desc '(OVPN) Subnet mask to be applied to clients'
  end

  newproperty(:mac_address) do
    desc '(OVPN) MAC address of the server (normally auto-generated)'
  end

  newproperty(:certificate) do
    desc '(OVPN) name of Certificate file'
  end

  newproperty(:require_client_certificate) do
    newvalue(:true)
    newvalue(:false)
  end

  newproperty(:cipher, :array_matching => :all) do
    desc '(OVPN) Cipher algorithms'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end

end


File: /lib\puppet\type\mikrotik_radius_server.rb
Puppet::Type.newtype(:mikrotik_radius_server) do
  apply_to_all
  
  ensurable
  # TODO -ENABLED-
  
  newparam(:name) do
    desc 'The server description'
    isnamevar
  end
  
  newproperty(:address) do
    desc 'The server IP address.'
  end

  newproperty(:services, :array_matching => :all) do
    desc 'The services that the server will handle requests for.'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end

  newproperty(:called_id) do
    desc 'The called ID.'
  end
  
  newproperty(:domain) do
    desc 'The domain to add to the username (?)'
  end
    
  newproperty(:secret) do
    desc 'The RADIUS shared secret.'
  end
  
  newproperty(:auth_port) do
    desc 'The RADIUS authentication port.'
  end
  
  newproperty(:acct_port) do
    desc 'The RADIUS accounting port.'
  end
  
  newproperty(:timeout) do
    desc 'The RADIUS timeout.'
  end
  
  newproperty(:accounting_backup) do
    desc 'Accounting backup (?)'
  end
  
  newproperty(:realm) do
    desc 'The realm that this server will listen for.'
  end
  
  newproperty(:src_address) do
    desc 'The source IP that will be used for requests.'
  end
end


File: /lib\puppet\type\mikrotik_romon.rb
Puppet::Type.newtype(:mikrotik_romon) do
  apply_to_all
  
  # Only 1 set of settings.
  newparam(:name) do
    desc 'Name should be -romon-'
    isnamevar
  end

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newproperty(:id) do
    desc 'The RoMON ID (MAC address).'
  end
  
  newproperty(:secrets, :array_matching => :all) do
    desc 'The default RoMON passwords for this router.'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end    
  end  
end


File: /lib\puppet\type\mikrotik_romon_port.rb
Puppet::Type.newtype(:mikrotik_romon_port) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Interface name'
    isnamevar
  end
  
  newproperty(:forbid) do
    desc 'Whether to forbid RoMON traffic on this interface (default = allow).'
    newvalues(true, false)
    defaultto false
  end

  newproperty(:secrets, :array_matching => :all) do
    desc 'The RoMON passwords specific to this interface.'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end    
  end
  
  newproperty(:cost) do
    desc 'The cost for this interface.'
    defaultto 100
  end
end


File: /lib\puppet\type\mikrotik_routing_filter.rb
Puppet::Type.newtype(:mikrotik_routing_filter) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'Filter description'
    isnamevar
  end

  newproperty(:chain) do
    desc 'Filter Chain'
  end
  
  newproperty(:chain_order) do
    desc 'Order number inside the chain (starts at 1).'
  end

  # Matchers
  newproperty(:prefix) do
    desc 'Match Prefix'
  end
  
  newproperty(:prefix_length) do
    desc 'Match Prefix length'
  end
  
  newproperty(:match_chain) do
    desc 'Match Chain'
  end
  
  newproperty(:protocols, :array_matching => :all) do
    desc 'Match Protocols'
    
    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:distance) do
    desc 'Match Distance'
  end
  
  newproperty(:scope) do
    desc 'Match Scope'
  end
  
  newproperty(:target_scope) do
    desc 'Match Target scope'
  end
  
  newproperty(:pref_src) do
    desc 'Match Preferred source'
  end
  
  newproperty(:routing_mark) do
    desc 'Match Routing mark'
  end
  
  newproperty(:route_comment) do
    desc 'Match Route comment'
  end
  
  newproperty(:route_tag) do
    desc 'Match Route tag'
  end
  
  newproperty(:route_targets, :array_matching => :all) do
    desc 'Match Route targets'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:sites_of_origin, :array_matching => :all) do
    desc 'Match Sites of origin'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:address_families, :array_matching => :all) do
    desc 'Match Address families'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:ospf_type) do
    desc 'Match OSPF type'
    newvalues('external-type-1', 'external-type-2', 'inter-area', 'intra-area', 'nssa-external-type-1', 'nssa-external-type-2')
  end
  
  newproperty(:invert_match) do
    desc 'Whether to invert match'
  end

  # BGP Matchers
  newproperty(:bgp_as_path) do
    desc 'Match BGP AS path'
  end
  
  newproperty(:bgp_as_path_length) do
    desc 'Match BGP AS path length'
  end
  
  newproperty(:bgp_weight) do
    desc 'Match BGP weight'
  end
  
  newproperty(:bgp_local_pref) do
    desc 'Match BGP local preference'
  end
  
  newproperty(:bgp_med) do
    desc 'Match BGP MED'
  end
  
  newproperty(:bgp_atomic_aggregate) do
    desc 'Match BGP atomic aggregate'
    newvalues('present', 'absent')
  end
  
  newproperty(:bgp_origins, :array_matching => :all) do
    desc 'Match BGP origins'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:locally_originated_bgp) do
    desc 'Match only locally originated BGP'
    newvalues('yes', 'no')
  end

  newproperty(:bgp_communities, :array_matching => :all) do
    desc 'Match BGP communities'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  # Actions
  newproperty(:action) do
    desc 'Action to take if matched'
    newvalues('accept', 'jump', 'discard', 'log', 'reject', 'passthrough', 'return')
  end
  
  newproperty(:jump_target) do
    desc 'Chain to jump to if action is jump and filter is matched'
  end
  
  newproperty(:set_distance) do
    desc 'Set distance if matched'
  end
  
  newproperty(:set_scope) do
    desc 'Set scope if matched'
  end
  
  newproperty(:set_target_scope) do
    desc 'Set target scope if matched'
  end
  
  newproperty(:set_pref_src) do
    desc 'Set preferred source if matched'
  end
  
  newproperty(:set_in_nexthops, :array_matching => :all) do
    desc 'Set inbound nexthop if matched'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:set_in_nexthops_direct, :array_matching => :all) do
    desc 'Set inbound nexthop (interface) if matched'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:set_out_nexthop) do
    desc 'Set outbound nexthop if matched'
  end
  
  newproperty(:set_routing_mark) do
    desc 'Set routing mark if matched'
  end
  
  newproperty(:set_route_comment) do
    desc 'Set route comment if matched'
  end
  
  newproperty(:set_check_gateway) do
    desc 'Whether to check gateway if matched'
    newvalues('ping', 'arp', 'none')
  end
  
  newproperty(:set_disabled) do
    desc 'Whether to set route disabled if matched'
    newvalues('yes', 'no')
  end
  
  newproperty(:set_type) do
    desc 'Set route type if matched'
    newvalues('unicast', 'blackhole', 'prohibit', 'unreachable')
  end
  
  newproperty(:set_route_tag) do
    desc 'Set route tag if matched'
  end
  
  newproperty(:set_use_te_nexthop) do
    desc 'Set MPLS TE nexthop if matched'
    newvalues('yes', 'no')
  end
  
  newproperty(:set_route_targets, :array_matching => :all) do
    desc 'Set route targets if matched'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:append_route_targets, :array_matching => :all) do
    desc 'Append route targets if matched'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:set_site_of_origin, :array_matching => :all) do
    desc 'Set site of origin if matched'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end

  # BGP Actions
  newproperty(:set_bgp_weight) do
    desc 'Set BGP weight if matched'
  end
  
  newproperty(:set_bgp_local_pref) do
    desc 'Set BGP local preference if matched'
  end
  
  newproperty(:set_bgp_prepend) do
    desc 'Set BGP AS path count prepend if matched'
  end
  
  newproperty(:set_bgp_prepend_path, :array_matching => :all) do
    desc 'Set BGP AS path (acxtual path) prepend if matched'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:set_bgp_med) do
    desc 'Set BGP MED if matched'
  end
  
  newproperty(:set_bgp_communities, :array_matching => :all) do
    desc 'Set BGP communities if matched'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:append_bgp_communities, :array_matching => :all) do
    desc 'Append BGP communities if matched'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  # Not defined in winbox? 
  #   set-in-nexthop-ipv6
  #   set-in-nexthop-linklocal
  #   set-out-nexthop-ipv6
  #   set-out-nexthop-linklocal
end


File: /lib\puppet\type\mikrotik_schedule.rb
Puppet::Type.newtype(:mikrotik_schedule) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'Scheduled event name'
    isnamevar
  end
  
  newproperty(:start_date) do
    desc 'Date of first execution'
  end
  
  newproperty(:start_time) do
    desc 'Time of first execution'
  end
  
  newproperty(:interval) do
    desc 'Interval between two script executions'
  end

  newproperty(:policies, :array_matching => :all) do
    desc 'The permissions that the script is given.'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:on_event) do
    desc 'Script name or actual commands to execute'
  end
end


File: /lib\puppet\type\mikrotik_script.rb
Puppet::Type.newtype(:mikrotik_script) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'Name of the script'
    isnamevar
  end
  
  newproperty(:policies, :array_matching => :all) do
    desc 'The permissions that the script is given.'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end
  
  newproperty(:source) do
    desc 'The script itself'
  end
end


File: /lib\puppet\type\mikrotik_snmp.rb
Puppet::Type.newtype(:mikrotik_snmp) do
  apply_to_all
  
  # Only 1 set of settings.
  newparam(:name) do
    desc 'Name should be -snmp-'
    isnamevar
  end
  
  ensurable do    
    defaultto :present

    newvalue(:present)
        
    newvalue(:enabled) do
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return true
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newproperty(:contact) do
    desc 'The SNMP contact information.'
  end

  newproperty(:location) do
    desc 'The SNMP location information.'
  end
  
  newproperty(:trap_targets, :array_matching => :all) do
    desc 'The SNMP trap targets.'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end    
  end
  
  newproperty(:trap_community) do
    desc 'The SNMP trap community.'
  end
  
  newproperty(:trap_version) do
    desc 'The SNMP trap version.'
    newvalues(1, 2, 3)
  end
  
  newproperty(:trap_generators, :array_matching => :all) do
    desc 'The objects that generate SNMP traps.'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end    
  end
end


File: /lib\puppet\type\mikrotik_snmp_community.rb
Puppet::Type.newtype(:mikrotik_snmp_community) do
  apply_to_all
  
  ensurable
  
  newparam(:name) do
    desc 'SNMP community name'
    isnamevar
  end
  
  newproperty(:read_access) do
    desc 'Whether community provides read access.'
    newvalues(true, false)
    defaultto true
  end

  newproperty(:write_access) do
    desc 'Whether community provides write access.'
    newvalues(true, false)
    defaultto false    
  end
  
  newproperty(:addresses, :array_matching => :all) do
    desc 'The IP addresses allowed to use the community.'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        if is == ['0.0.0.0/0'] and @should == []
          true
        else
          is.sort == @should.sort          
        end        
      else
        is == @should
      end
    end    
  end
end


File: /lib\puppet\type\mikrotik_system.rb
Puppet::Type.newtype(:mikrotik_system) do
  apply_to_all
  
  # Only 1 set of settings that is always enabled. NOT ensurable 
  
  newparam(:name) do
    desc 'Name should be -system-'
    isnamevar
  end

  newproperty(:identity) do
    desc 'The System Identity Name.'
  end
  
  newproperty(:timezone) do
    desc 'The Clock timezone.'
  end
  
  newproperty(:ntp_enabled) do
    desc 'Whether to enable NTP Client.'
  end

  newproperty(:ntp_primary) do
    desc 'The primary server for the NTP Client.'
  end

  newproperty(:ntp_secondary) do
    desc 'The secondary server for the NTP Client.'
  end
end


File: /lib\puppet\type\mikrotik_tool_email.rb
Puppet::Type.newtype(:mikrotik_tool_email) do
  apply_to_all
  
  # Only 1 set of settings that is always enabled. NOT ensurable 
  
  newparam(:name) do
    desc 'Name should be -email-'
    isnamevar
  end
  
  newproperty(:server) do
    desc 'The SMTP server to use when using the e-mail tool.'
  end
  
  newproperty(:port) do
    desc 'The SMTP port to use when using the e-mail tool.'
  end
  
  newproperty(:username) do
    desc 'The SMTP username to use when using the e-mail tool.'
  end
  
  newproperty(:password) do
    desc 'The SMTP password to use when using the e-mail tool.'
  end

  newproperty(:from_address) do
    desc 'The E-mail address to send from when using the e-mail tool.'
  end

  newproperty(:enable_starttls) do
    desc 'Whether to enable STARTTLS when using the e-mail tool.'
    newvalues(true, false)
  end
end


File: /lib\puppet\type\mikrotik_tool_netwatch.rb
Puppet::Type.newtype(:mikrotik_tool_netwatch) do
  apply_to_all

  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end

  newparam(:name) do
    desc 'IP/Hostname to test'
    isnamevar
  end
  
  newproperty(:interval) do
    desc 'Interval between checks in seconds.'
  end
  
  newproperty(:timeout) do
    desc 'Timeout in seconds after which the host is considered down.'
  end
  
  newproperty(:down_script) do
    desc 'Script that is started when host goes down.'
  end
  
  newproperty(:up_script) do
    desc 'Script that is started when host goes up.'
  end

  newproperty(:comment) do
    desc 'Short description'
  end
end


File: /lib\puppet\type\mikrotik_upgrade.rb
Puppet::Type.newtype(:mikrotik_upgrade) do
  apply_to_all

  ensurable do
    defaultto :present

    newvalue(:present) do
      provider.create  
    end

    newvalue(:absent) do
      provider.destroy
    end

    newvalue(:downloaded) do
      provider.create  
      provider.setState(:downloaded)      
    end

    newvalue(:installed) do
      provider.create  
      provider.setState(:installed)
    end

    def retrieve
      provider.getState
    end

    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :downloaded                   
            return (provider.getState == :downloaded or provider.getState == :installed)
          when :installed                      
            return (provider.getState == :installed)       
        end
      }
    end
  end

  newparam(:name) do
    desc 'Firmware Version'
    isnamevar
  end

  newparam(:force_reboot) do
    desc 'Whether to reboot after downloading package'
    newvalues(true, false)
  end
end


File: /lib\puppet\type\mikrotik_upgrade_source.rb
Puppet::Type.newtype(:mikrotik_upgrade_source) do
  apply_to_all
  
  ensurable
  
  newparam(:name) do
    desc 'IP Address to fetch packages from'
    isnamevar
  end
  
  newproperty(:username) do
    desc 'Username for authentication on package source'
  end
  
  newparam(:password) do
    desc 'Password for authentication on package source'
  end
end


File: /lib\puppet\type\mikrotik_user.rb
Puppet::Type.newtype(:mikrotik_user) do
  apply_to_all
  
  ensurable do
    defaultto :present
    
    newvalue(:present) do
      provider.create  
    end
    
    newvalue(:absent) do
      provider.destroy
    end
    
    newvalue(:enabled) do
      provider.create  
      provider.setState(:enabled)      
    end

    newvalue(:disabled) do
      provider.create  
      provider.setState(:disabled)
    end

    def retrieve
      provider.getState
    end
    
    def insync?(is)
      @should.each { |should| 
        case should
          when :present
            return (provider.getState != :absent)
          when :absent
            return (provider.getState == :absent)
          when :enabled                   
            return (provider.getState == :enabled)
          when :disabled                      
            return (provider.getState == :disabled)       
        end
      }      
    end
  end
  
  newparam(:name) do
    desc 'User name'
    isnamevar
  end
  
  newproperty(:group) do
    desc 'Group that the user belongs to (required)'
  end
  
  newproperty(:addresses, :array_matching => :all) do
    desc 'The IP addresses allowed for the user'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end
  end

  newparam(:password) do
    desc 'User password (only set on create)'
  end
end


File: /lib\puppet\type\mikrotik_user_aaa.rb
Puppet::Type.newtype(:mikrotik_user_aaa) do
  apply_to_all
  
  # Only 1 set of settings that is always enabled. NOT ensurable 
  
  newparam(:name) do
    desc 'Name should be -aaa-'
    isnamevar
  end

  newproperty(:use_radius) do
    desc 'Whether to enable RADIUS for user authentication.'
    newvalues(true, false)
  end
  
  newproperty(:accounting) do
    desc 'Whether to enable RADIUS accounting.'
    newvalues(true, false)
  end
  
  newproperty(:interim_update) do
    desc 'The time period between RADIUS accounting updates.'
  end
  
  newproperty(:default_group) do
    desc 'The default group the user belongs to if not set by RADIUS (Mikrotik-Group).'
  end
  
  newproperty(:exclude_groups, :array_matching => :all) do
    desc 'The groups that can not be used by RADIUS.'
    
    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort     
      else
        is == @should
      end
    end    
  end
end


File: /lib\puppet\type\mikrotik_user_group.rb
Puppet::Type.newtype(:mikrotik_user_group) do
  apply_to_all
  
  ensurable do
    defaultvalues
    defaultto :present
  end
  
  newparam(:name) do
    desc 'Usergroup name'
    isnamevar
  end
  
  newproperty(:skin) do
    desc 'The skin to apply on the webinterface for these users.'
  end
  
  newproperty(:policy, :array_matching => :all) do
    desc 'The allowed permissions for the usergroup.'

    def insync?(is)
      if is.is_a?(Array) and @should.is_a?(Array)
        is.sort == @should.sort
      else
        is == @should
      end
    end    
  end
end


File: /lib\puppet\type\mikrotik_user_sshkey.rb
Puppet::Type.newtype(:mikrotik_user_sshkey) do
  apply_to_all
  
  ensurable

  newparam(:user) do
    desc 'The user that the public key belongs to'
    isnamevar
  end

  newparam(:public_key) do
    desc 'The SSH public key (DSA/RSA)'
  end
end


File: /lib\puppet\util\network_device\mikrotik\device.rb
require 'puppet/util/network_device'
require_relative 'facts'
require_relative '../transport/mikrotik'

class Puppet::Util::NetworkDevice::Mikrotik::Device
  attr_reader :connection
  attr_accessor :url, :transport

  def initialize(url, options = {})
    # Puppet 5 support
    if Gem::Version.new(Puppet.version) < Gem::Version.new("6.0.0")      
      @autoloader = Puppet::Util::Autoload.new(self, 'puppet/util/network_device/transport')
      @autoloader.load('mikrotik')
    end
 
    @transport = Puppet::Util::NetworkDevice::Transport::Mikrotik.new(url, options[:debug])
  end

  def facts
    @facts ||= Puppet::Util::NetworkDevice::Mikrotik::Facts.new(@transport)

    @facts.retrieve
  end
end

File: /lib\puppet\util\network_device\mikrotik\facts.rb
require_relative '../mikrotik'

class Puppet::Util::NetworkDevice::Mikrotik::Facts
  attr_reader :transport
  
  def initialize(transport)
    @transport = transport
  end

  def connection
    @transport.connection
  end

  def retrieve
    facts_raw = {}    
    system_resources = connection.get_reply("/system/resource/getall")    
    system_resources.each do |system_resource| 
      if system_resource.key?('!re')
        facts_raw = system_resource.reject { |k, v| ['!re', '.tag'].include? k }
      end
    end
    
    facts = {}
    facts_raw.each do |k, v|
      new_key = k.gsub(/-/, '_')
      facts[new_key] = v
    end
    
    facts
  end
end

File: /lib\puppet\util\network_device\mikrotik.rb
require 'puppet/util/network_device'

module Puppet::Util::NetworkDevice::Mikrotik
end

File: /lib\puppet\util\network_device\transport\mikrotik.rb
require 'puppet/util/network_device'
require 'puppet/util/network_device/transport'
require 'puppet/util/network_device/transport/base'

require 'mtik' if Puppet.features.mtik?

class Puppet::Util::NetworkDevice::Transport::Mikrotik < Puppet::Util::NetworkDevice::Transport::Base
  attr_reader :connection

  def initialize(url, _options = {})
    require 'uri'

    url_object = URI(url)

    if (url_object.scheme == 'api')
      @connection = MTik::Connection.new :host => url_object.host, :user => url_object.user, :pass => url_object.password, :unencrypted_plaintext => true, :conn_timeout => 10
    else
      raise "The Mikrotik module currently only support API access. Use api:// in URL."
    end
  end
end

File: /LICENSE
Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "{}"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2017 Nicolas Truyens

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

File: /manifests\init.pp
class mikrotik (
  $version = '4.1.2'
) {
  # mtik-4.0.4 => Mikrotik pre 6.43
  # mtik 4.1.2 => MUST BE USED FROM 6.45.1

  # Dependencies for running the custom Type/Provider
  file { "/usr/src/mtik-${version}.gem":
    ensure => 'file',
    source => "puppet:///modules/mikrotik/mtik-${version}.gem",
  }
  ->
  package { 'mtik':
    ensure   => 'present',
    provider => 'puppet_gem',
    source   => "/usr/src/mtik-${version}.gem",
  }

  # We could use classes/defines to set up devices.conf
}


File: /metadata.json
{
  "name": "puppet-mikrotik",
  "version": "0.9.0",
  "author": "Lavaburn",
  "summary": "This module provides resources for managing a Mikrotik device.",
  "license": "Apache 2.0",
  "source": "git://github.com/Lavaburn/puppet-mikrotik.git",
  "project_page": "https://github.com/Lavaburn/puppet-mikrotik",
  "issues_url": "https://github.com/Lavaburn/puppet-mikrotik/issues",
  "tags": [
    "mikrotik", "router"
  ],
  "operatingsystem_support": [
    {
      "operatingsystem": "Ubuntu",
      "operatingsystemrelease": [ "14.04", "16.04" ]
    }
  ],
  "requirements": [
    {
      "name": "puppet",
      "version_requirement": ">= 4.0.0"
    }
  ],
  "dependencies": []
}


File: /Rakefile
# Required gems
require 'rubygems'

# Rake Tasks
require 'puppetlabs_spec_helper/rake_tasks'


File: /README.md
# puppet-mikrotik
Puppet Module for managing Mikrotik Devices

Work in Progress.


## Local Testing

### Bootstrap
For local testing using RVM:
* rvm use 2.4.5
* gem install bundler
* bundle install --binstubs [LEGACY?]


## Acceptance Testing

Single run:

	rake beaker
	
Multiple runs: 
	
	BEAKER_provision=yes BEAKER_destroy=no rake beaker
	
	BEAKER_provision=no BEAKER_destroy=no rake beaker
	
	BEAKER_provision=no BEAKER_destroy=onpass rake beaker
	
### Debugging inside Vagrant

	cd .vagrant/beaker_vagrant_files/default.yml
	
	vagrant ssh puppet
	vagrant ssh ubuntu-16-04

### Defining SUT and environment
* See spec/fixtures/testnodes.example.yaml
* See spec/fixtures/upgrade_source.example.yaml

### Optional: using CHR as testmachine
* vagrant boxes add dulin/mikrotik
* cd vagrant; vagrant up
See spec/fixtures/testnodes.example.yaml


## NOTES

### IPv6
The IPv6 package is not installed by default!

### Tested Using
Works:
* Ruby 2.1.8
* Puppet 4.3.2

Works: 
* Ruby 2.4.5
* Puppet 5.5.10

Works ("puppet6" branch): 
* Ruby 2.4.5
* Puppet 6.13.0


File: /spec\acceptance\.gitignore
/custom_*_spec.rb


File: /spec\acceptance\address_list_spec.rb
require 'spec_helper_acceptance'

describe '/ip/firewall/address-list' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_address_list { 'MT_TEST_LIST':
          ensure => 'absent',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "create new list" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_address_list { 'MT_TEST_LIST':
          addresses => [
            '1.1.1.0/24',
            '1.1.2.0/24',
          ],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "add entries to list" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_address_list { 'MT_TEST_LIST':
          addresses => [
            '1.1.1.0/24',
            '1.1.2.0/24',
            '1.1.4.0/24',
            '1.1.3.0/24',
          ],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "remove entries from list" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_address_list { 'MT_TEST_LIST':
          addresses => [
            '1.1.2.0/24',
            '1.1.4.0/24',
          ],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "delete list" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_address_list { 'MT_TEST_LIST':
          ensure => 'absent',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

describe '/ipv6/firewall/address-list' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_address_list { 'MT_TEST_LIST':
          ensure => 'absent',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "create new list" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_address_list { 'MT_TEST_LIST':
          addresses => [
            '2001:db8:100::/64',
            '2001:db8:200::/64',
          ],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "add entries to list" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_address_list { 'MT_TEST_LIST':
          addresses => [
            '2001:db8:100::/64',
            '2001:db8:200::/64',
            '2001:db8:300::/64',
            '2001:db8:400::/64',
          ],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "remove entries from list" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_address_list { 'MT_TEST_LIST':
          addresses => [
            '2001:db8:200::/64',
            '2001:db8:400::/64',
          ],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "delete list" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_address_list { 'MT_TEST_LIST':
          ensure => 'absent',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

File: /spec\acceptance\bridge_spec.rb
require 'spec_helper_acceptance'

describe '/interface/bridge' do  
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge_msti_port { '4011_2':  
          ensure => absent,
        }
      
        mikrotik_interface_bridge_msti { ['mst_402', 'mst_403']:
          ensure => absent,
        }

        mikrotik_interface_bridge_vlan { ['vlan_402', 'vlan_403']:   
          ensure => absent,
        }      
      
        mikrotik_interface_bridge_port { ['VLAN_4011', 'VLAN_4012']:
          ensure => absent,
        }

        mikrotik_interface_vlan { ['VLAN_4011', 'VLAN_4012']:
          ensure => absent,
        }
        
        mikrotik_interface_bridge { 'MSTP_TEST':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 2
  end  
  
  context "create new bridge" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_vlan { 'VLAN_4011':  
          ensure    => enabled,    
          vlan_id   => '4011',
          interface => 'ether1',
        }
        
        mikrotik_interface_vlan { 'VLAN_4012':  
          ensure    => enabled,    
          vlan_id   => '4012',
          interface => 'ether1',
        }

        mikrotik_interface_bridge { 'MSTP_TEST':
          vlan_filtering => true,
          pvid           => "21",
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end  

  context "update bridge" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge { 'MSTP_TEST':
          protocol_mode   => 'mstp',
          priority        => '0x6000',
          region_name     => 'TEST',
          region_revision => '1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "attach to bridge" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge_port { 'VLAN_4011':      
          bridge  => 'MSTP_TEST',
          horizon => '40',
          pvid    => '4011',
        }
        
        mikrotik_interface_bridge_port { 'VLAN_4012':      
          bridge  => 'MSTP_TEST',
          horizon => '40',
          pvid    => '4012',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update bridge ports" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge_port { 'VLAN_4011':      
          bridge            => 'MSTP_TEST',
          ingress_filtering => true,
        }
        
        mikrotik_interface_bridge_port { 'VLAN_4012':
          bridge             => 'MSTP_TEST',
          priority           => '0x60',
          path_cost          => '20',
          internal_path_cost => '15',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "create bridge vlans" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge_vlan { 'vlan_402':   
          bridge   => 'MSTP_TEST',   
          tagged   => [ 'VLAN_4011', 'VLAN_4012' ],
          vlan_ids => [ '4021', '4022' ],
        }
  
        mikrotik_interface_bridge_vlan { 'vlan_403':   
          bridge   => 'MSTP_TEST',   
          vlan_ids => [ '4031', '4032', '4033' ],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update bridge vlans" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge_vlan { 'vlan_402':   
          bridge   => 'MSTP_TEST',   
          vlan_ids => [ '4021', '4022', '4023' ],
        }
        
        mikrotik_interface_bridge_vlan { 'vlan_403':   
          bridge   => 'MSTP_TEST',   
          vlan_ids => [ '4031', '4032' ],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "create MST instances" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge_msti { 'mst_402':   
          bridge       => 'MSTP_TEST',
          identifier   => '2',
          vlan_mapping => [ '4021-4029' ],
        }
        
        mikrotik_interface_bridge_msti { 'mst_403':   
          bridge       => 'MSTP_TEST',
          identifier   => '3',
          vlan_mapping => [ '4031-4039' ],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update MST instances" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge_msti { 'mst_402':   
          bridge       => 'MSTP_TEST',
          identifier   => '2',
          priority     => '0x6000',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "create port MST override" do 
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge_msti_port { '4011_2':   
          interface    => 'VLAN_4011',
          identifier   => '2',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update port MST override" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge_msti_port { '4011_2':   
          interface          => 'VLAN_4011',
          identifier         => '2',
          priority           => '0x40',
          internal_path_cost => '20',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end


File: /spec\acceptance\dns_spec.rb
require 'spec_helper_acceptance'

describe '/ip/dns' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
      mikrotik_dns { 'dns':
        servers               => ['8.8.8.8','8.8.4.4'],
        allow_remote_requests => false,
      }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "correct settings" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_dns { 'dns':
          servers               => ['105.235.209.31','208.67.222.222'],
          allow_remote_requests => true,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable remote requests" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_dns { 'dns':
          allow_remote_requests => false,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
# TODO - exist code = 0 ??? => Find other way to detect error...
#  context "with ensure absent" do
#    it 'should update master' do
#      site_pp = <<-EOS
#        mikrotik_dns { 'dns':
#          ensure => 'absent',
#        }
#      EOS
#      
#      set_site_pp_on_master(site_pp)
#    end
#  
#    it_behaves_like 'a faulty device run'
#  end
  
  context "with wrong title" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_dns { 'myDNS2':
          servers               => ['105.235.209.31','208.67.222.222'],
          allow_remote_requests => false,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'a faulty device run'
  end
end


File: /spec\acceptance\interface_spec.rb
require 'spec_helper_acceptance'

describe '/interface' do  
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_vrrp { 'br0_vip':
          ensure => absent,        
        }
  
        mikrotik_interface_bridge_port { 'VLAN_4001':
          ensure => absent,
        }
        
        mikrotik_interface_bridge { ['br0', 'br1', 'br2']:
          ensure => absent,
        }
                
        mikrotik_interface_bond { 'ip_tnl_bond':
          ensure => absent,
        }
  
        mikrotik_interface_eoip { ['ip_tnl_01', 'ip_tnl_02']:
          ensure => absent,
        }
        
        mikrotik_interface_vlan { 'VLAN_4001':
          ensure => absent,
        }
  
        mikrotik_interface_ethernet { 'ether1': 
          alias => 'ether1',
        }
      
        mikrotik_interface_list { 'interface_list_1':
          ensure => 'absent',
        }
        
        mikrotik_interface_bgp_vpls { 'Virtual1':
          ensure => 'absent',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 9
  end  
  
  context "create new bridge" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge { 'br0':
          
        }
        
        mikrotik_interface_bridge { 'br1':
          mtu => 1300,
          admin_mac => '02:02:02:12:34:56',
        }
        
        mikrotik_interface_bridge { 'br2':
          ensure => disabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end  

  context "update bridge" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge { 'br0':
          mtu => 1000,
        }
        
        mikrotik_interface_bridge { 'br1':
          mtu => 1200,
        }
        
        mikrotik_interface_bridge { 'br2':
          ensure => enabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "create eoip" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_eoip { 'ip_tnl_01':
          local_address  => '10.150.1.1',
          remote_address => '10.150.1.2',
          tunnel_id      => '1501',
        }
          
        mikrotik_interface_eoip { 'ip_tnl_02':
          ensure         => disabled,
          local_address  => '10.150.2.1',
          remote_address => '10.150.2.2',
          tunnel_id      => '1502',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "create vrrp" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_vrrp { 'br0_vip':   
          ensure          => enabled,       
          interface       => 'br0',
          vrid            => 123,
          priority        => 50,
          preemption_mode => false,
          # authentication  => 'simple',
          # password        => 'secret',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "create vlan" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_vlan { 'VLAN_4001':  
          ensure    => enabled,    
          vlan_id   => '4001',
          interface => 'ether1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "attach to bridge" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge_port { 'VLAN_4001':      
          bridge => 'br0',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "create bond" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bond { 'ip_tnl_bond':      
          slaves               => ['ip_tnl_01', 'ip_tnl_02'],
          mode                 => '802.3ad',
          link_monitoring      => 'mii',
          transmit_hash_policy => 'layer-2',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "create vpls bgp interface" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bgp_vpls { 'Virtual1':
          route_distinguisher  => '1234:54321',            
          import_route_targets => ['1234:54321', '1234:54322'],
          export_route_targets => '1234:54321',                  
          site_id              => 1,
          bridge               => 'br0',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "rename ethernet" do      
    it 'should update master' do
      site_pp = <<-EOS
      mikrotik_interface_ethernet { 'ether1':      
          alias => 'ether1-test',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  # Don't mess with future tests...
  context "reset ethernet name" do      
    it 'should update master' do
      site_pp = <<-EOS
      mikrotik_interface_ethernet { 'ether1':      
          alias => 'ether1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "create interface list" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_list { 'interface_list_1':
          members => ['VLAN_4001', 'ip_tnl_01']
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update interface list" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_list { 'interface_list_1':
          members => ['VLAN_4001', 'ip_tnl_bond']
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update vpls bgp interface" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bgp_vpls { 'Virtual1':  
          import_route_targets => ['1234:54322', '1234:54323'],
          export_route_targets => '1234:54322',                  
          bridge_cost          => 100,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable some interfaces" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge { 'br0':
          ensure => disabled
        }
  
        mikrotik_interface_eoip { 'ip_tnl_01':
          ensure => disabled
        }
        
        mikrotik_interface_vrrp { 'br0_vip':  
          ensure => disabled
        }
        
        mikrotik_interface_vlan { 'VLAN_4001':      
          ensure => disabled
        }
        
        mikrotik_interface_bond { 'ip_tnl_bond':   
          ensure => disabled
        }
          
        mikrotik_interface_bgp_vpls { 'Virtual1':
          ensure => disabled
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end  
  
  context "enable some interfaces" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_bridge { 'br0':
          ensure => enabled
        }
  
        mikrotik_interface_eoip { 'ip_tnl_01':
          ensure => enabled
        }
        
        mikrotik_interface_vrrp { 'br0_vip':  
          ensure => enabled
        }
        
        mikrotik_interface_vlan { 'VLAN_4001':      
          ensure => enabled
        }
        
        mikrotik_interface_bond { 'ip_tnl_bond':   
          ensure => enabled
        }
          
        mikrotik_interface_bgp_vpls { 'Virtual1':
          ensure => enabled
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end  
end


File: /spec\acceptance\ipv6_firewall_spec.rb
require 'spec_helper_acceptance'

describe '/ipv6/firewall' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { ['Puppet Test 1', 'Puppet Test 2', 'Puppet Test 3']:
          ensure => absent, 
          table  => 'filter',          
        }
        
        mikrotik_ipv6_firewall_rule { ['SSH_JUMP', 'SSH_DROP', 'SSH_STAGE3', 'SSH_STAGE2', 'SSH_STAGE1', 'SSH_NEW']:
          ensure => absent, 
          table  => 'filter',          
        }
        
        mikrotik_ipv6_firewall_rule { ['unsorted_1', 'unsorted_2', 'unsorted_3']:
          ensure => absent, 
          table  => 'mangle',          
        }
  
        mikrotik_ipv6_firewall_rule { ['rule_a', 'rule_b', 'rule_c', 'rule_d', 'rule_e', 'rule_f', 'rule_g', 'rule_h', 'rule_i']:
          ensure => absent,    
          table  => 'mangle',       
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "create 3 new rules" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { 'Puppet Test 1':
          ensure      => present,
          table       => 'filter',
          chain       => 'input',
          src_address => '2001:db8:1111::/64',
          action      => 'accept',
          #sequence    => '3',
        }
        
        mikrotik_ipv6_firewall_rule { 'Puppet Test 2':
          ensure      => enabled,
          table       => 'filter',
          chain       => 'input',
          src_address => '2001:db8:1112::/64',
          action      => 'accept',
          #sequence    => '3',
        }
        
        mikrotik_ipv6_firewall_rule { 'Puppet Test 3':
          ensure      => disabled,
          table       => 'filter',
          chain       => 'input',
          src_address => '2001:db8:1113::/64',
          action      => 'accept',
          #sequence    => '3',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update a rule" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { 'Puppet Test 1':
          table       => 'filter',
          chain       => 'input',
          src_address => '2001:db8:2111::/64',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "delete a rule" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { 'Puppet Test 2':
           ensure => 'absent',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "ssh brute-force rules" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { 'SSH_JUMP':
          ensure           => present,
          table            => 'filter',
          chain            => 'input',
          protocol         => 'tcp',
          dst_port         => '22',
          src_address_list => "!RCS_INFRA",
          action           => 'jump',
          jump_target      => 'SSH',
        }
        
        mikrotik_ipv6_firewall_rule { 'SSH_DROP':
          ensure           => 'enabled',
          table            => 'filter',
          chain            => 'SSH',
          src_address_list => 'ssh_block',
          action           => 'drop',
        }

        mikrotik_ipv6_firewall_rule { 'SSH_STAGE3':
          ensure           => 'disabled',
          table            => 'filter',
          chain            => 'SSH',
          connection_state => 'new',
          src_address_list => 'ssh_stage3',          
          action           => 'add-src-to-address-list',  
          address_list     => 'ssh_block',
        }
        
        mikrotik_ipv6_firewall_rule { 'SSH_STAGE2':
          table                => 'filter',
          chain                => 'SSH',
          connection_state     => 'new',
          src_address_list     => 'ssh_stage2',          
          action               => 'add-src-to-address-list',
          address_list         => 'ssh_stage3',
          address_list_timeout => '1m',
        }
        
        mikrotik_ipv6_firewall_rule { 'SSH_STAGE1':
          table                => 'filter',
          chain                => 'SSH',
          connection_state     => 'new',
          src_address_list     => 'ssh_stage1',
          action               => 'add-src-to-address-list',
          address_list         => 'ssh_stage2',            
          address_list_timeout => '1m',
        }
        
        mikrotik_ipv6_firewall_rule { 'SSH_NEW':
          table                => 'filter',
          chain                => 'SSH',
          connection_state     => 'new',
          action               => 'add-src-to-address-list',
          address_list         => 'ssh_stage1',
          address_list_timeout => '1m',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "clean up ssh brute-force rules" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { ['SSH_JUMP', 'SSH_DROP', 'SSH_STAGE3', 'SSH_STAGE2', 'SSH_STAGE1', 'SSH_NEW']:
          table  => 'filter',
          ensure => 'absent',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

describe '/ipv6/firewall ordering' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'
  
  context "insert rules with simple ordering" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { 'unsorted_1':
          ensure           => present,
          table            => 'mangle',
          chain            => 'unsorted_1',
          src_address      => '2001:db8:1111::/64',
          action           => 'accept',
        }
  
        mikrotik_ipv6_firewall_rule { 'rule_a':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 1,          
          src_address      => '2001:db8:2222::/64',
          action           => 'accept',
        }
  
        mikrotik_ipv6_firewall_rule { 'rule_d':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 3,          
          src_address      => '2001:db8:2224::/64',
          action           => 'accept',
        }
  
        mikrotik_ipv6_firewall_rule { 'unsorted_2':
          ensure           => present,
          table            => 'mangle',
          chain            => 'unsorted_2',
          src_address      => '2001:db8:1112::/64',
          action           => 'accept',
        }
  
        mikrotik_ipv6_firewall_rule { 'rule_b':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 2,          
          src_address      => '2001:db8:2221::/64',
          action           => 'accept',
        }   
  
        mikrotik_ipv6_firewall_rule { 'rule_f':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 5,          
          src_address      => '2001:db8:2227::/64',
          action           => 'accept',
        }
  
        mikrotik_ipv6_firewall_rule { 'rule_e':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 4,          
          src_address      => '2001:db8:2225::/64',
          action           => 'accept',
        }
          
        mikrotik_ipv6_firewall_rule { 'unsorted_3':
          ensure           => present,
          table            => 'mangle',
          chain            => 'unsorted_3',
          src_address      => '2001:db8:1113::/64',
          action           => 'accept',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "insert more rules" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { 'rule_c':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 3,          
          src_address      => '2001:db8:2223::/64',
          action           => 'accept',
        }
  
        mikrotik_ipv6_firewall_rule { 'rule_g':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 7,          
          src_address      => '2001:db8:2226::/64',
          action           => 'accept',
        }       
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "move some rules" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { 'rule_a':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 2,
        }
              
        mikrotik_ipv6_firewall_rule { 'rule_b':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 1,
        }
          
        mikrotik_ipv6_firewall_rule { 'rule_g':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 6,
        }          
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "move rule to start of chain" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { 'rule_f':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 1,
        }    
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "move rule to end of chain" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { 'rule_b':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 7,
        }           
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "complex move" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ipv6_firewall_rule { 'unsorted_1':
          ensure           => absent,
          table            => 'mangle',
          chain            => 'unsorted_1',
        }
        
        mikrotik_ipv6_firewall_rule { 'unsorted_2':
          ensure           => absent,
          table            => 'mangle',
          chain            => 'unsorted_2',
        }
        
        mikrotik_ipv6_firewall_rule { 'unsorted_3':
          ensure           => absent,
          table            => 'mangle',
          chain            => 'unsorted_3',
        }
          
        mikrotik_ipv6_firewall_rule { 'rule_f':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 2,
        }      
  
        mikrotik_ipv6_firewall_rule { 'rule_g':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 3,
        } 
        
        mikrotik_ipv6_firewall_rule { 'rule_e':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 4,
        } 
        
        mikrotik_ipv6_firewall_rule { 'rule_d':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 5,
        } 
        
        mikrotik_ipv6_firewall_rule { 'rule_c':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 6,
        } 
  
        mikrotik_ipv6_firewall_rule { 'rule_a':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 7,
        } 
        
        mikrotik_ipv6_firewall_rule { 'rule_b':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 8,
        } 
  
        mikrotik_ipv6_firewall_rule { 'rule_h':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 9,          
          src_address      => '2001:db8:2220::/64',
          action           => 'accept',
        }  
  
        mikrotik_ipv6_firewall_rule { 'rule_i':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 1,          
          src_address      => '2001:db8:2228::/64',
          action           => 'accept',
        }  
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "cleanup" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_firewall_rule { ['unsorted_1', 'unsorted_2', 'unsorted_3']:
          ensure => absent,  
          table  => 'mangle',        
        }
  
        mikrotik_ipv6_firewall_rule { ['rule_a', 'rule_b', 'rule_c', 'rule_d', 'rule_e', 'rule_f', 'rule_g', 'rule_h', 'rule_i']:
          ensure => absent,   
          table  => 'mangle',       
        }     
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end


File: /spec\acceptance\ipv6_spec.rb
require 'spec_helper_acceptance'

describe '/system/package' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_package { 'ipv6':
          ensure => enabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "disable package" do      
    it 'should update master' do
      site_pp = <<-EOS           
        mikrotik_package { 'ipv6':
          ensure => disabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end

    it_behaves_like 'an idempotent device run'
  end

  context "enable package and reboot" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_package { 'ipv6':
          ensure       => enabled,
          force_reboot => true          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end

    it_behaves_like 'an idempotent device run'
  end
end

describe '/ipv6/address' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_address { ['2001:db8:1::/64', '2001:db8:2::/64']:
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  

  context "create new address" do
    it 'should update master' do
      site_pp = <<-EOS
        # TODO: fix and test: "eui64 => true" is never idempotent!                                                              # TODO !
      
        mikrotik_ipv6_address { '2001:db8:1::1/64':
          interface => 'ether1',
          advertise => false,
        }
        
        mikrotik_ipv6_address { '2001:db8:2::1/64':
          ensure    => disabled,          
          interface => 'ether1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "enable/disable address" do
    it 'should update master' do
      site_pp = <<-EOS       
      mikrotik_ipv6_address { '2001:db8:1::1/64':
          ensure    => disabled,          
          interface => 'ether1',
        }
        
        mikrotik_ipv6_address { '2001:db8:2::1/64':
          ensure    => enabled,          
          interface => 'ether1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

describe '/ipv6/route' do
  before { skip("Skipping this test for now") }

  include_context 'testnodes defined'

  context "reset configuration" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_route { ['test_route61', 'test_route62']:
          ensure => absent,
        }
      EOS

      set_site_pp_on_master(site_pp)
    end

    it_behaves_like 'an idempotent device run after failures', 1
  end  

  context "create ip routes" do
    it 'should update master' do
      site_pp = <<-EOS      
        mikrotik_ipv6_route { 'test_route61':
          dst_address  => '2000::/4',
          gateway      => 'ether1',
          distance     => 50,
        }  

        mikrotik_ipv6_route { 'test_route62':
          ensure      => disabled,
          dst_address => '1000::/4',
          type        => 'unreachable',
        }
      EOS

      set_site_pp_on_master(site_pp)
    end

    it_behaves_like 'an idempotent device run'
  end

  context "update ip route" do
    it 'should update master' do
      site_pp = <<-EOS      
        mikrotik_ipv6_route { 'test_route61':
          dst_address   => '2000::/3',
          distance      => 60,
          check_gateway => ping,
        }     
          
        mikrotik_ipv6_route { 'test_route62':
          ensure      => enabled,
          dst_address => 'a000::/4',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end  
end

describe '/ipv6/pool' do  
  before { skip("Skipping this test for now") }
    
  include_context 'testnodes defined'
  
  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS              
        mikrotik_ipv6_pool { ['SWIMMING']:
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "create new ip pool" do
    it 'should update master' do
      site_pp = <<-EOS        
        mikrotik_ipv6_pool { 'SWIMMING':
          prefix        => '2001:db8:1000::/48',
          prefix_length => '56',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

describe '/ipv6/dhcp' do  
  before { skip("Skipping this test for now") }
    
  include_context 'testnodes defined'
  
  context "reset configuration" do           
    it 'should update master' do
      site_pp = <<-EOS        
        mikrotik_dhcpv6_server { 'DHCPD1':
          ensure => absent,
        }
  
        mikrotik_dhcpv6_client { 'ether1':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 2
  end  
  
  # Server
  context "create dhcp server" do            
    it 'should update master' do
      site_pp = <<-EOS
        # Default = disabled (!)
        mikrotik_dhcpv6_server { 'DHCPD1':
          interface     => 'ether1',
          lease_time    => '6h',
          address_pool  => 'SWIMMING',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable dhcp server" do  
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_dhcpv6_server { 'DHCPD1':
          ensure => disabled
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "enable dhcp server" do       
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_dhcpv6_server { 'DHCPD1':
          ensure     => enabled,
          lease_time => '2h'
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  # Client
  context "create dhcp client" do            
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_dhcpv6_client { 'ether1':
          request_address => true,
          use_peer_dns    => true,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable dhcp client" do  
    it 'should update master' do
      site_pp = <<-EOS
      mikrotik_dhcpv6_client { 'ether1':
          ensure => disabled
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update dhcp client" do       
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_dhcpv6_client { 'ether1':
          request_prefix => true,
          pool_name      => 'TESTPOOL'
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

describe '/ipv6/nd' do  
  before { skip("Skipping this test for now") }
    
  include_context 'testnodes defined'
  
  context "reset configuration" do           
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_nd_interface { 'ether1':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  

  context "create nd interface" do            
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_nd_interface { 'ether1':    
          hop_limit     => 10,
          advertise_dns => true,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable nd interface" do  
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_nd_interface { 'ether1':
          ensure => disabled
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update nd interface" do       
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ipv6_nd_interface { 'ether1': 
          ra_delay               => '5s',
          reachable_time         => '30s', 
          managed_address_config => true,
          other_config           => true,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end


File: /spec\acceptance\ip_address_spec.rb
require 'spec_helper_acceptance'

describe '/ip/address' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ip_address { ['192.168.201.1/24', '192.168.202.1/24']:
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "create new address" do
    it 'should update master' do
      site_pp = <<-EOS      
        mikrotik_ip_address { '192.168.201.1/24':
          interface => 'ether1',
        }
        
        mikrotik_ip_address { '192.168.202.1/24':
          ensure    => disabled,
          interface => 'ether1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "enable address" do
    it 'should update master' do
      site_pp = <<-EOS           
        mikrotik_ip_address { '192.168.202.1/24':
          ensure    => enabled,
          interface => 'ether1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

describe '/ip/pool' do  
  before { skip("Skipping this test for now") }
    
  include_context 'testnodes defined'
  
  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS              
        mikrotik_ip_pool { ['SWIMMING', 'POOL2']:
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "create new ip pool" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ip_pool { 'POOL2':
          ranges => '172.23.9.1-172.23.9.100'
        }
        
        mikrotik_ip_pool { 'SWIMMING':
          ranges => [
            '172.23.0.1-172.23.3.255',
            '172.23.5.1-172.23.8.255',
          ],
          next_pool => 'POOL2',
        }    
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

describe '/ip/dhcp' do  
  before { skip("Skipping this test for now") }
    
  include_context 'testnodes defined'
  
  context "reset configuration" do           
    it 'should update master' do
      site_pp = <<-EOS        
        mikrotik_dhcp_server { ['DHCPD1', 'DHCPD2']:
          ensure => absent,
        }
        
        mikrotik_dhcp_server_network { 'DHCPD_NET1':
          ensure => absent,
        }
                      
        mikrotik_interface_vlan { ['VLAN_DHCP1', 'VLAN_DHCP2']:
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 3
  end  
  
  context "create dhcp server" do            
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_vlan { 'VLAN_DHCP1':
          vlan_id   => '4010',
          interface => 'ether1',
        }
          
        mikrotik_interface_vlan { 'VLAN_DHCP2':
          vlan_id   => '4020',
          interface => 'ether1',
        }
        
        # Default = disabled (!)
        mikrotik_dhcp_server { 'DHCPD1':
          interface     => 'VLAN_DHCP1',
          lease_time    => '6h',
          address_pool  => 'SWIMMING',
          authoritative => 'after-2sec-delay',
          use_radius    => true,
        }
          
        mikrotik_dhcp_server { 'DHCPD2':
          ensure        => enabled,
          interface     => 'VLAN_DHCP2',
          lease_time    => '1h',
          address_pool  => 'SWIMMING',
          authoritative => 'after-10sec-delay',
          use_radius    => false,
        }
          
        mikrotik_dhcp_server_network { '172.21.100.0/24':    
          gateways    => ['172.21.100.1', '172.21.100.2'],
          dns_servers => ['105.235.209.31', '105.235.209.32'],
          domain      => 'rcswimax.com',
        }   
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "enable dhcp server" do       
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_dhcp_server { 'DHCPD1':
          ensure => enabled
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable dhcp server" do  
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_dhcp_server { 'DHCPD1':
          ensure => disabled
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

end


File: /spec\acceptance\ip_firewall_spec.rb
require 'spec_helper_acceptance'

describe '/ip/firewall' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { ['Puppet Test 1', 'Puppet Test 2', 'Puppet Test 3']:
          ensure => absent, 
          table  => 'filter',          
        }
        
        mikrotik_firewall_rule { ['SSH_JUMP', 'SSH_DROP', 'SSH_STAGE3', 'SSH_STAGE2', 'SSH_STAGE1', 'SSH_NEW']:
          ensure => absent, 
          table  => 'filter',          
        }
        
        mikrotik_firewall_rule { ['unsorted_1', 'unsorted_2', 'unsorted_3']:
          ensure => absent, 
          table  => 'mangle',          
        }
  
        mikrotik_firewall_rule { ['rule_a', 'rule_b', 'rule_c', 'rule_d', 'rule_e', 'rule_f', 'rule_g', 'rule_h', 'rule_i']:
          ensure => absent,    
          table  => 'mangle',       
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "create 3 new rules" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { 'Puppet Test 1':
          ensure      => present,
          table       => 'filter',
          chain       => 'input',
          src_address => '1.1.1.1',
          action      => 'accept',
          #sequence    => '3',
        }
        
        mikrotik_firewall_rule { 'Puppet Test 2':
          ensure      => enabled,
          table       => 'filter',
          chain       => 'input',
          src_address => '1.1.1.2',
          action      => 'accept',
          #sequence    => '3',
        }
        
        mikrotik_firewall_rule { 'Puppet Test 3':
          ensure      => disabled,
          table       => 'filter',
          chain       => 'input',
          src_address => '1.1.1.3',
          action      => 'accept',
          #sequence    => '3',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update a rule" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { 'Puppet Test 1':
          table       => 'filter',
          chain       => 'input',
          src_address => '2.1.1.1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "delete a rule" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { 'Puppet Test 2':
           ensure => 'absent',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "ssh brute-force rules" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { 'SSH_JUMP':
          ensure           => present,
          table            => 'filter',
          chain            => 'input',
          protocol         => 'tcp',
          dst_port         => '22',
          src_address_list => "!RCS_INFRA",
          action           => 'jump',
          jump_target      => 'SSH',
        }
        
        mikrotik_firewall_rule { 'SSH_DROP':
          ensure           => 'enabled',
          table            => 'filter',
          chain            => 'SSH',
          src_address_list => 'ssh_block',
          action           => 'drop',
        }

        mikrotik_firewall_rule { 'SSH_STAGE3':
          ensure           => 'disabled',
          table            => 'filter',
          chain            => 'SSH',
          connection_state => 'new',
          src_address_list => 'ssh_stage3',          
          action           => 'add-src-to-address-list',  
          address_list     => 'ssh_block',
        }
        
        mikrotik_firewall_rule { 'SSH_STAGE2':
          table                => 'filter',
          chain                => 'SSH',
          connection_state     => 'new',
          src_address_list     => 'ssh_stage2',          
          action               => 'add-src-to-address-list',
          address_list         => 'ssh_stage3',
          address_list_timeout => '1m',
        }
        
        mikrotik_firewall_rule { 'SSH_STAGE1':
          table                => 'filter',
          chain                => 'SSH',
          connection_state     => 'new',
          src_address_list     => 'ssh_stage1',
          action               => 'add-src-to-address-list',
          address_list         => 'ssh_stage2',            
          address_list_timeout => '1m',
        }
        
        mikrotik_firewall_rule { 'SSH_NEW':
          table                => 'filter',
          chain                => 'SSH',
          connection_state     => 'new',
          action               => 'add-src-to-address-list',
          address_list         => 'ssh_stage1',
          address_list_timeout => '1m',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "clean up ssh brute-force rules" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { ['SSH_JUMP', 'SSH_DROP', 'SSH_STAGE3', 'SSH_STAGE2', 'SSH_STAGE1', 'SSH_NEW']:
          table  => 'filter',
          ensure => 'absent',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

describe '/ip/firewall ordering' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'
  
  context "insert rules with simple ordering" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { 'unsorted_1':
          ensure           => present,
          table            => 'mangle',
          chain            => 'unsorted_1',
          src_address      => '1.1.1.1',
          action           => 'accept',
        }
  
        mikrotik_firewall_rule { 'rule_a':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 1,          
          src_address      => '2.2.2.2',
          action           => 'accept',
        }
  
        mikrotik_firewall_rule { 'rule_d':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 3,          
          src_address      => '2.2.2.4',
          action           => 'accept',
        }
  
        mikrotik_firewall_rule { 'unsorted_2':
          ensure           => present,
          table            => 'mangle',
          chain            => 'unsorted_2',
          src_address      => '1.1.1.2',
          action           => 'accept',
        }
  
        mikrotik_firewall_rule { 'rule_b':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 2,          
          src_address      => '2.2.2.1',
          action           => 'accept',
        }   
  
        mikrotik_firewall_rule { 'rule_f':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 5,          
          src_address      => '2.2.2.7',
          action           => 'accept',
        }
  
        mikrotik_firewall_rule { 'rule_e':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 4,          
          src_address      => '2.2.2.5',
          action           => 'accept',
        }
          
        mikrotik_firewall_rule { 'unsorted_3':
          ensure           => present,
          table            => 'mangle',
          chain            => 'unsorted_3',
          src_address      => '1.1.1.3',
          action           => 'accept',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "insert more rules" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { 'rule_c':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 3,          
          src_address      => '2.2.2.3',
          action           => 'accept',
        }
  
        mikrotik_firewall_rule { 'rule_g':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 7,          
          src_address      => '2.2.2.6',
          action           => 'accept',
        }       
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "move some rules" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { 'rule_a':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 2,
        }
              
        mikrotik_firewall_rule { 'rule_b':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 1,
        }
          
        mikrotik_firewall_rule { 'rule_g':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 6,
        }          
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "move rule to start of chain" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { 'rule_f':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 1,
        }    
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "move rule to end of chain" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { 'rule_b':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 7,
        }           
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "complex move" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_firewall_rule { 'unsorted_1':
          ensure           => absent,
          table            => 'mangle',
          chain            => 'unsorted_1',
        }
        
        mikrotik_firewall_rule { 'unsorted_2':
          ensure           => absent,
          table            => 'mangle',
          chain            => 'unsorted_2',
        }
        
        mikrotik_firewall_rule { 'unsorted_3':
          ensure           => absent,
          table            => 'mangle',
          chain            => 'unsorted_3',
        }
          
        mikrotik_firewall_rule { 'rule_f':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 2,
        }      
  
        mikrotik_firewall_rule { 'rule_g':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 3,
        } 
        
        mikrotik_firewall_rule { 'rule_e':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 4,
        } 
        
        mikrotik_firewall_rule { 'rule_d':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 5,
        } 
        
        mikrotik_firewall_rule { 'rule_c':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 6,
        } 
  
        mikrotik_firewall_rule { 'rule_a':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 7,
        } 
        
        mikrotik_firewall_rule { 'rule_b':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 8,
        } 
  
        mikrotik_firewall_rule { 'rule_h':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 9,          
          src_address      => '2.2.2.0/30',
          action           => 'accept',
        }  
  
        mikrotik_firewall_rule { 'rule_i':
          ensure           => present,
          table            => 'mangle',
          chain            => 'order_test',
          chain_order      => 1,          
          src_address      => '2.2.2.8',
          action           => 'accept',
        }  
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "cleanup" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_firewall_rule { ['unsorted_1', 'unsorted_2', 'unsorted_3']:
          ensure => absent,  
          table  => 'mangle',        
        }
  
        mikrotik_firewall_rule { ['rule_a', 'rule_b', 'rule_c', 'rule_d', 'rule_e', 'rule_f', 'rule_g', 'rule_h', 'rule_i']:
          ensure => absent,   
          table  => 'mangle',       
        }     
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end


File: /spec\acceptance\ip_hotspot_spec.rb
require 'spec_helper_acceptance'

describe '/ip/hotspot' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ip_hotspot_profile { 'hs_profile_a':
          ensure => 'absent',
        }
        mikrotik_ip_hotspot { 'hotspot1':
          ensure => 'absent',
        }

        mikrotik_interface_vlan { 'VLAN_4001':  
          ensure    => present,    
          vlan_id   => '4001',
          interface => 'ether1',
        }
        
        mikrotik_ip_pool { 'POOL2':
          ensure => present,    
          ranges => '172.23.9.1-172.23.9.100'
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 4
  end  
  
  context "create hotspot" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ip_hotspot_profile { 'hs_profile_a':
          hotspot_address       => '192.168.88.1',
          login_by              => [ 'http-chap', 'cookie' ],
          use_radius            => true,
          radius_interim_update => '5m',
        }
        
        mikrotik_ip_hotspot { 'hotspot1':
          ensure            => 'enabled',
          interface         => 'VLAN_4001',
          address_pool      => 'POOL2',
          profile           => 'default',
          keepalive_timeout => '1m',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update hotspot" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ip_hotspot_profile { 'hs_profile_a':
          split_user_domain     => true,
          radius_default_domain => 'CLIENT',
        }
        
        mikrotik_ip_hotspot { 'hotspot1':
          ensure       => 'enabled',
          profile      => 'hs_profile_a',
          idle_timeout => '2m',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable hotspot" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ip_hotspot { 'hotspot1':
          ensure => 'disabled',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end


File: /spec\acceptance\ip_service_spec.rb
require 'spec_helper_acceptance'

describe '/ip/service' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ip_service { 'telnet':
          ensure => 'disabled',
        }
        mikrotik_ip_service { 'api-ssl':
          ensure => 'enabled',
        }
        mikrotik_ip_service { 'www':
          addresses => [],
        }
        mikrotik_ip_service { 'ftp':
          port => 21,
        }  
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "valid changes" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ip_service { 'telnet':
          ensure => 'enabled',
        }
        mikrotik_ip_service { 'api-ssl':
          ensure => 'disabled',
        }
        mikrotik_ip_service { 'www':
          addresses => ['83.101.0.0/16', '172.16.0.0/12'],
        }
        mikrotik_ip_service { 'ftp':
          port      => 2121,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "addresses clearing" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ip_service { 'www':
          addresses => [],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end


File: /spec\acceptance\logging_spec.rb
require 'spec_helper_acceptance'

describe '/system/logging' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_logging_rule { 'info_!dhcp_myRemote':
          ensure => absent,
          topics => ['info','!dhcp'],
          action => 'myRemote',
        }
          
        mikrotik_logging_rule { 'debug_!dhcp_myRemote':
          ensure => absent,
          topics => ['info','!dhcp'],
          action => 'myRemote',
        }
        
        mikrotik_logging_action { 'myRemote':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 2
  end  
  
  context "log to new action" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_logging_action { 'myRemote':
          remote      => '105.235.209.12',
          remote_port => 5143,
          src_address => '172.20.111.69',
        }
        
        mikrotik_logging_rule { 'debug_!dhcp_myRemote':
          topics => ['debug','!dhcp'],
          action => 'myRemote',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update rule and action" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_logging_action { 'myRemote':
          src_address => '105.235.209.44',
        }
        
        mikrotik_logging_rule { 'debug_!dhcp_myRemote':
          ensure => absent,
          topics => ['debug','!dhcp'],
          action => 'myRemote',
        }
        
        mikrotik_logging_rule { 'info_!dhcp_myRemote':
          topics => ['info','!dhcp'],
          action => 'myRemote',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "clean up" do
    it 'should update master' do
      site_pp = <<-EOS        
        mikrotik_logging_rule { 'info_!dhcp_myRemote':
          ensure => absent,
          topics => ['info','!dhcp'],
          action => 'myRemote',
        }
        
        mikrotik_logging_action { 'myRemote':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "incomplete rule" do
    it 'should update master' do
      site_pp = <<-EOS                   
        mikrotik_logging_rule { 'debug_remote':
          topics => ['debug'],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end

    it_behaves_like 'a faulty device run'
  end
end


File: /spec\acceptance\mpls_spec.rb
require 'spec_helper_acceptance'

describe '/mpls ldp' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_ldp { 'ldp':
          ensure            => disabled,
          lsr_id            => '0.0.0.0',
          transport_address => '0.0.0.0',
          loop_detect       =>  false,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "update ldp" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_ldp { 'ldp':
          ensure            => enabled,
          lsr_id            => '105.235.209.44',
          transport_address => '172.20.111.69',
          loop_detect       =>  true,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
# TODO - exist code = 0 ??? => Find other way to detect error...
#  context "with ensure absent" do
#    it 'should update master' do
#      site_pp = <<-EOS
#        mikrotik_mpls_ldp { 'ldp':
#          ensure => 'absent',
#        }
#      EOS
#      
#      set_site_pp_on_master(site_pp)
#    end
#  
#    it_behaves_like 'a faulty device run'
#  end
#  
#  context "with wrong title" do
#    it 'should update master' do
#      site_pp = <<-EOS
#        mikrotik_mpls_ldp { 'myLDP2':
#        
#        }
#      EOS
#      
#      set_site_pp_on_master(site_pp)
#    end
#  
#    it_behaves_like 'a faulty device run'
#  end
end

describe '/mpls ldp interface' do
  before { skip("Skipping this test for now") }

  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_ldp_interface { 'ether1':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "create ldp interface" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_ldp_interface { 'ether1':
          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update ldp interface" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_ldp_interface { 'ether1':
          hello_interval           => '10s',
          hold_time                => '30s',
          transport_address        => '10.0.2.15',
          accept_dynamic_neighbors => false,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable ldp interface" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_ldp_interface { 'ether1':
          ensure => disabled,          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "enable ldp interface" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_ldp_interface { 'ether1':
          ensure => enabled,          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "remove ldp interface" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_ldp_interface { 'ether1':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

File: /spec\acceptance\mpls_te_spec.rb
require 'spec_helper_acceptance'

describe '/mpls te' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_te { 'TE_TUNNEL':
          ensure => absent,
        }

        mikrotik_mpls_te_path { 'dynamic':
          ensure => absent,
        }
        
        mikrotik_mpls_te_path { 'static':
          ensure => absent,
        }
      
        mikrotik_mpls_te_interface { 'ether1':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    #it_behaves_like 'an idempotent device run after failures', 1
    it_behaves_like 'an idempotent device run'
  end  
  
  context "create te interface" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_te_interface { 'ether1':
          bandwidth => '10000000',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update te interface" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_te_interface { 'ether1':
          bandwidth => '20000000',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

    
  context "create te path" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_te_path { 'dynamic':
          
        }
        
        mikrotik_mpls_te_path { 'static':
          use_cspf     => false,
          hops         => [ '1.1.1.1:loose', '1.1.1.2:loose', '1.1.1.3:loose' ],
          record_route => true,
          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update te path" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_mpls_te_path { 'dynamic':
          record_route => true,
        }
        
        mikrotik_mpls_te_path { 'static':
          hops         => [ '1.1.1.1:strict', '1.1.1.2:strict', '1.1.1.3:strict' ],
          record_route => false,
        }        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
    
  context "create te tunnel" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_te { 'TE_TUNNEL':
          from_address    => '2.2.2.1',
          to_address      => '2.2.2.2',
          bandwidth       => '20000000',
          primary_path    => 'static',
          secondary_paths => [ 'dynamic' ],
          record_route    => true,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update te tunnel" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_te { 'TE_TUNNEL':
          ensure                 => enabled,
          bandwidth_limit        => '90',
          auto_bandwidth_range   => '10000000-30000000',
          auto_bandwidth_reserve => '10',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

File: /spec\acceptance\nodesets\default.yml
HOSTS:
  puppet:
    roles:
      - master
    platform: ubuntu-16.04-x64
    box: puppetlabs/ubuntu-16.04-64-puppet
    box_url: https://vagrantcloud.com/puppetlabs/boxes/ubuntu-16.04-64-puppet
    hypervisor: vagrant
    vagrant_memsize: 4096
  ubuntu-16-04:
    roles:
      - agent
    platform: ubuntu-16.04-x64
    box: puppetlabs/ubuntu-16.04-64-puppet
    box_url: https://vagrantcloud.com/puppetlabs/boxes/ubuntu-16.04-64-puppet
    hypervisor: vagrant
CONFIG:
  log_level: debug
  type: aio
  vagrant_memsize: 2048


File: /spec\acceptance\ppp_spec.rb
require 'spec_helper_acceptance'

describe '/ppp' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_aaa { 'aaa':
          use_radius     => false,
          accounting     => false,
          interim_update => '1m',
        }
  
        mikrotik_ppp_profile { ['profile1', 'profile2']:
          ensure => absent,
        }
                  
        mikrotik_ppp_server { ['pptp', 'l2tp']:
          ensure => 'disabled',          
        }
        
        mikrotik_ppp_secret  { ['ppp_user1', 'ppp_user2']:
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 4
  end  
  
  context "create ppp profiles" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_profile { 'profile1':
          # Defaults
        }
             
        mikrotik_ppp_profile { 'profile2':
          local_address   => '192.168.0.1',
          incoming_filter => 'PPP_FILTER',
          address_list    => 'PPP_USERS',
          use_compression => 'yes',
          use_encryption  => 'required',
          session_timeout => '1h',
          rate_limit      => '256k/1M',   
          only_one        => 'no',       
        }      
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update ppp profile" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_profile { 'profile1':
          outgoing_filter => 'PPP_FILTER_OUT',
          use_compression => 'no',
          idle_timeout    => '10m',          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "correct aaa settings" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_aaa { 'aaa':
          use_radius     => true,
          accounting     => true,
          interim_update => '5m',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "disable aaa" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_aaa { 'aaa':
          use_radius => false,
          accounting => false,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
    
  context "with wrong title" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_aaa { 'myAAA2':
          use_radius     => true,
          interim_update => '10m',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'a faulty device run'
  end

  context "pptp server" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_server { 'pptp':
          authentication  => ['pap', 'chap'],
          default_profile => 'profile1',
        }
        
        mikrotik_ppp_server { 'l2tp':
          ensure          => 'present',
          authentication  => ['chap', 'mschap1'],
          default_profile => 'profile1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'    
  end

  context "l2tp server" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_server { 'pptp':
          ensure => 'disabled',
        }
      
        mikrotik_ppp_server { 'l2tp':
          ensure          => 'enabled',
          authentication  => ['mschap1'],
          default_profile => 'profile2',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'    
  end

  context "server with wrong title" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_server { 'myPPPServer':
          ensure => enabled,# TODO: BUG - does not enforce if ensure != enabled/disabled !!!
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end

    it_behaves_like 'a faulty device run'  
  end

  context "create secret" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_secret  { 'ppp_user1':
          password       => 'password',
          service        => 'any',
          profile        => 'profile1',
          local_address  => '192.168.10.1',  
          remote_address => '192.168.10.2',      
        }
        
        mikrotik_ppp_secret  { 'ppp_user2':
          ensure         => 'disabled',
          password       => 'password',
          service        => 'pptp',
          routes         => ['192.168.11.0/24', '192.168.12.0/24'],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update secret" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_secret  { 'ppp_user1':
          ensure         => 'present',
          password       => 'password2',    
          profile        => 'profile2',
          local_address  => '192.168.10.5',  
          remote_address => '192.168.10.6',  
        }
        
        mikrotik_ppp_secret  { 'ppp_user2':
          ensure         => 'enabled',
          service        => 'l2tp',
          routes         => ['192.168.11.1/24'],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "disable secret" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ppp_secret  { 'ppp_user1':
          ensure => 'disabled',
        }
        
        mikrotik_ppp_secret  { 'ppp_user2':
          ensure => 'absent',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end


describe '/pppoe' do
  #before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_pppoe_server { 'PPPOE1':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 4
  end  

  # DISABLED BY DEFAULT!
  context "create server" do
    it 'should create server' do
      site_pp = <<-EOS
        mikrotik_interface_pppoe_server { 'PPPOE1':
          interface            => 'ether1',
          one_session_per_host => true,
          pado_delay           => 5000,          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update server" do
    it 'should update server' do
      site_pp = <<-EOS
        mikrotik_interface_pppoe_server { 'PPPOE1':
          interface            => 'ether1',
          one_session_per_host => false,
          pado_delay           => 0,          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "enable server" do
    it 'should enable server' do
      site_pp = <<-EOS
        mikrotik_interface_pppoe_server { 'PPPOE1':
          interface => 'ether1',
          ensure    => 'enabled'
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end


File: /spec\acceptance\radius_spec.rb
require 'spec_helper_acceptance'

describe '/radius' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_radius_server { 'auth-backup':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "add server" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_radius_server { 'auth-backup':
          services => ['ppp'],
          address  => '1.2.3.4',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "configure server" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_radius_server { 'auth-backup':
          services    => ['ppp', 'hotspot'],
          auth_port   => 18120,
          acct_port   => 18130,
          secret      => 'password',
          src_address => '1.2.3.5',
          timeout     => '3s',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  # TODO remove
end


File: /spec\acceptance\romon_spec.rb
require 'spec_helper_acceptance'

describe '/tool/romon' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_romon { 'romon':
          ensure  => disabled,
          secrets => [],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "correct settings" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_romon { 'romon':
          ensure  => enabled,
          secrets => ["secret1", "secret2"],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable romon" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_romon { 'romon':
          ensure  => disabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "enable romon" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_romon { 'romon':
          ensure  => enabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "with wrong title" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_romon { 'myRMN':
          secrets => ["secret1", "secret2"],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'a faulty device run'
  end
end

describe '/tool/romon/port' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_romon_port { 'all':
          ensure  => enabled,
          forbid  => false,
          cost    => 100,
          secrets => [],
        }
        
        mikrotik_romon_port { 'ether1':
          ensure  => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "add interface" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_romon_port { 'ether1':
          ensure  => enabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "change settings for ether1" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_romon_port { 'ether1':
          ensure  => enabled,
          forbid  => false,
          secrets => ["overwrite1"],
          cost    => 200,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "change settings for all" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_romon_port { 'all':
          ensure  => enabled,
          forbid  => true,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable interface" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_romon_port { 'ether1':
          ensure  => disabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end  
end


File: /spec\acceptance\route_spec.rb
require 'spec_helper_acceptance'

describe '/ip/route' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ip_route { ['test_route1', 'test_route2']:
          ensure => absent,
        }
    
        mikrotik_ip_route_rule { ['test_rule1', 'test_rule2']:
          ensure => absent,
        }
                  
        mikrotik_ip_route_vrf { 'VRF_1001':
          ensure => absent,
        }
  
        mikrotik_interface_vlan { 'VRF_VLAN1001':
          ensure => absent,          
        }        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 4
  end  
  
  context "create ip routes" do
    it 'should update master' do
      site_pp = <<-EOS      
        mikrotik_ip_route { 'test_route1':
          dst_address  => '172.22.0.0/24',
          gateway      => '172.16.0.1',
          distance     => 50,
          routing_mark => 'TEST_TABLE',
        }  
        
        mikrotik_ip_route { 'test_route2':
          ensure      => disabled,
          dst_address => '172.22.1.0/24',
          type        => 'blackhole',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update ip route" do
    it 'should update master' do
      site_pp = <<-EOS      
        mikrotik_ip_route { 'test_route1':
          dst_address   => '172.22.0.0/24',
          distance      => 60,
          check_gateway => ping,
        }     
          
        mikrotik_ip_route { 'test_route2':
          ensure      => enabled,
          dst_address => '172.22.1.0/24',
        }     
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "create ip route rule" do
    it 'should update master' do
      site_pp = <<-EOS      
        mikrotik_ip_route_rule { 'test_rule1':
          ensure      => disabled,
          src_address => '172.24.0.0/24',
          dst_address => '172.24.1.0/24',     
          action      => unreachable,
        }   
        
        mikrotik_ip_route_rule { 'test_rule2':
          ensure       => enabled,
          routing_mark => 'ROUTE_TABLE1',
          interface    => 'ether1',     
          action       => lookup,
          table        => 'ROUTE_TABLE1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "enable ip route rule" do
    it 'should update master' do
      site_pp = <<-EOS      
        mikrotik_ip_route_rule { 'test_rule1':
          ensure => enabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "create ip route vrf" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_interface_vlan { 'VRF_VLAN1001':
          vlan_id   => 1001,
          interface => 'ether1',
        }
      
        mikrotik_ip_route_vrf { 'VRF_1001':
          ensure     => enabled,
          interfaces => 'VRF_VLAN1001'
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "disable ip route vrf" do
    it 'should update master' do
      site_pp = <<-EOS      
      mikrotik_ip_route_vrf { 'VRF_1001':
          ensure => disabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

describe '/routing/filter ensurable' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS        
        mikrotik_routing_filter { ['test_filter1', 'test_filter2', 'test_filter3']:
          ensure => absent,          
        }        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  
  context "create new filter" do
    it 'should update master' do
      site_pp = <<-EOS   
        mikrotik_routing_filter { 'test_filter1':
          chain         => 'OSPF_TEST1',
          prefix        => '172.21.0.0/16',
          action        => 'discard',
        }
        
        mikrotik_routing_filter { 'test_filter2':
          ensure        => present,
          chain         => 'OSPF_TEST2',
          prefix        => '172.22.0.0/16',
          action        => 'discard',
        }     
        
        mikrotik_routing_filter { 'test_filter3':
          ensure        => disabled,
          chain         => 'OSPF_TEST3',
          prefix        => '172.23.0.0/16',
          action        => 'discard',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update filter" do
    it 'should update master' do
      site_pp = <<-EOS   
        mikrotik_routing_filter { 'test_filter1':
          ensure        => disabled,
          chain         => 'OSPF_TEST1',
          prefix        => '172.21.0.0/16',
          action        => 'discard',
        }
        
        mikrotik_routing_filter { 'test_filter2':
          chain         => 'OSPF_TEST2',
          prefix        => '172.22.0.0/16',
          action        => 'discard',
        }     
        
        mikrotik_routing_filter { 'test_filter3':
          ensure        => enabled,
          chain         => 'OSPF_TEST3',
          prefix        => '172.23.0.0/16',
          action        => 'discard',
        }            
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

describe '/routing/filter' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS        
        mikrotik_routing_filter { ['test_filter1', 'test_filter2', 'test_filter3']:
          ensure => absent,          
        }
                
        mikrotik_routing_filter { ['filter_chain2', 'filter_chain3', 'filter_chain4']:
          ensure => absent,          
        }
      
        mikrotik_routing_filter { ['filter_a', 'filter_b', 'filter_c', 'filter_d', 'filter_e', 'filter_f', 'filter_g', 'filter_h', 'filter_i']:
          ensure => absent,          
        }
        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 4
  end  
  
  
  context "create new filter" do
    it 'should update master' do
      site_pp = <<-EOS   
        mikrotik_routing_filter { 'test_filter1':
          chain         => 'OSPF_TEST1',
          prefix        => '172.22.0.0/16',
          prefix_length => '25-32',
          protocols     => ['ospf'],
          ospf_type     => 'external-type-2',
          action        => 'discard',
        }
        
        mikrotik_routing_filter { 'test_filter2':
          ensure       => enabled,
          chain        => 'BGP_IN_TEST2',        
          action       => 'jump',  
          jump_target  => 'test_filter3',
          set_distance => 150,
        }     
        
        mikrotik_routing_filter { 'test_filter3':
          ensure                 => disabled,
          chain                  => 'BGP_OUT_TEST3',
          protocols              => ['bgp'], 
          bgp_communities        => ['62123:20000', '62123:10000'],
          action                 => 'accept',
          set_bgp_weight         => 100,
          set_bgp_local_pref     => 150,
          set_bgp_prepend        => 3,   
          set_bgp_med            => 50,                   
          append_bgp_communities => ['62124:30000'],
        }              
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "enable/disable filter" do
    it 'should update master' do
      site_pp = <<-EOS   
        mikrotik_routing_filter { 'test_filter2':
          ensure => disabled,
          chain  => 'BGP_IN_TEST2',        
        }             
         
        mikrotik_routing_filter { 'test_filter3':
          ensure => enabled,
          chain  => 'BGP_OUT_TEST3',
        }              
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "sort on insert" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_routing_filter { 'filter_chain2':
          chain         => 'chain2',
          prefix        => '1.2.3.100',
          action        => 'accept',
        }
              
        mikrotik_routing_filter { 'filter_a':
          chain         => 'testing_sort',
          chain_order   => 1,
          prefix        => '1.2.3.2',
          action        => 'accept',
        }
  
        mikrotik_routing_filter { 'filter_d':
          chain         => 'testing_sort',
          chain_order   => 3,
          prefix        => '1.2.3.4',
          action        => 'accept',
        }
  
        mikrotik_routing_filter { 'filter_chain3':
          chain         => 'chain3',
          prefix        => '1.2.3.110',
          action        => 'accept',
        }

        mikrotik_routing_filter { 'filter_b':
          chain         => 'testing_sort',
          chain_order   => 2,
          prefix        => '1.2.3.1',
          action        => 'accept',
        }
        
        mikrotik_routing_filter { 'filter_f':
          chain         => 'testing_sort',
          chain_order   => 5,
          prefix        => '1.2.3.7',
          action        => 'accept',
        }
  
        mikrotik_routing_filter { 'filter_e':
          chain         => 'testing_sort',
          chain_order   => 4,
          prefix        => '1.2.3.5',
          action        => 'accept',
        }
  
        mikrotik_routing_filter { 'filter_chain4':
          chain         => 'chain4',
          prefix        => '1.2.3.120',
          action        => 'accept',
        }  
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "insert more" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_routing_filter { 'filter_c':
          chain         => 'testing_sort',
          chain_order   => 3,
          prefix        => '1.2.3.3',
          action        => 'accept',
        }
  
        mikrotik_routing_filter { 'filter_g':
          chain         => 'testing_sort',
          chain_order   => 7,
          prefix        => '1.2.3.6',
          action        => 'accept',
        }  
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "move filters" do
    it 'should update master' do
      site_pp = <<-EOS
        # side-by-side swap (starting FORWARD)
        mikrotik_routing_filter { 'filter_a':
          chain         => 'testing_sort',
          chain_order   => 2,
        }

        # Should not make a change anymore
        mikrotik_routing_filter { 'filter_b':
          chain         => 'testing_sort',
          chain_order   => 1,
        }  
        
        # BACKWARD change
        mikrotik_routing_filter { 'filter_g':
          chain         => 'testing_sort',
          chain_order   => 6,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "move filter to start of chain" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_routing_filter { 'filter_f':
          chain         => 'testing_sort',
          chain_order   => 1,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "move filter to end of chain" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_routing_filter { 'filter_b':
          chain         => 'testing_sort',
          chain_order   => 7,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "complex move" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_routing_filter { 'filter_chain2':
          ensure => absent,
        }
        
        mikrotik_routing_filter { 'filter_chain3':
          ensure => absent,
        }
        
        mikrotik_routing_filter { 'filter_chain4':
          ensure => absent,
        }      
      
        mikrotik_routing_filter { 'filter_f':
          chain         => 'testing_sort',
          chain_order   => 2,
        }  
        
        mikrotik_routing_filter { 'filter_g':
          chain         => 'testing_sort',
          chain_order   => 3,
        }  
        
        mikrotik_routing_filter { 'filter_e':
          chain         => 'testing_sort',
          chain_order   => 4,
        }  
        
        mikrotik_routing_filter { 'filter_d':
          chain         => 'testing_sort',
          chain_order   => 5,
        }  
      
        mikrotik_routing_filter { 'filter_c':
          chain         => 'testing_sort',
          chain_order   => 6,
        }
  
        mikrotik_routing_filter { 'filter_a':
          chain         => 'testing_sort',
          chain_order   => 7,
        }  
        
        mikrotik_routing_filter { 'filter_b':
          chain         => 'testing_sort',
          chain_order   => 8,
        }

        mikrotik_routing_filter { 'filter_h':
          chain         => 'testing_sort',
          chain_order   => 9,
          prefix        => '1.2.3.0/30',
          action        => 'accept',
        }  
        
        mikrotik_routing_filter { 'filter_i':
          chain         => 'testing_sort',
          chain_order   => 1,
          prefix        => '1.2.3.8',
          action        => 'accept',
        }  
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "cleanup" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_routing_filter { ['filter_chain2', 'filter_chain3', 'filter_chain4']:
          ensure => absent,          
        }
      
        mikrotik_routing_filter { ['filter_a', 'filter_b', 'filter_c', 'filter_d', 'filter_e', 'filter_f', 'filter_g', 'filter_h', 'filter_i']:
          ensure => absent,          
        }        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end


File: /spec\acceptance\routing_bgp_spec.rb
require 'spec_helper_acceptance'

describe '/routing/bgp' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS        
        mikrotik_bgp_instance_vrf { 'VIRTUAL1':
          instance => 'PUPPET',# Always required...
          ensure   => absent,
        }
        
        mikrotik_bgp_instance { 'PUPPET':
          ensure => absent,
        }
        
        mikrotik_bgp_peer { 'peer1':
          ensure => absent,
        }
  
        mikrotik_bgp_network { ['1.1.1.0/24', '1.1.2.0/24', '1.1.3.0/24']: 
          ensure => absent,
        }
          
        mikrotik_bgp_aggregate { ['1.1.0.0/16', '1.2.0.0/16', '1.3.0.0/16']:
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 5
  end  

  context "instance creation" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_instance { 'PUPPET':
          as                          => '64500',
          router_id                   => '1.2.3.4',
          redistribute_connected      => true,
          redistribute_static         => true,
          out_filter                  => 'PUPPET_OUT',
          client_to_client_reflection => true,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "instance update" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_instance { 'PUPPET':
          redistribute_connected      => false,
          redistribute_static         => false,
          out_filter                  => 'PUPPET_OUT1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
    
  context "create peer" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_peer { 'peer1':
          instance           => 'PUPPET',
          peer_address       => '1.2.3.6',
          peer_as            => '64500',
          source             => 'ether1',       
          out_filter         => 'PUPPET_PEER_OUT',
          in_filter          => 'PUPPET_PEER_IN',
          route_reflect      =>  true,
          default_originate  => 'always',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
    
  context "update peer 1" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_peer { 'peer1':
          source             => '1.2.3.4',   
          out_filter         => 'PUPPET_PEER_OUT2',
          in_filter          => 'PUPPET_PEER_IN2',
          route_reflect      =>  false,
          default_originate  => 'if-installed',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update peer 2" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_peer { 'peer1':
          nexthop_choice  => 'force-self',
          multihop        => true,
          route_reflect   => false,
          passive         => true,
          source          => 'ether1',            
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update peer 3" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_peer { 'peer1':
          nexthop_choice    => 'propagate',
          multihop          => false,
          route_reflect     => true,
          remove_private_as => true,
          as_override       => true,
          use_bfd           => true,
          address_families  => ['ip', 'l2vpn'],
          comment           => 'VPLS peer',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable peer" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_peer { 'peer1':
          ensure => disabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "create BGP aggregate" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_aggregate { '1.1.0.0/16': 
          instance         => 'PUPPET',
          summary_only     => true,
          attribute_filter => 'ATTRIBS1'
        }
          
        mikrotik_bgp_aggregate { '1.2.0.0/16': 
          ensure             => present,
          instance           => 'PUPPET',
          inherit_attributes => false,
          suppress_filter    => 'SUPRESS2',
        }
          
        mikrotik_bgp_aggregate { '1.3.0.0/16': 
          ensure           => disabled,
          instance         => 'PUPPET',
          include_igp      => true,
          advertise_filter => 'ADV3',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update BGP aggregate" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_aggregate { '1.1.0.0/16': 
          instance         => 'PUPPET',
          summary_only     => false,
          suppress_filter  => 'SUPRESS1',
        }
          
        mikrotik_bgp_aggregate { '1.2.0.0/16': 
          ensure             => disabled,
          instance           => 'PUPPET',
          inherit_attributes => true,
          suppress_filter    => 'SUPRESSNEW',
        }
          
        mikrotik_bgp_aggregate { '1.3.0.0/16': 
          ensure           => enabled,
          instance         => 'PUPPET',
          include_igp      => false,
          advertise_filter => 'ADVNEW',
          suppress_filter  => 'SUPRESS3',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "remove BGP aggregate" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_aggregate { '1.1.0.0/16': 
          ensure => absent,
        }
          
        mikrotik_bgp_aggregate { '1.2.0.0/16': 
          ensure => absent,
        }
          
        mikrotik_bgp_aggregate { '1.3.0.0/16': 
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "create BGP network" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_network { '1.1.1.0/24': 
          
        }
        
        mikrotik_bgp_network { '1.1.2.0/24': 
          ensure      => present,
          synchronize => false,
        }
        
        mikrotik_bgp_network { '1.1.3.0/24': 
          ensure => enabled,  
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update BGP network" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_network { '1.1.2.0/24': 
          synchronize => true,
        } 
        
        mikrotik_bgp_network { '1.1.3.0/24': 
          ensure => disabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "remove BGP network" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_network { '1.1.1.0/24': 
          ensure => absent,
        }
        
        mikrotik_bgp_network { '1.1.2.0/24': 
          ensure => absent,
        }
        
        mikrotik_bgp_network { '1.1.3.0/24': 
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
    
  context "create BGP instance VRF" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_instance_vrf { 'VIRTUAL1':
          instance               => 'PUPPET',# Always required...
          ensure                 => 'disabled',
          redistribute_connected => true,
          redistribute_static    => true,
        }
        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update BGP instance VRF" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_instance_vrf { 'VIRTUAL1':
          instance             => 'PUPPET',
          redistribute_static  => false,
          redistribute_bgp     => true,
          in_filter            => 'FILTER1',
        }        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "enable BGP instance VRF" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_bgp_instance_vrf { 'VIRTUAL1':
          instance => 'PUPPET',# Always required...
          ensure   => 'enabled',
        }        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end  
end


File: /spec\acceptance\routing_ospf_spec.rb
require 'spec_helper_acceptance'

describe '/routing/ospf' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ospf_interface { 'ether1':
          ensure => absent,        
        }
        
        mikrotik_ospf_network { '9.8.7.6/32':
          ensure => absent,        
        }
          
        mikrotik_ospf_area { 'BORDER3':
          ensure => absent,        
        }
    
        mikrotik_ospf_nmba_neighbor { '1.2.3.4':
          ensure => absent,
        }
        
        mikrotik_ospf_instance { 'PUPPET':
          ensure => absent,        
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 6
  end  

  context "instance creation" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospf_instance { 'PUPPET':
          ensure                 => disabled,
          router_id              => '9.8.7.6',
          distribute_default     => 'always-as-type-1',
          redistribute_connected => 'as-type-2',
          redistribute_static    => 'as-type-2',
          out_filter             => 'PUPPET_PEER_OUT',
          in_filter              => 'PUPPET_PEER_IN',
          metric_connected       => 100,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "instance update" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospf_instance { 'PUPPET':
          ensure                 => enabled,
          distribute_default     => 'if-installed-as-type-1',
          redistribute_connected => 'as-type-1',
          redistribute_static    => 'as-type-1',
          metric_connected       => 50,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
    
  context "area creation" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospf_area { 'BORDER3':
          area_id  => '0.0.1.63',
          instance => 'PUPPET',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "area update" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospf_area { 'BORDER3':
          area_id  => '0.0.0.63',
          instance => 'PUPPET',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "network creation" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospf_network { '9.8.7.6/32':
          area  => 'backbone',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "network update" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospf_network { '9.8.7.6/32':
          area  => 'BORDER3',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "interface creation" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospf_interface { 'ether1':
          cost     => 100,
          priority => 20,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "interface update" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospf_interface { 'ether1':
          cost     => 10,
          priority => 200,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "neighbor creation" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospf_nmba_neighbor { '1.2.3.4':
          instance => 'PUPPET',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "neighbor update" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospf_nmba_neighbor { '1.2.3.4':
          poll_interval => '5m',
          priority      => 100,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "neighbor disable" do
    it 'should update master' do
      site_pp = <<-EOS      
        mikrotik_ospf_nmba_neighbor { '1.2.3.4':
          ensure => disabled,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end  
end

describe '/routing/ospfv3' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_ospfv3_interface { 'ether1':
          ensure => absent,        
        }
                  
        mikrotik_ospfv3_area { 'BORDER3':
          ensure => absent,        
        }

        mikrotik_ospfv3_instance { 'PUPPET':
          ensure => absent,        
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  

  context "instance creation" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospfv3_instance { 'PUPPET':
          ensure                 => disabled,
          router_id              => '9.8.7.6',
          distribute_default     => 'always-as-type-1',
          redistribute_connected => 'as-type-2',
          redistribute_static    => 'as-type-2',
          metric_connected       => 100,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "instance update" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospfv3_instance { 'PUPPET':
          ensure                 => enabled,
          distribute_default     => 'if-installed-as-type-1',
          redistribute_connected => 'as-type-1',
          redistribute_static    => 'as-type-1',
          metric_connected       => 50,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
    
  context "area creation" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospfv3_area { 'BORDER3':
          area_id  => '0.0.1.63',
          instance => 'PUPPET',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "area update" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospfv3_area { 'BORDER3':
          area_id  => '0.0.0.63',
          instance => 'PUPPET',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "interface creation" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospfv3_interface { 'ether1':
          area     => 'BORDER3',
          cost     => 100,
          priority => 20,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "interface update" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospfv3_interface { 'ether1':
          area     => 'BORDER3',
          cost     => 10,
          priority => 200,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "interface disable" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_ospfv3_interface { 'ether1':
          ensure  => disabled,
          passive => true,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

File: /spec\acceptance\settings_spec.rb
require 'spec_helper_acceptance'

describe '/ip settings' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_ip_settings { 'ip':
          rp_filter => 'no',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
 
    it_behaves_like 'an idempotent device run after failures', 1
  end  

  context "rp-filter=loose" do
    it 'should update master' do
      site_pp = <<-EOS                
        mikrotik_ip_settings { 'ip':
          rp_filter => 'loose',
        }    
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "rp-filter=strict" do
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_ip_settings { 'ip':
          rp_filter => 'strict',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "with wrong title" do
    it 'should update master' do
      site_pp = <<-EOS               
        mikrotik_ip_settings { 'MyIP2':
          rp_filter => 'no',
        }        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'a faulty device run'
  end
end

describe '/ipv6 settings' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_ipv6_settings { 'ipv6':
          accept_redirects             => true,
          accept_router_advertisements => 'yes-if-forwarding-disabled',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
 
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  context "accept_redirects=false" do
    it 'should update master' do
      site_pp = <<-EOS                
        mikrotik_ipv6_settings { 'ipv6':
          accept_redirects => false,
        }    
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "accept_router_advertisements=no" do
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_ipv6_settings { 'ipv6':
          accept_router_advertisements => 'no',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "with wrong title" do
    it 'should update master' do
      site_pp = <<-EOS               
        mikrotik_ipv6_settings { 'MyIP6':
          accept_router_advertisements => 'no',
        }        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'a faulty device run'
  end
end

describe '/interface bridge settings' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_interface_bridge_settings { 'bridge':
          allow_fast_path           => true,
          use_ip_firewall           => false,
          use_ip_firewall_for_pppoe => false,
          use_ip_firewall_for_vlan  => false,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
 
    it_behaves_like 'an idempotent device run after failures', 1
  end  

  context "enable firewall for bridged PPPoE" do
    it 'should update master' do
      site_pp = <<-EOS                
        mikrotik_interface_bridge_settings { 'bridge':
          use_ip_firewall_for_pppoe => true,
        }    
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end # EXPECT FAILURE !!

  context "enable firewall for bridged VLAN" do
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_interface_bridge_settings { 'bridge':
          use_ip_firewall           => true,
          use_ip_firewall_for_pppoe => true,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "disable fastpath" do
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_interface_bridge_settings { 'bridge':
          allow_fast_path => false,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "with wrong title" do
    it 'should update master' do
      site_pp = <<-EOS               
        mikrotik_interface_bridge_settings { 'MyBridge2':
          allow_fast_path => true,
        }        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'a faulty device run'
  end
end


File: /spec\acceptance\snmp_spec.rb
require 'spec_helper_acceptance'

describe '/snmp' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_snmp { 'snmp':
          ensure          => disabled,
          contact         => "",
          location        => "",
          trap_version    => 1,
          trap_community  => "public",
          trap_generators => [],
          trap_targets    => [],
        }
        mikrotik_snmp_community { ['test_ro', 'test_rw']:
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 2
  end  
  
  context "snmp normal config" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_snmp { 'snmp':
          ensure   => enabled,
          contact  => "nicolas@rcswimax.com",
          location => "Juba",
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "snmp add community" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_snmp_community { 'test_ro':
          ensure     => present,
        }
        mikrotik_snmp_community { 'test_rw':
          ensure       => present,
          write_access => true,          
          addresses    => ['105.235.208.0/22'],  
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "snmp community - disable all permissions" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_snmp_community { 'test_ro':
          read_access  => false,
          write_access => false,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  

  context "snmp update community" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_snmp_community { 'test_ro':
          ensure => absent,
        }
        mikrotik_snmp_community { 'test_rw':
          addresses => ['172.16.0.0/22', '105.235.208.0/22'],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
    
  context "snmp trap config" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_snmp { 'snmp':
          trap_community  => "test_rw",
          trap_version    => 2,
          trap_generators => ["interfaces"],
          trap_targets    => ["105.235.209.12"],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "snmp clear community array" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_snmp_community { 'test_rw':
          addresses => [],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "snmp clear traps array" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_snmp { 'snmp':
          trap_generators => ["start-trap"],
          trap_targets    => [],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "snmp invalid trap community" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_snmp { 'snmp':
          trap_targets => ['newcommunity'],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'a faulty device run'
  end
    
#  context "with ensure absent" do
#    it 'should update master' do
#      site_pp = <<-EOS
#        mikrotik_snmp { 'snmp':
#          ensure => 'absent',
#        }
#      EOS
#      
#      set_site_pp_on_master(site_pp)
#    end
#  
#    it_behaves_like 'a faulty device run'
#  end
#
#  context "with wrong title" do
#    it 'should update master' do
#      site_pp = <<-EOS
#        mikrotik_snmp { 'test':
#          ensure => 'enabled',  
#        }
#      EOS
#      
#      set_site_pp_on_master(site_pp)
#    end
#  
#    it_behaves_like 'a faulty device run'
#  end
end


File: /spec\acceptance\system_spec.rb
require 'spec_helper_acceptance'

describe '/system' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_system { 'system':
          identity      => 'mikrotik',
          timezone      => 'Europe/Brussels',
          ntp_enabled   => false,
          ntp_primary   => '193.190.147.153',
          ntp_secondary => '195.200.224.66',
        }   
        
        mikrotik_script { 'script1': 
          ensure => absent,
        }
      
        mikrotik_schedule { 'daily_run_script1': 
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 3
  end  

  context "correct settings" do
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_system { 'system':
          identity      => 'chr_dude1',
          timezone      => 'Africa/Juba',
          ntp_enabled   => true,
          ntp_primary   => '193.190.253.212',
          ntp_secondary => '79.132.231.103',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
      
  context "with wrong title" do
    it 'should update master' do
      site_pp = <<-EOS       
        mikrotik_system { 'systemTEST':
          identity      => 'mikrotik',
          timezone      => 'Europe/Brussels',
          ntp_enabled   => false,
          ntp_primary   => '193.190.147.153',
          ntp_secondary => '195.200.224.66',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'a faulty device run'
  end

  context "script with schedule" do
    it 'should update master' do
      site_pp = <<-EOS    
        mikrotik_script { 'script1': 
          policies => ['read'],
          source   => '/log info message="Hello World!"',   
        }
      
        mikrotik_schedule { 'daily_run_script1': 
          ensure   => disabled,
          interval => '1h',
          policies => ['read'],
          on_event => 'script1',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update script and schedule" do
    it 'should update master' do
      site_pp = <<-EOS    
        mikrotik_script { 'script1': 
          policies => ['write'],
          source   => '/log info message="Hello World 2 !"',   
        }
      
        mikrotik_schedule { 'daily_run_script1': 
          ensure   => enabled,
          interval => '1d',
          policies => ['read', 'write'],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "disable schedule" do
    it 'should update master' do
      site_pp = <<-EOS    
        mikrotik_schedule { 'daily_run_script1': 
          ensure => disabled
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "enable schedule" do      
    it 'should update master' do
      site_pp = <<-EOS    
        mikrotik_schedule { 'daily_run_script1': 
          ensure => enabled
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end  
end


File: /spec\acceptance\tools_spec.rb
require 'spec_helper_acceptance'

describe '/tool/e-mail' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_tool_email { 'email':
          server       => '0.0.0.0',
          from_address => '<>',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  

  context "with valid settings" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_tool_email { 'email':
          server          => '105.235.209.19',
          from_address    => 'chr_dude1@rcswimax.com',
          enable_starttls => true,
          username        => 'test', 
          password        => 'test',          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "without STARTTLS" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_tool_email { 'email':
          enable_starttls => false,          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "with wrong title" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_tool_email { 'MyE-mail':
          server       => '127.0.0.1',
          from_address => 'jubanoc@rcswimax.com',
        }
      EOS

      set_site_pp_on_master(site_pp)
    end

    it_behaves_like 'a faulty device run'
  end
end

describe '/tool/netwatch' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_tool_netwatch { '8.8.4.4':
          ensure => 'absent'
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  

  context "create watches" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_tool_netwatch { '8.8.4.4':
          down_script => '/log info Host Down',
          up_script   => '/log info Host Up',
        }        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "update watches" do
      it 'should update master' do
        site_pp = <<-EOS
          mikrotik_tool_netwatch { '8.8.4.4':
            ensure   => disabled,
            interval => '5m',
            timeout  => '5s',
          }
        EOS
        
        set_site_pp_on_master(site_pp)
      end
    
      it_behaves_like 'an idempotent device run'
    end
    
  context "enable watches" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_tool_netwatch { '8.8.4.4':
          ensure   => enabled,
        }        
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end

File: /spec\acceptance\tool_graph_spec.rb
require 'spec_helper_acceptance'

describe '/tool/graphing' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_graph_interface { 'all':
          ensure => absent,
        }
        
        mikrotik_graph_resource { 'resource':
          ensure => absent,
        }
        
        mikrotik_graph_queue { 'all':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 3
  end  

  context "interface" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_graph_interface { 'all':
          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "resource" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_graph_resource { 'resource':
          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "queue" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_graph_queue { 'all':
          
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "filtering allowed" do
    it 'should update master' do
      site_pp = <<-EOS  
        mikrotik_graph_interface { 'all':
          allow => '83.101.0.0/16'
        }
        mikrotik_graph_resource { 'resource':
          allow => '83.101.0.0/16'
        }
        mikrotik_graph_queue { 'all':
          allow => '83.101.0.0/16'
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  # TODO - exist code = 0 ??? => Find other way to detect error...
#  context "with wrong title" do
#    it 'should update master' do
#      site_pp = <<-EOS
#        mikrotik_graph_resource { 'resources2':
#          allow => '83.101.0.0/16'
#        }
#      EOS
#
#      set_site_pp_on_master(site_pp)
#    end
#
#    it_behaves_like 'a faulty device run'
#  end
end


File: /spec\acceptance\upgrade_spec.rb
require 'spec_helper_acceptance'

describe '/system/upgrade' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  before(:each) do
    # Upgrade Source
    @upgrade_source = get_upgrade_source
  end 

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_upgrade_source { '#{@upgrade_source[:hostname]}':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 1
  end  
  
  # Package Source
  context "add package source" do            
    it 'should update master' do
      site_pp = <<-EOS                  
        mikrotik_upgrade_source { '#{@upgrade_source[:hostname]}':
          username => 'testuser',
          password => '#{@upgrade_source[:password]}',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update package source" do            
    it 'should update master' do
      site_pp = <<-EOS                      
        mikrotik_upgrade_source { '#{@upgrade_source[:hostname]}':
          username => '#{@upgrade_source[:username]}',
          password => 'unchanged',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  # Sanity Check
  context "wrong package" do      
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_upgrade { '8.0.1':
          ensure => downloaded,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'a faulty device run'
  end

  context "package present" do      
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_upgrade { '#{@upgrade_source[:version1]}':
          ensure => present,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an empty device run'
  end

  context "package absent" do      
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_upgrade { '8.0.1':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an empty device run'
  end

  context "package removal" do
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_upgrade { '#{@upgrade_source[:version1]}':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end

    it_behaves_like 'a faulty device run'
  end

  # Action: Download + Reboot
  context "install package and reboot" do      
    before { skip("Skipping this test for now") }
    
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_upgrade { '#{@upgrade_source[:version2]}':
          ensure       => installed,
          force_reboot => true
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "download installed package" do     
    before { skip("Skipping this test for now") }
     
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_upgrade { '#{@upgrade_source[:version2]}':
          ensure => downloaded,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an empty device run'
  end
  
  # Action: Download and forget forced reboot
  context "download package" do          
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_upgrade { '#{@upgrade_source[:version1]}':
          ensure => downloaded,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "install package without force" do      
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_upgrade { '#{@upgrade_source[:version1]}':
          ensure => installed,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'a changing device run'
  end
  
  # Package Source Cleanup
  context "remove package source" do
    it 'should update master' do
      site_pp = <<-EOS            
        mikrotik_upgrade_source { '#{@upgrade_source[:hostname]}':
          ensure => absent,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end  
end


File: /spec\acceptance\user_spec.rb
require 'spec_helper_acceptance'

describe '/user' do
  before { skip("Skipping this test for now") }
  
  include_context 'testnodes defined'

  context "reset configuration" do      
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_user_aaa { 'aaa':
          use_radius     => false,
          accounting     => false,
          interim_update => '1m',
          default_group  => 'read',
          exclude_groups => []
        }
        
        mikrotik_user { 'testuser1':
          ensure => absent,
        }
        
        mikrotik_user_group { ['admin1', 'admin2']:
          ensure => absent,
        }
             
        # TODO
        # mikrotik_user_sshkey { 'testuser1':
        #   ensure => absent,
        # }      
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run after failures', 3
  end  
  
  context "create user groups" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_user_group { 'admin1':
          # Defaults
        }
             
        mikrotik_user_group { 'admin2':
          policy => ['read', 'ssh', 'winbox']
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
  
  context "correct aaa settings" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_user_aaa { 'aaa':
          use_radius     => true,
          accounting     => true,
          interim_update => '5m',
          default_group  => 'write',
          exclude_groups => ['admin1', 'admin2']
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "disable aaa" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_user_aaa { 'aaa':
          use_radius => false,
          accounting => false,
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
    
  context "with wrong title" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_user_aaa { 'myAAA2':
          use_radius     => true,
          interim_update => '10m',
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'a faulty device run'
  end
  
  context "create user" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_user { 'testuser1':
          ensure    => disabled,
          password  => 'password',
          group     => 'admin1',
          addresses => ['192.168.0.0/24'],
        }

      # TODO
#        mikrotik_user_sshkey { 'testuser1':
#          public_key => 'TODO',
#        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "update user" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_user { 'testuser1':
          ensure    => enabled,
          password  => 'password2',
          group     => 'admin2',
          addresses => ['192.168.0.0/24', '192.168.1.0/24'],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end

  context "disable user" do
    it 'should update master' do
      site_pp = <<-EOS
        mikrotik_user { 'testuser1':
          ensure    => 'disabled',
          addresses => ['192.168.1.0/24'],
        }
      EOS
      
      set_site_pp_on_master(site_pp)
    end
  
    it_behaves_like 'an idempotent device run'
  end
end


File: /spec\fixtures\.gitignore
/testnodes.yaml
/upgrade_source.yaml


File: /spec\fixtures\testnodes.example.yaml
---
# COPY THIS FILE TO testnodes.yaml and adjust according to your own test infra (Mikrotik Routers).
testnodes:
  # Phyiscal Router
  'HOSTNAME1':
    name: 'HOSTNAME1'
    ip: 'IP1'
    username: 'admin'
    password: 'PASSWORD1'
  # Mikrotik CHR
  # cd vagrant; vagrant up
  'vagrant_node':
    name: 'vagrant_node'
    ip: '192.168.1.1'   # Your Computer LAN IP ! (ifconfig)
    username: 'vagrant'
    password: 'vagrant'
  

File: /spec\fixtures\upgrade_source.example.yaml
---
# COPY THIS FILE TO upgrade_source.yaml and adjust according to your own test infra (Mikrotik Routers).
# The router should contain 2 x86 packages (routeros-x86-V.npk)
hostname: 'IP1'
username: 'admin'
password: 'PASSWORD1'
version1: '6.40.8'
version2: '6.42.7'

File: /spec\spec_helper_acceptance.rb
require 'puppet'

require 'beaker-rspec'
require 'beaker-rspec/spec_helper'
require 'beaker-rspec/helpers/serverspec'

require 'beaker-puppet'

require 'beaker'
require 'beaker/puppet_install_helper'

require 'support/changing_device_run'
require 'support/empty_device_run'
require 'support/faulty_device_run'
require 'support/idempotent_device_run'
require 'support/idempotent_device_run_after_failures'
require 'support/idempotent_manifest'
require 'support/testnodes'

RSpec.configure do |c|
  c.before :suite do
    # Test Nodes
    @testnodes = get_testnodes
    
    proj_root = File.expand_path(File.join(File.dirname(__FILE__), '..'))
      
    # Install the correct Puppet version
    #run_puppet_install_helper("agent", "5.5.10")
    run_puppet_install_helper("agent", "6.13.0")
      
    # Generic for every host    
    hosts.each do |host|
      # Install this module
      install_dev_puppet_module_on(host, :source => proj_root, :module_name => 'mikrotik', :target_module_path => '/etc/puppetlabs/code/environments/production/modules')
    end

    # On master
    unless ENV['BEAKER_provision'] == 'no'
      on master, 'apt-key adv --keyserver keyserver.ubuntu.com --recv-keys --recv-keys 7F438280EF8D349F'
      on master, 'apt-get update'
      on master, 'apt-get install -y puppetserver'
      on master, 'cp /etc/default/puppetserver /tmp/puppetserver'
      on master, 'sed -e "s/2g/1g/g" /tmp/puppetserver > /etc/default/puppetserver'
      
      autosign_conf = ""
      # TODO ? agents.each { |agent| autosign_conf << "#{agent[:name]}\n" }
      autosign_file = '/etc/puppetlabs/puppet/autosign.conf'
      @testnodes.each { |node| autosign_conf << "#{node[:name]}\n" }
      
      create_remote_file(master, autosign_file, autosign_conf)
      on master, "chown puppet #{autosign_file}"
      
      on master, 'service puppetserver start'  
        
      # TODO: The strangest BUGFIX for Puppetserver 6.15.1
      on master, 'mkdir -p /opt/puppetlabs/server/data/puppetserver/yaml/facts'
      on master, 'chown -R puppet:puppet /opt/puppetlabs/server/data/puppetserver/yaml'
        
      # TODO ? # Pluginsync requires 1 run on master?
      # TODO ? site_pp = '/etc/puppetlabs/code/environments/production/manifests/site.pp'
      # TODO ? create_remote_file(master, site_pp, 'node default {}')
      # TODO ? on master, "chown puppet #{site_pp}"
      # TODO ? on master, "puppet agent -t"
  
      # First time, install mtik gem on all hosts
      hosts.each do |host|
        # on host, '/opt/puppetlabs/puppet/bin/gem install mtik'
        apply_manifest_on(host, "include ::mikrotik")
      end
    end
  
    # Agents
    agents.each do |agent|      
      # TODO ? # Pluginsync requires 1 run on agent?
      # TODO ? on master, "puppet agent -t"
        
      # Set device.conf
      device_conf = ""
      @testnodes.each { |node| device_conf << "[#{node[:name]}]\n  type mikrotik\n  url api://#{node[:username]}:#{node[:password]}@#{node[:ip]}\n" }

      create_remote_file(agent, '/etc/puppetlabs/puppet/device.conf', device_conf)
    end
  end
end

def run_puppet_device_on(devices) 
  if ENV['BEAKER_debug']
    debug="--debug"
  else
    debug="--verbose"
  end
  
  devices.each do |device| 
    @result = on(device, "/opt/puppetlabs/puppet/bin/puppet device --detailed-exitcodes #{debug}", :accept_all_exit_codes => true)
  end
  
  @result
end

def apply_manifests(devices, manifest) 
  devices.each do |device| 
    @result = apply_manifest_on(device, manifest, :accept_all_exit_codes => true)
  end
  
  @result
end  

def set_site_pp_on_master(nodes_config)
  site_pp = '/etc/puppetlabs/code/environments/production/manifests/site.pp'
  
  create_remote_file(master, site_pp, create_site_pp(nodes_config))
  on master, "chown puppet #{site_pp}"
end

def create_site_pp(site_pp)
  result = ""
  @testnodes.each { |node| result << "node default {\n\n}\n\nnode '#{node[:name]}' {\n#{site_pp}\n}\n" }
  
  result
end

def get_testnodes
  yaml = YAML.load_file("spec/fixtures/testnodes.yaml")
  nodes = yaml["testnodes"].values.collect { |node|
    {
      :name     => node["name"],
      :ip       => node["ip"],
      :username => node["username"],
      :password => node["password"],    
    }
  }
  nodes
end

def get_upgrade_source
  yaml = YAML.load_file("spec/fixtures/upgrade_source.yaml")

  {
    :hostname => yaml["hostname"],
    :username => yaml["username"],
    :password => yaml["password"],
    :version1 => yaml["version1"],
    :version2 => yaml["version2"],
  }
end


File: /spec\support\changing_device_run.rb
shared_examples 'a changing device run' do  
  it 'should make changes the first time' do
    @result = run_puppet_device_on(agents)
    expect(@result.exit_code).to eq(2)
  end

  it 'should make changes on the second run' do
    @result = run_puppet_device_on(agents)
    expect(@result.exit_code).to eq(2)    
  end
end


File: /spec\support\empty_device_run.rb
shared_examples 'an empty device run' do  
  it 'should not make changes the first time' do
    @result = run_puppet_device_on(agents)
    expect(@result.exit_code).to eq(0)
  end
end


File: /spec\support\faulty_device_run.rb
shared_examples 'a faulty device run' do  
  it 'should raise an error' do
    @result = run_puppet_device_on(agents)
    expect([1, 6]).to include(@result.exit_code)
  end
end


File: /spec\support\idempotent_device_run.rb
shared_examples 'an idempotent device run' do  
  it 'should make changes the first time' do
    @result = run_puppet_device_on(agents)
    expect(@result.exit_code).to eq(2)
  end

  it 'should be idempotent on the second run' do
    @result = run_puppet_device_on(agents)
    expect(@result.exit_code).to eq(0)    
  end
end


File: /spec\support\idempotent_device_run_after_failures.rb
shared_examples 'an idempotent device run after failures' do |allowed_fail_runs|   
  it "can fail for new resources" do 
    allowed_fail_runs.times do |run|
      @result = run_puppet_device_on(agents)      
      expect([0, 1, 2]).to include(@result.exit_code)
  
      break unless @result.exit_code == 1
    end
  end

  # Only run if loop was not broken...
  it 'can make changes on the second run' do
    @result = run_puppet_device_on(agents)
    expect([0, 2]).to include(@result.exit_code)
  end

  it 'should be idempotent on the third run' do
    @result = run_puppet_device_on(agents)
    expect(@result.exit_code).to eq(0)    
  end
end


File: /spec\support\idempotent_manifest.rb
shared_examples 'an idempotent manifest' do  
  it 'should make changes the first time' do
    @result = apply_manifests(agents, @pp)
    expect(@result.exit_code).to eq(2)
  end

  it 'be idempotent on the second run' do
    @result = apply_manifests(agents, @pp)
    expect(@result.exit_code).to eq(0)    
  end
end


File: /spec\support\testnodes.rb
shared_examples 'testnodes defined' do
  before(:all) do
    # Test Nodes
    @testnodes = get_testnodes
  end 
end


File: /vagrant\.gitignore
/.vagrant/


File: /vagrant\Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "dulin/mikrotik"

  config.ssh.username = "vagrant"
  config.ssh.password = "vagrant"

  config.ssh.keys_only = false
  config.ssh.insert_key = false

  config.vm.box_check_update = false
  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.network "forwarded_port", guest: 8728, host: 8728
  config.vm.network "forwarded_port", guest: 8291, host: 8291

  if Vagrant.has_plugin?("vagrant-vbguest")
    config.vbguest.auto_update = false
  end
end


