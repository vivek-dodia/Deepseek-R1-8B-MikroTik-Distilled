# Repository Information
Name: terraform-provider-mikrotik

# Directory Structure
Directory structure:
└── github_repos/terraform-provider-mikrotik/
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
    │   │       ├── pack-aa34acbd4e9b6d67363a48e54c163ea6f1cf4c98.idx
    │   │       └── pack-aa34acbd4e9b6d67363a48e54c163ea6f1cf4c98.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── .github/
    │   ├── dependabot.yml
    │   ├── release.yml
    │   └── workflows/
    │       ├── continuous-integration.yml
    │       ├── release.yml
    │       └── tfplugindocs.yml
    ├── .gitignore
    ├── .goreleaser.yml
    ├── .travis.yml
    ├── bin/
    │   └── wait-for-routeros.sh
    ├── client/
    │   ├── bgp_instance.go
    │   ├── bgp_instance_test.go
    │   ├── bgp_peer.go
    │   ├── bgp_peer_test.go
    │   ├── bridge.go
    │   ├── bridge_port.go
    │   ├── bridge_port_test.go
    │   ├── bridge_test.go
    │   ├── bridge_vlan.go
    │   ├── bridge_vlan_test.go
    │   ├── client.go
    │   ├── client_crud.go
    │   ├── client_test.go
    │   ├── console-inspected/
    │   │   ├── parse.go
    │   │   ├── parse_test.go
    │   │   ├── split_strategy.go
    │   │   └── types.go
    │   ├── console_inspect.go
    │   ├── dhcp_server.go
    │   ├── dhcp_server_network.go
    │   ├── dhcp_server_network_test.go
    │   ├── dhcp_server_test.go
    │   ├── dns.go
    │   ├── dns_test.go
    │   ├── errors.go
    │   ├── errors_test.go
    │   ├── firewall_filter.go
    │   ├── firewall_filter_test.go
    │   ├── go.mod
    │   ├── go.sum
    │   ├── helpers.go
    │   ├── interface_list.go
    │   ├── interface_list_member.go
    │   ├── interface_list_member_test.go
    │   ├── interface_list_test.go
    │   ├── interface_wireguard.go
    │   ├── interface_wireguard_peer.go
    │   ├── interface_wireguard_peer_test.go
    │   ├── interface_wireguard_test.go
    │   ├── ipv6_addr.go
    │   ├── ipv6_addr_test.go
    │   ├── ip_addr.go
    │   ├── ip_addr_test.go
    │   ├── lease.go
    │   ├── lease_test.go
    │   ├── pool.go
    │   ├── pool_test.go
    │   ├── resource_wrappers.go
    │   ├── scheduler.go
    │   ├── scheduler_test.go
    │   ├── script.go
    │   ├── script_test.go
    │   ├── setup.go
    │   ├── setup_test.go
    │   ├── system_resources.go
    │   ├── system_resources_test.go
    │   ├── types/
    │   │   ├── duration.go
    │   │   ├── duration_test.go
    │   │   ├── list.go
    │   │   └── list_test.go
    │   ├── vlan_interface.go
    │   ├── vlan_interface_test.go
    │   ├── wireless_interface.go
    │   ├── wireless_interface_test.go
    │   ├── wireless_security_profile.go
    │   └── wireless_security_profile_test.go
    ├── cmd/
    │   └── mikrotik-codegen/
    │       ├── internal/
    │       │   ├── codegen/
    │       │   │   ├── formatter.go
    │       │   │   ├── generator_mikrotik.go
    │       │   │   ├── generator_terraform.go
    │       │   │   ├── parser.go
    │       │   │   ├── parser_test.go
    │       │   │   ├── README.md
    │       │   │   ├── templates.go
    │       │   │   ├── types.go
    │       │   │   └── types_test.go
    │       │   └── utils/
    │       │       ├── utils.go
    │       │       └── utils_test.go
    │       └── main.go
    ├── docker/
    │   └── docker-compose.yml
    ├── docs/
    │   ├── index.md
    │   └── resources/
    │       ├── bgp_instance.md
    │       ├── bgp_peer.md
    │       ├── bridge.md
    │       ├── bridge_port.md
    │       ├── bridge_vlan.md
    │       ├── dhcp_lease.md
    │       ├── dhcp_server.md
    │       ├── dhcp_server_network.md
    │       ├── dns_record.md
    │       ├── firewall_filter_rule.md
    │       ├── interface_list.md
    │       ├── interface_list_member.md
    │       ├── interface_wireguard.md
    │       ├── interface_wireguard_peer.md
    │       ├── ipv6_address.md
    │       ├── ip_address.md
    │       ├── pool.md
    │       ├── scheduler.md
    │       ├── script.md
    │       ├── vlan_interface.md
    │       └── wireless_interface.md
    ├── examples/
    │   ├── provider/
    │   │   └── provider.tf
    │   └── resources/
    │       ├── mikrotik_bgp_instance/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_bgp_peer/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_bridge/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_bridge_port/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_bridge_vlan/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_dhcp_lease/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_dhcp_server/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_dhcp_server_network/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_dns_record/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_firewall_filter_rule/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_interface_list/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_interface_list_member/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_interface_wireguard/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_interface_wireguard_peer/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_ipv6_address/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_ip_address/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_pool/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_scheduler/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       ├── mikrotik_script/
    │       │   ├── import.sh
    │       │   └── resource.tf
    │       └── mikrotik_vlan_interface/
    │           ├── import.sh
    │           └── resource.tf
    ├── go.mod
    ├── go.sum
    ├── go.work
    ├── go.work.sum
    ├── LICENSE
    ├── main.go
    ├── Makefile
    ├── mikrotik/
    │   ├── acc_setup_test.go
    │   ├── internal/
    │   │   ├── test_helpers.go
    │   │   ├── types/
    │   │   │   └── defaultaware/
    │   │   │       ├── bool.go
    │   │   │       ├── bool_test.go
    │   │   │       ├── int64.go
    │   │   │       ├── int64_test.go
    │   │   │       ├── resource_wrapper.go
    │   │   │       ├── resource_wrapper_test.go
    │   │   │       ├── string.go
    │   │   │       └── string_test.go
    │   │   └── utils/
    │   │       ├── provider.go
    │   │       ├── provider_test.go
    │   │       ├── string.go
    │   │       ├── struct_copy.go
    │   │       └── struct_copy_test.go
    │   ├── provider.go
    │   ├── provider_framework.go
    │   ├── provider_test.go
    │   ├── resource_bgp_instance.go
    │   ├── resource_bgp_instance_test.go
    │   ├── resource_bgp_peer.go
    │   ├── resource_bgp_peer_test.go
    │   ├── resource_bridge.go
    │   ├── resource_bridge_port.go
    │   ├── resource_bridge_port_test.go
    │   ├── resource_bridge_test.go
    │   ├── resource_bridge_vlan.go
    │   ├── resource_bridge_vlan_test.go
    │   ├── resource_dhcp_lease.go
    │   ├── resource_dhcp_lease_test.go
    │   ├── resource_dhcp_server.go
    │   ├── resource_dhcp_server_network.go
    │   ├── resource_dhcp_server_network_test.go
    │   ├── resource_dhcp_server_test.go
    │   ├── resource_dns_record.go
    │   ├── resource_dns_record_test.go
    │   ├── resource_firewall_filter.go
    │   ├── resource_firewall_filter_rule_test.go
    │   ├── resource_generic_crud_operations.go
    │   ├── resource_interface_list.go
    │   ├── resource_interface_list_member.go
    │   ├── resource_interface_list_member_test.go
    │   ├── resource_interface_list_test.go
    │   ├── resource_interface_wireguard.go
    │   ├── resource_interface_wireguard_peer.go
    │   ├── resource_interface_wireguard_peer_test.go
    │   ├── resource_interface_wireguard_test.go
    │   ├── resource_ipv6_address.go
    │   ├── resource_ipv6_address_test.go
    │   ├── resource_ip_address.go
    │   ├── resource_ip_address_test.go
    │   ├── resource_pool.go
    │   ├── resource_pool_test.go
    │   ├── resource_scheduler.go
    │   ├── resource_scheduler_test.go
    │   ├── resource_script.go
    │   ├── resource_script_test.go
    │   ├── resource_vlan_interface.go
    │   ├── resource_vlan_interface_test.go
    │   ├── resource_wireless_interface.go
    │   └── resource_wireless_interface_test.go
    ├── README.md
    ├── templates/
    │   ├── index.md.tmpl
    │   ├── resources/
    │   │   ├── bgp_instance.md.tmpl
    │   │   └── bgp_peer.md.tmpl
    │   └── resources.md.tmpl
    └── tools/
        └── tools.go


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
	url = https://github.com/ddelnano/terraform-provider-mikrotik.git
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
0000000000000000000000000000000000000000 5bc3b68c62458e2b1ddb5f4df8eed29783f31cf8 vivek-dodia <vivek.dodia@icloud.com> 1738605802 -0500	clone: from https://github.com/ddelnano/terraform-provider-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 5bc3b68c62458e2b1ddb5f4df8eed29783f31cf8 vivek-dodia <vivek.dodia@icloud.com> 1738605802 -0500	clone: from https://github.com/ddelnano/terraform-provider-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 5bc3b68c62458e2b1ddb5f4df8eed29783f31cf8 vivek-dodia <vivek.dodia@icloud.com> 1738605802 -0500	clone: from https://github.com/ddelnano/terraform-provider-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
6e361b9bb3767c9b718448ab78cdb1990b3b96dc refs/remotes/origin/add-dependandabot-for-security-and-dep-upgrades
646f3585cda3f3521fe77c3c692aad6e95aac12b refs/remotes/origin/add-support-for-ipv6_address-resource
045b1283ec78bf1be88ffa9c6dad875e1b531ab5 refs/remotes/origin/add-travis-ci-build
c10b6e6a7b0c61981261260ee8a98711bce1d464 refs/remotes/origin/add-txt-dns-records
e964a5a2c25e26fc0f67f76c01b2f2d15f3de791 refs/remotes/origin/auto-generate-mikrotik-resources
1d740c6806b03f19814cfb982e943e50593fa8cb refs/remotes/origin/dawoud/interface_peer
f9feb1d1bd49cbad9c3cf1e7ac8f80c257094e56 refs/remotes/origin/ddelnano/add-tfplugindocs-linting
6819a92ea6abefa5ec72eb0af54d5451daa4b158 refs/remotes/origin/ddelnano/add-wireguard-resource
06a0aaaa1fd25a019cacf4dd67be4ef81372236f refs/remotes/origin/ddelnano/update-github-releases-to-publish-automatically
8992d1f0ac37b99d4aaab993d5ca22e7c7dc0474 refs/remotes/origin/dependabot/go_modules/golang.org/x/crypto-0.31.0
23f916b69493c94a4c075896960c982560697686 refs/remotes/origin/improve-dhcp-lease-documention
ad75c29a2d7b31d24f319f24c06c78fb26f7d3bc refs/remotes/origin/interface_wireguard_peer
3c27bc0c6a467a08b32834103df37dcf1203a385 refs/remotes/origin/interface_wireguard_peer_jdelnano
bbeadf640715cadbfd8dbfa0e6d1799d41506e74 refs/remotes/origin/interface_wireguard_peer_jdelnano_refactor
1b79a6044a7c7183eaae44d42ea15d7591178758 refs/remotes/origin/jdelnano/correct-command-building
343df0c4c41a27d1083d706f60b4b692a5bfe93c refs/remotes/origin/jdelnano/dawoud/interface-wireguard
852effa502e419f47166f961709414625f6890f4 refs/remotes/origin/jdelnano/enhance-marshaling-related-to-struct-tags
c3dd00c48142e744b5bb241fb73cc75ca9df7f03 refs/remotes/origin/jdelnano/enhance-marshaling-related-to-struct-tags-break-tests
581fc013698b62df25c0a5d79463486971ddae85 refs/remotes/origin/jdelnano/interface_peer
3a7135f145850d0ef6bf09d8beb22b20211a7749 refs/remotes/origin/jdelnano/interface_peer_update_testacc_troubleshooting
5bc3b68c62458e2b1ddb5f4df8eed29783f31cf8 refs/remotes/origin/master
d2d1287bdd751a2fff07aa8ed81c61ad92dced38 refs/remotes/origin/upgrade-terraform-sdk
5570b556039aca7e3128b9d27d5145fef61caa79 refs/remotes/origin/use-github-native-goreleaser-changelog-generation
701df57f5bccc9759074a2442cb3ca005e35b1c6 refs/tags/0.1
671934c121c105e612bf2439559f283bab9c7c08 refs/tags/0.2.0
925d42f885b9aaa485cc5aa8c8787e47650eba6a refs/tags/0.2.1
e0cf6167a180304c3268c6451a2ba11f9ba7f56f refs/tags/0.2.1-test
a217572b326c3968f22b606958c1fd26fe8518f8 refs/tags/0.2.2
f728ff283a72b140c8bbc09993d6443dd09bbe7c refs/tags/0.3.0
c6346e5f598d9182bf48e69e32220a8d25530fc5 refs/tags/0.3.1
fc9431232d1d5f69131755a192727c0069390330 refs/tags/0.3.2
697022dc7d78040bf30593dec1100f34ae79c865 refs/tags/testing
^4d32433f05cd367768bf8416bfaed96f8b9c18f3
d5af553cfaab9a13169e78128e88226c504df196 refs/tags/testing2
^165ef1a47c79a78f83aed045d754e154fab2d453
006ea157d77bb7d1fd3678a7f9b9321ea8517b33 refs/tags/v0.10.0
38afe58c99861b2e3958e900523a26369e114228 refs/tags/v0.11.0
de902dce582e95b05b0421935410b7be31fe526f refs/tags/v0.12.0
837b111d12752094574a1938827c105e1e006a92 refs/tags/v0.13.0
8bc1906fb466e6ccb4cabba451ff3cc07905a818 refs/tags/v0.14.0
1884f408c1f240ffeebfe3aff8e882cb748f1c1c refs/tags/v0.15.0
bcaea5c65b3595a30943f24738dc67913bcfd6a7 refs/tags/v0.16.0
33fb6288057592adc9ab02da8fbbd3455c7badab refs/tags/v0.16.1
5857a10a1136c128076778597aa2d2ca9e1cdc25 refs/tags/v0.3.2
84349704261e390b03d8d62df7b32c1df97af2a0 refs/tags/v0.3.2-pre
84349704261e390b03d8d62df7b32c1df97af2a0 refs/tags/v0.3.3
776c5939dec81b92333d5db3679efaecdce2d1dc refs/tags/v0.3.4
4d58db30d82b6520bc574e3d1f00e1a341202771 refs/tags/v0.3.5
e3c4feb643ac0ca532a8d6387006bdbb8034b211 refs/tags/v0.3.6
1e81eab7f966b71279d7b129d7424c6524accb79 refs/tags/v0.4.0
4ee3f3f4bee7c33c64b8fa580c8e9c1b050d0a13 refs/tags/v0.4.1
b1206467a9736dbeb90dcc0b6a2963ab7c9a55f8 refs/tags/v0.5.0
f55cf5ddfca0288c1699791ee18cf0940b148b1a refs/tags/v0.5.1
^8e786058dd6584e317aa923e7276a096164b26c6
f74d8c7ac426566182f6c56acd5bb7bb9c9c3662 refs/tags/v0.6.0
f74d8c7ac426566182f6c56acd5bb7bb9c9c3662 refs/tags/v0.6.0-rc1
7f652169b2c408429f6cc61b04174ba44cbe380f refs/tags/v0.6.1
4ef51ac553643218a092ce9b7618af91293adc9d refs/tags/v0.6.2
^e40ebe8913dedec5fe0ffa199efcc590bbca8f31
d9648a2829c4c7264195607bffbfcd2afaf94464 refs/tags/v0.7.0
33813f29662fdb19d6a5131f8d4e528a0d6dc9b5 refs/tags/v0.8.0
^52918b8cd379db0b7da1c7820c92e65a1b24a9ed
a879b45b30fc795536f940a0d5002be7b2d52a2b refs/tags/v0.8.1
86b8317f19e15a7572a6e92d268cb21577e75684 refs/tags/v0.8.1-test
259b84a8b8ce4938c9ad8f0b024f4ecd08c84cc5 refs/tags/v0.8.1-test2
3fd9e3cb883a218c38bfaf9288f7c7d89044afd7 refs/tags/v0.9.0
^c2a1c2c1e254957f8fb92e328214be2212ee7088
66efed6cfa4b4f6c4c26577a0facc0c934bc3549 refs/tags/v0.9.1


File: /.git\refs\heads\master
5bc3b68c62458e2b1ddb5f4df8eed29783f31cf8


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
# do not expand these files by default in diff viewer
go.sum linguist-generated


File: /.github\dependabot.yml
---
version: 2
updates:
  open-pull-requests-limit: 0
- package-ecosystem: "gomod"
  directory: "/"
  schedule:
    interval: "daily"
  open-pull-requests-limit: 0
- package-ecosystem: github-actions
  directory: /
  schedule:
    interval: daily
  open-pull-requests-limit: 0


File: /.github\release.yml
changelog:
  categories:
    - title: Breaking Changes 🛠
      labels:
        - breaking-change
    - title: New Features 🎉
      labels:
        - enhancement
    - title: Bug fixes
      labels:
        - bug
    - title: Other Changes
      labels:
        - "*"


File: /.github\workflows\continuous-integration.yml
name: Continuous Integration
on:
  push:
    branches:
      - master
  pull_request:
    branches:
      - master
jobs:
  build:
    name: Build
    runs-on: ${{ matrix.os }}
    continue-on-error: ${{ matrix.experimental }}
    strategy:
      matrix:
        experimental: [false]
        go: ["1.18"]
        os: [ubuntu-latest]
        # Test against latest stable 6.x and 7.x and "latest" stable
        routeros: ["6.49.15", "7.14.3"]
        include:
          - experimental: true
            go: 1.18
            os: ubuntu-latest
            routeros: "latest"

    steps:
      - name: Set up Go
        uses: actions/setup-go@v4
        with:
          go-version: ${{ matrix.go }}
        id: go

      - name: Check out code into the Go module directory
        uses: actions/checkout@v3

      - name: Get dependencies
        run: go mod download

      - name: Build
        run: go build -v .

      - name: Run linters
        run: make lint

      - name: Wait until RouterOS container is ready
        run: ./bin/wait-for-routeros.sh 127.0.0.1 8080

      - name: Run provider tests
        run: make testacc
        env:
          MIKROTIK_HOST: 127.0.0.1:8728
          MIKROTIK_USER: admin
          MIKROTIK_PASSWORD: ''
          TF_ACC: 1

      - name: Run client tests
        run: make testclient
        env:
          MIKROTIK_HOST: 127.0.0.1:8728
          MIKROTIK_USER: admin
          MIKROTIK_PASSWORD: ''
          TF_ACC: 1

    services:
      routeros:
        image: mnazarenko/docker-routeros:${{ matrix.routeros }}
        ports:
          - 8728:8728
          - 8080:80
        options: >-
          --cap-add=NET_ADMIN
          --device=/dev/net/tun


File: /.github\workflows\release.yml
# This GitHub action can publish assets for release when a tag is created.
# Currently its setup to run on any tag that matches the pattern "v*" (ie. v0.1.0).
#
# This uses an action (paultyng/ghaction-import-gpg) that assumes you set your
# private key in the `GPG_PRIVATE_KEY` secret and passphrase in the `PASSPHRASE`
# secret. If you would rather own your own GPG handling, please fork this action
# or use an alternative one for key handling.
#
# You will need to pass the `--batch` flag to `gpg` in your signing step
# in `goreleaser` to indicate this is being used in a non-interactive mode.
#
name: release
on:
  push:
    tags:
      - 'v*'
jobs:
  goreleaser:
    runs-on: ubuntu-latest
    steps:
      -
        name: Checkout
        uses: actions/checkout@v3
      -
        name: Unshallow
        run: git fetch --prune --unshallow
      -
        name: Set up Go
        uses: actions/setup-go@v4
        with:
          go-version: 1.18
      -
        name: Import GPG key
        id: import_gpg
        # TODO: move this to HashiCorp namespace or find alternative that is just simple gpg commands
        # see https://github.com/hashicorp/terraform-provider-scaffolding/issues/22
        uses: paultyng/ghaction-import-gpg@v2.1.0
        env:
          # These secrets will need to be configured for the repository:
          GPG_PRIVATE_KEY: ${{ secrets.GPG_PRIVATE_KEY }}
          PASSPHRASE: ${{ secrets.PASSPHRASE }}
      -
        name: Run GoReleaser
        uses: goreleaser/goreleaser-action@v5
        with:
          version: latest
          args: release --rm-dist
        env:
          GPG_FINGERPRINT: ${{ steps.import_gpg.outputs.fingerprint }}
          # GitHub sets this automatically
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}


File: /.github\workflows\tfplugindocs.yml
---
name: 'tfplugindocs'
on:
  pull_request:
permissions:
  contents: read
jobs:
  tfplugindocs:
    permissions:
      contents: read
      pull-requests: read
    runs-on: ubuntu-latest
    steps:
      - name: Set up Go
        uses: actions/setup-go@v4
        with:
          go-version: 1.18
      - name: Check out code into the Go module directory
        uses: actions/checkout@v3
      - name: Get dependencies
        run: go mod download
      - name: Run tfplugindocs
        run: go generate ./...
      - name: Fail if any files changed
        shell: bash
        run: |
          if [[ $(git status --porcelain=v1 docs/ | wc -l) -ne 0 ]]; then
            echo "Please ensure tfplugindocs changes are committed to docs/"
            echo "Changed files:"
            git diff --name-only docs/
            git status docs/
            exit 1
          fi


File: /.gitignore
terraform-provider-mikrotik
dist/
vendor
File: /.goreleaser.yml
# Visit https://goreleaser.com for documentation on how to customize this
# behavior.
before:
  hooks:
    # this is just an example and not a requirement for provider building/publishing
    - go mod tidy
builds:
- env:
    # goreleaser does not work with CGO, it could also complicate
    # usage by users in CI/CD systems like Terraform Cloud where
    # they are unable to install libraries.
    - CGO_ENABLED=0
  mod_timestamp: '{{ .CommitTimestamp }}'
  flags:
    - -trimpath
  ldflags:
    - '-s -w -X main.version={{.Version}} -X main.commit={{.Commit}}'
  goos:
    - freebsd
    - windows
    - linux
    - darwin
  goarch:
    - amd64
    - '386'
    - arm
    - arm64
  ignore:
    - goos: darwin
      goarch: '386'
  binary: '{{ .ProjectName }}_v{{ .Version }}'
archives:
- format: zip
  name_template: '{{ .ProjectName }}_{{ .Version }}_{{ .Os }}_{{ .Arch }}'
checksum:
  name_template: '{{ .ProjectName }}_{{ .Version }}_SHA256SUMS'
  algorithm: sha256
signs:
  - artifacts: checksum
    args:
      # if you are using this is a GitHub action or some other automated pipeline, you 
      # need to pass the batch flag to indicate its not interactive.
      - "--batch"
      - "--local-user"
      - "{{ .Env.GPG_FINGERPRINT }}" # set this environment variable for your signing key
      - "--output"
      - "${signature}"
      - "--detach-sign"
      - "${artifact}"
release:
  draft: false
changelog:
  use: github-native


File: /.travis.yml
language: go
go:
- 1.15.x
script:
- make build


File: /bin\wait-for-routeros.sh
#!/bin/sh

routeros_host=${1:-127.0.0.1}
routeros_port=${2:-8080}

echo "waiting for RouterOS (${routeros_host}:${routeros_port}) to be up and running"
for i in $(seq 1 60); do
    if curl -s --connect-timeout 1 -o /dev/null ${routeros_host}:${routeros_port}; then
        exit 0;
    else
        printf "."
        sleep 1
    fi
done;

exit 1


File: /client\bgp_instance.go
package client

import (
	"strings"

	"github.com/go-routeros/routeros"
)

type LegacyBgpUnsupported struct{}

func (LegacyBgpUnsupported) Error() string {
	return "Your RouterOS version does not support /routing/bgp/{instance,peer} commands"
}

func legacyBgpUnsupported(err error) bool {
	if err != nil {
		if strings.Contains(err.Error(), "no such command prefix") {
			return true
		}
	}
	return false
}

// BgpInstance Mikrotik resource
type BgpInstance struct {
	Id                       string `mikrotik:".id" codegen:"id,mikrotikID"`
	Name                     string `mikrotik:"name" codegen:"name,required,terraformID"`
	As                       int    `mikrotik:"as" codegen:"as,required"`
	ClientToClientReflection bool   `mikrotik:"client-to-client-reflection" codegen:"client_to_client_reflection"`
	Comment                  string `mikrotik:"comment" codegen:"comment"`
	ConfederationPeers       string `mikrotik:"confederation-peers" codegen:"confederation_peers"`
	Disabled                 bool   `mikrotik:"disabled" codegen:"disabled"`
	IgnoreAsPathLen          bool   `mikrotik:"ignore-as-path-len" codegen:"ignore_as_path_len"`
	OutFilter                string `mikrotik:"out-filter" codegen:"out_filter"`
	RedistributeConnected    bool   `mikrotik:"redistribute-connected" codegen:"redistribute_connected"`
	RedistributeOspf         bool   `mikrotik:"redistribute-ospf" codegen:"redistribute_ospf"`
	RedistributeOtherBgp     bool   `mikrotik:"redistribute-other-bgp" codegen:"redistribute_other_bgp"`
	RedistributeRip          bool   `mikrotik:"redistribute-rip" codegen:"redistribute_rip"`
	RedistributeStatic       bool   `mikrotik:"redistribute-static" codegen:"redistribute_static"`
	RouterID                 string `mikrotik:"router-id" codegen:"router_id,required"`
	RoutingTable             string `mikrotik:"routing-table" codegen:"routing_table"`
	ClusterID                string `mikrotik:"cluster-id" codegen:"cluster_id"`
	Confederation            int    `mikrotik:"confederation" codegen:"confederation"`
}

var _ Resource = (*BgpInstance)(nil)

func (b *BgpInstance) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/routing/bgp/instance/add",
		Find:   "/routing/bgp/instance/print",
		Update: "/routing/bgp/instance/set",
		Delete: "/routing/bgp/instance/remove",
	}[a]
}

func (b *BgpInstance) IDField() string {
	return ".id"
}

func (b *BgpInstance) ID() string {
	return b.Id
}

func (b *BgpInstance) SetID(id string) {
	b.Id = id
}

func (b *BgpInstance) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (b *BgpInstance) FindField() string {
	return "name"
}

func (b *BgpInstance) FindFieldValue() string {
	return b.Name
}

func (b *BgpInstance) DeleteField() string {
	return "numbers"
}

func (b *BgpInstance) DeleteFieldValue() string {
	return b.Name
}

// HandleError intercepts errors during CRUD operations.
// It is used to catch "no such command prefix" on RouterOS >= v7.0
func (b *BgpInstance) HandleError(err error) error {
	if legacyBgpUnsupported(err) {
		return LegacyBgpUnsupported{}
	}

	return err
}

// Typed wrappers
func (c Mikrotik) AddBgpInstance(r *BgpInstance) (*BgpInstance, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*BgpInstance), nil
}

func (c Mikrotik) UpdateBgpInstance(r *BgpInstance) (*BgpInstance, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*BgpInstance), nil
}

func (c Mikrotik) FindBgpInstance(name string) (*BgpInstance, error) {
	res, err := c.Find(&BgpInstance{Name: name})
	if err != nil {
		return nil, err
	}

	return res.(*BgpInstance), nil
}

func (c Mikrotik) DeleteBgpInstance(name string) error {
	err := c.Delete(&BgpInstance{Name: name})
	return err
}


File: /client\bgp_instance_test.go
package client

import (
	"reflect"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

var bgpName string = "test-bgp"
var as int = 65533
var updatedAs int = 65534
var clientToClientReflection bool = true
var clusterID string = "172.21.16.1"
var bgpComment string = "test comment with spaces"
var confederation int = 8
var updatedConfederation int = 5
var confederationPeers string = ""
var disabled bool = false
var ignoreAsPathLen bool = false
var outFilter string = ""
var redistributeConnected bool = false
var redistributeOspf bool = false
var redistributeOtherBgp bool = false
var redistributeRip bool = false
var redistributeStatic bool = false
var routerID string = "172.21.16.2"
var routingTable string = ""

func TestAddBgpInstanceAndDeleteBgpInstance(t *testing.T) {
	SkipIfRouterOSV7OrLater(t, sysResources)
	c := NewClient(GetConfigFromEnv())

	expectedBgpInstance := &BgpInstance{
		Name:                     bgpName,
		As:                       as,
		ClientToClientReflection: clientToClientReflection,
		IgnoreAsPathLen:          ignoreAsPathLen,
		OutFilter:                outFilter,
		RedistributeConnected:    redistributeConnected,
		RedistributeOspf:         redistributeOspf,
		RedistributeOtherBgp:     redistributeOtherBgp,
		RedistributeRip:          redistributeRip,
		RedistributeStatic:       redistributeStatic,
		RouterID:                 routerID,
		RoutingTable:             routingTable,
	}
	bgpInstance, err := c.AddBgpInstance(expectedBgpInstance)
	if err != nil {
		t.Fatalf("Error creating a bpg instance with: %v", err)
	}

	expectedBgpInstance.Id = bgpInstance.Id

	if !reflect.DeepEqual(bgpInstance, expectedBgpInstance) {
		t.Errorf("The bgp instance does not match what we expected. actual: %v expected: %v", bgpInstance, expectedBgpInstance)
	}

	err = c.DeleteBgpInstance(bgpInstance.Name)

	if err != nil {
		t.Errorf("Error deleting bgp instance with: %v", err)
	}
}

func TestAddAndUpdateBgpInstanceWithOptionalFieldsAndDeleteBgpInstance(t *testing.T) {
	SkipIfRouterOSV7OrLater(t, sysResources)
	c := NewClient(GetConfigFromEnv())

	expectedBgpInstance := &BgpInstance{
		Name:                     bgpName,
		As:                       as,
		ClientToClientReflection: clientToClientReflection,
		Comment:                  bgpComment,
		ConfederationPeers:       confederationPeers,
		Disabled:                 disabled,
		IgnoreAsPathLen:          ignoreAsPathLen,
		OutFilter:                outFilter,
		RedistributeConnected:    redistributeConnected,
		RedistributeOspf:         redistributeOspf,
		RedistributeOtherBgp:     redistributeOtherBgp,
		RedistributeRip:          redistributeRip,
		RedistributeStatic:       redistributeStatic,
		RouterID:                 routerID,
		RoutingTable:             routingTable,
		ClusterID:                clusterID,
		Confederation:            confederation,
	}
	bgpInstance, err := c.AddBgpInstance(expectedBgpInstance)
	require.NoError(t, err)

	expectedBgpInstance.Id = bgpInstance.Id
	assert.Equal(t, expectedBgpInstance, bgpInstance)

	// update fields
	expectedBgpInstance.Confederation = updatedConfederation
	expectedBgpInstance.As = updatedAs

	bgpInstance, err = c.UpdateBgpInstance(expectedBgpInstance)
	require.NoError(t, err)

	assert.Equal(t, expectedBgpInstance, bgpInstance)

	err = c.DeleteBgpInstance(bgpInstance.Name)
	require.NoError(t, err)
}

func TestFindBgpInstance_onNonExistantBgpInstance(t *testing.T) {
	SkipIfRouterOSV7OrLater(t, sysResources)
	c := NewClient(GetConfigFromEnv())

	name := "bgp instance does not exist"
	_, err := c.FindBgpInstance(name)

	require.Truef(t, IsNotFoundError(err),
		"Expecting to receive NotFound error for bgp instance %q", name)
}


File: /client\bgp_peer.go
package client

import (
	"github.com/go-routeros/routeros"
)

// BgpPeer Mikrotik resource
type BgpPeer struct {
	Id                   string `mikrotik:".id" codegen:"id,mikrotikID"`
	Name                 string `mikrotik:"name" codegen:"name,required,terraformID"`
	AddressFamilies      string `mikrotik:"address-families" codegen:"address_families,optional,computed"`
	AllowAsIn            int    `mikrotik:"allow-as-in" codegen:"allow_as_in"`
	AsOverride           bool   `mikrotik:"as-override" codegen:"as_override"`
	CiscoVplsNlriLenFmt  string `mikrotik:"cisco-vpls-nlri-len-fmt" codegen:"cisco_vpls_nlri_len_fmt"`
	Comment              string `mikrotik:"comment" codegen:"comment"`
	DefaultOriginate     string `mikrotik:"default-originate" codegen:"default_originate,optional,computed"`
	Disabled             bool   `mikrotik:"disabled" codegen:"disabled"`
	HoldTime             string `mikrotik:"hold-time" codegen:"hold_time,optional,computed"`
	InFilter             string `mikrotik:"in-filter" codegen:"in_filter"`
	Instance             string `mikrotik:"instance" codegen:"instance"`
	KeepAliveTime        string `mikrotik:"keepalive-time" codegen:"keepalive_time"`
	MaxPrefixLimit       int    `mikrotik:"max-prefix-limit" codegen:"max_prefix_limit"`
	MaxPrefixRestartTime string `mikrotik:"max-prefix-restart-time" codegen:"max_prefix_restart_time"`
	Multihop             bool   `mikrotik:"multihop" codegen:"multihop"`
	NexthopChoice        string `mikrotik:"nexthop-choice" codegen:"nexthop_choice,optional,computed"`
	OutFilter            string `mikrotik:"out-filter" codegen:"out_filter"`
	Passive              bool   `mikrotik:"passive" codegen:"passive"`
	RemoteAddress        string `mikrotik:"remote-address" codegen:"remote_address,required"`
	RemoteAs             int    `mikrotik:"remote-as" codegen:"remote_as,required"`
	RemotePort           int    `mikrotik:"remote-port" codegen:"remote_port"`
	RemovePrivateAs      bool   `mikrotik:"remove-private-as" codegen:"remove_private_as"`
	RouteReflect         bool   `mikrotik:"route-reflect" codegen:"route_reflect"`
	TCPMd5Key            string `mikrotik:"tcp-md5-key" codegen:"tcp_md5_key"`
	TTL                  string `mikrotik:"ttl" codegen:"ttl,optional,computed"`
	UpdateSource         string `mikrotik:"update-source" codegen:"update_source"`
	UseBfd               bool   `mikrotik:"use-bfd" codegen:"use_bfd"`
}

var _ Resource = (*BgpPeer)(nil)

func (b *BgpPeer) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/routing/bgp/peer/add",
		Find:   "/routing/bgp/peer/print",
		Update: "/routing/bgp/peer/set",
		Delete: "/routing/bgp/peer/remove",
	}[a]
}

func (b *BgpPeer) IDField() string {
	return ".id"
}

func (b *BgpPeer) ID() string {
	return b.Id
}

func (b *BgpPeer) SetID(id string) {
	b.Id = id
}

func (b *BgpPeer) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (b *BgpPeer) FindField() string {
	return "name"
}

func (b *BgpPeer) FindFieldValue() string {
	return b.Name
}

func (b *BgpPeer) DeleteField() string {
	return "numbers"
}

func (b *BgpPeer) DeleteFieldValue() string {
	return b.Name
}

// Typed wrappers
func (c Mikrotik) AddBgpPeer(r *BgpPeer) (*BgpPeer, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*BgpPeer), nil
}

func (c Mikrotik) UpdateBgpPeer(r *BgpPeer) (*BgpPeer, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*BgpPeer), nil
}

func (c Mikrotik) FindBgpPeer(name string) (*BgpPeer, error) {
	res, err := c.Find(&BgpPeer{Name: name})
	if err != nil {
		return nil, err
	}

	return res.(*BgpPeer), nil
}

func (c Mikrotik) DeleteBgpPeer(name string) error {
	return c.Delete(&BgpPeer{Name: name})
}


File: /client\bgp_peer_test.go
package client

import (
	"reflect"
	"testing"

	"github.com/stretchr/testify/require"
)

// required BGP Peer fields
var remoteAs int = 65533
var remoteAddress string = "172.21.16.0"

var peerTTL string = "default"
var addressFamilies string = "ip"
var defaultOriginate string = "never"
var holdTime string = "3m"
var nextHopChoice string = "default"

func TestAddBgpPeerAndDeleteBgpPeer(t *testing.T) {
	SkipIfRouterOSV7OrLater(t, sysResources)
	c := NewClient(GetConfigFromEnv())

	instanceName := "peer-test"
	bgpPeerName := "test-peer"

	_, err := c.AddBgpInstance(&BgpInstance{Name: instanceName, As: 65530, RouterID: "172.16.0.254"})
	if err != nil {
		t.Fatalf("unable to create BGP instance used for testing: %v", err)
	}
	defer func(c *Mikrotik, name string) {
		_ = c.DeleteBgpInstance(name)
	}(c, instanceName)

	expectedBgpPeer := &BgpPeer{
		Name:             bgpPeerName,
		Instance:         instanceName,
		RemoteAs:         remoteAs,
		RemoteAddress:    remoteAddress,
		TTL:              peerTTL,
		AddressFamilies:  addressFamilies,
		DefaultOriginate: defaultOriginate,
		HoldTime:         holdTime,
		NexthopChoice:    nextHopChoice,
	}
	bgpPeer, err := c.AddBgpPeer(expectedBgpPeer)
	if err != nil {
		t.Fatalf("Error creating a bpg peer with: %v", err)
	}

	expectedBgpPeer.Id = bgpPeer.Id

	if !reflect.DeepEqual(bgpPeer, expectedBgpPeer) {
		t.Errorf("The bgp peer does not match what we expected. actual: %v expected: %v", bgpPeer, expectedBgpPeer)
	}

	err = c.DeleteBgpPeer(bgpPeer.Name)

	if err != nil {
		t.Errorf("Error deleting bgp peer with: %v", err)
	}
}

func TestAddAndUpdateBgpPeerWithOptionalFieldsAndDeleteBgpPeer(t *testing.T) {
	SkipIfRouterOSV7OrLater(t, sysResources)
	c := NewClient(GetConfigFromEnv())

	instanceName := "peer-update-test"
	bgpPeerName := "test-peer-update"

	_, err := c.AddBgpInstance(&BgpInstance{Name: instanceName, As: 65530, RouterID: "172.16.1.254"})
	if err != nil {
		t.Fatalf("unable to create BGP instance used for testing: %v", err)
	}
	defer func(c *Mikrotik, name string) {
		_ = c.DeleteBgpInstance(name)
	}(c, instanceName)

	expectedBgpPeer := &BgpPeer{
		Name:             bgpPeerName,
		Instance:         instanceName,
		RemoteAs:         remoteAs,
		RemoteAddress:    remoteAddress,
		TTL:              peerTTL,
		AddressFamilies:  addressFamilies,
		DefaultOriginate: defaultOriginate,
		HoldTime:         holdTime,
		NexthopChoice:    nextHopChoice,
	}
	bgpPeer, err := c.AddBgpPeer(expectedBgpPeer)
	if err != nil {
		t.Fatalf("Error creating a bpg peer with: %v", err)
	}

	expectedBgpPeer.Id = bgpPeer.Id

	if !reflect.DeepEqual(bgpPeer, expectedBgpPeer) {
		t.Errorf("The bgp peer does not match what we expected. actual: %v expected: %v", bgpPeer, expectedBgpPeer)
	}

	// update fields
	expectedBgpPeer.UpdateSource = "172.21.16.1"
	expectedBgpPeer.TCPMd5Key = "test-key-name"
	expectedBgpPeer.RemotePort = 65000
	expectedBgpPeer.OutFilter = "test out filter"
	expectedBgpPeer.MaxPrefixRestartTime = "infinity"
	expectedBgpPeer.MaxPrefixLimit = 20
	expectedBgpPeer.KeepAliveTime = "30m"
	expectedBgpPeer.InFilter = "test in filter"
	expectedBgpPeer.Comment = "test comment"
	expectedBgpPeer.CiscoVplsNlriLenFmt = "bits"
	expectedBgpPeer.AllowAsIn = 0

	bgpPeer, err = c.UpdateBgpPeer(expectedBgpPeer)

	if !reflect.DeepEqual(bgpPeer, expectedBgpPeer) {
		t.Errorf("The bgp peer does not match what we expected. actual: %v expected: %v", bgpPeer, expectedBgpPeer)
	}

	err = c.DeleteBgpPeer(bgpPeer.Name)

	if err != nil {
		t.Errorf("Error deleting bgp peer with: %v", err)
	}
}

func TestFindBgpPeer_onNonExistantBgpPeer(t *testing.T) {
	SkipIfRouterOSV7OrLater(t, sysResources)
	c := NewClient(GetConfigFromEnv())

	name := "bgp peer does not exist"
	_, err := c.FindBgpPeer(name)

	require.Truef(t, IsNotFoundError(err),
		"Expecting to receive NotFound error for bgp peer %q.", name)
}


File: /client\bridge.go
package client

import (
	"github.com/go-routeros/routeros"
)

// Bridge defines /bridge resource
type Bridge struct {
	Id            string `mikrotik:".id" codegen:"id,mikrotikID"`
	Name          string `mikrotik:"name" codegen:"name,required,terraformID"`
	FastForward   bool   `mikrotik:"fast-forward" codegen:"fast_forward"`
	VlanFiltering bool   `mikrotik:"vlan-filtering" codegen:"vlan_filtering"`
	Comment       string `mikrotik:"comment" codegen:"comment"`
}

var _ Resource = (*Bridge)(nil)

func (b *Bridge) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/interface/bridge/add",
		Find:   "/interface/bridge/print",
		Update: "/interface/bridge/set",
		Delete: "/interface/bridge/remove",
	}[a]
}

func (b *Bridge) IDField() string {
	return ".id"
}

func (b *Bridge) ID() string {
	return b.Id
}

func (b *Bridge) SetID(id string) {
	b.Id = id
}

func (b *Bridge) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (b *Bridge) FindField() string {
	return "name"
}

func (b *Bridge) FindFieldValue() string {
	return b.Name
}

func (b *Bridge) DeleteField() string {
	return "numbers"
}

func (b *Bridge) DeleteFieldValue() string {
	return b.Name
}

// Typed wrappers
func (c Mikrotik) AddBridge(r *Bridge) (*Bridge, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*Bridge), nil
}

func (c Mikrotik) UpdateBridge(r *Bridge) (*Bridge, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*Bridge), nil
}

func (c Mikrotik) FindBridge(name string) (*Bridge, error) {
	res, err := c.Find(&Bridge{Name: name})
	if err != nil {
		return nil, err
	}

	return res.(*Bridge), nil
}

func (c Mikrotik) DeleteBridge(name string) error {
	return c.Delete(&Bridge{Name: name})
}


File: /client\bridge_port.go
package client

import (
	"github.com/go-routeros/routeros"
)

// BridgePort defines port-in-bridge association
type BridgePort struct {
	Id        string `mikrotik:".id" codegen:"id,mikrotikID"`
	Bridge    string `mikrotik:"bridge" codegen:"bridge"`
	Interface string `mikrotik:"interface" codegen:"interface"`
	PVId      int    `mikrotik:"pvid" codegen:"pvid"`
	Comment   string `mikrotik:"comment" codegen:"comment"`
}

var _ Resource = (*BridgePort)(nil)

func (b *BridgePort) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/interface/bridge/port/add",
		Find:   "/interface/bridge/port/print",
		Update: "/interface/bridge/port/set",
		Delete: "/interface/bridge/port/remove",
	}[a]
}

func (b *BridgePort) IDField() string {
	return ".id"
}

func (b *BridgePort) ID() string {
	return b.Id
}

func (b *BridgePort) SetID(id string) {
	b.Id = id
}

func (b *BridgePort) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (b *BridgePort) DeleteField() string {
	return "numbers"
}

func (b *BridgePort) DeleteFieldValue() string {
	return b.Id
}

// Typed wrappers
func (c Mikrotik) AddBridgePort(r *BridgePort) (*BridgePort, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*BridgePort), nil
}

func (c Mikrotik) UpdateBridgePort(r *BridgePort) (*BridgePort, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*BridgePort), nil
}

func (c Mikrotik) FindBridgePort(id string) (*BridgePort, error) {
	res, err := c.Find(&BridgePort{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*BridgePort), nil
}

func (c Mikrotik) DeleteBridgePort(id string) error {
	return c.Delete(&BridgePort{Id: id})
}


File: /client\bridge_port_test.go
package client

import (
	"reflect"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestBridgePort_basic(t *testing.T) {
	c := NewClient(GetConfigFromEnv())
	bridge, err := c.AddBridge(&Bridge{
		Name: "test_bridge",
	})
	if err != nil {
		t.Fatal(err)
		return
	}
	defer func() {
		if err := c.DeleteBridge(bridge.Name); err != nil {
			t.Error(err)
		}
	}()

	bridgePort, err := c.AddBridgePort(&BridgePort{
		Bridge:    bridge.Name,
		Interface: "*0",
	})
	require.NoError(t, err)

	defer func() {
		c.DeleteBridgePort(bridgePort.Id)
		require.NoError(t, err)

		_, err = c.FindBridgePort(bridgePort.Id)
		require.True(t, IsNotFoundError(err), "expected to get NotFound error")
	}()

	expected := &BridgePort{
		Id:        bridgePort.Id,
		Bridge:    "test_bridge",
		Interface: "*0",
		PVId:      1,
		Comment:   bridgePort.Comment,
	}
	if !reflect.DeepEqual(expected, bridgePort) {
		t.Errorf(`expected and actual bridge port objects are not equal:
		want: %+v,
		got: %+v
	`, expected, bridgePort)
	}
}


File: /client\bridge_test.go
package client

import (
	"reflect"
	"testing"
)

func TestBridgeBasic(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	name := "test_bridge"
	bridge := &Bridge{
		Name:          name,
		FastForward:   false,
		VlanFiltering: false,
		Comment:       "a test bridge",
	}
	_, err := c.AddBridge(bridge)
	if err != nil {
		t.Fatalf("expected no error, got %v", err)
	}

	found, err := c.FindBridge(name)
	if err != nil {
		t.Fatalf("expected no error, got %v", err)
	}
	bridge.Id = found.Id
	if !reflect.DeepEqual(bridge, found) {
		t.Fatalf("expected found resource to have pre-defined fields but it didn't")
	}

	updatedResource := &Bridge{
		Id:            found.Id,
		Name:          found.Name + "_updated",
		FastForward:   true,
		VlanFiltering: true,
		Comment:       "updated comment",
	}
	_, err = c.UpdateBridge(updatedResource)
	if err != nil {
		t.Fatalf("expected no error, got %v", err)
	}
	foundAfterUpdate, err := c.FindBridge(updatedResource.Name)
	if err != nil {
		t.Fatalf("expected no error, got %v", err)
	}
	if !reflect.DeepEqual(updatedResource, foundAfterUpdate) {
		t.Fatalf("expected found resource to have pre-defined fields but it didn't")
	}

	if err = c.DeleteBridge(name); err != nil {
		t.Fatalf("expected no error, got %v", err)
	}

	if err = c.DeleteBridge(name); err == nil {
		t.Fatal("expected notfound error, got nothing")
	}
}


File: /client\bridge_vlan.go
package client

import (
	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/go-routeros/routeros"
)

// BridgeVlan defines vlan filtering in bridge resource
type BridgeVlan struct {
	Id       string                `mikrotik:".id" codegen:"id,mikrotikID"`
	Bridge   string                `mikrotik:"bridge" codegen:"bridge,required"`
	Tagged   types.MikrotikList    `mikrotik:"tagged" codegen:"tagged,elemType=String"`
	Untagged types.MikrotikList    `mikrotik:"untagged" codegen:"untagged,elemType=String"`
	VlanIds  types.MikrotikIntList `mikrotik:"vlan-ids" codegen:"vlan_ids,elemType=Int64"`
}

var _ Resource = (*BridgeVlan)(nil)

func (b *BridgeVlan) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/interface/bridge/vlan/add",
		Find:   "/interface/bridge/vlan/print",
		Update: "/interface/bridge/vlan/set",
		Delete: "/interface/bridge/vlan/remove",
	}[a]
}

func (b *BridgeVlan) IDField() string {
	return ".id"
}

func (b *BridgeVlan) ID() string {
	return b.Id
}

func (b *BridgeVlan) SetID(id string) {
	b.Id = id
}

func (b *BridgeVlan) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (c Mikrotik) AddBridgeVlan(r *BridgeVlan) (*BridgeVlan, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*BridgeVlan), nil
}

func (c Mikrotik) UpdateBridgeVlan(r *BridgeVlan) (*BridgeVlan, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*BridgeVlan), nil
}

func (c Mikrotik) FindBridgeVlan(id string) (*BridgeVlan, error) {
	res, err := c.Find(&BridgeVlan{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*BridgeVlan), nil
}

func (c Mikrotik) DeleteBridgeVlan(id string) error {
	return c.Delete(&BridgeVlan{Id: id})
}


File: /client\bridge_vlan_test.go
package client

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestBridgeVlanBasic(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	bridge1Name := "test_bridge1_" + RandomString()
	bridge1 := &Bridge{
		Name:          bridge1Name,
		FastForward:   false,
		VlanFiltering: false,
		Comment:       "a test bridge",
	}
	_, err := c.AddBridge(bridge1)
	if err != nil {
		t.Fatalf("expected no error, got %v", err)
	}
	defer func() {
		if err = c.DeleteBridge(bridge1Name); err != nil {
			t.Fatalf("expected no error, got %v", err)
		}
	}()

	bridge2Name := "test_bridge2_" + RandomString()
	bridge2 := &Bridge{
		Name:          bridge2Name,
		FastForward:   false,
		VlanFiltering: false,
		Comment:       "a test bridge",
	}
	_, err = c.AddBridge(bridge2)
	if err != nil {
		t.Fatalf("expected no error, got %v", err)
	}
	defer func() {
		if err = c.DeleteBridge(bridge2Name); err != nil {
			t.Fatalf("expected no error, got %v", err)
		}
	}()

	bridgeVlan := &BridgeVlan{
		Bridge:  bridge1.Name,
		VlanIds: []int{10, 20},
	}

	createdBridgeVlan, err := c.AddBridgeVlan(bridgeVlan)
	if err != nil {
		t.Fatal(err)
	}

	expectedBridgeVlan := &BridgeVlan{
		Id:       createdBridgeVlan.Id,
		Bridge:   bridge1Name,
		VlanIds:  []int{10, 20},
		Tagged:   []string{},
		Untagged: []string{},
	}
	assert.Equal(t, expectedBridgeVlan, createdBridgeVlan)

	createdBridgeVlan.Bridge = bridge2Name
	updatedBridgeVlan, err := c.UpdateBridgeVlan(createdBridgeVlan)
	require.NoError(t, err)

	expectedBridgeVlan = &BridgeVlan{
		Id:       createdBridgeVlan.Id,
		Bridge:   bridge2Name,
		VlanIds:  []int{10, 20},
		Tagged:   []string{},
		Untagged: []string{},
	}
	assert.Equal(t, expectedBridgeVlan, updatedBridgeVlan)
}


File: /client\client.go
package client

import (
	"crypto/tls"
	"crypto/x509"
	"errors"
	"fmt"
	"log"
	"os"
	"reflect"
	"strconv"
	"strings"

	"github.com/go-routeros/routeros"
	"github.com/go-routeros/routeros/proto"
)

// Mikrotik struct defines connection parameters for RouterOS client
type Mikrotik struct {
	Host     string
	Username string
	Password string
	TLS      bool
	CA       string
	Insecure bool

	connection *routeros.Client
}

type (
	// Marshaler interface will be used to serialize struct to RouterOS sentence
	Marshaler interface {
		// MarshalMikrotik serializes Go type value as RouterOS field value
		MarshalMikrotik() string
	}

	// Unmarshaler interface will be used to de-serialize reply from RouterOS into Go struct
	Unmarshaler interface {
		// UnmarshalMikrotik de-serializes RouterOS field into Go type value
		UnmarshalMikrotik(string) error
	}
)

// NewClient initializes new Mikrotik client object
func NewClient(host, username, password string, tls bool, caCertificate string, insecure bool) *Mikrotik {
	return &Mikrotik{
		Host:     host,
		Username: username,
		Password: password,
		TLS:      tls,
		CA:       caCertificate,
		Insecure: insecure,
	}
}

func Marshal(c string, s interface{}) []string {
	var elem reflect.Value
	rv := reflect.ValueOf(s)

	if rv.Kind() == reflect.Ptr {
		// get Value of what pointer points to
		elem = rv.Elem()
	} else {
		elem = rv
	}

	cmd := []string{c}

	for i := 0; i < elem.NumField(); i++ {
		value := elem.Field(i)
		fieldType := elem.Type().Field(i)
		// fetch mikrotik struct tag, which supports multiple values separated by commas
		tags := fieldType.Tag.Get("mikrotik")
		// extract tag value that is the Mikrotik property name
		// it is assumed that the first is mikrotik field name
		mikrotikTags := strings.Split(tags, ",")
		mikrotikPropName := mikrotikTags[0]
		// now we have field name in separate variable,
		// so leave only modifiers in this slice
		mikrotikTags = mikrotikTags[1:]

		if mikrotikPropName == "" {
			// skip if property name is not set in struct tag
			continue
		}

		// skip attributes marked as `readonly` (computed by RouterOS), such as the following wireguard props
		// https://help.mikrotik.com/docs/display/ROS/WireGuard#WireGuard-Read-onlyproperties
		if contains(mikrotikTags, "readonly") {
			// if a struct field contains the tag value of 'readonly', do not marshal it
			continue
		}

		// types, which implement `Marshaler` interface, have higher priority as they likely to have specific logic
		// even for zero or nil values
		if mar, ok := value.Interface().(Marshaler); ok {
			// if type supports custom marshaling, use that result immediately
			stringValue := mar.MarshalMikrotik()
			cmd = append(cmd, fmt.Sprintf("=%s=%s", mikrotikPropName, stringValue))
			continue
		}

		// try to marshal non-zero values only
		// here `bool` is exception as we want to toggle boolean switches
		if !value.IsZero() || value.Kind() == reflect.Bool {
			switch value.Kind() {
			case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
				cmd = append(cmd, fmt.Sprintf("=%s=%d", mikrotikPropName, elem.Field(i).Interface()))
			case reflect.Uint, reflect.Uint8, reflect.Uint16, reflect.Uint32, reflect.Uint64:
				cmd = append(cmd, fmt.Sprintf("=%s=%d", mikrotikPropName, elem.Field(i).Interface()))
			case reflect.String:
				stringValue := elem.Field(i).Interface().(string)
				cmd = append(cmd, fmt.Sprintf("=%s=%s", mikrotikPropName, stringValue))
			case reflect.Bool:
				boolValue := elem.Field(i).Interface().(bool)
				stringBoolValue := boolToMikrotikBool(boolValue)
				cmd = append(cmd, fmt.Sprintf("=%s=%s", mikrotikPropName, stringBoolValue))
			}
		}
	}

	return cmd
}

// Unmarshal decodes MikroTik's API reply into Go object
func Unmarshal(reply routeros.Reply, v interface{}) error {
	rv := reflect.ValueOf(v)
	elem := rv.Elem()

	if rv.Kind() != reflect.Ptr {
		panic("Unmarshal cannot work without a pointer")
	}

	switch elem.Kind() {
	case reflect.Slice:
		l := len(reply.Re)
		t := elem.Type()
		if l < 1 {
			elem.Set(reflect.MakeSlice(t, 0, 0))
			break
		}

		d := reflect.MakeSlice(t, l, l)

		for i := 0; i < l; i++ {
			item := d.Index(i)
			sentence := reply.Re[i]

			parseStruct(&item, *sentence)
		}
		elem.Set(d)

	case reflect.Struct:
		if len(reply.Re) < 1 {
			// This is an empty message
			return nil
		}
		if len(reply.Re) > 1 {
			msg := fmt.Sprintf("Failed to decode reply: %v", reply)
			return errors.New(msg)
		}

		parseStruct(&elem, *reply.Re[0])
	}

	return nil
}

func GetConfigFromEnv() (host, username, password string, tls bool, caCertificate string, insecure bool) {
	host = os.Getenv("MIKROTIK_HOST")
	username = os.Getenv("MIKROTIK_USER")
	password = os.Getenv("MIKROTIK_PASSWORD")
	tlsString := os.Getenv("MIKROTIK_TLS")
	if tlsString == "true" {
		tls = true
	} else {
		tls = false
	}
	caCertificate = os.Getenv("MIKROTIK_CA_CERTIFICATE")
	insecureString := os.Getenv("MIKROTIK_INSECURE")
	if insecureString == "true" {
		insecure = true
	} else {
		insecure = false
	}
	if host == "" || username == "" || password == "" {
		// panic("Unable to find the MIKROTIK_HOST, MIKROTIK_USER or MIKROTIK_PASSWORD environment variable")
	}
	return host, username, password, tls, caCertificate, insecure
}

func (client *Mikrotik) getMikrotikClient() (*routeros.Client, error) {
	if client.connection != nil {
		return client.connection, nil
	}

	address := client.Host
	username := client.Username
	password := client.Password

	var mikrotikClient *routeros.Client
	var err error

	if client.TLS {
		var tlsCfg tls.Config
		tlsCfg.InsecureSkipVerify = client.Insecure

		if client.CA != "" {
			certPool := x509.NewCertPool()
			file, err := os.ReadFile(client.CA)
			if err != nil {
				log.Printf("[ERROR] Failed to read CA file %s: %v", client.CA, err)
				return nil, err
			}
			certPool.AppendCertsFromPEM(file)
			tlsCfg.RootCAs = certPool
		}

		mikrotikClient, err = routeros.DialTLS(address, username, password, &tlsCfg)
		if err != nil {
			return nil, err
		}
	} else {
		mikrotikClient, err = routeros.Dial(address, username, password)
	}

	if err != nil {
		log.Printf("[ERROR] Failed to login to routerOS with error: %v", err)
		return nil, err
	}

	client.connection = mikrotikClient

	return mikrotikClient, nil
}

func parseStruct(v *reflect.Value, sentence proto.Sentence) {
	elem := *v
	for i := 0; i < elem.NumField(); i++ {
		field := elem.Field(i)
		fieldType := elem.Type().Field(i)
		tags := strings.Split(fieldType.Tag.Get("mikrotik"), ",")

		path := strings.ToLower(fieldType.Name)
		fieldName := tags[0]

		for _, pair := range sentence.List {
			if strings.Compare(pair.Key, path) == 0 || strings.Compare(pair.Key, fieldName) == 0 {
				if field.CanAddr() {
					if unmar, ok := field.Addr().Interface().(Unmarshaler); ok {
						// if type supports custom unmarshaling, try it and skip the rest
						if err := unmar.UnmarshalMikrotik(pair.Value); err != nil {
							log.Printf("[ERROR] cannot unmarshal RouterOS reply: %v", err)
						}
						continue
					}
				}

				switch fieldType.Type.Kind() {
				case reflect.String:
					field.SetString(pair.Value)
				case reflect.Bool:
					b, _ := strconv.ParseBool(pair.Value)
					field.SetBool(b)
				case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
					intValue, _ := strconv.Atoi(pair.Value)
					field.SetInt(int64(intValue))
				case reflect.Uint, reflect.Uint8, reflect.Uint16, reflect.Uint32, reflect.Uint64:
					uintValue, _ := strconv.ParseUint(pair.Value, 10, 0)
					field.SetUint(uint64(uintValue))
				}
			}
		}
	}
}

func contains(s []string, e string) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func boolToMikrotikBool(b bool) string {
	if b {
		return "yes"
	} else {
		return "no"
	}
}


File: /client\client_crud.go
package client

import (
	"fmt"
	"log"
	"reflect"

	"github.com/go-routeros/routeros"
)

const (
	Add    Action = "add"
	Update Action = "update"
	Find   Action = "find"
	List   Action = "list"
	Delete Action = "delete"
)

type (
	// Action represents possible action on resource.
	Action string

	// Resource interface defines a contract for abstract RouterOS resource.
	Resource interface {
		// ActionToCommand translates CRUD action to RouterOS command path.
		ActionToCommand(Action) string

		// IDField reveals name of ID field to use in requests to MikroTik router.
		// It is used in operations like Find.
		IDField() string

		// ID returns value of the ID field.
		ID() string

		// SetID updates a value of the ID field.
		SetID(string)
	}

	// Adder defines contract for resources which require custom behaviour during resource creation.
	Adder interface {
		// AfterAddHook is called right after the resource successfully added.
		// This hook is mainly used to set resource's ID field based on reply from RouterOS.
		AfterAddHook(r *routeros.Reply)
	}

	// Finder defines contract for resources which provide custom behaviour during resource retrieval.
	Finder interface {
		// FindField retrieves a name of a field to use as key for resource retrieval.
		FindField() string

		// FindFieldValue retrieves a value to use for resource retrieval.
		FindFieldValue() string
	}

	// Deleter defines contract for resources which require custom behaviour during resource deletion.
	Deleter interface {
		// DeleteField retrieves a name of a field which is used for resource deletion.
		DeleteField() string

		// DeleteFieldValue retrieves a value for DeleteField field.
		DeleteFieldValue() string
	}

	// Normalizer is used to normalize response from RouterOS.
	// The main use-case is to populate fields which are empty in response but have default value,
	// for example `authoritative=yes` in `DHCPServer` resource is not returned by remote RouterOS instance.
	Normalizer interface {
		Normalize(r *routeros.Reply)
	}

	// ErrorHandler Defines contract to handle errors returned by RouterOS.
	// It can either return another error, or supress original error by returning nil.
	ErrorHandler interface {
		HandleError(error) error
	}

	// ResourceInstanceCreator interface defines methods to create new instance of a Resource.
	ResourceInstanceCreator interface {
		Create() Resource
	}
)

// Add creates new resource on remote system
func (client Mikrotik) Add(d Resource) (Resource, error) {
	c, err := client.getMikrotikClient()
	if err != nil {
		return nil, err
	}

	cmd := Marshal(d.ActionToCommand(Add), d)
	log.Printf("[INFO] Running the mikrotik command: `%s`", cmd)
	r, err := c.RunArgs(cmd)
	if eh, ok := d.(ErrorHandler); ok {
		err = eh.HandleError(err)
	}
	if err != nil {
		return nil, err
	}
	log.Printf("[DEBUG] creation response: `%v`", r)
	if adder, ok := d.(Adder); ok {
		adder.AfterAddHook(r)
	}

	return client.Find(d)
}

// Find retrieves resource from remote system
func (client Mikrotik) List(d Resource) ([]Resource, error) {
	cmd := []string{d.ActionToCommand(Find)}
	log.Printf("[INFO] Running the mikrotik command: `%s`", cmd)

	c, err := client.getMikrotikClient()
	if err != nil {
		return nil, err
	}
	r, err := c.RunArgs(cmd)
	if eh, ok := d.(ErrorHandler); ok {
		err = eh.HandleError(err)
	}
	if err != nil {
		return nil, err
	}
	log.Printf("[DEBUG] find response: %v", r)

	targetStruct := client.newTargetStruct(d)
	targetSlicePtr := reflect.New(reflect.SliceOf(reflect.Indirect(targetStruct).Type()))
	targetSlice := reflect.Indirect(targetSlicePtr)
	err = Unmarshal(*r, targetSlicePtr.Interface())
	if err != nil {
		return nil, err
	}

	returnSlice := make([]Resource, 0)
	for i := 0; i < targetSlice.Len(); i++ {
		returnSlice = append(returnSlice, targetSlice.Index(i).Addr().Interface().(Resource))
	}

	return returnSlice, nil
}

// Find retrieves resource from remote system
func (client Mikrotik) Find(d Resource) (Resource, error) {
	findField := d.IDField()
	findFieldValue := d.ID()
	if finder, ok := d.(Finder); ok {
		findField = finder.FindField()
		findFieldValue = finder.FindFieldValue()
	}
	return client.findByField(d, findField, findFieldValue)
}

// Update updates existing resource on remote system
func (client Mikrotik) Update(resource Resource) (Resource, error) {
	c, err := client.getMikrotikClient()
	if err != nil {
		return nil, err
	}

	cmd := Marshal(resource.ActionToCommand(Update), resource)
	log.Printf("[INFO] Running the mikrotik command: `%s`", cmd)
	_, err = c.RunArgs(cmd)
	if eh, ok := resource.(ErrorHandler); ok {
		err = eh.HandleError(err)
	}
	if err != nil {
		return nil, err
	}

	return client.Find(resource)
}

// Delete removes existing resource from remote system
func (client Mikrotik) Delete(d Resource) error {
	c, err := client.getMikrotikClient()
	if err != nil {
		return err
	}

	deleteField := d.IDField()
	deleteFieldValue := d.ID()
	if deleter, ok := d.(Deleter); ok {
		deleteField = deleter.DeleteField()
		deleteFieldValue = deleter.DeleteFieldValue()
	}
	cmd := []string{d.ActionToCommand(Delete), "=" + deleteField + "=" + deleteFieldValue}
	log.Printf("[INFO] Running the mikrotik command: `%s`", cmd)
	_, err = c.RunArgs(cmd)
	if rosErr, ok := err.(*routeros.DeviceError); ok {
		if rosErr.Sentence.Map["message"] == "no such item" {
			return NewNotFound(rosErr.Sentence.Map["message"])
		}
	}
	if eh, ok := d.(ErrorHandler); ok {
		err = eh.HandleError(err)
	}

	return err
}

func (client Mikrotik) findByField(d Resource, field, value string) (Resource, error) {
	cmd := []string{d.ActionToCommand(Find), "?" + field + "=" + value}
	log.Printf("[INFO] Running the mikrotik command: `%s`", cmd)

	c, err := client.getMikrotikClient()
	if err != nil {
		return nil, err
	}
	r, err := c.RunArgs(cmd)
	if eh, ok := d.(ErrorHandler); ok {
		err = eh.HandleError(err)
	}
	if err != nil {
		return nil, err
	}
	log.Printf("[DEBUG] find response: %v", r)

	targetStruct := client.newTargetStruct(d)
	targetStructInterface := targetStruct.Interface()
	err = Unmarshal(*r, targetStructInterface)
	if eh, ok := d.(ErrorHandler); ok {
		err = eh.HandleError(err)
	}
	if err != nil {
		return nil, err
	}

	if n, ok := targetStructInterface.(Normalizer); ok {
		n.Normalize(r)
	}

	// assertion is not checked as we are creating the targetStruct from 'd' argument which satisfies Resource interface
	targetResource := targetStructInterface.(Resource)
	if targetResource.ID() == "" {
		return nil, NewNotFound(fmt.Sprintf("resource `%T` with field `%s=%s` not found", targetStruct, field, value))
	}

	return targetResource, nil
}

func (client Mikrotik) newTargetStruct(d interface{}) reflect.Value {
	if c, ok := d.(ResourceInstanceCreator); ok {
		return reflect.New(reflect.Indirect(reflect.ValueOf(c.Create())).Type())
	}

	return reflect.New(reflect.Indirect(reflect.ValueOf(d)).Type())
}


File: /client\client_test.go
package client

import (
	"reflect"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/go-routeros/routeros"
	"github.com/go-routeros/routeros/proto"
	"github.com/stretchr/testify/assert"
)

func TestUnmarshal(t *testing.T) {
	type testStruct struct {
		Name          string
		NotNamedOwner string `mikrotik:"owner"`
		RunCount      int    `mikrotik:"run-count"`
		RunCount8     int8   `mikrotik:"run-count8"`
		RunCount16    int16  `mikrotik:"run-count16"`
		RunCount32    int32  `mikrotik:"run-count32"`
		RunCount64    int64  `mikrotik:"run-count64"`
		CountUint     uint   `mikrotik:"run-count-uint"`
		CountUint8    uint8  `mikrotik:"run-count-uint8"`
		CountUint16   uint16 `mikrotik:"run-count-uint16"`
		CountUint32   uint32 `mikrotik:"run-count-uint32"`
		CountUint64   uint64 `mikrotik:"run-count-uint64"`

		Allowed  bool
		Schedule types.MikrotikList
	}

	testCases := []struct {
		name           string
		expectedResult testStruct
		reply          routeros.Reply
	}{
		{
			name: "basic types only",
			reply: routeros.Reply{
				Re: []*proto.Sentence{
					{
						Word: "!re",
						List: []proto.Pair{
							{
								Key:   "name",
								Value: "testing script",
							},
							{
								Key:   "owner",
								Value: "admin",
							},
							{
								Key:   "run-count",
								Value: "3",
							},
							{
								Key:   "run-count8",
								Value: "-3",
							},
							{
								Key:   "run-count16",
								Value: "12000",
							},
							{
								Key:   "run-count32",
								Value: "12000000",
							},
							{
								Key:   "run-count64",
								Value: "12000000000000",
							},
							{
								Key:   "run-count-uint",
								Value: "500",
							},
							{
								Key:   "run-count-uint8",
								Value: "5",
							},
							{
								Key:   "run-count-uint16",
								Value: "15000",
							},
							{
								Key:   "run-count-uint32",
								Value: "15000000",
							},
							{
								Key:   "run-count-uint64",
								Value: "15000000000000000",
							},
							{
								Key:   "allowed",
								Value: "true",
							},
						},
					},
				},
			},
			expectedResult: testStruct{
				Name:          "testing script",
				NotNamedOwner: "admin",
				RunCount:      3,
				RunCount8:     -3,
				RunCount16:    12000,
				RunCount32:    12000000,
				RunCount64:    12000000000000,
				CountUint:     500,
				CountUint8:    5,
				CountUint16:   15000,
				CountUint32:   15000000,
				CountUint64:   15000000000000000,
				Allowed:       true,
			},
		},
		{
			name: "MikrotikList type",
			reply: routeros.Reply{
				Re: []*proto.Sentence{
					{
						Word: "!re",
						List: []proto.Pair{
							{
								Key:   "owner",
								Value: "admin",
							},
							{
								Key:   "schedule",
								Value: "mon,wed,fri",
							},
						},
					},
				},
			},
			expectedResult: testStruct{
				NotNamedOwner: "admin",
				Schedule:      []string{"mon", "wed", "fri"},
			},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			targetStruct := testStruct{}
			err := Unmarshal(tc.reply, &targetStruct)
			assert.NoError(t, err)
			assert.Equal(t, tc.expectedResult, targetStruct)
		})
	}
}

func TestUnmarshalOnSlices(t *testing.T) {
	name := "testing script"
	owner := "admin"
	allowed := "true"
	type testStruct struct {
		Name          string
		NotNamedOwner string `mikrotik:"owner"`
		Allowed       bool
	}

	cases := []struct {
		name     string
		reply    routeros.Reply
		expected []testStruct
	}{
		{
			name: "reply with len > 1",
			reply: routeros.Reply{
				Re: []*proto.Sentence{
					{
						Word: "!re",
						List: []proto.Pair{
							{
								Key:   "name",
								Value: name,
							},
							{
								Key:   "owner",
								Value: owner,
							},
							{
								Key:   "allowed",
								Value: allowed,
							},
						},
					},
					{
						Word: "!re",
						List: []proto.Pair{
							{
								Key:   "name",
								Value: name + " 2",
							},
							{
								Key:   "owner",
								Value: owner + " 2",
							},
							{
								Key:   "allowed",
								Value: allowed,
							},
						},
					},
				},
			},
			expected: []testStruct{
				{
					Name:          name,
					NotNamedOwner: owner,
					Allowed:       true,
				},
				{
					Name:          name + " 2",
					NotNamedOwner: owner + " 2",
					Allowed:       true,
				},
			},
		},
		{
			name: "reply with single element",
			reply: routeros.Reply{
				Re: []*proto.Sentence{
					{
						Word: "!re",
						List: []proto.Pair{
							{
								Key:   "name",
								Value: name,
							},
							{
								Key:   "owner",
								Value: owner,
							},
							{
								Key:   "allowed",
								Value: allowed,
							},
						},
					},
				},
			},
			expected: []testStruct{
				{
					Name:          name,
					NotNamedOwner: owner,
					Allowed:       true,
				},
			},
		},
		{
			name: "empty reply",
			reply: routeros.Reply{
				Re: []*proto.Sentence{},
			},
			expected: []testStruct{},
		},
	}

	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			var result []testStruct
			err := Unmarshal(tc.reply, &result)

			if err != nil {
				t.Errorf("Failed to unmarshal with error: %v", err)
			}

			if !reflect.DeepEqual(tc.expected, result) {
				t.Errorf(`unexpected result:
				want: %#v
				got: %#v
				`, tc.expected, result)
			}
		})
	}
}

func TestMarshal(t *testing.T) {
	action := "/test/owner/add"
	testCases := []struct {
		name        string
		testStruct  interface{}
		expectedCmd []string
	}{
		{
			name: "basic types",
			testStruct: struct {
				Name          string `mikrotik:"name"`
				NotNamedOwner string `mikrotik:"owner,extraTagNotUsed"`
				RunCount      int    `mikrotik:"run-count"`
				RunCount8     int8   `mikrotik:"run-count8"`
				RunCount16    int16  `mikrotik:"run-count16"`
				RunCount32    int32  `mikrotik:"run-count32"`
				RunCount64    int64  `mikrotik:"run-count64"`
				CountUint     uint   `mikrotik:"run-count-uint"`
				CountUint8    uint8  `mikrotik:"run-count-uint8"`
				CountUint16   uint16 `mikrotik:"run-count-uint16"`
				CountUint32   uint32 `mikrotik:"run-count-uint32"`
				CountUint64   uint64 `mikrotik:"run-count-uint64"`
				ReadOnlyProp  bool   `mikrotik:"read-only-prop,readonly"`
				Allowed       bool   `mikrotik:"allowed-or-not"`
			}{
				Name:          "test owner",
				NotNamedOwner: "admin",
				RunCount:      3,
				RunCount8:     10,
				RunCount16:    12000,
				RunCount32:    -12_000_000,
				RunCount64:    12_000_000_000_000_000,
				CountUint:     15000,
				CountUint8:    250,
				CountUint16:   15000,
				CountUint32:   15_000_000,
				CountUint64:   15_000_000_000_000_000,
				Allowed:       true,
			},
			expectedCmd: []string{
				"/test/owner/add",
				"=name=test owner",
				"=owner=admin",
				"=run-count=3",
				"=run-count8=10",
				"=run-count16=12000",
				"=run-count32=-12000000",
				"=run-count64=12000000000000000",
				"=run-count-uint=15000",
				"=run-count-uint8=250",
				"=run-count-uint16=15000",
				"=run-count-uint32=15000000",
				"=run-count-uint64=15000000000000000",
				"=allowed-or-not=yes",
			},
		},
		{
			name: "MikrotikList type",
			testStruct: struct {
				Name          string             `mikrotik:"name"`
				NotNamedOwner string             `mikrotik:"owner,extraTagNotUsed"`
				RunCount      int                `mikrotik:"run-count"`
				Allowed       bool               `mikrotik:"allowed-or-not"`
				Schedule      types.MikrotikList `mikrotik:"schedule"`
			}{
				Name:          "test owner",
				NotNamedOwner: "admin",
				RunCount:      3,
				Allowed:       true,
				Schedule:      []string{"mon", "tue", "fri"},
			},
			expectedCmd: []string{
				"/test/owner/add",
				"=name=test owner",
				"=owner=admin",
				"=run-count=3",
				"=allowed-or-not=yes",
				"=schedule=mon,tue,fri",
			},
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			cmd := Marshal(action, tc.testStruct)
			if !reflect.DeepEqual(cmd, tc.expectedCmd) {
				t.Errorf("Failed to marshal: %v does not equal expected %v", cmd, tc.expectedCmd)
			}
		})
	}
}

func TestMarshalStructWithoutTags(t *testing.T) {
	action := "/test/owner/add"
	name := "test owner"
	owner := "admin"
	runCount := 3
	allowed := true
	retain := false
	testStruct := struct {
		Name           string `example:"name"`
		NotNamedOwner  string `json:"not-named"`
		RunCount       int
		Allowed        bool
		Retain         bool
		SecondaryOwner string
	}{name, owner, runCount, allowed, retain, ""}

	expectedCmd := []string{action}
	cmd := Marshal(action, &testStruct)

	if !reflect.DeepEqual(cmd, expectedCmd) {
		t.Errorf("Marshaling with a struct without tags should return the command action supplied: %v does not equal expected %v", cmd, expectedCmd)
	}
}


File: /client\console-inspected\parse.go
package consoleinspected

import (
	"fmt"
	"strings"
)

// Parse parses definition of inspected console item and extracts items using splitStrategy.
//
// It returns console item struct with its subcommands, commands, arguments, etc.
func Parse(input string, splitStrategy ItemsDefinitionSplitStrategy) (ConsoleItem, error) {
	chunks, err := splitStrategy.Split(input)
	if err != nil {
		return ConsoleItem{}, err
	}

	var result ConsoleItem
	result.Self = Item{}

	for _, v := range chunks {
		item, err := parseItem(v)
		if err != nil {
			return ConsoleItem{}, err
		}
		if item.Type == TypeSelf {
			result.Self = item
			continue
		}
		switch t := item.NodeType; t {
		case NodeTypeDir:
			result.Subcommands = append(result.Subcommands, item.Name)
		case NodeTypeArg:
			result.Arguments = append(result.Arguments, item)
		case NodeTypeCommand:
			result.Commands = append(result.Commands, item.Name)
		default:
			return ConsoleItem{}, fmt.Errorf("unknown node type %q", t)
		}
	}

	return result, nil
}

func parseItem(input string) (Item, error) {
	result := Item{}
	for _, v := range strings.Split(input, ";") {
		if strings.TrimSpace(v) == "" {
			continue
		}
		if strings.HasPrefix(v, "name=") {
			result.Name = strings.TrimPrefix(v, "name=")
		}
		if strings.HasPrefix(v, "node-type=") {
			result.NodeType = NodeType(strings.TrimPrefix(v, "node-type="))
		}
		if strings.HasPrefix(v, "type=") {
			result.Type = Type(strings.TrimPrefix(v, "type="))
		}
	}

	return result, nil
}


File: /client\console-inspected\parse_test.go
package consoleinspected

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestParse(t *testing.T) {
	testCases := []struct {
		name          string
		input         string
		expected      ConsoleItem
		expectedError bool
	}{
		{
			name:  "simple command",
			input: "name=add;node-type=cmd;type=self;name=comment;node-type=arg;type=child;name=copy-from;node-type=arg;type=child;",
			expected: ConsoleItem{
				Self: Item{
					Name:     "add",
					NodeType: NodeTypeCommand,
					Type:     TypeSelf,
				},
				Arguments: []Item{
					{Name: "comment", NodeType: NodeTypeArg, Type: TypeChild},
					{Name: "copy-from", NodeType: NodeTypeArg, Type: TypeChild},
				},
			},
		},
		{
			name:  "command with subcommands",
			input: "name=list;node-type=dir;type=self;name=add;node-type=cmd;type=child;name=comment;node-type=cmd;type=child;name=edit;node-type=cmd;type=child;name=export;node-type=cmd;type=child;name=find;node-type=cmd;type=child;name=get;node-type=cmd;type=child;name=member;node-type=dir;type=child;name=print;node-type=cmd;type=child;name=remove;node-type=cmd;type=child;name=reset;node-type=cmd;type=child;name=set;node-type=cmd;type=child",
			expected: ConsoleItem{
				Self: Item{
					Name:     "list",
					NodeType: NodeTypeDir,
					Type:     TypeSelf,
				},
				Commands: []string{
					"add",
					"comment",
					"edit",
					"export",
					"find",
					"get",
					"print",
					"remove",
					"reset",
					"set",
				},
				Subcommands: []string{"member"},
			},
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			item, err := Parse(tc.input, DefaultSplitStrategy)
			if !assert.Equal(t, !tc.expectedError, err == nil) || tc.expectedError {
				return
			}
			assert.Equal(t, tc.expected, item)
		})
	}
}


File: /client\console-inspected\split_strategy.go
package consoleinspected

import "strings"

var DefaultSplitStrategy = splitStrategyFunc(orderedSplit)

type splitStrategyFunc func(string) ([]string, error)

func (f splitStrategyFunc) Split(in string) ([]string, error) {
	return f(in)
}

// orderedSplit splits items definition using order of fields.
//
// Each 'name=' key starts a new item definition.
func orderedSplit(in string) ([]string, error) {
	result := []string{}

	buf := strings.Builder{}
	for _, v := range strings.Split(in, ";") {
		if strings.TrimSpace(v) == "" {
			continue
		}
		if strings.HasPrefix(v, "name=") {
			if buf.Len() > 0 {
				result = append(result, buf.String())
			}
			buf.Reset()
		}
		buf.WriteString(v)
		buf.WriteString(";")
	}
	if buf.Len() > 0 {
		result = append(result, buf.String())
	}

	return result, nil
}


File: /client\console-inspected\types.go
package consoleinspected

const (
	// NodeTypeDir represents console menu level.
	NodeTypeDir NodeType = "dir"

	// NodeTypeCommand represents console command that can be called.
	NodeTypeCommand NodeType = "cmd"

	// NodeTypeArg represents console item that is argument to a command.
	NodeTypeArg NodeType = "arg"

	// TypeSelf is console item type for currently inspected item.
	TypeSelf Type = "self"

	// TypeChild is console item type of all items within inspected container.
	TypeChild Type = "child"
)

type (
	// NodeType is dedicated type that holds values of "node-type" field of console item.
	NodeType string

	// Type is dedicated type that holds values of "type" field of console item.
	Type string

	// Item represents inspected console items.
	Item struct {
		NodeType NodeType `mikrotik:"node-type"`
		Type     Type     `mikrotik:"type"`
		Name     string   `mikrotik:"name"`
	}

	// ConsoleItem represents inspected console item with extracted commands, arguments, etc.
	ConsoleItem struct {
		// Self holds information about current console item.
		Self Item

		// Commands holds a list of commands available for this menu level.
		// Valid only for ConsoleItem of type NodeTypeDir.
		Commands []string

		// Subcommands holds a list of commands for the nested menu level.
		// Valid only for ConsoleItem of type NodeTypeDir.
		Subcommands []string

		// Arguments holds a list of argument items for a command.
		// Valid only for ConsoleItem of type NodeItemCommand.
		Arguments []Item
	}
)

type (
	ItemsDefinitionSplitStrategy interface {
		// Split splits set of items definition represented by a single string into chunks of separate item definitions.
		Split(string) ([]string, error)
	}
)


File: /client\console_inspect.go
package client

import (
	"strings"

	consoleinspected "github.com/ddelnano/terraform-provider-mikrotik/client/console-inspected"
)

func (c Mikrotik) InspectConsoleCommand(command string) (consoleinspected.ConsoleItem, error) {
	client, err := c.getMikrotikClient()
	if err != nil {
		return consoleinspected.ConsoleItem{}, err
	}
	normalizedCommand := strings.ReplaceAll(command[1:], "/", ",")
	cmd := []string{"/console/inspect", "as-value", "=path=" + normalizedCommand, "=request=child"}
	reply, err := client.RunArgs(cmd)
	if err != nil {
		return consoleinspected.ConsoleItem{}, err
	}
	var items []consoleinspected.Item
	var result consoleinspected.ConsoleItem
	if err := Unmarshal(*reply, &items); err != nil {
		return consoleinspected.ConsoleItem{}, err
	}

	for _, v := range items {
		if v.Type == consoleinspected.TypeSelf {
			result.Self = v
			continue
		}
		switch v.NodeType {
		case consoleinspected.NodeTypeArg:
			result.Arguments = append(result.Arguments, v)
		case consoleinspected.NodeTypeCommand:
			result.Commands = append(result.Commands, v.Name)
		case consoleinspected.NodeTypeDir:
			result.Subcommands = append(result.Subcommands, v.Name)
		}
	}

	return result, nil
}


File: /client\dhcp_server.go
package client

import (
	"github.com/go-routeros/routeros"
)

// DhcpServer represents DHCP server resource
type DhcpServer struct {
	Id            string `mikrotik:".id" codegen:"id,mikrotikID"`
	Name          string `mikrotik:"name" codegen:"name,terraformID,required"`
	Disabled      bool   `mikrotik:"disabled" codegen:"disabled"`
	AddArp        bool   `mikrotik:"add-arp" codegen:"add_arp"`
	AddressPool   string `mikrotik:"address-pool" codegen:"address_pool"`
	Authoritative string `mikrotik:"authoritative" codegen:"authoritative"`
	Interface     string `mikrotik:"interface" codegen:"interface"`
	LeaseScript   string `mikrotik:"lease-script" codegen:"lease_script"`
}

var _ Resource = (*DhcpServer)(nil)

func (b *DhcpServer) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/ip/dhcp-server/add",
		Find:   "/ip/dhcp-server/print",
		Update: "/ip/dhcp-server/set",
		Delete: "/ip/dhcp-server/remove",
	}[a]
}

func (b *DhcpServer) IDField() string {
	return ".id"
}

func (b *DhcpServer) ID() string {
	return b.Id
}

func (b *DhcpServer) SetID(id string) {
	b.Id = id
}

func (b *DhcpServer) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (b *DhcpServer) FindField() string {
	return "name"
}

func (b *DhcpServer) Normalize(r *routeros.Reply) {
	if len(r.Re) < 1 || len(r.Re[0].Map) < 1 {
		return
	}

	if _, ok := r.Re[0].Map["authoritative"]; !ok {
		b.Authoritative = "yes"
	}
}

func (b *DhcpServer) FindFieldValue() string {
	return b.Name
}

func (b *DhcpServer) DeleteField() string {
	return "numbers"
}

func (b *DhcpServer) DeleteFieldValue() string {
	return b.Name
}

// Typed wrappers
func (c Mikrotik) AddDhcpServer(r *DhcpServer) (*DhcpServer, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*DhcpServer), nil
}

func (c Mikrotik) UpdateDhcpServer(r *DhcpServer) (*DhcpServer, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*DhcpServer), nil
}

func (c Mikrotik) FindDhcpServer(name string) (*DhcpServer, error) {
	res, err := c.Find(&DhcpServer{Name: name})
	if err != nil {
		return nil, err
	}

	return res.(*DhcpServer), nil
}

func (c Mikrotik) DeleteDhcpServer(name string) error {
	return c.Delete(&DhcpServer{Name: name})
}


File: /client\dhcp_server_network.go
package client

import "github.com/go-routeros/routeros"

// DhcpServerNetwork describes network configuration for DHCP server
type DhcpServerNetwork struct {
	Id        string `mikrotik:".id" codegen:"id,mikrotikID"`
	Comment   string `mikrotik:"comment" codegen:"comment"`
	Address   string `mikrotik:"address" codegen:"address"`
	Netmask   string `mikrotik:"netmask" codegen:"netmask"`
	Gateway   string `mikrotik:"gateway" codegen:"gateway"`
	DnsServer string `mikrotik:"dns-server" codegen:"dns_server"`
}

var _ Resource = (*DhcpServerNetwork)(nil)

func (b *DhcpServerNetwork) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/ip/dhcp-server/network/add",
		Find:   "/ip/dhcp-server/network/print",
		Update: "/ip/dhcp-server/network/set",
		Delete: "/ip/dhcp-server/network/remove",
	}[a]
}

func (b *DhcpServerNetwork) IDField() string {
	return ".id"
}

func (b *DhcpServerNetwork) ID() string {
	return b.Id
}

func (b *DhcpServerNetwork) SetID(id string) {
	b.Id = id
}

func (b *DhcpServerNetwork) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

// Typed wrappers
func (c Mikrotik) AddDhcpServerNetwork(r *DhcpServerNetwork) (*DhcpServerNetwork, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*DhcpServerNetwork), nil
}

func (c Mikrotik) UpdateDhcpServerNetwork(r *DhcpServerNetwork) (*DhcpServerNetwork, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*DhcpServerNetwork), nil
}

func (c Mikrotik) FindDhcpServerNetwork(id string) (*DhcpServerNetwork, error) {
	res, err := c.Find(&DhcpServerNetwork{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*DhcpServerNetwork), nil
}

func (c Mikrotik) DeleteDhcpServerNetwork(id string) error {
	return c.Delete(&DhcpServerNetwork{Id: id})
}


File: /client\dhcp_server_network_test.go
package client

import "testing"

func TestAddDhcpServerNetworkUpdateAndDelete(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	netmask := "255.255.255.0"
	network := "192.168.99.0"
	dhcpServerNetwork, err := c.AddDhcpServerNetwork(&DhcpServerNetwork{
		Address: network + "/" + netmask,
		Netmask: netmask,
		Comment: "Created by terraform",
	})
	if err != nil {
		t.Fatal(err)
	}

	found, err := c.FindDhcpServerNetwork(dhcpServerNetwork.Id)
	if err != nil {
		t.Fatal(err)
	}

	if found.Address != dhcpServerNetwork.Address {
		t.Errorf("expected network address to be %q, got %q", dhcpServerNetwork.Address, found.Address)
	}

	dhcpServerNetwork.Comment = "updated network"
	updated, err := c.UpdateDhcpServerNetwork(dhcpServerNetwork)
	if err != nil {
		t.Error(err)
	}

	if updated.Comment != "updated network" {
		t.Errorf("expected comment to be %q, got %q", dhcpServerNetwork.Comment, updated.Comment)
	}

	// cleanup
	if err := c.DeleteDhcpServerNetwork(dhcpServerNetwork.Id); err != nil {
		t.Error(err)
	}

	_, err = c.FindDhcpServerNetwork(dhcpServerNetwork.Id)
	if err == nil {
		t.Error("expected error, got nil")
	}
}


File: /client\dhcp_server_test.go
package client

import "testing"

func TestAddDhcpServerUpdateAndDelete(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	name := "myserver"
	disabled := true
	dhcpServer, err := c.AddDhcpServer(&DhcpServer{
		Name:      name,
		Disabled:  disabled,
		Interface: "*0",
	})
	if err != nil {
		t.Fatal(err)
	}

	foundServer, err := c.FindDhcpServer(name)
	if err != nil {
		t.Fatal(err)
	}

	if foundServer.Name != name {
		t.Errorf("expected server name to be %q, got %q", name, foundServer.Name)
	}

	dhcpServer.Name = dhcpServer.Name + "updated"
	updatedServer, err := c.UpdateDhcpServer(dhcpServer)
	if err != nil {
		t.Error(err)
	}

	if updatedServer.Name != dhcpServer.Name {
		t.Errorf("expected name to be %q, got %q", dhcpServer.Name, updatedServer.Name)
	}

	// cleanup
	if err := c.DeleteDhcpServer(dhcpServer.Id); err != nil {
		t.Error(err)
	}

	_, err = c.FindDhcpServer(name)
	if err == nil {
		t.Error("expected error, got nil")
	}
}


File: /client\dns.go
package client

import (
	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/go-routeros/routeros"
)

type DnsRecord struct {
	Id      string                 `mikrotik:".id" codegen:"id,mikrotikID"`
	Name    string                 `mikrotik:"name" codegen:"name,terraformID,required"`
	Address string                 `mikrotik:"address" codegen:"address,required"`
	Regexp  string                 `mikrotik:"regexp" codegen:"regexp"`
	Ttl     types.MikrotikDuration `mikrotik:"ttl" codegen:"ttl"`
	Comment string                 `mikrotik:"comment" codegen:"comment"`
}

func (d *DnsRecord) ActionToCommand(action Action) string {
	return map[Action]string{
		Add:    "/ip/dns/static/add",
		Find:   "/ip/dns/static/print",
		List:   "/ip/dns/static/print",
		Update: "/ip/dns/static/set",
		Delete: "/ip/dns/static/remove",
	}[action]
}

func (d *DnsRecord) IDField() string {
	return ".id"
}

func (d *DnsRecord) ID() string {
	return d.Id
}

func (d *DnsRecord) SetID(id string) {
	d.Id = id
}

func (d *DnsRecord) AfterAddHook(r *routeros.Reply) {
	d.Id = r.Done.Map["ret"]
}

func (d *DnsRecord) DeleteField() string {
	return "numbers"
}

func (d *DnsRecord) DeleteFieldValue() string {
	return d.Id
}

func (client Mikrotik) AddDnsRecord(d *DnsRecord) (*DnsRecord, error) {
	res, err := client.Add(d)
	if err != nil {
		return nil, err
	}

	return res.(*DnsRecord), nil
}

func (client Mikrotik) FindDnsRecord(name string) (*DnsRecord, error) {
	res, err := client.Find(&FindByFieldWrapper{
		Resource:       &DnsRecord{Name: name},
		field:          "name",
		fieldValueFunc: func() string { return name },
	})
	if err != nil {
		return nil, err
	}

	return res.(*DnsRecord), nil
}

func (client Mikrotik) UpdateDnsRecord(d *DnsRecord) (*DnsRecord, error) {
	res, err := client.Update(d)
	if err != nil {
		return nil, err
	}

	return res.(*DnsRecord), nil
}

func (client Mikrotik) DeleteDnsRecord(id string) error {
	return client.Delete(&DnsRecord{Id: id})
}


File: /client\dns_test.go
package client

import (
	"reflect"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestFindDnsRecord_onNonExistantDnsRecord(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	name := "dns record does not exist"
	_, err := c.FindDnsRecord(name)

	require.Truef(t, IsNotFoundError(err),
		"Expecting to receive NotFound error for dns record %q", name)
}

func TestDnsRecord_basic(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	recordName := "new_record"
	record := &DnsRecord{
		Name:    recordName,
		Address: "10.10.10.200",
		Ttl:     300,
		Comment: "new record from test",
	}

	created, err := c.Add(record)
	if err != nil {
		t.Errorf("expected no error, got %v", err)
		return
	}

	found, err := c.Find(&DnsRecord{Id: created.ID()})
	require.NoError(t, err)

	if !reflect.DeepEqual(created, found) {
		t.Error("expected created and found resources to be equal, but they don't")
	}

	created.(*DnsRecord).Comment = "updated comment"
	_, err = c.Update(created)
	require.NoError(t, err)
	found, err = c.Find(&DnsRecord{Id: created.ID()})
	require.NoError(t, err)
	assert.Equal(t, created, found)

	err = c.Delete(found)
	assert.NoError(t, err)

	_, err = c.Find(&DnsRecord{Id: created.ID()})
	require.Error(t, err)

	require.True(t, IsNotFoundError(err),
		"expected to get NotFound error")
}

func TestDns_Regexp(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	recordName := "new_record"
	record := &DnsRecord{
		Name:    recordName,
		Regexp:  ".*\\.domain\\.com",
		Address: "10.10.10.200",
		Ttl:     300,
		Comment: "new record from test",
	}

	_, err := c.Add(record)
	require.Error(t, err, "usage of 'name' and 'regexp' at the same type should result in error")

	regexRecord := &DnsRecord{
		Address: "10.10.10.201",
		Ttl:     300,
		Regexp:  ".+\\.domain\\.com",
		Comment: "new record from test",
	}
	regexCreated, err := c.Add(regexRecord)
	require.NoError(t, err)
	defer func() {
		_ = c.Delete(regexCreated)
	}()
	assert.Equal(t, regexRecord, regexCreated)
}


File: /client\errors.go
package client

import "errors"

type NotFound struct {
	s string
}

func NewNotFound(text string) error {
	return NotFound{text}
}

func (e NotFound) Error() string {
	return e.s
}

func IsNotFoundError(err error) bool {
	var e NotFound
	var ePtr *NotFound

	return errors.As(err, &e) || errors.As(err, &ePtr)
}


File: /client\errors_test.go
package client

import (
	"errors"
	"fmt"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestIsNotFoundError(t *testing.T) {

	testCases := []struct {
		name     string
		err      error
		expected bool
	}{
		{
			name:     "nil error",
			expected: false,
		},
		{
			name:     "created via NewNotFoundError()",
			err:      NewNotFound("not found"),
			expected: true,
		},
		{
			name:     "created directly via struct initialization",
			err:      NotFound{},
			expected: true,
		},
		{
			name:     "chained with other errors",
			err:      fmt.Errorf("cannot load object info: %w", NewNotFound("no such object")),
			expected: true,
		},
		{
			name:     "chain of non-matching errors",
			err:      fmt.Errorf("cannot load object info: %w", errors.New("no such object")),
			expected: false,
		},
		{
			name:     "generic error",
			err:      errors.New("no such object"),
			expected: false,
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := IsNotFoundError(tc.err)
			require.Equal(t, tc.expected, result)
		})
	}
}


File: /client\firewall_filter.go
package client

import (
	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/go-routeros/routeros"
)

// FirewallFilterRule defines /ip/firewall/filter rule
type FirewallFilterRule struct {
	Id               string             `mikrotik:".id" codegen:"id,mikrotikID,terraformID"`
	Action           string             `mikrotik:"action" codegen:"action"`
	Chain            string             `mikrotik:"chain" codegen:"chain,required"`
	Comment          string             `mikrotik:"comment" codegen:"comment"`
	ConnectionState  types.MikrotikList `mikrotik:"connection-state" codegen:"connection_state"`
	DestPort         string             `mikrotik:"dst-port" codegen:"dst_port"`
	InInterface      string             `mikrotik:"in-interface" codegen:"in_interface"`
	InInterfaceList  string             `mikrotik:"in-interface-list" codegen:"in_interface_list"`
	OutInterfaceList string             `mikrotik:"out-interface-list" codegen:"out_interface_list"`
	Protocol         string             `mikrotik:"protocol" codegen:"protocol"`
}

var _ Resource = (*FirewallFilterRule)(nil)

func (b *FirewallFilterRule) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/ip/firewall/filter/add",
		Find:   "/ip/firewall/filter/print",
		Update: "/ip/firewall/filter/set",
		Delete: "/ip/firewall/filter/remove",
	}[a]
}

func (b *FirewallFilterRule) IDField() string {
	return ".id"
}

func (b *FirewallFilterRule) ID() string {
	return b.Id
}

func (b *FirewallFilterRule) SetID(id string) {
	b.Id = id
}

func (b *FirewallFilterRule) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (c Mikrotik) AddFirewallFilterRule(r *FirewallFilterRule) (*FirewallFilterRule, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*FirewallFilterRule), nil
}

func (c Mikrotik) UpdateFirewallFilterRule(r *FirewallFilterRule) (*FirewallFilterRule, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*FirewallFilterRule), nil
}

func (c Mikrotik) FindFirewallFilterRule(id string) (*FirewallFilterRule, error) {
	res, err := c.Find(&FirewallFilterRule{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*FirewallFilterRule), nil
}

func (c Mikrotik) DeleteFirewallFilterRule(id string) error {
	return c.Delete(&FirewallFilterRule{Id: id})
}


File: /client\firewall_filter_test.go
package client

import (
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestFirewallFilter_customChain(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	rule := &FirewallFilterRule{
		Chain:           "mychain",
		Comment:         "Test rule",
		DestPort:        "1001",
		ConnectionState: types.MikrotikList{"new"},
		Protocol:        "tcp",
	}

	createdRule, err := c.AddFirewallFilterRule(rule)
	require.NoError(t, err)

	defer func(id string) {
		assert.NoError(t, c.DeleteFirewallFilterRule(id))
	}(createdRule.Id)

	rule.Id = createdRule.Id

	foundRule, err := c.FindFirewallFilterRule(createdRule.Id)
	require.NoError(t, err)
	assert.Equal(t, rule, foundRule)
}

func TestFirewallFilter_builtinChain(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	rule := &FirewallFilterRule{
		Chain:           "filter",
		Comment:         "Test rule for builtin chain",
		DestPort:        "1001",
		ConnectionState: types.MikrotikList{"established", "related"},
		Protocol:        "tcp",
	}

	createdRule, err := c.AddFirewallFilterRule(rule)
	require.NoError(t, err)

	defer func(id string) {
		assert.NoError(t, c.DeleteFirewallFilterRule(id))
	}(createdRule.Id)

	rule.Id = createdRule.Id

	foundRule, err := c.FindFirewallFilterRule(rule.Id)
	require.NoError(t, err)
	assert.Equal(t, rule, foundRule)

	rule.Protocol = "udp"
	rule.Comment = "Updated protocol"
	_, err = c.UpdateFirewallFilterRule(rule)
	require.NoError(t, err)

	foundRule, err = c.FindFirewallFilterRule(rule.Id)
	require.NoError(t, err)
	assert.Equal(t, rule, foundRule)
}


File: /client\go.mod
module github.com/ddelnano/terraform-provider-mikrotik/client

go 1.18

require (
	github.com/go-routeros/routeros v0.0.0-20210123142807-2a44d57c6730
	github.com/stretchr/testify v1.8.0
)

require (
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)


File: /client\go.sum
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/go-routeros/routeros v0.0.0-20210123142807-2a44d57c6730 h1:EuqwWLv/LPPjhvFqkeD2bz+FOlvw2DjvDI7vK8GVeyY=
github.com/go-routeros/routeros v0.0.0-20210123142807-2a44d57c6730/go.mod h1:em1mEqFKnoeQuQP9Sg7i26yaW8o05WwcNj7yLhrXxSQ=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.4.0/go.mod h1:YvHI0jy2hoMjB+UWwv71VJQ9isScKT/TqJzVSSt89Yw=
github.com/stretchr/testify v1.7.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.8.0 h1:pSgiaMZlXftHpm5L7V1+rVB+AZJydKsMxsQBIJw4PKk=
github.com/stretchr/testify v1.8.0/go.mod h1:yNjHg4UonilssWZ8iaSj1OCr/vHnekPRkoO+kdMU+MU=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405 h1:yhCVgyC4o1eVCa2tZl7eS0r+SDo693bJlVdllGtEeKM=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=


File: /client\helpers.go
package client

import (
	"errors"
	"strconv"
	"testing"
	"time"
)

func getRouterOSMajorVersion(systemResources SystemResources) (majorVersion int, err error) {
	if len(systemResources.Version) == 0 {
		return 0, errors.New("RouterOS system resources returned empty string")
	}
	majorVersion, err = strconv.Atoi(string(systemResources.Version[0]))
	return
}

func SkipIfRouterOSV6OrEarlier(t *testing.T, systemResources SystemResources) {
	majorVersion, err := getRouterOSMajorVersion(systemResources)
	if err != nil {
		t.Errorf("failed to get the system resource major version: %v", err)
	}
	if majorVersion <= 6 {
		t.Skip()
	}
}

func SkipIfRouterOSV7OrLater(t *testing.T, systemResources SystemResources) {
	majorVersion, err := getRouterOSMajorVersion(systemResources)
	if err != nil {
		t.Errorf("failed to get the system resource major version: %v", err)
	}
	if majorVersion >= 7 {
		t.Skip()
	}
}

// RandomString returns a random string
func RandomString() string {
	// a naive implementation with all-digits for now
	return strconv.FormatInt(time.Now().UTC().UnixNano(), 10)
}


File: /client\interface_list.go
package client

import (
	"github.com/go-routeros/routeros"
)

// InterfaceList manages a list of interfaces
type InterfaceList struct {
	Id      string `mikrotik:".id" codegen:"id,mikrotikID"`
	Comment string `mikrotik:"comment" codegen:"comment"`
	Name    string `mikrotik:"name" codegen:"name,terraformID,required"`
}

var _ Resource = (*InterfaceList)(nil)

func (b *InterfaceList) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/interface/list/add",
		Find:   "/interface/list/print",
		Update: "/interface/list/set",
		Delete: "/interface/list/remove",
	}[a]
}

func (b *InterfaceList) IDField() string {
	return ".id"
}

func (b *InterfaceList) ID() string {
	return b.Id
}

func (b *InterfaceList) SetID(id string) {
	b.Id = id
}

// Uncomment extra methods to satisfy more interfaces

func (b *InterfaceList) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (b *InterfaceList) FindField() string {
	return "name"
}

func (b *InterfaceList) FindFieldValue() string {
	return b.Name
}

func (b *InterfaceList) DeleteField() string {
	return "numbers"
}

func (b *InterfaceList) DeleteFieldValue() string {
	return b.Name
}

// Typed wrappers
func (c Mikrotik) AddInterfaceList(r *InterfaceList) (*InterfaceList, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceList), nil
}

func (c Mikrotik) UpdateInterfaceList(r *InterfaceList) (*InterfaceList, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceList), nil
}

func (c Mikrotik) FindInterfaceList(name string) (*InterfaceList, error) {
	res, err := c.Find(&InterfaceList{Name: name})
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceList), nil
}

func (c Mikrotik) DeleteInterfaceList(name string) error {
	return c.Delete(&InterfaceList{Name: name})
}


File: /client\interface_list_member.go
package client

import (
	"github.com/go-routeros/routeros"
)

// InterfaceListMember manages an interface list's members
type InterfaceListMember struct {
	Id        string `mikrotik:".id" codegen:"id,mikrotikID"`
	Interface string `mikrotik:"interface" codegen:"interface,required"`
	List      string `mikrotik:"list" codegen:"list,required"`
}

var _ Resource = (*InterfaceListMember)(nil)

func (b *InterfaceListMember) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/interface/list/member/add",
		Find:   "/interface/list/member/print",
		Update: "/interface/list/member/set",
		Delete: "/interface/list/member/remove",
	}[a]
}

func (b *InterfaceListMember) IDField() string {
	return ".id"
}

func (b *InterfaceListMember) ID() string {
	return b.Id
}

func (b *InterfaceListMember) SetID(id string) {
	b.Id = id
}

func (b *InterfaceListMember) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (b *InterfaceListMember) DeleteField() string {
	return "numbers"
}

func (b *InterfaceListMember) DeleteFieldValue() string {
	return b.Id
}

// Typed wrappers
func (c Mikrotik) AddInterfaceListMember(r *InterfaceListMember) (*InterfaceListMember, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceListMember), nil
}

func (c Mikrotik) UpdateInterfaceListMember(r *InterfaceListMember) (*InterfaceListMember, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceListMember), nil
}

func (c Mikrotik) FindInterfaceListMember(id string) (*InterfaceListMember, error) {
	res, err := c.Find(&InterfaceListMember{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceListMember), nil
}

func (c Mikrotik) DeleteInterfaceListMember(id string) error {
	return c.Delete(&InterfaceListMember{Id: id})
}


File: /client\interface_list_member_test.go
package client

import "testing"

func TestAddInterfaceListMemberUpdateAndDelete(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	listName := "test_list"

	list, err := c.AddInterfaceList(&InterfaceList{
		Name: listName,
	})
	if err != nil {
		t.Fatal(err)
	}
	defer func() {
		if err := c.DeleteInterfaceList(list.Id); err != nil {
			t.Error(err)
		}
	}()

	listMember, err := c.AddInterfaceListMember(&InterfaceListMember{
		List:      list.Name,
		Interface: "*0",
	})
	if err != nil {
		t.Fatal(err)
	}
	defer func() {
		if err := c.DeleteInterfaceListMember(listMember.Id); err != nil {
			t.Error(err)
		}
		if m, err := c.FindInterfaceListMember(listMember.Id); err == nil || m != nil {
			t.Errorf("expected error to be present and list member to be nil")
		}
	}()

	found, err := c.FindInterfaceListMember(listMember.Id)
	if err != nil {
		t.Fatal(err)
	}

	if found.List != list.Name {
		t.Errorf("expected name to be %q, got %q", list.Name, found.List)
	}

	listMember.Interface = "ether1"
	updated, err := c.UpdateInterfaceListMember(listMember)
	if err != nil {
		t.Error(err)
	}

	if updated.Interface != "ether1" {
		t.Errorf("expected updated interface to be %q, got %q", listMember.Interface, updated.Interface)
	}
}


File: /client\interface_list_test.go
package client

import "testing"

func TestAddInterfaceListUpdateAndDelete(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	list, err := c.AddInterfaceList(&InterfaceList{
		Name:    "mylist",
		Comment: "Created by terraform",
	})
	if err != nil {
		t.Fatal(err)
	}

	found, err := c.FindInterfaceList(list.Name)
	if err != nil {
		t.Fatal(err)
	}

	if found.Name != list.Name {
		t.Errorf("expected name to be %q, got %q", list.Name, found.Name)
	}

	list.Comment = "updated list"
	updated, err := c.UpdateInterfaceList(list)
	if err != nil {
		t.Error(err)
	}

	if updated.Comment != "updated list" {
		t.Errorf("expected comment to be %q, got %q", list.Comment, updated.Comment)
	}

	// cleanup
	if err := c.DeleteInterfaceList(list.Name); err != nil {
		t.Error(err)
	}

	_, err = c.FindInterfaceList(list.Name)
	if err == nil {
		t.Error("expected error, got nil")
	}
}


File: /client\interface_wireguard.go
package client

import (
	"github.com/go-routeros/routeros"
)

type InterfaceWireguard struct {
	Id         string `mikrotik:".id"`
	Name       string `mikrotik:"name"`
	Comment    string `mikrotik:"comment"`
	Disabled   bool   `mikrotik:"disabled"`
	ListenPort int    `mikrotik:"listen-port"`
	Mtu        int    `mikrotik:"mtu"`
	PrivateKey string `mikrotik:"private-key"`
	PublicKey  string `mikrotik:"public-key,readonly"` //read only property
	Running    bool   `mikrotik:"running,readonly"`    //read only property
}

func (i *InterfaceWireguard) ActionToCommand(action Action) string {
	return map[Action]string{
		Add:    "/interface/wireguard/add",
		Find:   "/interface/wireguard/print",
		List:   "/interface/wireguard/print",
		Update: "/interface/wireguard/set",
		Delete: "/interface/wireguard/remove",
	}[action]
}

func (i *InterfaceWireguard) IDField() string {
	return ".id"
}

func (i *InterfaceWireguard) ID() string {
	return i.Id
}

func (i *InterfaceWireguard) SetID(id string) {
	i.Id = id
}

func (i *InterfaceWireguard) AfterAddHook(r *routeros.Reply) {
	i.Id = r.Done.Map["ret"]
}

func (i *InterfaceWireguard) FindField() string {
	return "name"
}

func (i *InterfaceWireguard) FindFieldValue() string {
	return i.Name
}

func (i *InterfaceWireguard) DeleteField() string {
	return "numbers"
}

func (i *InterfaceWireguard) DeleteFieldValue() string {
	return i.Name
}

func (client Mikrotik) AddInterfaceWireguard(i *InterfaceWireguard) (*InterfaceWireguard, error) {
	res, err := client.Add(i)
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceWireguard), nil
}

func (client Mikrotik) FindInterfaceWireguard(name string) (*InterfaceWireguard, error) {
	res, err := client.Find(&InterfaceWireguard{Name: name})
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceWireguard), nil
}

func (client Mikrotik) UpdateInterfaceWireguard(i *InterfaceWireguard) (*InterfaceWireguard, error) {
	res, err := client.Update(i)
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceWireguard), nil
}

func (client Mikrotik) DeleteInterfaceWireguard(name string) error {
	return client.Delete(&InterfaceWireguard{Name: name})
}


File: /client\interface_wireguard_peer.go
package client

import (
	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/go-routeros/routeros"
)

type InterfaceWireguardPeer struct {
	Id                  string                 `mikrotik:".id"`
	AllowedAddress      string                 `mikrotik:"allowed-address"`
	Comment             string                 `mikrotik:"comment"`
	Disabled            bool                   `mikrotik:"disabled"`
	EndpointAddress     string                 `mikrotik:"endpoint-address"`
	EndpointPort        int64                  `mikrotik:"endpoint-port"`
	Interface           string                 `mikrotik:"interface"`
	PersistentKeepalive types.MikrotikDuration `mikrotik:"persistent-keepalive"`
	PresharedKey        string                 `mikrotik:"preshared-key"`
	PublicKey           string                 `mikrotik:"public-key"`
}

func (i *InterfaceWireguardPeer) ActionToCommand(action Action) string {
	return map[Action]string{
		Add:    "/interface/wireguard/peers/add",
		Find:   "/interface/wireguard/peers/print",
		List:   "/interface/wireguard/peers/print",
		Update: "/interface/wireguard/peers/set",
		Delete: "/interface/wireguard/peers/remove",
	}[action]
}

func (i *InterfaceWireguardPeer) IDField() string {
	return ".id"
}

func (i *InterfaceWireguardPeer) ID() string {
	return i.Id
}

func (i *InterfaceWireguardPeer) SetID(id string) {
	i.Id = id
}

func (i *InterfaceWireguardPeer) AfterAddHook(r *routeros.Reply) {
	i.Id = r.Done.Map["ret"]
}

func (i *InterfaceWireguardPeer) DeleteField() string {
	return "numbers"
}

func (i *InterfaceWireguardPeer) DeleteFieldValue() string {
	return i.Id
}

func (client Mikrotik) AddInterfaceWireguardPeer(i *InterfaceWireguardPeer) (*InterfaceWireguardPeer, error) {
	res, err := client.Add(i)
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceWireguardPeer), nil
}

func (client Mikrotik) FindInterfaceWireguardPeer(id string) (*InterfaceWireguardPeer, error) {
	res, err := client.Find(&InterfaceWireguardPeer{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceWireguardPeer), nil
}

func (client Mikrotik) UpdateInterfaceWireguardPeer(i *InterfaceWireguardPeer) (*InterfaceWireguardPeer, error) {
	res, err := client.Update(i)
	if err != nil {
		return nil, err
	}

	return res.(*InterfaceWireguardPeer), nil
}

func (client Mikrotik) DeleteInterfaceWireguardPeer(id string) error {
	return client.Delete(&InterfaceWireguardPeer{Id: id})
}


File: /client\interface_wireguard_peer_test.go
package client

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestFindInterfaceWireguardPeer_onNonExistantInterfacePeer(t *testing.T) {
	SkipIfRouterOSV6OrEarlier(t, sysResources)
	c := NewClient(GetConfigFromEnv())

	peerID := "Interface peer does not exist"
	_, err := c.FindInterfaceWireguardPeer(peerID)

	require.Truef(t, IsNotFoundError(err),
		"Expecting to receive NotFound error for Interface peer `%q`, instead error was nil.", peerID)
}

func TestInterfaceWireguardPeer_Crud(t *testing.T) {
	SkipIfRouterOSV6OrEarlier(t, sysResources)
	c := NewClient(GetConfigFromEnv())

	name := "new_interface_wireguard"
	interfaceWireguard := &InterfaceWireguard{
		Name:       name,
		Disabled:   false,
		ListenPort: 10000,
		Mtu:        10001,
		PrivateKey: "YOi0P0lTTiN8hAQvuRET23Srb+U7C52iOZokj0CCSkM=",
		Comment:    "new interface from test",
	}

	createdInterface, err := c.Add(interfaceWireguard)
	if err != nil {
		t.Errorf("expected no error, got %v", err)
		return
	}
	defer func() {
		err = c.Delete(interfaceWireguard)
		if err != nil {
			t.Errorf("expected no error, got %v", err)
		}
	}()

	interfaceWireguardPeer := &InterfaceWireguardPeer{
		Interface:      createdInterface.(*InterfaceWireguard).Name,
		Disabled:       false,
		AllowedAddress: "0.0.0.0/0",
		EndpointPort:   13250,
		Comment:        "new interface from test",
		PublicKey:      "/yZWgiYAgNNSy7AIcxuEewYwOVPqJJRKG90s9ypwfiM=",
	}

	created, err := c.Add(interfaceWireguardPeer)
	require.NoError(t, err)
	defer func() {
		err = c.Delete(interfaceWireguardPeer)
		assert.NoError(t, err)
	}()

	findPeer := &InterfaceWireguardPeer{}
	findPeer.Id = created.(*InterfaceWireguardPeer).Id
	foundPeer, err := c.Find(findPeer)
	require.NoError(t, err)

	assert.Equal(t, created, foundPeer)
}


File: /client\interface_wireguard_test.go
package client

import (
	"reflect"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestFindInterfaceWireguard_onNonExistantInterfaceWireguard(t *testing.T) {
	SkipIfRouterOSV6OrEarlier(t, sysResources)
	c := NewClient(GetConfigFromEnv())

	name := "Interface wireguard does not exist"
	_, err := c.FindInterfaceWireguard(name)

	require.Truef(t, IsNotFoundError(err),
		"Expecting to receive NotFound error for Interface wireguard %q.", name)
}

func TestAddFindDeleteInterfaceWireguard(t *testing.T) {
	SkipIfRouterOSV6OrEarlier(t, sysResources)
	c := NewClient(GetConfigFromEnv())

	name := "new_interface_wireguard"
	interfaceWireguard := &InterfaceWireguard{
		Name:       name,
		Disabled:   false,
		ListenPort: 10000,
		Mtu:        10001,
		PrivateKey: "YOi0P0lTTiN8hAQvuRET23Srb+U7C52iOZokj0CCSkM=",
		Comment:    "new interface from test",
	}

	created, err := c.Add(interfaceWireguard)
	if err != nil {
		t.Errorf("expected no error, got %v", err)
		return
	}
	defer func() {
		err = c.Delete(interfaceWireguard)
		require.NoError(t, err)

		_, err := c.Find(interfaceWireguard)
		require.True(t, IsNotFoundError(err), "expected to get NotFound error")
	}()

	findInterface := &InterfaceWireguard{}
	findInterface.Name = name
	found, err := c.Find(findInterface)
	if err != nil {
		t.Errorf("expected no error, got %v", err)
		return
	}

	if _, ok := found.(Resource); !ok {
		t.Error("expected found resource to implement Resource interface, but it doesn't")
		return
	}
	if !reflect.DeepEqual(created, found) {
		t.Error("expected created and found resources to be equal, but they don't")
	}
}


File: /client\ipv6_addr.go
package client

import (
	"github.com/go-routeros/routeros"
)

// Ipv6Address defines resource
type Ipv6Address struct {
	Id        string `mikrotik:".id" codegen:"id,mikrotikID,terraformID"`
	Address   string `mikrotik:"address" codegen:"address,required"`
	Advertise bool   `mikrotik:"advertise" codegen:"advertise"`
	Comment   string `mikrotik:"comment" codegen:"comment"`
	Disabled  bool   `mikrotik:"disabled" codegen:"disabled"`
	Eui64     bool   `mikrotik:"eui-64" codegen:"eui_64"`
	FromPool  string `mikrotik:"from-pool" codegen:"from_pool"`
	Interface string `mikrotik:"interface" codegen:"interface,required"`
	NoDad     bool   `mikrotik:"no-dad" codegen:"no_dad"`
}

var _ Resource = (*Ipv6Address)(nil)

func (b *Ipv6Address) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/ipv6/address/add",
		Find:   "/ipv6/address/print",
		Update: "/ipv6/address/set",
		Delete: "/ipv6/address/remove",
	}[a]
}

func (b *Ipv6Address) IDField() string {
	return ".id"
}

func (b *Ipv6Address) ID() string {
	return b.Id
}

func (b *Ipv6Address) SetID(id string) {
	b.Id = id
}

func (b *Ipv6Address) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

// Typed wrappers
func (c Mikrotik) AddIpv6Address(r *Ipv6Address) (*Ipv6Address, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*Ipv6Address), nil
}

func (c Mikrotik) UpdateIpv6Address(r *Ipv6Address) (*Ipv6Address, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*Ipv6Address), nil
}

func (c Mikrotik) ListIpv6Address() ([]Ipv6Address, error) {
	res, err := c.List(&Ipv6Address{})
	if err != nil {
		return nil, err
	}
	returnSlice := make([]Ipv6Address, len(res))
	for i, v := range res {
		returnSlice[i] = *(v.(*Ipv6Address))
	}

	return returnSlice, nil
}

func (c Mikrotik) FindIpv6Address(id string) (*Ipv6Address, error) {
	res, err := c.Find(&Ipv6Address{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*Ipv6Address), nil
}

func (c Mikrotik) DeleteIpv6Address(id string) error {
	return c.Delete(&Ipv6Address{Id: id})
}


File: /client\ipv6_addr_test.go
package client

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestAddIpv6AddressAndDeleteIpv6Address(t *testing.T) {
	SkipIfRouterOSV6OrEarlier(t, sysResources)
	c := NewClient(GetConfigFromEnv())

	address := "1:1:1:1:1:1:1:1/64"
	comment := "terraform-acc-test"
	disabled := false
	ifname := "ether1"
	updatedComment := "terraform acc test updated"

	expectedIpv6Address := &Ipv6Address{
		Address:   address,
		Comment:   comment,
		Disabled:  disabled,
		Interface: ifname,
	}

	ipv6addr, err := c.AddIpv6Address(expectedIpv6Address)
	require.NoError(t, err)

	expectedIpv6Address.Id = ipv6addr.Id
	assert.Equal(t, expectedIpv6Address, ipv6addr)

	expectedIpv6Address.Comment = updatedComment
	ipv6addr, err = c.UpdateIpv6Address(expectedIpv6Address)
	require.NoError(t, err)
	assert.Equal(t, expectedIpv6Address, ipv6addr)

	foundIpv6Address, err := c.FindIpv6Address(ipv6addr.Id)
	require.NoError(t, err)
	assert.Equal(t, ipv6addr, foundIpv6Address)

	err = c.DeleteIpv6Address(ipv6addr.Id)
	assert.NoError(t, err)
}


File: /client\ip_addr.go
package client

import (
	"github.com/go-routeros/routeros"
)

type IpAddress struct {
	Id        string `mikrotik:".id" codegen:"id,mikrotikID"`
	Address   string `mikrotik:"address" codegen:"address,required"`
	Comment   string `mikrotik:"comment" codegen:"comment"`
	Disabled  bool   `mikrotik:"disabled" codegen:"disabled"`
	Interface string `mikrotik:"interface" codegen:"interface,required"`
	Network   string `mikrotik:"network" codegen:"network,computed"`
}

var _ Resource = (*IpAddress)(nil)

func (b *IpAddress) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/ip/address/add",
		Find:   "/ip/address/print",
		Update: "/ip/address/set",
		Delete: "/ip/address/remove",
	}[a]
}

func (b *IpAddress) IDField() string {
	return ".id"
}

func (b *IpAddress) ID() string {
	return b.Id
}

func (b *IpAddress) SetID(id string) {
	b.Id = id
}

func (b *IpAddress) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

// Typed wrappers
func (c Mikrotik) AddIpAddress(r *IpAddress) (*IpAddress, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*IpAddress), nil
}

func (c Mikrotik) UpdateIpAddress(r *IpAddress) (*IpAddress, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*IpAddress), nil
}

func (c Mikrotik) FindIpAddress(id string) (*IpAddress, error) {
	res, err := c.Find(&IpAddress{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*IpAddress), nil
}

func (client Mikrotik) ListIpAddress() ([]IpAddress, error) {
	res, err := client.List(&IpAddress{})
	if err != nil {
		return nil, err
	}
	returnSlice := make([]IpAddress, len(res))
	for i, v := range res {
		returnSlice[i] = *(v.(*IpAddress))
	}

	return returnSlice, nil
}

func (c Mikrotik) DeleteIpAddress(id string) error {
	return c.Delete(&IpAddress{Id: id})
}


File: /client\ip_addr_test.go
package client

import (
	"reflect"
	"testing"
)

func TestAddIpAddressAndDeleteIpAddress(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	address := "1.1.1.1/24"
	comment := "terraform-acc-test"
	disabled := false
	network := "1.1.1.0"
	ifname := "ether1"
	updatedComment := "terraform acc test updated"

	expectedIpAddress := &IpAddress{
		Address:   address,
		Comment:   comment,
		Disabled:  disabled,
		Interface: ifname,
		Network:   network,
	}

	ipaddr, err := c.AddIpAddress(expectedIpAddress)

	if err != nil {
		t.Errorf("Error creating an ip address with: %v", err)
	}

	expectedIpAddress.Id = ipaddr.Id

	if !reflect.DeepEqual(ipaddr, expectedIpAddress) {
		t.Errorf("The ip address does not match what we expected. actual: %v expected: %v", ipaddr, expectedIpAddress)
	}

	expectedIpAddress.Comment = updatedComment
	ipaddr, err = c.UpdateIpAddress(expectedIpAddress)

	if err != nil {
		t.Errorf("Error updating an ip address with: %v", err)
	}
	if !reflect.DeepEqual(ipaddr, expectedIpAddress) {
		t.Errorf("The ip address does not match what we expected. actual: %v expected: %v", ipaddr, expectedIpAddress)
	}

	foundIpAddress, err := c.FindIpAddress(ipaddr.Id)

	if err != nil {
		t.Errorf("Error getting ip address with: %v", err)
	}

	if !reflect.DeepEqual(ipaddr, foundIpAddress) {
		t.Errorf("Created ip address and found ip address do not match. actual: %v expected: %v", foundIpAddress, ipaddr)
	}

	err = c.DeleteIpAddress(ipaddr.Id)

	if err != nil {
		t.Errorf("Error deleting ip address with: %v", err)
	}
}


File: /client\lease.go
package client

import (
	"log"

	"github.com/go-routeros/routeros"
)

type DhcpLease struct {
	Id          string `mikrotik:".id" codegen:"id,mikrotikID,terraformID"`
	Address     string `mikrotik:"address" codegen:"address,required"`
	MacAddress  string `mikrotik:"mac-address" codegen:"macaddress,required"`
	Comment     string `mikrotik:"comment" codegen:"comment"`
	BlockAccess bool   `mikrotik:"block-access" codegen:"blocked"`
	Dynamic     bool   `mikrotik:"dynamic,readonly" codegen:"dynamic,computed"` // TODO:  don't see this listed as a param https://wiki.mikrotik.com/wiki/Manual:IP/DHCP_Server, but our docs list it as one
	Hostname    string `mikrotik:"host-name,readonly" codegen:"hostname,computed"`
}

func (client Mikrotik) ListDhcpLeases() ([]DhcpLease, error) {
	c, err := client.getMikrotikClient()

	if err != nil {
		return nil, err
	}
	cmd := []string{"/ip/dhcp-server/lease/print"}
	log.Printf("[INFO] Running the mikrotik command: `%s`", cmd)
	r, err := c.RunArgs(cmd)

	if err != nil {
		return nil, err
	}
	log.Printf("[DEBUG] Found dhcp leases: %v", r)

	leases := []DhcpLease{}

	err = Unmarshal(*r, &leases)

	if err != nil {
		return nil, err
	}

	return leases, nil
}

var _ Resource = (*DhcpLease)(nil)

func (b *DhcpLease) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/ip/dhcp-server/lease/add",
		Find:   "/ip/dhcp-server/lease/print",
		Update: "/ip/dhcp-server/lease/set",
		Delete: "/ip/dhcp-server/lease/remove",
	}[a]
}

func (b *DhcpLease) IDField() string {
	return ".id"
}

func (b *DhcpLease) ID() string {
	return b.Id
}

func (b *DhcpLease) SetID(id string) {
	b.Id = id
}

func (b *DhcpLease) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

// Typed wrappers
func (c Mikrotik) AddDhcpLease(r *DhcpLease) (*DhcpLease, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*DhcpLease), nil
}

func (c Mikrotik) UpdateDhcpLease(r *DhcpLease) (*DhcpLease, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*DhcpLease), nil
}

func (c Mikrotik) FindDhcpLease(id string) (*DhcpLease, error) {
	res, err := c.Find(&DhcpLease{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*DhcpLease), nil
}

func (client Mikrotik) ListDhcpLease() ([]DhcpLease, error) {
	res, err := client.List(&DhcpLease{})
	if err != nil {
		return nil, err
	}
	returnSlice := make([]DhcpLease, len(res))
	for i, v := range res {
		returnSlice[i] = *(v.(*DhcpLease))
	}

	return returnSlice, nil
}

func (c Mikrotik) DeleteDhcpLease(id string) error {
	return c.Delete(&DhcpLease{Id: id})
}


File: /client\lease_test.go
package client

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestAddLeaseAndDeleteLease(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	address := "1.1.1.1"
	macaddress := "11:11:11:11:11:11"
	comment := "terraform-acc-test"
	blocked := false
	updatedMacaddress := "11:11:11:11:11:12"
	updatedComment := "terraform acc test updated"

	expectedLease := &DhcpLease{
		Address:     address,
		MacAddress:  macaddress,
		Comment:     comment,
		BlockAccess: blocked,
	}
	lease, err := c.AddDhcpLease(expectedLease)
	require.NoError(t, err)

	expectedLease.Id = lease.Id
	assert.Equal(t, expectedLease, lease)

	expectedLease.Comment = updatedComment
	expectedLease.MacAddress = updatedMacaddress

	lease, err = c.UpdateDhcpLease(expectedLease)
	assert.NoError(t, err)
	assert.Equal(t, expectedLease, lease)

	foundLease, err := c.FindDhcpLease(lease.Id)
	assert.NoError(t, err)
	assert.Equal(t, lease, foundLease)

	err = c.DeleteDhcpLease(lease.Id)
	assert.NoError(t, err)
}

func TestFindDhcpLease_forNonExistantLease(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	leaseId := "Invalid id"
	_, err := c.FindDhcpLease(leaseId)

	assert.Error(t, err)
	assert.True(t, IsNotFoundError(err), "expected error to be of NotFound type")
}


File: /client\pool.go
package client

import (
	"github.com/go-routeros/routeros"
)

type Pool struct {
	Id       string `mikrotik:".id" codegen:"id,mikrotikID,terraformID"`
	Name     string `mikrotik:"name" codegen:"name,required"`
	Ranges   string `mikrotik:"ranges" codegen:"ranges,required"`
	NextPool string `mikrotik:"next-pool" codegen:"next_pool,optiona,computed"`
	Comment  string `mikrotik:"comment" codegen:"comment,optional,computed"`
}

var _ Resource = (*Pool)(nil)

func (b *Pool) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/ip/pool/add",
		Find:   "/ip/pool/print",
		Update: "/ip/pool/set",
		Delete: "/ip/pool/remove",
	}[a]
}

func (b *Pool) IDField() string {
	return ".id"
}

func (b *Pool) ID() string {
	return b.Id
}

func (b *Pool) SetID(id string) {
	b.Id = id
}

func (b *Pool) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

// Typed wrappers
func (c Mikrotik) AddPool(r *Pool) (*Pool, error) {
	return r.processResourceErrorTuplePtr(c.Add(r))
}

func (c Mikrotik) UpdatePool(r *Pool) (*Pool, error) {
	return r.processResourceErrorTuplePtr(c.Update(r))
}

func (c Mikrotik) FindPool(id string) (*Pool, error) {
	return Pool{}.processResourceErrorTuplePtr(c.Find(&Pool{Id: id}))
}

func (c Mikrotik) FindPoolByName(name string) (*Pool, error) {
	return Pool{}.processResourceErrorTuplePtr(c.findByField(&Pool{}, "name", name))
}

func (c Mikrotik) DeletePool(id string) error {
	return c.Delete(&Pool{Id: id})
}

func (c Mikrotik) ListPools() ([]Pool, error) {
	res, err := c.List(&Pool{})
	if err != nil {
		return nil, err
	}
	returnSlice := make([]Pool, len(res))
	for i, v := range res {
		returnSlice[i] = *(v.(*Pool))
	}
	return returnSlice, nil
}

func (b Pool) processResourceErrorTuplePtr(r Resource, err error) (*Pool, error) {
	if err != nil {
		return nil, err
	}
	return r.(*Pool), nil
}


File: /client\pool_test.go
package client

import (
	"reflect"
	"testing"

	"github.com/stretchr/testify/require"
)

func TestAddUpdateAndDeletePool(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	expectedPool := &Pool{
		Name:    "pool-" + RandomString(),
		Ranges:  "172.16.0.1-172.16.0.8,172.16.0.10",
		Comment: "pool comment",
	}
	pool, err := c.AddPool(expectedPool)

	if err != nil {
		t.Fatalf("Error creating a pool with: %v", err)
	}

	expectedPool.Id = pool.Id
	if !reflect.DeepEqual(pool, expectedPool) {
		t.Errorf("The pool does not match what we expected. actual: %v expected: %v", pool, expectedPool)
	}

	expectedPool.Comment = "updated comment"
	expectedPool.Ranges = "172.16.0.1-172.16.0.8,172.16.0.16"
	pool, err = c.UpdatePool(expectedPool)

	if err != nil {
		t.Errorf("Error updating pool with: %v", err)
	}

	if !reflect.DeepEqual(pool, expectedPool) {
		t.Errorf("Updated pool does not match the expected: %v expected: %v", expectedPool, pool)
	}

	err = c.DeletePool(pool.Id)

	if err != nil {
		t.Errorf("Error deleting pool with: %v", err)
	}
}

func TestFindPool_forNonExistingPool(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	poolId := "Invalid id"
	_, err := c.FindPool(poolId)

	require.Truef(t, IsNotFoundError(err), "client should have NotFound error error but instead received")
}

func TestFindPoolByName_forExistingPool(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	p := &Pool{
		Name:    "pool-" + RandomString(),
		Ranges:  "172.16.0.1-172.16.0.8,172.16.0.10",
		Comment: "existing pool",
	}
	pool, err := c.AddPool(p)

	expectedPool, err := c.FindPoolByName(pool.Name)
	if err != nil {
		t.Fatalf("Error finding pool by name with: %v", err)
	}
	if pool.Name != expectedPool.Name {
		t.Errorf("The pool Name fields do not match. actual: %v expected: %v", pool.Name, expectedPool.Name)
	}
	c.DeletePool(pool.Id)
}

func TestFindPoolByName_forNonExistingPool(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	poolName := "Invalid name"
	_, err := c.FindPoolByName(poolName)

	require.True(t, IsNotFoundError(err),
		"client should have NotFound error")
}


File: /client\resource_wrappers.go
package client

import "reflect"

type (
	// FindByFieldWrapper changes the fields used to find the remote resource.
	FindByFieldWrapper struct {
		Resource
		field          string
		fieldValueFunc func() string
	}
)

var (
	_ Finder   = (*FindByFieldWrapper)(nil)
	_ Resource = (*FindByFieldWrapper)(nil)
)

func (fw FindByFieldWrapper) FindField() string {
	return fw.field
}

func (fw FindByFieldWrapper) FindFieldValue() string {
	return fw.fieldValueFunc()
}

// Create satisfies ResourceInstanceCreator interface and returns new object of the wrapped resource.
func (fw FindByFieldWrapper) Create() Resource {
	reflectNew := reflect.New(reflect.Indirect(reflect.ValueOf(fw.Resource)).Type())

	return reflectNew.Interface().(Resource)
}


File: /client\scheduler.go
package client

import (
	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/go-routeros/routeros"
)

type Scheduler struct {
	Id        string                 `mikrotik:".id"`
	Name      string                 `mikrotik:"name"`
	OnEvent   string                 `mikrotik:"on-event"`
	StartDate string                 `mikrotik:"start-date"`
	StartTime string                 `mikrotik:"start-time"`
	Interval  types.MikrotikDuration `mikrotik:"interval"`
}

var _ Resource = (*Scheduler)(nil)

func (b *Scheduler) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/system/scheduler/add",
		Find:   "/system/scheduler/print",
		Update: "/system/scheduler/set",
		Delete: "/system/scheduler/remove",
	}[a]
}

func (b *Scheduler) IDField() string {
	return ".id"
}

func (b *Scheduler) ID() string {
	return b.Id
}

func (b *Scheduler) SetID(id string) {
	b.Id = id
}

func (b *Scheduler) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (b *Scheduler) FindField() string {
	return "name"
}

func (b *Scheduler) FindFieldValue() string {
	return b.Name
}

func (b *Scheduler) DeleteField() string {
	return "numbers"
}

func (b *Scheduler) DeleteFieldValue() string {
	return b.Id
}

// typed wrappers
func (client Mikrotik) AddScheduler(s *Scheduler) (*Scheduler, error) {
	return client.CreateScheduler(s)
}

func (client Mikrotik) CreateScheduler(s *Scheduler) (*Scheduler, error) {
	r, err := client.Add(s)
	if err != nil {
		return nil, err
	}

	return r.(*Scheduler), nil
}

func (client Mikrotik) UpdateScheduler(s *Scheduler) (*Scheduler, error) {
	r, err := client.Update(s)
	if err != nil {
		return nil, err
	}

	return r.(*Scheduler), nil
}

func (client Mikrotik) FindScheduler(name string) (*Scheduler, error) {
	r, err := client.Find(&Scheduler{Name: name})
	if err != nil {
		return nil, err
	}

	return r.(*Scheduler), nil
}

func (client Mikrotik) DeleteScheduler(name string) error {
	return client.Delete(&Scheduler{Name: name})
}


File: /client\scheduler_test.go
package client

import (
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/stretchr/testify/require"
)

func TestCreateUpdateDeleteAndFindScheduler(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	schedulerName := "scheduler_" + RandomString()
	onEvent := "onevent"
	interval := 0
	expectedScheduler := &Scheduler{
		Name:     schedulerName,
		OnEvent:  onEvent,
		Interval: types.MikrotikDuration(interval),
	}
	scheduler, err := c.AddScheduler(expectedScheduler)
	require.NoError(t, err)
	require.NotNil(t, scheduler)

	expectedScheduler.Id = scheduler.Id
	expectedScheduler.StartDate = scheduler.StartDate
	expectedScheduler.StartTime = scheduler.StartTime

	require.Equal(t, expectedScheduler, scheduler)

	// update and reassert
	expectedScheduler.OnEvent = "test"
	scheduler, err = c.UpdateScheduler(expectedScheduler)
	require.Equal(t, expectedScheduler, scheduler)

	err = c.DeleteScheduler(schedulerName)
	require.NoError(t, err)
}

func TestFindScheduler_onNonExistantScript(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	name := "scheduler does not exist"
	_, err := c.FindScheduler(name)

	require.Truef(t, IsNotFoundError(err),
		"Expecting to receive NotFound error for scheduler %q.", name)
}


File: /client\script.go
package client

import (
	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/go-routeros/routeros"
)

type Script struct {
	Id                     string             `mikrotik:".id" codegen:"id,deleteID"`
	Name                   string             `mikrotik:"name" codegen:"name,required,mikrotikID"`
	Owner                  string             `mikrotik:"owner,readonly" codegen:"owner,computed"`
	Policy                 types.MikrotikList `mikrotik:"policy" codegen:"policy,required"`
	DontRequirePermissions bool               `mikrotik:"dont-require-permissions" codegen:"dont_require_permissions"`
	Source                 string             `mikrotik:"source" codegen:"source,required"`
}

var _ Resource = (*Script)(nil)

func (b *Script) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/system/script/add",
		Find:   "/system/script/print",
		Update: "/system/script/set",
		Delete: "/system/script/remove",
	}[a]
}

func (b *Script) IDField() string {
	return ".id"
}

func (b *Script) ID() string {
	return b.Id
}

func (b *Script) SetID(id string) {
	b.Id = id
}

func (b *Script) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (b *Script) FindField() string {
	return "name"
}

func (b *Script) FindFieldValue() string {
	return b.Name
}

func (b *Script) DeleteField() string {
	return "numbers"
}

func (b *Script) DeleteFieldValue() string {
	return b.Id
}

// Typed wrappers
func (c Mikrotik) AddScript(r *Script) (*Script, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*Script), nil
}

func (c Mikrotik) UpdateScript(r *Script) (*Script, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*Script), nil
}

func (c Mikrotik) FindScript(name string) (*Script, error) {
	res, err := c.Find(&Script{Name: name})
	if err != nil {
		return nil, err
	}

	return res.(*Script), nil
}

func (c Mikrotik) DeleteScript(id string) error {
	return c.Delete(&Script{Id: id})
}


File: /client\script_test.go
package client

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

var scriptSource string = ":put testing"
var scriptName string = "testing"
var scriptPolicies []string = []string{
	"ftp",
	"reboot",
	"read",
	"write",
	"policy",
	"test",
	"password",
	"sniff",
	"sensitive",
	"romon",
}
var scriptDontReqPerms = true

func TestCreateScriptAndDeleteScript(t *testing.T) {
	c := NewClient(GetConfigFromEnv())
	_, owner, _, _, _, _ := GetConfigFromEnv()

	expectedScript := &Script{
		Name:                   scriptName,
		Owner:                  owner,
		Source:                 scriptSource,
		Policy:                 scriptPolicies,
		DontRequirePermissions: scriptDontReqPerms,
	}
	script, err := NewClient(GetConfigFromEnv()).
		AddScript(&Script{
			Name:                   scriptName,
			Source:                 scriptSource,
			Policy:                 scriptPolicies,
			DontRequirePermissions: scriptDontReqPerms,
		},
		)
	require.NoError(t, err)

	expectedScript.Id = script.Id

	defer func() {
		if err := c.DeleteScript(scriptName); err != nil {
			assert.True(t, IsNotFoundError(err), "the only acceptable error is NotFound")
		}
	}()

	require.Equal(t, expectedScript, script)

	err = c.DeleteScript(scriptName)
	require.NoError(t, err)
}

func TestFindScript_onNonExistantScript(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	name := "script-not-found"
	_, err := c.FindScript(name)

	if !IsNotFoundError(err) {
		t.Errorf("client should have received error indicating the following script `%s` was not found. Instead error was %v", name, err)
	}
}


File: /client\setup.go
package client

import (
	"fmt"
	"os"
	"testing"
)

func SetupAndTestMainExec(m *testing.M, sysResources *SystemResources) {
	c := NewClient(GetConfigFromEnv())
	s, err := c.GetSystemResources()

	if err != nil {
		fmt.Printf("Unable to perform test setup, failed with error: %v\n", err)
		os.Exit(1)
	}

	*sysResources = *s

	os.Exit(m.Run())
}


File: /client\setup_test.go
package client

import (
	"testing"
)

var sysResources SystemResources

func TestMain(m *testing.M) {
	SetupAndTestMainExec(m, &sysResources)
}


File: /client\system_resources.go
package client

import (
	"log"

	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
)

type SystemResources struct {
	Uptime  types.MikrotikDuration `mikrotik:"uptime,readonly"`
	Version string                 `mikrotik:"version,readonly"`
}

func (d *SystemResources) ActionToCommand(action Action) string {
	return map[Action]string{
		Find: "/system/resource/print",
	}[action]
}

func (client Mikrotik) GetSystemResources() (*SystemResources, error) {
	c, err := client.getMikrotikClient()
	if err != nil {
		return nil, err
	}
	sysResources := &SystemResources{}
	cmd := Marshal(sysResources.ActionToCommand(Find), sysResources)

	log.Printf("[INFO] Running the mikrotik command: `%s`", cmd)
	r, err := c.RunArgs(cmd)
	if err != nil {
		return nil, err
	}

	err = Unmarshal(*r, sysResources)
	return sysResources, err
}


File: /client\system_resources_test.go
package client

import (
	"strings"
	"testing"
)

func TestGetSystemResources(t *testing.T) {
	c := NewClient(GetConfigFromEnv())
	sysResources, err := c.GetSystemResources()

	if err != nil {
		t.Fatalf("failed to get system resources with error: %v", err)
	}

	if sysResources.Uptime <= 0 {
		t.Fatalf("expected uptime > 0, instead received '%d'", sysResources.Uptime)
	}

	version := sysResources.Version
	if strings.Index(version, "6") != 0 && strings.Index(version, "7") != 0 {
		t.Errorf("expected RouterOS version to start with a '7' or '6' major release, instead received '%s'", version)
	}
}


File: /client\types\duration.go
package types

import (
	"errors"
	"fmt"
	"strconv"
	"strings"
	"time"
)

// MikrotikDuration type represents a RouterOS durations [w,d] in seconds
type MikrotikDuration int

func (m MikrotikDuration) MarshalMikrotik() string {
	return strconv.Itoa(int(m))
}

func (m *MikrotikDuration) UnmarshalMikrotik(value string) error {
	value = strings.TrimSpace(value)
	if len(value) == 0 {
		return errors.New("cannot unmarshal empty value")
	}
	d, err := parseDuration(value)
	if err != nil {
		return err
	}
	*m = MikrotikDuration(d.Seconds())

	return nil
}

func parseDuration(s string) (time.Duration, error) {
	var digitsStartIndex, unitStartIndex int
	var nanoseconds int64

	parsePart := func(s string, unitStart int) (int64, error) {
		var ret int64
		digits, err := strconv.Atoi(s[:unitStart])
		if err != nil {
			return 0, err
		}

		unit := s[unitStart:]
		switch unit {
		case "ns":
			ret = int64(digits)
		case "us":
			ret = int64(digits) * time.Microsecond.Nanoseconds()
		case "ms":
			ret = int64(digits) * time.Millisecond.Nanoseconds()
		case "s":
			ret = int64(digits) * time.Second.Nanoseconds()
		case "m":
			ret = int64(digits) * time.Minute.Nanoseconds()
		case "h":
			ret = int64(digits) * time.Hour.Nanoseconds()
		case "d":
			ret = int64(digits) * time.Hour.Nanoseconds() * 24
		case "w":
			ret = int64(digits) * time.Hour.Nanoseconds() * 24 * 7
		default:
			return 0, fmt.Errorf("unknown unit: %q", unit)
		}
		return ret, nil
	}

	for i := 0; i < len(s); i++ {
		char := string(s[i])
		if char >= "0" && char <= "9" {
			if unitStartIndex > digitsStartIndex {
				parsed, err := parsePart(s[digitsStartIndex:i], unitStartIndex-digitsStartIndex)
				if err != nil {
					return 0, err
				}
				nanoseconds += parsed
				digitsStartIndex = i
				unitStartIndex = i
			}
			continue
		}
		if digitsStartIndex == unitStartIndex {
			unitStartIndex = i
		}
		continue
	}
	if digitsStartIndex == unitStartIndex {
		return 0, errors.New("duration without unit is not supported")
	}
	parsed, err := parsePart(s[digitsStartIndex:], unitStartIndex-digitsStartIndex)
	if err != nil {
		return 0, err
	}
	nanoseconds += parsed

	return time.Duration(nanoseconds), nil
}


File: /client\types\duration_test.go
package types

import (
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestDurationUnmarshal(t *testing.T) {

	testCases := []struct {
		name        string
		in          string
		expected    MikrotikDuration
		expectError bool
	}{
		{
			name:     "single unit",
			in:       "23s",
			expected: MikrotikDuration(23),
		},
		{
			name:     "units below second are zeroed",
			in:       "20ms",
			expected: MikrotikDuration(0),
		},
		{
			name:     "parse week",
			in:       "2w",
			expected: MikrotikDuration(time.Hour.Seconds() * 24 * 7 * 2),
		},
		{
			name:     "multiple units",
			in:       "2h17m01s",
			expected: MikrotikDuration(time.Hour.Seconds()*2 + time.Minute.Seconds()*17 + 1),
		},
		{
			name:        "no-unit produces error",
			in:          "17",
			expectError: true,
		},
		{
			name:        "unit and no-unit produces error",
			in:          "2h17",
			expectError: true,
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			m := MikrotikDuration(0)
			err := (&m).UnmarshalMikrotik(tc.in)
			if tc.expectError {
				require.Error(t, err)
				return
			}
			require.NoError(t, err)
			assert.Equal(t, tc.expected, m)
		})
	}
}


File: /client\types\list.go
package types

import (
	"strconv"
	"strings"
)

// MikrotikList type translates slice of strings to comma separated list and back
//
// It is useful to seamless serialize/deserialize data during communication with RouterOS
type MikrotikList []string

func (m MikrotikList) MarshalMikrotik() string {
	return strings.Join(m, ",")
}

func (m *MikrotikList) UnmarshalMikrotik(value string) error {
	if len(value) == 0 {
		*m = []string{}
		return nil
	}
	*m = strings.Split(value, ",")

	return nil
}

// MikrotikIntList type translates slice of ints to comma separated list and back
type MikrotikIntList []int

func (m MikrotikIntList) MarshalMikrotik() string {
	if len(m) == 0 {
		return ""
	}
	if len(m) == 1 {
		return strconv.Itoa(m[0])
	}

	buf := strings.Builder{}
	buf.WriteString(strconv.Itoa(m[0]))
	for i := range m[1:] {
		buf.WriteRune(',')
		buf.WriteString(strconv.Itoa(m[i+1]))
	}

	return buf.String()
}

func (m *MikrotikIntList) UnmarshalMikrotik(value string) error {
	if len(value) == 0 {
		*m = []int{}
		return nil
	}
	stringSlice := strings.Split(value, ",")
	res := []int{}
	for _, s := range stringSlice {
		elem, err := strconv.Atoi(s)
		if err != nil {
			return err
		}
		res = append(res, elem)
	}
	*m = res

	return nil
}


File: /client\types\list_test.go
package types

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestMikrotikList_marshal(t *testing.T) {
	testCases := []struct {
		name     string
		list     MikrotikList
		expected string
	}{
		{
			name:     "empty list",
			list:     MikrotikList{},
			expected: "",
		},
		{
			name:     "nil list",
			list:     nil,
			expected: "",
		},
		{
			name:     "one element",
			list:     MikrotikList{"2"},
			expected: "2",
		},
		{
			name:     "several elements",
			list:     MikrotikList{"2", "3", "one more"},
			expected: "2,3,one more",
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := tc.list.MarshalMikrotik()
			assert.Equal(t, tc.expected, result)
		})
	}
}

func TestMikrotikList_unmarshal(t *testing.T) {
	testCases := []struct {
		name        string
		in          string
		expected    MikrotikList
		expectError bool
	}{
		{
			name:     "empty list",
			in:       "",
			expected: MikrotikList{},
		},
		{
			name:     "one element",
			in:       "one",
			expected: MikrotikList{"one"},
		},
		{
			name:     "several elements",
			in:       "one,two,three",
			expected: MikrotikList{"one", "two", "three"},
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			l := MikrotikList{}
			err := l.UnmarshalMikrotik(tc.in)
			if tc.expectError {
				require.Error(t, err)
				return
			}
			require.NoError(t, err)
			assert.Equal(t, tc.expected, l)
		})
	}
}

func TestMikrotikIntList_marshal(t *testing.T) {
	testCases := []struct {
		name     string
		list     MikrotikIntList
		expected string
	}{
		{
			name:     "empty list",
			list:     MikrotikIntList{},
			expected: "",
		},
		{
			name:     "nil list",
			list:     nil,
			expected: "",
		},
		{
			name:     "one element",
			list:     MikrotikIntList{2},
			expected: "2",
		},
		{
			name:     "several elements",
			list:     MikrotikIntList{2, 3, 5},
			expected: "2,3,5",
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := tc.list.MarshalMikrotik()
			assert.Equal(t, tc.expected, result)
		})
	}
}

func TestMikrotikIntList_unmarshal(t *testing.T) {
	testCases := []struct {
		name        string
		in          string
		expected    MikrotikIntList
		expectError bool
	}{
		{
			name:     "empty list",
			in:       "",
			expected: MikrotikIntList{},
		},
		{
			name:     "one element",
			in:       "2",
			expected: MikrotikIntList{2},
		},
		{
			name:     "several elements",
			in:       "2,10,15",
			expected: MikrotikIntList{2, 10, 15},
		},
		{
			name:        "bogus element",
			in:          "2,10,not_an_integer,15",
			expectError: true,
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			l := MikrotikIntList{}
			err := l.UnmarshalMikrotik(tc.in)
			if tc.expectError {
				require.Error(t, err)
				return
			}
			require.NoError(t, err)
			assert.Equal(t, tc.expected, l)
		})
	}
}


File: /client\vlan_interface.go
package client

import (
	"github.com/go-routeros/routeros"
)

// VlanInterface represents vlan interface resource
type VlanInterface struct {
	Id            string `mikrotik:".id" codegen:"id,mikrotikID"`
	Interface     string `mikrotik:"interface" codegen:"interface"`
	Mtu           int    `mikrotik:"mtu" codegen:"mtu"`
	Name          string `mikrotik:"name" codegen:"name,required,terraformID"`
	Disabled      bool   `mikrotik:"disabled" codegen:"disabled"`
	UseServiceTag bool   `mikrotik:"use-service-tag" codegen:"use_service_tag"`
	VlanId        int    `mikrotik:"vlan-id" codegen:"vlan_id"`
}

var _ Resource = (*VlanInterface)(nil)

func (b *VlanInterface) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/interface/vlan/add",
		Find:   "/interface/vlan/print",
		Update: "/interface/vlan/set",
		Delete: "/interface/vlan/remove",
	}[a]
}

func (b *VlanInterface) IDField() string {
	return ".id"
}

func (b *VlanInterface) ID() string {
	return b.Id
}

func (b *VlanInterface) SetID(id string) {
	b.Id = id
}

func (b *VlanInterface) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

func (b *VlanInterface) FindField() string {
	return "name"
}

func (b *VlanInterface) FindFieldValue() string {
	return b.Name
}

func (b *VlanInterface) DeleteField() string {
	return "numbers"
}

func (b *VlanInterface) DeleteFieldValue() string {
	return b.Name
}

// Typed wrappers
func (c Mikrotik) AddVlanInterface(r *VlanInterface) (*VlanInterface, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*VlanInterface), nil
}

func (c Mikrotik) UpdateVlanInterface(r *VlanInterface) (*VlanInterface, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*VlanInterface), nil
}

func (c Mikrotik) FindVlanInterface(name string) (*VlanInterface, error) {
	res, err := c.Find(&VlanInterface{Name: name})
	if err != nil {
		return nil, err
	}

	return res.(*VlanInterface), nil
}

func (c Mikrotik) ListVlanInterface() ([]VlanInterface, error) {
	res, err := c.List(&VlanInterface{})
	if err != nil {
		return nil, err
	}
	returnSlice := make([]VlanInterface, len(res))
	for i, v := range res {
		returnSlice[i] = *(v.(*VlanInterface))
	}

	return returnSlice, nil
}

func (c Mikrotik) DeleteVlanInterface(name string) error {
	return c.Delete(&VlanInterface{Name: name})
}


File: /client\vlan_interface_test.go
package client

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestAddVlanInterfaceUpdateAndDelete(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	expectedIface := &VlanInterface{
		Name:      "vlan-20",
		VlanId:    20,
		Mtu:       1000,
		Interface: "*0",
		Disabled:  false,
	}

	iface, err := c.AddVlanInterface(&VlanInterface{
		Name:      expectedIface.Name,
		Disabled:  expectedIface.Disabled,
		Interface: expectedIface.Interface,
		VlanId:    expectedIface.VlanId,
		Mtu:       expectedIface.Mtu,
	})
	require.NoError(t, err)

	expectedIface.Id = iface.Id

	foundInterface, err := c.FindVlanInterface(expectedIface.Name)
	require.NoError(t, err)
	assert.Equal(t, expectedIface, foundInterface)

	expectedIface.Name = expectedIface.Name + "updated"
	expectedIface.Mtu = expectedIface.Mtu - 100
	updatedIface, err := c.UpdateVlanInterface(expectedIface)
	require.NoError(t, err)
	assert.Equal(t, expectedIface, updatedIface)
	// cleanup
	err = c.DeleteVlanInterface(iface.Name)
	assert.NoError(t, err)

	_, err = c.FindVlanInterface(expectedIface.Name)
	assert.Error(t, err)
}


File: /client\wireless_interface.go
package client

import "github.com/go-routeros/routeros"

const (
	WirelessInterfaceModeStation                   = "station"
	WirelessInterfaceModeStationWDS                = "station-wds"
	WirelessInterfaceModeAPBridge                  = "ap-bridge"
	WirelessInterfaceModeBridge                    = "bridge"
	WirelessInterfaceModeAlignmentOnly             = "alignment-only"
	WirelessInterfaceModeNstremeDualSlave          = "nstreme-dual-slave"
	WirelessInterfaceModeWDSSlave                  = "wds-slave"
	WirelessInterfaceModeStationPseudobridge       = "station-pseudobridge"
	WirelessInterfaceModeStationsPseudobridgeClone = "station-pseudobridge-clone"
	WirelessInterfaceModeStationBridge             = "station-bridge"
)

// WirelessInterface defines resource
type WirelessInterface struct {
	Id              string `mikrotik:".id" codegen:"id,mikrotikID"`
	Name            string `mikrotik:"name" codegen:"name,required"`
	MasterInterface string `mikrotik:"master-interface" codegen:"master_interface"`
	Mode            string `mikrotik:"mode" codegen:"mode"`
	Disabled        bool   `mikrotik:"disabled" codegen:"disabled"`
	SecurityProfile string `mikrotik:"security-profile" codegen:"security_profile"`
	SSID            string `mikrotik:"ssid" codegen:"ssid"`
	HideSSID        bool   `mikrotik:"hide-ssid" codegen:"hide_ssid"`
	VlanID          int    `mikrotik:"vlan-id" codegen:"vlan_id"`
	VlanMode        string `mikrotik:"vlan-mode" codegen:"vlan_mode"`
}

var _ Resource = (*WirelessInterface)(nil)

func (b *WirelessInterface) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/interface/wireless/add",
		Find:   "/interface/wireless/print",
		Update: "/interface/wireless/set",
		Delete: "/interface/wireless/remove",
	}[a]
}

func (b *WirelessInterface) IDField() string {
	return ".id"
}

func (b *WirelessInterface) ID() string {
	return b.Id
}

func (b *WirelessInterface) SetID(id string) {
	b.Id = id
}

func (b *WirelessInterface) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

// Typed wrappers
func (c Mikrotik) AddWirelessInterface(r *WirelessInterface) (*WirelessInterface, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*WirelessInterface), nil
}

func (c Mikrotik) UpdateWirelessInterface(r *WirelessInterface) (*WirelessInterface, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*WirelessInterface), nil
}

func (c Mikrotik) FindWirelessInterface(id string) (*WirelessInterface, error) {
	res, err := c.Find(&WirelessInterface{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*WirelessInterface), nil
}

func (c Mikrotik) ListWirelessInterface() ([]WirelessInterface, error) {
	res, err := c.List(&WirelessInterface{})
	if err != nil {
		return nil, err
	}
	returnSlice := make([]WirelessInterface, len(res))
	for i, v := range res {
		returnSlice[i] = *(v.(*WirelessInterface))
	}

	return returnSlice, nil
}

func (c Mikrotik) DeleteWirelessInterface(id string) error {
	return c.Delete(&WirelessInterface{Id: id})
}


File: /client\wireless_interface_test.go
package client

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestWirelessInterface_basic(t *testing.T) {
	// This test is skipped, until we find a way to include required packages.
	//
	// Since RouterOS 7.13, 'wireless' package is separate from the main system package
	// and there is no easy way to install it in Docker during tests.
	// see https://help.mikrotik.com/docs/spaces/ROS/pages/40992872/Packages#Packages-RouterOSpackages
	SkipIfRouterOSV7OrLater(t, sysResources)

	randSuffix := RandomString()
	c := NewClient(GetConfigFromEnv())
	expected := &WirelessInterface{
		Name:            "wireless-" + randSuffix,
		SSID:            "ssid-" + randSuffix,
		MasterInterface: "*0",
	}
	created, err := c.AddWirelessInterface(expected)
	require.NoError(t, err)
	defer c.DeleteWirelessInterface(created.Id)

	assert.Equal(t, expected.Name, created.Name)
	assert.Equal(t, expected.SSID, created.SSID)
	assert.Equal(t, false, created.Disabled)

	created.Disabled = true
	created.Name = "wireless-updated-" + randSuffix
	updated, err := c.UpdateWirelessInterface(created)
	require.NoError(t, err)
	assert.Equal(t, created, updated)

	found, err := c.FindWirelessInterface(updated.Id)
	require.NoError(t, err)
	assert.Equal(t, updated, found)
}


File: /client\wireless_security_profile.go
package client

import (
	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/go-routeros/routeros"
)

const (
	WirelessAuthenticationTypeWpaPsk  = "wpa-psk"
	WirelessAuthenticationTypeWpa2Psk = "wpa2-psk"
	WirelessAuthenticationTypeWpaEap  = "wpa-eap"
	WirelessAuthenticationTypeWpa2Eap = "wpa2-eap"

	WirelessModeNone               = "none"
	WirelessModeStaticKeysOptional = "static-keys-optional"
	WirelessModeStaticKeysRequired = "static-keys-required"
	WirelessModeDynamicKeys        = "dynamic-keys"
)

// WirelessSecurityProfile defines resource
type WirelessSecurityProfile struct {
	Id                  string             `mikrotik:".id" codegen:"id,mikrotikID"`
	Name                string             `mikrotik:"name" codegen:"name,required"`
	Mode                string             `mikrotik:"mode" codegen:"mode,optional"`
	AuthenticationTypes types.MikrotikList `mikrotik:"authentication-types" codegen:"authentication_types,optional"`
	WPA2PreSharedKey    string             `mikrotik:"wpa2-pre-shared-key" codegen:"wpa2_pre_shared_key"`
}

var _ Resource = (*WirelessSecurityProfile)(nil)

func (b *WirelessSecurityProfile) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "/interface/wireless/security-profiles/add",
		Find:   "/interface/wireless/security-profiles/print",
		Update: "/interface/wireless/security-profiles/set",
		Delete: "/interface/wireless/security-profiles/remove",
	}[a]
}

func (b *WirelessSecurityProfile) IDField() string {
	return ".id"
}

func (b *WirelessSecurityProfile) ID() string {
	return b.Id
}

func (b *WirelessSecurityProfile) SetID(id string) {
	b.Id = id
}

func (b *WirelessSecurityProfile) AfterAddHook(r *routeros.Reply) {
	b.Id = r.Done.Map["ret"]
}

// Typed wrappers
func (c Mikrotik) AddWirelessSecurityProfile(r *WirelessSecurityProfile) (*WirelessSecurityProfile, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*WirelessSecurityProfile), nil
}

func (c Mikrotik) UpdateWirelessSecurityProfile(r *WirelessSecurityProfile) (*WirelessSecurityProfile, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*WirelessSecurityProfile), nil
}

func (c Mikrotik) FindWirelessSecurityProfile(id string) (*WirelessSecurityProfile, error) {
	res, err := c.Find(&WirelessSecurityProfile{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*WirelessSecurityProfile), nil
}

func (c Mikrotik) ListWirelessSecurityProfile() ([]WirelessSecurityProfile, error) {
	res, err := c.List(&WirelessSecurityProfile{})
	if err != nil {
		return nil, err
	}
	returnSlice := make([]WirelessSecurityProfile, len(res))
	for i, v := range res {
		returnSlice[i] = *(v.(*WirelessSecurityProfile))
	}

	return returnSlice, nil
}

func (c Mikrotik) DeleteWirelessSecurityProfile(id string) error {
	return c.Delete(&WirelessSecurityProfile{Id: id})
}


File: /client\wireless_security_profile_test.go
package client

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestWirelessSecurityProfile_basic(t *testing.T) {
	// This test is skipped, until we find a way to include required packages.
	//
	// Since RouterOS 7.13, 'wireless' package is separate from the main system package
	// and there is no easy way to install it in Docker during tests.
	// see https://help.mikrotik.com/docs/spaces/ROS/pages/40992872/Packages#Packages-RouterOSpackages
	SkipIfRouterOSV7OrLater(t, sysResources)

	c := NewClient(GetConfigFromEnv())

	randSuffix := RandomString()
	expected := &WirelessSecurityProfile{
		Name:                "test-profile-" + randSuffix,
		Mode:                WirelessModeNone,
		AuthenticationTypes: []string{},
	}

	created, err := c.AddWirelessSecurityProfile(expected)
	require.NoError(t, err)
	defer c.DeleteWirelessSecurityProfile(created.Id)

	expected.Id = created.Id
	assert.Equal(t, expected, created)

	updated := &WirelessSecurityProfile{}
	*updated = *created
	updated.Name += "-updated"
	updated.Mode = WirelessModeDynamicKeys
	updated.AuthenticationTypes = []string{WirelessAuthenticationTypeWpa2Psk}
	updated.WPA2PreSharedKey = "1234567890"
	_, err = c.UpdateWirelessSecurityProfile(updated)
	require.NoError(t, err)

	found, err := c.FindWirelessSecurityProfile(updated.Id)
	require.NoError(t, err)

	assert.Equal(t, updated, found)

}


File: /cmd\mikrotik-codegen\internal\codegen\formatter.go
package codegen

import (
	"go/format"
)

// SourceFormatHook formats code using Go's formatter
func SourceFormatHook(p []byte) ([]byte, error) {
	return format.Source(p)
}


File: /cmd\mikrotik-codegen\internal\codegen\generator_mikrotik.go
package codegen

import (
	"io"
	"text/template"
	consoleinspected "github.com/ddelnano/terraform-provider-mikrotik/client/console-inspected"
	"github.com/ddelnano/terraform-provider-mikrotik/cmd/mikrotik-codegen/internal/utils"
)

func GenerateMikrotikResource(resourceName, commandBasePath string,
	consoleCommandDefinition consoleinspected.ConsoleItem,
	w io.Writer) error {
	if err := writeWrapper(w, []byte(generatedNotice)); err != nil {
		return err
	}
	t := template.New("resource")
	t.Funcs(template.FuncMap{
		"pascalCase": utils.PascalCase,
	})
	if _, err := t.Parse(mikrotikResourceDefinitionTemplate); err != nil {
		return err
	}

	fieldNames := make([]string, 0, len(consoleCommandDefinition.Arguments))
	for i := range consoleCommandDefinition.Arguments {
		fieldNames = append(fieldNames, consoleCommandDefinition.Arguments[i].Name)
	}

	data := struct {
		CommandBasePath string
		ResourceName    string
		FieldNames      []string
	}{
		CommandBasePath: commandBasePath,
		ResourceName:    resourceName,
		FieldNames:      fieldNames,
	}
	return generateCode(
		w,
		"resource",
		mikrotikResourceDefinitionTemplate,
		data,
	)
}

func GenerateMikrotikResourceTest(resourceName string, s *Struct, w io.Writer) error {
	data, err := generateTemplateData(*s)
	if err != nil {
		return err
	}

	return generateCode(
		w,
		"resource-test",
		mikrotikResourceTestDefinitionTemplate,
		data,
	)
}


File: /cmd\mikrotik-codegen\internal\codegen\generator_terraform.go
package codegen

import (
	"errors"
	"io"
	"reflect"
	"strings"
	"text/template"

	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/ddelnano/terraform-provider-mikrotik/cmd/mikrotik-codegen/internal/utils"
)

const (
	// List of declaration identifiers from ast package while parsing the source code
	AstVarTypeString = "string"
	AstVarTypeInt    = "int"
	AstVarTypeBool   = "bool"
)

var (
	// Handle custom types from the client package
	AstVarTypeMikrotikList     = reflect.TypeOf(types.MikrotikList{}).Name()
	AstVarTypeMikrotikIntList  = reflect.TypeOf(types.MikrotikIntList{}).Name()
	AstVarTypeMikrotikDuration = reflect.TypeOf(types.MikrotikDuration(0)).Name()

	terraformResourceImports = []string{
		"context",
		"github.com/ddelnano/terraform-provider-mikrotik/client",
		"github.com/hashicorp/terraform-plugin-framework/path",
		"github.com/hashicorp/terraform-plugin-framework/resource",
		"github.com/hashicorp/terraform-plugin-framework/resource/schema",
		"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier",
		"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier",
	}

	terraformResourceTestImports = []string{
		"fmt",
		"testing",
		"github.com/ddelnano/terraform-provider-mikrotik/client",
		"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource",
		"github.com/hashicorp/terraform-plugin-sdk/v2/terraform",
	}
)

type (
	// SourceWriteHookFunc defines a hook func to mutate source before writing to destination
	SourceWriteHookFunc func([]byte) ([]byte, error)

	sourceWriter interface {
		Write([]byte) (int, error)
	}

	terraformField struct {
		Name          string
		AttributeName string
		Required      bool
		Optional      bool
		Computed      bool
		MikrotikField *Field
		Type          Type
		ElemType      Type
	}

	templateData struct {
		Imports          []string
		ResourceName     string
		Fields           []*terraformField
		TerraformIDField *terraformField
		MikrotikIDField  *Field
		DeleteField      *terraformField
	}
)

// GenerateResource generates Terraform resource and writes it to specified output
func GenerateResource(s *Struct, w io.Writer) error {
	data, err := generateTemplateData(*s)
	if err != nil {
		return err
	}
	data.Imports = terraformResourceImports

	return generateCode(w,
		"resource",
		terraformResourceDefinitionTemplate,
		data,
	)
}

// GenerateResourceTest generates Terraform resource acceptance test and writes it to specified output
func GenerateResourceTest(s *Struct, w io.Writer) error {
	data, err := generateTemplateData(*s)
	if err != nil {
		return err
	}
	data.Imports = terraformResourceTestImports

	return generateCode(w,
		"resource_test",
		terraformResourceTestDefinitionTemplate,
		data,
	)
}

func generateTemplateData(s Struct) (templateData, error) {
	fields, err := convertToTerraformDefinition(s.Fields)
	if err != nil {
		return templateData{}, err
	}

	findTerraformFieldByName := func(fields []*terraformField, name string) *terraformField {
		for i := range fields {
			if fields[i].MikrotikField.OriginalName == name {
				return fields[i]
			}
		}
		return &terraformField{}
	}
	findMikrotikFieldByName := func(fields []*Field, name string) *Field {
		for i := range fields {
			if fields[i].OriginalName == name {
				return fields[i]
			}
		}
		return &Field{}
	}

	idField := findTerraformFieldByName(fields, s.MikrotikIDField)
	if idField.AttributeName == "" {
		return templateData{}, errors.New("The source struct does not provide information about ID field. Did you forget to mark one via 'id' tag?")
	}
	terraformIdField := findTerraformFieldByName(fields, s.TerraformIDField)
	if terraformIdField.AttributeName == "" {
		terraformIdField = idField
	}
	deleteField := findTerraformFieldByName(fields, s.DeleteField)
	if deleteField.AttributeName == "" {
		deleteField = idField
	}

	mikrotikIdField := findMikrotikFieldByName(s.Fields, s.MikrotikIDField)
	if mikrotikIdField.OriginalName == "" {
		mikrotikIdField = idField.MikrotikField
	}

	idField.Computed = true
	idField.Required = false
	idField.Optional = false

	return templateData{
		ResourceName:     s.Name,
		Fields:           fields,
		TerraformIDField: terraformIdField,
		MikrotikIDField:  mikrotikIdField,
		DeleteField:      deleteField,
	}, nil
}

func generateCode(w io.Writer, templateName, templateBody string, templateData interface{}) error {
	t := template.New(templateName)
	t.Funcs(template.FuncMap{
		"lowerCase":  strings.ToLower,
		"snakeCase":  utils.ToSnakeCase,
		"firstLower": utils.FirstLower,
		"sampleData": sampleData,
	})
	if _, err := t.Parse(templateBody); err != nil {
		return err
	}

	if err := writeWrapper(w, []byte(generatedNotice)); err != nil {
		return err
	}

	if err := t.Execute(w, templateData); err != nil {
		return err
	}

	return nil
}

func convertToTerraformDefinition(fields []*Field) ([]*terraformField, error) {
	result := []*terraformField{}

	for _, f := range fields {
		fieldType := typeToTerraformType(f.Type)
		elemType := UnknownType
		// currently, only list supports element typing
		if fieldType.Is(ListType) || fieldType.Is(SetType) {
			elemType = typeToTerraformType(f.ElemType)
		}
		result = append(result, &terraformField{
			Name:          f.OriginalName,
			AttributeName: f.Name,
			Type:          fieldType,
			ElemType:      elemType,
			Required:      f.Required,
			Optional:      f.Optional,
			Computed:      f.Computed,
			MikrotikField: f,
		})
	}

	return result, nil
}

func typeToTerraformType(typ string) Type {
	switch typ {
	case AstVarTypeBool:
		return BoolType
	case AstVarTypeInt, AstVarTypeMikrotikDuration:
		return Int64Type
	case AstVarTypeString:
		return StringType
	case AstVarTypeMikrotikList:
		return StringSliceType
	case AstVarTypeMikrotikIntList:
		return IntSliceType
	}

	return UnknownType
}

func writeWrapper(w sourceWriter, data []byte) error {
	_, err := w.Write(data)

	return err
}

// sampleData generates sample value for provided type.
func sampleData(typeName string) string {
	switch typeName {
	case typeString:
		return `"sample"`
	case typeList:
		return `[]`
	case typeSet:
		return `[]`
	case typeInt64:
		return "42"
	case typeBool:
		return "false"
	case typeStringSlice:
		return `["one", "two"]`
	case typeIntSlice:
		return `[1, 2, 3]`
	default:
		return `"` + typeUnknown + `"`
	}
}


File: /cmd\mikrotik-codegen\internal\codegen\parser.go
package codegen

import (
	"errors"
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"reflect"
	"strconv"
	"strings"
)

type (
	// Struct holds information about parsed struct.
	Struct struct {
		// Name is a of parsed struct.
		Name string

		// MikrotikIDField is a field name which holds MikroTik resource ID.
		MikrotikIDField string

		// TerraformIDField holds a field name which will be used as Terraform resource ID.
		TerraformIDField string

		// DeleteField holds a field name to use when deleting resource on MikroTik system.
		DeleteField string

		// Fields is a collection of field definitions in the parsed struct.
		Fields []*Field
	}

	// Field holds information about particular field in parsed struct.
	Field struct {
		// OriginalName is an original field name without chnages.
		OriginalName string

		// Name is a field name defined by struct tag.
		Name string

		// Required marks field as `required` in Terraform definition.
		Required bool

		// Optional marks field as `optional` in Terraform definition.
		Optional bool

		// Computed marks field as `computed` in Terraform definition.
		Computed bool

		// Type holds a field type.
		Type string

		// ElemType holds an element type if field type is List or Set
		ElemType string
	}
)

const (
	codegenTagKey = "codegen"

	optTerraformID = "terraformID"
	optMikrotikID  = "mikrotikID"
	optDeleteID    = "deleteID"
	optRequired    = "required"
	optOptional    = "optional"
	optComputed    = "computed"
	optElemType    = "elemType="
	optOmit        = "omit"
)

// ParseFile parses a .go file with struct declaration.
//
// This functions searches for struct definition `structName` and parses it.
// If `structName` is empty, function stops at first struct definition in the file right after `startLine`.
func ParseFile(filename string, startLine int, structName string) (*Struct, error) {
	_, err := os.Stat(filename)
	if err != nil {
		return nil, err
	}

	fSet := token.NewFileSet()
	aFile, err := parser.ParseFile(fSet, filename, nil, parser.ParseComments)
	if err != nil {
		return nil, err
	}

	if aFile == nil {
		return nil, errors.New("parsing of the file returned unexpected nil as *ast.File")
	}

	s, err := parse(fSet, aFile, startLine, structName)
	if err != nil {
		return nil, err
	}

	return s, nil
}

func parse(fSet *token.FileSet, node ast.Node, startLine int, structName string) (*Struct, error) {
	structNode, foundName, err := findStruct(fSet, node, startLine, structName)
	if err != nil {
		return nil, err
	}

	parsedStruct, err := parseStructUsingTags(structNode)
	if err != nil {
		return nil, err
	}
	parsedStruct.Name = foundName

	return parsedStruct, nil
}

func findStruct(fSet *token.FileSet, node ast.Node, startLine int, structName string) (*ast.StructType, string, error) {
	var foundName string
	var structNode *ast.StructType

	ast.Inspect(node, func(n ast.Node) bool {
		if n == nil {
			return true
		}
		if n.Pos().IsValid() {
			pos := fSet.Position(n.Pos())
			if pos.Line < startLine {
				return true
			}
		}
		typeSpec, ok := n.(*ast.TypeSpec)
		if !ok {
			return true
		}
		if typeSpec.Type == nil {
			return true
		}
		// if struct name is provided, ignore other structs on the way
		if structName != "" && typeSpec.Name.Name != structName {
			return true
		}

		foundName = typeSpec.Name.Name
		t, ok := typeSpec.Type.(*ast.StructType)
		if !ok {
			return true
		}

		structNode = t

		// stop after first struct is found
		return false
	})
	if foundName == "" {
		return nil, "", errors.New("struct not found")
	}
	return structNode, foundName, nil
}

func parseStructUsingTags(structNode *ast.StructType) (*Struct, error) {
	result := &Struct{}

	for _, astField := range structNode.Fields.List {
		if astField.Tag == nil {
			continue
		}

		// always unquote tag literal, otherwise it is treated as '`key:"options,here"`'
		unquoted, err := strconv.Unquote(astField.Tag.Value)
		if err != nil {
			return nil, err
		}
		tag := reflect.StructTag(unquoted)
		tagKey := codegenTagKey
		tagValue, ok := tag.Lookup(tagKey)
		if !ok {
			continue
		}
		parts := strings.Split(tagValue, ",")
		name, opts := parts[0], parts[1:]

		if name == "-" {
			continue
		}

		// determine the type of the field
		typeName := typeUnknown
		if exp, ok := astField.Type.(*ast.SelectorExpr); ok {
			// selector expression when type comes from another package, e.g. types.MikrotikList
			typeName = exp.Sel.Name
		}
		if exp, ok := astField.Type.(*ast.Ident); ok {
			// identifier, when it is a builtin type, e.g. "string"
			typeName = exp.Name
		}
		field := Field{
			OriginalName: astField.Names[0].Name,
			Name:         name,
			Type:         typeName,
		}
		omit := false
		for _, o := range opts {
			switch {
			case o == optTerraformID:
				if result.TerraformIDField != "" {
					return nil, fmt.Errorf("failed to set '%s' as Terraform ID field - it is already set to '%s'", field.OriginalName, result.TerraformIDField)
				}
				result.TerraformIDField = field.OriginalName
			case o == optMikrotikID:
				if result.MikrotikIDField != "" {
					return nil, fmt.Errorf("failed to set '%s' as Mikrotik ID field - it is already set to '%s'", field.OriginalName, result.MikrotikIDField)
				}
				result.MikrotikIDField = field.OriginalName
			case o == optDeleteID:
				if result.DeleteField != "" {
					return nil, fmt.Errorf("failed to set '%s' as delete ID field - it is already set to '%s'", field.OriginalName, result.DeleteField)
				}
				result.DeleteField = field.OriginalName
			case o == optRequired:
				field.Required = true
			case o == optOptional:
				field.Optional = true
			case strings.HasPrefix(o, optElemType):
				field.ElemType = strings.TrimPrefix(o, optElemType)
			case o == optComputed:
				field.Computed = true
			case o == optOmit:
				omit = true
			}
		}
		if omit {
			continue
		}
		if !(field.Computed || field.Required || field.Optional) {
			field.Optional = true
		}
		if field.OriginalName == result.MikrotikIDField {
			field.Computed = true
			field.Required = false
			field.Optional = false
		}

		result.Fields = append(result.Fields, &field)
	}

	if result.MikrotikIDField == "" {
		return nil, fmt.Errorf("MikroTik ID field is not set for any of the fields. Did you forget to mark one with '%s'?", optMikrotikID)
	}
	if result.TerraformIDField == "" {
		result.TerraformIDField = result.MikrotikIDField
	}

	return result, nil
}


File: /cmd\mikrotik-codegen\internal\codegen\parser_test.go
package codegen

import (
	"errors"
	"go/parser"
	"go/token"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestParse(t *testing.T) {
	cases := []struct {
		name          string
		source        []byte
		structName    string
		startLine     int
		expected      *Struct
		expectedError error
	}{
		{
			name: "terraform and mikrotik id fields are parsed",
			source: []byte(`
package testpackage

type DnsRecord struct {
	ID	 			   string` + " `codegen:\"id,mikrotikID\"`" + `
	Name 			   string` + " `codegen:\"name,required,terraformID\"`" + `
	GeneratedNumber	   string` + " `codegen:\"internal_id,computed\"`" + `
	Enabled 		   bool` + " `codegen:\"enabled,optional\"`" + `
	Omitted			   bool` + " `codegen:\"-\"`" + `
	ExplicitlyOmitted  bool` + " `codegen:\"-,omit\"`" + `
}
			`),

			expected: &Struct{
				Name:             "DnsRecord",
				TerraformIDField: "Name",
				MikrotikIDField:  "ID",
				Fields: []*Field{
					{
						OriginalName: "ID",
						Name:         "id",
						Type:         "string",
						Computed:     true,
					},
					{
						OriginalName: "Name",
						Name:         "name",
						Type:         "string",
						Required:     true,
					},
					{
						OriginalName: "GeneratedNumber",
						Name:         "internal_id",
						Type:         "string",
						Computed:     true,
					},
					{
						OriginalName: "Enabled",
						Name:         "enabled",
						Type:         "bool",
						Optional:     true,
					},
				},
			},
		},
		{
			name: "deleteID field is parsed",
			source: []byte(`
package testpackage

type DnsRecord struct {
	ID	 			   string` + " `codegen:\"id,mikrotikID\"`" + `
	Name 			   string` + " `codegen:\"name,terraformID,deleteID,required\"`" + `
	GeneratedNumber	   string` + " `codegen:\"internal_id,computed\"`" + `
	Enabled 		   bool` + " `codegen:\"enabled,optional\"`" + `
	ExplicitlyOmitted  bool` + " `codegen:\"-\"`" + `
}
			`),

			expected: &Struct{
				Name:             "DnsRecord",
				TerraformIDField: "Name",
				MikrotikIDField:  "ID",
				DeleteField:      "Name",
				Fields: []*Field{
					{
						OriginalName: "ID",
						Name:         "id",
						Type:         "string",
						Computed:     true,
					},
					{
						OriginalName: "Name",
						Name:         "name",
						Type:         "string",
						Required:     true,
					},
					{
						OriginalName: "GeneratedNumber",
						Name:         "internal_id",
						Type:         "string",
						Computed:     true,
					},
					{
						OriginalName: "Enabled",
						Name:         "enabled",
						Type:         "bool",
						Optional:     true,
					},
				},
			},
		},
		{
			name: "mikrotikID is not set",
			source: []byte(`
package testpackage

type DnsRecord struct {
	Id 			   	   string` + " `codegen:\"id\"`" + `
	Name 			   string` + " `codegen:\"name,terraformID,required\"`" + `
	GeneratedNumber	   string` + " `codegen:\"internal_id,computed\"`" + `
	Enabled 		   bool` + " `codegen:\"enabled,id,optional\"`" + `
	ExplicitlyOmitted  bool` + " `codegen:\"-,omit\"`" + `
}
			`),

			expectedError: errors.New(""),
		},
		{
			name: "terraform id field set multiple times",
			source: []byte(`
package testpackage

type DnsRecord struct {
	Id 			   	   string` + " `codegen:\"id,mikrotikID\"`" + `
	Name 			   string` + " `codegen:\"name,terraformID,required\"`" + `
	GeneratedNumber	   string` + " `codegen:\"internal_id,computed\"`" + `
	Enabled 		   bool` + " `codegen:\"enabled,terraformID,optional\"`" + `
	ExplicitlyOmitted  bool` + " `codegen:\"-,omit\"`" + `
}
			`),

			expectedError: errors.New(""),
		},
		{
			name: "mikrotik id field set multiple times",
			source: []byte(`
package testpackage

type DnsRecord struct {
	ID 				   string` + " `codegen:\"id,mikrotikID\"`" + `
	Name 			   string` + " `codegen:\"name,mikrotikID,required\"`" + `
	GeneratedNumber	   string` + " `codegen:\"internal_id,computed\"`" + `
	Enabled 		   bool` + " `codegen:\"enabled,optional\"`" + `
	ExplicitlyOmitted  bool` + " `codegen:\"-,omit\"`" + `
}
			`),

			expectedError: errors.New(""),
		},
		{
			name: "delete id field set multiple times",
			source: []byte(`
package testpackage

type DnsRecord struct {
	ID 				   string` + " `codegen:\"id,required\"`" + `
	Name 			   string` + " `codegen:\"name,mikrotikID,deleteID,required\"`" + `
	GeneratedNumber	   string` + " `codegen:\"internal_id,deleteID,computed\"`" + `
	Enabled 		   bool` + " `codegen:\"enabled,optional\"`" + `
	ExplicitlyOmitted  bool` + " `codegen:\"-,omit\"`" + `
}
			`),

			expectedError: errors.New(""),
		},
	}
	for _, tc := range cases {
		t.Run(tc.name, func(t *testing.T) {
			fSet := token.NewFileSet()
			node, err := parser.ParseFile(fSet, "", tc.source, parser.ParseComments)
			if err != nil {
				t.Error(err)
			}
			result, err := parse(fSet, node, tc.startLine, tc.structName)
			// todo(maksym): this condition does not check the error type since we don't have specific errors yet
			if (tc.expectedError == nil) != (err == nil) {
				t.Errorf("expected error to be %v, got %v", tc.expectedError, err)
			}
			if err != nil {
				return
			}
			assert.Equal(t, tc.expected, result)
		})
	}
}


File: /cmd\mikrotik-codegen\internal\codegen\README.md
MikroTik code generation
========================

This tool allows generating MikroTik resources for API client and Terraform resources based on Mikrotik struct definition.

## MikroTik client resource
To generate new MikroTik resource definition, simply run
```sh
$ go run ./cmd/mikrotik-codegen mikrotik -name BridgeVlan -commandBase "/interface/bridge/vlan"
```
where

`name` - a name of MikroTik resource to generate.

`commandBase` - base path to craft commands for CRUD operations.

It is also possible to pre-fill list of fields using either `-inspect-definition-file` argument
```sh
$ go run ./cmd/mikrotik-codegen mikrotik -name BridgeVlan -commandBase "/interface/bridge/vlan" -inspect-definition-file ./inspect_vlan.txt
```

or `-query-definition` flag (requires valid credentials in evironment)
```sh
$ go run ./cmd/mikrotik-codegen mikrotik -name BridgeVlan -commandBase "/interface/bridge/vlan" -query-definition
```
For details, see [Experimental](#experimental) section.

## Terraform resource
Just add a `codegen` tag key to struct fields:
```go
type MikrotikResource struct{
	Id             string   `mikrotik:".id"             codegen:"id,mikrotikID,deleteID"`
	Name           string   `mikrotik:"name"            codegen:"name,required,terraformID"`
	Enabled        bool     `mikrotik:"enabled"         codegen:"enabled"`
	Items          []string `mikrotik:"items"           codegen:"items,elemType=string"`
	UpdatedAt      string   `mikrotik:"updated_at"      codegen:"updated_at,computed"`
	Unused         int      `mikrotik:"unused"          codegen:"-"`
	NotImplemented int      `mikrotik:"not_implemented" codegen:"not_implemented,omit"`
	Comment        string   `mikrotik:"comment"         codegen:"comment"`
}
```

and run:
```sh
$ go run ./cmd/mikrotik-codegen terraform -src client/resource.go -struct MikrotikResource > mikrotik/resource_new.go
```


## Supported options

|Name|Description|
|-|-|
|terraformID|Use this field during `Read` and `Import` resource|
|mikrotikID|This field is MikroTik ID field, usually `.id`|
|deleteID|Terraform resource will use this field to delete resource|
|required|Mark field as `required` in resource schema|
|optional|Mark field as `optional` in resource schema|
|computed|Mark field as `computed` in resource schema|
|elemType|Explicitly set element type for `List` or `Set` attributes. Usage `elemType=int`|
|omit|Skip this field from code generation process|


## Experimental

This section contains documentation for experimental and non-stable features.

### Generate Mikrotik resource using /console/inspect definition

Modern RouterOS versions (>7.x) provide new `/console/inspect` command to query hierarchy or syntax of particular command.

For example, `/console/inspect  path=interface,list request=child` prints `parent-child` relationship of the command:
```
Columns: TYPE, NAME, NODE-TYPE
TYPE   NAME     NODE-TYPE
self   list     dir
child  add      cmd
child  comment  cmd
child  edit     cmd
child  export   cmd
child  find     cmd
child  get      cmd
child  member   dir
child  print    cmd
child  remove   cmd
child  reset    cmd
child  set      cmd
```

while `/console/inspect  path=interface,list request=syntax` gives another set of attributes:
```
Columns: TYPE, SYMBOL, SYMBOL-TYPE, NESTED, NONORM, TEXT
TYPE    SYMBOL   SYMBOL-TYPE  NESTED  NONORM  TEXT
syntax           collection        0  yes
syntax  ..       explanation       1  no      go up to interface
syntax  add      explanation       1  no      Create a new item
syntax  comment  explanation       1  no      Set comment for items
syntax  edit     explanation       1  no
syntax  export   explanation       1  no      Print or save an export script that can be used to restore configuration
syntax  find     explanation       1  no      Find items by value
syntax  get      explanation       1  no      Gets value of item's property
syntax  member   explanation       1  no
syntax  print    explanation       1  no      Print values of item properties
syntax  remove   explanation       1  no      Remove item
syntax  reset    explanation       1  no
syntax  set      explanation       1  no      Change item properties
```

Using that information, it is possible to query (even recursively) information about all menu items and sub-commands, starting from the root `/` command.

:Warning: Since this feature is recent, trying to call it with our client package sometimes results in `terminal crush`.

#### Using definition in file

For this case, one needs:
1. Machine-readable data about available fields
2. Pass this data as `-inspect-definition-file` argument.

To get resource definition, run the following command on remote system:
```
$ :put [/console/inspect  path=interface,list,add request=child as-value]
```

which produces:
```
name=add;node-type=cmd;type=self;name=comment;node-type=arg;type=child;name=copy-from;node-type=arg;type=child;name=exclude;node-type=arg;type=child;name=include;node-type=arg;type=child;name=name;node-type=arg;type=child
```

If you have `ssh` access to the Mikrotik, the following command will produce the same string:
```shell
$ ssh -o Port=XXXX -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null admin@board ":put [/console inspect as-value request=child path=interface,list,add]" > inspect_definition.txt
```

After getting the definition file, just generate Mikrotik resource as usual with extra flag:
```sh
$ go run ./cmd/mikrotik-codegen mikrotik -name InterfaceList -commandBase "/interface/list" -inspect-definition-file ./inspect_definition.txt
```
and all fields for the struct will be created.


Note, that we used `interface,list,add` as argument to `path`. The terminal equivalent would be `/interface/list/add` (not sure why it works that way, you can check [forum topic](https://forum.mikrotik.com/viewtopic.php?t=199139#p1024410))

The reason we used `add` command and not `/interface/list` menu itself, is that we need only args (fields) of `add` command - not information about possible commands for `/interface/list`
#### Query resource definition automatically

To use this method, current environment must contain valid credentials.

```shell
$ go run cmd/mikrotik-codegen/main.go mikrotik -commandBase /ip/dhcp-server -name DhcpServer -query-definition
```


File: /cmd\mikrotik-codegen\internal\codegen\templates.go
package codegen

const (
	generatedNotice = "// This code was generated. Review it carefully."

	terraformResourceDefinitionTemplate = `
package mikrotik

import (
	{{ range $import := .Imports -}}
		"{{ $import }}"
	{{ end }}
	tftypes "github.com/hashicorp/terraform-plugin-framework/types"

)
{{ $resourceStructName := .ResourceName | firstLower}}
type {{$resourceStructName}} struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &{{$resourceStructName}}{}
	_ resource.ResourceWithConfigure   = &{{$resourceStructName}}{}
	_ resource.ResourceWithImportState = &{{$resourceStructName}}{}
)

// New{{.ResourceName}}Resource is a helper function to simplify the provider implementation.
func New{{.ResourceName}}Resource() resource.Resource {
	return &{{$resourceStructName}}{}
}

func (r *{{$resourceStructName}}) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *{{$resourceStructName}}) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_{{.ResourceName | snakeCase}}"
}

// Schema defines the schema for the resource.
func (s *{{$resourceStructName}}) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a MikroTik {{.ResourceName}}.",
		Attributes: map[string]schema.Attribute{
			{{range .Fields -}}
			"{{.AttributeName}}": schema.{{.Type.Name}}Attribute{
				Required: {{.Required}},
				Optional: {{.Optional}},
				Computed: {{.Computed}},
				{{if .Computed -}}
				PlanModifiers: []planmodifier.{{.Type.Name}}{
					{{.Type.Name | lowerCase}}planmodifier.UseStateForUnknown(),
				},
				{{- end}}
				Description: "",
			},
			{{end}}
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *{{$resourceStructName}}) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel {{$resourceStructName}}Model
	var mikrotikModel client.{{.ResourceName}}
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *{{$resourceStructName}}) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel {{$resourceStructName}}Model
	var mikrotikModel client.{{.ResourceName}}
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *{{$resourceStructName}}) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel {{$resourceStructName}}Model
	var mikrotikModel client.{{.ResourceName}}
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *{{$resourceStructName}}) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel {{$resourceStructName}}Model
	var mikrotikModel client.{{.ResourceName}}
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *{{$resourceStructName}}) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("{{.TerraformIDField.AttributeName}}"), req, resp)
}

type {{$resourceStructName}}Model struct {
	{{range .Fields -}}
	{{.Name}}        tftypes.{{.Type.Name}} ` + "`" + `tfsdk:"{{.AttributeName}}"` + "`" + `
	{{end}}
}
`

	mikrotikResourceDefinitionTemplate = `
package client

import (
	"github.com/ddelnano/terraform-provider-mikrotik/client/internal/types"
	"github.com/go-routeros/routeros"
)

// {{.ResourceName}} defines resource
type {{.ResourceName}} struct {
	Id string ` + "`" + `mikrotik:".id"` + "`" + `
	{{range $fieldName := .FieldNames -}}
		{{$fieldName | pascalCase}} string ` + "`" + `mikrotik:"{{$fieldName}}"` + "`" + `
	{{end}}
}

var _ Resource = (*{{.ResourceName}})(nil)

func (b *{{.ResourceName}}) ActionToCommand(a Action) string {
	return map[Action]string{
		Add:    "{{.CommandBasePath}}/add",
		Find:   "{{.CommandBasePath}}/print",
		Update: "{{.CommandBasePath}}/set",
		Delete: "{{.CommandBasePath}}/remove",
	}[a]
}

func (b *{{.ResourceName}}) IDField() string {
	return ".id"
}

func (b *{{.ResourceName}}) ID() string {
	return b.Id
}

func (b *{{.ResourceName}}) SetID(id string) {
	b.Id = id
}

// Uncomment extra methods to satisfy more interfaces

// Adder
// func (b *{{.ResourceName}}) AfterAddHook(r *routeros.Reply) {
// 	b.Id = r.Done.Map["ret"]
// }

// Finder
// func (b *{{.ResourceName}}) FindField() string {
// 	return "name"
// }

// func (b *{{.ResourceName}}) FindFieldValue() string {
// 	return b.Name
// }

// Deleter
// func (b *{{.ResourceName}}) DeleteField() string {
// 	return "numbers"
// }

// func (b *{{.ResourceName}}) DeleteFieldValue() string {
// 	return b.Id
// }


// Typed wrappers
func (c Mikrotik) Add{{.ResourceName}}(r *{{.ResourceName}}) (*{{.ResourceName}}, error) {
	res, err := c.Add(r)
	if err != nil {
		return nil, err
	}

	return res.(*{{.ResourceName}}), nil
}

func (c Mikrotik) Update{{.ResourceName}}(r *{{.ResourceName}}) (*{{.ResourceName}}, error) {
	res, err := c.Update(r)
	if err != nil {
		return nil, err
	}

	return res.(*{{.ResourceName}}), nil
}

func (c Mikrotik) Find{{.ResourceName}}(id string) (*{{.ResourceName}}, error) {
	res, err := c.Find(&{{.ResourceName}}{Id: id})
	if err != nil {
		return nil, err
	}

	return res.(*{{.ResourceName}}), nil
}

func (c Mikrotik) List{{.ResourceName}}() ([]{{.ResourceName}}, error) {
	res, err := c.List(&{{.ResourceName}}{})
	if err != nil {
		return nil, err
	}
	returnSlice := make([]{{.ResourceName}}, len(res))
	for i, v := range res {
		returnSlice[i] = *(v.(*{{.ResourceName}}))
	}

	return returnSlice, nil
}


func (c Mikrotik) Delete{{.ResourceName}}(id string) error {
	return c.Delete(&{{.ResourceName}}{Id: id})
}

`

	mikrotikResourceTestDefinitionTemplate = `
package client

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestAdd{{.ResourceName}}UpdateAndDelete(t *testing.T) {
	c := NewClient(GetConfigFromEnv())

	expectedResource := &{{.ResourceName}}{
	{{- range $field := .Fields }}
		{{- if and $field.Computed (not $field.Optional) }}{{continue}}{{end}}
		{{$field.Name}}: {{$field.Type.Name | sampleData}},
	{{- end }}
	}

	createdResource, err := c.Add{{.ResourceName}}(expectedResource)
	require.NoError(t, err)

	defer func(){
		id := createdResource.{{.TerraformIDField.Name}}
		err := c.Delete{{.ResourceName}}(id)
		if !assert.True(t, IsNotFoundError(err)) {
			assert.NoError(t, err)
		}
	}()

	expectedResource.Id = createdResource.Id

	foundResource, err := c.Find{{.ResourceName}}(expectedResource.{{.TerraformIDField.Name}})
	require.NoError(t, err)
	assert.Equal(t, expectedResource, foundResource)
{{ range $field := .Fields }}
	{{- if and $field.Computed (not $field.Optional) }}{{continue}}{{end}}
	expectedResource.{{$field.Name}} = expectedResource.{{$field.Name}} + {{$field.Type.Name | sampleData}}
{{- end }}

	updatedResource, err := c.Update{{.ResourceName}}(expectedResource)
	require.NoError(t, err)
	assert.Equal(t, expectedResource, updatedResource)

	// cleanup
	err = c.Delete{{.ResourceName}}(updatedResource.{{.TerraformIDField.Name}})
	assert.NoError(t, err)

	_, err = c.Find{{.ResourceName}}(expectedResource.{{.TerraformIDField.Name}})
	assert.Error(t, err)
}
`

	terraformResourceTestDefinitionTemplate = `
package mikrotik

import (
	{{ range $import := .Imports -}}
		"{{ $import }}"
	{{ end }}
)

{{ $resourceNameLower := .ResourceName | snakeCase }}
{{ $resourceType := .ResourceName | snakeCase | printf "mikrotik_%s" }}

func TestAcc{{.ResourceName}}_basic(t *testing.T) {
	resourceName := "{{$resourceType}}.testacc_{{$resourceNameLower}}"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheck{{.ResourceName}}Destroy,
		Steps: []resource.TestStep{
			{
				Config: ` + "`" + `
				resource "{{$resourceType}}" "testacc_{{$resourceNameLower}}" {
					{{ range $x := .Fields -}}
					{{if and $x.Computed (not $x.Optional) -}}{{continue}}{{end -}}
						{{ $x.AttributeName }} = {{$x.Type.Name | sampleData}}
					{{ end }}
				}
				` +
		"`" +
		`,
				Check: resource.ComposeAggregateTestCheckFunc(
					testAcc{{.ResourceName}}Exists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
				),
			},
			{
				ResourceName: resourceName,
				ImportState:  true,
				ImportStateVerify: true,
				ImportStateIdFunc: func(s *terraform.State) (string, error) {
					rs, ok := s.RootModule().Resources[resourceName]
					if !ok {
						return "", fmt.Errorf("Not found: %s", resourceName)
					}
					return rs.Primary.Attributes["{{.TerraformIDField.AttributeName}}"], nil
				},
			},
		},
	})
}

func testAccCheck{{.ResourceName}}Destroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_{{.ResourceName | snakeCase}}" {
			continue
		}

		remoteRecord, err := c.Find{{.ResourceName}}(rs.Primary.Attributes["{{.TerraformIDField.AttributeName}}"])

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if remoteRecord != nil {
			return fmt.Errorf("remote record (%s) still exists", remoteRecord.ID())
		}

	}
	return nil
}

func testAcc{{.ResourceName}}Exists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("%s does not exist in the statefile", resourceName)
		}

		c := client.NewClient(client.GetConfigFromEnv())
		record, err := c.Find{{.ResourceName}}(rs.Primary.Attributes["{{.TerraformIDField.AttributeName}}"])
		if err != nil {
			return fmt.Errorf("Unable to get remote record for %s: %v", resourceName, err)
		}

		if record == nil {
			return fmt.Errorf("Unable to get the remote record %s", resourceName)
		}

		return nil
	}
}

`
)


File: /cmd\mikrotik-codegen\internal\codegen\types.go
package codegen

const (
	typeString      = "String"
	typeInt64       = "Int64"
	typeList        = "List"
	typeSet         = "Set"
	typeBool        = "Bool"
	typeStringSlice = "StringSlice"
	typeIntSlice    = "IntSlice"
	typeUnknown     = "unknown"
)

type (
	basetype struct {
		typeName string
	}

	// Type represents Terraform field type to use for particular MikroTik field.
	Type interface {
		// Type returns a type name as string.
		// It must be stable for the same type.
		Name() string

		// Is checks whether two types are the same.
		Is(Type) bool
	}
)

var (
	StringType      Type = basetype{typeName: typeString}
	Int64Type       Type = basetype{typeName: typeInt64}
	ListType        Type = basetype{typeName: typeList}
	SetType         Type = basetype{typeName: typeSet}
	BoolType        Type = basetype{typeName: typeBool}
	StringSliceType Type = basetype{typeName: typeStringSlice}
	IntSliceType    Type = basetype{typeName: typeIntSlice}
	UnknownType     Type = basetype{typeName: typeUnknown}
)

func (b basetype) Name() string {
	return b.typeName
}

func (b basetype) Is(t Type) bool {
	return b.typeName == t.Name()
}


File: /cmd\mikrotik-codegen\internal\codegen\types_test.go
package codegen

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestTypeIs(t *testing.T) {
	testCases := []struct {
		name     string
		type1    Type
		type2    Type
		expected bool
	}{
		{
			name:     "int==int",
			type1:    Int64Type,
			type2:    Int64Type,
			expected: true,
		},
		{
			name:     "list==list",
			type1:    ListType,
			type2:    ListType,
			expected: true,
		},
		{
			name:  "int==string",
			type1: Int64Type,
			type2: StringType,
		},
		{
			name:  "list==string",
			type1: ListType,
			type2: StringType,
		},
		{
			name:  "list==set",
			type1: ListType,
			type2: SetType,
		},
		{
			name:  "bool==unknown",
			type1: BoolType,
			type2: UnknownType,
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			actual := tc.type1.Is(tc.type2)
			assert.Equal(t, tc.expected, actual)
		})
	}
}


File: /cmd\mikrotik-codegen\internal\utils\utils.go
package utils

import (
	"regexp"
	"strings"
)

// ToSnakeCase converts in string to snake_case
func ToSnakeCase(in string) string {
	var isPrevLower bool
	var buf strings.Builder

	for _, r := range in {
		if 'A' <= r && r <= 'Z' && isPrevLower {
			buf.WriteByte('_')
			buf.WriteString(strings.ToLower(string(r)))
			isPrevLower = false
			continue
		}

		isPrevLower = 'a' <= r && r <= 'z'
		buf.WriteString(strings.ToLower(string(r)))
	}

	return buf.String()
}

// FirstLower makes first symbol lowercase in the string
func FirstLower(s string) string {
	if len(s) < 1 {
		return s
	}
	if len(s) == 1 {
		return strings.ToLower(s)
	}

	return strings.ToLower(s[:1]) + s[1:]
}

// PascalCase makes every word in input string upper case and removes all not alpha-numeric symbols.
func PascalCase(s string) string {
	r := regexp.MustCompile(`[^0-9a-zA-Z-]+`)
	rClean := regexp.MustCompile(`[^0-9a-zA-Z]+`)
	s = string(r.ReplaceAll([]byte(s), []byte("-")))
	s = strings.Title(s)

	return string(rClean.ReplaceAll([]byte(s), []byte("")))
}


File: /cmd\mikrotik-codegen\internal\utils\utils_test.go
package utils

import (
	"testing"
)

func TestToSnakeCase(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected string
	}{
		{
			name:     "title case",
			input:    "ClientResourceName",
			expected: "client_resource_name",
		},
		{
			name:     "kebab case",
			input:    "clientResourceName",
			expected: "client_resource_name",
		},
		{
			name:     "all lowercase",
			input:    "clientresourcename",
			expected: "clientresourcename",
		},
		{
			name:     "several uppercase at beginning",
			input:    "IPAddress",
			expected: "ipaddress",
		},
		{
			name:     "several uppercase inside",
			input:    "DefaultHTTPConfig",
			expected: "default_httpconfig",
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := ToSnakeCase(tc.input)
			if result != tc.expected {
				t.Errorf(`
				expected %s,
				got %s`, tc.expected, result)
			}
		})
	}
}

func TestFirstLower(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected string
	}{
		{
			name:     "title case",
			input:    "ClientResourceName",
			expected: "clientResourceName",
		},
		{
			name:     "kebab case",
			input:    "clientResourceName",
			expected: "clientResourceName",
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := FirstLower(tc.input)
			if result != tc.expected {
				t.Errorf(`
				expected %s,
				got %s`, tc.expected, result)
			}
		})
	}
}
func TestPascalCase(t *testing.T) {
	testCases := []struct {
		name     string
		input    string
		expected string
	}{
		{
			name:     "already PascalCase",
			input:    "FieldNameInProperCase",
			expected: "FieldNameInProperCase",
		},
		{
			name:     "dashes",
			input:    "field-name-with-dashes",
			expected: "FieldNameWithDashes",
		},
		{
			name:     "dashes, underscores",
			input:    "field-name_with_dashes-and___underscores",
			expected: "FieldNameWithDashesAndUnderscores",
		},
		{
			name:     "other symbols",
			input:    "field/name  with+++++different||||symbols",
			expected: "FieldNameWithDifferentSymbols",
		},
		{
			name:     "consecutive upper-cased if one-letter word",
			input:    "field/name  with-a/b-testing",
			expected: "FieldNameWithABTesting",
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := PascalCase(tc.input)
			if result != tc.expected {
				t.Errorf(`
				expected %s,
				got %s`, tc.expected, result)
			}
		})
	}
}


File: /cmd\mikrotik-codegen\main.go
package main

import (
	"bytes"
	"errors"
	"flag"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	consoleinspected "github.com/ddelnano/terraform-provider-mikrotik/client/console-inspected"
	"github.com/ddelnano/terraform-provider-mikrotik/cmd/mikrotik-codegen/internal/codegen"
)

type (
	MikrotikConfiguration struct {
		CommandBasePath       string
		ResourceName          string
		Test                  bool
		SrcFile               string
		InspectDefinitionFile string
		QueryDefinition       bool
	}

	TerraformConfiguration struct {
		SrcFile    string
		StructName string
		AccTest    bool
	}

	GeneratorFunc func(w io.Writer) error
)

func main() {
	if err := realMain(os.Args[1:]); err != nil {
		log.Fatalf("execution failed: %v", err)
	}

	os.Exit(0)
}

func usage(w io.Writer) {
	_, _ = w.Write([]byte(`
Sub commands:
  mikrotik - generate MikroTik model
  terraform - generate Terraform resource
`))
}

func realMain(args []string) error {
	if len(args) < 1 {
		usage(flag.CommandLine.Output())
		return nil
	}
	subcommand := args[0]
	args = args[1:]

	var formatCode bool
	var destFile string
	var generator func() GeneratorFunc

	switch subcommand {
	case "terraform":
		config := TerraformConfiguration{}
		fs := flag.NewFlagSet("terraform", flag.ExitOnError)
		commonFlags(fs, &destFile, &formatCode)
		fs.StringVar(&config.SrcFile, "src", "", "Source file to parse struct from.")
		fs.StringVar(&config.StructName, "struct", "", "Name of a struct to process.")
		fs.BoolVar(&config.AccTest, "accTest", false, "Generate acceptance test instead.")
		_ = fs.Parse(args)

		startLine := 1
		lineStr := os.Getenv("GOLINE")
		if lineStr != "" {
			lineInt, err := strconv.Atoi(lineStr)
			if err != nil {
				return fmt.Errorf("fail to parse GOLINE: %v", err.Error())
			}
			startLine = lineInt
		}

		s, err := parseFile(config.SrcFile, startLine, config.StructName)
		if err != nil {
			return err
		}

		// If struct name is not provider, use one found in the parsed file.
		// See `ParseFile()` for details.
		if config.StructName == "" {
			config.StructName = s.Name
		}

		if destFile == "" {
			return errors.New("destination file must be set via flags or 'go:generate' mode must be used")
		}

		generator = func(s *codegen.Struct) func() GeneratorFunc {
			return func() GeneratorFunc {
				return func(w io.Writer) error {
					return codegen.GenerateResource(s, w)
				}
			}
		}(s)

		if config.AccTest {
			generator = func(s *codegen.Struct) func() GeneratorFunc {
				return func() GeneratorFunc {
					return func(w io.Writer) error {
						return codegen.GenerateResourceTest(s, w)
					}
				}
			}(s)

		}

	case "mikrotik":
		config := MikrotikConfiguration{}
		fs := flag.NewFlagSet("mikrotik", flag.ExitOnError)
		commonFlags(fs, &destFile, &formatCode)

		fs.StringVar(&config.ResourceName, "name", "", "Name of the resource to generate main code or test-file.")
		fs.StringVar(&config.CommandBasePath, "commandBase", "", "The command base path in MikroTik.")
		fs.StringVar(&config.SrcFile, "src", "", "Source file to parse struct from. Conflicts with 'commandBase'")
		fs.BoolVar(&config.Test, "test", false, "Generate resource test-file instead.")
		fs.StringVar(&config.InspectDefinitionFile, "inspect-definition-file", "",
			"[EXPERIMENTAL] File with command definition. Conflicts with query-definition.")
		fs.BoolVar(&config.QueryDefinition, "query-definition", false,
			"[EXPERIMENTAL] Query remote MikroTik device to fetch resource fields. Conflicts with inspect-definition-file.")

    _ = fs.Parse(args)

		if config.InspectDefinitionFile != "" && config.QueryDefinition {
			return errors.New("only one of inspect-definition-file or query-definition can be used")
		}

		consoleCommandDefinition := consoleinspected.ConsoleItem{}
		if config.InspectDefinitionFile != "" {
			fileBytes, err := os.ReadFile(config.InspectDefinitionFile)
			if err != nil {
				return err
			}

			consoleCommandDefinition, err = consoleinspected.Parse(string(fileBytes), consoleinspected.DefaultSplitStrategy)
			if err != nil {
				return err
			}
		}

		if config.QueryDefinition {
			var err error
			c := client.NewClient(client.GetConfigFromEnv())
			consoleCommandDefinition, err = c.InspectConsoleCommand(config.CommandBasePath + "/add")
			if err != nil {
				return err
			}
		}

		generator = func() GeneratorFunc {
			return func(w io.Writer) error {
				return codegen.GenerateMikrotikResource(config.ResourceName, config.CommandBasePath, consoleCommandDefinition, w)
			}
		}
		if config.Test {
			if config.CommandBasePath != "" {
				return errors.New("while generating test-file, 'commandBase' flags must not be set")
			}
			if config.SrcFile == "" {
				return errors.New("in test-file generating mode, 'src' flag must point to source file with struct.")
			}

			startLine := 1
			lineStr := os.Getenv("GOLINE")
			if lineStr != "" {
				lineInt, err := strconv.Atoi(lineStr)
				if err != nil {
					return fmt.Errorf("fail to parse GOLINE: %v", err.Error())
				}
				startLine = lineInt
			}

			s, err := parseFile(config.SrcFile, startLine, config.ResourceName)
			if err != nil {
				return err
			}

			generator = func() GeneratorFunc {
				return func(w io.Writer) error {
					return codegen.GenerateMikrotikResourceTest(config.ResourceName, s, w)
				}
			}
		}

	default:
		return errors.New("unsupported subcommand: " + subcommand)
	}

	var out io.Writer
	if destFile == "-" {
		out = os.Stdout
	} else {
		file, err := os.OpenFile(destFile, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0644)
		if err != nil {
			return err
		}
		out = file
		defer func() {
			file.Close()
		}()
	}
	writeHooks := []codegen.SourceWriteHookFunc{}
	if formatCode {
		writeHooks = append(writeHooks, codegen.SourceFormatHook)
	}

	var err error
	var buf bytes.Buffer

	if err := generator()(&buf); err != nil {
		return err
	}

	var result []byte
	result = buf.Bytes()
	for _, h := range writeHooks {
		result, err = h(result)
		if err != nil {
			return err
		}
	}

	if _, err := out.Write(result); err != nil {
		return err
	}

	return nil
}

func commonFlags(fs *flag.FlagSet, dest *string, formatCode *bool) {
	fs.StringVar(dest, "dest", "-", "File to write result to. Default: write to stdout.")
	fs.BoolVar(formatCode, "formatCode", true, "Whether to format resulting code. Useful for debugging to see raw source code right after generation.")
}

func parseFile(srcFile string, startLine int, structName string) (*codegen.Struct, error) {
	s, err := codegen.ParseFile(srcFile, startLine, structName)
	if err != nil {
		return nil, err
	}

	return s, nil
}


File: /docker\docker-compose.yml
---

services:
  routeros:
    image: mnazarenko/docker-routeros:${ROUTEROS_VERSION:-latest}
    environment:
      DEBUG: "N"
      DISPLAY: "web"
    ports:
      - 127.0.0.1:8728:8728
      - 127.0.0.1:2222:22
      - 127.0.0.1:8006:8006
      - 127.0.0.1:5900:5900
    volumes:
      - /dev/net/tun:/dev/net/tun
    cap_add:
      - "NET_ADMIN"
    stop_grace_period: 20s


File: /docs\index.md
---
page_title: "Provider: Mikrotik"
description: |-
  The mikrotik provider is used to interact with the resources supported by RouterOS.
---

# MIKROTIK Provider

The mikrotik provider is used to interact with the resources supported by RouterOS.
The provider needs to be configured with the proper credentials before it can be used.

## Requirements

* RouterOS v6.45.2+ (It may work with other versions but it is untested against other versions!)


## Example Usage
```terraform
# Configure the mikrotik Provider
provider "mikrotik" {
  host           = "hostname-of-server:8728"     # Or set MIKROTIK_HOST environment variable
  username       = "<username>"                  # Or set MIKROTIK_USER environment variable
  password       = "<password>"                  # Or set MIKROTIK_PASSWORD environment variable
  tls            = true                          # Or set MIKROTIK_TLS environment variable
  ca_certificate = "/path/to/ca/certificate.pem" # Or set MIKROTIK_CA_CERTIFICATE environment variable
  insecure       = true                          # Or set MIKROTIK_INSECURE environment variable
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Optional

- `ca_certificate` (String) Path to MikroTik's certificate authority
- `host` (String) Hostname of the MikroTik router
- `insecure` (Boolean) Insecure connection does not verify MikroTik's TLS certificate
- `password` (String, Sensitive) Password for MikroTik api
- `tls` (Boolean) Whether to use TLS when connecting to MikroTik or not
- `username` (String) User account for MikroTik api


File: /docs\resources\bgp_instance.md
# mikrotik_bgp_instance (Resource)
Creates a Mikrotik BGP Instance.

!> This resource will not be supported in RouterOS v7+.
Mikrotik has deprecated the underlying commands so future BGP support will need new resources created
(See [this issue](https://github.com/ddelnano/terraform-provider-mikrotik/issues/52) for status of this work).

## Example Usage
```terraform
resource "mikrotik_bgp_instance" "instance" {
  name      = "bgp-instance-name"
  as        = 65533
  router_id = "172.21.16.20"
  comment   = "test comment"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `as` (Number) The 32-bit BGP autonomous system number. Must be a value within 0 to 4294967295.
- `name` (String) The name of the BGP instance.
- `router_id` (String) BGP Router ID (for this instance). If set to 0.0.0.0, BGP will use one of router's IP addresses.

### Optional

- `client_to_client_reflection` (Boolean) In case this instance is a route reflector: whether to redistribute routes learned from one routing reflection client to other clients. Default: `true`.
- `cluster_id` (String) In case this instance is a route reflector: cluster ID of the router reflector cluster this instance belongs to. Default: `""`.
- `comment` (String) The comment of the BGP instance to be created. Default: `""`.
- `confederation` (Number) In case of BGP confederations: autonomous system number that identifies the [local] confederation as a whole. Default: `0`.
- `confederation_peers` (String) List of AS numbers internal to the [local] confederation. For example: `10,20,30-50`. Default: `""`.
- `disabled` (Boolean) Whether instance is disabled. Default: `false`.
- `ignore_as_path_len` (Boolean) Whether to ignore AS_PATH attribute in BGP route selection algorithm. Default: `false`.
- `out_filter` (String) Output routing filter chain used by all BGP peers belonging to this instance. Default: `""`.
- `redistribute_connected` (Boolean) If enabled, this BGP instance will redistribute the information about connected routes. Default: `false`.
- `redistribute_ospf` (Boolean) If enabled, this BGP instance will redistribute the information about routes learned by OSPF. Default: `false`.
- `redistribute_other_bgp` (Boolean) If enabled, this BGP instance will redistribute the information about routes learned by other BGP instances. Default: `false`.
- `redistribute_rip` (Boolean) If enabled, this BGP instance will redistribute the information about routes learned by RIP. Default: `false`.
- `redistribute_static` (Boolean) If enabled, the router will redistribute the information about static routes added to its routing database. Default: `false`.
- `routing_table` (String) Name of routing table this BGP instance operates on.  Default: `""`.

### Read-Only

- `id` (String) ID of this resource.

## Import
Import is supported using the following syntax:
```shell
# import with name of bgp instance
terraform import mikrotik_bgp_instance.instance bgp-instance-name
```


File: /docs\resources\bgp_peer.md
# mikrotik_bgp_peer (Resource)
Creates a MikroTik BGP Peer.

!> This resource will not be supported in RouterOS v7+.
Mikrotik has deprecated the underlying commands so future BGP support will need new resources created
(See [this issue](https://github.com/ddelnano/terraform-provider-mikrotik/issues/52) for status of this work).

## Example Usage
```terraform
resource "mikrotik_bpg_instance" "instance" {
  name      = "bgp-instance-name"
  as        = 65533
  router_id = "172.21.16.20"
  comment   = "test comment"
}

resource "mikrotik_bgp_peer" "peer" {
  name           = "bgp-peer-name"
  remote_as      = 65533
  remote_address = "172.21.16.20"
  instance       = mikrotik_bgp_instance.instance.name
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name` (String) The name of the BGP peer.
- `remote_address` (String) The address of the remote peer
- `remote_as` (Number) The 32-bit AS number of the remote peer.

### Optional

- `address_families` (String) The list of address families about which this peer will exchange routing information. Default: `ip`.
- `allow_as_in` (Number) How many times to allow own AS number in AS-PATH, before discarding a prefix.
- `as_override` (Boolean) If set, then all instances of remote peer's AS number in BGP AS PATH attribute are replaced with local AS number before sending route update to that peer. Default: `false`.
- `cisco_vpls_nlri_len_fmt` (String) VPLS NLRI length format type.
- `comment` (String) The comment of the BGP peer to be created.
- `default_originate` (String) The comment of the BGP peer to be created. Default: `never`.
- `disabled` (Boolean) Whether peer is disabled. Default: `false`.
- `hold_time` (String) Specifies the BGP Hold Time value to use when negotiating with peer Default: `3m`.
- `in_filter` (String) The name of the routing filter chain that is applied to the incoming routing information.
- `instance` (String) The name of the instance this peer belongs to. See Mikrotik bgp instance resource. Default: `default`.
- `keepalive_time` (String)
- `max_prefix_limit` (Number) Maximum number of prefixes to accept from a specific peer.
- `max_prefix_restart_time` (String) Minimum time interval after which peers can reestablish BGP session.
- `multihop` (Boolean) Specifies whether the remote peer is more than one hop away.
- `nexthop_choice` (String) Affects the outgoing NEXT_HOP attribute selection, either: 'default', 'force-self', or 'propagate' Default: `default`.
- `out_filter` (String) The name of the routing filter chain that is applied to the outgoing routing information.
- `passive` (Boolean) Name of the routing filter chain that is applied to the outgoing routing information. Default: `false`.
- `remote_port` (Number) Remote peers port to establish tcp session.
- `remove_private_as` (Boolean) If set, then BGP AS-PATH attribute is removed before sending out route update if attribute contains only private AS numbers.
- `route_reflect` (Boolean) Specifies whether this peer is route reflection client.
- `tcp_md5_key` (String) Key used to authenticate the connection with TCP MD5 signature as described in RFC 2385.
- `ttl` (String) Time To Live, the hop limit for TCP connection. This is a `string` field that can be 'default' or '0'-'255'. Default: `default`.
- `update_source` (String) If address is specified, this address is used as the source address of the outgoing TCP connection.
- `use_bfd` (Boolean) Whether to use BFD protocol for fast state detection.

### Read-Only

- `id` (String) Unique MikroTik identifier.

## Import
Import is supported using the following syntax:
```shell
# import with name of bgp peer
terraform import mikrotik_bgp_peer.peer bgp-peer-name
```


File: /docs\resources\bridge.md
# mikrotik_bridge (Resource)
Manages a bridge resource on remote MikroTik device.

## Example Usage
```terraform
resource "mikrotik_bridge" "bridge" {
  name           = "default_bridge"
  fast_forward   = true
  vlan_filtering = false
  comment        = "Default bridge"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name` (String) Name of the bridge interface

### Optional

- `comment` (String) Short description of the interface.
- `fast_forward` (Boolean) Special and faster case of FastPath which works only on bridges with 2 interfaces (enabled by default only for new bridges). Default: `true`.
- `vlan_filtering` (Boolean) Globally enables or disables VLAN functionality for bridge.

### Read-Only

- `id` (String) Unique ID for the instance.

## Import
Import is supported using the following syntax:
```shell
# import with name of bridge
terraform import mikrotik_bridge.bridge <bridge_name>
```


File: /docs\resources\bridge_port.md
# mikrotik_bridge_port (Resource)
Manages ports in bridge associations.

## Example Usage
```terraform
resource "mikrotik_bridge" "bridge" {
  name           = "default_bridge"
  fast_forward   = true
  vlan_filtering = false
  comment        = "Default bridge"
}

resource mikrotik_bridge_port "eth2port" {
  bridge    = mikrotik_bridge.bridge.name
  interface = "ether2"
  pvid      = 10
  comment   = "bridge port"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Optional

- `bridge` (String) The bridge interface the respective interface is grouped in.
- `comment` (String) Short description for this association.
- `interface` (String) Name of the interface.
- `pvid` (Number) Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. This property only has effect when vlan-filtering is set to yes.

### Read-Only

- `id` (String) Unique ID for the instance.

## Import
Import is supported using the following syntax:
```shell
# The ID argument (*19) is a MikroTik's internal id.
terraform import mikrotik_bridge_port.port1 "*19"
```


File: /docs\resources\bridge_vlan.md
# mikrotik_bridge_vlan (Resource)
Creates a MikroTik BridgeVlan.

## Example Usage
```terraform
resource "mikrotik_bridge" "default" {
  name = "main"
}

resource "mikrotik_bridge_vlan" "testacc" {
  bridge   = mikrotik_bridge.default.name
  tagged   = ["ether2", "vlan30"]
  untagged = ["ether3"]
  vlan_ids = [10, 30]
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `bridge` (String) The bridge interface which the respective VLAN entry is intended for.

### Optional

- `tagged` (Set of String) Interface list with a VLAN tag adding action in egress.
- `untagged` (Set of String) Interface list with a VLAN tag removing action in egress.
- `vlan_ids` (Set of Number) The list of VLAN IDs for certain port configuration. Ranges are not supported yet.

### Read-Only

- `id` (String) A unique ID for this resource.

## Import
Import is supported using the following syntax:
```shell
# import with id of bridge vlan
terraform import mikrotik_bridge_vlan.default "*2"
```


File: /docs\resources\dhcp_lease.md
# mikrotik_dhcp_lease (Resource)
Creates a DHCP lease on the MikroTik device.

## Example Usage
```terraform
resource "mikrotik_dhcp_lease" "file_server" {
  address    = "192.168.88.1"
  macaddress = "11:22:33:44:55:66"
  comment    = "file server"
  blocked    = "false"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `address` (String) The IP address of the DHCP lease to be created.
- `macaddress` (String) The MAC addreess of the DHCP lease to be created.

### Optional

- `blocked` (Boolean) Whether to block access for this DHCP client (true|false). Default: `false`.
- `comment` (String) The comment of the DHCP lease to be created.

### Read-Only

- `dynamic` (Boolean) Whether the dhcp lease is static or dynamic. Dynamic leases are not guaranteed to continue to be assigned to that specific device. Defaults to false.
- `hostname` (String) The hostname of the device
- `id` (String) Unique resource identifier.

## Import
Import is supported using the following syntax:
```shell
# The resource ID (*19) is a MikroTik's internal id.
# It can be obtained via CLI:
# [admin@MikroTik] /ip dhcp-server lease> :put [find where address=10.0.1.254]
# *19
terraform import mikrotik_dhcp_lease.file_server '*19'
```


File: /docs\resources\dhcp_server.md
# mikrotik_dhcp_server (Resource)
Manages a DHCP server resource within MikroTik device.

## Example Usage
```terraform
resource "mikrotik_pool" "bar" {
  name    = "dhcp-pool"
  ranges  = "10.10.10.100-10.10.10.200"
  comment = "Home devices"
}

resource "mikrotik_dhcp_server" "default" {
  address_pool  = mikrotik_pool.bar.name
  authoritative = "yes"
  disabled      = false
  interface     = "ether2"
  name          = "main-dhcp-server"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name` (String) Reference name.

### Optional

- `add_arp` (Boolean) Whether to add dynamic ARP entry. If set to no either ARP mode should be enabled on that interface or static ARP entries should be administratively defined.
- `address_pool` (String) IP pool, from which to take IP addresses for the clients. If set to static-only, then only the clients that have a static lease (added in lease submenu) will be allowed. Default: `static-only`.
- `authoritative` (String) Option changes the way how server responds to DHCP requests. Default: `yes`.
- `disabled` (Boolean) Disable this DHCP server instance. Default: `true`.
- `interface` (String) Interface on which server will be running. Default: `*0`.
- `lease_script` (String) Script that will be executed after lease is assigned or de-assigned. Internal "global" variables that can be used in the script.

### Read-Only

- `id` (String) Unique ID of this resource.

## Import
Import is supported using the following syntax:
```shell
terraform import mikrotik_dhcp_server.default <server-name>
```


File: /docs\resources\dhcp_server_network.md
# mikrotik_dhcp_server_network (Resource)
Manages a DHCP network resource within Mikrotik device.

## Example Usage
```terraform
resource "mikrotik_dhcp_server_network" "default" {
  address    = "192.168.100.0/24"
  netmask    = "0" # use mask from address
  gateway    = "192.168.100.1"
  dns_server = "192.168.100.2"
  comment    = "Default DHCP server network"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Optional

- `address` (String) The network DHCP server(s) will lease addresses from.
- `comment` (String)
- `dns_server` (String) The DHCP client will use these as the default DNS servers.
- `gateway` (String) The default gateway to be used by DHCP Client. Default: `0.0.0.0`.
- `netmask` (String) The actual network mask to be used by DHCP client. If set to '0' - netmask from network address will be used.

### Read-Only

- `id` (String) Unique ID of this resource.

## Import
Import is supported using the following syntax:
```shell
terraform import mikrotik_dhcp_server_network.default <network-id>
```


File: /docs\resources\dns_record.md
# mikrotik_dns_record (Resource)
Creates a DNS record on the MikroTik device.

## Example Usage
```terraform
resource "mikrotik_dns_record" "record" {
  name    = "example.domain.com"
  address = "192.168.88.1"
  ttl     = 300
}

resource "mikrotik_dns_record" "record_regexp" {
  regexp  = ".+\\.example\\.domain\\.com"
  address = "192.168.88.1"
  ttl     = 300
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `address` (String) The A record to be returend from the DNS hostname.

### Optional

- `comment` (String) The comment text associated with the DNS record.
- `name` (String) The name of the DNS hostname to be created.
- `regexp` (String) Regular expression against which domain names should be verified.
- `ttl` (Number) The ttl of the DNS record.

### Read-Only

- `id` (String) Unique ID of this resource.

## Import
Import is supported using the following syntax:
```shell
# The ID argument (*2) is a MikroTik's internal id.
# It can be obtained via CLI:
#
# [admin@MikroTik] /ip dns static> :put [find where address="192.168.88.1/24"]
# *2
terraform import mikrotik_dns_record.record "*2"
```


File: /docs\resources\firewall_filter_rule.md
# mikrotik_firewall_filter_rule (Resource)
Creates a MikroTik FirewallFilterRule.

## Example Usage
```terraform
resource "mikrotik_firewall_filter_rule" "https" {
  action             = "accept"
  chain              = "forward"
  comment            = "Web access to local HTTP server"
  connection_state   = ["new"]
  dst_port           = "443"
  in_interface       = "ether1"
  in_interface_list  = "local_lan"
  out_interface_list = "ether3"
  protocol           = "tcp"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `chain` (String) Specifies to which chain rule will be added. If the input does not match the name of an already defined chain, a new chain will be created.

### Optional

- `action` (String) Action to take if packet is matched by the rule. Default: `accept`.
- `comment` (String) Comment to the rule.
- `connection_state` (Set of String) Interprets the connection tracking analysis data for a particular packet.
- `dst_port` (String) List of destination port numbers or port number ranges.
- `in_interface` (String) Interface the packet has entered the router.
- `in_interface_list` (String) Set of interfaces defined in interface list. Works the same as in-interface.
- `out_interface_list` (String) Set of interfaces defined in interface list. Works the same as out-interface.
- `protocol` (String) Matches particular IP protocol specified by protocol name or number. Default: `tcp`.

### Read-Only

- `id` (String) Unique ID of this resource.

## Import
Import is supported using the following syntax:
```shell
terraform import mikrotik_firewall_filter_rule.forward[0] '*19'
```


File: /docs\resources\interface_list.md
# mikrotik_interface_list (Resource)
Allows to define set of interfaces for easier interface management.

## Example Usage
```terraform
resource "mikrotik_interface_list" "default" {
  name    = "ethernet_interfaces"
  comment = "All ethernet interfaces"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name` (String) Name of the interface list.

### Optional

- `comment` (String) Comment to this list.

### Read-Only

- `id` (String) Unique ID of this resource.

## Import
Import is supported using the following syntax:
```shell
terraform import mikrotik_interface_list.default <list-name>
```


File: /docs\resources\interface_list_member.md
# mikrotik_interface_list_member (Resource)
Allows to define set of interfaces for easier interface management.

## Example Usage
```terraform
resource "mikrotik_interface_list" "lan" {
  name = "lan"
}

resource "mikrotik_interface_list_member" "lan" {
  interface = "ether2"
  list      = mikrotik_interface_list.lan.name
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `interface` (String) Name of the interface.
- `list` (String) Name of the interface list

### Read-Only

- `id` (String) Unique ID of this resource.

## Import
Import is supported using the following syntax:
```shell
terraform import mikrotik_interface_list_member.default <remote-id>
```


File: /docs\resources\interface_wireguard.md
# mikrotik_interface_wireguard (Resource)
Creates a Mikrotik interface wireguard only supported by RouterOS v7+.

## Example Usage
```terraform
resource "mikrotik_interface_wireguard" "default" {
  name    = "wireguard-interface"
  comment = "new interface"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name` (String) Name of the interface wireguard.

### Optional

- `comment` (String) Comment associated with interface wireguard. Default: `""`.
- `disabled` (Boolean) Boolean for whether or not the interface wireguard is disabled. Default: `false`.
- `listen_port` (Number) Port for WireGuard service to listen on for incoming sessions. Default: `13231`.
- `mtu` (Number) Layer3 Maximum transmission unit. Default: `1420`.
- `private_key` (String, Sensitive) A base64 private key. If not specified, it will be automatically generated upon interface creation.

### Read-Only

- `id` (String) Identifier of this resource assigned by RouterOS
- `public_key` (String) A base64 public key is calculated from the private key.
- `running` (Boolean) Whether the interface is running.

## Import
Import is supported using the following syntax:
```shell
terraform import mikrotik_interface_wireguard.default <interface-name>
```


File: /docs\resources\interface_wireguard_peer.md
# mikrotik_interface_wireguard_peer (Resource)
Creates a Mikrotik Interface Wireguard Peer only supported by RouterOS v7+.

## Example Usage
```terraform
resource "mikrotik_interface_wireguard" "default" {
  name    = "wireguard-interface"
  comment = "new interface"
}

resource "mikrotik_interface_wireguard_peer" "default" {
  interface       = mikrotik_interface_wireguard.default.name
  public_key      = "v/oIzPyFm1FPHrqhytZgsKjU7mUToQHLrW+Tb5e601M="
  comment         = "peer-1"
  allowed_address = "0.0.0.0/0"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `interface` (String) Name of the WireGuard interface the peer belongs to.

### Optional

- `allowed_address` (String) List of IP (v4 or v6) addresses with CIDR masks from which incoming traffic for this peer is allowed and to which outgoing traffic for this peer is directed. The catch-all 0.0.0.0/0 may be specified for matching all IPv4 addresses, and ::/0 may be specified for matching all IPv6 addresses. Default: `""`.
- `comment` (String) Short description of the peer. Default: `""`.
- `disabled` (Boolean) Boolean for whether or not the interface peer is disabled. Default: `false`.
- `endpoint_address` (String) An endpoint IP or hostname can be left blank to allow remote connection from any address. Default: `""`.
- `endpoint_port` (Number) An endpoint port can be left blank to allow remote connection from any port. Default: `0`.
- `persistent_keepalive` (Number) A seconds interval, between 1 and 65535 inclusive, of how often to send an authenticated empty packet to the peer for the purpose of keeping a stateful firewall or NAT mapping valid persistently. For example, if the interface very rarely sends traffic, but it might at anytime receive traffic from a peer, and it is behind NAT, the interface might benefit from having a persistent keepalive interval of 25 seconds. Default: `0`.
- `preshared_key` (String) A base64 preshared key. Optional, and may be omitted. This option adds an additional layer of symmetric-key cryptography to be mixed into the already existing public-key cryptography, for post-quantum resistance. Default: `""`.
- `public_key` (String) The remote peer's calculated public key.

### Read-Only

- `id` (String) Identifier of this resource assigned by RouterOS

## Import
Import is supported using the following syntax:
```shell
terraform import mikrotik_interface_wireguard_peer.default <id>
```


File: /docs\resources\ipv6_address.md
# mikrotik_ipv6_address (Resource)
Creates a MikroTik Ipv6Address.

## Example Usage
```terraform
resource "mikrotik_ipv6_address" "lan" {
  address   = "2001::1/64"
  comment   = "LAN Network"
  interface = "ether1"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `address` (String) The IPv6 address and prefix length of the interface using slash notation.
- `interface` (String) The interface on which the IPv6 address is assigned.

### Optional

- `advertise` (Boolean) Whether to enable stateless address configuration. The prefix of that address is automatically advertised to hosts using ICMPv6 protocol. The option is set by default for addresses with prefix length 64. Default: `false`.
- `comment` (String) The comment for the IPv6 address assignment.
- `disabled` (Boolean) Whether to disable IPv6 address. Default: `false`.
- `eui_64` (Boolean) Whether to calculate EUI-64 address and use it as last 64 bits of the IPv6 address. Default: `false`.
- `from_pool` (String) Name of the pool from which prefix will be taken to construct IPv6 address taking last part of the address from address property. Default: `""`.
- `no_dad` (Boolean) If set indicates that address is anycast address and Duplicate Address Detection should not be performed. Default: `false`.

### Read-Only

- `id` (String) Unique identifier for this resource.

## Import
Import is supported using the following syntax:
```shell
# The ID argument (*19) is a MikroTik's internal id.
# It can be obtained via CLI:
#
# [admin@MikroTik] /ipv6 address> :put [find where address="192.168.88.1/24"]
# *19
terraform import mikrotik_ipv6_address.lan *19
```


File: /docs\resources\ip_address.md
# mikrotik_ip_address (Resource)
Assigns an IP address to an interface.

## Example Usage
```terraform
resource "mikrotik_ip_address" "lan" {
  address   = "192.168.88.1/24"
  comment   = "LAN Network"
  interface = "ether1"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `address` (String) The IP address and netmask of the interface using slash notation.
- `interface` (String) The interface on which the IP address is assigned.

### Optional

- `comment` (String) The comment for the IP address assignment.
- `disabled` (Boolean) Whether to disable IP address.

### Read-Only

- `id` (String) Unique ID of this resource.
- `network` (String) IP address for the network.

## Import
Import is supported using the following syntax:
```shell
# The ID argument (*19) is a MikroTik's internal id.
# It can be obtained via CLI:
#
# [admin@MikroTik] /ip address> :put [find where address="192.168.88.1/24"]
# *19
terraform import mikrotik_ip_address.lan '*19'
```


File: /docs\resources\pool.md
# mikrotik_pool (Resource)
Creates a Mikrotik IP Pool.

## Example Usage
```terraform
resource "mikrotik_pool" "pool" {
  name    = "pool-name"
  ranges  = "172.16.0.6-172.16.0.12"
  comment = "ip pool with range specified"
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name` (String) The name of IP pool.
- `ranges` (String) The IP range(s) of the pool. Multiple ranges can be specified, separated by commas: `172.16.0.6-172.16.0.12,172.16.0.50-172.16.0.60`.

### Optional

- `comment` (String) The comment of the IP Pool to be created.
- `next_pool` (String) The IP pool to pick next address from if current is exhausted.

### Read-Only

- `id` (String) ID of this resource.

## Import
Import is supported using the following syntax:
```shell
# The ID argument (*17) is a MikroTik's internal id.
# It can be obtained via CLI:
#
# [admin@MikroTik] /ip pool> :put [ find where name=pool-name]
# *17
terraform import mikrotik_pool.pool '*17'
```


File: /docs\resources\scheduler.md
# mikrotik_scheduler (Resource)
Creates a Mikrotik scheduler.

## Example Usage
```terraform
resource "mikrotik_scheduler" "scheduler" {
  name     = "scheduler-name"
  on_event = "scheduler-to-execute"
  # Run every 5 mins
  interval = 300
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name` (String) Name of the task.
- `on_event` (String) Name of the script to execute. It must exist `/system script`.

### Optional

- `interval` (Number) Interval between two script executions, if time interval is set to zero, the script is only executed at its start time, otherwise it is executed repeatedly at the time interval is specified.
- `start_date` (String) Date of the first script execution.
- `start_time` (String) Time of the first script execution.

### Read-Only

- `id` (String) Identifier of this resource assigned by RouterOS

## Import
Import is supported using the following syntax:
```shell
terraform import mikrotik_scheduler.scheduler scheduler-name
```


File: /docs\resources\script.md
# mikrotik_script (Resource)
Creates a MikroTik Script.

## Example Usage
```terraform
resource "mikrotik_script" "script" {
  name  = "script-name"
  owner = "admin"
  policy = [
    "ftp",
    "reboot",
  ]
  source = <<EOF
:put testing
EOF
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name` (String) The name of script.
- `policy` (List of String) What permissions the script has. This must be one of the following: ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon.
- `source` (String) The source code of the script. See the [MikroTik docs](https://wiki.mikrotik.com/wiki/Manual:Scripting) for the scripting language.

### Optional

- `dont_require_permissions` (Boolean) If the script requires permissions or not. Default: `false`.

### Read-Only

- `id` (String) ID of this resource.
- `owner` (String) The owner of the script.

## Import
Import is supported using the following syntax:
```shell
terraform import mikrotik_script.script script-name
```


File: /docs\resources\vlan_interface.md
# mikrotik_vlan_interface (Resource)
Manages Virtual Local Area Network (VLAN) interfaces.

## Example Usage
```terraform
resource "mikrotik_vlan_interface" "default" {
  interface = "ether2"
  mtu       = 1500
  name      = "vlan-20"
  vlan_id   = 20
}
```

<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name` (String) Interface name.

### Optional

- `disabled` (Boolean) Whether to create the interface in disabled state. Default: `false`.
- `interface` (String) Name of physical interface on top of which VLAN will work. Default: `*0`.
- `mtu` (Number) Layer3 Maximum transmission unit. Default: `1500`.
- `use_service_tag` (Boolean) 802.1ad compatible Service Tag. Default: `false`.
- `vlan_id` (Number) Virtual LAN identifier or tag that is used to distinguish VLANs. Must be equal for all computers that belong to the same VLAN. Default: `1`.

### Read-Only

- `id` (String) ID of the resource.

## Import
Import is supported using the following syntax:
```shell
terraform import mikrotik_vlan_interface.default <interface-name>
```


File: /docs\resources\wireless_interface.md
# mikrotik_wireless_interface (Resource)
Creates a MikroTik WirelessInterface.



<!-- schema generated by tfplugindocs -->
## Schema

### Required

- `name` (String) Name of the interface.

### Optional

- `disabled` (Boolean) Whether interface is disabled. Default: `true`.
- `hide_ssid` (Boolean) This property has an effect only in AP mode. Default: `false`.
- `master_interface` (String) Name of wireless interface that has virtual-ap capability. Virtual AP interface will only work if master interface is in ap-bridge, bridge, station or wds-slave mode. This property is only for virtual AP interfaces. Default: `""`.
- `mode` (String) Selection between different station and access point (AP) modes. Default: `station`.
- `security_profile` (String) Name of profile from security-profiles. Default: `default`.
- `ssid` (String) SSID (service set identifier) is a name that identifies wireless network.
- `vlan_id` (Number) VLAN identification number. Default: `1`.
- `vlan_mode` (String) Three VLAN modes are available: no-tag|use-service-tag|use-tag. Default: `no-tag`.

### Read-Only

- `id` (String) Unique identifier for this resource.




File: /examples\provider\provider.tf
# Configure the mikrotik Provider
provider "mikrotik" {
  host           = "hostname-of-server:8728"     # Or set MIKROTIK_HOST environment variable
  username       = "<username>"                  # Or set MIKROTIK_USER environment variable
  password       = "<password>"                  # Or set MIKROTIK_PASSWORD environment variable
  tls            = true                          # Or set MIKROTIK_TLS environment variable
  ca_certificate = "/path/to/ca/certificate.pem" # Or set MIKROTIK_CA_CERTIFICATE environment variable
  insecure       = true                          # Or set MIKROTIK_INSECURE environment variable
}


File: /examples\resources\mikrotik_bgp_instance\import.sh
# import with name of bgp instance
terraform import mikrotik_bgp_instance.instance bgp-instance-name


File: /examples\resources\mikrotik_bgp_instance\resource.tf
resource "mikrotik_bgp_instance" "instance" {
  name      = "bgp-instance-name"
  as        = 65533
  router_id = "172.21.16.20"
  comment   = "test comment"
}


File: /examples\resources\mikrotik_bgp_peer\import.sh
# import with name of bgp peer
terraform import mikrotik_bgp_peer.peer bgp-peer-name


File: /examples\resources\mikrotik_bgp_peer\resource.tf
resource "mikrotik_bpg_instance" "instance" {
  name      = "bgp-instance-name"
  as        = 65533
  router_id = "172.21.16.20"
  comment   = "test comment"
}

resource "mikrotik_bgp_peer" "peer" {
  name           = "bgp-peer-name"
  remote_as      = 65533
  remote_address = "172.21.16.20"
  instance       = mikrotik_bgp_instance.instance.name
}


File: /examples\resources\mikrotik_bridge\import.sh
# import with name of bridge
terraform import mikrotik_bridge.bridge <bridge_name>


File: /examples\resources\mikrotik_bridge\resource.tf
resource "mikrotik_bridge" "bridge" {
  name           = "default_bridge"
  fast_forward   = true
  vlan_filtering = false
  comment        = "Default bridge"
}


File: /examples\resources\mikrotik_bridge_port\import.sh
# The ID argument (*19) is a MikroTik's internal id.
terraform import mikrotik_bridge_port.port1 "*19"


File: /examples\resources\mikrotik_bridge_port\resource.tf
resource "mikrotik_bridge" "bridge" {
  name           = "default_bridge"
  fast_forward   = true
  vlan_filtering = false
  comment        = "Default bridge"
}

resource mikrotik_bridge_port "eth2port" {
  bridge    = mikrotik_bridge.bridge.name
  interface = "ether2"
  pvid      = 10
  comment   = "bridge port"
}


File: /examples\resources\mikrotik_bridge_vlan\import.sh
# import with id of bridge vlan
terraform import mikrotik_bridge_vlan.default "*2"


File: /examples\resources\mikrotik_bridge_vlan\resource.tf
resource "mikrotik_bridge" "default" {
  name = "main"
}

resource "mikrotik_bridge_vlan" "testacc" {
  bridge   = mikrotik_bridge.default.name
  tagged   = ["ether2", "vlan30"]
  untagged = ["ether3"]
  vlan_ids = [10, 30]
}


File: /examples\resources\mikrotik_dhcp_lease\import.sh
# The resource ID (*19) is a MikroTik's internal id.
# It can be obtained via CLI:
# [admin@MikroTik] /ip dhcp-server lease> :put [find where address=10.0.1.254]
# *19
terraform import mikrotik_dhcp_lease.file_server '*19'


File: /examples\resources\mikrotik_dhcp_lease\resource.tf
resource "mikrotik_dhcp_lease" "file_server" {
  address    = "192.168.88.1"
  macaddress = "11:22:33:44:55:66"
  comment    = "file server"
  blocked    = "false"
}


File: /examples\resources\mikrotik_dhcp_server\import.sh
terraform import mikrotik_dhcp_server.default <server-name>


File: /examples\resources\mikrotik_dhcp_server\resource.tf
resource "mikrotik_pool" "bar" {
  name    = "dhcp-pool"
  ranges  = "10.10.10.100-10.10.10.200"
  comment = "Home devices"
}

resource "mikrotik_dhcp_server" "default" {
  address_pool  = mikrotik_pool.bar.name
  authoritative = "yes"
  disabled      = false
  interface     = "ether2"
  name          = "main-dhcp-server"
}


File: /examples\resources\mikrotik_dhcp_server_network\import.sh
terraform import mikrotik_dhcp_server_network.default <network-id>


File: /examples\resources\mikrotik_dhcp_server_network\resource.tf
resource "mikrotik_dhcp_server_network" "default" {
  address    = "192.168.100.0/24"
  netmask    = "0" # use mask from address
  gateway    = "192.168.100.1"
  dns_server = "192.168.100.2"
  comment    = "Default DHCP server network"
}


File: /examples\resources\mikrotik_dns_record\import.sh
# The ID argument (*2) is a MikroTik's internal id.
# It can be obtained via CLI:
#
# [admin@MikroTik] /ip dns static> :put [find where address="192.168.88.1/24"]
# *2
terraform import mikrotik_dns_record.record "*2"


File: /examples\resources\mikrotik_dns_record\resource.tf
resource "mikrotik_dns_record" "record" {
  name    = "example.domain.com"
  address = "192.168.88.1"
  ttl     = 300
}

resource "mikrotik_dns_record" "record_regexp" {
  regexp  = ".+\\.example\\.domain\\.com"
  address = "192.168.88.1"
  ttl     = 300
}


File: /examples\resources\mikrotik_firewall_filter_rule\import.sh
terraform import mikrotik_firewall_filter_rule.forward[0] '*19'


File: /examples\resources\mikrotik_firewall_filter_rule\resource.tf
resource "mikrotik_firewall_filter_rule" "https" {
  action             = "accept"
  chain              = "forward"
  comment            = "Web access to local HTTP server"
  connection_state   = ["new"]
  dst_port           = "443"
  in_interface       = "ether1"
  in_interface_list  = "local_lan"
  out_interface_list = "ether3"
  protocol           = "tcp"
}


File: /examples\resources\mikrotik_interface_list\import.sh
terraform import mikrotik_interface_list.default <list-name>


File: /examples\resources\mikrotik_interface_list\resource.tf
resource "mikrotik_interface_list" "default" {
  name    = "ethernet_interfaces"
  comment = "All ethernet interfaces"
}


File: /examples\resources\mikrotik_interface_list_member\import.sh
terraform import mikrotik_interface_list_member.default <remote-id>


File: /examples\resources\mikrotik_interface_list_member\resource.tf
resource "mikrotik_interface_list" "lan" {
  name = "lan"
}

resource "mikrotik_interface_list_member" "lan" {
  interface = "ether2"
  list      = mikrotik_interface_list.lan.name
}


File: /examples\resources\mikrotik_interface_wireguard\import.sh
terraform import mikrotik_interface_wireguard.default <interface-name>


File: /examples\resources\mikrotik_interface_wireguard\resource.tf
resource "mikrotik_interface_wireguard" "default" {
  name    = "wireguard-interface"
  comment = "new interface"
}


File: /examples\resources\mikrotik_interface_wireguard_peer\import.sh
terraform import mikrotik_interface_wireguard_peer.default <id>


File: /examples\resources\mikrotik_interface_wireguard_peer\resource.tf
resource "mikrotik_interface_wireguard" "default" {
  name    = "wireguard-interface"
  comment = "new interface"
}

resource "mikrotik_interface_wireguard_peer" "default" {
  interface       = mikrotik_interface_wireguard.default.name
  public_key      = "v/oIzPyFm1FPHrqhytZgsKjU7mUToQHLrW+Tb5e601M="
  comment         = "peer-1"
  allowed_address = "0.0.0.0/0"
}


File: /examples\resources\mikrotik_ipv6_address\import.sh
# The ID argument (*19) is a MikroTik's internal id.
# It can be obtained via CLI:
#
# [admin@MikroTik] /ipv6 address> :put [find where address="192.168.88.1/24"]
# *19
terraform import mikrotik_ipv6_address.lan *19


File: /examples\resources\mikrotik_ipv6_address\resource.tf
resource "mikrotik_ipv6_address" "lan" {
  address   = "2001::1/64"
  comment   = "LAN Network"
  interface = "ether1"
}


File: /examples\resources\mikrotik_ip_address\import.sh
# The ID argument (*19) is a MikroTik's internal id.
# It can be obtained via CLI:
#
# [admin@MikroTik] /ip address> :put [find where address="192.168.88.1/24"]
# *19
terraform import mikrotik_ip_address.lan '*19'


File: /examples\resources\mikrotik_ip_address\resource.tf
resource "mikrotik_ip_address" "lan" {
  address   = "192.168.88.1/24"
  comment   = "LAN Network"
  interface = "ether1"
}


File: /examples\resources\mikrotik_pool\import.sh
# The ID argument (*17) is a MikroTik's internal id.
# It can be obtained via CLI:
#
# [admin@MikroTik] /ip pool> :put [ find where name=pool-name]
# *17
terraform import mikrotik_pool.pool '*17'


File: /examples\resources\mikrotik_pool\resource.tf
resource "mikrotik_pool" "pool" {
  name    = "pool-name"
  ranges  = "172.16.0.6-172.16.0.12"
  comment = "ip pool with range specified"
}


File: /examples\resources\mikrotik_scheduler\import.sh
terraform import mikrotik_scheduler.scheduler scheduler-name


File: /examples\resources\mikrotik_scheduler\resource.tf
resource "mikrotik_scheduler" "scheduler" {
  name     = "scheduler-name"
  on_event = "scheduler-to-execute"
  # Run every 5 mins
  interval = 300
}


File: /examples\resources\mikrotik_script\import.sh
terraform import mikrotik_script.script script-name


File: /examples\resources\mikrotik_script\resource.tf
resource "mikrotik_script" "script" {
  name  = "script-name"
  owner = "admin"
  policy = [
    "ftp",
    "reboot",
  ]
  source = <<EOF
:put testing
EOF
}


File: /examples\resources\mikrotik_vlan_interface\import.sh
terraform import mikrotik_vlan_interface.default <interface-name>


File: /examples\resources\mikrotik_vlan_interface\resource.tf
resource "mikrotik_vlan_interface" "default" {
  interface = "ether2"
  mtu       = 1500
  name      = "vlan-20"
  vlan_id   = 20
}


File: /go.mod
module github.com/ddelnano/terraform-provider-mikrotik

go 1.18

require (
	github.com/ddelnano/terraform-provider-mikrotik/client v0.0.0-00010101000000-000000000000
	github.com/hashicorp/terraform-plugin-docs v0.13.0
	github.com/hashicorp/terraform-plugin-framework v1.2.0
	github.com/hashicorp/terraform-plugin-framework-validators v0.10.0
	github.com/hashicorp/terraform-plugin-go v0.14.3
	github.com/hashicorp/terraform-plugin-log v0.8.0
	github.com/hashicorp/terraform-plugin-mux v0.8.0
	github.com/hashicorp/terraform-plugin-sdk/v2 v2.20.0
	github.com/stretchr/testify v1.8.0
)

require (
	github.com/Masterminds/goutils v1.1.1 // indirect
	github.com/Masterminds/semver/v3 v3.1.1 // indirect
	github.com/Masterminds/sprig/v3 v3.2.2 // indirect
	github.com/agext/levenshtein v1.2.2 // indirect
	github.com/apparentlymart/go-cidr v1.1.0 // indirect
	github.com/apparentlymart/go-textseg/v13 v13.0.0 // indirect
	github.com/armon/go-radix v1.0.0 // indirect
	github.com/bgentry/speakeasy v0.1.0 // indirect
	github.com/davecgh/go-spew v1.1.1 // indirect
	github.com/fatih/color v1.13.0 // indirect
	github.com/go-routeros/routeros v0.0.0-20210123142807-2a44d57c6730 // indirect
	github.com/golang/protobuf v1.5.3 // indirect
	github.com/google/go-cmp v0.5.9 // indirect
	github.com/google/uuid v1.3.0 // indirect
	github.com/hashicorp/errwrap v1.1.0 // indirect
	github.com/hashicorp/go-checkpoint v0.5.0 // indirect
	github.com/hashicorp/go-cleanhttp v0.5.2 // indirect
	github.com/hashicorp/go-cty v1.4.1-0.20200414143053-d3edf31b6320 // indirect
	github.com/hashicorp/go-hclog v1.4.0 // indirect
	github.com/hashicorp/go-multierror v1.1.1 // indirect
	github.com/hashicorp/go-plugin v1.4.8 // indirect
	github.com/hashicorp/go-uuid v1.0.3 // indirect
	github.com/hashicorp/go-version v1.6.0 // indirect
	github.com/hashicorp/hc-install v0.4.0 // indirect
	github.com/hashicorp/hcl/v2 v2.13.0 // indirect
	github.com/hashicorp/logutils v1.0.0 // indirect
	github.com/hashicorp/terraform-exec v0.17.2 // indirect
	github.com/hashicorp/terraform-json v0.14.0 // indirect
	github.com/hashicorp/terraform-registry-address v0.1.0 // indirect
	github.com/hashicorp/terraform-svchost v0.0.0-20200729002733-f050f53b9734 // indirect
	github.com/hashicorp/yamux v0.0.0-20181012175058-2f1d1f20f75d // indirect
	github.com/huandu/xstrings v1.3.2 // indirect
	github.com/imdario/mergo v0.3.13 // indirect
	github.com/mattn/go-colorable v0.1.12 // indirect
	github.com/mattn/go-isatty v0.0.14 // indirect
	github.com/mitchellh/cli v1.1.4 // indirect
	github.com/mitchellh/copystructure v1.2.0 // indirect
	github.com/mitchellh/go-testing-interface v1.14.1 // indirect
	github.com/mitchellh/go-wordwrap v1.0.0 // indirect
	github.com/mitchellh/mapstructure v1.5.0 // indirect
	github.com/mitchellh/reflectwalk v1.0.2 // indirect
	github.com/oklog/run v1.0.0 // indirect
	github.com/pmezard/go-difflib v1.0.0 // indirect
	github.com/posener/complete v1.2.3 // indirect
	github.com/russross/blackfriday v1.6.0 // indirect
	github.com/shopspring/decimal v1.3.1 // indirect
	github.com/spf13/cast v1.5.0 // indirect
	github.com/vmihailenco/msgpack v4.0.4+incompatible // indirect
	github.com/vmihailenco/msgpack/v4 v4.3.12 // indirect
	github.com/vmihailenco/tagparser v0.1.2 // indirect
	github.com/zclconf/go-cty v1.10.0 // indirect
	golang.org/x/crypto v0.17.0 // indirect
	golang.org/x/net v0.17.0 // indirect
	golang.org/x/sys v0.15.0 // indirect
	golang.org/x/text v0.14.0 // indirect
	google.golang.org/appengine v1.6.7 // indirect
	google.golang.org/genproto v0.0.0-20230410155749-daa745c078e1 // indirect
	google.golang.org/grpc v1.56.3 // indirect
	google.golang.org/protobuf v1.33.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)

replace github.com/ddelnano/terraform-provider-mikrotik/client => ./client


File: /go.sum
cloud.google.com/go v0.34.0/go.mod h1:aQUYkXzVsufM+DwF1aE+0xfcU+56JwCaLick0ClmMTw=
github.com/Masterminds/goutils v1.1.0/go.mod h1:8cTjp+g8YejhMuvIA5y2vz3BpJxksy863GQaJW2MFNU=
github.com/Masterminds/goutils v1.1.1 h1:5nUrii3FMTL5diU80unEVvNevw1nH4+ZV4DSLVJLSYI=
github.com/Masterminds/goutils v1.1.1/go.mod h1:8cTjp+g8YejhMuvIA5y2vz3BpJxksy863GQaJW2MFNU=
github.com/Masterminds/semver/v3 v3.1.1 h1:hLg3sBzpNErnxhQtUy/mmLR2I9foDujNK030IGemrRc=
github.com/Masterminds/semver/v3 v3.1.1/go.mod h1:VPu/7SZ7ePZ3QOrcuXROw5FAcLl4a0cBrbBpGY/8hQs=
github.com/Masterminds/sprig/v3 v3.2.0/go.mod h1:tWhwTbUTndesPNeF0C900vKoq283u6zp4APT9vaF3SI=
github.com/Masterminds/sprig/v3 v3.2.2 h1:17jRggJu518dr3QaafizSXOjKYp94wKfABxUmyxvxX8=
github.com/Masterminds/sprig/v3 v3.2.2/go.mod h1:UoaO7Yp8KlPnJIYWTFkMaqPUYKTfGFPhxNuwnnxkKlk=
github.com/Microsoft/go-winio v0.4.14/go.mod h1:qXqCSQ3Xa7+6tgxaGTIe4Kpcdsi+P8jBhyzoq1bpyYA=
github.com/Microsoft/go-winio v0.4.16 h1:FtSW/jqD+l4ba5iPBj9CODVtgfYAD8w2wS923g/cFDk=
github.com/Microsoft/go-winio v0.4.16/go.mod h1:XB6nPKklQyQ7GC9LdcBEcBl8PF76WugXOPRXwdLnMv0=
github.com/ProtonMail/go-crypto v0.0.0-20210428141323-04723f9f07d7 h1:YoJbenK9C67SkzkDfmQuVln04ygHj3vjZfd9FL+GmQQ=
github.com/ProtonMail/go-crypto v0.0.0-20210428141323-04723f9f07d7/go.mod h1:z4/9nQmJSSwwds7ejkxaJwO37dru3geImFUdJlaLzQo=
github.com/acomagu/bufpipe v1.0.3 h1:fxAGrHZTgQ9w5QqVItgzwj235/uYZYgbXitB+dLupOk=
github.com/acomagu/bufpipe v1.0.3/go.mod h1:mxdxdup/WdsKVreO5GpW4+M/1CE2sMG4jeGJ2sYmHc4=
github.com/agext/levenshtein v1.2.2 h1:0S/Yg6LYmFJ5stwQeRp6EeOcCbj7xiqQSdNelsXvaqE=
github.com/agext/levenshtein v1.2.2/go.mod h1:JEDfjyjHDjOF/1e4FlBE/PkbqA9OfWu2ki2W0IB5558=
github.com/anmitsu/go-shlex v0.0.0-20161002113705-648efa622239/go.mod h1:2FmKhYUyUczH0OGQWaF5ceTx0UBShxjsH6f8oGKYe2c=
github.com/apparentlymart/go-cidr v1.1.0 h1:2mAhrMoF+nhXqxTzSZMUzDHkLjmIHC+Zzn4tdgBZjnU=
github.com/apparentlymart/go-cidr v1.1.0/go.mod h1:EBcsNrHc3zQeuaeCeCtQruQm+n9/YjEn/vI25Lg7Gwc=
github.com/apparentlymart/go-dump v0.0.0-20190214190832-042adf3cf4a0 h1:MzVXffFUye+ZcSR6opIgz9Co7WcDx6ZcY+RjfFHoA0I=
github.com/apparentlymart/go-textseg v1.0.0/go.mod h1:z96Txxhf3xSFMPmb5X/1W05FF/Nj9VFpLOpjS5yuumk=
github.com/apparentlymart/go-textseg/v12 v12.0.0/go.mod h1:S/4uRK2UtaQttw1GenVJEynmyUenKwP++x/+DdGV/Ec=
github.com/apparentlymart/go-textseg/v13 v13.0.0 h1:Y+KvPE1NYz0xl601PVImeQfFyEy6iT90AvPUL1NNfNw=
github.com/apparentlymart/go-textseg/v13 v13.0.0/go.mod h1:ZK2fH7c4NqDTLtiYLvIkEghdlcqw7yxLeM89kiTRPUo=
github.com/armon/go-radix v0.0.0-20180808171621-7fddfc383310/go.mod h1:ufUuZ+zHj4x4TnLV4JWEpy2hxWSpsRywHrMgIH9cCH8=
github.com/armon/go-radix v1.0.0 h1:F4z6KzEeeQIMeLFa97iZU6vupzoecKdU5TX24SNppXI=
github.com/armon/go-radix v1.0.0/go.mod h1:ufUuZ+zHj4x4TnLV4JWEpy2hxWSpsRywHrMgIH9cCH8=
github.com/armon/go-socks5 v0.0.0-20160902184237-e75332964ef5/go.mod h1:wHh0iHkYZB8zMSxRWpUBQtwG5a7fFgvEO+odwuTv2gs=
github.com/bgentry/speakeasy v0.1.0 h1:ByYyxL9InA1OWqxJqqp2A5pYHUrCiAL6K3J+LKSsQkY=
github.com/bgentry/speakeasy v0.1.0/go.mod h1:+zsyZBPWlz7T6j88CTgSN5bM796AkVf0kBD4zp0CCIs=
github.com/creack/pty v1.1.9/go.mod h1:oKZEueFk5CKHvIhNR5MUki03XCEU+Q6VDXinZuGJ33E=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/emirpasic/gods v1.12.0 h1:QAUIPSaCu4G+POclxeqb3F+WPpdKqFGlw36+yOzGlrg=
github.com/emirpasic/gods v1.12.0/go.mod h1:YfzfFFoVP/catgzJb4IKIqXjX78Ha8FMSDh3ymbK86o=
github.com/fatih/color v1.7.0/go.mod h1:Zm6kSWBoL9eyXnKyktHP6abPY2pDugNf5KwzbycvMj4=
github.com/fatih/color v1.13.0 h1:8LOYc1KYPPmyKMuN8QV2DNRWNbLo6LZ0iLs8+mlH53w=
github.com/fatih/color v1.13.0/go.mod h1:kLAiJbzzSOZDVNGyDpeOxJ47H46qBXwg5ILebYFFOfk=
github.com/flynn/go-shlex v0.0.0-20150515145356-3f9db97f8568/go.mod h1:xEzjJPgXI435gkrCt3MPfRiAkVrwSbHsst4LCFVfpJc=
github.com/frankban/quicktest v1.14.3 h1:FJKSZTDHjyhriyC81FLQ0LY93eSai0ZyR/ZIkd3ZUKE=
github.com/gliderlabs/ssh v0.2.2/go.mod h1:U7qILu1NlMHj9FlMhZLlkCdDnU1DBEAqr0aevW3Awn0=
github.com/go-git/gcfg v1.5.0 h1:Q5ViNfGF8zFgyJWPqYwA7qGFoMTEiBmdlkcfRmpIMa4=
github.com/go-git/gcfg v1.5.0/go.mod h1:5m20vg6GwYabIxaOonVkTdrILxQMpEShl1xiMF4ua+E=
github.com/go-git/go-billy/v5 v5.2.0/go.mod h1:pmpqyWchKfYfrkb/UVH4otLvyi/5gJlGI4Hb3ZqZ3W0=
github.com/go-git/go-billy/v5 v5.3.1 h1:CPiOUAzKtMRvolEKw+bG1PLRpT7D3LIs3/3ey4Aiu34=
github.com/go-git/go-billy/v5 v5.3.1/go.mod h1:pmpqyWchKfYfrkb/UVH4otLvyi/5gJlGI4Hb3ZqZ3W0=
github.com/go-git/go-git-fixtures/v4 v4.2.1/go.mod h1:K8zd3kDUAykwTdDCr+I0per6Y6vMiRR/nnVTBtavnB0=
github.com/go-git/go-git/v5 v5.4.2 h1:BXyZu9t0VkbiHtqrsvdq39UDhGJTl1h55VW6CSC4aY4=
github.com/go-git/go-git/v5 v5.4.2/go.mod h1:gQ1kArt6d+n+BGd+/B/I74HwRTLhth2+zti4ihgckDc=
github.com/go-routeros/routeros v0.0.0-20210123142807-2a44d57c6730 h1:EuqwWLv/LPPjhvFqkeD2bz+FOlvw2DjvDI7vK8GVeyY=
github.com/go-routeros/routeros v0.0.0-20210123142807-2a44d57c6730/go.mod h1:em1mEqFKnoeQuQP9Sg7i26yaW8o05WwcNj7yLhrXxSQ=
github.com/go-test/deep v1.0.3 h1:ZrJSEWsXzPOxaZnFteGEfooLba+ju3FYIbOrS+rQd68=
github.com/golang/protobuf v1.1.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.2.0/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.1/go.mod h1:6lQm79b+lXiMfvg/cZm0SGofjICqVBUtrP5yJMmIC1U=
github.com/golang/protobuf v1.3.4/go.mod h1:vzj43D7+SQXF/4pzW/hwtAqwc6iTitCiVSaWz5lYuqw=
github.com/golang/protobuf v1.5.0/go.mod h1:FsONVRAS9T7sI+LIUmWTfcYkHO4aIWwzhcaSAoJOfIk=
github.com/golang/protobuf v1.5.3 h1:KhyjKVUg7Usr/dYsdSqoFveMYd5ko72D+zANwlG1mmg=
github.com/golang/protobuf v1.5.3/go.mod h1:XVQd3VNwM+JqD3oG2Ue2ip4fOMUkwXdXDdiuN0vRsmY=
github.com/google/go-cmp v0.3.0/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
github.com/google/go-cmp v0.3.1/go.mod h1:8QqcDgzrUqlUb/G2PQTWiueGozuR1884gddMywk6iLU=
github.com/google/go-cmp v0.5.5/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/go-cmp v0.5.8/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/go-cmp v0.5.9 h1:O2Tfq5qg4qc4AmwVlvv0oLiVAGB7enBSJ2x2DqQFi38=
github.com/google/go-cmp v0.5.9/go.mod h1:17dUlkBOakJ0+DkrSSNjCkIjxS6bF9zb3elmeNGIjoY=
github.com/google/uuid v1.1.1/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/google/uuid v1.1.2/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/google/uuid v1.3.0 h1:t6JiXgmwXMjEs8VusXIJk2BXHsn+wx8BZdTaoZ5fu7I=
github.com/google/uuid v1.3.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/hashicorp/errwrap v1.0.0/go.mod h1:YH+1FKiLXxHSkmPseP+kNlulaMuP3n2brvKWEqk/Jc4=
github.com/hashicorp/errwrap v1.1.0 h1:OxrOeh75EUXMY8TBjag2fzXGZ40LB6IKw45YeGUDY2I=
github.com/hashicorp/errwrap v1.1.0/go.mod h1:YH+1FKiLXxHSkmPseP+kNlulaMuP3n2brvKWEqk/Jc4=
github.com/hashicorp/go-checkpoint v0.5.0 h1:MFYpPZCnQqQTE18jFwSII6eUQrD/oxMFp3mlgcqk5mU=
github.com/hashicorp/go-checkpoint v0.5.0/go.mod h1:7nfLNL10NsxqO4iWuW6tWW0HjZuDrwkBuEQsVcpCOgg=
github.com/hashicorp/go-cleanhttp v0.5.0/go.mod h1:JpRdi6/HCYpAwUzNwuwqhbovhLtngrth3wmdIIUrZ80=
github.com/hashicorp/go-cleanhttp v0.5.1/go.mod h1:JpRdi6/HCYpAwUzNwuwqhbovhLtngrth3wmdIIUrZ80=
github.com/hashicorp/go-cleanhttp v0.5.2 h1:035FKYIWjmULyFRBKPs8TBQoi0x6d9G4xc9neXJWAZQ=
github.com/hashicorp/go-cleanhttp v0.5.2/go.mod h1:kO/YDlP8L1346E6Sodw+PrpBSV4/SoxCXGY6BqNFT48=
github.com/hashicorp/go-cty v1.4.1-0.20200414143053-d3edf31b6320 h1:1/D3zfFHttUKaCaGKZ/dR2roBXv0vKbSCnssIldfQdI=
github.com/hashicorp/go-cty v1.4.1-0.20200414143053-d3edf31b6320/go.mod h1:EiZBMaudVLy8fmjf9Npq1dq9RalhveqZG5w/yz3mHWs=
github.com/hashicorp/go-hclog v1.4.0 h1:ctuWFGrhFha8BnnzxqeRGidlEcQkDyL5u8J8t5eA11I=
github.com/hashicorp/go-hclog v1.4.0/go.mod h1:W4Qnvbt70Wk/zYJryRzDRU/4r0kIg0PVHBcfoyhpF5M=
github.com/hashicorp/go-multierror v1.0.0/go.mod h1:dHtQlpGsu+cZNNAkkCN/P3hoUDHhCYQXV3UM06sGGrk=
github.com/hashicorp/go-multierror v1.1.1 h1:H5DkEtf6CXdFp0N0Em5UCwQpXMWke8IA0+lD48awMYo=
github.com/hashicorp/go-multierror v1.1.1/go.mod h1:iw975J/qwKPdAO1clOe2L8331t/9/fmwbPZ6JB6eMoM=
github.com/hashicorp/go-plugin v1.4.8 h1:CHGwpxYDOttQOY7HOWgETU9dyVjOXzniXDqJcYJE1zM=
github.com/hashicorp/go-plugin v1.4.8/go.mod h1:viDMjcLJuDui6pXb8U4HVfb8AamCWhHGUjr2IrTF67s=
github.com/hashicorp/go-uuid v1.0.0/go.mod h1:6SBZvOh/SIDV7/2o3Jml5SYk/TvGqwFJ/bN7x4byOro=
github.com/hashicorp/go-uuid v1.0.3 h1:2gKiV6YVmrJ1i2CKKa9obLvRieoRGviZFL26PcT/Co8=
github.com/hashicorp/go-uuid v1.0.3/go.mod h1:6SBZvOh/SIDV7/2o3Jml5SYk/TvGqwFJ/bN7x4byOro=
github.com/hashicorp/go-version v1.2.0/go.mod h1:fltr4n8CU8Ke44wwGCBoEymUuxUHl09ZGVZPK5anwXA=
github.com/hashicorp/go-version v1.5.0/go.mod h1:fltr4n8CU8Ke44wwGCBoEymUuxUHl09ZGVZPK5anwXA=
github.com/hashicorp/go-version v1.6.0 h1:feTTfFNnjP967rlCxM/I9g701jU+RN74YKx2mOkIeek=
github.com/hashicorp/go-version v1.6.0/go.mod h1:fltr4n8CU8Ke44wwGCBoEymUuxUHl09ZGVZPK5anwXA=
github.com/hashicorp/hc-install v0.4.0 h1:cZkRFr1WVa0Ty6x5fTvL1TuO1flul231rWkGH92oYYk=
github.com/hashicorp/hc-install v0.4.0/go.mod h1:5d155H8EC5ewegao9A4PUTMNPZaq+TbOzkJJZ4vrXeI=
github.com/hashicorp/hcl/v2 v2.13.0 h1:0Apadu1w6M11dyGFxWnmhhcMjkbAiKCv7G1r/2QgCNc=
github.com/hashicorp/hcl/v2 v2.13.0/go.mod h1:e4z5nxYlWNPdDSNYX+ph14EvWYMFm3eP0zIUqPc2jr0=
github.com/hashicorp/logutils v1.0.0 h1:dLEQVugN8vlakKOUE3ihGLTZJRB4j+M2cdTm/ORI65Y=
github.com/hashicorp/logutils v1.0.0/go.mod h1:QIAnNjmIWmVIIkWDTG1z5v++HQmx9WQRO+LraFDTW64=
github.com/hashicorp/terraform-exec v0.17.2 h1:EU7i3Fh7vDUI9nNRdMATCEfnm9axzTnad8zszYZ73Go=
github.com/hashicorp/terraform-exec v0.17.2/go.mod h1:tuIbsL2l4MlwwIZx9HPM+LOV9vVyEfBYu2GsO1uH3/8=
github.com/hashicorp/terraform-json v0.14.0 h1:sh9iZ1Y8IFJLx+xQiKHGud6/TSUCM0N8e17dKDpqV7s=
github.com/hashicorp/terraform-json v0.14.0/go.mod h1:5A9HIWPkk4e5aeeXIBbkcOvaZbIYnAIkEyqP2pNSckM=
github.com/hashicorp/terraform-plugin-docs v0.13.0 h1:6e+VIWsVGb6jYJewfzq2ok2smPzZrt1Wlm9koLeKazY=
github.com/hashicorp/terraform-plugin-docs v0.13.0/go.mod h1:W0oCmHAjIlTHBbvtppWHe8fLfZ2BznQbuv8+UD8OucQ=
github.com/hashicorp/terraform-plugin-framework v1.2.0 h1:MZjFFfULnFq8fh04FqrKPcJ/nGpHOvX4buIygT3MSNY=
github.com/hashicorp/terraform-plugin-framework v1.2.0/go.mod h1:nToI62JylqXDq84weLJ/U3umUsBhZAaTmU0HXIVUOcw=
github.com/hashicorp/terraform-plugin-framework-validators v0.10.0 h1:4L0tmy/8esP6OcvocVymw52lY0HyQ5OxB7VNl7k4bS0=
github.com/hashicorp/terraform-plugin-framework-validators v0.10.0/go.mod h1:qdQJCdimB9JeX2YwOpItEu+IrfoJjWQ5PhLpAOMDQAE=
github.com/hashicorp/terraform-plugin-go v0.14.3 h1:nlnJ1GXKdMwsC8g1Nh05tK2wsC3+3BL/DBBxFEki+j0=
github.com/hashicorp/terraform-plugin-go v0.14.3/go.mod h1:7ees7DMZ263q8wQ6E4RdIdR6nHHJtrdt4ogX5lPkX1A=
github.com/hashicorp/terraform-plugin-log v0.8.0 h1:pX2VQ/TGKu+UU1rCay0OlzosNKe4Nz1pepLXj95oyy0=
github.com/hashicorp/terraform-plugin-log v0.8.0/go.mod h1:1myFrhVsBLeylQzYYEV17VVjtG8oYPRFdaZs7xdW2xs=
github.com/hashicorp/terraform-plugin-mux v0.8.0 h1:WCTP66mZ+iIaIrCNJnjPEYnVjawTshnDJu12BcXK1EI=
github.com/hashicorp/terraform-plugin-mux v0.8.0/go.mod h1:vdW0daEi8Kd4RFJmet5Ot+SIVB/B8SwQVJiYKQwdCy8=
github.com/hashicorp/terraform-plugin-sdk/v2 v2.20.0 h1:+KxZULPsbjpAVoP0WNj/8aVW6EqpcX5JcUcQ5wl7Da4=
github.com/hashicorp/terraform-plugin-sdk/v2 v2.20.0/go.mod h1:DwGJG3KNxIPluVk6hexvDfYR/MS/eKGpiztJoT3Bbbw=
github.com/hashicorp/terraform-registry-address v0.1.0 h1:W6JkV9wbum+m516rCl5/NjKxCyTVaaUBbzYcMzBDO3U=
github.com/hashicorp/terraform-registry-address v0.1.0/go.mod h1:EnyO2jYO6j29DTHbJcm00E5nQTFeTtyZH3H5ycydQ5A=
github.com/hashicorp/terraform-svchost v0.0.0-20200729002733-f050f53b9734 h1:HKLsbzeOsfXmKNpr3GiT18XAblV0BjCbzL8KQAMZGa0=
github.com/hashicorp/terraform-svchost v0.0.0-20200729002733-f050f53b9734/go.mod h1:kNDNcF7sN4DocDLBkQYz73HGKwN1ANB1blq4lIYLYvg=
github.com/hashicorp/yamux v0.0.0-20181012175058-2f1d1f20f75d h1:kJCB4vdITiW1eC1vq2e6IsrXKrZit1bv/TDYFGMp4BQ=
github.com/hashicorp/yamux v0.0.0-20181012175058-2f1d1f20f75d/go.mod h1:+NfK9FKeTrX5uv1uIXGdwYDTeHna2qgaIlx54MXqjAM=
github.com/huandu/xstrings v1.3.1/go.mod h1:y5/lhBue+AyNmUVz9RLU9xbLR0o4KIIExikq4ovT0aE=
github.com/huandu/xstrings v1.3.2 h1:L18LIDzqlW6xN2rEkpdV8+oL/IXWJ1APd+vsdYy4Wdw=
github.com/huandu/xstrings v1.3.2/go.mod h1:y5/lhBue+AyNmUVz9RLU9xbLR0o4KIIExikq4ovT0aE=
github.com/imdario/mergo v0.3.11/go.mod h1:jmQim1M+e3UYxmgPu/WyfjB3N3VflVyUjjjwH0dnCYA=
github.com/imdario/mergo v0.3.12/go.mod h1:jmQim1M+e3UYxmgPu/WyfjB3N3VflVyUjjjwH0dnCYA=
github.com/imdario/mergo v0.3.13 h1:lFzP57bqS/wsqKssCGmtLAb8A0wKjLGrve2q3PPVcBk=
github.com/imdario/mergo v0.3.13/go.mod h1:4lJ1jqUDcsbIECGy0RUJAXNIhg+6ocWgb1ALK2O4oXg=
github.com/jbenet/go-context v0.0.0-20150711004518-d14ea06fba99 h1:BQSFePA1RWJOlocH6Fxy8MmwDt+yVQYULKfN0RoTN8A=
github.com/jbenet/go-context v0.0.0-20150711004518-d14ea06fba99/go.mod h1:1lJo3i6rXxKeerYnT8Nvf0QmHCRC1n8sfWVwXF2Frvo=
github.com/jessevdk/go-flags v1.5.0/go.mod h1:Fw0T6WPc1dYxT4mKEZRfG5kJhaTDP9pj1c2EWnYs/m4=
github.com/jhump/protoreflect v1.6.0 h1:h5jfMVslIg6l29nsMs0D8Wj17RDVdNYti0vDN/PZZoE=
github.com/kevinburke/ssh_config v0.0.0-20201106050909-4977a11b4351 h1:DowS9hvgyYSX4TO5NpyC606/Z4SxnNYbT+WX27or6Ck=
github.com/kevinburke/ssh_config v0.0.0-20201106050909-4977a11b4351/go.mod h1:CT57kijsi8u/K/BOFA39wgDQJ9CxiF4nAY/ojJ6r6mM=
github.com/konsorten/go-windows-terminal-sequences v1.0.1/go.mod h1:T0+1ngSBFLxvqU3pZ+m/2kptfBszLMUkC4ZK/EgS/cQ=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pretty v0.2.1/go.mod h1:ipq/a2n7PKx3OHsz4KJII5eveXtPO4qwEXGdVfWzfnI=
github.com/kr/pretty v0.3.0 h1:WgNl7dwNpEZ6jJ9k1snq4pZsg7DOEN8hP9Xw0Tsjwk0=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/kr/text v0.2.0 h1:5Nx0Ya0ZqY2ygV366QzturHI13Jq95ApcVaJBhpS+AY=
github.com/kr/text v0.2.0/go.mod h1:eLer722TekiGuMkidMxC/pM04lWEeraHUUmBw8l2grE=
github.com/kylelemons/godebug v0.0.0-20170820004349-d65d576e9348/go.mod h1:B69LEHPfb2qLo0BaaOLcbitczOKLWTsrBG9LczfCD4k=
github.com/kylelemons/godebug v1.1.0 h1:RPNrshWIDI6G2gRW9EHilWtl7Z6Sb1BR0xunSBf0SNc=
github.com/matryer/is v1.2.0/go.mod h1:2fLPjFQM9rhQ15aVEtbuwhJinnOqrmgXPNdZsdwlWXA=
github.com/mattn/go-colorable v0.0.9/go.mod h1:9vuHe8Xs5qXnSaW/c/ABM9alt+Vo+STaOChaDxuIBZU=
github.com/mattn/go-colorable v0.1.9/go.mod h1:u6P/XSegPjTcexA+o6vUJrdnUu04hMope9wVRipJSqc=
github.com/mattn/go-colorable v0.1.12 h1:jF+Du6AlPIjs2BiUiQlKOX0rt3SujHxPnksPKZbaA40=
github.com/mattn/go-colorable v0.1.12/go.mod h1:u5H1YNBxpqRaxsYJYSkiCWKzEfiAb1Gb520KVy5xxl4=
github.com/mattn/go-isatty v0.0.3/go.mod h1:M+lRXTBqGeGNdLjl/ufCoiOlB5xdOkqRJdNxMWT7Zi4=
github.com/mattn/go-isatty v0.0.12/go.mod h1:cbi8OIDigv2wuxKPP5vlRcQ1OAZbq2CE4Kysco4FUpU=
github.com/mattn/go-isatty v0.0.14 h1:yVuAays6BHfxijgZPzw+3Zlu5yQgKGP2/hcQbHb7S9Y=
github.com/mattn/go-isatty v0.0.14/go.mod h1:7GGIvUiUoEMVVmxf/4nioHXj79iQHKdU27kJ6hsGG94=
github.com/mitchellh/cli v1.1.4 h1:qj8czE26AU4PbiaPXK5uVmMSM+V5BYsFBiM9HhGRLUA=
github.com/mitchellh/cli v1.1.4/go.mod h1:vTLESy5mRhKOs9KDp0/RATawxP1UqBmdrpVRMnpcvKQ=
github.com/mitchellh/copystructure v1.0.0/go.mod h1:SNtv71yrdKgLRyLFxmLdkAbkKEFWgYaq1OVrnRcwhnw=
github.com/mitchellh/copystructure v1.2.0 h1:vpKXTN4ewci03Vljg/q9QvCGUDttBOGBIa15WveJJGw=
github.com/mitchellh/copystructure v1.2.0/go.mod h1:qLl+cE2AmVv+CoeAwDPye/v+N2HKCj9FbZEVFJRxO9s=
github.com/mitchellh/go-homedir v1.1.0 h1:lukF9ziXFxDFPkA1vsr5zpc1XuPDn/wFntq5mG+4E0Y=
github.com/mitchellh/go-homedir v1.1.0/go.mod h1:SfyaCUpYCn1Vlf4IUYiD9fPX4A5wJrkLzIz1N1q0pr0=
github.com/mitchellh/go-testing-interface v1.14.1 h1:jrgshOhYAUVNMAJiKbEu7EqAwgJJ2JqpQmpLJOu07cU=
github.com/mitchellh/go-testing-interface v1.14.1/go.mod h1:gfgS7OtZj6MA4U1UrDRp04twqAjfvlZyCfX3sDjEym8=
github.com/mitchellh/go-wordwrap v1.0.0 h1:6GlHJ/LTGMrIJbwgdqdl2eEH8o+Exx/0m8ir9Gns0u4=
github.com/mitchellh/go-wordwrap v1.0.0/go.mod h1:ZXFpozHsX6DPmq2I0TCekCxypsnAUbP2oI0UX1GXzOo=
github.com/mitchellh/mapstructure v1.5.0 h1:jeMsZIYE/09sWLaz43PL7Gy6RuMjD2eJVyuac5Z2hdY=
github.com/mitchellh/mapstructure v1.5.0/go.mod h1:bFUtVrKA4DC2yAKiSyO/QUcy7e+RRV2QTWOzhPopBRo=
github.com/mitchellh/reflectwalk v1.0.0/go.mod h1:mSTlrgnPZtwu0c4WaC2kGObEpuNDbx0jmZXqmk4esnw=
github.com/mitchellh/reflectwalk v1.0.2 h1:G2LzWKi524PWgd3mLHV8Y5k7s6XUvT0Gef6zxSIeXaQ=
github.com/mitchellh/reflectwalk v1.0.2/go.mod h1:mSTlrgnPZtwu0c4WaC2kGObEpuNDbx0jmZXqmk4esnw=
github.com/niemeyer/pretty v0.0.0-20200227124842-a10e7caefd8e/go.mod h1:zD1mROLANZcx1PVRCS0qkT7pwLkGfwJo4zjcN/Tysno=
github.com/oklog/run v1.0.0 h1:Ru7dDtJNOyC66gQ5dQmaCa0qIsAUFY3sFpK1Xk8igrw=
github.com/oklog/run v1.0.0/go.mod h1:dlhp/R75TPv97u0XWUtDeV/lRKWPKSdTuV0TZvrmrQA=
github.com/pkg/errors v0.8.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/posener/complete v1.1.1/go.mod h1:em0nMJCgc9GFtwrmVmEMR/ZL6WyhyjMBndrE9hABlRI=
github.com/posener/complete v1.2.3 h1:NP0eAhjcjImqslEwo/1hq7gpajME0fTLTezBKDqfXqo=
github.com/posener/complete v1.2.3/go.mod h1:WZIdtGGp+qx0sLrYKtIRAruyNpv6hFCicSgv7Sy7s/s=
github.com/rogpeppe/go-internal v1.6.1 h1:/FiVV8dS/e+YqF2JvO3yXRFbBLTIuSDkuC7aBOAvL+k=
github.com/russross/blackfriday v1.6.0 h1:KqfZb0pUVN2lYqZUYRddxF4OR8ZMURnJIG5Y3VRLtww=
github.com/russross/blackfriday v1.6.0/go.mod h1:ti0ldHuxg49ri4ksnFxlkCfN+hvslNlmVHqNRXXJNAY=
github.com/sebdah/goldie v1.0.0/go.mod h1:jXP4hmWywNEwZzhMuv2ccnqTSFpuq8iyQhtQdkkZBH4=
github.com/sergi/go-diff v1.1.0/go.mod h1:STckp+ISIX8hZLjrqAeVduY0gWCT9IjLuqbuNXdaHfM=
github.com/sergi/go-diff v1.2.0 h1:XU+rvMAioB0UC3q1MFrIQy4Vo5/4VsRDQQXHsEya6xQ=
github.com/shopspring/decimal v1.2.0/go.mod h1:DKyhrW/HYNuLGql+MJL6WCR6knT2jwCFRcu2hWCYk4o=
github.com/shopspring/decimal v1.3.1 h1:2Usl1nmF/WZucqkFZhnfFYxxxu8LG21F6nPQBE5gKV8=
github.com/shopspring/decimal v1.3.1/go.mod h1:DKyhrW/HYNuLGql+MJL6WCR6knT2jwCFRcu2hWCYk4o=
github.com/sirupsen/logrus v1.4.1/go.mod h1:ni0Sbl8bgC9z8RoU9G6nDWqqs/fq4eDPysMBDgk/93Q=
github.com/spf13/cast v1.3.1/go.mod h1:Qx5cxh0v+4UWYiBimWS+eyWzqEqokIECu5etghLkUJE=
github.com/spf13/cast v1.5.0 h1:rj3WzYc11XZaIZMPKmwP96zkFEnnAmV8s6XbB2aY32w=
github.com/spf13/cast v1.5.0/go.mod h1:SpXXQ5YoyJw6s3/6cMTQuxvgRl3PCJiyaX9p6b155UU=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.1.1/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.4.0/go.mod h1:YvHI0jy2hoMjB+UWwv71VJQ9isScKT/TqJzVSSt89Yw=
github.com/stretchr/testify v1.2.2/go.mod h1:a8OnRcib4nhh0OaRAV+Yts87kKdq0PP7pXfy6kDkUVs=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
github.com/stretchr/testify v1.5.1/go.mod h1:5W2xD1RspED5o8YsWQXVCued0rvSQ+mT+I5cxcmMvtA=
github.com/stretchr/testify v1.6.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.7.0/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.7.1/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/stretchr/testify v1.7.2/go.mod h1:R6va5+xMeoiuVRoj+gSkQ7d3FALtqAAGI1FQKckRals=
github.com/stretchr/testify v1.8.0 h1:pSgiaMZlXftHpm5L7V1+rVB+AZJydKsMxsQBIJw4PKk=
github.com/stretchr/testify v1.8.0/go.mod h1:yNjHg4UonilssWZ8iaSj1OCr/vHnekPRkoO+kdMU+MU=
github.com/vmihailenco/msgpack v3.3.3+incompatible/go.mod h1:fy3FlTQTDXWkZ7Bh6AcGMlsjHatGryHQYUTf1ShIgkk=
github.com/vmihailenco/msgpack v4.0.4+incompatible h1:dSLoQfGFAo3F6OoNhwUmLwVgaUXK79GlxNBwueZn0xI=
github.com/vmihailenco/msgpack v4.0.4+incompatible/go.mod h1:fy3FlTQTDXWkZ7Bh6AcGMlsjHatGryHQYUTf1ShIgkk=
github.com/vmihailenco/msgpack/v4 v4.3.12 h1:07s4sz9IReOgdikxLTKNbBdqDMLsjPKXwvCazn8G65U=
github.com/vmihailenco/msgpack/v4 v4.3.12/go.mod h1:gborTTJjAo/GWTqqRjrLCn9pgNN+NXzzngzBKDPIqw4=
github.com/vmihailenco/tagparser v0.1.1/go.mod h1:OeAg3pn3UbLjkWt+rN9oFYB6u/cQgqMEUPoW2WPyhdI=
github.com/vmihailenco/tagparser v0.1.2 h1:gnjoVuB/kljJ5wICEEOpx98oXMWPLj22G67Vbd1qPqc=
github.com/vmihailenco/tagparser v0.1.2/go.mod h1:OeAg3pn3UbLjkWt+rN9oFYB6u/cQgqMEUPoW2WPyhdI=
github.com/xanzy/ssh-agent v0.3.0 h1:wUMzuKtKilRgBAD1sUb8gOwwRr2FGoBVumcjoOACClI=
github.com/xanzy/ssh-agent v0.3.0/go.mod h1:3s9xbODqPuuhK9JV1R321M/FlMZSBvE5aY6eAcqrDh0=
github.com/zclconf/go-cty v1.1.0/go.mod h1:xnAOWiHeOqg2nWS62VtQ7pbOu17FtxJNW8RLEih+O3s=
github.com/zclconf/go-cty v1.2.0/go.mod h1:hOPWgoHbaTUnI5k4D2ld+GRpFJSCe6bCM7m1q/N4PQ8=
github.com/zclconf/go-cty v1.10.0 h1:mp9ZXQeIcN8kAwuqorjH+Q+njbJKjLrvB2yIh4q7U+0=
github.com/zclconf/go-cty v1.10.0/go.mod h1:vVKLxnk3puL4qRAv72AO+W99LUD4da90g3uUAzyuvAk=
github.com/zclconf/go-cty-debug v0.0.0-20191215020915-b22d67c1ba0b/go.mod h1:ZRKQfBXbGkpdV6QMzT3rU1kSTAnfu1dO8dPKjYprgj8=
golang.org/x/crypto v0.0.0-20190219172222-a4c6cb3142f2/go.mod h1:6SG95UA2DQfeDnfUPMdvaQW0Q7yPrPDi9nlGo2tz2b4=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20200414173820-0848c9571904/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20200820211705-5c72a883971a/go.mod h1:LzIPMQfyMNhhGPhUkYOs5KpL4U8rLKemX1yGLhDgUto=
golang.org/x/crypto v0.0.0-20210322153248-0c34fe9e7dc2/go.mod h1:T9bdIzuCu7OtxOm1hfPfRQxPLYneinmdGuTeoZ9dtd4=
golang.org/x/crypto v0.0.0-20210421170649-83a5a9bb288b/go.mod h1:T9bdIzuCu7OtxOm1hfPfRQxPLYneinmdGuTeoZ9dtd4=
golang.org/x/crypto v0.0.0-20210616213533-5ff15b29337e/go.mod h1:GvvjBRRGRdwPK5ydBHafDWAxML/pGHZbMvKqRZ5+Abc=
golang.org/x/crypto v0.17.0 h1:r8bRNjWL3GshPW3gkd+RpvzWrZAwPS49OmTGZ/uhM4k=
golang.org/x/crypto v0.17.0/go.mod h1:gCAAfMLgwOJRpTjQ2zCCt2OcSfYMTeZVSRtQlPC7Nq4=
golang.org/x/net v0.0.0-20180724234803-3673e40ba225/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20180811021610-c39426892332/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190108225652-1e06a53dbb7e/go.mod h1:mL1N/T3taQHkDXs73rZJwtUhF3w3ftmwwsq0BUmARs4=
golang.org/x/net v0.0.0-20190404232315-eb5bcb51f2a3/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190603091049-60506f45cf65/go.mod h1:HSz+uSET+XFnRR8LxR5pz3Of3rY3CfYBVs4xY44aLks=
golang.org/x/net v0.0.0-20191009170851-d66e71096ffb/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20200301022130-244492dfa37a/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/net v0.0.0-20210119194325-5f4716e94777/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20210226172049-e18ecbb05110/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/net v0.0.0-20210326060303-6b1517762897/go.mod h1:uSPa2vr4CLtc/ILN5odXGNXS6mhrKVzTaCXzk9m6W3k=
golang.org/x/net v0.17.0 h1:pVaXccu2ozPjCXewfr1S7xza/zcXTity9cCdXQYSjIM=
golang.org/x/net v0.17.0/go.mod h1:NxSsAGuq816PNPmqtQdLE42eU2Fs7NoRIZrHJAlaCOE=
golang.org/x/oauth2 v0.0.0-20190604053449-0f29369cfe45/go.mod h1:gOpvHmFTYa4IltrdGE7lF6nIHvwfUNPOp7c8zoXwtLw=
golang.org/x/sync v0.0.0-20180314180146-1d60e4601c6f/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20181221193216-37e7f081c4d4/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sys v0.0.0-20180905080454-ebe1bf3edb33/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190412213103-97732733099d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190507160741-ecd444e8653b/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190916202348-b4ddaad3f8a3/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200116001909-b77594299b42/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200223170610-d5e6a3e2c0ae/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20200302150141-5c8b2ff67527/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210320140829-1e4c9ba3b0c4/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210324051608-47abb6519492/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210502180810-71e4cd670f79/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20210615035016-665e8c7367d1/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210630005230-0f9fa26af87c/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20210927094055-39ccf1dd6fa6/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.0.0-20220503163025-988cb79eb6c6/go.mod h1:oPkhp1MJrh7nUepCBck5+mAzfO9JrbApNNgaTdGDITg=
golang.org/x/sys v0.15.0 h1:h48lPFYpsTvQJZF4EKyI4aLHaev3CxivZmv7yZig9pc=
golang.org/x/sys v0.15.0/go.mod h1:/VUhepiaJMQUp4+oa/7Zr1D23ma6VTLIYjOOTFZPUcA=
golang.org/x/term v0.0.0-20201126162022-7de9c90e9dd1/go.mod h1:bj7SfCRtBDWHUb9snDiAeCFNEtKQo2Wmx5Cou7ajbmo=
golang.org/x/term v0.15.0 h1:y/Oo/a/q3IXu26lQgl04j/gjuBDOBlx7X6Om1j2CPW4=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.2/go.mod h1:bEr9sfX3Q8Zfm5fL9x+3itogRgK3+ptLWKqgva+5dAk=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.3.5/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/text v0.14.0 h1:ScX5w1eTa3QqT8oi6+ziP7dTV1S2+ALU0bI+0zXKWiQ=
golang.org/x/text v0.14.0/go.mod h1:18ZOQIKpY8NJVqYksKHtTdi31H5itFRjB5/qKTNYzSU=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/appengine v1.1.0/go.mod h1:EbEs0AVv82hx2wNQdGPgUI5lhzA/G0D9YwlJXL52JkM=
google.golang.org/appengine v1.4.0/go.mod h1:xpcJRLb0r/rnEns0DIKYYv+WjYCduHsrkT7/EB5XEv4=
google.golang.org/appengine v1.6.5/go.mod h1:8WjMMxjGQR8xUklV/ARdw2HLXBOI7O7uCIDZVag1xfc=
google.golang.org/appengine v1.6.7 h1:FZR1q0exgwxzPzp/aF+VccGrSfxfPpkBqjIIEq3ru6c=
google.golang.org/appengine v1.6.7/go.mod h1:8WjMMxjGQR8xUklV/ARdw2HLXBOI7O7uCIDZVag1xfc=
google.golang.org/genproto v0.0.0-20230410155749-daa745c078e1 h1:KpwkzHKEF7B9Zxg18WzOa7djJ+Ha5DzthMyZYQfEn2A=
google.golang.org/genproto v0.0.0-20230410155749-daa745c078e1/go.mod h1:nKE/iIaLqn2bQwXBg8f1g2Ylh6r5MN5CmZvuzZCgsCU=
google.golang.org/grpc v1.56.3 h1:8I4C0Yq1EjstUzUJzpcRVbuYA2mODtEmpWiQoN/b2nc=
google.golang.org/grpc v1.56.3/go.mod h1:I9bI3vqKfayGqPUAwGdOSu7kt6oIJLixfffKrpXqQ9s=
google.golang.org/protobuf v1.26.0-rc.1/go.mod h1:jlhhOSvTdKEhbULTjvd4ARK9grFBp09yW+WbY/TyQbw=
google.golang.org/protobuf v1.26.0/go.mod h1:9q0QmTI4eRPtz6boOQmLYwt+qCgq0jsYwAQnmE0givc=
google.golang.org/protobuf v1.33.0 h1:uNO2rsAINq/JlFpSdYEKIZ0uKD/R9cpdv0T+yoGwGmI=
google.golang.org/protobuf v1.33.0/go.mod h1:c6P6GXX6sHbq/GpV6MGZEdwhWPcYBgnhAHhKbcUYpos=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20190902080502-41f04d3bba15/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20200227125254-8fa46927fb4f/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c h1:Hei/4ADfdWqJk1ZMxUNpqntNwaWcugrBjAiHlqqRiVk=
gopkg.in/check.v1 v1.0.0-20201130134442-10cb98267c6c/go.mod h1:JHkPIbrfpd72SG/EVd6muEfDQjcINNoR0C8j2r3qZ4Q=
gopkg.in/warnings.v0 v0.1.2 h1:wFXVbFY8DY5/xOe1ECiWdKCzZlxgshcYVNkBHstARME=
gopkg.in/warnings.v0 v0.1.2/go.mod h1:jksf8JmL6Qr/oQM2OXTHunEvvTAsrWBLb6OOjuVWRNI=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.2.4/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.3.0/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.0/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=


File: /go.work
go 1.18

use (
	.
	./client
)


File: /go.work.sum
github.com/apparentlymart/go-textseg v1.0.0 h1:rRmlIsPEEhUTIKQb7T++Nz/A5Q6C9IuX2wFoYVvnCs0=
golang.org/x/mod v0.6.0-dev.0.20220419223038-86c51ed26bb4 h1:6zppjxzCulZykYSLyVDYbneBfbaBIQPYMevg0bEwv2s=


File: /LICENSE
Copyright 2019-2022 Dom Del Nano and others

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


File: /main.go
package main

import (
	"context"
	"flag"
	"log"

	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik"
	"github.com/hashicorp/terraform-plugin-framework/providerserver"
	"github.com/hashicorp/terraform-plugin-go/tfprotov5"
	"github.com/hashicorp/terraform-plugin-go/tfprotov5/tf5server"
	"github.com/hashicorp/terraform-plugin-mux/tf5muxserver"
	"github.com/hashicorp/terraform-plugin-mux/tf6to5server"
)

// Generate the Terraform provider documentation using `tfplugindocs`:
//
//go:generate go run github.com/hashicorp/terraform-plugin-docs/cmd/tfplugindocs
func main() {
	var debugMode bool

	flag.BoolVar(&debugMode, "debuggable", false, "set to true to run the provider with support for debuggers like delve")
	flag.Parse()

	ctx := context.Background()

	downgradedProviderFramework, err := tf6to5server.DowngradeServer(
		ctx,
		providerserver.NewProtocol6(mikrotik.NewProviderFramework(nil)),
	)
	if err != nil {
		log.Fatal(err)
	}

	providers := []func() tfprotov5.ProviderServer{
		mikrotik.NewProvider().GRPCProvider,
		func() tfprotov5.ProviderServer { return downgradedProviderFramework },
	}

	muxServer, err := tf5muxserver.NewMuxServer(ctx, providers...)
	if err != nil {
		log.Fatal(err)
	}

	serverOpts := []tf5server.ServeOpt{}
	if debugMode {
		serverOpts = append(serverOpts, tf5server.WithManagedDebug())
	}

	err = tf5server.Serve("registry.terraform.io/ddelnano/mikrotik", muxServer.ProviderServer, serverOpts...)
	if err != nil {
		log.Fatal(err)
	}
}


File: /Makefile
.PHONY: build generate clean plan apply lint-client lint-provider lint testacc testclient test

TIMEOUT ?= 40m
ROUTEROS_VERSION ?= ""
ifdef TEST
    override TEST := ./... -run $(TEST)
else
    override TEST := ./...
endif

ifdef TF_LOG
    override TF_LOG := TF_LOG=$(TF_LOG)
endif

compose := docker compose -f docker/docker-compose.yml

build:
	go build -o terraform-provider-mikrotik

generate:
	go generate ./...

clean:
	rm dist/*

plan: build
	terraform init
	terraform plan

apply:
	terraform apply

lint-client:
	go vet ./client/...

lint-provider:
	go vet ./mikrotik/...

lint: lint-client lint-provider

test: lint testclient testacc

testclient:
	cd client; go test $(TEST) -race -v -count 1

testacc:
	TF_ACC=1 $(TF_LOG) go test $(TEST) -v -count 1 -timeout $(TIMEOUT)

routeros: routeros-clean
	ROUTEROS_VERSION=$(ROUTEROS_VERSION) ${compose} up -d --build --remove-orphans routeros

routeros-stop:
	${compose} stop routeros

routeros-logs:
	${compose} logs -f routeros

routeros-clean:
	${compose} rm -sfv routeros


File: /mikrotik\acc_setup_test.go
package mikrotik

import (
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
)

var sysResources client.SystemResources

func TestMain(m *testing.M) {
	client.SetupAndTestMainExec(m, &sysResources)
}


File: /mikrotik\internal\test_helpers.go
package internal

import (
	"fmt"
	"net"
	"strconv"
	"strings"
)

const ipv6U uint64 = 0x2001000000000000 // upper half of ipv6 address

var ipCounter uint = 0xC0A80001              // 192 = C0, 168 = A8, 0 = 00, 1 = 01
var ipRangeCounter uint = 0xAC100001         // 172 = AC, 16 = 10, 0 = 00, 1 = 01
var ipv6LCounter uint64 = 0x0000000000000000 // lower half of ipv6 address
var macCounter = 0
var dnsCounter = 0

func GetNewIpAddr() string {
	ipCounter++
	return formatIPv4(ipCounter)
}

func GetNewIpv6Addr() string {
	ipv6LCounter++
	return formatIPv6(ipv6LCounter)
}

func GetNewIpAddrRange(count uint) string {
	var ipRangeStart = ipRangeCounter + 1
	ipRangeCounter = ipRangeCounter + count
	return fmt.Sprintf("%s-%s", formatIPv4(ipRangeStart), formatIPv4(ipRangeCounter))
}

func GetNewMacAddr() string {
	macCounter++

	if macCounter > 255 {
		macCounter = 1
	}

	return fmt.Sprintf("01:23:45:67:89:%02x", macCounter)
}

func GetNewDnsName() string {
	dnsCounter++
	return fmt.Sprintf("dns-%02d.terraform", dnsCounter)
}

// JoinIntsToString builds textualrepresentation of a list of integers
func JoinIntsToString(ints []int, sep string) string {
	if len(ints) < 1 {
		return ""
	}

	if len(ints) == 1 {
		return strconv.Itoa(ints[0])
	}

	s := strings.Builder{}
	s.WriteString(strconv.Itoa(ints[0]))
	ints = ints[1:]
	for _, v := range ints {
		s.WriteString(sep)
		s.WriteString(strconv.Itoa(v))
	}

	return s.String()
}

// JoinStringsToString builds textual representation of a list of strings
func JoinStringsToString(items []string, sep string) string {
	if len(items) < 1 {
		return ""
	}

	if len(items) == 1 {
		return "\"" + items[0] + "\""
	}

	return "\"" + strings.Join(items, "\",\"") + "\""
}

func formatIPv4(ipAddr uint) string {
	return fmt.Sprintf("%d.%d.%d.%d", (ipAddr>>24)&0xFF, (ipAddr>>16)&0xFF, (ipAddr>>8)&0xFF, ipAddr&0xFF)
}

func formatIPv6(ipv6Addr uint64) string {
	return net.ParseIP(fmt.Sprintf(
		"%x:%x:%x:%x:%x:%x:%x:%x",
		(ipv6U>>48)&0xFFFF,
		(ipv6U>>32)&0xFFFF,
		(ipv6U>>16)&0xFFFF,
		ipv6U&0xFFFF,
		(ipv6Addr>>48)&0xFFFF,
		(ipv6Addr>>32)&0xFFFF,
		(ipv6Addr>>16)&0xFFFF,
		ipv6Addr&0xFFFF,
	)).String()
}


File: /mikrotik\internal\types\defaultaware\bool.go
package defaultaware

import (
	"context"
	"fmt"

	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/defaults"
)

// BoolAttribute creates a wrapper for schema.BoolAttribute object and generates documentation with default value.
func BoolAttribute(wrapped schema.BoolAttribute) schema.Attribute {
	return boolWrapper{wrapped}
}

func (w boolWrapper) GetDescription() string {
	desc := w.BoolAttribute.GetDescription()
	if w.Default == nil {
		return desc
	}

	resp := defaults.BoolResponse{}
	w.Default.DefaultBool(context.TODO(), defaults.BoolRequest{}, &resp)
	defaultValue := resp.PlanValue.ValueBool()
	desc = fmt.Sprintf("%s Default: `%t`.", desc, defaultValue)

	return desc
}

type boolWrapper struct {
	schema.BoolAttribute
}

var _ schema.Attribute = &boolWrapper{}


File: /mikrotik\internal\types\defaultaware\bool_test.go
package defaultaware

import (
	"testing"

	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/defaults"
	"github.com/stretchr/testify/require"
)

func TestBoolWrapper(t *testing.T) {
	testCases := []struct {
		name           string
		description    string
		defaultValue   defaults.Bool
		expectedResult string
	}{
		{
			name:           "no default value",
			description:    "Attribute description.",
			expectedResult: "Attribute description.",
		},
		{
			name:           "true default value",
			description:    "Attribute description.",
			defaultValue:   booldefault.StaticBool(true),
			expectedResult: "Attribute description. Default: `true`.",
		}, {
			name:           "false default value",
			description:    "Attribute description.",
			defaultValue:   booldefault.StaticBool(false),
			expectedResult: "Attribute description. Default: `false`.",
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			attr := BoolAttribute(
				schema.BoolAttribute{
					Description: tc.description,
					Default:     tc.defaultValue,
				},
			)
			require.Equal(t, tc.expectedResult, attr.GetDescription())
		})
	}
}


File: /mikrotik\internal\types\defaultaware\int64.go
package defaultaware

import (
	"context"
	"fmt"

	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/defaults"
)

// Int64Attribute creates a wrapper for schema.Int64Attribute object and generates documentation with default value.
func Int64Attribute(wrapped schema.Int64Attribute) schema.Attribute {
	return int64Wrapper{wrapped}
}

func (w int64Wrapper) GetDescription() string {
	desc := w.Int64Attribute.GetDescription()
	if w.Default == nil {
		return desc
	}

	resp := defaults.Int64Response{}
	w.Default.DefaultInt64(context.TODO(), defaults.Int64Request{}, &resp)
	defaultValue := resp.PlanValue.ValueInt64()
	desc = fmt.Sprintf("%s Default: `%d`.", desc, defaultValue)

	return desc
}

type int64Wrapper struct {
	schema.Int64Attribute
}

var _ schema.Attribute = &int64Wrapper{}


File: /mikrotik\internal\types\defaultaware\int64_test.go
package defaultaware

import (
	"testing"

	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/defaults"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/int64default"
	"github.com/stretchr/testify/require"
)

func TestInt64Wrapper(t *testing.T) {
	testCases := []struct {
		name           string
		description    string
		defaultValue   defaults.Int64
		expectedResult string
	}{
		{
			name:           "no default value",
			description:    "Attribute description.",
			expectedResult: "Attribute description.",
		},
		{
			name:           "with default value",
			description:    "Attribute description.",
			defaultValue:   int64default.StaticInt64(2),
			expectedResult: "Attribute description. Default: `2`.",
		}, {
			name:           "with zero default value",
			description:    "Attribute description.",
			defaultValue:   int64default.StaticInt64(0),
			expectedResult: "Attribute description. Default: `0`.",
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			attr := Int64Attribute(
				schema.Int64Attribute{
					Description: tc.description,
					Default:     tc.defaultValue,
				},
			)
			require.Equal(t, tc.expectedResult, attr.GetDescription())
		})
	}
}


File: /mikrotik\internal\types\defaultaware\resource_wrapper.go
package defaultaware

import (
	"context"

	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
)

// WrapResources wraps the list of provider's resource contructors.
//
// Later, during actual call, the resource instance is wrapped in special proxy to replace every attribute in the schema
// with proper wrapper from "defaultsaware" package.
func WrapResources(funcs []func() resource.Resource) []func() resource.Resource {
	for i, f := range funcs {
		f := f
		funcs[i] = func() resource.Resource {
			r := resourceWrapper{f()}
			return &r
		}
	}

	return funcs
}

// Schema overrides Schema functions from the wrapped resource and makes attributes default-aware.
//
// Default-aware wrappers allows generating documentation with default values, if any.
func (r resourceWrapper) Schema(ctx context.Context, req resource.SchemaRequest, resp *resource.SchemaResponse) {
	r.Resource.Schema(ctx, req, resp)

	for name, attr := range resp.Schema.Attributes {
		switch schemaAttr := attr.(type) {
		case schema.StringAttribute:
			if schemaAttr.Default != nil {
				resp.Schema.Attributes[name] = StringAttribute(schemaAttr)
			}
		case schema.BoolAttribute:
			if schemaAttr.Default != nil {
				resp.Schema.Attributes[name] = BoolAttribute(schemaAttr)
			}
		case schema.Int64Attribute:
			if schemaAttr.Default != nil {
				resp.Schema.Attributes[name] = Int64Attribute(schemaAttr)
			}
		}
	}
}

func (r resourceWrapper) Configure(ctx context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	rwc := r.Resource.(resource.ResourceWithConfigure)
	rwc.Configure(ctx, req, resp)
}

func (r resourceWrapper) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	rwi := r.Resource.(resource.ResourceWithImportState)
	rwi.ImportState(ctx, req, resp)
}

type resourceWrapper struct {
	resource.Resource
}

var (
	_ resource.Resource                = &resourceWrapper{}
	_ resource.ResourceWithConfigure   = &resourceWrapper{}
	_ resource.ResourceWithImportState = &resourceWrapper{}
)


File: /mikrotik\internal\types\defaultaware\resource_wrapper_test.go
package defaultaware

import (
	"context"
	"testing"

	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/int64default"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/hashicorp/terraform-plugin-framework/types"
	"github.com/stretchr/testify/assert"
)

func TestResource_wrappers(t *testing.T) {
	testCases := []struct {
		name                      string
		resourceConstructor       func() resource.Resource
		expectedWrappedAttributes map[string]bool
	}{
		{
			name: "wrapping attributes with default-aware wrappers",
			expectedWrappedAttributes: map[string]bool{
				"wrapped_string": true,
				"wrapped_bool":   true,
				"wrapped_int64":  true,
			},
			resourceConstructor: func() resource.Resource {
				return dummyResource{
					resourceSchema: schema.Schema{
						Description: "Resource description",
						Attributes: map[string]schema.Attribute{
							"wrapped_string": schema.StringAttribute{
								Optional:    true,
								Computed:    true,
								Default:     stringdefault.StaticString("*0"),
								Description: "String attribute.",
							},
							"wrapped_int64": schema.Int64Attribute{
								Optional:    true,
								Computed:    true,
								Default:     int64default.StaticInt64(42),
								Description: "Int64 attribute.",
							},
							"string_without_default": schema.StringAttribute{
								Optional:    true,
								Computed:    true,
								Description: "String attribute.",
							},
							"int64_without_default": schema.Int64Attribute{
								Optional:    true,
								Computed:    true,
								Description: "Int64 attribute.",
							},
							"wrapped_bool": schema.BoolAttribute{
								Optional:    true,
								Computed:    true,
								Default:     booldefault.StaticBool(true),
								Description: "Bool attribute.",
							},
							"bool_without_default": schema.BoolAttribute{
								Optional:    true,
								Computed:    true,
								Description: "Bool attribute.",
							},
							"unsupported_type": schema.ListAttribute{
								Optional:    true,
								Computed:    true,
								ElementType: types.StringType,
								Description: "List attribute.",
							},
						},
					},
				}
			},
		},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			wrapped := WrapResources([]func() resource.Resource{tc.resourceConstructor})[0]()
			resp := resource.SchemaResponse{}
			wrapped.Schema(context.TODO(), resource.SchemaRequest{}, &resp)
			for name, attr := range resp.Schema.Attributes {
				switch attr.(type) {
				case stringWrapper, int64Wrapper, boolWrapper:
					if _, ok := tc.expectedWrappedAttributes[name]; !ok {
						assert.Fail(t, "wrapping error", "attribute %q should have been not wrapped, but it was", name)
					}
					continue
				}
				if _, ok := tc.expectedWrappedAttributes[name]; ok {
					assert.Fail(t, "wrapping error", "attribute %q should have been wrapped, but it wasn't", name)
				}
			}
		})
	}

}

type dummyResource struct {
	resource.Resource
	resourceSchema schema.Schema
}

func (dr dummyResource) Schema(ctx context.Context, req resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = dr.resourceSchema
}


File: /mikrotik\internal\types\defaultaware\string.go
package defaultaware

import (
	"context"
	"fmt"

	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/defaults"
)

// StringAttribute creates a wrapper for schema.StringAttribute object and generates documentation with default value.
func StringAttribute(wrapped schema.StringAttribute) schema.Attribute {
	return stringWrapper{wrapped}
}

func (w stringWrapper) GetDescription() string {
	desc := w.StringAttribute.GetDescription()
	if w.Default == nil {
		return desc
	}

	resp := defaults.StringResponse{}
	w.Default.DefaultString(context.TODO(), defaults.StringRequest{}, &resp)
	defaultValue := resp.PlanValue.ValueString()
	if defaultValue == "" {
		defaultValue = `""`
	}
	desc = fmt.Sprintf("%s Default: `%s`.", desc, defaultValue)

	return desc
}

type stringWrapper struct {
	schema.StringAttribute
}

var _ schema.Attribute = &stringWrapper{}


File: /mikrotik\internal\types\defaultaware\string_test.go
package defaultaware

import (
	"testing"

	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/defaults"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/stretchr/testify/require"
)

func TestStringWrapper(t *testing.T) {
	testCases := []struct {
		name           string
		description    string
		defaultValue   defaults.String
		expectedResult string
	}{
		{
			name:           "no default value",
			description:    "Attribute description.",
			expectedResult: "Attribute description.",
		},
		{
			name:           "with default value",
			description:    "Attribute description.",
			defaultValue:   stringdefault.StaticString("some value"),
			expectedResult: "Attribute description. Default: `some value`.",
		}, {
			name:           "with empty string default value",
			description:    "Attribute description.",
			defaultValue:   stringdefault.StaticString(""),
			expectedResult: "Attribute description. Default: `\"\"`.",
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			attr := StringAttribute(
				schema.StringAttribute{
					Description: tc.description,
					Default:     tc.defaultValue,
				},
			)
			require.Equal(t, tc.expectedResult, attr.GetDescription())
		})
	}
}


File: /mikrotik\internal\utils\provider.go
package utils

import (
	"context"
	"strings"

	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)

// ImportStateContextUppercaseWrapper changes the ID of the resource to upper case before passing it to wrappedFunction
//
// This wrapper is useful when resource ID is MikroTik's .id.
// Due to wierd behavior, listing via MikroTik's CLI reports lowercase .id, but find request with this id via API fails
// as it expects upper case string.
//
// Usage in resource definition.
//
// SDKv2
//
//	schema.Resource{
//		Importer: &schema.ResourceImporter{
//			StateContext: utils.ImportStateContextUppercaseWrapper(schema.ImportStatePassthroughContext),
//		}
//	}
func ImportStateContextUppercaseWrapper(wrappedFunc schema.StateContextFunc) schema.StateContextFunc {
	return func(ctx context.Context, rd *schema.ResourceData, i interface{}) ([]*schema.ResourceData, error) {
		rd.SetId(strings.ToUpper(rd.Id()))
		return wrappedFunc(ctx, rd, i)
	}
}

// ImportUppercaseWrapper is ImportStateContextUppercaseWrapper equivalent for PluginFramework.
func ImportUppercaseWrapper(wrappedFunc importStateFunc) importStateFunc {
	return func(ctx context.Context, p path.Path, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
		wrappedFunc(ctx, p, resource.ImportStateRequest{ID: strings.ToUpper(req.ID)}, resp)
	}
}

type importStateFunc = func(context.Context, path.Path, resource.ImportStateRequest, *resource.ImportStateResponse)


File: /mikrotik\internal\utils\provider_test.go
package utils

import (
	"context"
	"testing"

	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
	"github.com/stretchr/testify/assert"
)

func TestImportStateContextUppercaseWrapper(t *testing.T) {
	testCases := []struct {
		name     string
		in       string
		expected string
	}{
		{
			name:     "input contains no letter, should be unchanged",
			in:       "*123",
			expected: "*123",
		},
		{
			name:     "input contains digits and only upper case letters, should be unchanged",
			in:       "*2E",
			expected: "*2E",
		},
		{
			name:     "input contains lower case letters, should be mapped to upper case",
			in:       "*f2",
			expected: "*F2",
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			var actual string
			f := ImportStateContextUppercaseWrapper(
				func(ctx context.Context, rd *schema.ResourceData, i interface{}) ([]*schema.ResourceData, error) {
					actual = rd.Id()
					return nil, nil
				},
			)
			rd := schema.ResourceData{}
			rd.SetId(tc.in)
			_, _ = f(context.TODO(), &rd, nil)
			assert.Equal(t, tc.expected, actual)
		})
	}
}


File: /mikrotik\internal\utils\string.go
package utils

import (
	"fmt"
	"strconv"
)

// ParseBool is wrapper around strconv.ParseBool to save few lines of code
func ParseBool(v string) (bool, error) {
	res, err := strconv.ParseBool(v)
	if err != nil {
		return res, fmt.Errorf("could not parse %q as bool: %w", v, err)
	}

	return res, nil
}


File: /mikrotik\internal\utils\struct_copy.go
package utils

import (
	"context"
	"errors"
	"fmt"
	"reflect"
	"strings"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework/attr"
	"github.com/hashicorp/terraform-plugin-framework/diag"
	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
	"github.com/hashicorp/terraform-plugin-log/tflog"
)

// MikrotikStructToTerraformModel is a wrapper for copyStruct() to ensure proper src/dest typing
func MikrotikStructToTerraformModel(ctx context.Context, src client.Resource, dest interface{}) error {
	return copyStruct(ctx, src, dest)
}

// TerraformModelToMikrotikStruct is a wrapper for copyStruct() to ensure proper src/dest typing
func TerraformModelToMikrotikStruct(ctx context.Context, src interface{}, dest client.Resource) error {
	return copyStruct(ctx, src, dest)
}

// copyStruct copies fields of src struct to fields of dest struct.
//
// The fields matching is done based on field names (case insensitive).
// Having multiple fields with the same name but different case leads to unpredictable behavior.
//
// If dest struct has no field with particular name, it is skipped.
func copyStruct(ctx context.Context, src, dest interface{}) error {
	if reflect.ValueOf(dest).Kind() != reflect.Pointer {
		return errors.New("destination must be a pointer")
	}

	reflectedSrc := reflect.Indirect(reflect.ValueOf(src))
	reflectedDest := reflect.Indirect(reflect.ValueOf(dest))
	if reflectedSrc.Kind() != reflect.Struct || reflectedDest.Kind() != reflect.Struct {
		return fmt.Errorf("source and destination must be structs, got %v and %v", reflectedSrc.Kind(), reflectedDest.Kind())
	}

	for i := 0; i < reflectedSrc.NumField(); i++ {
		srcField := reflectedSrc.Field(i)
		srcFieldType := reflectedSrc.Type().Field(i)

		destField := reflectedDest.FieldByNameFunc(
			func(s string) bool {
				return strings.EqualFold(srcFieldType.Name, s)
			})
		destFieldType, found := reflectedDest.Type().FieldByNameFunc(
			func(s string) bool {
				return strings.EqualFold(srcFieldType.Name, s)
			})
		tflog.Debug(ctx, fmt.Sprintf("trying to copy struct field %q to %q", srcFieldType.Name, destFieldType.Name))
		if !destField.IsValid() || !found {
			// skip if dest struct does not have it (by name)
			tflog.Debug(ctx, "target field was not found")
			continue
		}
		if srcFieldType.PkgPath != "" || destFieldType.PkgPath != "" {
			// skip unexported fields
			tflog.Debug(ctx, "the source/target fields are unexported")
			continue
		}
		if !destField.CanSet() {
			// skip if dest field is not settable
			tflog.Debug(ctx, "target field is not settable")
			continue
		}

		switch kind := srcFieldType.Type.Kind(); kind {
		case reflect.Bool,
			reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64,
			reflect.Uint, reflect.Uint8, reflect.Uint16, reflect.Uint32, reflect.Uint64,
			reflect.Float32, reflect.Float64,
			reflect.String,
			reflect.Slice:
			// core type -> terraform type
			// check if dest field is one of the Terraform types
			if _, ok := destField.Interface().(attr.Value); ok {
				if err := coreTypeToTerraformType(srcField, destField); err != nil {
					return err
				}
				break
			}

			// core type -> core type
			if err := coreTypeToCoreType(srcField, destField); err != nil {
				return err
			}
		case reflect.Struct:
			// source is terraform type and dest is core type
			if _, ok := srcField.Interface().(attr.Value); ok {
				if err := terraformTypeToCoreType(srcField, destField); err != nil {
					return err
				}
				break
			}
			return errors.New("unsupported source field of type 'struct'")
		default:
			return fmt.Errorf("unsupported source field type %q", kind)
		}
	}

	return nil
}

func coreTypeToTerraformType(src, dest reflect.Value) error {
	var tfValue attr.Value
	switch src.Kind() {
	case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
		tfValue = tftypes.Int64Value(src.Int())
	case reflect.Uint, reflect.Uint8, reflect.Uint16, reflect.Uint32, reflect.Uint64:
		tfValue = tftypes.Int64Value(int64(src.Uint()))
	case reflect.String:
		tfValue = tftypes.StringValue(src.String())
	case reflect.Bool:
		tfValue = tftypes.BoolValue(src.Bool())
	case reflect.Float32, reflect.Float64:
		tfValue = tftypes.Float64Value(src.Float())
	case reflect.Slice:
		var diags diag.Diagnostics
		elements := []interface{}{}
		for i := 0; i < src.Len(); i++ {
			elements = append(elements, src.Index(i).Interface())
		}
		var tfType attr.Type
		switch kind := src.Type().Elem().Kind(); kind {
		case reflect.Bool:
			tfType = tftypes.BoolType
		case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64,
			reflect.Uint, reflect.Uint8, reflect.Uint16, reflect.Uint32, reflect.Uint64:
			tfType = tftypes.Int64Type
		case reflect.String:
			tfType = tftypes.StringType
		default:
			return fmt.Errorf("unsupported slice element type %q", kind)
		}
		var valueFromFunc func(t attr.Type, elements []interface{}) (attr.Value, diag.Diagnostics)

		switch dest.Interface().(type) {
		case tftypes.List:
			valueFromFunc = func(t attr.Type, elements []interface{}) (attr.Value, diag.Diagnostics) {
				return tftypes.ListValueFrom(context.TODO(), t, elements)
			}
		case tftypes.Set:
			valueFromFunc = func(t attr.Type, elements []interface{}) (attr.Value, diag.Diagnostics) {
				return tftypes.SetValueFrom(context.TODO(), t, elements)
			}
		default:
			return fmt.Errorf("unsupported destination Terraform type %v", reflect.TypeOf(dest).Name())
		}

		tfValue, diags = valueFromFunc(tfType, elements)

		if diags.HasError() {
			return fmt.Errorf("error creating Terraform type: %v", diags.Errors())
		}
	}

	dest.Set(reflect.ValueOf(tfValue))

	return nil
}

func terraformTypeToCoreType(src, dest reflect.Value) error {
	switch f := src.Interface().(type) {
	case tftypes.Int64:
		dest.SetInt(f.ValueInt64())
	case tftypes.String:
		dest.SetString(f.ValueString())
	case tftypes.Bool:
		dest.SetBool(f.ValueBool())
	case tftypes.List:
		var diag diag.Diagnostics
		var sliceType reflect.Type

		switch dest.Type().Elem().Kind() {
		case reflect.Bool:
			sliceType = reflect.TypeOf(true)
		case reflect.Int:
			sliceType = reflect.TypeOf(int(0))
		case reflect.Int8:
			sliceType = reflect.TypeOf(int8(0))
		case reflect.Int16:
			sliceType = reflect.TypeOf(int16(0))
		case reflect.Int32:
			sliceType = reflect.TypeOf(int32(0))
		case reflect.Int64:
			sliceType = reflect.TypeOf(int64(0))
		case reflect.Uint:
			sliceType = reflect.TypeOf(uint(0))
		case reflect.Uint8:
			sliceType = reflect.TypeOf(uint8(0))
		case reflect.Uint16:
			sliceType = reflect.TypeOf(uint16(0))
		case reflect.Uint32:
			sliceType = reflect.TypeOf(uint32(0))
		case reflect.Uint64:
			sliceType = reflect.TypeOf(uint64(0))
		case reflect.String:
			sliceType = reflect.TypeOf("")
		default:
			return fmt.Errorf("unsupported list element types: %s -> []%s", src.Type().Name(), dest.Type().Elem().Kind())
		}
		targetPtr := reflect.New(reflect.SliceOf(sliceType))
		diag = f.ElementsAs(context.TODO(), targetPtr.Interface(), false)

		if diag.HasError() {
			return fmt.Errorf("%s", diag.Errors())
		}

		dest.Set(targetPtr.Elem())

		return nil
	case tftypes.Set:
		var diag diag.Diagnostics
		var sliceType reflect.Type

		switch dest.Type().Elem().Kind() {
		case reflect.Bool:
			sliceType = reflect.TypeOf(true)
		case reflect.Int:
			sliceType = reflect.TypeOf(int(0))
		case reflect.Int8:
			sliceType = reflect.TypeOf(int8(0))
		case reflect.Int16:
			sliceType = reflect.TypeOf(int16(0))
		case reflect.Int32:
			sliceType = reflect.TypeOf(int32(0))
		case reflect.Int64:
			sliceType = reflect.TypeOf(int64(0))
		case reflect.Uint:
			sliceType = reflect.TypeOf(uint(0))
		case reflect.Uint8:
			sliceType = reflect.TypeOf(uint8(0))
		case reflect.Uint16:
			sliceType = reflect.TypeOf(uint16(0))
		case reflect.Uint32:
			sliceType = reflect.TypeOf(uint32(0))
		case reflect.Uint64:
			sliceType = reflect.TypeOf(uint64(0))
		case reflect.String:
			sliceType = reflect.TypeOf("")
		default:
			return fmt.Errorf("unsupported list element types: %s -> []%s", src.Type().Name(), dest.Type().Elem().Kind())
		}
		targetPtr := reflect.New(reflect.SliceOf(sliceType))
		if len(f.Elements()) > 0 {
			diag = f.ElementsAs(context.TODO(), targetPtr.Interface(), false)
		}

		if diag.HasError() {
			return fmt.Errorf("%s", diag.Errors())
		}
		dest.Set(targetPtr.Elem())

		return nil
	default:
		return fmt.Errorf("unsupported field type assignment: %s -> %s", src.Type().Name(), dest.Kind())
	}

	return nil
}

func coreTypeToCoreType(src, dest reflect.Value) error {
	if src.Kind() != dest.Kind() {
		return fmt.Errorf("cannot assign %s to %s", src.Kind(), dest.Kind())
	}

	switch src.Kind() {
	case reflect.Bool:
		dest.SetBool(src.Bool())
	case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
		dest.SetInt(src.Int())
	case reflect.Uint, reflect.Uint8, reflect.Uint16, reflect.Uint32, reflect.Uint64:
		dest.SetUint(src.Uint())
	case reflect.Float32, reflect.Float64:
		dest.SetFloat(src.Float())
	case reflect.String:
		dest.SetString(src.String())
	case reflect.Slice:
		slice := reflect.MakeSlice(dest.Type(), 0, 0)
		for i := 0; i < src.Len(); i++ {
			slice = reflect.Append(slice, src.Index(i))
		}
		dest.Set(slice)
	}

	return nil
}


File: /mikrotik\internal\utils\struct_copy_test.go
package utils

import (
	"context"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/client/types"
	"github.com/hashicorp/terraform-plugin-framework/attr"
	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestCopyStruct(t *testing.T) {
	testCases := []struct {
		name        string
		src         interface{}
		dest        interface{}
		expected    interface{}
		expectError bool
	}{
		{
			name: "same fields",
			src: struct {
				Name         string
				AnotherField int
				Items        []string
			}{
				Name:         "source field name",
				AnotherField: 10,
				Items:        []string{"one", "two"},
			},
			dest: &struct {
				Name         string
				AnotherField int
				Items        []string
			}{
				Name:         "destination field name",
				AnotherField: 20,
				Items:        []string{"one", "two", "three"},
			},
			expected: &struct {
				Name         string
				AnotherField int
				Items        []string
			}{
				Name:         "source field name",
				AnotherField: 10,
				Items:        []string{"one", "two"},
			},
		},
		{
			name: "overlapping fields",
			src: struct {
				Name        string
				SourceField int
				Items       []string
			}{
				Name:        "field name",
				SourceField: 10,
				Items:       []string{"one", "two"},
			},
			dest: &struct {
				Name             string
				DestinationField int
				Items            []string
			}{
				Name:             "field name",
				DestinationField: 20,
				Items:            []string{"one", "two", "three"},
			},
			expected: &struct {
				Name             string
				DestinationField int
				Items            []string
			}{
				Name:             "field name",
				DestinationField: 20,
				Items:            []string{"one", "two"},
			},
		},
		{
			name: "different case",
			src: struct {
				NAME        string
				SourceField int
				itEMS       []string
			}{
				NAME:        "src field name",
				SourceField: 10,
				itEMS:       []string{"one", "two"},
			},
			dest: &struct {
				Name             string
				DestinationField int
				Items            []string
			}{
				Name:             "dest field name",
				DestinationField: 20,
				Items:            []string{"one", "two", "three"},
			},
			expected: &struct {
				Name             string
				DestinationField int
				Items            []string
			}{
				Name:             "src field name",
				DestinationField: 20,
				Items:            []string{"one", "two", "three"},
			},
		},
		{
			name: "custom field to regular",
			src: client.BridgeVlan{
				Id:       "identifier",
				Bridge:   "bridge1",
				Tagged:   types.MikrotikList{"tagged1", "tagged2"},
				Untagged: types.MikrotikList{"untagged1", "untagged2"},
				VlanIds:  types.MikrotikIntList{3, 4, 5},
			},
			dest: &struct {
				Id         string
				Bridge     string
				Tagged     []string
				Untagged   []string
				VlanIds    []int
				ExtraField string
			}{
				Id:         "identifier old",
				Bridge:     "bridge old",
				Tagged:     []string{"tagged old"},
				Untagged:   []string{"untagged old"},
				VlanIds:    []int{2},
				ExtraField: "unchanged",
			},
			expected: &struct {
				Id         string
				Bridge     string
				Tagged     []string
				Untagged   []string
				VlanIds    []int
				ExtraField string
			}{
				Id:         "identifier",
				Bridge:     "bridge1",
				Tagged:     []string{"tagged1", "tagged2"},
				Untagged:   []string{"untagged1", "untagged2"},
				VlanIds:    []int{3, 4, 5},
				ExtraField: "unchanged",
			},
		},
		{
			name: "regular type to custom field",
			src: struct {
				Id         string
				Bridge     string
				Tagged     []string
				Untagged   []string
				VlanIds    []int
				ExtraField string
			}{
				Id:         "identifier new",
				Bridge:     "bridge new",
				Tagged:     []string{"tagged new"},
				Untagged:   []string{"untagged new"},
				VlanIds:    []int{2},
				ExtraField: "extra field",
			},
			dest: &client.BridgeVlan{
				Id:       "identifier",
				Bridge:   "bridge1",
				Tagged:   types.MikrotikList{"tagged1", "tagged2"},
				Untagged: types.MikrotikList{"untagged1", "untagged2"},
				VlanIds:  types.MikrotikIntList{3, 4, 5},
			},
			expected: &client.BridgeVlan{
				Id:       "identifier new",
				Bridge:   "bridge new",
				Tagged:   types.MikrotikList{"tagged new"},
				Untagged: types.MikrotikList{"untagged new"},
				VlanIds:  types.MikrotikIntList{2},
			},
		},
		{
			name: "field type mismatch",
			src: struct {
				Name         string
				AnotherField float64
				Items        []string
			}{
				Name:         "field name",
				AnotherField: 10,
				Items:        []string{"one", "two"},
			},
			dest: &struct {
				Name         string
				AnotherField int
				Items        []string
			}{
				Name:         "field name",
				AnotherField: 10,
				Items:        []string{"one", "two"},
			},
			expectError: true,
		},
		{
			name: "core type to core type",
			src: struct {
				String      string
				Int         int
				Int8        int8
				Int16       int16
				Int32       int32
				Int64       int64
				Uint        uint
				Uint8       uint8
				Uint16      uint16
				Uint32      uint32
				Uint64      uint64
				IntSlice    []int
				UintSlice   []uint
				StringSlice []string
			}{
				String:      "source field name",
				Int:         10,
				Int8:        20,
				Int16:       20_000,
				Int32:       20_000_000,
				Int64:       20_000_000_000_000,
				Uint:        10,
				Uint8:       200,
				Uint16:      20_000,
				Uint32:      20_000_000,
				Uint64:      20_000_000_000_000,
				StringSlice: []string{"one", "two"},
				IntSlice:    []int{1, 2, 3},
				UintSlice:   []uint{5, 30},
			},
			dest: &struct {
				String      string
				Int         int
				Int8        int8
				Int16       int16
				Int32       int32
				Int64       int64
				Uint        uint
				Uint8       uint8
				Uint16      uint16
				Uint32      uint32
				Uint64      uint64
				IntSlice    []int
				UintSlice   []uint
				StringSlice []string
			}{},
			expected: &struct {
				String      string
				Int         int
				Int8        int8
				Int16       int16
				Int32       int32
				Int64       int64
				Uint        uint
				Uint8       uint8
				Uint16      uint16
				Uint32      uint32
				Uint64      uint64
				IntSlice    []int
				UintSlice   []uint
				StringSlice []string
			}{
				String:      "source field name",
				Int:         10,
				Int8:        20,
				Int16:       20_000,
				Int32:       20_000_000,
				Int64:       20_000_000_000_000,
				Uint:        10,
				Uint8:       200,
				Uint16:      20_000,
				Uint32:      20_000_000,
				Uint64:      20_000_000_000_000,
				StringSlice: []string{"one", "two"},
				IntSlice:    []int{1, 2, 3},
				UintSlice:   []uint{5, 30},
			},
		},
		{
			name: "core type to terraform type",
			src: struct {
				String     string
				ExtraField int
				Int        int
				Int8       int8
				Int16      int16
				Int32      int32
				Int64      int64
				Uint       uint
				Uint8      uint8
				Uint16     uint16
				Uint32     uint32
				Uint64     uint64
				Boolean    bool
				Float32    float32
				Float64    float64
				IntList    []int
				UintList   []uint
				StringList []string
			}{
				String:     "name new",
				ExtraField: 30,
				Int:        10,
				Int8:       20,
				Int16:      20_000,
				Int32:      20_000_000,
				Int64:      20_000_000_000_000,
				Uint:       20,
				Uint8:      200,
				Uint16:     20_000,
				Uint32:     20_000_000,
				Uint64:     20_000_000_000_000,
				Boolean:    true,
				IntList:    []int{10, 20, 30},
				UintList:   []uint{10, 20, 30},
				StringList: []string{"new value"},
			},
			dest: &struct {
				String        tftypes.String
				Int           tftypes.Int64
				Int8          tftypes.Int64
				Int16         tftypes.Int64
				Int32         tftypes.Int64
				Int64         tftypes.Int64
				Uint          tftypes.Int64
				Uint8         tftypes.Int64
				Uint16        tftypes.Int64
				Uint32        tftypes.Int64
				Uint64        tftypes.Int64
				UnmappedField tftypes.String
				Boolean       tftypes.Bool
				IntList       tftypes.List
				UintList      tftypes.List
				StringList    tftypes.List
			}{
				String:        tftypes.StringValue("field name"),
				Int:           tftypes.Int64Value(20),
				UnmappedField: tftypes.StringValue("unmapped field"),
				Boolean:       tftypes.BoolValue(false),
				IntList: tftypes.ListValueMust(tftypes.Int64Type,
					[]attr.Value{
						tftypes.Int64Value(2),
						tftypes.Int64Value(4),
						tftypes.Int64Value(5),
					}),
				StringList: tftypes.ListValueMust(tftypes.StringType,
					[]attr.Value{
						tftypes.StringValue("old value 1"),
						tftypes.StringValue("old value 2"),
					}),
			},
			expected: &struct {
				String        tftypes.String
				Int           tftypes.Int64
				Int8          tftypes.Int64
				Int16         tftypes.Int64
				Int32         tftypes.Int64
				Int64         tftypes.Int64
				Uint          tftypes.Int64
				Uint8         tftypes.Int64
				Uint16        tftypes.Int64
				Uint32        tftypes.Int64
				Uint64        tftypes.Int64
				UnmappedField tftypes.String
				Boolean       tftypes.Bool
				IntList       tftypes.List
				UintList      tftypes.List
				StringList    tftypes.List
			}{
				String:        tftypes.StringValue("name new"),
				Int:           tftypes.Int64Value(10),
				Int8:          tftypes.Int64Value(20),
				Int16:         tftypes.Int64Value(20_000),
				Int32:         tftypes.Int64Value(20_000_000),
				Int64:         tftypes.Int64Value(20_000_000_000_000),
				Uint:          tftypes.Int64Value(20),
				Uint8:         tftypes.Int64Value(200),
				Uint16:        tftypes.Int64Value(20_000),
				Uint32:        tftypes.Int64Value(20_000_000),
				Uint64:        tftypes.Int64Value(20_000_000_000_000),
				UnmappedField: tftypes.StringValue("unmapped field"),
				Boolean:       tftypes.BoolValue(true),
				IntList: tftypes.ListValueMust(tftypes.Int64Type,
					[]attr.Value{
						tftypes.Int64Value(10),
						tftypes.Int64Value(20),
						tftypes.Int64Value(30),
					}),
				UintList: tftypes.ListValueMust(tftypes.Int64Type,
					[]attr.Value{
						tftypes.Int64Value(10),
						tftypes.Int64Value(20),
						tftypes.Int64Value(30),
					}),
				StringList: tftypes.ListValueMust(tftypes.StringType,
					[]attr.Value{
						tftypes.StringValue("new value"),
					}),
			},
		},
		{
			name: "terraform type to core type",
			src: struct {
				String        tftypes.String
				Int           tftypes.Int64
				Int8          tftypes.Int64
				Int16         tftypes.Int64
				Int32         tftypes.Int64
				Int64         tftypes.Int64
				Uint          tftypes.Int64
				Uint8         tftypes.Int64
				Uint16        tftypes.Int64
				Uint32        tftypes.Int64
				Uint64        tftypes.Int64
				UnmappedField tftypes.String
				Boolean       tftypes.Bool
				IntList       tftypes.List
				UintList      tftypes.List
				StringList    tftypes.List
			}{
				String:        tftypes.StringValue("new field name"),
				Int:           tftypes.Int64Value(20),
				Int8:          tftypes.Int64Value(20),
				Int16:         tftypes.Int64Value(20_000),
				Int32:         tftypes.Int64Value(20_000_000),
				Int64:         tftypes.Int64Value(20_000_000_000_000),
				UnmappedField: tftypes.StringValue("unmapped field"),
				Boolean:       tftypes.BoolValue(true),
				IntList: tftypes.ListValueMust(tftypes.Int64Type,
					[]attr.Value{
						tftypes.Int64Value(2),
						tftypes.Int64Value(4),
						tftypes.Int64Value(5),
					}),
				UintList: tftypes.ListValueMust(tftypes.Int64Type,
					[]attr.Value{
						tftypes.Int64Value(2),
						tftypes.Int64Value(4),
						tftypes.Int64Value(5),
					}),
				StringList: tftypes.ListValueMust(tftypes.StringType,
					[]attr.Value{
						tftypes.StringValue("new value 1"),
						tftypes.StringValue("new value 2"),
					}),
			},
			dest: &struct {
				String     string
				Int        int
				Int8       int
				Int16      int
				Int32      int
				Int64      int
				ExtraField int
				Boolean    bool
				Float32    float32
				Float64    float64
				IntList    []int
				UintList   []uint
				StringList []string
			}{
				String:     "name old",
				Int:        10,
				ExtraField: 30,
				Boolean:    false,
				IntList:    []int{10, 20, 30},
				StringList: []string{"old value"},
			},
			expected: &struct {
				String     string
				Int        int
				Int8       int
				Int16      int
				Int32      int
				Int64      int
				ExtraField int
				Boolean    bool
				Float32    float32
				Float64    float64
				IntList    []int
				UintList   []uint
				StringList []string
			}{
				String:     "new field name",
				Int:        20,
				Int8:       20,
				Int16:      20_000,
				Int32:      20_000_000,
				Int64:      20_000_000_000_000,
				ExtraField: 30,
				Boolean:    true,
				IntList:    []int{2, 4, 5},
				UintList:   []uint{2, 4, 5},
				StringList: []string{"new value 1", "new value 2"},
			},
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			err := copyStruct(context.TODO(), tc.src, tc.dest)
			if tc.expectError {
				require.Error(t, err)
				return
			}
			require.NoError(t, err)
			assert.Equal(t, tc.expected, tc.dest)
		})
	}
}

func TestCopyTerraformToMikrotik(t *testing.T) {
	testCases := []struct {
		name        string
		src         interface{}
		dest        client.Resource
		expected    interface{}
		expectError bool
	}{
		{
			name: "pass",
			src: struct {
				Id       tftypes.String
				Bridge   tftypes.String
				Tagged   tftypes.Set
				Untagged tftypes.List
				VlanIds  tftypes.List
			}{
				Id:     tftypes.StringValue("new id field"),
				Bridge: tftypes.StringValue("new bridge"),
				Tagged: tftypes.SetValueMust(tftypes.StringType, []attr.Value{
					tftypes.StringValue("new tagged 3"),
				}),
				Untagged: tftypes.ListValueMust(tftypes.StringType, []attr.Value{
					tftypes.StringValue("new untagged 5"),
				}),

				VlanIds: tftypes.ListValueMust(tftypes.Int64Type, []attr.Value{
					tftypes.Int64Value(2),
					tftypes.Int64Value(5),
					tftypes.Int64Value(10),
				}),
			},
			dest: &client.BridgeVlan{
				Id:       "old id field",
				Bridge:   "old bridge",
				Tagged:   types.MikrotikList{"old tagged 1", "old tagged 2"},
				Untagged: types.MikrotikList{"old untagged 1"},
				VlanIds:  types.MikrotikIntList{1, 3},
			},
			expected: &client.BridgeVlan{
				Id:       "new id field",
				Bridge:   "new bridge",
				Tagged:   types.MikrotikList{"new tagged 3"},
				Untagged: types.MikrotikList{"new untagged 5"},
				VlanIds:  types.MikrotikIntList{2, 5, 10},
			},
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			err := TerraformModelToMikrotikStruct(context.TODO(), tc.src, tc.dest)
			if tc.expectError {
				require.Error(t, err)
				return
			}
			require.NoError(t, err)
			assert.Equal(t, tc.expected, tc.dest)
		})
	}
}

func TestCopyMikrotikToTerraform(t *testing.T) {
	testCases := []struct {
		name        string
		src         client.Resource
		dest        interface{}
		expected    interface{}
		expectError bool
	}{
		{
			name: "pass",
			src: &client.BridgeVlan{
				Id:       "new id field",
				Bridge:   "new bridge",
				Tagged:   types.MikrotikList{"new tagged 1", "new tagged 2"},
				Untagged: types.MikrotikList{"new untagged 1"},
				VlanIds:  types.MikrotikIntList{1, 3},
			},
			dest: &struct {
				Id       tftypes.String
				Bridge   tftypes.String
				Tagged   tftypes.List
				Untagged tftypes.List
				VlanIds  tftypes.List
			}{
				Id:     tftypes.StringValue("old id field"),
				Bridge: tftypes.StringValue("old bridge"),
				Tagged: tftypes.ListValueMust(tftypes.StringType, []attr.Value{
					tftypes.StringValue("old tagged 3"),
				}),
				Untagged: tftypes.ListValueMust(tftypes.StringType, []attr.Value{
					tftypes.StringValue("old untagged 5"),
				}),
				VlanIds: tftypes.ListValueMust(tftypes.Int64Type, []attr.Value{
					tftypes.Int64Value(2),
					tftypes.Int64Value(5),
					tftypes.Int64Value(10),
				}),
			},
			expected: &struct {
				Id       tftypes.String
				Bridge   tftypes.String
				Tagged   tftypes.List
				Untagged tftypes.List
				VlanIds  tftypes.List
			}{
				Id:     tftypes.StringValue("new id field"),
				Bridge: tftypes.StringValue("new bridge"),
				Tagged: tftypes.ListValueMust(tftypes.StringType, []attr.Value{
					tftypes.StringValue("new tagged 1"),
					tftypes.StringValue("new tagged 2"),
				}),
				Untagged: tftypes.ListValueMust(tftypes.StringType, []attr.Value{
					tftypes.StringValue("new untagged 1"),
				}),
				VlanIds: tftypes.ListValueMust(tftypes.Int64Type, []attr.Value{
					tftypes.Int64Value(1),
					tftypes.Int64Value(3),
				}),
			},
		},
	}
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			err := MikrotikStructToTerraformModel(context.TODO(), tc.src, tc.dest)
			if tc.expectError {
				require.Error(t, err)
				return
			}
			require.NoError(t, err)
			assert.Equal(t, tc.expected, tc.dest)
		})
	}
}


File: /mikrotik\provider.go
package mikrotik

import (
	"context"
	"fmt"
	"os"
	"strings"

	mt "github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-sdk/v2/diag"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)

func init() {
	schema.SchemaDescriptionBuilder = func(s *schema.Schema) string {
		desc := s.Description
		// add default value in description, if it was declared in the resource's schema.
		if s.Default != nil {
			if s.Default == "" {
				desc += " Default: `\"\"`."
			} else {
				desc += fmt.Sprintf(" Default: `%v`.", s.Default)
			}
		}

		return strings.TrimSpace(desc)
	}
}

func Provider(client *mt.Mikrotik) *schema.Provider {
	provider := &schema.Provider{
		Schema: map[string]*schema.Schema{
			"host": {
				Type:        schema.TypeString,
				Optional:    true,
				Description: "Hostname of the MikroTik router",
			},
			"username": {
				Type:        schema.TypeString,
				Optional:    true,
				Description: "User account for MikroTik api",
			},
			"password": {
				Type:        schema.TypeString,
				Optional:    true,
				Sensitive:   true,
				Description: "Password for MikroTik api",
			},
			"tls": {
				Type:        schema.TypeBool,
				Optional:    true,
				Description: "Whether to use TLS when connecting to MikroTik or not",
			},
			"ca_certificate": {
				Type:        schema.TypeString,
				Optional:    true,
				Description: "Path to MikroTik's certificate authority",
			},
			"insecure": {
				Type:        schema.TypeBool,
				Optional:    true,
				Description: "Insecure connection does not verify MikroTik's TLS certificate",
			},
		},
		ResourcesMap: map[string]*schema.Resource{},
	}

	provider.ConfigureContextFunc = func(ctx context.Context, d *schema.ResourceData) (interface{}, diag.Diagnostics) {
		if client != nil {
			return client, nil
		}
		var diags diag.Diagnostics

		address := d.Get("host").(string)
		username := d.Get("username").(string)
		password := d.Get("password").(string)
		tls := d.Get("tls").(bool)
		caCertificate := d.Get("ca_certificate").(string)
		insecure := d.Get("insecure").(bool)

		if v := os.Getenv("MIKROTIK_HOST"); v != "" {
			address = v
		}
		if v := os.Getenv("MIKROTIK_USER"); v != "" {
			username = v
		}
		if v := os.Getenv("MIKROTIK_PASSWORD"); v != "" {
			password = v
		}
		if v := os.Getenv("MIKROTIK_TLS"); v != "" {
			tlsValue, err := utils.ParseBool(v)
			if err != nil {
				diags = append(diags,
					diag.FromErr(fmt.Errorf("could not parse MIKROTIK_TLS environment variable: %w", err))...)
			}
			tls = tlsValue
		}
		if v := os.Getenv("MIKROTIK_CA_CERTIFICATE"); v != "" {
			caCertificate = v
		}
		if v := os.Getenv("MIKROTIK_INSECURE"); v != "" {
			insecureValue, err := utils.ParseBool(v)
			if err != nil {
				diags = append(diags,
					diag.FromErr(fmt.Errorf("could not parse MIKROTIK_INSECURE environment variable: %w", err))...)
			}
			insecure = insecureValue
		}

		return mt.NewClient(address, username, password, tls, caCertificate, insecure), diags
	}

	return provider
}

func NewProvider() *schema.Provider {
	return Provider(nil)
}


File: /mikrotik\provider_framework.go
package mikrotik

import (
	"context"
	"os"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/types/defaultaware"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-framework/datasource"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/provider"
	"github.com/hashicorp/terraform-plugin-framework/provider/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/types"
)

type ProviderFramework struct {
	predefinedAPIClient *client.Mikrotik
}

var (
	_ provider.Provider = (*ProviderFramework)(nil)
)

func NewProviderFramework(c *client.Mikrotik) provider.Provider {
	return &ProviderFramework{
		predefinedAPIClient: c,
	}
}

func (p *ProviderFramework) Metadata(ctx context.Context, req provider.MetadataRequest, resp *provider.MetadataResponse) {
	resp.TypeName = "mikrotik"
}

func (p *ProviderFramework) Schema(ctx context.Context, req provider.SchemaRequest, resp *provider.SchemaResponse) {
	resp.Schema = schema.Schema{
		Attributes: map[string]schema.Attribute{
			"host": schema.StringAttribute{
				Optional:    true,
				Description: "Hostname of the MikroTik router",
			},
			"username": schema.StringAttribute{
				Optional:    true,
				Description: "User account for MikroTik api",
			},
			"password": schema.StringAttribute{
				Optional:    true,
				Sensitive:   true,
				Description: "Password for MikroTik api",
			},
			"tls": schema.BoolAttribute{
				Optional:    true,
				Description: "Whether to use TLS when connecting to MikroTik or not",
			},
			"ca_certificate": schema.StringAttribute{
				Optional:    true,
				Description: "Path to MikroTik's certificate authority",
			},
			"insecure": schema.BoolAttribute{
				Optional:    true,
				Description: "Insecure connection does not verify MikroTik's TLS certificate",
			},
		},
	}
}

func (p *ProviderFramework) Configure(ctx context.Context, req provider.ConfigureRequest, resp *provider.ConfigureResponse) {
	if p.predefinedAPIClient != nil {
		resp.DataSourceData = p.predefinedAPIClient
		resp.ResourceData = p.predefinedAPIClient

		return
	}

	var data mikrotikProviderModel

	resp.Diagnostics.Append(req.Config.Get(ctx, &data)...)
	if resp.Diagnostics.HasError() {
		return
	}

	// if configuration sets provider configuration fields, the values must be known during provider configuration
	// otherwise, it is not possible to setup the client
	if data.Host.IsUnknown() {
		resp.Diagnostics.AddAttributeError(
			path.Root("host"),
			"Unknown value for MikroTik host",
			"The provider cannot create MikroTik API client as the 'host' is unknown at this moment. "+
				"Either target apply the source of the value first, set it statically or use MIKROTIK_HOST environment variable.",
		)
	}
	if data.Username.IsUnknown() {
		resp.Diagnostics.AddAttributeError(
			path.Root("username"),
			"Unknown value for MikroTik username",
			"The provider cannot create MikroTik API client as the 'username' is unknown at this moment. "+
				"Either target apply the source of the value first, set it statically or use MIKROTIK_USER environment variable.",
		)
	}
	if data.Password.IsUnknown() {
		resp.Diagnostics.AddAttributeError(
			path.Root("password"),
			"Unknown value for MikroTik password",
			"The provider cannot create MikroTik API client as the 'password' is unknown at this moment. "+
				"Either target apply the source of the value first, set it statically or use MIKROTIK_PASSWORD environment variable.",
		)
	}

	if resp.Diagnostics.HasError() {
		return
	}

	var mikrotikHost, mikrotikUser, mikrotikPassword, mikrotikCACertificates string
	var mikrotikTLS, mikrotikInsecure bool

	mikrotikHost = data.Host.ValueString()
	if v := os.Getenv("MIKROTIK_HOST"); v != "" {
		mikrotikHost = v
	}

	mikrotikUser = data.Username.ValueString()
	if v := os.Getenv("MIKROTIK_USER"); v != "" {
		mikrotikUser = v
	}

	mikrotikPassword = data.Password.ValueString()
	if v := os.Getenv("MIKROTIK_PASSWORD"); v != "" {
		mikrotikPassword = v
	}

	if !data.Tls.IsUnknown() {
		mikrotikTLS = data.Tls.ValueBool()
	}
	if v := os.Getenv("MIKROTIK_TLS"); v != "" {
		tls, err := utils.ParseBool(v)
		if err != nil {
			resp.Diagnostics.AddError("Could not parse MIKROTIK_TLS environment variable", err.Error())
		}
		mikrotikTLS = tls
	}

	mikrotikCACertificates = data.CACertificate.ValueString()
	if v := os.Getenv("MIKROTIK_CA_CERTIFICATE"); v != "" {
		mikrotikCACertificates = v
	}

	if !data.Insecure.IsUnknown() {
		mikrotikInsecure = data.Insecure.ValueBool()
	}
	if v := os.Getenv("MIKROTIK_INSECURE"); v != "" {
		insecure, err := utils.ParseBool(v)
		if err != nil {
			resp.Diagnostics.AddError("Could not parse MIKROTIK_INSECURE environment variable", err.Error())
		}
		mikrotikInsecure = insecure
	}

	if mikrotikHost == "" {
		resp.Diagnostics.AddError("Mikrotik 'host' is missing in configuration",
			"Provide it via 'host' provider configuration attribute or MIKROTIK_HOST environment variable")
	}

	if mikrotikUser == "" {
		resp.Diagnostics.AddError("Mikrotik 'username' is missing in configuration",
			"Provide it via 'host' provider configuration attribute or MIKROTIK_USER environment variable")
	}

	if resp.Diagnostics.HasError() {
		return
	}

	c := client.NewClient(mikrotikHost, mikrotikUser, mikrotikPassword,
		mikrotikTLS, mikrotikCACertificates, mikrotikInsecure)

	resp.DataSourceData = c
	resp.ResourceData = c
}

func (p *ProviderFramework) DataSources(ctx context.Context) []func() datasource.DataSource {
	return []func() datasource.DataSource{}
}

func (p *ProviderFramework) Resources(ctx context.Context) []func() resource.Resource {
	return defaultaware.WrapResources([]func() resource.Resource{
		NewBgpInstanceResource,
		NewBgpPeerResource,
		NewBridgePortResource,
		NewBridgeResource,
		NewBridgeVlanResource,
		NewDhcpLeaseResource,
		NewDhcpServerNetworkResource,
		NewDhcpServerResource,
		NewDnsRecordResource,
		NewFirewallFilterRuleResource,
		NewInterfaceListMemberResource,
		NewInterfaceListResource,
		NewInterfaceWireguardPeerResource,
		NewInterfaceWireguardResource,
		NewIpAddressResource,
		NewIpv6AddressResource,
		NewPoolResource,
		NewSchedulerResource,
		NewScriptResource,
		NewVlanInterfaceResource,
		NewWirelessInterfaceResource,
	},
	)
}

type mikrotikProviderModel struct {
	Host          types.String `tfsdk:"host"`
	Username      types.String `tfsdk:"username"`
	Password      types.String `tfsdk:"password"`
	Tls           types.Bool   `tfsdk:"tls"`
	CACertificate types.String `tfsdk:"ca_certificate"`
	Insecure      types.Bool   `tfsdk:"insecure"`
}


File: /mikrotik\provider_test.go
package mikrotik

import (
	"context"
	"os"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework/providerserver"
	"github.com/hashicorp/terraform-plugin-go/tfprotov5"
	"github.com/hashicorp/terraform-plugin-mux/tf5muxserver"
	"github.com/hashicorp/terraform-plugin-mux/tf6to5server"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema"
)

const (
	// Provider name for single configuration testing
	ProviderNameMikrotik = "mikrotik"
)

var testAccProtoV5ProviderFactories map[string]func() (tfprotov5.ProviderServer, error)
var testAccProvider *schema.Provider

var apiClient *client.Mikrotik

func init() {
	apiClient = client.NewClient(os.Getenv("MIKROTIK_HOST"), os.Getenv("MIKROTIK_USER"), os.Getenv("MIKROTIK_PASSWORD"), false, "", true)

	testAccProvider = Provider(apiClient)
	downgradedProviderFramework, _ := tf6to5server.DowngradeServer(
		context.Background(),
		providerserver.NewProtocol6(NewProviderFramework(apiClient)),
	)
	servers := []func() tfprotov5.ProviderServer{
		testAccProvider.GRPCProvider,
		func() tfprotov5.ProviderServer {
			return downgradedProviderFramework
		},
	}
	muxServer, _ := tf5muxserver.NewMuxServer(context.Background(), servers...)

	testAccProtoV5ProviderFactories = map[string]func() (tfprotov5.ProviderServer, error){
		ProviderNameMikrotik: func() (tfprotov5.ProviderServer, error) {
			return muxServer, nil
		},
	}
}

func testAccPreCheck(t *testing.T) {
	if v := os.Getenv("MIKROTIK_HOST"); v == "" {
		t.Fatal("The MIKROTIK_HOST environment variable must be set")
	}
	if v := os.Getenv("MIKROTIK_USER"); v == "" {
		t.Fatal("The MIKROTIK_USER environment variable must be set")
	}
	if _, exists := os.LookupEnv("MIKROTIK_PASSWORD"); !exists {
		t.Fatal("The MIKROTIK_PASSWORD environment variable must be set")
	}
}


File: /mikrotik\resource_bgp_instance.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/int64default"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type bgpInstance struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &bgpInstance{}
	_ resource.ResourceWithConfigure   = &bgpInstance{}
	_ resource.ResourceWithImportState = &bgpInstance{}
)

// NewBgpInstanceResource is a helper function to simplify the provider implementation.
func NewBgpInstanceResource() resource.Resource {
	return &bgpInstance{}
}

func (r *bgpInstance) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *bgpInstance) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_bgp_instance"
}

// Schema defines the schema for the resource.
func (s *bgpInstance) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a Mikrotik BGP Instance.",

		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "ID of this resource.",
			},
			"name": schema.StringAttribute{
				Required:    true,
				Description: "The name of the BGP instance.",
			},
			"as": schema.Int64Attribute{
				Required:    true,
				Description: "The 32-bit BGP autonomous system number. Must be a value within 0 to 4294967295.",
			},
			"client_to_client_reflection": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(true),
				Description: "In case this instance is a route reflector: whether to redistribute routes learned from one routing reflection client to other clients.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "The comment of the BGP instance to be created.",
			},
			"confederation_peers": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "List of AS numbers internal to the [local] confederation. For example: `10,20,30-50`.",
			},
			"disabled": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "Whether instance is disabled.",
			},
			"ignore_as_path_len": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "Whether to ignore AS_PATH attribute in BGP route selection algorithm.",
			},
			"out_filter": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "Output routing filter chain used by all BGP peers belonging to this instance.",
			},
			"redistribute_connected": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "If enabled, this BGP instance will redistribute the information about connected routes.",
			},
			"redistribute_ospf": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "If enabled, this BGP instance will redistribute the information about routes learned by OSPF.",
			},
			"redistribute_other_bgp": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "If enabled, this BGP instance will redistribute the information about routes learned by other BGP instances.",
			},
			"redistribute_rip": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "If enabled, this BGP instance will redistribute the information about routes learned by RIP.",
			},
			"redistribute_static": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "If enabled, the router will redistribute the information about static routes added to its routing database.",
			},
			"router_id": schema.StringAttribute{
				Required:    true,
				Description: "BGP Router ID (for this instance). If set to 0.0.0.0, BGP will use one of router's IP addresses.",
			},
			"routing_table": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "Name of routing table this BGP instance operates on. ",
			},
			"cluster_id": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "In case this instance is a route reflector: cluster ID of the router reflector cluster this instance belongs to.",
			},
			"confederation": schema.Int64Attribute{
				Optional:    true,
				Computed:    true,
				Default:     int64default.StaticInt64(0),
				Description: "In case of BGP confederations: autonomous system number that identifies the [local] confederation as a whole.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *bgpInstance) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel bgpInstanceModel
	var mikrotikModel client.BgpInstance
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *bgpInstance) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel bgpInstanceModel
	var mikrotikModel client.BgpInstance
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *bgpInstance) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel bgpInstanceModel
	var mikrotikModel client.BgpInstance
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *bgpInstance) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel bgpInstanceModel
	var mikrotikModel client.BgpInstance
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *bgpInstance) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("name"), req, resp)
}

type bgpInstanceModel struct {
	Id                       tftypes.String `tfsdk:"id"`
	Name                     tftypes.String `tfsdk:"name"`
	As                       tftypes.Int64  `tfsdk:"as"`
	ClientToClientReflection tftypes.Bool   `tfsdk:"client_to_client_reflection"`
	Comment                  tftypes.String `tfsdk:"comment"`
	ConfederationPeers       tftypes.String `tfsdk:"confederation_peers"`
	Disabled                 tftypes.Bool   `tfsdk:"disabled"`
	IgnoreAsPathLen          tftypes.Bool   `tfsdk:"ignore_as_path_len"`
	OutFilter                tftypes.String `tfsdk:"out_filter"`
	RedistributeConnected    tftypes.Bool   `tfsdk:"redistribute_connected"`
	RedistributeOspf         tftypes.Bool   `tfsdk:"redistribute_ospf"`
	RedistributeOtherBgp     tftypes.Bool   `tfsdk:"redistribute_other_bgp"`
	RedistributeRip          tftypes.Bool   `tfsdk:"redistribute_rip"`
	RedistributeStatic       tftypes.Bool   `tfsdk:"redistribute_static"`
	RouterID                 tftypes.String `tfsdk:"router_id"`
	RoutingTable             tftypes.String `tfsdk:"routing_table"`
	ClusterID                tftypes.String `tfsdk:"cluster_id"`
	Confederation            tftypes.Int64  `tfsdk:"confederation"`
}


File: /mikrotik\resource_bgp_instance_test.go
package mikrotik

import (
	"fmt"
	"regexp"
	"strconv"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/acctest"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestAccMikrotikBgpInstance_create(t *testing.T) {
	client.SkipIfRouterOSV7OrLater(t, sysResources)
	name := acctest.RandomWithPrefix("tf-acc-create")
	routerId := internal.GetNewIpAddr()
	as := acctest.RandIntRange(1, 65535)

	resourceName := "mikrotik_bgp_instance.bar"

	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikBgpInstanceDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccBgpInstance(name, as, routerId),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBgpInstanceExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "as", strconv.Itoa(as)),
					resource.TestCheckResourceAttr(resourceName, "router_id", routerId),
				),
			},
		},
	})
}

func TestAccMikrotikBgpInstance_createFailsOnRouterOSv7(t *testing.T) {
	client.SkipIfRouterOSV6OrEarlier(t, sysResources)

	name := acctest.RandomWithPrefix("tf-acc-create")
	routerId := internal.GetNewIpAddr()
	as := acctest.RandIntRange(1, 65535)

	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikBgpInstanceDestroy,
		Steps: []resource.TestStep{
			{
				Config:      testAccBgpInstance(name, as, routerId),
				ExpectError: regexp.MustCompile(`Your RouterOS version does not support`),
			},
		},
	})
}

func TestAccMikrotikBgpInstance_createAndPlanWithNonExistantBgpInstance(t *testing.T) {
	client.SkipIfRouterOSV7OrLater(t, sysResources)
	name := acctest.RandomWithPrefix("tf-acc-create_with_plan")
	routerId := internal.GetNewIpAddr()
	as := acctest.RandIntRange(1, 65535)

	resourceName := "mikrotik_bgp_instance.bar"

	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikBgpInstanceDestroy,

		Steps: []resource.TestStep{
			{
				Config: testAccBgpInstance(name, as, routerId),
				Check: resource.ComposeTestCheckFunc(
					testAccBgpInstanceExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
				),
			},
			{
				Config:  testAccBgpInstance(name, as, routerId),
				Destroy: true,
			},
			{
				Config:             testAccBgpInstance(name, as, routerId),
				PlanOnly:           true,
				ExpectNonEmptyPlan: true,
			},
		},
	})
}

func TestAccMikrotikBgpInstance_updateBgpInstance(t *testing.T) {
	client.SkipIfRouterOSV7OrLater(t, sysResources)
	name := acctest.RandomWithPrefix("tf-acc-update")
	routerId := internal.GetNewIpAddr()
	updatedRouterId := internal.GetNewIpAddr()
	clusterId := internal.GetNewIpAddr()
	as := acctest.RandIntRange(1, 65535)
	updatedAs := acctest.RandIntRange(1, 65535)
	comment := acctest.RandomWithPrefix("test comment ")
	confederation := 8

	resourceName := "mikrotik_bgp_instance.bar"

	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikBgpInstanceDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccBgpInstance(name, as, routerId),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBgpInstanceExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "as", strconv.Itoa(as)),
					resource.TestCheckResourceAttr(resourceName, "router_id", routerId),
				),
			},
			{
				Config: testAccBgpInstanceUpdatedAsAndRouterId(name, updatedAs, updatedRouterId),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBgpInstanceExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "as", strconv.Itoa(updatedAs)),
					resource.TestCheckResourceAttr(resourceName, "router_id", updatedRouterId),
				),
			},
			{
				Config: testAccBgpInstanceUpdatedOptionalFields(name, updatedAs, updatedRouterId, comment, clusterId, confederation),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBgpInstanceExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "as", strconv.Itoa(updatedAs)),
					resource.TestCheckResourceAttr(resourceName, "router_id", updatedRouterId),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
					resource.TestCheckResourceAttr(resourceName, "cluster_id", clusterId),
					resource.TestCheckResourceAttr(resourceName, "client_to_client_reflection", "false"),
					resource.TestCheckResourceAttr(resourceName, "confederation", strconv.Itoa(confederation)),
				),
			},
		},
	})
}

func TestAccMikrotikBgpInstance_import(t *testing.T) {
	client.SkipIfRouterOSV7OrLater(t, sysResources)
	name := acctest.RandomWithPrefix("tf-acc-import")
	routerId := internal.GetNewIpAddr()
	as := acctest.RandIntRange(1, 65535)

	resourceName := "mikrotik_bgp_instance.bar"

	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikBgpInstanceDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccBgpInstance(name, as, routerId),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBgpInstanceExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id")),
			},
			{
				ResourceName:      resourceName,
				ImportStateId:     name,
				ImportState:       true,
				ImportStateVerify: true,
			},
		},
	})
}

func testAccBgpInstance(name string, as int, routerId string) string {
	return fmt.Sprintf(`
resource "mikrotik_bgp_instance" "bar" {
    name = "%s"
    as = %d
    router_id = "%s"
}
`, name, as, routerId)
}

func testAccBgpInstanceUpdatedAsAndRouterId(name string, as int, routerId string) string {
	return fmt.Sprintf(`
resource "mikrotik_bgp_instance" "bar" {
    name = "%s"
    as = %d
    router_id = "%s"
}
`, name, as, routerId)
}

func testAccBgpInstanceUpdatedOptionalFields(name string, as int, routerId, comment, clusterId string, confederation int) string {
	return fmt.Sprintf(`
resource "mikrotik_bgp_instance" "bar" {
    name = "%s"
    as = %d
    router_id = "%s"
    comment = "%s"
    cluster_id = "%s"
    client_to_client_reflection = false
    confederation = %d
}
`, name, as, routerId, comment, clusterId, confederation)
}

func testAccBgpInstanceExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("resource not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("mikrotik_bgp_instance does not exist in the statefile")
		}

		_, err := apiClient.FindBgpInstance(rs.Primary.Attributes["name"])

		if err != nil {
			return fmt.Errorf("Unable to get the bgp instance with error: %v", err)
		}

		return nil
	}
}

func testAccCheckMikrotikBgpInstanceDestroy(s *terraform.State) error {
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_bgp_instance" {
			continue
		}

		bgpInstance, err := apiClient.FindBgpInstance(rs.Primary.Attributes["name"])

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if bgpInstance != nil {
			return fmt.Errorf("bgp instance (%s) still exists", bgpInstance.Name)
		}
	}
	return nil
}


File: /mikrotik\resource_bgp_peer.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"
	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type bgpPeer struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &bgpPeer{}
	_ resource.ResourceWithConfigure   = &bgpPeer{}
	_ resource.ResourceWithImportState = &bgpPeer{}
)

// NewBgpPeerResource is a helper function to simplify the provider implementation.
func NewBgpPeerResource() resource.Resource {
	return &bgpPeer{}
}

func (r *bgpPeer) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *bgpPeer) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_bgp_peer"
}

// Schema defines the schema for the resource.
func (s *bgpPeer) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a MikroTik BGP Peer.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique MikroTik identifier.",
			},
			"name": schema.StringAttribute{
				Required:    true,
				Description: "The name of the BGP peer.",
			},
			"address_families": schema.StringAttribute{
				Optional: true,
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Default:     stringdefault.StaticString("ip"),
				Description: "The list of address families about which this peer will exchange routing information.",
			},
			"allow_as_in": schema.Int64Attribute{
				Optional:    true,
				Computed:    true,
				Description: "How many times to allow own AS number in AS-PATH, before discarding a prefix.",
			},
			"as_override": schema.BoolAttribute{
				Computed:    true,
				Optional:    true,
				Default:     booldefault.StaticBool(false),
				Description: "If set, then all instances of remote peer's AS number in BGP AS PATH attribute are replaced with local AS number before sending route update to that peer.",
			},
			"cisco_vpls_nlri_len_fmt": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "VPLS NLRI length format type.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The comment of the BGP peer to be created.",
			},
			"default_originate": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("never"),
				Description: "The comment of the BGP peer to be created.",
			},
			"disabled": schema.BoolAttribute{
				Computed:    true,
				Optional:    true,
				Default:     booldefault.StaticBool(false),
				Description: "Whether peer is disabled.",
			},
			"hold_time": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("3m"),
				Description: "Specifies the BGP Hold Time value to use when negotiating with peer",
			},
			"in_filter": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The name of the routing filter chain that is applied to the incoming routing information.",
			},
			"instance": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("default"),
				Description: "The name of the instance this peer belongs to. See Mikrotik bgp instance resource.",
			},
			"keepalive_time": schema.StringAttribute{
				Optional: true,
				Computed: true,
			},
			"max_prefix_limit": schema.Int64Attribute{
				Optional:    true,
				Computed:    true,
				Description: "Maximum number of prefixes to accept from a specific peer.",
			},
			"max_prefix_restart_time": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Minimum time interval after which peers can reestablish BGP session.",
			},
			"multihop": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Specifies whether the remote peer is more than one hop away.",
			},
			"nexthop_choice": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("default"),
				Description: "Affects the outgoing NEXT_HOP attribute selection, either: 'default', 'force-self', or 'propagate'",
			},
			"out_filter": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The name of the routing filter chain that is applied to the outgoing routing information. ",
			},
			"passive": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "Name of the routing filter chain that is applied to the outgoing routing information.",
			},
			"remote_address": schema.StringAttribute{
				Required:    true,
				Description: "The address of the remote peer",
			},
			"remote_as": schema.Int64Attribute{
				Required:    true,
				Description: "The 32-bit AS number of the remote peer.",
			},
			"remote_port": schema.Int64Attribute{
				Optional:    true,
				Computed:    true,
				Description: "Remote peers port to establish tcp session.",
			},
			"remove_private_as": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Description: "If set, then BGP AS-PATH attribute is removed before sending out route update if attribute contains only private AS numbers.",
			},
			"route_reflect": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Specifies whether this peer is route reflection client.",
			},
			"tcp_md5_key": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Key used to authenticate the connection with TCP MD5 signature as described in RFC 2385.",
			},
			"ttl": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("default"),
				Description: "Time To Live, the hop limit for TCP connection. This is a `string` field that can be 'default' or '0'-'255'.",
			},
			"update_source": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "If address is specified, this address is used as the source address of the outgoing TCP connection.",
			},
			"use_bfd": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Whether to use BFD protocol for fast state detection.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *bgpPeer) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel bgpPeerModel
	var mikrotikModel client.BgpPeer
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *bgpPeer) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel bgpPeerModel
	var mikrotikModel client.BgpPeer
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *bgpPeer) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel bgpPeerModel
	var mikrotikModel client.BgpPeer
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *bgpPeer) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel bgpPeerModel
	var mikrotikModel client.BgpPeer
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *bgpPeer) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("name"), req, resp)
}

type bgpPeerModel struct {
	Id                   tftypes.String `tfsdk:"id"`
	Name                 tftypes.String `tfsdk:"name"`
	AddressFamilies      tftypes.String `tfsdk:"address_families"`
	AllowAsIn            tftypes.Int64  `tfsdk:"allow_as_in"`
	AsOverride           tftypes.Bool   `tfsdk:"as_override"`
	CiscoVplsNlriLenFmt  tftypes.String `tfsdk:"cisco_vpls_nlri_len_fmt"`
	Comment              tftypes.String `tfsdk:"comment"`
	DefaultOriginate     tftypes.String `tfsdk:"default_originate"`
	Disabled             tftypes.Bool   `tfsdk:"disabled"`
	HoldTime             tftypes.String `tfsdk:"hold_time"`
	InFilter             tftypes.String `tfsdk:"in_filter"`
	Instance             tftypes.String `tfsdk:"instance"`
	KeepAliveTime        tftypes.String `tfsdk:"keepalive_time"`
	MaxPrefixLimit       tftypes.Int64  `tfsdk:"max_prefix_limit"`
	MaxPrefixRestartTime tftypes.String `tfsdk:"max_prefix_restart_time"`
	Multihop             tftypes.Bool   `tfsdk:"multihop"`
	NexthopChoice        tftypes.String `tfsdk:"nexthop_choice"`
	OutFilter            tftypes.String `tfsdk:"out_filter"`
	Passive              tftypes.Bool   `tfsdk:"passive"`
	RemoteAddress        tftypes.String `tfsdk:"remote_address"`
	RemoteAs             tftypes.Int64  `tfsdk:"remote_as"`
	RemotePort           tftypes.Int64  `tfsdk:"remote_port"`
	RemovePrivateAs      tftypes.Bool   `tfsdk:"remove_private_as"`
	RouteReflect         tftypes.Bool   `tfsdk:"route_reflect"`
	TCPMd5Key            tftypes.String `tfsdk:"tcp_md5_key"`
	TTL                  tftypes.String `tfsdk:"ttl"`
	UpdateSource         tftypes.String `tfsdk:"update_source"`
	UseBfd               tftypes.Bool   `tfsdk:"use_bfd"`
}


File: /mikrotik\resource_bgp_peer_test.go
package mikrotik

import (
	"fmt"
	"strconv"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/acctest"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

var instanceName string = "default"
var peerTTL string = "default"
var addressFamilies string = "ip"
var defaultOriginate string = "never"
var holdTime string = "3m"
var nextHopChoice string = "default"

var maxPrefixRestartTime string = "1w3d"
var tcpMd5Key string = "test-tcp-md5-key"
var updatedTTL string = "255"
var updatedUseBfd string = "true"

func TestAccMikrotikBgpPeer_create(t *testing.T) {
	client.SkipIfRouterOSV7OrLater(t, sysResources)
	name := acctest.RandomWithPrefix("tf-acc-create")
	remoteAs := acctest.RandIntRange(1, 65535)
	remoteAddress, _ := acctest.RandIpAddress("192.168.0.0/24")

	resourceName := "mikrotik_bgp_peer.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikBgpPeerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccBgpPeer(name, remoteAs, remoteAddress),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBgpPeerExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "remote_as", strconv.Itoa(remoteAs)),
					resource.TestCheckResourceAttr(resourceName, "instance", instanceName),
					resource.TestCheckResourceAttr(resourceName, "ttl", peerTTL),
					resource.TestCheckResourceAttr(resourceName, "address_families", addressFamilies),
					resource.TestCheckResourceAttr(resourceName, "default_originate", defaultOriginate),
					resource.TestCheckResourceAttr(resourceName, "hold_time", holdTime),
					resource.TestCheckResourceAttr(resourceName, "nexthop_choice", nextHopChoice),
					resource.TestCheckResourceAttr(resourceName, "as_override", "false"),
					resource.TestCheckResourceAttr(resourceName, "disabled", "false"),
					resource.TestCheckResourceAttr(resourceName, "multihop", "false"),
					resource.TestCheckResourceAttr(resourceName, "passive", "false"),
					resource.TestCheckResourceAttr(resourceName, "remove_private_as", "false"),
					resource.TestCheckResourceAttr(resourceName, "route_reflect", "false"),
					resource.TestCheckResourceAttr(resourceName, "use_bfd", "false"),
				),
			},
		},
	})
}

func TestAccMikrotikBgpPeer_createAndPlanWithNonExistantBgpPeer(t *testing.T) {
	client.SkipIfRouterOSV7OrLater(t, sysResources)
	name := acctest.RandomWithPrefix("tf-acc-create_with_plan")
	remoteAs := acctest.RandIntRange(1, 65535)
	remoteAddress, _ := acctest.RandIpAddress("192.168.1.0/24")

	resourceName := "mikrotik_bgp_peer.bar"
	removeBgpPeer := func() {

		c := client.NewClient(client.GetConfigFromEnv())
		bgpPeer, err := c.FindBgpPeer(name)
		if err != nil {
			t.Fatalf("Error finding the bgp peer by name: %s", err)
		}
		err = c.DeleteBgpPeer(bgpPeer.Name)
		if err != nil {
			t.Fatalf("Error removing the bgp peer: %s", err)
		}
	}
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikBgpPeerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccBgpPeer(name, remoteAs, remoteAddress),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBgpPeerExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id")),
			},
			{
				PreConfig:          removeBgpPeer,
				Config:             testAccBgpPeer(name, remoteAs, remoteAddress),
				ExpectNonEmptyPlan: false,
			},
		},
	})
}

func TestAccMikrotikBgpPeer_updateBgpPeer(t *testing.T) {
	client.SkipIfRouterOSV7OrLater(t, sysResources)
	name := acctest.RandomWithPrefix("tf-acc-update")
	remoteAs := acctest.RandIntRange(1, 65535)
	remoteAddress, _ := acctest.RandIpAddress("192.168.3.0/24")

	resourceName := "mikrotik_bgp_peer.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikBgpPeerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccBgpPeer(name, remoteAs, remoteAddress),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBgpPeerExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "remote_as", strconv.Itoa(remoteAs)),
					resource.TestCheckResourceAttr(resourceName, "instance", instanceName),
					resource.TestCheckResourceAttr(resourceName, "ttl", peerTTL),
					resource.TestCheckResourceAttr(resourceName, "address_families", addressFamilies),
					resource.TestCheckResourceAttr(resourceName, "default_originate", defaultOriginate),
					resource.TestCheckResourceAttr(resourceName, "hold_time", holdTime),
					resource.TestCheckResourceAttr(resourceName, "nexthop_choice", nextHopChoice),
					resource.TestCheckResourceAttr(resourceName, "as_override", "false"),
					resource.TestCheckResourceAttr(resourceName, "disabled", "false"),
					resource.TestCheckResourceAttr(resourceName, "multihop", "false"),
					resource.TestCheckResourceAttr(resourceName, "passive", "false"),
					resource.TestCheckResourceAttr(resourceName, "remove_private_as", "false"),
					resource.TestCheckResourceAttr(resourceName, "route_reflect", "false"),
					resource.TestCheckResourceAttr(resourceName, "use_bfd", "false"),
				),
			},
			{
				Config: testAccBgpPeerUpdatedUseBfdTCPMd5KeyTTLAndMaxPrefixRestartTime(name, remoteAs, remoteAddress),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBgpPeerExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "remote_as", strconv.Itoa(remoteAs)),
					resource.TestCheckResourceAttr(resourceName, "instance", instanceName),
					resource.TestCheckResourceAttr(resourceName, "address_families", addressFamilies),
					resource.TestCheckResourceAttr(resourceName, "default_originate", defaultOriginate),
					resource.TestCheckResourceAttr(resourceName, "hold_time", holdTime),
					resource.TestCheckResourceAttr(resourceName, "nexthop_choice", nextHopChoice),
					resource.TestCheckResourceAttr(resourceName, "as_override", "false"),
					resource.TestCheckResourceAttr(resourceName, "disabled", "false"),
					resource.TestCheckResourceAttr(resourceName, "multihop", "false"),
					resource.TestCheckResourceAttr(resourceName, "passive", "false"),
					resource.TestCheckResourceAttr(resourceName, "remove_private_as", "false"),
					resource.TestCheckResourceAttr(resourceName, "route_reflect", "false"),
					resource.TestCheckResourceAttr(resourceName, "ttl", updatedTTL),
					resource.TestCheckResourceAttr(resourceName, "max_prefix_restart_time", maxPrefixRestartTime),
					resource.TestCheckResourceAttr(resourceName, "use_bfd", updatedUseBfd),
					resource.TestCheckResourceAttr(resourceName, "tcp_md5_key", tcpMd5Key),
				),
			},
		},
	})
}

func TestAccMikrotikBgpPeer_import(t *testing.T) {
	client.SkipIfRouterOSV7OrLater(t, sysResources)
	name := acctest.RandomWithPrefix("tf-acc-import")
	remoteAs := acctest.RandIntRange(1, 65535)
	remoteAddress, _ := acctest.RandIpAddress("192.168.4.0/24")

	resourceName := "mikrotik_bgp_peer.bar"

	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikBgpPeerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccBgpPeer(name, remoteAs, remoteAddress),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBgpPeerExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id")),
			},
			{
				ResourceName:      resourceName,
				ImportState:       true,
				ImportStateVerify: true,
				ImportStateId:     name,
			},
		},
	})
}

func testAccBgpPeer(name string, remoteAs int, remoteAddress string) string {
	return fmt.Sprintf(`
resource "mikrotik_bgp_peer" "bar" {
    name = "%s"
    remote_as = %d
    remote_address = "%s"
    instance = "%s"
    ttl = "%s"
    address_families = "%s"
    default_originate = "%s"
    hold_time = "%s"
    nexthop_choice = "%s"
}
`, name, remoteAs, remoteAddress, instanceName, peerTTL, addressFamilies, defaultOriginate, holdTime, nextHopChoice)
}

func testAccBgpPeerUpdatedUseBfdTCPMd5KeyTTLAndMaxPrefixRestartTime(name string, remoteAs int, remoteAddress string) string {
	return fmt.Sprintf(`
resource "mikrotik_bgp_peer" "bar" {
    name = "%s"
    remote_as = %d
    remote_address = "%s"
    instance = "%s"
    ttl = "%s"
    address_families = "%s"
    default_originate = "%s"
    hold_time = "%s"
    nexthop_choice = "%s"

    max_prefix_restart_time = "%s"
    use_bfd = true
    tcp_md5_key = "%s"
}
`, name, remoteAs, remoteAddress, instanceName, updatedTTL, addressFamilies, defaultOriginate, holdTime, nextHopChoice, maxPrefixRestartTime, tcpMd5Key)
}

func testAccBgpPeerExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("mikrotik_bgp_peer does not exist in the statefile")
		}

		c := client.NewClient(client.GetConfigFromEnv())

		bgpPeer, err := c.FindBgpPeer(rs.Primary.Attributes["name"])

		if err != nil {
			return fmt.Errorf("Unable to get the bgp peer with error: %v", err)
		}

		if bgpPeer == nil {
			return fmt.Errorf("Unable to get the bgp peer")
		}

		return nil
	}
}

func testAccCheckMikrotikBgpPeerDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_bgp_peer" {
			continue
		}

		bgpPeer, err := c.FindBgpPeer(rs.Primary.Attributes["name"])

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if bgpPeer != nil {
			return fmt.Errorf("bgp peer (%s) still exists", bgpPeer.Name)
		}
	}
	return nil
}


File: /mikrotik\resource_bridge.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type bridge struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &bridge{}
	_ resource.ResourceWithConfigure   = &bridge{}
	_ resource.ResourceWithImportState = &bridge{}
)

// NewBridgeResource is a helper function to simplify the provider implementation.
func NewBridgeResource() resource.Resource {
	return &bridge{}
}

func (r *bridge) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *bridge) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_bridge"
}

// Schema defines the schema for the resource.
func (s *bridge) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Manages a bridge resource on remote MikroTik device.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique ID for the instance.",
			},
			"name": schema.StringAttribute{
				Required:    true,
				Description: "Name of the bridge interface",
			},
			"fast_forward": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(true),
				Description: "Special and faster case of FastPath which works only on bridges with 2 interfaces (enabled by default only for new bridges).",
			},
			"vlan_filtering": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Globally enables or disables VLAN functionality for bridge.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Short description of the interface.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *bridge) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel bridgeModel
	var mikrotikModel client.Bridge
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *bridge) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel bridgeModel
	var mikrotikModel client.Bridge
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *bridge) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel bridgeModel
	var mikrotikModel client.Bridge
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *bridge) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel bridgeModel
	var mikrotikModel client.Bridge
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *bridge) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("name"), req, resp)
}

type bridgeModel struct {
	Id            tftypes.String `tfsdk:"id"`
	Name          tftypes.String `tfsdk:"name"`
	FastForward   tftypes.Bool   `tfsdk:"fast_forward"`
	VlanFiltering tftypes.Bool   `tfsdk:"vlan_filtering"`
	Comment       tftypes.String `tfsdk:"comment"`
}


File: /mikrotik\resource_bridge_port.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-framework-validators/int64validator"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"
	"github.com/hashicorp/terraform-plugin-framework/schema/validator"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type bridgePort struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &bridgePort{}
	_ resource.ResourceWithConfigure   = &bridgePort{}
	_ resource.ResourceWithImportState = &bridgePort{}
)

// NewBridgePortResource is a helper function to simplify the provider implementation.
func NewBridgePortResource() resource.Resource {
	return &bridgePort{}
}

func (r *bridgePort) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *bridgePort) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_bridge_port"
}

// Schema defines the schema for the resource.
func (s *bridgePort) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Manages ports in bridge associations.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique ID for the instance.",
			},
			"bridge": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The bridge interface the respective interface is grouped in.",
			},
			"interface": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Name of the interface.",
			},
			"pvid": schema.Int64Attribute{
				Optional: true,
				Computed: true,
				Validators: []validator.Int64{
					int64validator.Between(1, 4094),
				},
				Description: "Port VLAN ID (pvid) specifies which VLAN the untagged ingress traffic is assigned to. This property only has effect when vlan-filtering is set to yes.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Short description for this association.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *bridgePort) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel bridgePortModel
	var mikrotikModel client.BridgePort
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *bridgePort) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel bridgePortModel
	var mikrotikModel client.BridgePort
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *bridgePort) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel bridgePortModel
	var mikrotikModel client.BridgePort
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *bridgePort) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel bridgePortModel
	var mikrotikModel client.BridgePort
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *bridgePort) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	utils.ImportUppercaseWrapper(resource.ImportStatePassthroughID)(ctx, path.Root("id"), req, resp)
}

type bridgePortModel struct {
	Id        tftypes.String `tfsdk:"id"`
	Bridge    tftypes.String `tfsdk:"bridge"`
	Interface tftypes.String `tfsdk:"interface"`
	PVId      tftypes.Int64  `tfsdk:"pvid"`
	Comment   tftypes.String `tfsdk:"comment"`
}


File: /mikrotik\resource_bridge_port_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestBridgePort_basic(t *testing.T) {
	rStatePath := "mikrotik_bridge_port.testacc"
	bridgeName := "testacc_bridge"
	bridgeInterface := "*0"
	remoteBridgePort := client.BridgePort{}
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckBridgePortDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccBridgePortConfig(bridgeName, bridgeInterface, 1, "acceptance test bridge port"),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBridgePortExists(rStatePath, &remoteBridgePort),
					resource.TestCheckResourceAttrSet(rStatePath, "id"),
					resource.TestCheckResourceAttr(rStatePath, "bridge", bridgeName),
					resource.TestCheckResourceAttr(rStatePath, "interface", bridgeInterface),
					resource.TestCheckResourceAttr(rStatePath, "pvid", "1"),
					resource.TestCheckResourceAttr(rStatePath, "comment", "acceptance test bridge port"),
				),
			},
			{
				Config: testAccBridgePortConfig(bridgeName+"_updated", bridgeInterface, 2, "updated resource"),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBridgePortExists(rStatePath, &remoteBridgePort),
					resource.TestCheckResourceAttrSet(rStatePath, "id"),
					resource.TestCheckResourceAttr(rStatePath, "bridge", bridgeName+"_updated"),
					resource.TestCheckResourceAttr(rStatePath, "interface", bridgeInterface),
					resource.TestCheckResourceAttr(rStatePath, "pvid", "2"),
					resource.TestCheckResourceAttr(rStatePath, "comment", "updated resource"),
				),
			},
			{
				ImportState:       true,
				ResourceName:      rStatePath,
				ImportStateVerify: true,
			},
		},
	})
}

func testAccBridgePortExists(resourceID string, record *client.BridgePort) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		r, ok := s.RootModule().Resources[resourceID]
		if !ok {
			return fmt.Errorf("resource %q not found in state", resourceID)
		}
		if r.Primary.ID == "" {
			return fmt.Errorf("resource %q has empty primary ID in state", resourceID)
		}
		c := client.NewClient(client.GetConfigFromEnv())
		remoteRecord, err := c.FindBridgePort(r.Primary.ID)
		if err != nil {
			return err
		}
		*record = *remoteRecord

		return nil
	}
}

func testAccCheckBridgePortDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_bridge_port" {
			continue
		}

		remoteRecord, err := c.FindBridgePort(rs.Primary.ID)
		if err != nil && !client.IsNotFoundError(err) {
			return fmt.Errorf("expected not found error, got %+#v", err)
		}

		if remoteRecord != nil {
			return fmt.Errorf("bridge port %q still exists in remote system", remoteRecord.Id)
		}
	}

	return nil
}

func testAccBridgePortConfig(bridgeName, bridgeInterface string, pvid int, comment string) string {
	return fmt.Sprintf(`
		resource mikrotik_bridge "testacc" {
			name = %q
		}

		resource mikrotik_bridge_port "testacc" {
			bridge    = mikrotik_bridge.testacc.name
			interface = %q
			pvid      = %d
			comment   = %q
		}
	`, bridgeName, bridgeInterface, pvid, comment)
}


File: /mikrotik\resource_bridge_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestAccBridge_basic(t *testing.T) {
	rName := "testacc_bridge"
	bridge := client.Bridge{}
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccBridgeDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccBridgeConfig(rName, true, false, "testacc bridge"),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBridgeExists("mikrotik_bridge.testacc", &bridge),
					resource.TestCheckResourceAttr("mikrotik_bridge.testacc", "name", rName),
					resource.TestCheckResourceAttr("mikrotik_bridge.testacc", "fast_forward", "true"),
					resource.TestCheckResourceAttr("mikrotik_bridge.testacc", "vlan_filtering", "false"),
					resource.TestCheckResourceAttr("mikrotik_bridge.testacc", "comment", "testacc bridge"),
				),
			},
			{
				Config: testAccBridgeConfig(rName+"_updated", false, true, "updated bridge"),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBridgeExists("mikrotik_bridge.testacc", &bridge),
					resource.TestCheckResourceAttr("mikrotik_bridge.testacc", "name", rName+"_updated"),
					resource.TestCheckResourceAttr("mikrotik_bridge.testacc", "fast_forward", "false"),
					resource.TestCheckResourceAttr("mikrotik_bridge.testacc", "vlan_filtering", "true"),
					resource.TestCheckResourceAttr("mikrotik_bridge.testacc", "comment", "updated bridge"),
				),
			},
			{
				ImportState:       true,
				ResourceName:      "mikrotik_bridge.testacc",
				ImportStateId:     rName + "_updated",
				ImportStateVerify: true,
			},
		},
	})
}

func testAccBridgeExists(resource string, record *client.Bridge) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		r, ok := s.RootModule().Resources[resource]
		if !ok {
			return fmt.Errorf("resource %q not found in state", resource)
		}
		if r.Primary.ID == "" {
			return fmt.Errorf("resource %q has empty primary ID in state", resource)
		}
		c := client.NewClient(client.GetConfigFromEnv())
		remoteRecord, err := c.FindBridge(r.Primary.Attributes["name"])
		if err != nil {
			return err
		}
		*record = *remoteRecord

		return nil
	}
}

func testAccBridgeDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_bridge" {
			continue
		}

		remoteRecord, err := c.FindBridge(rs.Primary.Attributes["name"])
		if err != nil && !client.IsNotFoundError(err) {
			return fmt.Errorf("expected not found error, got %+#v", err)
		}

		if remoteRecord != nil {
			return fmt.Errorf("bridge %q (%s) still exists in remote system", remoteRecord.Name, remoteRecord.Id)
		}
	}

	return nil
}

func testAccBridgeConfig(name string, fastForward, vlanFiltering bool, comment string) string {
	return fmt.Sprintf(`
		resource "mikrotik_bridge" "testacc" {
			name = %q
			fast_forward = %t
			vlan_filtering = %t
			comment = %q
		}
	`, name, fastForward, vlanFiltering, comment)
}


File: /mikrotik\resource_bridge_vlan.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type bridgeVlan struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &bridgeVlan{}
	_ resource.ResourceWithConfigure   = &bridgeVlan{}
	_ resource.ResourceWithImportState = &bridgeVlan{}
)

// NewBridgeVlanResource is a helper function to simplify the provider implementation.
func NewBridgeVlanResource() resource.Resource {
	return &bridgeVlan{}
}

func (r *bridgeVlan) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *bridgeVlan) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_bridge_vlan"
}

// Schema defines the schema for the resource.
func (s *bridgeVlan) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a MikroTik BridgeVlan.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "A unique ID for this resource.",
			},
			"bridge": schema.StringAttribute{
				Required:    true,
				Description: "The bridge interface which the respective VLAN entry is intended for.",
			},
			"tagged": schema.SetAttribute{
				Optional:    true,
				Computed:    true,
				ElementType: tftypes.StringType,
				Description: "Interface list with a VLAN tag adding action in egress.",
			},
			"untagged": schema.SetAttribute{
				Optional:    true,
				Computed:    true,
				ElementType: tftypes.StringType,
				Description: "Interface list with a VLAN tag removing action in egress. ",
			},
			"vlan_ids": schema.SetAttribute{
				Optional:    true,
				Computed:    true,
				ElementType: tftypes.Int64Type,
				Description: "The list of VLAN IDs for certain port configuration. Ranges are not supported yet.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *bridgeVlan) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel bridgeVlanModel
	var mikrotikModel client.BridgeVlan
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *bridgeVlan) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel bridgeVlanModel
	var mikrotikModel client.BridgeVlan
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *bridgeVlan) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel bridgeVlanModel
	var mikrotikModel client.BridgeVlan
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *bridgeVlan) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel bridgeVlanModel
	var mikrotikModel client.BridgeVlan
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *bridgeVlan) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	utils.ImportUppercaseWrapper(resource.ImportStatePassthroughID)(ctx,
		path.Root("id"),
		req,
		resp,
	)
}

type bridgeVlanModel struct {
	Id       tftypes.String `tfsdk:"id"`
	Bridge   tftypes.String `tfsdk:"bridge"`
	Tagged   tftypes.Set    `tfsdk:"tagged"`
	Untagged tftypes.Set    `tfsdk:"untagged"`
	VlanIds  tftypes.Set    `tfsdk:"vlan_ids"`
}


File: /mikrotik\resource_bridge_vlan_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestBridgeVlan_basic(t *testing.T) {

	resourceName := "mikrotik_bridge_vlan.testacc"

	createdBridgeVlan := client.BridgeVlan{}
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckBridgeVlanDestroy,
		Steps: []resource.TestStep{
			{
				Config: `
						resource "mikrotik_bridge" "default" {
							name = "test_bridge"
						}

						resource "mikrotik_bridge_vlan" "testacc" {
							bridge   = mikrotik_bridge.default.name
							vlan_ids = [10, 15, 18]
							untagged = ["*0"]
						}
				`,
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBridgeVlanExists(resourceName, &createdBridgeVlan),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "bridge", "test_bridge"),
					resource.TestCheckResourceAttr(resourceName, "untagged.#", "1"),
				),
			},
			{
				Config: `
				resource "mikrotik_bridge" "default" {
					name = "test_bridge"
					}

					resource "mikrotik_bridge_vlan" "testacc" {
						bridge   = mikrotik_bridge.default.name
						vlan_ids = [10, 15, 18]
						untagged = []
						}
						`,
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccBridgeVlanExists(resourceName, &createdBridgeVlan),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "bridge", "test_bridge"),
					resource.TestCheckResourceAttr(resourceName, "untagged.#", "0"),
				),
			},
		},
	})
}

func testAccBridgeVlanExists(resourceID string, record *client.BridgeVlan) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		r, ok := s.RootModule().Resources[resourceID]
		if !ok {
			return fmt.Errorf("resource %q not found in state", resourceID)
		}
		if r.Primary.ID == "" {
			return fmt.Errorf("resource %q has empty primary ID in state", resourceID)
		}
		c := client.NewClient(client.GetConfigFromEnv())
		remoteRecord, err := c.FindBridgeVlan(r.Primary.ID)
		if err != nil {
			return err
		}
		*record = *remoteRecord

		return nil
	}
}

func testAccCheckBridgeVlanDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_bridge_vlan" {
			continue
		}

		remoteRecord, err := c.FindBridgeVlan(rs.Primary.ID)
		if err != nil && !client.IsNotFoundError(err) {
			return fmt.Errorf("expected not found error, got %+#v", err)
		}

		if remoteRecord != nil {
			return fmt.Errorf("bridge vlan %q still exists in remote system", remoteRecord.Id)
		}
	}

	return nil
}


File: /mikrotik\resource_dhcp_lease.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/boolplanmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type dhcpLease struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &dhcpLease{}
	_ resource.ResourceWithConfigure   = &dhcpLease{}
	_ resource.ResourceWithImportState = &dhcpLease{}
)

// NewDhcpLeaseResource is a helper function to simplify the provider implementation.
func NewDhcpLeaseResource() resource.Resource {
	return &dhcpLease{}
}

func (r *dhcpLease) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *dhcpLease) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_dhcp_lease"
}

// Schema defines the schema for the resource.
func (s *dhcpLease) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a DHCP lease on the MikroTik device.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique resource identifier.",
			},
			"address": schema.StringAttribute{
				Required:    true,
				Description: "The IP address of the DHCP lease to be created.",
			},
			"macaddress": schema.StringAttribute{
				Required:    true,
				Description: "The MAC addreess of the DHCP lease to be created.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The comment of the DHCP lease to be created.",
			},
			"blocked": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "Whether to block access for this DHCP client (true|false).",
			},
			"dynamic": schema.BoolAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.Bool{
					boolplanmodifier.UseStateForUnknown(),
				},
				Description: "Whether the dhcp lease is static or dynamic. Dynamic leases are not guaranteed to continue to be assigned to that specific device. Defaults to false.",
			},
			"hostname": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "The hostname of the device",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *dhcpLease) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel dhcpLeaseModel
	var mikrotikModel client.DhcpLease
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *dhcpLease) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel dhcpLeaseModel
	var mikrotikModel client.DhcpLease
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *dhcpLease) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel dhcpLeaseModel
	var mikrotikModel client.DhcpLease
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *dhcpLease) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel dhcpLeaseModel
	var mikrotikModel client.DhcpLease
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *dhcpLease) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	utils.ImportUppercaseWrapper(resource.ImportStatePassthroughID)(ctx, path.Root("id"), req, resp)
}

type dhcpLeaseModel struct {
	Id          tftypes.String `tfsdk:"id"`
	Address     tftypes.String `tfsdk:"address"`
	MacAddress  tftypes.String `tfsdk:"macaddress"`
	Comment     tftypes.String `tfsdk:"comment"`
	BlockAccess tftypes.Bool   `tfsdk:"blocked"`
	Dynamic     tftypes.Bool   `tfsdk:"dynamic"`
	Hostname    tftypes.String `tfsdk:"hostname"`
}


File: /mikrotik\resource_dhcp_lease_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/acctest"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestAccMikrotikDhcpLease_create(t *testing.T) {
	ipAddr := internal.GetNewIpAddr()
	macAddr := internal.GetNewMacAddr()
	comment := acctest.RandomWithPrefix("tf-acc-comment")

	resourceName := "mikrotik_dhcp_lease.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikDhcpLeaseDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccDhcpLease(ipAddr, macAddr, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpLeaseExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "macaddress", macAddr),
					resource.TestCheckResourceAttr(resourceName, "dynamic", "false"),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
				),
			},
		},
	})
}

func TestAccMikrotikDhcpLease_updateLease(t *testing.T) {
	ipAddr := internal.GetNewIpAddr()
	updatedIpAddr := internal.GetNewIpAddr()
	macAddr := internal.GetNewMacAddr()
	updatedMacAddr := internal.GetNewMacAddr()
	comment := acctest.RandomWithPrefix("tf-acc-comment")
	updatedComment := acctest.RandomWithPrefix("tf-acc-comment")

	resourceName := "mikrotik_dhcp_lease.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikDhcpLeaseDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccDhcpLease(ipAddr, macAddr, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpLeaseExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "macaddress", macAddr),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
				),
			},
			{
				Config: testAccDhcpLease(updatedIpAddr, macAddr, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpLeaseExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", updatedIpAddr),
					resource.TestCheckResourceAttr(resourceName, "macaddress", macAddr),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
				),
			},
			{
				Config: testAccDhcpLease(ipAddr, macAddr, updatedComment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpLeaseExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "macaddress", macAddr),
					resource.TestCheckResourceAttr(resourceName, "comment", updatedComment),
				),
			},
			{
				Config: testAccDhcpLease(ipAddr, updatedMacAddr, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpLeaseExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "macaddress", updatedMacAddr),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
				),
			},
			{
				Config: testAccDhcpLeaseUpdatedBlockAccess(ipAddr, macAddr, comment, true),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpLeaseExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "macaddress", macAddr),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
					resource.TestCheckResourceAttr(resourceName, "blocked", "true"),
				),
			},
		},
	})
}

func TestAccMikrotikDhcpLease_import(t *testing.T) {
	ipAddr := internal.GetNewIpAddr()
	macAddr := internal.GetNewMacAddr()
	comment := acctest.RandomWithPrefix("tf-acc-comment")

	resourceName := "mikrotik_dhcp_lease.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikDhcpLeaseDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccDhcpLease(ipAddr, macAddr, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpLeaseExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id")),
			},
			{
				ResourceName:      resourceName,
				ImportState:       true,
				ImportStateVerify: true,
			},
		},
	})
}

func testAccDhcpLease(ipAddr, macAddr, comment string) string {
	return fmt.Sprintf(`
resource "mikrotik_dhcp_lease" "bar" {
    address = "%s"
    macaddress = "%s"
    comment = "%s"
}
`, ipAddr, macAddr, comment)
}

func testAccDhcpLeaseUpdatedBlockAccess(ipAddr, macAddr, comment string, blocked bool) string {
	return fmt.Sprintf(`
resource "mikrotik_dhcp_lease" "bar" {
    address = "%s"
    macaddress = "%s"
    blocked = "%t"
    comment = "%s"
}
`, ipAddr, macAddr, blocked, comment)
}

func testAccDhcpLeaseExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("mikrotik_dhcp_lease does not exist in the statefile")
		}

		c := client.NewClient(client.GetConfigFromEnv())

		dhcpLease, err := c.FindDhcpLease(rs.Primary.ID)

		if err != nil {
			return fmt.Errorf("Unable to get the dhcp lease with error: %v", err)
		}

		if dhcpLease == nil {
			return fmt.Errorf("Unable to get the dhcp lease")
		}

		if dhcpLease.Id == rs.Primary.ID {
			return nil
		}
		return nil
	}
}

func testAccCheckMikrotikDhcpLeaseDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_dhcp_lease" {
			continue
		}

		dhcpLease, err := c.FindDhcpLease(rs.Primary.ID)

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if dhcpLease != nil {
			return fmt.Errorf("dhcp lease (%s) still exists", dhcpLease.Id)
		}
	}
	return nil
}


File: /mikrotik\resource_dhcp_server.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type dhcpServer struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &dhcpServer{}
	_ resource.ResourceWithConfigure   = &dhcpServer{}
	_ resource.ResourceWithImportState = &dhcpServer{}
)

// NewDhcpServerResource is a helper function to simplify the provider implementation.
func NewDhcpServerResource() resource.Resource {
	return &dhcpServer{}
}

func (r *dhcpServer) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *dhcpServer) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_dhcp_server"
}

// Schema defines the schema for the resource.
func (s *dhcpServer) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Manages a DHCP server resource within MikroTik device.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique ID of this resource.",
			},
			"name": schema.StringAttribute{
				Required: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.RequiresReplace(),
				},
				Description: "Reference name.",
			},
			"disabled": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(true),
				Description: "Disable this DHCP server instance.",
			},
			"add_arp": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Whether to add dynamic ARP entry. If set to no either ARP mode should be enabled on that interface or static ARP entries should be administratively defined.",
			},
			"address_pool": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("static-only"),
				Description: "IP pool, from which to take IP addresses for the clients. If set to static-only, then only the clients that have a static lease (added in lease submenu) will be allowed.",
			},
			"authoritative": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("yes"),
				Description: "Option changes the way how server responds to DHCP requests.",
			},
			"interface": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("*0"),
				Description: "Interface on which server will be running.",
			},
			"lease_script": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Script that will be executed after lease is assigned or de-assigned. Internal \"global\" variables that can be used in the script.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *dhcpServer) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel dhcpServerModel
	var mikrotikModel client.DhcpServer
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *dhcpServer) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel dhcpServerModel
	var mikrotikModel client.DhcpServer
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *dhcpServer) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel dhcpServerModel
	var mikrotikModel client.DhcpServer
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *dhcpServer) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel dhcpServerModel
	var mikrotikModel client.DhcpServer
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *dhcpServer) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("name"), req, resp)
}

type dhcpServerModel struct {
	Id            tftypes.String `tfsdk:"id"`
	Name          tftypes.String `tfsdk:"name"`
	Disabled      tftypes.Bool   `tfsdk:"disabled"`
	AddArp        tftypes.Bool   `tfsdk:"add_arp"`
	AddressPool   tftypes.String `tfsdk:"address_pool"`
	Authoritative tftypes.String `tfsdk:"authoritative"`
	Interface     tftypes.String `tfsdk:"interface"`
	LeaseScript   tftypes.String `tfsdk:"lease_script"`
}


File: /mikrotik\resource_dhcp_server_network.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type dhcpServerNetwork struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &dhcpServerNetwork{}
	_ resource.ResourceWithConfigure   = &dhcpServerNetwork{}
	_ resource.ResourceWithImportState = &dhcpServerNetwork{}
)

// NewDhcpServerNetworkResource is a helper function to simplify the provider implementation.
func NewDhcpServerNetworkResource() resource.Resource {
	return &dhcpServerNetwork{}
}

func (r *dhcpServerNetwork) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *dhcpServerNetwork) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_dhcp_server_network"
}

// Schema defines the schema for the resource.
func (s *dhcpServerNetwork) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Manages a DHCP network resource within Mikrotik device.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique ID of this resource.",
			},
			"comment": schema.StringAttribute{
				Optional: true,
				Computed: true,
			},
			"address": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The network DHCP server(s) will lease addresses from.",
			},
			"netmask": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The actual network mask to be used by DHCP client. If set to '0' - netmask from network address will be used.",
			},
			"gateway": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("0.0.0.0"),
				Description: "The default gateway to be used by DHCP Client.",
			},
			"dns_server": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The DHCP client will use these as the default DNS servers.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *dhcpServerNetwork) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel dhcpServerNetworkModel
	var mikrotikModel client.DhcpServerNetwork
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *dhcpServerNetwork) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel dhcpServerNetworkModel
	var mikrotikModel client.DhcpServerNetwork
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *dhcpServerNetwork) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel dhcpServerNetworkModel
	var mikrotikModel client.DhcpServerNetwork
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *dhcpServerNetwork) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel dhcpServerNetworkModel
	var mikrotikModel client.DhcpServerNetwork
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *dhcpServerNetwork) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	utils.ImportUppercaseWrapper(resource.ImportStatePassthroughID)(ctx, path.Root("id"), req, resp)
}

type dhcpServerNetworkModel struct {
	Id        tftypes.String `tfsdk:"id"`
	Comment   tftypes.String `tfsdk:"comment"`
	Address   tftypes.String `tfsdk:"address"`
	Netmask   tftypes.String `tfsdk:"netmask"`
	Gateway   tftypes.String `tfsdk:"gateway"`
	DnsServer tftypes.String `tfsdk:"dns_server"`
}


File: /mikrotik\resource_dhcp_server_network_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestDhcpServerNetwork_basic(t *testing.T) {
	resourceName := "mikrotik_dhcp_server_network.testacc"
	netmask := "24"
	address := "10.10.10.0/" + netmask
	gateway := "10.10.10.2"
	dnsServer := "10.10.10.3"
	comment := "Terraform managed"
	dnsServerUpdated := "192.168.5.3"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckDhcpServerNetworkDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccDhcpServerNetwork(address, netmask, gateway, dnsServer, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpServerNetworkExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", address),
					resource.TestCheckResourceAttr(resourceName, "netmask", netmask),
					resource.TestCheckResourceAttr(resourceName, "gateway", gateway),
					resource.TestCheckResourceAttr(resourceName, "dns_server", dnsServer),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
				),
			},
			{
				Config: testAccDhcpServerNetwork(address, netmask, gateway, dnsServerUpdated, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpServerNetworkExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", address),
					resource.TestCheckResourceAttr(resourceName, "netmask", netmask),
					resource.TestCheckResourceAttr(resourceName, "gateway", gateway),
					resource.TestCheckResourceAttr(resourceName, "dns_server", dnsServerUpdated),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
				),
			},
		},
	})
}

func TestDhcpServerNetwork_incompleteFieldsSet(t *testing.T) {
	resourceName := "mikrotik_dhcp_server_network.testacc"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckDhcpServerNetworkDestroy,
		Steps: []resource.TestStep{
			{
				Config: `
					resource mikrotik_dhcp_server_network "testacc" {
						address    = "10.10.10.0/24"
					}
				`,
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpServerNetworkExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", "10.10.10.0/24"),
				),
			},
			{
				Config: `
					resource mikrotik_dhcp_server_network "testacc" {
						address    = "10.10.10.0/24"
						netmask    = "24"
					}
				`,
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpServerNetworkExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", "10.10.10.0/24"),
					resource.TestCheckResourceAttr(resourceName, "netmask", "24"),
				),
			},
			{
				Config: `
					resource mikrotik_dhcp_server_network "testacc" {
						address    = "10.10.10.0/24"
					}
				`,
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpServerNetworkExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", "10.10.10.0/24"),
					resource.TestCheckResourceAttr(resourceName, "netmask", "24"),
				),
			},
		},
	})
}

func testAccDhcpServerNetwork(address, netmask, gateway, dns_server, comment string) string {
	return fmt.Sprintf(`
resource mikrotik_dhcp_server_network "testacc" {
	address    = %q
	netmask    = %q
	gateway    = %q
	dns_server = %q
	comment    = %q
}
`, address, netmask, gateway, dns_server, comment)
}

func testAccCheckDhcpServerNetworkDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_dhcp_server_network" {
			continue
		}

		remoteRecord, err := c.FindDhcpServerNetwork(rs.Primary.ID)

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if remoteRecord != nil {
			return fmt.Errorf("remote recrod (%s) still exists", remoteRecord.Id)
		}

	}
	return nil
}

func testAccDhcpServerNetworkExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("%s does not exist in the statefile", resourceName)
		}

		c := client.NewClient(client.GetConfigFromEnv())
		record, err := c.FindDhcpServerNetwork(rs.Primary.ID)
		if err != nil {
			return fmt.Errorf("Unable to get remote record for %s: %v", resourceName, err)
		}

		if record == nil {
			return fmt.Errorf("Unable to get the remote record %s", resourceName)
		}

		return nil
	}
}


File: /mikrotik\resource_dhcp_server_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestAccDhcpServer_basic(t *testing.T) {
	rName := "dhcp-server"
	rLeaseScript := ":put 123"
	dhcpServer := client.DhcpServer{}
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckDhcpServerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccDhcpServerConfig(rName, true, rLeaseScript),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpServerResourceExists("mikrotik_dhcp_server.testacc", &dhcpServer),
					resource.TestCheckResourceAttr("mikrotik_dhcp_server.testacc", "name", rName),
					resource.TestCheckResourceAttr("mikrotik_dhcp_server.testacc", "disabled", "true"),
					resource.TestCheckResourceAttr("mikrotik_dhcp_server.testacc", "lease_script", rLeaseScript),
				),
			},
			{
				Config: testAccDhcpServerConfig(rName, false, ":put updated"),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDhcpServerResourceExists("mikrotik_dhcp_server.testacc", &dhcpServer),
					resource.TestCheckResourceAttr("mikrotik_dhcp_server.testacc", "name", rName),
					resource.TestCheckResourceAttr("mikrotik_dhcp_server.testacc", "disabled", "false"),
					resource.TestCheckResourceAttr("mikrotik_dhcp_server.testacc", "lease_script", ":put updated"),
				),
			},
		},
	})
}

func testAccDhcpServerResourceExists(resource string, record *client.DhcpServer) resource.TestCheckFunc {
	return func(s *terraform.State) error {

		r, ok := s.RootModule().Resources[resource]
		if !ok {
			return fmt.Errorf("resource %q not found in state", resource)
		}
		if r.Primary.ID == "" {
			return fmt.Errorf("resource %q has empty primary ID in state", resource)
		}
		c := client.NewClient(client.GetConfigFromEnv())
		dhcpServer, err := c.FindDhcpServer(r.Primary.Attributes["name"])
		if err != nil {
			return err
		}
		*record = *dhcpServer

		return nil
	}
}

func testAccCheckDhcpServerDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_dhcp_server" {
			continue
		}

		dhcpServer, err := c.FindDhcpServer(rs.Primary.Attributes["name"])
		if err != nil && !client.IsNotFoundError(err) {
			return fmt.Errorf("expected not found error, got %+#v", err)
		}

		if dhcpServer != nil {
			return fmt.Errorf("dhcp-server %q (%s) still exists in remote system", dhcpServer.Name, dhcpServer.Name)
		}
	}

	return nil
}

func testAccDhcpServerConfig(name string, disabled bool, leaseScript string) string {
	return fmt.Sprintf(`
		resource "mikrotik_dhcp_server" "testacc" {
			name = %q
			disabled = %t
			lease_script = %q
		}
	`, name, disabled, leaseScript)
}


File: /mikrotik\resource_dns_record.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework-validators/resourcevalidator"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type dnsRecord struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                     = &dnsRecord{}
	_ resource.ResourceWithConfigure        = &dnsRecord{}
	_ resource.ResourceWithConfigValidators = &dnsRecord{}
	_ resource.ResourceWithImportState      = &dnsRecord{}
)

// NewDnsRecordResource is a helper function to simplify the provider implementation.
func NewDnsRecordResource() resource.Resource {
	return &dnsRecord{}
}

func (r *dnsRecord) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *dnsRecord) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_dns_record"
}

// Schema defines the schema for the resource.
func (s *dnsRecord) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a DNS record on the MikroTik device.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique ID of this resource.",
			},
			"name": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The name of the DNS hostname to be created.",
			},
			"regexp": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Regular expression against which domain names should be verified.",
			},
			"ttl": schema.Int64Attribute{
				Optional:    true,
				Computed:    true,
				Description: "The ttl of the DNS record.",
			},
			"address": schema.StringAttribute{
				Required:    true,
				Description: "The A record to be returend from the DNS hostname.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The comment text associated with the DNS record.",
			},
		},
	}
}

func (r *dnsRecord) ConfigValidators(context.Context) []resource.ConfigValidator {
	return []resource.ConfigValidator{
		resourcevalidator.ExactlyOneOf(
			path.MatchRoot("name"),
			path.MatchRoot("regexp"),
		),
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *dnsRecord) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel dnsRecordModel
	var mikrotikModel client.DnsRecord
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *dnsRecord) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel dnsRecordModel
	var mikrotikModel client.DnsRecord
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *dnsRecord) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel dnsRecordModel
	var mikrotikModel client.DnsRecord
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *dnsRecord) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel dnsRecordModel
	var mikrotikModel client.DnsRecord
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *dnsRecord) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("id"), req, resp)
}

type dnsRecordModel struct {
	Id      tftypes.String `tfsdk:"id"`
	Name    tftypes.String `tfsdk:"name"`
	Regexp  tftypes.String `tfsdk:"regexp"`
	Ttl     tftypes.Int64  `tfsdk:"ttl"`
	Address tftypes.String `tfsdk:"address"`
	Comment tftypes.String `tfsdk:"comment"`
}


File: /mikrotik\resource_dns_record_test.go
package mikrotik

import (
	"fmt"
	"regexp"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestAccMikrotikDnsRecord_create(t *testing.T) {
	dnsName := internal.GetNewDnsName()
	ipAddr := internal.GetNewIpAddr()

	resourceName := "mikrotik_dns_record.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikDnsRecordDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccDnsRecord(dnsName, ipAddr),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDnsRecordExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id")),
			},
			{
				Config: `
					resource "mikrotik_dns_record" "bar" {
						address = "10.10.200.100"
						regexp  = ".+\\.domain\\.com"
						ttl     = "300"
					}
				`,
				ExpectError: regexp.MustCompile("only name or regexp allowed"),
			},
		},
	})
}

func TestAccMikrotikDnsRecord_createRegexp(t *testing.T) {
	resourceName := "mikrotik_dns_record.bar"
	resource.ParallelTest(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikDnsRecordDestroy,
		Steps: []resource.TestStep{
			{
				Config: `
					resource "mikrotik_dns_record" "bar" {
						address = "10.10.200.100"
						regexp  = ".+\\.domain\\.com"
						ttl     = "300"
					}
				`,
				Check: resource.ComposeAggregateTestCheckFunc(
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr("mikrotik_dns_record.bar", "regexp", ".+\\.domain\\.com"),
				),
			},
		},
	})
}

func TestAccMikrotikDnsRecord_createAndPlanWithNonExistantRecord(t *testing.T) {
	dnsName := internal.GetNewDnsName()
	ipAddr := internal.GetNewIpAddr()

	resourceName := "mikrotik_dns_record.bar"
	removeDnsRecord := func() {
		c := client.NewClient(client.GetConfigFromEnv())
		dns, err := c.FindDnsRecord(dnsName)

		if err != nil {
			t.Fatalf("Error finding the DNS record: %s", err)
		}
		err = c.DeleteDnsRecord(dns.Id)
		if err != nil {
			t.Fatalf("Error removing the DNS record: %s", err)
		}

	}
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikDnsRecordDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccDnsRecord(dnsName, ipAddr),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDnsRecordExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id")),
			},
			{
				PreConfig:          removeDnsRecord,
				Config:             testAccDnsRecord(dnsName, ipAddr),
				ExpectNonEmptyPlan: false,
			},
		},
	})
}

func TestAccMikrotikDnsRecord_updateAddress(t *testing.T) {
	dnsName := internal.GetNewDnsName()
	ipAddr := internal.GetNewIpAddr()
	updatedIpAddr := internal.GetNewIpAddr()

	resourceName := "mikrotik_dns_record.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikDnsRecordDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccDnsRecord(dnsName, ipAddr),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDnsRecordExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
				),
			},
			{
				Config: testAccDnsRecord(dnsName, updatedIpAddr),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDnsRecordExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", updatedIpAddr)),
			},
		},
	})
}

func TestAccMikrotikDnsRecord_updateComment(t *testing.T) {
	dnsName := internal.GetNewDnsName()
	ipAddr := internal.GetNewIpAddr()
	comment := "Initial comment"
	updatedComment := "new comment"

	resourceName := "mikrotik_dns_record.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikDnsRecordDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccDnsRecordWithComment(dnsName, ipAddr, comment),

				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDnsRecordExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
				),
			},
			{
				Config: testAccDnsRecordWithComment(dnsName, ipAddr, updatedComment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDnsRecordExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "comment", updatedComment)),
			},
		},
	})
}

func TestAccMikrotikDnsRecord_import(t *testing.T) {
	dnsName := internal.GetNewDnsName()
	ipAddr := internal.GetNewIpAddr()

	resourceName := "mikrotik_dns_record.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikDnsRecordDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccDnsRecord(dnsName, ipAddr),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccDnsRecordExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id")),
			},
			{
				ImportState:       true,
				ResourceName:      resourceName,
				ImportStateVerify: true,
			},
		},
	})
}

func testAccDnsRecord(dnsName, ipAddr string) string {
	return fmt.Sprintf(`
resource "mikrotik_dns_record" "bar" {
    name = "%s"
    address = "%s"
    ttl = "300"
}
`, dnsName, ipAddr)
}

func testAccDnsRecordWithComment(dnsName, ipAddr, comment string) string {
	return fmt.Sprintf(`
resource "mikrotik_dns_record" "bar" {
    name = "%s"
    address = "%s"
    ttl = "300"
    comment = "%s"
}
`, dnsName, ipAddr, comment)
}

func testAccDnsRecordExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("mikrotik_dns_record does not exist in the statefile")
		}

		c := client.NewClient(client.GetConfigFromEnv())

		dnsRecord, err := c.FindDnsRecord(rs.Primary.Attributes["name"])

		if err != nil {
			return fmt.Errorf("Unable to get the dns record with error: %v", err)
		}

		if dnsRecord == nil {
			return fmt.Errorf("Unable to get the dns record with name: %s", rs.Primary.Attributes["name"])
		}

		if dnsRecord.Name == rs.Primary.Attributes["name"] {
			return nil
		}

		return nil
	}
}

func testAccCheckMikrotikDnsRecordDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_dns_record" {
			continue
		}

		dnsRecord, err := c.FindDnsRecord(rs.Primary.Attributes["name"])

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if dnsRecord != nil {
			return fmt.Errorf("dns recrod (%s) still exists", dnsRecord.Id)
		}
	}
	return nil
}


File: /mikrotik\resource_firewall_filter.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type firewallFilterRule struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &firewallFilterRule{}
	_ resource.ResourceWithConfigure   = &firewallFilterRule{}
	_ resource.ResourceWithImportState = &firewallFilterRule{}
)

// NewFirewallFilterRuleResource is a helper function to simplify the provider implementation.
func NewFirewallFilterRuleResource() resource.Resource {
	return &firewallFilterRule{}
}

func (r *firewallFilterRule) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *firewallFilterRule) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_firewall_filter_rule"
}

// Schema defines the schema for the resource.
func (s *firewallFilterRule) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a MikroTik FirewallFilterRule.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique ID of this resource.",
			},
			"action": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("accept"),
				Description: "Action to take if packet is matched by the rule.",
			},
			"chain": schema.StringAttribute{
				Required:    true,
				Description: "Specifies to which chain rule will be added. If the input does not match the name of an already defined chain, a new chain will be created.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Comment to the rule.",
			},
			"connection_state": schema.SetAttribute{
				Optional:    true,
				Computed:    true,
				ElementType: tftypes.StringType,
				Description: "Interprets the connection tracking analysis data for a particular packet.",
			},
			"dst_port": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "List of destination port numbers or port number ranges.",
			},
			"in_interface": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Interface the packet has entered the router.",
			},
			"in_interface_list": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Set of interfaces defined in interface list. Works the same as in-interface.",
			},
			"out_interface_list": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Set of interfaces defined in interface list. Works the same as out-interface.",
			},
			"protocol": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("tcp"),
				Description: "Matches particular IP protocol specified by protocol name or number.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *firewallFilterRule) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel firewallFilterRuleModel
	var mikrotikModel client.FirewallFilterRule
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *firewallFilterRule) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel firewallFilterRuleModel
	var mikrotikModel client.FirewallFilterRule
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *firewallFilterRule) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel firewallFilterRuleModel
	var mikrotikModel client.FirewallFilterRule
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *firewallFilterRule) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel firewallFilterRuleModel
	var mikrotikModel client.FirewallFilterRule
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *firewallFilterRule) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	utils.ImportUppercaseWrapper(resource.ImportStatePassthroughID)(ctx, path.Root("id"), req, resp)
}

type firewallFilterRuleModel struct {
	Id               tftypes.String `tfsdk:"id"`
	Action           tftypes.String `tfsdk:"action"`
	Chain            tftypes.String `tfsdk:"chain"`
	Comment          tftypes.String `tfsdk:"comment"`
	ConnectionState  tftypes.Set    `tfsdk:"connection_state"`
	DestPort         tftypes.String `tfsdk:"dst_port"`
	InInterface      tftypes.String `tfsdk:"in_interface"`
	InInterfaceList  tftypes.String `tfsdk:"in_interface_list"`
	OutInterfaceList tftypes.String `tfsdk:"out_interface_list"`
	Protocol         tftypes.String `tfsdk:"protocol"`
}


File: /mikrotik\resource_firewall_filter_rule_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

var terraformResourceTypeFirewallFilterRule string = "mikrotik_firewall_filter_rule"

func TestFirewallFilterRule_basic(t *testing.T) {

	resourceName := terraformResourceTypeFirewallFilterRule + ".testacc"

	action := "accept"
	chain := "testChain"
	connectionState := []string{"new"}
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckFirewallFilterRuleDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccFirewallFilterRuleConfigBasic(action, chain, connectionState, "80", "tcp"),
				Check: resource.ComposeAggregateTestCheckFunc(
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "action", action),
					resource.TestCheckResourceAttr(resourceName, "chain", chain),
					resource.TestCheckResourceAttr(resourceName, "dst_port", "80"),
					resource.TestCheckResourceAttr(resourceName, "protocol", "tcp"),
				),
			},
			{
				Config: testAccFirewallFilterRuleConfigBasic(action, chain, connectionState, "68", "udp"),
				Check: resource.ComposeAggregateTestCheckFunc(
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "action", action),
					resource.TestCheckResourceAttr(resourceName, "chain", chain),
					resource.TestCheckResourceAttr(resourceName, "dst_port", "68"),
					resource.TestCheckResourceAttr(resourceName, "protocol", "udp"),
				),
			},
		},
	})
}

func testAccCheckFirewallFilterRuleDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != terraformResourceTypeFirewallFilterRule {
			continue
		}

		remoteRecord, err := c.FindFirewallFilterRule(rs.Primary.ID)
		if err != nil && !client.IsNotFoundError(err) {
			return fmt.Errorf("expected not found error, got %+#v", err)
		}

		if remoteRecord != nil {
			return fmt.Errorf("resource %T with id %q still exists in remote system", remoteRecord, remoteRecord.Id)
		}
	}
	return nil
}

func testAccFirewallFilterRuleConfigBasic(action, chain string, connectionState []string, destPort, protocol string) string {
	return fmt.Sprintf(`
		resource "mikrotik_firewall_filter_rule" "testacc" {
			action             = %q
			chain              = %q
			connection_state   = [%s]
			dst_port           = %q
			protocol           = %q
		}
	`, action, chain, internal.JoinStringsToString(connectionState, ","), destPort, protocol)
}


File: /mikrotik\resource_generic_crud_operations.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-framework/resource"
)

type (
	CreateFunc func(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse)
	ReadFunc   func(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse)
	UpdateFunc func(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse)
	DeleteFunc func(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse)
)

// GenericCreateResource creates the resource and sets the initial Terraform state.
//
// terraformModel and mikrotikModel must be passed as pointers
func GenericCreateResource(terraformModel interface{}, mikrotikModel client.Resource, client *client.Mikrotik) CreateFunc {
	return func(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {

		diags := req.Plan.Get(ctx, terraformModel)
		resp.Diagnostics.Append(diags...)
		if resp.Diagnostics.HasError() {
			return
		}
		if err := utils.TerraformModelToMikrotikStruct(ctx, terraformModel, mikrotikModel); err != nil {
			resp.Diagnostics.AddError("Cannot copy model: Terraform -> MikroTik", err.Error())
			return
		}

		created, err := client.Add(mikrotikModel)
		if err != nil {
			resp.Diagnostics.AddError("Creation failed", err.Error())
			return
		}

		if err := utils.MikrotikStructToTerraformModel(ctx, created, terraformModel); err != nil {
			resp.Diagnostics.AddError("Cannot copy model: MikroTik -> Terraform", err.Error())
			return
		}

		resp.Diagnostics.Append(resp.State.Set(ctx, terraformModel)...)
		if resp.Diagnostics.HasError() {
			return
		}
	}
}

// GenericReadResource refreshes the Terraform state with the latest data.
func GenericReadResource(terraformModel interface{}, mikrotikModel client.Resource, mikrotikClient *client.Mikrotik) ReadFunc {
	return func(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
		resp.Diagnostics.Append(req.State.Get(ctx, terraformModel)...)
		if resp.Diagnostics.HasError() {
			return
		}
		if err := utils.TerraformModelToMikrotikStruct(ctx, terraformModel, mikrotikModel); err != nil {
			resp.Diagnostics.AddError("Cannot copy model: Terraform -> MikroTik", err.Error())
			return
		}

		resource, err := mikrotikClient.Find(mikrotikModel)
		if client.IsNotFoundError(err) {
			resp.State.RemoveResource(ctx)
			return
		}
		if err != nil {
			resp.Diagnostics.AddError(
				"Error reading remote resource",
				err.Error(),
			)
			return
		}
		if err := utils.MikrotikStructToTerraformModel(ctx, resource, terraformModel); err != nil {
			resp.Diagnostics.AddError("Cannot copy model: MikroTik -> Terraform", err.Error())
			return
		}

		resp.Diagnostics.Append(resp.State.Set(ctx, terraformModel)...)
		if resp.Diagnostics.HasError() {
			return
		}
	}
}

// GenericUpdateResource updates the resource and sets the updated Terraform state on success.
func GenericUpdateResource(terraformModel interface{}, mikrotikModel client.Resource, client *client.Mikrotik) UpdateFunc {
	return func(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
		resp.Diagnostics.Append(req.Plan.Get(ctx, terraformModel)...)
		if resp.Diagnostics.HasError() {
			return
		}
		if err := utils.TerraformModelToMikrotikStruct(ctx, terraformModel, mikrotikModel); err != nil {
			resp.Diagnostics.AddError("Cannot copy model: Terraform -> MikroTik", err.Error())
			return
		}
		updated, err := client.Update(mikrotikModel)
		if err != nil {
			resp.Diagnostics.AddError("Update failed", err.Error())
			return
		}
		if err := utils.MikrotikStructToTerraformModel(ctx, updated, terraformModel); err != nil {
			resp.Diagnostics.AddError("Cannot copy model: MikroTik -> Terraform", err.Error())
			return
		}

		resp.Diagnostics.Append(resp.State.Set(ctx, terraformModel)...)
	}
}

// GenericDeleteResource deletes the resource and removes the Terraform state on success.
func GenericDeleteResource(terraformModel interface{}, mikrotikModel client.Resource, client *client.Mikrotik) DeleteFunc {
	return func(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
		resp.Diagnostics.Append(req.State.Get(ctx, terraformModel)...)
		if resp.Diagnostics.HasError() {
			return
		}

		if err := utils.TerraformModelToMikrotikStruct(ctx, terraformModel, mikrotikModel); err != nil {
			resp.Diagnostics.AddError("Cannot copy model: Terraform -> MikroTik", err.Error())
			return
		}

		if err := client.Delete(mikrotikModel); err != nil {
			resp.Diagnostics.AddError("Could not delete MikroTik resource", err.Error())
			return
		}
	}
}


File: /mikrotik\resource_interface_list.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type interfaceList struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &interfaceList{}
	_ resource.ResourceWithConfigure   = &interfaceList{}
	_ resource.ResourceWithImportState = &interfaceList{}
)

// NewInterfaceListResource is a helper function to simplify the provider implementation.
func NewInterfaceListResource() resource.Resource {
	return &interfaceList{}
}

func (r *interfaceList) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *interfaceList) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_interface_list"
}

// Schema defines the schema for the resource.
func (s *interfaceList) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Allows to define set of interfaces for easier interface management.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique ID of this resource.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Comment to this list.",
			},
			"name": schema.StringAttribute{
				Required:    true,
				Description: "Name of the interface list.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *interfaceList) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel interfaceListModel
	var mikrotikModel client.InterfaceList
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *interfaceList) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel interfaceListModel
	var mikrotikModel client.InterfaceList
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *interfaceList) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel interfaceListModel
	var mikrotikModel client.InterfaceList
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *interfaceList) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel interfaceListModel
	var mikrotikModel client.InterfaceList
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *interfaceList) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("name"), req, resp)
}

type interfaceListModel struct {
	Id      tftypes.String `tfsdk:"id"`
	Comment tftypes.String `tfsdk:"comment"`
	Name    tftypes.String `tfsdk:"name"`
}


File: /mikrotik\resource_interface_list_member.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type interfaceListMember struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &interfaceListMember{}
	_ resource.ResourceWithConfigure   = &interfaceListMember{}
	_ resource.ResourceWithImportState = &interfaceListMember{}
)

// NewInterfaceListMemberResource is a helper function to simplify the provider implementation.
func NewInterfaceListMemberResource() resource.Resource {
	return &interfaceListMember{}
}

func (r *interfaceListMember) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *interfaceListMember) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_interface_list_member"
}

// Schema defines the schema for the resource.
func (s *interfaceListMember) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Allows to define set of interfaces for easier interface management.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique ID of this resource.",
			},
			"interface": schema.StringAttribute{
				Required:    true,
				Description: "Name of the interface.",
			},
			"list": schema.StringAttribute{
				Required:    true,
				Description: " 	Name of the interface list",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *interfaceListMember) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel interfaceListMemberModel
	var mikrotikModel client.InterfaceListMember
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *interfaceListMember) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel interfaceListMemberModel
	var mikrotikModel client.InterfaceListMember
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *interfaceListMember) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel interfaceListMemberModel
	var mikrotikModel client.InterfaceListMember
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *interfaceListMember) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel interfaceListMemberModel
	var mikrotikModel client.InterfaceListMember
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *interfaceListMember) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	utils.ImportUppercaseWrapper(resource.ImportStatePassthroughID)(ctx, path.Root("id"), req, resp)
}

type interfaceListMemberModel struct {
	Id        tftypes.String `tfsdk:"id"`
	Interface tftypes.String `tfsdk:"interface"`
	List      tftypes.String `tfsdk:"list"`
}


File: /mikrotik\resource_interface_list_member_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestInterfaceListMember_basic(t *testing.T) {
	resourceName := "mikrotik_interface_list_member.list_member"

	listName1 := "interface_list1"
	listName2 := "interface_list2"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckInterfaceListMemberDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccInterfaceListMember(listName1, listName2, "list1", "*0"),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceListMemberExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "list", listName1),
					resource.TestCheckResourceAttr(resourceName, "interface", "*0"),
				),
			},
			{
				Config: testAccInterfaceListMember(listName1, listName2, "list2", "*0"),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceListMemberExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "list", listName2),
					resource.TestCheckResourceAttr(resourceName, "interface", "*0"),
				),
			},
		},
	})
}

func testAccInterfaceListMemberExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("%s does not exist in the statefile", resourceName)
		}

		c := client.NewClient(client.GetConfigFromEnv())
		record, err := c.FindInterfaceListMember(rs.Primary.ID)
		if err != nil {
			return fmt.Errorf("Unable to get remote record for %s: %v", resourceName, err)
		}

		if record == nil {
			return fmt.Errorf("Unable to get the remote record %s", resourceName)
		}

		return nil
	}
}

func testAccCheckInterfaceListMemberDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_interface_list_member" {
			continue
		}

		remoteRecord, err := c.FindInterfaceListMember(rs.Primary.ID)
		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if remoteRecord != nil {
			return fmt.Errorf("remote record (%s) still exists", remoteRecord.Id)
		}
	}

	return nil
}

func testAccInterfaceListMember(listName1, listName2, listToUse string, iface string) string {
	return fmt.Sprintf(`
		resource mikrotik_interface_list "list1" {
			name = %q
		}

		resource mikrotik_interface_list "list2" {
			name = %q
		}

		resource mikrotik_interface_list_member "list_member" {
			interface = %q
			list      = mikrotik_interface_list.%s.name
		}
	`, listName1, listName2, iface, listToUse)
}


File: /mikrotik\resource_interface_list_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestInterfaceList_basic(t *testing.T) {
	resourceName := "mikrotik_interface_list.testacc"
	listName := "custom_list"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckInterfaceListDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccInterfaceList(listName, "Initial record"),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceListExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", listName),
				),
			},
			{
				Config: testAccInterfaceList(listName+"_updated", "updated record"),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceListExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", listName+"_updated"),
					resource.TestCheckResourceAttr(resourceName, "comment", "updated record"),
				),
			},
		},
	})
}

func testAccCheckInterfaceListDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_interface_list" {
			continue
		}

		remoteRecord, err := c.FindInterfaceList(rs.Primary.Attributes["name"])
		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if remoteRecord != nil {
			return fmt.Errorf("remote record (%s) still exists", remoteRecord.Name)
		}
	}

	return nil
}

func testAccInterfaceListExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("%s does not exist in the statefile", resourceName)
		}

		c := client.NewClient(client.GetConfigFromEnv())
		record, err := c.FindInterfaceList(rs.Primary.Attributes["name"])
		if err != nil {
			return fmt.Errorf("Unable to get remote record for %s: %v", resourceName, err)
		}

		if record == nil {
			return fmt.Errorf("Unable to get the remote record %s", resourceName)
		}

		return nil
	}
}

func testAccInterfaceList(name, comment string) string {
	return fmt.Sprintf(`
		resource "mikrotik_interface_list" "testacc" {
			name    = %q
			comment = %q
		}
`, name, comment)
}


File: /mikrotik\resource_interface_wireguard.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework-validators/int64validator"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/int64default"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"
	"github.com/hashicorp/terraform-plugin-framework/schema/validator"
	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type interfaceWireguard struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &interfaceWireguard{}
	_ resource.ResourceWithConfigure   = &interfaceWireguard{}
	_ resource.ResourceWithImportState = &interfaceWireguard{}
)

// NewInterfaceWireguardResource is a helper function to simplify the provider implementation.
func NewInterfaceWireguardResource() resource.Resource {
	return &interfaceWireguard{}

}

func (i *interfaceWireguard) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	i.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (i *interfaceWireguard) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_interface_wireguard"
}

// Schema defines the schema for the resource.
func (i *interfaceWireguard) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a Mikrotik interface wireguard only supported by RouterOS v7+.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Identifier of this resource assigned by RouterOS",
			},
			"name": schema.StringAttribute{
				Required:    true,
				Description: "Name of the interface wireguard.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "Comment associated with interface wireguard.",
			},
			"disabled": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "Boolean for whether or not the interface wireguard is disabled.",
			},
			"listen_port": schema.Int64Attribute{
				Optional:    true,
				Computed:    true,
				Default:     int64default.StaticInt64(13231),
				Description: "Port for WireGuard service to listen on for incoming sessions.",
			},
			"mtu": schema.Int64Attribute{
				Optional: true,
				Computed: true,
				Default:  int64default.StaticInt64(1420),
				Validators: []validator.Int64{
					int64validator.Between(0, 65536),
				},
				Description: "Layer3 Maximum transmission unit.",
			},
			"private_key": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Sensitive:   true,
				Description: "A base64 private key. If not specified, it will be automatically generated upon interface creation.",
			},
			"public_key": schema.StringAttribute{
				Optional:    false,
				Computed:    true,
				Description: "A base64 public key is calculated from the private key.",
			},
			"running": schema.BoolAttribute{
				Optional:    false,
				Computed:    true,
				Description: "Whether the interface is running.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (i *interfaceWireguard) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel interfaceWireguardModel
	var mikrotikModel client.InterfaceWireguard
	GenericCreateResource(&terraformModel, &mikrotikModel, i.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (i *interfaceWireguard) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel interfaceWireguardModel
	var mikrotikModel client.InterfaceWireguard
	GenericReadResource(&terraformModel, &mikrotikModel, i.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (i *interfaceWireguard) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel interfaceWireguardModel
	var mikrotikModel client.InterfaceWireguard
	GenericUpdateResource(&terraformModel, &mikrotikModel, i.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (i *interfaceWireguard) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel interfaceWireguardModel
	var mikrotikModel client.InterfaceWireguard
	GenericDeleteResource(&terraformModel, &mikrotikModel, i.client)(ctx, req, resp)
}

func (i *interfaceWireguard) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("name"), req, resp)
}

type interfaceWireguardModel struct {
	Id         tftypes.String `tfsdk:"id"`
	Name       tftypes.String `tfsdk:"name"`
	Comment    tftypes.String `tfsdk:"comment"`
	Disabled   tftypes.Bool   `tfsdk:"disabled"`
	ListenPort tftypes.Int64  `tfsdk:"listen_port"`
	Mtu        tftypes.Int64  `tfsdk:"mtu"`
	PrivateKey tftypes.String `tfsdk:"private_key"`
	PublicKey  tftypes.String `tfsdk:"public_key"`
	Running    tftypes.Bool   `tfsdk:"running"`
}


File: /mikrotik\resource_interface_wireguard_peer.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-framework-validators/int64validator"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/int64default"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"
	"github.com/hashicorp/terraform-plugin-framework/schema/validator"
	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type interfaceWireguardPeer struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &interfaceWireguardPeer{}
	_ resource.ResourceWithConfigure   = &interfaceWireguardPeer{}
	_ resource.ResourceWithImportState = &interfaceWireguardPeer{}
)

// NewInterfaceWireguardPeerResource is a helper function to simplify the provider implementation.
func NewInterfaceWireguardPeerResource() resource.Resource {
	return &interfaceWireguardPeer{}

}

func (i *interfaceWireguardPeer) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	i.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (i *interfaceWireguardPeer) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_interface_wireguard_peer"
}

// Schema defines the schema for the resource.
// TODO: Reevaluate the Computed schema attributes and determine if that is correct
func (i *interfaceWireguardPeer) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a Mikrotik Interface Wireguard Peer only supported by RouterOS v7+.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Identifier of this resource assigned by RouterOS",
			},
			"allowed_address": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "List of IP (v4 or v6) addresses with CIDR masks from which incoming traffic for this peer is allowed and to which outgoing traffic for this peer is directed. The catch-all 0.0.0.0/0 may be specified for matching all IPv4 addresses, and ::/0 may be specified for matching all IPv6 addresses.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "Short description of the peer.",
			},
			"disabled": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "Boolean for whether or not the interface peer is disabled.",
			},
			"endpoint_address": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "An endpoint IP or hostname can be left blank to allow remote connection from any address.",
			},
			"endpoint_port": schema.Int64Attribute{
				Optional: true,
				Computed: true,
				Default:  int64default.StaticInt64(0),
				Validators: []validator.Int64{
					int64validator.Between(0, 65535),
				},
				Description: "An endpoint port can be left blank to allow remote connection from any port.",
			},
			"interface": schema.StringAttribute{
				Required:    true,
				Description: "Name of the WireGuard interface the peer belongs to.",
			},
			"persistent_keepalive": schema.Int64Attribute{
				Optional: true,
				Computed: true,
				Default:  int64default.StaticInt64(0),
				Validators: []validator.Int64{
					int64validator.Between(0, 65535),
				},
				Description: "A seconds interval, between 1 and 65535 inclusive, of how often to send an authenticated empty packet to the peer for the purpose of keeping a stateful firewall or NAT mapping valid persistently. For example, if the interface very rarely sends traffic, but it might at anytime receive traffic from a peer, and it is behind NAT, the interface might benefit from having a persistent keepalive interval of 25 seconds.",
			},
			"preshared_key": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "A base64 preshared key. Optional, and may be omitted. This option adds an additional layer of symmetric-key cryptography to be mixed into the already existing public-key cryptography, for post-quantum resistance.",
			},
			"public_key": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The remote peer's calculated public key.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (i *interfaceWireguardPeer) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel interfaceWireguardPeerModel
	var mikrotikModel client.InterfaceWireguardPeer
	GenericCreateResource(&terraformModel, &mikrotikModel, i.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (i *interfaceWireguardPeer) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel interfaceWireguardPeerModel
	var mikrotikModel client.InterfaceWireguardPeer
	GenericReadResource(&terraformModel, &mikrotikModel, i.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (i *interfaceWireguardPeer) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel interfaceWireguardPeerModel
	var mikrotikModel client.InterfaceWireguardPeer
	GenericUpdateResource(&terraformModel, &mikrotikModel, i.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (i *interfaceWireguardPeer) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel interfaceWireguardPeerModel
	var mikrotikModel client.InterfaceWireguardPeer
	GenericDeleteResource(&terraformModel, &mikrotikModel, i.client)(ctx, req, resp)
}

func (i *interfaceWireguardPeer) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	utils.ImportUppercaseWrapper(resource.ImportStatePassthroughID)(ctx, path.Root("id"), req, resp)
}

type interfaceWireguardPeerModel struct {
	Id                  tftypes.String `tfsdk:"id"`
	AllowedAddress      tftypes.String `tfsdk:"allowed_address"`
	Comment             tftypes.String `tfsdk:"comment"`
	Disabled            tftypes.Bool   `tfsdk:"disabled"`
	EndpointAddress     tftypes.String `tfsdk:"endpoint_address"`
	EndpointPort        tftypes.Int64  `tfsdk:"endpoint_port"`
	Interface           tftypes.String `tfsdk:"interface"`
	PersistentKeepalive tftypes.Int64  `tfsdk:"persistent_keepalive"`
	PresharedKey        tftypes.String `tfsdk:"preshared_key"`
	PublicKey           tftypes.String `tfsdk:"public_key"`
}


File: /mikrotik\resource_interface_wireguard_peer_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/acctest"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

var origCommentPeer string = "testing"
var origAllowedAddress string = "192.168.8.1/32"
var updatedCommentPeer string = "new_comment"

func TestAccMikrotikInterfaceWireguardPeer_create(t *testing.T) {
	client.SkipIfRouterOSV6OrEarlier(t, sysResources)

	interfaceName := acctest.RandomWithPrefix("tf-acc-interface-wireguard")
	publicKey := "/yZWgiYAgNNSy7AIcxuEewYwOVPqJJRKG90s9ypwfiM="
	resourceName := "mikrotik_interface_wireguard_peer.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikInterfaceWireguardPeerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccInterfaceWireguardPeer(interfaceName, publicKey),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceWireguardPeerExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "allowed_address", origAllowedAddress),
					resource.TestCheckResourceAttr(resourceName, "public_key", publicKey),
					resource.TestCheckResourceAttr(resourceName, "interface", interfaceName)),
			},
		},
	})
}

func TestAccMikrotikInterfaceWireguardPeer_updatedComment(t *testing.T) {
	client.SkipIfRouterOSV6OrEarlier(t, sysResources)

	interfaceName := acctest.RandomWithPrefix("tf-acc-interface-wireguard")
	publicKey := "/bTmUihbgNsSy2AIcxuEcwYwOVdqJJRKG51s4ypwfiM="
	resourceName := "mikrotik_interface_wireguard_peer.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikInterfaceWireguardPeerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccInterfaceWireguardPeer(interfaceName, publicKey),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceWireguardPeerExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "interface", interfaceName),
					resource.TestCheckResourceAttr(resourceName, "public_key", publicKey),
					resource.TestCheckResourceAttr(resourceName, "comment", origCommentPeer)),
			},
			{
				Config: testAccInterfaceWireguardPeerUpdatedComment(interfaceName, publicKey),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceWireguardPeerExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "interface", interfaceName),
					resource.TestCheckResourceAttr(resourceName, "comment", updatedCommentPeer)),
			},
		},
	})
}

func TestAccMikrotikInterfaceWireguardPeer_update(t *testing.T) {
	client.SkipIfRouterOSV6OrEarlier(t, sysResources)

	interfaceName := acctest.RandomWithPrefix("tf-acc-interface-wireguard")
	publicKey := "/bTmUihbgNsSy2AIcxuEcwYwOVdqJJRKG51s4ypwfiM="
	resourceName := "mikrotik_interface_wireguard_peer.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikInterfaceWireguardPeerDestroy,
		Steps: []resource.TestStep{
			{
				Config: fmt.Sprintf(`
				resource "mikrotik_interface_wireguard" "bar" {
					name = "%s"
					listen_port = 13231
					mtu = 1420
				}

				resource "mikrotik_interface_wireguard_peer" "bar" {
					interface = mikrotik_interface_wireguard.bar.name
					public_key = "%s"
					allowed_address = "%s"
					endpoint_port = 13251
				}`, interfaceName, publicKey, origAllowedAddress),

				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceWireguardPeerExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "interface", interfaceName),
					resource.TestCheckResourceAttr(resourceName, "public_key", publicKey),
				),
			},
			{
				Config: fmt.Sprintf(`
				resource "mikrotik_interface_wireguard" "bar" {
					name = "%s"
					listen_port = 13231
					mtu = 1420
				}

				resource "mikrotik_interface_wireguard_peer" "bar" {
					interface = mikrotik_interface_wireguard.bar.name
					public_key = "%s"
					allowed_address = "%s"
					endpoint_port = 13251
					persistent_keepalive = 3602
				}`, interfaceName, publicKey, origAllowedAddress),

				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceWireguardPeerExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "interface", interfaceName),
					resource.TestCheckResourceAttr(resourceName, "persistent_keepalive", "3602"),
				),
			},
		},
	})
}

func TestAccMikrotikInterfaceWireguardPeer_import(t *testing.T) {
	client.SkipIfRouterOSV6OrEarlier(t, sysResources)

	interfaceName := acctest.RandomWithPrefix("tf-acc-interface-wireguard")
	publicKey := "/zYaGiYbgNsSy8AIcxuEcwYwOVdqJJRKG91s9ypwfiM="
	resourceName := "mikrotik_interface_wireguard_peer.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikInterfaceWireguardPeerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccInterfaceWireguardPeer(interfaceName, publicKey),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceWireguardPeerExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "interface"),
					resource.TestCheckResourceAttr(resourceName, "public_key", publicKey),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
				),
			},
			{
				ResourceName:      resourceName,
				ImportState:       true,
				ImportStateVerify: true,
			},
		},
	})
}

func testAccInterfaceWireguardPeer(interfaceName string, publicKey string) string {
	return testAccInterfaceWireguard(interfaceName) + fmt.Sprintf(`
	resource "mikrotik_interface_wireguard_peer" "bar" {
		interface = mikrotik_interface_wireguard.bar.name
		public_key = "%s"
		comment = "%s"
		allowed_address = "%s"
	}
	`, publicKey, origCommentPeer, origAllowedAddress)
}

func testAccInterfaceWireguardPeerUpdatedComment(interfaceName string, publicKey string) string {
	return testAccInterfaceWireguard(interfaceName) + fmt.Sprintf(`
	resource "mikrotik_interface_wireguard_peer" "bar" {
		interface = mikrotik_interface_wireguard.bar.name
		public_key = "%s"
		comment = "%s"
		allowed_address = "%s"
	}
	`, publicKey, updatedCommentPeer, origAllowedAddress)
}

func testAccCheckMikrotikInterfaceWireguardPeerDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_interface_wireguard_peer" {
			continue
		}

		interfaceWireguardPeer, err := c.FindInterfaceWireguardPeer(rs.Primary.Attributes["interface"])

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if interfaceWireguardPeer != nil {
			return fmt.Errorf("interface wireguard peer (%s) still exists", interfaceWireguardPeer.Interface)
		}
	}
	return nil
}

func testAccInterfaceWireguardPeerExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("mikrotik_interface_wireguard_peer does not exist in the statefile")
		}

		c := client.NewClient(client.GetConfigFromEnv())

		interfaceWireguardPeer, err := c.FindInterfaceWireguardPeer(rs.Primary.ID)

		_, ok = err.(*client.NotFound)
		if !ok && err != nil {
			return fmt.Errorf("Unable to get the interface wireguard peer with error: %v", err)
		}

		if interfaceWireguardPeer == nil {
			return fmt.Errorf("Unable to get the interface wireguard peer with interface: %s", rs.Primary.Attributes["interface"])
		}

		if interfaceWireguardPeer.Id == rs.Primary.Attributes[".id"] {
			return nil
		}
		return nil
	}
}


File: /mikrotik\resource_interface_wireguard_test.go
package mikrotik

import (
	"fmt"
	"strconv"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/acctest"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

var origComment string = "testing"
var origListenPort int = 13231
var origMTU int = 1420
var updatedComment string = "new_comment"

func TestAccMikrotikInterfaceWireguard_create(t *testing.T) {
	client.SkipIfRouterOSV6OrEarlier(t, sysResources)
	name := acctest.RandomWithPrefix("tf-acc-create")

	resourceName := "mikrotik_interface_wireguard.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikInterfaceWireguardDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccInterfaceWireguard(name),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceWireguardExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "comment", origComment),
					resource.TestCheckResourceAttr(resourceName, "listen_port", strconv.Itoa(origListenPort)),
					resource.TestCheckResourceAttr(resourceName, "mtu", strconv.Itoa(origMTU)),
					resource.TestCheckResourceAttr(resourceName, "disabled", "false")),
			},
		},
	})
}

func TestAccMikrotikInterfaceWireguard_updatedComment(t *testing.T) {
	client.SkipIfRouterOSV6OrEarlier(t, sysResources)
	name := acctest.RandomWithPrefix("tf-acc-update-comment")

	resourceName := "mikrotik_interface_wireguard.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikInterfaceWireguardDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccInterfaceWireguard(name),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceWireguardExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "comment", origComment)),
			},
			{
				Config: testAccInterfaceWireguardUpdatedComment(name),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceWireguardExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "comment", updatedComment)),
			},
		},
	})
}

func TestAccMikrotikInterfaceWireguard_import(t *testing.T) {
	client.SkipIfRouterOSV6OrEarlier(t, sysResources)
	name := acctest.RandomWithPrefix("tf-acc-import")

	resourceName := "mikrotik_interface_wireguard.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikInterfaceWireguardDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccInterfaceWireguard(name),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccInterfaceWireguardExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttrSet(resourceName, "name"),
				),
			},
			{
				ResourceName:      resourceName,
				ImportState:       true,
				ImportStateId:     name,
				ImportStateVerify: true,
			},
		},
	})
}

func testAccInterfaceWireguard(name string) string {
	return fmt.Sprintf(`
resource "mikrotik_interface_wireguard" "bar" {
    name = "%s"
	comment = "%s"
	listen_port = "%d"
	mtu = "%d"
}
`, name, origComment, origListenPort, origMTU)
}

func testAccInterfaceWireguardUpdatedComment(name string) string {
	return fmt.Sprintf(`
	resource "mikrotik_interface_wireguard" "bar" {
		name = "%s"
		comment = "%s"
		listen_port = "%d"
		mtu = "%d"
	}
	`, name, updatedComment, origListenPort, origMTU)
}

func testAccCheckMikrotikInterfaceWireguardDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_interface_wireguard" {
			continue
		}

		interfaceWireguard, err := c.FindInterfaceWireguard(rs.Primary.Attributes["name"])

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if interfaceWireguard != nil {
			return fmt.Errorf("interface wireguard (%s) still exists", interfaceWireguard.Name)
		}
	}
	return nil
}

func testAccInterfaceWireguardExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("mikrotik_interface_wireguard does not exist in the statefile")
		}

		c := client.NewClient(client.GetConfigFromEnv())

		interfaceWireguard, err := c.FindInterfaceWireguard(rs.Primary.Attributes["name"])

		if err != nil {
			return fmt.Errorf("Unable to get the interface wireguard with error: %v", err)
		}

		if interfaceWireguard == nil {
			return fmt.Errorf("Unable to get the interface wireguard with name: %s", rs.Primary.Attributes["name"])
		}

		if interfaceWireguard.Name == rs.Primary.Attributes["name"] {
			return nil
		}
		return nil
	}
}


File: /mikrotik\resource_ipv6_address.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"
	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type ipv6Address struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &ipv6Address{}
	_ resource.ResourceWithConfigure   = &ipv6Address{}
	_ resource.ResourceWithImportState = &ipv6Address{}
)

// NewIpv6AddressResource is a helper function to simplify the provider implementation.
func NewIpv6AddressResource() resource.Resource {
	return &ipv6Address{}
}

func (r *ipv6Address) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *ipv6Address) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_ipv6_address"
}

// Schema defines the schema for the resource.
func (s *ipv6Address) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a MikroTik Ipv6Address.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique identifier for this resource.",
			},
			"address": schema.StringAttribute{
				Required:    true,
				Description: "The IPv6 address and prefix length of the interface using slash notation.",
			},
			"advertise": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "Whether to enable stateless address configuration. The prefix of that address is automatically advertised to hosts using ICMPv6 protocol. The option is set by default for addresses with prefix length 64.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The comment for the IPv6 address assignment.",
			},
			"disabled": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "Whether to disable IPv6 address.",
			},
			"eui_64": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "Whether to calculate EUI-64 address and use it as last 64 bits of the IPv6 address.",
			},
			"from_pool": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "Name of the pool from which prefix will be taken to construct IPv6 address taking last part of the address from address property.",
			},
			"interface": schema.StringAttribute{
				Required:    true,
				Description: "The interface on which the IPv6 address is assigned.",
			},
			"no_dad": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "If set indicates that address is anycast address and Duplicate Address Detection should not be performed.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *ipv6Address) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel ipv6AddressModel
	var mikrotikModel client.Ipv6Address
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *ipv6Address) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel ipv6AddressModel
	var mikrotikModel client.Ipv6Address
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *ipv6Address) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel ipv6AddressModel
	var mikrotikModel client.Ipv6Address
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *ipv6Address) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel ipv6AddressModel
	var mikrotikModel client.Ipv6Address
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *ipv6Address) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	utils.ImportUppercaseWrapper(resource.ImportStatePassthroughID)(ctx, path.Root("id"), req, resp)
}

type ipv6AddressModel struct {
	Id        tftypes.String `tfsdk:"id"`
	Address   tftypes.String `tfsdk:"address"`
	Advertise tftypes.Bool   `tfsdk:"advertise"`
	Comment   tftypes.String `tfsdk:"comment"`
	Disabled  tftypes.Bool   `tfsdk:"disabled"`
	Eui64     tftypes.Bool   `tfsdk:"eui_64"`
	FromPool  tftypes.String `tfsdk:"from_pool"`
	Interface tftypes.String `tfsdk:"interface"`
	NoDad     tftypes.Bool   `tfsdk:"no_dad"`
}


File: /mikrotik\resource_ipv6_address_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/acctest"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestAccMikrotikResourceIpv6Address_create(t *testing.T) {
	client.SkipIfRouterOSV6OrEarlier(t, sysResources)

	ipv6Addr := internal.GetNewIpv6Addr() + "/64"
	ifName := "ether1"
	comment := acctest.RandomWithPrefix("tf-acc-comment")

	resourceName := "mikrotik_ipv6_address.test"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikIpv6AddressDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccIpv6Address(ipv6Addr, ifName, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccIpv6AddressExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "address", ipv6Addr),
					resource.TestCheckResourceAttr(resourceName, "interface", ifName),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
				),
			},
		},
	})
}

func TestAccMikrotikResourceIpv6Address_create_onlyRequiredFields(t *testing.T) {
	client.SkipIfRouterOSV6OrEarlier(t, sysResources)

	ipv6Addr := internal.GetNewIpv6Addr() + "/64"
	ifName := "ether1"

	resourceName := "mikrotik_ipv6_address.test_required_fields"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikIpv6AddressDestroy,
		Steps: []resource.TestStep{
			{
				Config: fmt.Sprintf(`resource "mikrotik_ipv6_address" "test_required_fields" {
							address = "%s"
							interface = "%s"
						}`, ipv6Addr, ifName,
				),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccIpv6AddressExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "address", ipv6Addr),
					resource.TestCheckResourceAttr(resourceName, "interface", ifName),
					resource.TestCheckResourceAttr(resourceName, "comment", ""),
				),
			},
		},
	})
}

func TestAccMikrotikResourceIpv6Address_updateAddr(t *testing.T) {
	client.SkipIfRouterOSV6OrEarlier(t, sysResources)

	ipAddr := internal.GetNewIpv6Addr() + "/64"
	updatedIpv6Addr := internal.GetNewIpv6Addr() + "/64"
	ifName := "ether1"
	comment := acctest.RandomWithPrefix("tf-acc-comment")
	disabled := "false"
	updatedComment := acctest.RandomWithPrefix("tf-acc-comment")
	updatedDisabled := "true"

	resourceName := "mikrotik_ipv6_address.test"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikIpv6AddressDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccIpv6Address(ipAddr, ifName, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccIpv6AddressExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "interface", ifName),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
					resource.TestCheckResourceAttr(resourceName, "disabled", disabled),
				),
			},
			{
				Config: testAccIpv6Address(updatedIpv6Addr, ifName, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccIpv6AddressExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", updatedIpv6Addr),
					resource.TestCheckResourceAttr(resourceName, "interface", ifName),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
					resource.TestCheckResourceAttr(resourceName, "disabled", disabled),
				),
			},
			{
				Config: testAccIpv6Address(ipAddr, ifName, updatedComment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccIpv6AddressExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "interface", ifName),
					resource.TestCheckResourceAttr(resourceName, "comment", updatedComment),
					resource.TestCheckResourceAttr(resourceName, "disabled", disabled),
				),
			},
			{
				Config: testAccIpv6AddressUpdatedDisabled(ipAddr, ifName, comment, updatedDisabled),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccIpv6AddressExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "interface", ifName),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
					resource.TestCheckResourceAttr(resourceName, "disabled", updatedDisabled),
				),
			},
		},
	})
}

func testAccIpv6Address(ipAddr, ifName, comment string) string {
	return fmt.Sprintf(`
resource "mikrotik_ipv6_address" "test" {
	address = "%s"
	interface = "%s"
	comment = "%s"
}
`, ipAddr, ifName, comment)
}

func testAccIpv6AddressUpdatedDisabled(ipAddr, ifName, comment string, disabled string) string {
	return fmt.Sprintf(`
resource "mikrotik_ipv6_address" "test" {
	address = "%s"
	interface = "%s"
	comment = "%s"
	disabled = "%s"
}
`, ipAddr, ifName, comment, disabled)
}

func testAccIpv6AddressExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("mikrotik_ipv6_address does not exist in the statefile")
		}

		c := client.NewClient(client.GetConfigFromEnv())

		ipaddr, err := c.FindIpv6Address(rs.Primary.ID)

		if err != nil {
			return fmt.Errorf("Unable to get the ipv6 address with error: %v", err)
		}

		if ipaddr == nil {
			return fmt.Errorf("Unable to get the ipv6 address")
		}

		if ipaddr.Id == rs.Primary.ID {
			return nil
		}
		return nil
	}
}

func testAccCheckMikrotikIpv6AddressDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_ipv6_address" {
			continue
		}

		ipaddr, err := c.FindIpv6Address(rs.Primary.ID)

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if ipaddr != nil {
			return fmt.Errorf("ipv6 address (%s) still exists", ipaddr.Id)
		}
	}
	return nil
}


File: /mikrotik\resource_ip_address.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"

	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type ipAddress struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &ipAddress{}
	_ resource.ResourceWithConfigure   = &ipAddress{}
	_ resource.ResourceWithImportState = &ipAddress{}
)

// NewIpAddressResource is a helper function to simplify the provider implementation.
func NewIpAddressResource() resource.Resource {
	return &ipAddress{}
}

func (r *ipAddress) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *ipAddress) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_ip_address"
}

// Schema defines the schema for the resource.
func (s *ipAddress) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Assigns an IP address to an interface.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique ID of this resource.",
			},
			"address": schema.StringAttribute{
				Required:    true,
				Description: "The IP address and netmask of the interface using slash notation.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The comment for the IP address assignment.",
			},
			"disabled": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Description: "Whether to disable IP address.",
			},
			"interface": schema.StringAttribute{
				Required:    true,
				Description: "The interface on which the IP address is assigned.",
			},
			"network": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "IP address for the network.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *ipAddress) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel ipAddressModel
	var mikrotikModel client.IpAddress
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *ipAddress) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel ipAddressModel
	var mikrotikModel client.IpAddress
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *ipAddress) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel ipAddressModel
	var mikrotikModel client.IpAddress
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *ipAddress) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel ipAddressModel
	var mikrotikModel client.IpAddress
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *ipAddress) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	utils.ImportUppercaseWrapper(resource.ImportStatePassthroughID)(ctx, path.Root("id"), req, resp)
}

type ipAddressModel struct {
	Id        tftypes.String `tfsdk:"id"`
	Address   tftypes.String `tfsdk:"address"`
	Comment   tftypes.String `tfsdk:"comment"`
	Disabled  tftypes.Bool   `tfsdk:"disabled"`
	Interface tftypes.String `tfsdk:"interface"`
	Network   tftypes.String `tfsdk:"network"`
}


File: /mikrotik\resource_ip_address_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/acctest"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestAccMikrotikResourceIpAddress_create(t *testing.T) {
	ipAddr := internal.GetNewIpAddr() + "/24"
	ifName := "ether1"
	comment := acctest.RandomWithPrefix("tf-acc-comment")

	resourceName := "mikrotik_ip_address.test"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikIpAddressDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccIpAddress(ipAddr, ifName, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccIpAddressExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "interface", ifName),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
				),
			},
		},
	})
}

func TestAccMikrotikResourceIpAddress_updateAddr(t *testing.T) {
	ipAddr := internal.GetNewIpAddr() + "/24"
	updatedIpAddr := internal.GetNewIpAddr() + "/24"
	ifName := "ether1"
	comment := acctest.RandomWithPrefix("tf-acc-comment")
	disabled := "false"
	updatedComment := acctest.RandomWithPrefix("tf-acc-comment")
	updatedDisabled := "true"

	resourceName := "mikrotik_ip_address.test"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikIpAddressDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccIpAddress(ipAddr, ifName, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccIpAddressExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "interface", ifName),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
					resource.TestCheckResourceAttr(resourceName, "disabled", disabled),
				),
			},
			{
				Config: testAccIpAddress(updatedIpAddr, ifName, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccIpAddressExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", updatedIpAddr),
					resource.TestCheckResourceAttr(resourceName, "interface", ifName),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
					resource.TestCheckResourceAttr(resourceName, "disabled", disabled),
				),
			},
			{
				Config: testAccIpAddress(ipAddr, ifName, updatedComment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccIpAddressExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "interface", ifName),
					resource.TestCheckResourceAttr(resourceName, "comment", updatedComment),
					resource.TestCheckResourceAttr(resourceName, "disabled", disabled),
				),
			},
			{
				Config: testAccIpAddressUpdatedDisabled(ipAddr, ifName, comment, updatedDisabled),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccIpAddressExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "address", ipAddr),
					resource.TestCheckResourceAttr(resourceName, "interface", ifName),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
					resource.TestCheckResourceAttr(resourceName, "disabled", updatedDisabled),
				),
			},
		},
	})
}

func testAccIpAddress(ipAddr, ifName, comment string) string {
	return fmt.Sprintf(`
resource "mikrotik_ip_address" "test" {
	address = "%s"
	interface = "%s"
	comment = "%s"
}
`, ipAddr, ifName, comment)
}

func testAccIpAddressUpdatedDisabled(ipAddr, ifName, comment string, disabled string) string {
	return fmt.Sprintf(`
resource "mikrotik_ip_address" "test" {
	address = "%s"
	interface = "%s"
	comment = "%s"
	disabled = "%s"
}
`, ipAddr, ifName, comment, disabled)
}

func testAccIpAddressExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("mikrotik_ip_address does not exist in the statefile")
		}

		c := client.NewClient(client.GetConfigFromEnv())

		ipaddr, err := c.FindIpAddress(rs.Primary.ID)

		if err != nil {
			return fmt.Errorf("Unable to get the ip address with error: %v", err)
		}

		if ipaddr == nil {
			return fmt.Errorf("Unable to get the ip address")
		}

		if ipaddr.Id == rs.Primary.ID {
			return nil
		}
		return nil
	}
}

func testAccCheckMikrotikIpAddressDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_ip_address" {
			continue
		}

		ipaddr, err := c.FindIpAddress(rs.Primary.ID)

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if ipaddr != nil {
			return fmt.Errorf("ip address (%s) still exists", ipaddr.Id)
		}
	}

	return nil
}


File: /mikrotik\resource_pool.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal/utils"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"
	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type pool struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &pool{}
	_ resource.ResourceWithConfigure   = &pool{}
	_ resource.ResourceWithImportState = &pool{}
)

// NewPoolResource is a helper function to simplify the provider implementation.
func NewPoolResource() resource.Resource {
	return &pool{}
}

func (r *pool) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *pool) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_pool"
}

// Schema defines the schema for the resource.
func (s *pool) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a Mikrotik IP Pool.",

		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "ID of this resource.",
			},
			"name": schema.StringAttribute{
				Required:    true,
				Description: "The name of IP pool.",
			},
			"ranges": schema.StringAttribute{
				Required:    true,
				Description: "The IP range(s) of the pool. Multiple ranges can be specified, separated by commas: `172.16.0.6-172.16.0.12,172.16.0.50-172.16.0.60`.",
			},
			"next_pool": schema.StringAttribute{
				Optional: true,
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "The IP pool to pick next address from if current is exhausted.",
			},
			"comment": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "The comment of the IP Pool to be created.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *pool) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel poolModel
	var mikrotikModel client.Pool

	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *pool) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel poolModel
	var mikrotikModel client.Pool

	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
//
// The body is a copy-paste code from `GenericUpdateResource()` functions.
// It's done to support special case of 'unsetting' the 'next_pool' field.
// Since RouterOS API does not support empty value `""` for this field,
// a 'magic' value of 'none' is used.
// In that case, Terraform argues that planned value was `none` but actual (after Read() method) is `""`
// The only difference from `GenericUpdateResource()` in this implementation is checking of
// transition from some value to `""` for `next_pool` field. In that case, we simply change value to `none`,
// so API client can unset this value and subsequent `Read()` method will see `""` which is the same as config value.
//
// Be aware, that this hack prevents using `none` value explicitly in the configuration.
func (r *pool) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel, state poolModel
	var mikrotikModel client.Pool
	resp.Diagnostics.Append(req.Plan.Get(ctx, &terraformModel)...)
	resp.Diagnostics.Append(req.State.Get(ctx, &state)...)
	if resp.Diagnostics.HasError() {
		return
	}
	// if practitioner sets this value to `""` to unset field in remote system,
	// implicitly send `"none"` via API
	if !terraformModel.NextPool.Equal(state.NextPool) && terraformModel.NextPool.ValueString() == "" {
		terraformModel.NextPool = tftypes.StringValue("none")
	}

	if err := utils.TerraformModelToMikrotikStruct(ctx, &terraformModel, &mikrotikModel); err != nil {
		resp.Diagnostics.AddError("Cannot copy model: Terraform -> MikroTik", err.Error())
		return
	}
	updated, err := r.client.Update(&mikrotikModel)
	if err != nil {
		resp.Diagnostics.AddError("Update failed", err.Error())
		return
	}
	if err := utils.MikrotikStructToTerraformModel(ctx, updated, &terraformModel); err != nil {
		resp.Diagnostics.AddError("Cannot copy model: MikroTik -> Terraform", err.Error())
		return
	}

	resp.Diagnostics.Append(resp.State.Set(ctx, terraformModel)...)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *pool) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel poolModel
	var mikrotikModel client.Pool
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *pool) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	utils.ImportUppercaseWrapper(resource.ImportStatePassthroughID)(ctx, path.Root("id"), req, resp)
}

type poolModel struct {
	Id       tftypes.String `tfsdk:"id"`
	Name     tftypes.String `tfsdk:"name"`
	Ranges   tftypes.String `tfsdk:"ranges"`
	NextPool tftypes.String `tfsdk:"next_pool"`
	Comment  tftypes.String `tfsdk:"comment"`
}


File: /mikrotik\resource_pool_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/ddelnano/terraform-provider-mikrotik/mikrotik/internal"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/acctest"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestAccMikrotikPool_create(t *testing.T) {
	name := acctest.RandomWithPrefix("pool-create")
	ranges := fmt.Sprintf("%s,%s", internal.GetNewIpAddrRange(10), internal.GetNewIpAddr())

	resourceName := "mikrotik_pool.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikPoolDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccPool(name, ranges),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccPoolExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "ranges", ranges),
				),
			},
		},
	})
}

func TestAccMikrotikPool_createNextPool(t *testing.T) {
	name := acctest.RandomWithPrefix("pool-create")
	nextPoolName := acctest.RandomWithPrefix("next_ip_pool")
	ranges := fmt.Sprintf("%s,%s", internal.GetNewIpAddrRange(10), internal.GetNewIpAddr())

	resourceName := "mikrotik_pool.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikPoolDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccPoolWithNextPool(name, ranges, "", nextPoolName),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccPoolExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "ranges", ranges),
					resource.TestCheckResourceAttr(resourceName, "next_pool", ""),
				),
			}, {
				Config: testAccPoolWithNextPool(name, ranges, nextPoolName, nextPoolName),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccPoolExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "ranges", ranges),
					resource.TestCheckResourceAttr(resourceName, "next_pool", nextPoolName),
				),
			},
			{
				Config: testAccPoolWithNextPool(name, ranges, "", "next_ip_pool"),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccPoolExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "ranges", ranges),
					resource.TestCheckResourceAttr(resourceName, "next_pool", ""),
				),
			},
		},
	})
}

func TestAccMikrotikPool_createAndPlanWithNonExistantPool(t *testing.T) {
	name := acctest.RandomWithPrefix("pool-plan")
	ranges := fmt.Sprintf("%s,%s", internal.GetNewIpAddrRange(10), internal.GetNewIpAddr())

	resourceName := "mikrotik_pool.bar"
	removePool := func() {

		c := client.NewClient(client.GetConfigFromEnv())
		pool, err := c.FindPoolByName(name)
		if err != nil {
			t.Fatalf("Error finding the pool by name: %s", err)
		}
		err = c.DeletePool(pool.Id)
		if err != nil {
			t.Fatalf("Error removing the pool: %s", err)
		}
	}
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikPoolDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccPool(name, ranges),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccPoolExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id")),
			},
			{
				PreConfig:          removePool,
				Config:             testAccPool(name, ranges),
				ExpectNonEmptyPlan: false,
			},
		},
	})
}

func TestAccMikrotikPool_updatePool(t *testing.T) {
	name := acctest.RandomWithPrefix("pool-update-1")
	updatedName := acctest.RandomWithPrefix("pool-update-2")
	ranges := fmt.Sprintf("%s,%s", internal.GetNewIpAddrRange(10), internal.GetNewIpAddr())
	updatedRanges := fmt.Sprintf("%s,%s", internal.GetNewIpAddrRange(10), internal.GetNewIpAddr())
	comment := acctest.RandomWithPrefix("tf-acc-comment")

	resourceName := "mikrotik_pool.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikPoolDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccPool(name, ranges),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccPoolExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "ranges", ranges),
				),
			},
			{
				Config: testAccPool(updatedName, ranges),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccPoolExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", updatedName),
					resource.TestCheckResourceAttr(resourceName, "ranges", ranges),
				),
			},
			{
				Config: testAccPool(name, updatedRanges),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccPoolExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "ranges", updatedRanges),
				),
			},
			{
				Config: testAccPoolWithComment(name, ranges, comment),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccPoolExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "ranges", ranges),
					resource.TestCheckResourceAttr(resourceName, "comment", comment),
				),
			},
		},
	})
}

func TestAccMikrotikPool_import(t *testing.T) {
	name := acctest.RandomWithPrefix("pool-import")
	ranges := fmt.Sprintf("%s,%s", internal.GetNewIpAddrRange(10), internal.GetNewIpAddr())

	resourceName := "mikrotik_pool.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikPoolDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccPool(name, ranges),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccPoolExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id")),
			},
			{
				ResourceName:      resourceName,
				ImportState:       true,
				ImportStateVerify: true,
			},
		},
	})
}

func testAccPool(name, ranges string) string {
	return fmt.Sprintf(`
resource "mikrotik_pool" "bar" {
    name = "%s"
    ranges = "%s"
}
`, name, ranges)
}

func testAccPoolWithNextPool(name, ranges, nextPoolToUse, nextPoolName string) string {
	return fmt.Sprintf(`
resource "mikrotik_pool" "bar" {
    name = %q
    ranges = %q
    next_pool = %q
    depends_on = [mikrotik_pool.next_pool]
}

resource "mikrotik_pool" "next_pool" {
    name = %q
    ranges = "10.10.10.10-10.10.10.20"
}
`, name, ranges, nextPoolToUse, nextPoolName)
}

func testAccPoolWithComment(name, ranges, comment string) string {
	return fmt.Sprintf(`
resource "mikrotik_pool" "bar" {
    name = "%s"
    ranges = "%s"
    comment = "%s"
}
`, name, ranges, comment)
}

func testAccPoolExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("mikrotik_pool does not exist in the statefile")
		}

		c := client.NewClient(client.GetConfigFromEnv())

		pool, err := c.FindPool(rs.Primary.ID)

		if err != nil {
			return fmt.Errorf("Unable to get the pool with error: %v", err)
		}

		if pool == nil {
			return fmt.Errorf("Unable to get the pool")
		}

		if pool.Id == rs.Primary.ID {
			return nil
		}
		return nil
	}
}

func testAccCheckMikrotikPoolDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_pool" {
			continue
		}

		pool, err := c.FindPool(rs.Primary.ID)

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if pool != nil {
			return fmt.Errorf("pool (%s) still exists", pool.Id)
		}
	}
	return nil
}


File: /mikrotik\resource_scheduler.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"
	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type scheduler struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &scheduler{}
	_ resource.ResourceWithConfigure   = &scheduler{}
	_ resource.ResourceWithImportState = &scheduler{}
)

// NewSchedulerResource is a helper function to simplify the provider implementation.
func NewSchedulerResource() resource.Resource {
	return &scheduler{}
}

func (s *scheduler) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	s.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (s *scheduler) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_scheduler"
}

// Schema defines the schema for the resource.
func (s *scheduler) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a Mikrotik scheduler.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Identifier of this resource assigned by RouterOS",
			},
			"name": schema.StringAttribute{
				Required:    true,
				Description: "Name of the task.",
			},
			"on_event": schema.StringAttribute{
				Required:    true,
				Description: "Name of the script to execute. It must exist `/system script`.",
			},
			"start_date": schema.StringAttribute{
				Optional: true,
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Date of the first script execution.",
			},
			"start_time": schema.StringAttribute{
				Optional: true,
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Time of the first script execution.",
			},
			"interval": schema.Int64Attribute{
				Optional:    true,
				Computed:    true,
				Description: "Interval between two script executions, if time interval is set to zero, the script is only executed at its start time, otherwise it is executed repeatedly at the time interval is specified.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (s *scheduler) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel schedulerModel
	var mikrotikModel client.Scheduler
	GenericCreateResource(&terraformModel, &mikrotikModel, s.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (s *scheduler) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel schedulerModel
	var mikrotikModel client.Scheduler
	GenericReadResource(&terraformModel, &mikrotikModel, s.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (s *scheduler) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel schedulerModel
	var mikrotikModel client.Scheduler
	GenericUpdateResource(&terraformModel, &mikrotikModel, s.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (s *scheduler) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel schedulerModel
	var mikrotikModel client.Scheduler
	GenericDeleteResource(&terraformModel, &mikrotikModel, s.client)(ctx, req, resp)
}

func (s *scheduler) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("name"), req, resp)
}

type schedulerModel struct {
	Id        tftypes.String `tfsdk:"id"`
	Name      tftypes.String `tfsdk:"name"`
	OnEvent   tftypes.String `tfsdk:"on_event"`
	StartDate tftypes.String `tfsdk:"start_date"`
	StartTime tftypes.String `tfsdk:"start_time"`
	Interval  tftypes.Int64  `tfsdk:"interval"`
}


File: /mikrotik\resource_scheduler_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/acctest"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

var origOnEvent string = "testing"
var origInterval int = 0
var updatedOnEvent string = "updated"
var updatedInterval int = 300

func TestAccMikrotikScheduler_create(t *testing.T) {
	name := acctest.RandomWithPrefix("tf-acc-create")

	resourceName := "mikrotik_scheduler.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikSchedulerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccScheduler(name),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccSchedulerExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttrSet(resourceName, "name"),
					resource.TestCheckResourceAttrSet(resourceName, "on_event"),
					resource.TestCheckResourceAttrSet(resourceName, "start_date"),
					resource.TestCheckResourceAttrSet(resourceName, "start_time"),
					resource.TestCheckResourceAttrSet(resourceName, "interval")),
			},
		},
	})
}

func TestAccMikrotikScheduler_updateInterval(t *testing.T) {
	name := acctest.RandomWithPrefix("tf-acc-update")

	resourceName := "mikrotik_scheduler.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikSchedulerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccScheduler(name),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccSchedulerExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "interval", "0")),
			},
			{
				Config: testAccSchedulerUpdatedInterval(name),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccSchedulerExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "interval", "300")),
			},
		},
	})
}

func TestAccMikrotikScheduler_updatedOnEvent(t *testing.T) {
	name := acctest.RandomWithPrefix("tf-acc-update-event")

	resourceName := "mikrotik_scheduler.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikSchedulerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccScheduler(name),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccSchedulerExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "on_event", origOnEvent)),
			},
			{
				Config: testAccSchedulerUpdatedOnEvent(name),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccSchedulerExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "on_event", updatedOnEvent)),
			},
		},
	})
}

func TestAccMikrotikScheduler_import(t *testing.T) {
	name := acctest.RandomWithPrefix("tf-acc-import")

	resourceName := "mikrotik_scheduler.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikSchedulerDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccScheduler(name),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccSchedulerExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttrSet(resourceName, "name"),
				),
			},
			{
				ResourceName: resourceName,
				ImportState:  true,
				ImportStateIdFunc: func(s *terraform.State) (string, error) {
					return name, nil
				},
				ImportStateVerify: true,
			},
		},
	})
}

func testAccScheduler(name string) string {
	return fmt.Sprintf(`
resource "mikrotik_scheduler" "bar" {
    name = "%s"
    on_event = "%s"
}
`, name, origOnEvent)
}

func testAccSchedulerUpdatedInterval(name string) string {
	return fmt.Sprintf(`
resource "mikrotik_scheduler" "bar" {
    name = "%s"
    on_event = "%s"
    interval = "%d"
}
`, name, origOnEvent, updatedInterval)
}

func testAccSchedulerUpdatedOnEvent(name string) string {
	return fmt.Sprintf(`
resource "mikrotik_scheduler" "bar" {
    name = "%s"
    on_event = "%s"
    interval = "%d"
}
`, name, updatedOnEvent, origInterval)
}

func testAccCheckMikrotikSchedulerDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_scheduler" {
			continue
		}

		scheduler, err := c.FindScheduler(rs.Primary.ID)

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if scheduler != nil {
			return fmt.Errorf("scheduler (%s) still exists", scheduler.Name)
		}
	}
	return nil
}

func testAccSchedulerExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("mikrotik_scheduler does not exist in the statefile")
		}

		c := client.NewClient(client.GetConfigFromEnv())

		scheduler, err := c.FindScheduler(rs.Primary.Attributes["name"])

		if !client.IsNotFoundError(err) && err != nil {
			return fmt.Errorf("Unable to get the scheduler with error: %v", err)
		}

		if scheduler == nil {
			return fmt.Errorf("Unable to get the scheduler with name: %s", rs.Primary.ID)
		}

		if scheduler.Name == rs.Primary.ID {
			return nil
		}
		return nil
	}
}


File: /mikrotik\resource_script.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type script struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &script{}
	_ resource.ResourceWithConfigure   = &script{}
	_ resource.ResourceWithImportState = &script{}
)

// NewScriptResource is a helper function to simplify the provider implementation.
func NewScriptResource() resource.Resource {
	return &script{}
}

func (r *script) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *script) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_script"
}

// Schema defines the schema for the resource.
func (s *script) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a MikroTik Script.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "ID of this resource.",
			},
			"name": schema.StringAttribute{
				Required: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "The name of script.",
			},
			"policy": schema.ListAttribute{
				Required:    true,
				ElementType: tftypes.StringType,
				Description: "What permissions the script has. This must be one of the following: ftp, reboot, read, write, policy, test, password, sniff, sensitive, romon.",
			},
			"dont_require_permissions": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "If the script requires permissions or not.",
			},
			"source": schema.StringAttribute{
				Required:    true,
				Description: "The source code of the script. See the [MikroTik docs](https://wiki.mikrotik.com/wiki/Manual:Scripting) for the scripting language.",
			},
			"owner": schema.StringAttribute{
				Computed:    true,
				Description: "The owner of the script.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *script) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var plan scriptModel
	resp.Diagnostics.Append(req.Plan.Get(ctx, &plan)...)
	if resp.Diagnostics.HasError() {
		return
	}

	GenericCreateResource(&plan, &client.Script{}, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *script) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var state scriptModel
	resp.Diagnostics.Append(req.State.Get(ctx, &state)...)
	if resp.Diagnostics.HasError() {
		return
	}
	GenericReadResource(&state, &client.Script{}, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *script) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var plan scriptModel
	resp.Diagnostics.Append(req.Plan.Get(ctx, &plan)...)
	if resp.Diagnostics.HasError() {
		return
	}

	GenericUpdateResource(&plan, &client.Script{}, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *script) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var state scriptModel
	resp.Diagnostics.Append(req.State.Get(ctx, &state)...)
	if resp.Diagnostics.HasError() {
		return
	}
	GenericDeleteResource(&state, &client.Script{}, r.client)(ctx, req, resp)
}

func (r *script) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("name"), req, resp)
}

type scriptModel struct {
	Id                     tftypes.String `tfsdk:"id"`
	Name                   tftypes.String `tfsdk:"name"`
	Owner                  tftypes.String `tfsdk:"owner"`
	Policy                 tftypes.List   `tfsdk:"policy"`
	DontRequirePermissions tftypes.Bool   `tfsdk:"dont_require_permissions"`
	Source                 tftypes.String `tfsdk:"source"`
}


File: /mikrotik\resource_script_test.go
package mikrotik

import (
	"fmt"
	"strings"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/acctest"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

var defaultSource = ":put testing"
var defaultPolicies = []string{"ftp", "reboot"}

func TestAccMikrotikScript_create(t *testing.T) {
	name := acctest.RandomWithPrefix("tf-acc-create")

	resourceName := "mikrotik_script.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikScriptDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccScriptRecord(name, defaultSource, defaultPolicies),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccScriptExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id")),
			},
		},
	})
}

func TestAccMikrotikScript_updateSource(t *testing.T) {
	name := acctest.RandomWithPrefix("tf-acc-update-src")
	updatedSource := ":put updated"

	resourceName := "mikrotik_script.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikScriptDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccScriptRecord(name, defaultSource, defaultPolicies),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccScriptExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "source", defaultSource)),
			},
			{
				Config: testAccScriptRecord(name, updatedSource, defaultPolicies),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccScriptExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "source", updatedSource)),
			},
		},
	})
}

func TestAccMikrotikScript_updateDontReqPerms(t *testing.T) {
	name := acctest.RandomWithPrefix("tf-acc-update-perm")

	resourceName := "mikrotik_script.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikScriptDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccScriptRecord(name, defaultSource, defaultPolicies),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccScriptExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "dont_require_permissions", "false")),
			},
			{
				Config: testAccScriptRecordWithPerms(name, defaultSource, defaultPolicies, true),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccScriptExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "dont_require_permissions", "true")),
			},
		},
	})
}

func TestAccMikrotikScript_updatePolicies(t *testing.T) {
	name := acctest.RandomWithPrefix("tf-acc-update-pol")
	updatedPolicies := []string{"ftp"}

	resourceName := "mikrotik_script.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikScriptDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccScriptRecord(name, defaultSource, defaultPolicies),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccScriptExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "policy.#", "2"),
					resource.TestCheckResourceAttr(resourceName, "policy.0", defaultPolicies[0]),
					resource.TestCheckResourceAttr(resourceName, "policy.1", defaultPolicies[1])),
			},
			{
				Config: testAccScriptRecord(name, defaultSource, updatedPolicies),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccScriptExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "policy.#", "1"),
					resource.TestCheckResourceAttr(resourceName, "policy.0", updatedPolicies[0])),
			},
		},
	})
}

func TestAccMikrotikScript_import(t *testing.T) {
	name := acctest.RandomWithPrefix("tf-acc-import")

	resourceName := "mikrotik_script.bar"
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckMikrotikScriptDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccScriptRecord(name, defaultSource, defaultPolicies),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccScriptExists(resourceName),
					resource.TestCheckResourceAttr(resourceName, "dont_require_permissions", "false"),
					resource.TestCheckResourceAttr(resourceName, "owner", "admin")),
			},
			{
				ResourceName:      resourceName,
				ImportState:       true,
				ImportStateVerify: true,
				ImportStateId:     name,
			},
		},
	})
}

func testAccScriptRecord(name, source string, policies []string) string {
	return fmt.Sprintf(`
resource "mikrotik_script" "bar" {
    name = "%s"
    source = "%s"
    policy = ["%s"]
}
`, name, source, strings.Join(policies, "\",\""))
}

func testAccScriptRecordWithPerms(name, source string, policies []string, dontRequirePermissions bool) string {
	return fmt.Sprintf(`
resource "mikrotik_script" "bar" {
    name = "%s"
    source = "%s"
    policy = ["%s"]
    dont_require_permissions = %t
}
`, name, source, strings.Join(policies, "\",\""), dontRequirePermissions)
}

func testAccCheckMikrotikScriptDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_script" {
			continue
		}

		script, err := c.FindScript(rs.Primary.ID)

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if script != nil && script.Name != "" {
			return fmt.Errorf("script (%s) still exists", script.Name)
		}
	}
	return nil
}

func testAccScriptExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("mikrotik_script does not exist in the statefile")
		}

		c := client.NewClient(client.GetConfigFromEnv())

		script, err := c.FindScript(rs.Primary.Attributes["name"])
		if err != nil {
			return fmt.Errorf("Unable to get the script with error: %v", err)
		}

		if script.Name == "" {
			return fmt.Errorf("Unable to get the script with name: %s", rs.Primary.ID)
		}

		if script.Name == rs.Primary.ID {
			return nil
		}
		return nil
	}
}


File: /mikrotik\resource_vlan_interface.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/int64default"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type vlanInterface struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &vlanInterface{}
	_ resource.ResourceWithConfigure   = &vlanInterface{}
	_ resource.ResourceWithImportState = &vlanInterface{}
)

// NewVlanInterfaceResource is a helper function to simplify the provider implementation.
func NewVlanInterfaceResource() resource.Resource {
	return &vlanInterface{}
}

func (r *vlanInterface) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *vlanInterface) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_vlan_interface"
}

// Schema defines the schema for the resource.
func (s *vlanInterface) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Manages Virtual Local Area Network (VLAN) interfaces.",

		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "ID of the resource.",
			},
			"interface": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("*0"),
				Description: "Name of physical interface on top of which VLAN will work.",
			},
			"mtu": schema.Int64Attribute{
				Optional:    true,
				Computed:    true,
				Default:     int64default.StaticInt64(1500),
				Description: "Layer3 Maximum transmission unit.",
			},
			"name": schema.StringAttribute{
				Required:    true,
				Description: "Interface name.",
			},
			"disabled": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "Whether to create the interface in disabled state.",
			},
			"use_service_tag": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "802.1ad compatible Service Tag.",
			},
			"vlan_id": schema.Int64Attribute{
				Optional:    true,
				Computed:    true,
				Default:     int64default.StaticInt64(1),
				Description: "Virtual LAN identifier or tag that is used to distinguish VLANs. Must be equal for all computers that belong to the same VLAN.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *vlanInterface) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel vlanInterfaceModel
	var mikrotikModel client.VlanInterface
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *vlanInterface) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel vlanInterfaceModel
	var mikrotikModel client.VlanInterface
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *vlanInterface) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel vlanInterfaceModel
	var mikrotikModel client.VlanInterface
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *vlanInterface) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel vlanInterfaceModel
	var mikrotikModel client.VlanInterface
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *vlanInterface) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("name"), req, resp)
}

type vlanInterfaceModel struct {
	Id            tftypes.String `tfsdk:"id"`
	Interface     tftypes.String `tfsdk:"interface"`
	Mtu           tftypes.Int64  `tfsdk:"mtu"`
	Name          tftypes.String `tfsdk:"name"`
	Disabled      tftypes.Bool   `tfsdk:"disabled"`
	UseServiceTag tftypes.Bool   `tfsdk:"use_service_tag"`
	VlanId        tftypes.Int64  `tfsdk:"vlan_id"`
}


File: /mikrotik\resource_vlan_interface_test.go
package mikrotik

import (
	"fmt"
	"strconv"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
	"github.com/hashicorp/terraform-plugin-sdk/v2/terraform"
)

func TestVlanInterface_basic(t *testing.T) {
	resourceName := "mikrotik_vlan_interface.testacc"
	iface := "ether1"
	mtu := 1500
	name := "test-vlan"
	useServiceTag := false
	vlanID := 20
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckVlanInterfaceDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccVlanInterface(iface, mtu, name, useServiceTag, vlanID),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccVlanInterfaceExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "mtu", strconv.Itoa(mtu)),
					resource.TestCheckResourceAttr(resourceName, "vlan_id", strconv.Itoa(vlanID)),
				),
			},
			{
				Config: testAccVlanInterface(iface, mtu, name+"updated", useServiceTag, vlanID+1),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccVlanInterfaceExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "name", name+"updated"),
					resource.TestCheckResourceAttr(resourceName, "mtu", strconv.Itoa(mtu)),
					resource.TestCheckResourceAttr(resourceName, "vlan_id", strconv.Itoa(vlanID+1)),
				),
			},
		},
	})
}

func TestVlanInterface_noVlanID(t *testing.T) {
	resourceName := "mikrotik_vlan_interface.testacc"
	iface := "ether1"
	mtu := 1500
	name := "test-vlan"
	useServiceTag := false
	resource.Test(t, resource.TestCase{
		PreCheck:                 func() { testAccPreCheck(t) },
		ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
		CheckDestroy:             testAccCheckVlanInterfaceDestroy,
		Steps: []resource.TestStep{
			{
				Config: testAccVlanInterfaceNoVLANID(iface, mtu, name, useServiceTag),
				Check: resource.ComposeAggregateTestCheckFunc(
					testAccVlanInterfaceExists(resourceName),
					resource.TestCheckResourceAttrSet(resourceName, "id"),
					resource.TestCheckResourceAttr(resourceName, "name", name),
					resource.TestCheckResourceAttr(resourceName, "mtu", strconv.Itoa(mtu)),
					resource.TestCheckResourceAttr(resourceName, "vlan_id", "1"),
				),
			},
		},
	})
}

func testAccVlanInterfaceExists(resourceName string) resource.TestCheckFunc {
	return func(s *terraform.State) error {
		rs, ok := s.RootModule().Resources[resourceName]
		if !ok {
			return fmt.Errorf("Not found: %s", resourceName)
		}

		if rs.Primary.ID == "" {
			return fmt.Errorf("%s does not exist in the statefile", resourceName)
		}

		c := client.NewClient(client.GetConfigFromEnv())
		record, err := c.FindVlanInterface(rs.Primary.Attributes["name"])
		if err != nil {
			return fmt.Errorf("Unable to get remote record for %s: %v", resourceName, err)
		}

		if record == nil {
			return fmt.Errorf("Unable to get the remote record %s", resourceName)
		}

		return nil
	}
}

func testAccCheckVlanInterfaceDestroy(s *terraform.State) error {
	c := client.NewClient(client.GetConfigFromEnv())
	for _, rs := range s.RootModule().Resources {
		if rs.Type != "mikrotik_vlan_interface" {
			continue
		}

		remoteRecord, err := c.FindVlanInterface(rs.Primary.Attributes["name"])

		if !client.IsNotFoundError(err) && err != nil {
			return err
		}

		if remoteRecord != nil {
			return fmt.Errorf("remote record (%s) still exists", remoteRecord.Id)
		}

	}
	return nil
}

func testAccVlanInterface(iface string, mtu int, name string, useServiceTag bool, vlanID int) string {
	return fmt.Sprintf(`
		resource "mikrotik_vlan_interface" "testacc" {
			interface = %q
			mtu = %d
			name = %q
			use_service_tag = %t
			vlan_id = %d
		}
	`, iface, mtu, name, useServiceTag, vlanID)
}

func testAccVlanInterfaceNoVLANID(iface string, mtu int, name string, useServiceTag bool) string {
	return fmt.Sprintf(`
		resource "mikrotik_vlan_interface" "testacc" {
			interface = %q
			mtu = %d
			name = %q
			use_service_tag = %t
		}
	`, iface, mtu, name, useServiceTag)
}


File: /mikrotik\resource_wireless_interface.go
package mikrotik

import (
	"context"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-framework/path"
	"github.com/hashicorp/terraform-plugin-framework/resource"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/booldefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/int64default"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/planmodifier"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringdefault"
	"github.com/hashicorp/terraform-plugin-framework/resource/schema/stringplanmodifier"

	tftypes "github.com/hashicorp/terraform-plugin-framework/types"
)

type wirelessInterface struct {
	client *client.Mikrotik
}

// Ensure the implementation satisfies the expected interfaces.
var (
	_ resource.Resource                = &wirelessInterface{}
	_ resource.ResourceWithConfigure   = &wirelessInterface{}
	_ resource.ResourceWithImportState = &wirelessInterface{}
)

// NewWirelessInterfaceResource is a helper function to simplify the provider implementation.
func NewWirelessInterfaceResource() resource.Resource {
	return &wirelessInterface{}
}

func (r *wirelessInterface) Configure(_ context.Context, req resource.ConfigureRequest, resp *resource.ConfigureResponse) {
	if req.ProviderData == nil {
		return
	}

	r.client = req.ProviderData.(*client.Mikrotik)
}

// Metadata returns the resource type name.
func (r *wirelessInterface) Metadata(_ context.Context, req resource.MetadataRequest, resp *resource.MetadataResponse) {
	resp.TypeName = req.ProviderTypeName + "_wireless_interface"
}

// Schema defines the schema for the resource.
func (s *wirelessInterface) Schema(_ context.Context, _ resource.SchemaRequest, resp *resource.SchemaResponse) {
	resp.Schema = schema.Schema{
		Description: "Creates a MikroTik WirelessInterface.",
		Attributes: map[string]schema.Attribute{
			"id": schema.StringAttribute{
				Computed: true,
				PlanModifiers: []planmodifier.String{
					stringplanmodifier.UseStateForUnknown(),
				},
				Description: "Unique identifier for this resource.",
			},
			"name": schema.StringAttribute{
				Required:    true,
				Description: "Name of the interface.",
			},
			"master_interface": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString(""),
				Description: "Name of wireless interface that has virtual-ap capability. Virtual AP interface will only work if master interface is in ap-bridge, bridge, station or wds-slave mode. This property is only for virtual AP interfaces.",
			},
			"mode": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("station"),
				Description: "Selection between different station and access point (AP) modes.",
			},
			"disabled": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(true),
				Description: "Whether interface is disabled.",
			},
			"security_profile": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("default"),
				Description: "Name of profile from security-profiles.",
			},
			"ssid": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Description: "SSID (service set identifier) is a name that identifies wireless network.",
			},
			"hide_ssid": schema.BoolAttribute{
				Optional:    true,
				Computed:    true,
				Default:     booldefault.StaticBool(false),
				Description: "This property has an effect only in AP mode.",
			},
			"vlan_id": schema.Int64Attribute{
				Optional:    true,
				Computed:    true,
				Default:     int64default.StaticInt64(1),
				Description: "VLAN identification number.",
			},
			"vlan_mode": schema.StringAttribute{
				Optional:    true,
				Computed:    true,
				Default:     stringdefault.StaticString("no-tag"),
				Description: "Three VLAN modes are available: no-tag|use-service-tag|use-tag.",
			},
		},
	}
}

// Create creates the resource and sets the initial Terraform state.
func (r *wirelessInterface) Create(ctx context.Context, req resource.CreateRequest, resp *resource.CreateResponse) {
	var terraformModel wirelessInterfaceModel
	var mikrotikModel client.WirelessInterface
	GenericCreateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Read refreshes the Terraform state with the latest data.
func (r *wirelessInterface) Read(ctx context.Context, req resource.ReadRequest, resp *resource.ReadResponse) {
	var terraformModel wirelessInterfaceModel
	var mikrotikModel client.WirelessInterface
	GenericReadResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Update updates the resource and sets the updated Terraform state on success.
func (r *wirelessInterface) Update(ctx context.Context, req resource.UpdateRequest, resp *resource.UpdateResponse) {
	var terraformModel wirelessInterfaceModel
	var mikrotikModel client.WirelessInterface
	GenericUpdateResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

// Delete deletes the resource and removes the Terraform state on success.
func (r *wirelessInterface) Delete(ctx context.Context, req resource.DeleteRequest, resp *resource.DeleteResponse) {
	var terraformModel wirelessInterfaceModel
	var mikrotikModel client.WirelessInterface
	GenericDeleteResource(&terraformModel, &mikrotikModel, r.client)(ctx, req, resp)
}

func (r *wirelessInterface) ImportState(ctx context.Context, req resource.ImportStateRequest, resp *resource.ImportStateResponse) {
	// Retrieve import ID and save to id attribute
	resource.ImportStatePassthroughID(ctx, path.Root("id"), req, resp)
}

type wirelessInterfaceModel struct {
	Id              tftypes.String `tfsdk:"id"`
	Name            tftypes.String `tfsdk:"name"`
	MasterInterface tftypes.String `tfsdk:"master_interface"`
	Mode            tftypes.String `tfsdk:"mode"`
	Disabled        tftypes.Bool   `tfsdk:"disabled"`
	SecurityProfile tftypes.String `tfsdk:"security_profile"`
	SSID            tftypes.String `tfsdk:"ssid"`
	HideSSID        tftypes.Bool   `tfsdk:"hide_ssid"`
	VlanID          tftypes.Int64  `tfsdk:"vlan_id"`
	VlanMode        tftypes.String `tfsdk:"vlan_mode"`
}


File: /mikrotik\resource_wireless_interface_test.go
package mikrotik

import (
	"fmt"
	"testing"

	"github.com/ddelnano/terraform-provider-mikrotik/client"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/acctest"
	"github.com/hashicorp/terraform-plugin-sdk/v2/helper/resource"
)

func TestWirelessInterface_basic(t *testing.T) {
	// This test is skipped, until we find a way to include required packages.
	//
	// Since RouterOS 7.13, 'wireless' package is separate from the main system package
	// and there is no easy way to install it in Docker during tests.
	// see https://help.mikrotik.com/docs/spaces/ROS/pages/40992872/Packages#Packages-RouterOSpackages
	client.SkipIfRouterOSV7OrLater(t, sysResources)

	resourceName := "mikrotik_wireless_interface.testacc"
	name := acctest.RandomWithPrefix("ssid")
	resource.Test(t,
		resource.TestCase{
			ProtoV5ProviderFactories: testAccProtoV5ProviderFactories,
			Steps: []resource.TestStep{
				{
					Config: fmt.Sprintf(`
					resource "mikrotik_wireless_interface" "testacc" {
						name = %q
						mode = %q
						ssid = %q
						vlan_id = 2
						hide_ssid = false
						master_interface = "*0"
					}`, name, client.WirelessInterfaceModeAPBridge, name+"-ssid"),

					Check: resource.ComposeAggregateTestCheckFunc(
						resource.TestCheckResourceAttrSet(resourceName, "id"),
						resource.TestCheckResourceAttr(resourceName, "name", name),
						resource.TestCheckResourceAttr(resourceName, "disabled", "true"),
						resource.TestCheckResourceAttr(resourceName, "mode", client.WirelessInterfaceModeAPBridge),
						resource.TestCheckResourceAttr(resourceName, "ssid", name+"-ssid"),
						resource.TestCheckResourceAttr(resourceName, "hide_ssid", "false"),
						resource.TestCheckResourceAttr(resourceName, "vlan_id", "2"),
					),
				},
				{
					Config: fmt.Sprintf(`
					resource mikrotik_wireless_interface testacc {
						name = %q
						mode = %q
						disabled = false
						ssid = %q
						hide_ssid = true
						master_interface = "*0"
					}`, name, client.WirelessInterfaceModeAPBridge, name+"-ssid"),

					Check: resource.ComposeAggregateTestCheckFunc(
						resource.TestCheckResourceAttrSet(resourceName, "id"),
						resource.TestCheckResourceAttr(resourceName, "name", name),
						resource.TestCheckResourceAttr(resourceName, "disabled", "false"),
						resource.TestCheckResourceAttr(resourceName, "mode", client.WirelessInterfaceModeAPBridge),
						resource.TestCheckResourceAttr(resourceName, "ssid", name+"-ssid"),
						resource.TestCheckResourceAttr(resourceName, "hide_ssid", "true"),
					),
				},
				{
					ImportState:       true,
					ImportStateVerify: true,
					ResourceName:      resourceName,
				},
			},
		},
	)
}


File: /README.md
# Mikrotik provider for Terraform 

## Intro

This is a terraform provider for managing resources on your RouterOS device. To see what resources and data sources are supported, please see the [documentation](https://registry.terraform.io/providers/ddelnano/mikrotik/latest/docs) on the terraform registry.

## Support

You can discuss any issues you have or feature requests in [Discord](https://discord.gg/ZpNq8ez).

## Donations

If you get value out this project and want to show your support you can find me on [patreon](https://www.patreon.com/ddelnano).

## Building provider locally

Requirements:
* [Go](https://go.dev/doc/install) >= 1.18
* [Terraform]() >= 0.14

To build the provider with `make`:
```shell
$ make build
```
which creates a `terraform-provider-mikrotik` binary in repository's root folder.

or build with `go` compiler:
```shell
$ go build -o terraform-provider-mikrotik
```

To use locally built provider, Terraform should be aware of its binary.

It could be done with custom CLI config file:
```hcl
# custom.tfrc

provider_installation {
    dev_overrides {
        "ddelnano/mikrotik" = "/path/to/clones/repository/terraform-provider-mikrotik"
    }

    direct {}
}
```
The [dev_overrides](https://developer.hashicorp.com/terraform/cli/config/config-file#development-overrides-for-provider-developers) section is available since Terraform `0.14`.

Finally, tell Terraform CLI to use custom confiuration by exporting environment variable:
```shell
$ export TF_CLI_CONFIG_FILE=path/to/custom.tfrc
```

**NOTE**: with `dev_overrides` it is not possible to run `terraform init` (see [official docs](https://developer.hashicorp.com/terraform/cli/config/config-file#development-overrides-for-provider-developers)) so you should immediately use `terraform plan` and `terraform apply` without initializing.

## Contributing

### Dependencies
- RouterOS. See which versions are supported by what is tested in [CI](.github/workflows/continuous-integration.yml)
- Terraform 0.12+


For code generation of boilerplate code, see [codegen Readme](./cmd/mikrotik-codegen/internal/codegen/README.md)

### Testing

The provider is tested with Terraform's acceptance testing framework. As long as you have a RouterOS device you should be able to run them. Please be aware it will create resources on your device! Code that is accepted by the project will not be destructive for anything existing on your router but be careful when changing test code!

In order to run the tests you will need to set the following environment variables:
```bash
export MIKROTIK_HOST=router-hostname:8728
export MIKROTIK_USER=username
# Please be aware this will put your password in your bash history and is not safe
export MIKROTIK_PASSWORD=password
```

After those environment variables are set you can run the tests with the following command:
```bash
make testacc
```

### Testing without MikroTik hardware

If you do not have MikroTik hardware or virtual machine with pre-installed RouterOS, you still have a way to run tests locally.

To make this happen, install [Docker](https://www.docker.com) on your developer machine, and run from the root of the repository:
```sh
$ make routeros
```
It will start RouterOS container locally and make its API server available at `127.0.0.1:8728`

Just export connection settings
```sh
export MIKROTIK_HOST=127.0.0.1:8728
export MIKROTIK_USER=admin
export MIKROTIK_PASSWORD=""
```

and you are ready to run tests with
```sh
$ make test
```

You can use specific RouterOS version by passing `ROUTEROS_VERSION` argument
```sh
$ make routeros ROUTEROS_VERSION="6.49beta54"
```

or even
```sh
$ make routeros ROUTEROS_VERSION=latest
```

To cleanup everything, just run:
```sh
$ make routeros-clean
```


File: /templates\index.md.tmpl
---
page_title: "Provider: Mikrotik"
description: |-
  The mikrotik provider is used to interact with the resources supported by RouterOS.
---

# {{ .ProviderShortName | upper }} Provider

The mikrotik provider is used to interact with the resources supported by RouterOS.
The provider needs to be configured with the proper credentials before it can be used.

## Requirements

* RouterOS v6.45.2+ (It may work with other versions but it is untested against other versions!)


{{ if .HasExample -}}
## Example Usage
{{ tffile .ExampleFile }}
{{- end }}

{{ .SchemaMarkdown | trimspace }}


File: /templates\resources\bgp_instance.md.tmpl
# {{.Name}} ({{.Type}})
{{ .Description | trimspace }}

!> This resource will not be supported in RouterOS v7+.
Mikrotik has deprecated the underlying commands so future BGP support will need new resources created
(See [this issue](https://github.com/ddelnano/terraform-provider-mikrotik/issues/52) for status of this work).

{{ if .HasExample -}}
## Example Usage
{{ tffile .ExampleFile }}
{{- end }}

{{ .SchemaMarkdown | trimspace }}

{{ if .HasImport -}}
## Import
Import is supported using the following syntax:
{{ codefile "shell" .ImportFile }}
{{- end }}


File: /templates\resources\bgp_peer.md.tmpl
# {{.Name}} ({{.Type}})
{{ .Description | trimspace }}

!> This resource will not be supported in RouterOS v7+.
Mikrotik has deprecated the underlying commands so future BGP support will need new resources created
(See [this issue](https://github.com/ddelnano/terraform-provider-mikrotik/issues/52) for status of this work).

{{ if .HasExample -}}
## Example Usage
{{ tffile .ExampleFile }}
{{- end }}

{{ .SchemaMarkdown | trimspace }}

{{ if .HasImport -}}
## Import
Import is supported using the following syntax:
{{ codefile "shell" .ImportFile }}
{{- end }}


File: /templates\resources.md.tmpl
# {{.Name}} ({{.Type}})
{{ .Description | trimspace }}

{{ if .HasExample -}}
## Example Usage
{{ tffile .ExampleFile }}
{{- end }}

{{ .SchemaMarkdown | trimspace }}

{{ if .HasImport -}}
## Import
Import is supported using the following syntax:
{{ codefile "shell" .ImportFile }}
{{- end }}


File: /tools\tools.go
//go:build tools
// +build tools

package tools

import (
	_ "github.com/ddelnano/terraform-provider-mikrotik/cmd/mikrotik-codegen/internal/codegen"
	_ "github.com/hashicorp/terraform-plugin-docs/cmd/tfplugindocs"
)


