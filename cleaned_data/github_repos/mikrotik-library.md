# Repository Information
Name: mikrotik-library

# Directory Structure
Directory structure:
└── github_repos/mikrotik-library/
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
    │   │       ├── pack-f8e195354d3d077f62c24b4b6d607bed59839605.idx
    │   │       └── pack-f8e195354d3d077f62c24b4b6d607bed59839605.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── composer.json
    └── src/
        ├── config/
        │   └── mikrotik.php
        ├── Facades/
        │   ├── MikrotikFacade.php
        │   └── RouterosFacade.php
        ├── Libs/
        │   ├── mikrotik/
        │   │   ├── core/
        │   │   │   ├── mapi_core.php
        │   │   │   ├── mapi_error.php
        │   │   │   ├── mapi_query.php
        │   │   │   ├── mapi_routerosapi.php
        │   │   │   └── read_me.txt
        │   │   ├── file/
        │   │   │   └── mapi_file.php
        │   │   ├── interface/
        │   │   │   ├── mapi_interfaces.php
        │   │   │   ├── mapi_interface_bonding.php
        │   │   │   ├── mapi_interface_bridge.php
        │   │   │   ├── mapi_interface_eoip.php
        │   │   │   ├── mapi_interface_ethernet.php
        │   │   │   ├── mapi_interface_ipip.php
        │   │   │   ├── mapi_interface_l2tp_client.php
        │   │   │   ├── mapi_interface_l2tp_server.php
        │   │   │   ├── mapi_interface_pppoe_client.php
        │   │   │   ├── mapi_interface_pppoe_server.php
        │   │   │   ├── mapi_interface_ppp_client.php
        │   │   │   ├── mapi_interface_ppp_server.php
        │   │   │   ├── mapi_interface_pptp_client.php
        │   │   │   ├── mapi_interface_pptp_server.php
        │   │   │   ├── mapi_interface_vlan.php
        │   │   │   └── mapi_interface_vrrp.php
        │   │   ├── ip/
        │   │   │   ├── mapi_ip.php
        │   │   │   ├── mapi_ip_accounting.php
        │   │   │   ├── mapi_ip_address.php
        │   │   │   ├── mapi_ip_arp.php
        │   │   │   ├── mapi_ip_dhcp_client.php
        │   │   │   ├── mapi_ip_dhcp_relay.php
        │   │   │   ├── mapi_ip_dhcp_server.php
        │   │   │   ├── mapi_ip_dns.php
        │   │   │   ├── mapi_ip_firewall.php
        │   │   │   ├── mapi_ip_hotspot.php
        │   │   │   ├── mapi_ip_pool.php
        │   │   │   ├── mapi_ip_proxy.php
        │   │   │   ├── mapi_ip_route.php
        │   │   │   └── mapi_ip_service.php
        │   │   ├── ppp/
        │   │   │   ├── mapi_ppp.php
        │   │   │   ├── mapi_ppp_aaa.php
        │   │   │   ├── mapi_ppp_active.php
        │   │   │   ├── mapi_ppp_profile.php
        │   │   │   └── mapi_ppp_secret.php
        │   │   └── system/
        │   │       ├── mapi_curl.php
        │   │       ├── mapi_system.php
        │   │       ├── mapi_system_checker.php
        │   │       └── mapi_system_scheduler.php
        │   └── pear2/
        │       │   ├── mikrotik.iml
        │       │   ├── misc.xml
        │       │   ├── modules.xml
        │       │   ├── php.xml
        │       │   ├── vcs.xml
        │       │   └── workspace.xml
        │       ├── composer.json
        │       ├── index.php
        │       └── vendor/
        │           ├── autoload.php
        │           ├── bin/
        │           │   ├── roscon.php
        │           │   └── roscon.php.bat
        │           ├── composer/
        │           │   ├── autoload_classmap.php
        │           │   ├── autoload_namespaces.php
        │           │   ├── autoload_psr4.php
        │           │   ├── autoload_real.php
        │           │   ├── autoload_static.php
        │           │   ├── ClassLoader.php
        │           │   ├── installed.json
        │           │   └── LICENSE
        │           └── pear2/
        │               ├── cache_shm/
        │               │   ├── .gitignore
        │               │   ├── .scrutinizer.yml
        │               │   ├── composer.json
        │               │   ├── CREDITS
        │               │   ├── docs/
        │               │   │   ├── apigen.neon
        │               │   │   ├── doxygen.ini
        │               │   │   └── phpdoc.dist.xml
        │               │   ├── extrasetup.php
        │               │   ├── package.xml
        │               │   ├── packagexmlsetup.php
        │               │   ├── README
        │               │   ├── README.md
        │               │   ├── RELEASE-0.1.0
        │               │   ├── RELEASE-0.1.1
        │               │   ├── RELEASE-0.1.2
        │               │   ├── RELEASE-0.1.3
        │               │   ├── RELEASE-0.2.0
        │               │   ├── src/
        │               │   │   └── PEAR2/
        │               │   │       └── Cache/
        │               │   │           ├── SHM/
        │               │   │           │   ├── Adapter/
        │               │   │           │   │   ├── APC.php
        │               │   │           │   │   ├── APCu.php
        │               │   │           │   │   ├── Placebo.php
        │               │   │           │   │   └── Wincache.php
        │               │   │           │   ├── Exception.php
        │               │   │           │   └── InvalidArgumentException.php
        │               │   │           └── SHM.php
        │               │   ├── stub.php
        │               │   └── tests/
        │               │       ├── bootstrap.php
        │               │       ├── PHPT/
        │               │       │   ├── APC.phpt
        │               │       │   ├── APCu.phpt
        │               │       │   ├── Common/
        │               │       │   │   ├── testAddingTtlValue_part1.phpt
        │               │       │   │   ├── testAddingTtlValue_part2.phpt
        │               │       │   │   ├── testAddingTtlValue_part3.phpt
        │               │       │   │   ├── testAddingValue.phpt
        │               │       │   │   ├── testSettingAndDeletingValue.phpt
        │               │       │   │   ├── testSettingAndGettingValue.phpt
        │               │       │   │   └── testSingleFileLockAndUnlock.phpt
        │               │       │   ├── includes/
        │               │       │   │   ├── runner.php
        │               │       │   │   └── SHM-factory.php
        │               │       │   ├── Placebo.phpt
        │               │       │   ├── SHM-factory_CGI.phpt
        │               │       │   ├── SHM-factory_CLI.phpt
        │               │       │   └── Wincache.phpt
        │               │       └── phpunit.xml
        │               ├── console_commandline/
        │               │   ├── .gitignore
        │               │   ├── .travis.yml
        │               │   ├── composer.json
        │               │   ├── CREDITS
        │               │   ├── data/
        │               │   │   └── xmlschema.rng
        │               │   ├── examples/
        │               │   │   ├── ex1.php
        │               │   │   ├── ex2.php
        │               │   │   ├── ex2.xml
        │               │   │   ├── ex3.php
        │               │   │   ├── ex4.php
        │               │   │   └── ex4.xml
        │               │   ├── extrasetup.php
        │               │   ├── package.xml
        │               │   ├── packagexmlsetup.php
        │               │   ├── README
        │               │   ├── RELEASE-0.1.0
        │               │   ├── RELEASE-0.2.0
        │               │   ├── RELEASE-0.2.1
        │               │   ├── RELEASE-0.2.2
        │               │   ├── RELEASE-0.2.3
        │               │   ├── src/
        │               │   │   └── PEAR2/
        │               │   │       └── Console/
        │               │   │           ├── CommandLine/
        │               │   │           │   ├── Action/
        │               │   │           │   │   ├── Callback.php
        │               │   │           │   │   ├── Counter.php
        │               │   │           │   │   ├── Help.php
        │               │   │           │   │   ├── List.php
        │               │   │           │   │   ├── Password.php
        │               │   │           │   │   ├── StoreArray.php
        │               │   │           │   │   ├── StoreFalse.php
        │               │   │           │   │   ├── StoreFloat.php
        │               │   │           │   │   ├── StoreInt.php
        │               │   │           │   │   ├── StoreString.php
        │               │   │           │   │   ├── StoreTrue.php
        │               │   │           │   │   └── Version.php
        │               │   │           │   ├── Action.php
        │               │   │           │   ├── Argument.php
        │               │   │           │   ├── Command.php
        │               │   │           │   ├── CustomMessageProvider.php
        │               │   │           │   ├── Element.php
        │               │   │           │   ├── Exception.php
        │               │   │           │   ├── MessageProvider/
        │               │   │           │   │   └── DefaultProvider.php
        │               │   │           │   ├── MessageProvider.php
        │               │   │           │   ├── Option.php
        │               │   │           │   ├── Outputter/
        │               │   │           │   │   └── Default.php
        │               │   │           │   ├── Outputter.php
        │               │   │           │   ├── Renderer/
        │               │   │           │   │   └── Default.php
        │               │   │           │   ├── Renderer.php
        │               │   │           │   ├── Result.php
        │               │   │           │   └── XmlParser.php
        │               │   │           └── CommandLine.php
        │               │   └── tests/
        │               │       ├── console_commandline_accept.phpt
        │               │       ├── console_commandline_addargument.phpt
        │               │       ├── console_commandline_addargument2.phpt
        │               │       ├── console_commandline_addcommand.phpt
        │               │       ├── console_commandline_addcommand_3.phpt
        │               │       ├── console_commandline_addoption.phpt
        │               │       ├── console_commandline_addoption_errors_1.phpt
        │               │       ├── console_commandline_addoption_errors_2.phpt
        │               │       ├── console_commandline_addoption_errors_3.phpt
        │               │       ├── console_commandline_addoption_errors_4.phpt
        │               │       ├── console_commandline_addoption_errors_5.phpt
        │               │       ├── console_commandline_addoption_errors_6.phpt
        │               │       ├── console_commandline_addoption_errors_7.phpt
        │               │       ├── console_commandline_bug18682.phpt
        │               │       ├── console_commandline_fromxmlfile.phpt
        │               │       ├── console_commandline_fromxmlfile_error.phpt
        │               │       ├── console_commandline_fromxmlstring.phpt
        │               │       ├── console_commandline_options_defaults.phpt
        │               │       ├── console_commandline_parse_1.phpt
        │               │       ├── console_commandline_parse_10.phpt
        │               │       ├── console_commandline_parse_11.phpt
        │               │       ├── console_commandline_parse_12.phpt
        │               │       ├── console_commandline_parse_13.phpt
        │               │       ├── console_commandline_parse_14.phpt
        │               │       ├── console_commandline_parse_15.phpt
        │               │       ├── console_commandline_parse_16.phpt
        │               │       ├── console_commandline_parse_17.phpt
        │               │       ├── console_commandline_parse_18.phpt
        │               │       ├── console_commandline_parse_19.phpt
        │               │       ├── console_commandline_parse_2.phpt
        │               │       ├── console_commandline_parse_20.phpt
        │               │       ├── console_commandline_parse_21.phpt
        │               │       ├── console_commandline_parse_22.phpt
        │               │       ├── console_commandline_parse_23.phpt
        │               │       ├── console_commandline_parse_24.phpt
        │               │       ├── console_commandline_parse_25.phpt
        │               │       ├── console_commandline_parse_26.phpt
        │               │       ├── console_commandline_parse_27.phpt
        │               │       ├── console_commandline_parse_28.phpt
        │               │       ├── console_commandline_parse_29.phpt
        │               │       ├── console_commandline_parse_3.phpt
        │               │       ├── console_commandline_parse_4.phpt
        │               │       ├── console_commandline_parse_5.phpt
        │               │       ├── console_commandline_parse_6.phpt
        │               │       ├── console_commandline_parse_7.phpt
        │               │       ├── console_commandline_parse_8.phpt
        │               │       ├── console_commandline_parse_9.phpt
        │               │       ├── console_commandline_webrequest_1.phpt
        │               │       ├── console_commandline_webrequest_2.phpt
        │               │       ├── console_commandline_webrequest_3.phpt
        │               │       ├── test.xml
        │               │       └── tests.inc.php
        │               └── net_routeros/
        │                   ├── .gitmodules
        │                   ├── composer.json
        │                   ├── data/
        │                   │   └── roscon.xml
        │                   ├── scripts/
        │                   │   ├── roscon
        │                   │   ├── roscon.bat
        │                   │   └── roscon.php
        │                   ├── src/
        │                   │   └── PEAR2/
        │                   │       └── Net/
        │                   │           └── RouterOS/
        │                   │               ├── Client.php
        │                   │               ├── Communicator.php
        │                   │               ├── DataFlowException.php
        │                   │               ├── Exception.php
        │                   │               ├── InvalidArgumentException.php
        │                   │               ├── LengthException.php
        │                   │               ├── Message.php
        │                   │               ├── NotSupportedException.php
        │                   │               ├── ParserException.php
        │                   │               ├── Query.php
        │                   │               ├── Registry.php
        │                   │               ├── Request.php
        │                   │               ├── Response.php
        │                   │               ├── ResponseCollection.php
        │                   │               ├── RouterErrorException.php
        │                   │               ├── Script.php
        │                   │               ├── SocketException.php
        │                   │               ├── UnexpectedValueException.php
        │                   │               └── Util.php
        │                   └── stub.php
        ├── MikrotikServiceProvider.php
        └── Services/
            ├── Mikrotik.php
            └── Routeros.php


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
	url = https://github.com/jewel-rana/mikrotik-library.git
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
0000000000000000000000000000000000000000 cfea10fbcb69743399307366a13570dd5dc8afc4 vivek-dodia <vivek.dodia@icloud.com> 1738606300 -0500	clone: from https://github.com/jewel-rana/mikrotik-library.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 cfea10fbcb69743399307366a13570dd5dc8afc4 vivek-dodia <vivek.dodia@icloud.com> 1738606300 -0500	clone: from https://github.com/jewel-rana/mikrotik-library.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 cfea10fbcb69743399307366a13570dd5dc8afc4 vivek-dodia <vivek.dodia@icloud.com> 1738606300 -0500	clone: from https://github.com/jewel-rana/mikrotik-library.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
cfea10fbcb69743399307366a13570dd5dc8afc4 refs/remotes/origin/master


File: /.git\refs\heads\master
cfea10fbcb69743399307366a13570dd5dc8afc4


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /composer.json
{
    "name": "rajtika/mikrotik",
    "description": "Mikrotik router management through pear2 library",
    "type": "library",
    "license": "MIT",
    "authors": [
        {
            "name": "Jewel Rana",
            "email": "jewelrana.dev@gmail.com"
        }
    ],
    "minimum-stability": "dev",
    "require": {
        "pear2/net_routeros": "*@beta",
        "pear2/cache_shm": "*@alpha",
        "pear2/console_commandline": "*@alpha",
        "pear2/console_color": "dev-master"
    }
}


File: /src\config\mikrotik.php
<?php
return [
    'host' => '123.253.96.22', // Mikrotik Public IP
    'port' => '8728',
    'user' => 'api_user',
    'password' => '#System:Users.C',
    'service' => 'pppoe'
];


File: /src\Facades\MikrotikFacade.php
<?php
namespace Rajtika\Mikrotik\Facades;

use Illuminate\Support\Facades\Facade;

/**
 * Class ShoppingCartFacade
 * @package LaraShout\ShoppingCart
 */
class MikrotikFacade extends Facade
{
    /**
     * @return string
     */
    protected static function getFacadeAccessor()
    {
        return 'mikrotik';
    }
}


File: /src\Facades\RouterosFacade.php
<?php
namespace Rajtika\Mikrotik\Facades;

use Illuminate\Support\Facades\Facade;

/**
 * Class ShoppingCartFacade
 * @package LaraShout\ShoppingCart
 */
class RouterosFacade extends Facade
{
    /**
     * @return string
     */
    protected static function getFacadeAccessor()
    {
        return 'routeros';
    }
}


File: /src\Libs\mikrotik\core\mapi_core.php
<?php
/**
 * @author Denis Basta denis.basta@gmail.com
 * 
 * Revised By Nick Barner 
 * read() function altered to take into account 
 * the placing of the "!done" reply and also 
 * correct calculation of the reply length.
 * 
 * Revised By Ben Menking ben@infotechsc.com 
 * read() function altered removed echo 
 * statement that dumped byte data to screen
 * 
 * Revised By Jeremy Jefferson <http://jeremyj.com/>
 * January 8, 2010,  Fixed write function in 
 * order to allow for queries to be executed
 * 
 * Revised By Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * Create constructur for integrating with codeigniter
 * and added isset Response in function connect
 * 
 * Revised By Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * Change function encode_length from useing if code to switch code
 * and change class name from Routeros_api to Mapi_Core
 * 
 * @category    Library
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @access  protected
 * 
 */
class Mapi_Core {
        /**
         *
         * @var type array
         */
        private $param;
        
        /**
         *
         * @var type int
         */
	private $error_no;				// Variable for storing connection error number, if any
	/**
         *
         * @var type string
         */
        private $error_str;				// Variable for storing connection error text, if any
	
        /**
         *
         * @var type boolean
         */
        private $connected = false;                 // Connection state
	
        /**
         *
         * @var type mixed
         */
        private $socket;				// Variable for storing socket resource

        /**
         *
         * @param type $param 
         */
        function __construct($param=array()) {
            $this->param = $param;
        }
	
        /**
         * @access protected
         * @param type $text string
         */
	private function debug($text) {
            if ($this->param['debug']) echo $text . "\n";
	}

        /**
         * @access protected
         * @param type $length
         * @return string 
         */
	private function encode_length($length) {
            switch ($length){
                case $length < 0x80 :
                    $length = chr($length);
                    break;
                case $length < 0x4000:
                    $length |= 0x8000;
                    $length = chr( ($length >> 8 ) & 0xFF) . chr($length & 0x0FF);
                    break;
                case $length < 200000:
                    $length |= 0xC00000;
                    $length = chr(($length >> 8) & 0xFF). chr(($length >> 8) & 0xFF). chr($length & 0xFF);
                    break;
                case $length < 0x10000000:
                    $length |= 0xE0000000;
                    $length = chr(($length >> 8) & 0xFF). chr(($length >> 8) & 0xFF). chr(($length >> 8) & 0xFF). chr($length & 0xFF);
                    break;
                case $length >= 0x10000000:
                    $length = character_limiter(0xF0). chr(($length >> 8) & 0xFF). chr(($length >> 8) & 0xFF). chr(($length >> 8) & 0xFF). chr($length & 0xFF);
                    break;   
            }
            return $length;
	}
        
        /**
         * @access protected
         * @return type boolean
         */
	function connect() {
            for ($ATTEMPT = 1; $ATTEMPT <= $this->param['attempts']; $ATTEMPT++) {
                $this->connected = false;
                $this->debug('Connection attempt #' . $ATTEMPT . ' to ' . $this->param['host'] . ':' . $this->param['port'] . '...');
                if ($this->socket = @fsockopen($this->param['host'], $this->param['port'], $this->error_no, $this->error_str, $this->param['timeout']) ) {
                    socket_set_timeout($this->socket, $this->param['timeout']);
                    $this->write('/login');
                    $RESPONSE = $this->read(false);
                    if ($RESPONSE[0] == '!done') {
                        if (isset($RESPONSE[1])){
                            if (preg_match_all('/[^=]+/i', $RESPONSE[1], $MATCHES) ) {
                                if ($MATCHES[0][0] == 'ret' && strlen($MATCHES[0][1]) == 32) {
                                    $this->write('/login', false);
                                    $this->write('=name=' . $this->param['username'], false);
                                    $this->write('=response=00' . md5(chr(0) . $this->param['password'] . pack('H*', $MATCHES[0][1]) ) );
                                    $RESPONSE = $this->read(false);
                                    if (isset ($RESPONSE[0])){
                                    if ($RESPONSE[0] == '!done') {
                                        $this->connected = true;
                                        break;
                                        }
                                    }
                                }
                            }
                        }
                    }
                            fclose($this->socket);
                    }
                    sleep($this->param['delay']);
            }

            if ($this->connected) $this->debug('Connected...'); else $this->debug('Error...');
            return $this->connected;
	}

        
        /**
         *  @access protected
         */
	public function disconnect() {
		fclose($this->socket);
		$this->connected = false;
		$this->debug('Disconnected...');
	}
        
        /** 
         * @access protected
         * @param type $response mixed
         * @return array 
         */
	private function parse_response($response) {
		if (is_array($response) ) {
			$PARSED = array();
			$CURRENT = null;
			foreach ($response as $x) {
				if (in_array($x, array('!fatal', '!re', '!trap') ) ) {
					if ($x == '!re')
						$CURRENT = &$PARSED[];
					else
						$CURRENT = &$PARSED[$x][];
				} else if ($x != '!done') {
					if (preg_match_all('/[^=]+/i', $x, $MATCHES) )
						$CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
				}
			}
			return $PARSED;
		}else {
			return array();
                }
	}
        
        /**
         * @access protected
         * @param type $array array
         * @return type 
         */
        private function array_change_key_name(&$array) {
                if (is_array($array) ) {
                        foreach ($array as $k => $v) {
                                $tmp = str_replace("-","_",$k);
                                $tmp = str_replace("/","_",$tmp);
                                if ($tmp) {
                                        $array_new[$tmp] = $v;
                                } else {
                                        $array_new[$k] = $v;
                                }
                        }
                        return $array_new;
                } else {
                        return $array;
                }
        }

        /**
         * @access protected
         * @param type $response mixed
         * @return type array
         */
        private function parse_response4smarty($response) {
                if (is_array($response) ) {
                        $PARSED = array();
                        $CURRENT = null;
                        foreach ($response as $x) {
                                if (in_array($x, array('!fatal', '!re', '!trap') ) ) {
                                        if ($x == '!re')
                                                $CURRENT = &$PARSED[];
                                        else
                                                $CURRENT = &$PARSED[$x][];
                                }
                                else
                                if ($x != '!done') {
                                        if (preg_match_all('/[^=]+/i', $x, $MATCHES) )
                                                $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                                }
                        }
                        foreach ($PARSED as $key => $value) {
                                $PARSED[$key] = $this->array_change_key_name($value);
                        }
                        return $PARSED;
                }
                else {
                        return array();
                }
        }

       /**
        * @access protected
        * @param type $parse boolean
        * @return type mixed
        */
       function read($parse = true) {

          $RESPONSE = array();

          while (true) {

             // Read the first byte of input which gives us some or all of the length
             // of the remaining reply.
             $BYTE = ord(fread($this->socket, 1) );
             $LENGTH = 0;

             // If the first bit is set then we need to remove the first four bits, shift left 8
             // and then read another byte in.
             // We repeat this for the second and third bits.
             // If the fourth bit is set, we need to remove anything left in the first byte
             // and then read in yet another byte.
             if ($BYTE & 128) {
                if (($BYTE & 192) == 128) {
                   $LENGTH = (($BYTE & 63) << 8 ) + ord(fread($this->socket, 1)) ;
                } else {
                   if (($BYTE & 224) == 192) {
                      $LENGTH = (($BYTE & 31) << 8 ) + ord(fread($this->socket, 1)) ;
                      $LENGTH = ($LENGTH << 8 ) + ord(fread($this->socket, 1)) ;
                   } else {
                      if (($BYTE & 240) == 224) {
                         $LENGTH = (($BYTE & 15) << 8 ) + ord(fread($this->socket, 1)) ;
                         $LENGTH = ($LENGTH << 8 ) + ord(fread($this->socket, 1)) ;
                         $LENGTH = ($LENGTH << 8 ) + ord(fread($this->socket, 1)) ;
                      } else {
                         $LENGTH = ord(fread($this->socket, 1)) ;
                         $LENGTH = ($LENGTH << 8 ) + ord(fread($this->socket, 1)) ;
                         $LENGTH = ($LENGTH << 8 ) + ord(fread($this->socket, 1)) ;
                         $LENGTH = ($LENGTH << 8 ) + ord(fread($this->socket, 1)) ;
                      }
                   }
                }
             } else {
                $LENGTH = $BYTE;
             }

             // If we have got more characters to read, read them in.
             $note = "";
             if ($LENGTH > 0) {

                $retlen=0;
                while ($retlen < $LENGTH) {
                   $toread = $LENGTH - $retlen ;
                   $note .= fread($this->socket, $toread);
                   $retlen = strlen($note);
                }
                $RESPONSE[] = $note ;
                $this->debug('>>> [' . $retlen . '/' . $LENGTH . ' bytes read.');
             }

             // If we get a !done, make a note of it.
             if ($note == "!done")
                $receiveddone=true;

             $STATUS = socket_get_status($this->socket);


             if ($LENGTH > 0)
                $this->debug('>>> [' . $LENGTH . ', ' . $STATUS['unread_bytes'] . '] ' . $note);

             if ( (!$this->connected && !$STATUS['unread_bytes']) ||
                ($this->connected && !$STATUS['unread_bytes'] && isset ($receiveddone)))
                break;

          }

          if ($parse)
             $RESPONSE = $this->parse_response($RESPONSE);

          return $RESPONSE;

       }
	
       /**
        * @access protected
        * @param type $command string
        * @param type $param2 boolean
        * @return type mixed
        */
       function write($command, $param2 = true) {
                if ($command) {
                    $data = explode("\n",$command);
                    foreach ($data as $com) {
                        $com = trim($com);
                        fwrite($this->socket, $this->encode_length(strlen($com) ) . $com);
                        $this->debug('<<< [' . strlen($com) . '] ' . $com);
                    }

                    if (gettype($param2) == 'integer') {
                        fwrite($this->socket, $this->encode_length(strlen('.tag=' . $param2) ) . '.tag=' . $param2 . chr(0) );
                        $this->debug('<<< [' . strlen('.tag=' . $param2) . '] .tag=' . $param2);
                    } else if (gettype($param2) == 'boolean'){
                        fwrite($this->socket, ($param2 ? chr(0) : '') );
                    }

                    return true;
                } else {
                    return false;
                }
        }

}



File: /src\Libs\mikrotik\core\mapi_error.php
<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');
class Apperror {
	protected $error;
	protected $code;
	public function __construct() {
		$this->error = array (
			601 => 'Sorry! Cannot validate the licence key. Please contact the provider ( <a href="http://rajtika.com" target="ext">here</a> ).',
			602 => 'Sorry! Your license is not valid.',
			603 => 'Sorry! Your license has expired.',
			604 => 'Sorry! Your license expired the demo period.',
			605 => 'Sorry! Your license is not valid.',
			606 => 'Sorry! Your license is not valid.',
			607 => 'Your licence of this product is not passed, please contact the provider ( <a href="http://rajtika.com" target="ext">here</a> ).',
			608 => 'Your trial period has end. Please purchase the licence <a href="http://rajtika.com" target="ext">here</a>'
		);
	}

	protected function err( $code = 601 ) {
		$msg = $this->error[$code];
		if( array_key_exists( $code, $this->error ) )
			die( $msg );
	}
}

File: /src\Libs\mikrotik\core\mapi_query.php
<?php

/**
 * Description of Mapi_Query
 * 
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 * @version     0.5.0
 */
class Mapi_Query extends Mapi_Core {
    /**
     * @access private
     * @var type array
     */
    private $param;

    /**
     * Instantiation
     * @param type $param array
     */
    function __construct($param=array()) {
        $this->param = $param;
        parent::__construct($param); //Mikrotik_Api_Core
    }
    
    /**
     * @access protected
     * @param type $param string/array
     * @return boolean 
     */
    function query($param){
        $out='';
        if ($this->connect()){
            $out= $this->__build($param);
            $this->disconnect();
        } else {
            $out = FALSE;
        }
        return $out;
    }
    
    /**
     * @access protected
     * @param type $param array
     * @return type array
     */
    private function __build($param){
        $tmp='';
        if (!is_array($param)){
             $tmp=explode('/', $param);
        } else {
             $tmp=explode('/', $param['command']);
        }
       
        $tmp_count=count($tmp);
        $last_command=$tmp[$tmp_count-1];
        
        //write check
        if (is_array($param)){
             $count = count($param);
             $i=0;
             foreach ($param as $key => $value){
                 $status=FALSE;
                 if ($i==$count-1){
                     $status=TRUE;
                 } 
                 if ($key=='command'){
                     $this->write($value,false);
                 } else {
                     if ($key=='id'){
                         if ($last_command=="print"){
                                $this->write('?.'.$key.'='.$value, $status);
                         } else {
                                $this->write('=.'.$key.'='.$value, $status);
                         }  
                     } else {
                         $this->write('='.$key.'='.$value,$status);
                     }
                 }            
                 $i++;
             }
        } else {
            $this->write($param);
        }
        
        $r_status='';
        if ($last_command=="print"||$last_command=="getall"){
            $r_status=TRUE;
        } else {
            $r_status=FALSE;
        }
        
        return $this->read($r_status);
    }

}

File: /src\Libs\mikrotik\core\mapi_routerosapi.php
<?php
/*****************************
 *
 * RouterOS PHP API class v1.6
 * Author: Denis Basta
 * Contributors:
 *    Nick Barnes
 *    Ben Menking (ben [at] infotechsc [dot] com)
 *    Jeremy Jefferson (http://jeremyj.com)
 *    Cristian Deluxe (djcristiandeluxe [at] gmail [dot] com)
 *    Mikhail Moskalev (mmv.rus [at] gmail [dot] com)
 *
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 ******************************/

class RouterosAPI
{
    var $debug     = false; //  Show debug information
    var $connected = false; //  Connection state
    var $host;
    var $port      = 8728;  //  Port to connect to (default 8729 for ssl)
    var $user;
    var $password;
    var $ssl       = false; //  Connect using SSL (must enable api-ssl in IP/Services)
    var $timeout   = 3;     //  Connection attempt timeout and data read timeout
    var $attempts  = 5;     //  Connection attempt count
    var $delay     = 3;     //  Delay between connection attempts in seconds

    var $socket;            //  Variable for storing socket resource
    var $error_no;          //  Variable for storing connection error number, if any
    var $error_str;         //  Variable for storing connection error text, if any

    /* Check, can be var used in foreach  */
    public function isIterable($var)
    {
        return $var !== null
            && (is_array($var)
                || $var instanceof Traversable
                || $var instanceof Iterator
                || $var instanceof IteratorAggregate
            );
    }

    /**
     * Print text for debug purposes
     *
     * @param string      $text       Text to print
     *
     * @return void
     */
    public function debug($text)
    {
        if ($this->debug) {
            echo $text . "\n";
        }
    }


    /**
     *
     *
     * @param string        $length
     *
     * @return void
     */
    public function encodeLength($length)
    {
        if ($length < 0x80) {
            $length = chr($length);
        } elseif ($length < 0x4000) {
            $length |= 0x8000;
            $length = chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x200000) {
            $length |= 0xC00000;
            $length = chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x10000000) {
            $length |= 0xE0000000;
            $length = chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length >= 0x10000000) {
            $length = chr(0xF0) . chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        }

        return $length;
    }


    /**
     * Login to RouterOS
     *
     * @return boolean                If we are connected or not
     */
    public function connect()
    {
        for ($ATTEMPT = 1; $ATTEMPT <= $this->attempts; $ATTEMPT++) {
            $this->connected = false;
            $PROTOCOL = ($this->ssl ? 'ssl://' : '' );
            $context = stream_context_create(array('ssl' => array('ciphers' => 'ADH:ALL', 'verify_peer' => false, 'verify_peer_name' => false)));
            $this->debug('Connection attempt #' . $ATTEMPT . ' to ' . $PROTOCOL . $this->host . ':' . $this->port . '...');
            $this->socket = @stream_socket_client($PROTOCOL . $this->host .':'. $this->port, $this->error_no, $this->error_str, $this->timeout, STREAM_CLIENT_CONNECT,$context);
            if ($this->socket) {
                socket_set_timeout($this->socket, $this->timeout);
                $this->write('/login', false);
                $this->write('=name=' . $this->user, false);
                $this->write('=password=' . $this->password);
                $RESPONSE = $this->read(false);
                if (isset($RESPONSE[0])) {
                    if ($RESPONSE[0] == '!done') {
                        if (!isset($RESPONSE[1])) {
                            // Login method post-v6.43
                            $this->connected = true;
                            break;
                        } else {
                            // Login method pre-v6.43
                            $MATCHES = array();
                            if (preg_match_all('/[^=]+/i', $RESPONSE[1], $MATCHES)) {
                                if ($MATCHES[0][0] == 'ret' && strlen($MATCHES[0][1]) == 32) {
                                    $this->write('/login', false);
                                    $this->write('=name=' . $this->user, false);
                                    $this->write('=response=00' . md5(chr(0) . $this->password . pack('H*', $MATCHES[0][1])));
                                    $RESPONSE = $this->read(false);
                                    if (isset($RESPONSE[0]) && $RESPONSE[0] == '!done') {
                                        $this->connected = true;
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
                fclose($this->socket);
            }
            sleep($this->delay);
        }

        if ($this->connected) {
            $this->debug('Connected...');
        } else {
            $this->debug('Error...');
        }
        return $this->connected;
    }


    /**
     * Disconnect from RouterOS
     *
     * @return void
     */
    public function disconnect()
    {
        // let's make sure this socket is still valid.  it may have been closed by something else
        if( is_resource($this->socket) ) {
            fclose($this->socket);
        }
        $this->connected = false;
        $this->debug('Disconnected...');
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }

            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }

            return $PARSED;
        } else {
            return array();
        }
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse4Smarty($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }
            foreach ($PARSED as $key => $value) {
                $PARSED[$key] = $this->arrayChangeKeyName($value);
            }
            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }
            return $PARSED;
        } else {
            return array();
        }
    }


    /**
     * Change "-" and "/" from array key to "_"
     *
     * @param array       $array      Input array
     *
     * @return array                  Array with changed key names
     */
    public function arrayChangeKeyName(&$array)
    {
        if (is_array($array)) {
            foreach ($array as $k => $v) {
                $tmp = str_replace("-", "_", $k);
                $tmp = str_replace("/", "_", $tmp);
                if ($tmp) {
                    $array_new[$tmp] = $v;
                } else {
                    $array_new[$k] = $v;
                }
            }
            return $array_new;
        } else {
            return $array;
        }
    }


    /**
     * Read data from Router OS
     *
     * @param boolean     $parse      Parse the data? default: true
     *
     * @return array                  Array with parsed or unparsed data
     */
    public function read($parse = true)
    {
        $RESPONSE     = array();
        $receiveddone = false;
        while (true) {
            // Read the first byte of input which gives us some or all of the length
            // of the remaining reply.
            $BYTE   = ord(fread($this->socket, 1));
            $LENGTH = 0;
            // If the first bit is set then we need to remove the first four bits, shift left 8
            // and then read another byte in.
            // We repeat this for the second and third bits.
            // If the fourth bit is set, we need to remove anything left in the first byte
            // and then read in yet another byte.
            if ($BYTE & 128) {
                if (($BYTE & 192) == 128) {
                    $LENGTH = (($BYTE & 63) << 8) + ord(fread($this->socket, 1));
                } else {
                    if (($BYTE & 224) == 192) {
                        $LENGTH = (($BYTE & 31) << 8) + ord(fread($this->socket, 1));
                        $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                    } else {
                        if (($BYTE & 240) == 224) {
                            $LENGTH = (($BYTE & 15) << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        } else {
                            $LENGTH = ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        }
                    }
                }
            } else {
                $LENGTH = $BYTE;
            }

            $_ = "";

            // If we have got more characters to read, read them in.
            if ($LENGTH > 0) {
                $_      = "";
                $retlen = 0;
                while ($retlen < $LENGTH) {
                    $toread = $LENGTH - $retlen;
                    $_ .= fread($this->socket, $toread);
                    $retlen = strlen($_);
                }
                $RESPONSE[] = $_;
                $this->debug('>>> [' . $retlen . '/' . $LENGTH . '] bytes read.');
            }

            // If we get a !done, make a note of it.
            if ($_ == "!done") {
                $receiveddone = true;
            }

            $STATUS = socket_get_status($this->socket);
            if ($LENGTH > 0) {
                $this->debug('>>> [' . $LENGTH . ', ' . $STATUS['unread_bytes'] . ']' . $_);
            }

            if ((!$this->connected && !$STATUS['unread_bytes']) || ($this->connected && !$STATUS['unread_bytes'] && $receiveddone)) {
                break;
            }
        }

        if ($parse) {
            $RESPONSE = $this->parseResponse($RESPONSE);
        }

        return $RESPONSE;
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $command    A string with the command to send
     * @param mixed       $param2     If we set an integer, the command will send this data as a "tag"
     *                                If we set it to boolean true, the funcion will send the comand and finish
     *                                If we set it to boolean false, the funcion will send the comand and wait for next command
     *                                Default: true
     *
     * @return boolean                Return false if no command especified
     */
    public function write($command, $param2 = true)
    {
        if ($command) {
            $data = explode("\n", $command);
            foreach ($data as $com) {
                $com = trim($com);
                fwrite($this->socket, $this->encodeLength(strlen($com)) . $com);
                $this->debug('<<< [' . strlen($com) . '] ' . $com);
            }

            if (gettype($param2) == 'integer') {
                fwrite($this->socket, $this->encodeLength(strlen('.tag=' . $param2)) . '.tag=' . $param2 . chr(0));
                $this->debug('<<< [' . strlen('.tag=' . $param2) . '] .tag=' . $param2);
            } elseif (gettype($param2) == 'boolean') {
                fwrite($this->socket, ($param2 ? chr(0) : ''));
            }

            return true;
        } else {
            return false;
        }
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $com        A string with the command to send
     * @param array       $arr        An array with arguments or queries
     *
     * @return array                  Array with parsed
     */
    public function comm($com, $arr = array())
    {
        $count = count($arr);
        $this->write($com, !$arr);
        $i = 0;
        if ($this->isIterable($arr)) {
            foreach ($arr as $k => $v) {
                switch ($k[0]) {
                    case "?":
                        $el = "$k=$v";
                        break;
                    case "~":
                        $el = "$k~$v";
                        break;
                    default:
                        $el = "=$k=$v";
                        break;
                }

                $last = ($i++ == $count - 1);
                $this->write($el, $last);
            }
        }

        return $this->read();
    }

    /**
     * Standard destructor
     *
     * @return void
     */
    public function __destruct()
    {
        $this->disconnect();
    }
}


File: /src\Libs\mikrotik\core\read_me.txt




1543604563

0

File: /src\Libs\mikrotik\file\mapi_file.php
<?php

/**
 * Description of Mapi_File
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */

class Mapi_File extends Mapi_Query {
    /**
     * @access private
     * @var type array
     */
    private $param;
    
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to display all file in mikrotik RouterOs
     * @return type array
     */
    public function get_all_file(){
        return $this->query('/file/getall');
    }
    
    /**
     * This method is used to display one file 
     * in detail based on the id
     * @param type $id string 
     * @return type array
     */
    public function detail_file($id){
        $input = array(
                    'command'       => '/file/print',
                    'id'            => $id    
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to delete file by id
     * @param type $id string
     * @return type array
     */
    public function delete_file($id){
        $input = array(
                'command'       => '/file/remove',
                'id'            => $id
        );
        return $this->query($input);
    }
}


File: /src\Libs\mikrotik\interface\mapi_interfaces.php
<?php

/**
 * Description of Mapi_Interfaces
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interfaces {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param = array()) {
        $this->param = $param;
    }
    
     /**
     * This method is used to call class Mapi_Interface_Ethetrnet
     * @return Mapi_Ip 
     */
    public function ethernet(){
        return new Mapi_Interface_Ethernet($this->param);
    }
    
    /**
     * This method is used to call class Mapi_Interface_Pppoe_Client
     * @return Mapi_Ip 
     */
    public function pppoe_client(){
        return new Mapi_Interface_Pppoe_Client($this->param);
    }
    
    /**
     * This method is used to call class Mapi_Interface_Pppoe_Server
     * @return Mapi_Ip 
     */
    public function pppoe_server(){
        return new Mapi_Interface_Pppoe_Server($this->param);
    }
    
    /**
     * This method is used to call class Mapi_Interface_Eoip
     * @return Mapi_Ip 
     */
    public function eoip(){
        return new Mapi_Interface_Eoip($this->param);
        
    }
    
    /**
     * This method is used to call class Mapi_Interface_Ipip
     * @return Mapi_Ip 
     */
    public function ipip(){
        return new Mapi_Interface_Ipip($this->param);
    }
    
    /**
     * This method is used to call class Mapi_Interface_Vlan
     * @return Mapi_Ip 
     */
    public function vlan(){
        return new Mapi_Interface_Vlan($this->param);
    }
    
    /**
     * This method is used to call class Mapi_Interface_Vrrp
     * @return Mapi_Ip 
     */
    public function vrrp(){
        return new Mapi_Interface_Vrrp($this->param);
    }
    
    /**
     * This method is used to call class Mapi_Interface_Bonding
     * @return Mapi_Ip 
     */
    public function bonding(){
        return new Mapi_Interface_Bonding($this->param);
    }
    
    /**
     * This method for used call class Mapi_Interface_Bridge
     * @return Mapi_Ip
     */
    public function bridge(){
        return new Mapi_Interface_Bridge($this->param);
    }
    
    /**
     * This method used call class Mapi_Interface_L2tp_Client 
     * @return Mapi_Ip
     */
    public function l2tp_client(){
        return new Mapi_Interface_L2tp_Client($this->param);
    }
    
    /**
     * This method used call class Mapi_Interface_L2tp_Server 
     * @return Mapi_Ip
     */
    public function l2tp_server(){
        return new Mapi_Interface_L2tp_Server($this->param);
    }
    
    /**
     * This method used call class Mapi_Interface_Ppp_Client 
     * @return Mapi_Ip
     */
    public function ppp_client(){
        return new Mapi_Interface_Ppp_Client($this->param);
    }
    
    /**
     * This method used call class Mapi_Interface_Ppp_Server 
     * @return Mapi_Ip
     */
    public function ppp_server(){
        return new Mapi_Interface_Ppp_Server($this->param);
    }
    
    /**
     * This method used call class Mapi_Interface_Pptp_Client 
     * @return Mapi_Ip
     */
    public function pptp_client(){
        return new Mapi_Interface_Pptp_Client($this->param);
    }
    
    /**
     * This method used call class Mapi_Interface_Pptp_Server 
     * @return Mapi_Ip
     */
    public function pptp_server(){
        return new Mapi_Interface_Pptp_Server($this->param);
    }
    
}



File: /src\Libs\mikrotik\interface\mapi_interface_bonding.php
<?php

/**
 * Description of Mapi_interface_Bonding
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Bonding extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add interface bonding
     * 
     * Example in Mikrotik RouterOs :
     * 
     * [admin@Router1] interface bonding> add slaves=ether1,ether2
     * 
     * Exmple : 
     * 
     * $param = array(
     *                          'name'    => 'bonding1',
     *                          'slaves'  => 'ether1,ether2');
     * 
     * $this->mikrotik_api->interfaces()->bonding()->add_bonding($param);
     * 
     * The $param that you can send to Mikrotik RouterOs are :
     * 
     * 1. arp -- Address Resolution Protocol
     * 
     * 2. arp-interval -- Time in milliseconds for monitoring ARP requests
     * 
     * 3. arp-ip-targets -- IP addresses for monitoring
     * 
     * 4. comment -- Set comment for items
     * 
     * 5. copy-from -- Item number
     * 
     * 6. disabled -- Defines whether MAC Telnet Server is disabled or not
     * 
     * 7. down-delay -- Time period the interface is disabled  if a link failure has been detected
     * 
     * 8. lacp-rate -- Link Aggregation Control Protocol rate specifies how often to exchange with LACPDUs between bonding peer
     * 
     * 9. link-monitoring -- Method for monitoring the link
     * 
     * 10. mii-interval -- Time in milliseconds for monitoring mii-type link
     * 
     * 11. mode -- Interface bonding mode
     * 
     * 12. mtu -- Maximum Transmit Unit
     * 
     * 13. name -- Interface name
     * 
     * 14. primary -- Slave that will be used in active-backup mode as active link
     * 
     * 16. slaves -- Interfaces that are used in bonding
     * 
     * 17. up-delay -- Time period the interface is disabled if a link has been brought up
     * 
     * 18. up-delay -- Time period the interface is disabled if a link has been brought up
     *  
     * @param type $param array
     * @return type array
     */
     public function add_bonding($param){
        $input = array(
                    'command'       => '/interface/bonding/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to display all interface bonding
     * 
     * Example :
     * 
     * print_r($this->mikrotik_api->interfaces()->bonding()->get_all_bonding());
     * @return type array
     */
     public function get_all_bonding(){
        return $this->query('/interface/bonding/getall');
    }
    
    /**
     * This method is used to enable interface bonding by id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->bonding()->enable_bonding('*1');
     * @param type $id string
     * @return type array
     */
     public function enable_bonding($id){
        $input = array(
                    'command'       => '/interface/bonding/enable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to disable interface bonding by id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->bonding()->disable_bonding('*1');
     * @param type $id string
     * @return type array
     */
     public function disable_bonding($id){
        $input = array(
                    'command'       => '/interface/bonding/disable',
                    'id'            => $id
        );
        return $this->query($input);
    }
      
    /**
     * This method is used to set or edit interface bonding by id
     * 
     * Example :
     * 
     * $param = array(
     *                          'name'    => 'bonding1',
     *                          'slaves'  => 'ether1,ether2');
     * 
     * $this->mikrotik_api->interfaces()->bonding()->set_bonding($param, '*1');
     * 
     * 
     * The $param that you can send to Mikrotik RouterOs are :
     * 
     * 1. arp -- Address Resolution Protocol
     * 
     * 2. arp-interval -- Time in milliseconds for monitoring ARP requests
     * 
     * 3. arp-ip-targets -- IP addresses for monitoring
     * 
     * 4. comment -- Set comment for items
     * 
     * 5. copy-from -- Item number
     * 
     * 6. disabled -- Defines whether MAC Telnet Server is disabled or not
     * 
     * 7. down-delay -- Time period the interface is disabled  if a link failure has been detected
     * 
     * 8. lacp-rate -- Link Aggregation Control Protocol rate specifies how often to exchange with LACPDUs between bonding peer
     * 
     * 9. link-monitoring -- Method for monitoring the link
     * 
     * 10. mii-interval -- Time in milliseconds for monitoring mii-type link
     * 
     * 11. mode -- Interface bonding mode
     * 
     * 12. mtu -- Maximum Transmit Unit
     * 
     * 13. name -- Interface name
     * 
     * 14. primary -- Slave that will be used in active-backup mode as active link
     * 
     * 16. slaves -- Interfaces that are used in bonding
     * 
     * 17. up-delay -- Time period the interface is disabled if a link has been brought up
     * 
     * 18. up-delay -- Time period the interface is disabled if a link has been brought up
     *  
     * @param type $param array
     * @param type $id string
     * @return type array
     */
      public function set_bonding($param, $id){
        $input = array(
                    'command'   => '/interface/bonding/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }     
    
    /**
     * This method is used to display one interface bonding
     * in detail based on the id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->bonding()->detail_bonding('*1');
     * @param type $id string
     * @return type array
     */
     public function detail_bonding($id){
        $input = array(
                   'command'    => '/interface/bonding/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
    /**
     * This method is used to delete interface bonding by id
     * 
     * $this->mikrotik_api->interfaces()->bonding()->delete_bonding('*1');
     * @param type $id string
     * @return type array
     */
     public function delete_bonding($id){
        $input = array(
                   'command'    => '/interface/bonding/remove',
                   'id'         => $id
        );
        return $this->query($input);
    }
}

File: /src\Libs\mikrotik\interface\mapi_interface_bridge.php
<?php

/**
 * Description of Mapi_interface_Bridge
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Bridge extends Mapi_Query {
    private $param;
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method used for add new interface bridge
     * @param type $param array
     * @return type array
     */
    public function add_bridge($param){
       $input = array(
            'command'       => '/interface/bridge/add',
         );
       $out = array_merge($input, $param);
       return $this->query($out);
    }
    
    /**
     * This method used for disable interface bridge
     * @param type $id string
     * @return type array
     */
    public function disable_bridge($id){
        $input = array(
                'command'       => '/interface/bridge/disable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for enable interface bridge
     * @param type $id string
     * @return type array
     */
    public function enable_bridge($id){
        $input = array(
                'command'       => '/interface/bridge/enable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for delete interface bridge
     * @param type $id string
     * @return type array
     */
    public function delete_bridge($id){
        $input = array(
                'command'       => '/interface/bridge/remove',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for get all interface bridge
     * @return type array
     */
    public function get_all_bridge(){
        return $this->query('/interface/bridge/getall'); 
    }
    
    /**
     * This method used for set or edit interface bridge
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_bridge($param, $id){
        $input = array(
                'command'       => '/interface/bridge/set',
                'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for detail interface bridge
     * @param type $id string
     * @return type array
     */
    public function detail_bridge($id){
        $input = array(
                'command'       => '/interface/bridge/print',
                'id'            => $id
        );
        return $this->query($input);
    }
    
     public function add_bridge_nat($param){
       $input = array(
            'command'       => '/interface/bridge/nat/add',
         );
       $out = array_merge($input, $param);
       return $this->query($out);
    }
    
    /**
     * This method used for disable interface bridge
     * @param type $id string
     * @return type array
     */
    public function disable_bridge_nat($id){
        $input = array(
                'command'       => '/interface/bridge/nat/disable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for enable interface bridge
     * @param type $id string
     * @return type array
     */
    public function enable_bridge_nat($id){
        $input = array(
                'command'       => '/interface/bridge/nat/enable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for delete interface bridge
     * @param type $id string
     * @return type array
     */
    public function delete_bridge_nat($id){
        $input = array(
                'command'       => '/interface/bridge/nat/remove',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for get all interface bridge
     * @return type array
     */
    public function get_all_bridge_nat(){
        return $this->query('/interface/bridge/nat/getall'); 
    }
    
    /**
     * This method used for set or edit interface bridge
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_bridge_nat($param, $id){
        $input = array(
                'command'       => '/interface/bridge/nat/set',
                'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for detail interface bridge
     * @param type $id string
     * @return type array
     */
    public function detail_bridge_nat($id){
        $input = array(
                'command'       => '/interface/bridge/nat/print',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for set interface Bridge Settings
     * @param type $use_ip_firewall string (default : yes or no)
     * @param type $use_ip_firewall_for_vlan string (default : yes or no)
     * @param type $use_ip_firewall_for_pppoe string (default : yes or no)
     * @return type array
     */
    public function set_bridge_settings($use_ip_firewall, $use_ip_firewall_for_vlan, $use_ip_firewall_for_pppoe){
       $input = array(
                'command'                   => '/interface/bridge/settings/set',
                'use-ip-firewall'           => $use_ip_firewall,
                'use-ip-firewall-for-vlan'  => $use_ip_firewall_for_vlan,
                'use-ip-firewall-for-pppoe' => $use_ip_firewall_for_pppoe
       ); 
       return $this->query($input);
    }
    
    /**
     * This method used for get all interface Bridge Settings
     * @return type array
     */
    public function get_all_bridge_settings(){
        return $this->query('/interface/bridge/settings/getall');
    }
}



File: /src\Libs\mikrotik\interface\mapi_interface_eoip.php
<?php

/**
 * Description of Mapi_Interface_Eoip
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Eoip extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add interface eoip
     * 
     * Example :
     * 
     * $param = array(
     *                'remote-address'  => '172.17.18.18',
     *                'tunnel-id'       => '0',
     *                'arp'             => 'disabled',
     *                'comment'         => 'krisna-eoip',
     *                'mtu'             => '0',
     *                'name'            => 'krisna',
     *                'mac-address'     => '00:00:00:00:00:00',
     *                'copy-from'       => 'krisna.txt'
     *                'disabled'        => 'no'
     *              );
     * 
     * $this->mikrotik_api->interfaces()->eoip()->add_eoip($param);
     * 
     * @param type $param array
     * @return type array
     */
     public function add_eoip($param){
        $input = array(
                    'command'       => '/interface/eoip/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to display all interface eoip
     * 
     * Example :
     * 
     * print_r($this->mikrotik_api->interfaces()->eoip()->get_all_eoip());
     * @return type array
     */
     public function get_all_eoip(){
        return $this->query('/interface/eoip/getall');
    }
    
    /**
     * This method is used to enable interface eoip by id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->eoip()->enable_eoip('*1');
     * @param type $id string
     * @return type array
     */
     public function enable_eoip($id){
        $input = array(
                    'command'       => '/interface/eoip/enable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to disable interface eoip by id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->eoip()->disable_eoip('*1');
     * @param type $id string
     * @return type array
     */
     public function disable_eoip($id){
        $input = array(
                    'command'       => '/interface/eoip/disable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to remove interface eoip by id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->eoip()->delete_eoip('*1');
     * @param type $id string
     * @return type array
     */
     public function delete_eoip($id){
        $input = array(
                   'command'    => '/interface/eoip/remove',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to set or edit interface eoip by id
     * 
     * Example :
     * 
     * $param = array(
     *                'remote-address'  => '172.17.18.18',
     *                'tunnel-id'       => '0',
     *                'arp'             => 'disabled',
     *                'comment'         => 'krisna-eoip',
     *                'mtu'             => '0',
     *                'name'            => 'krisna',
     *                'mac-address'     => '00:00:00:00:00:00',
     *                'copy-from'       => 'krisna.txt'
     *                'disabled'        => 'no'
     *              );
     * 
     *  $this->mikrotik_api->interfaces()->eoip()->set_eoip($param, '*1');
     * @param type $param array
     * @param type $id string
     * @return type array
     */
      public function set_eoip($param, $id){
        $input = array(
                    'command'   => '/interface/eoip/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }     
    
    /**
     * This method is used to display one interface eoip 
     * in detail based on the id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->eoip()->detail_eoip($param, '*1');
     * @param type $id string
     * @return type array
     */
     public function detail_eoip($id){
        $input = array(
                   'command'    => '/interface/eoip/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}


File: /src\Libs\mikrotik\interface\mapi_interface_ethernet.php
<?php

/**
 * Description of Mapi_File
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Ethernet extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
     
     /**
      * This method is used to display all interface
      * @return type array
      */
     public function get_all_interface(){
         return $this->query('/interface/getall');
    }
    
    /**
     * This method is used to display one interface  
     * in detail based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    
    public function set_interface($param, $id){
        $input = array(
            'command'       => '/interface/set',
            'id'            => $id                
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to enable interface by id
     * @param type $id string
     * @return type array
     */
    public function enable_interface($id){
        $input = array(
            'command'       => '/interface/enable',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to disable interface by id
     * @param type $id string
     * @return type array
     */
    public function disable_interface($id){
        $input = array(
            'command'       => '/interface/disable',
            'id'            => $id
        );
        return $this->query($input);
    }
    /**
     * This method is used to display one interafce 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail_interface($id){
        $input = array(
                   'command'    => '/interface/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}


File: /src\Libs\mikrotik\interface\mapi_interface_ipip.php
<?php
/**
 * Description of Mapi_Interface_Ipip
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Ipip extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
     
    /**
     * This method is used to add interface ipip
     * @param type $param array
     * @return type array
     */
     public function add_ipip($param){
        $input = array(
                    'command'       => '/interface/ipip/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to display all interface ipip
     * @return type array
     */
     public function get_all_ipip(){
        return $this->query('/interface/ipip/getall');
    }
    
    /**
     * This method is used to enable interface ipip by id
     * @param type $id string
     * @return type array
     */
     public function enable_ipip($id){
        $input = array(
                    'command'       => '/interface/ipip/enable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to disable interface ipip by id
     * @param type $id string
     * @return type array
     */
     public function disable_ipip($id){
        $input = array(
                    'command'       => '/interface/ipip/disable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to remove interface ipip
     * @param type $id string
     * @return type array
     */
     public function delete_ipip($id){
        $input = array(
                   'command'    => '/interface/ipip/remove',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to set or edit interface ipip by id
     * @param type $param array
     * @param type $id string
     * @return type 
     */
    public function set_ipip($param, $id){
        $input = array(
                    'command'   => '/interface/ipip/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }     
    
    /**
     * This method is used to display one interface ipip 
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail_ipip($id){
        $input = array(
                   'command'    => '/interface/ipip/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}

File: /src\Libs\mikrotik\interface\mapi_interface_l2tp_client.php
<?php

/**
 * Description of Mapi_interface_l2tp_client
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_L2tp_Client extends Mapi_Query {
    private $param;
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method used for add new l2tp client
     * @param type $param array
     * @return type array
     */
    public function add_l2tp_client($param){
        $input = array(
            'command'       => '/interface/l2tp-client/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for disable l2tp client
     * @param type $id string
     * @return type array
     */
    public function disable_l2tp_client($id){
        $input = array(
            'command'       => '/interface/l2tp-client/disable',
            'id'            => $id
        ); 
        return $this->query($input);
    }
    
    /**
     * This method used for enable l2tp client
     * @param type $id string
     * @return type array
     */
    public function enable_l2tp_client($id){
         $input = array(
             'command'      => '/interface/l2tp-client/enable',
             'id'           => $id
         );
         return $this->query($input);
     }
     
     /**
      * This method used for delete l2tp client
      * @param type $id string
      * @return type array
      */
    public function delete_l2tp_client($id){
          $input = array(
              'command'     => '/interface/l2tp-client/remove',
              'id'          => $id
          );
          return $this->query($input);
      }
      
      /**
       * This method used for detail l2tp client
       * @param type $id string
       * @return type array
       */
    public function detail_l2tp_client($id){
        $input = array(
            'command'       => '/interface/l2tp-client/print',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for set or edit l2tp client
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_l2tp_client($param, $id){
        $input = array(
            'command'       => '/interface/l2tp-client/set',
            'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for get all l2tp client
     * @return type array
     */
    public function get_all_l2tp_client(){
        return $this->query('/interface/l2tp-client/getall');
    }
}



File: /src\Libs\mikrotik\interface\mapi_interface_l2tp_server.php
<?php

/**
 * Description of Mapi_interface_l2tp_server
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_L2tp_Server extends Mapi_Query {
    private $param;
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method used for add new l2tp server
     * @param type $param array
     * @return type array
     */
    public function add_l2tp_server($param){
        $input = array(
            'command'       => '/interface/l2tp-server/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for disable l2tp server
     * @param type $id string
     * @return type array
     */
    public function disable_l2tp_server($id){
        $input = array(
            'command'       => '/interface/l2tp-server/disable',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for enable l2tp server
     * @param type $id string
     * @return type array
     */
    public function enable_l2tp_server($id){
        $input = array(
            'command'       => '/interface/l2tp-server/enable',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for delete l2tp server
     * @param type $id string
     * @return type array
     */
    public function delete_l2tp_server($id){
        $input = array(
            'command'       => '/interface/l2tp-server/remove',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for detail l2tp server
     * @param type $id string
     * @return type array
     */
    public function detail_l2tp_server($id){
        $input = array(
            'command'       => '/interface/l2tp-server/print',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for set or edit l2tp server
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_l2tp_server($param, $id){
        $input = array(
            'command'       => '/interface/l2tp-server/set',
            'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for get all l2tp server
     * @return type array
     */
    public function get_all_l2tp_server(){
        return $this->query('/interface/l2tp-server/getall');
    }
    
    /**
     * This method used for get all l2tp server server
     * @return type array
     */
    public function get_all_l2tp_server_server(){
        return $this->query('/interface/l2tp-server/server/getall');
    }
    
    /**
     * This method used for set l2tp server server
     * @param type $param array
     * @return type array
     */
    public function set_l2tp_server_server($param){
        $input = array(
            'command'       => '/interface/l2tp-server/server/set'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
        
    }
}




File: /src\Libs\mikrotik\interface\mapi_interface_pppoe_client.php
<?php

/**
 * Description of Mapi_Interface_Pppoe_Client
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Pppoe_Client extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add pppoe-client
     * @param type $param array
     * @return type array
     * 
     */
    public function add_pppoe_client($param){
        $input = array(
                    'command'       => '/interface/pppoe-client/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to display all pppoe-client 
     * @return type array
     * 
     */
    public function get_all_pppoe_client(){
        return $this->query('/interface/pppoe-client/getall');
    }
    
    /**
     * This method is used to enable pppoe-client by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable_pppoe_client($id){
        $input = array(
                    'command'       => '/interface/pppoe-client/enable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to disable pppoe-client by id
     * @param type $id string
     * @return type array
     * 
     */
     public function disable_pppoe_client($id){
        $input = array(
                    'command'       => '/interface/pppoe-client/disable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to delete pppoe-client by id
     * @param type $id string
     * @return type array
     * 
     */
     public function delete_pppoe_client($id){
        $input = array(
                   'command'    => '/interface/pppoe-client/remove',
                   'id'         => $id
        );
        return $this->query($input);
    }
   
    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
     public function set_pppoe_client($param, $id){
        $input = array(
                    'command'   => '/interface/pppoe-client/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }     
    
     /**
     * This method is used to display one pppoe-client
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail_pppoe_client($id){
        $input = array(
                   'command'    => '/interface/pppoe-client/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}




File: /src\Libs\mikrotik\interface\mapi_interface_pppoe_server.php
<?php

/**
 * Description of Mapi_Interface_Pppoe_Server
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Pppoe_Server extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param) {
        $this->param  = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add pppoe-server
     * @param type $param array
     * @return type array
     * 
     */
    public function add_pppoe_server($param){
        $input = array(
            'command'       => '/interface/pppoe-server/server/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to disable pppoe-server by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable_pppoe_server($id){
        $input = array(
            'command'       => '/interface/pppoe-server/server/disable',
            'id'            => $id
        );
        return $this->query($input);        
    }
    
    /**
     * This method is used to enable pppoe-server by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable_pppoe_server($id){
        $input = array(
            'command'       => '/interface/pppoe-server/server/enable',
            'id'            => $id
        );
        return $this->query($input); 
    }
    
     /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set_pppoe_server($param, $id){
        $input = array(
                    'command'   => '/interface/pppoe-server/server/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to delete pppoe-server by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete_pppoe_server($id){
         $input = array(
                   'command'    => '/interface/pppoe-server/server/remove',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to display all pppoe-server
     * @return type array
     * 
     */
    public function get_all_pppoe_server(){
         return $this->query('/interface/pppoe-server/server/getall');
    }
    
     /**
     * This method is used to display one pppoe-server 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail_pppoe_server($id){
        $input = array(
                   'command'    => '/interface/pppoe-server/server/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}



File: /src\Libs\mikrotik\interface\mapi_interface_ppp_client.php
<?php

/**
 * Description of Mapi_interface_ppp_client
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Ppp_Client extends Mapi_Query {
    private $param;
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method used for add new interface ppp-client
     * @param type $param array
     * @return type array
     */
    public function add_ppp_client($param){
        $input = array(
            'command'       => '/interface/ppp-client/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for disable interface ppp-client
     * @param type $id string
     * @return type array
     */
    public function disable_ppp_client($id){
        $input = array(
            'command'       => '/interface/ppp-client/disable',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for enable interface ppp-client
     * @param type $id string
     * @return type array
     */
    public function enable_ppp_client($id){
        $input = array(
            'command'       => '/interface/ppp-client/enable',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for delete interface ppp-client
     * @param type $id string
     * @return type array
     */
    public function delete_ppp_client($id){
        $input = array(
            'command'       => '/interface/ppp-client/remove',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for detail interface ppp-client
     * @param type $id string
     * @return type array
     */
    public function detail_ppp_client($id){
        $input = array(
            'command'       => '/interface/ppp-client/print',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for set or edit interface ppp-client
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_ppp_client($param, $id){
        $input = array(
            'command'       => '/interface/ppp-client/set',
            'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);    
    }
    
    /**
     * This method used for get all interface ppp-client
     * @return type array
     */
    public function get_all_ppp_client(){
        return $this->query('/interface/ppp-client/getall');
    }
}



File: /src\Libs\mikrotik\interface\mapi_interface_ppp_server.php
<?php

/**
 * Description of Mapi_interface_ppp_server
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Ppp_Server extends Mapi_Query {
    private $param;
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    /**
     * This method used for add new interface ppp-sever
     * @param type $param array
     * @return type array
     */
    public function add_ppp_server($param){
        $input = array(
            'command'       => '/interface/ppp-server/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for disable interface ppp-sever
     * @param type $id string
     * @return type array
     */
    public function disable_ppp_server($id){
        $input = array(
            'command'       => '/interface/ppp-server/disable',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for enable interface ppp-sever
     * @param type $id string
     * @return type array
     */
    public function enable_ppp_server($id){
        $input = array(
            'command'       => '/interface/ppp-server/enable',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for delete interface ppp-sever
     * @param type $id string
     * @return type array
     */
    public function delete_ppp_server($id){
        $input = array(
            'command'       => '/interface/ppp-server/remove',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for detail interface ppp-sever
     * @param type $id string
     * @return type array
     */
    public function detail_ppp_server($id){
        $input = array(
            'command'       => '/interface/ppp-server/print',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for set or edit interface ppp-sever
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_ppp_server($param, $id){
        $input = array(
            'command'       => '/interface/ppp-server/set',
            'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);    
    }
    
    /**
     * This method used for get all interface ppp-sever
     * @return type array
     */
    public function get_all_ppp_server(){
        return $this->query('/interface/ppp-server/getall');
    }
}


File: /src\Libs\mikrotik\interface\mapi_interface_pptp_client.php
<?php

/**
 * Description of Mapi_interface_pptp_client
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Pptp_Client extends Mapi_Query {
    private $param;
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
  /**
     * This method used for add new interface pptp-client
     * @param type $param array
     * @return type array
     */
    public function add_pptp_client($param){
        $input = array(
            'command'       => '/interface/pptp-client/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for disable interface pptp-client
     * @param type $id string
     * @return type array
     */
    public function disable_pptp_client($id){
        $input = array(
            'command'       => '/interface/pptp-client/disable',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for enable interface pptp-client
     * @param type $id string
     * @return type array
     */
    public function enable_pptp_client($id){
        $input = array(
            'command'       => '/interface/pptp-client/enable',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for delete interface pptp-client
     * @param type $id string
     * @return type array
     */
    public function delete_pptp_client($id){
        $input = array(
            'command'       => '/interface/pptp-client/remove',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for detail interface pptp-client
     * @param type $id string
     * @return type array
     */
    public function detail_pptp_client($id){
        $input = array(
            'command'       => '/interface/pptp-client/print',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for set or edit interface pptp-client
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_pptp_client($param, $id){
        $input = array(
            'command'       => '/interface/pptp-client/set',
            'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);    
    }
    
    /**
     * This method used for get all interface pptp-client
     * @return type array
     */
    public function get_all_pptp_client(){
        return $this->query('/interface/pptp-client/getall');
    }
}




File: /src\Libs\mikrotik\interface\mapi_interface_pptp_server.php
<?php

/**
 * Description of Mapi_Interface_Pptp_Server
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Pptp_Server extends Mapi_Query {
    private $param;
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
   /**
     * This method used for add new interface pptp-server
     * @param type $param array
     * @return type array
     */
    public function add_pptp_server($param){
        $input = array(
            'command'       => '/interface/pptp-server/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for disable interface pptp-server
     * @param type $id string
     * @return type array
     */
    public function disable_pptp_server($id){
        $input = array(
            'command'       => '/interface/pptp-server/disable',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for enable interface pptp-server
     * @param type $id string
     * @return type array
     */
    public function enable_pptp_server($id){
        $input = array(
            'command'       => '/interface/pptp-server/enable',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for delete interface pptp-server
     * @param type $id string
     * @return type array
     */
    public function delete_pptp_server($id){
        $input = array(
            'command'       => '/interface/pptp-server/remove',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for detail interface pptp-server
     * @param type $id string
     * @return type array
     */
    public function detail_pptp_server($id){
        $input = array(
            'command'       => '/interface/pptp-server/print',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for set or edit interface pptp-server
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_pptp_server($param, $id){
        $input = array(
            'command'       => '/interface/pptp-server/set',
            'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);    
    }
    
    /**
     * This method used for get all interface pptp-server
     * @return type array
     */
    public function get_all_pptp_server(){
        return $this->query('/interface/pptp-server/getall');
    }
    
    /**
     * This method used for get all pptp-server server
     * @return type array
     */
    public function get_all_pptp_server_server(){
        return $this->query('/interface/pptp-server/server/getall');
    }
    
    /**
     * This method used for set pptp-server server
     * @param type $param array
     * @return type array
     */
    public function set_pptp_server_server($param){
        $input = array(
            'command'       => '/interface/pptp-server/server/set'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
        
    }
}


File: /src\Libs\mikrotik\interface\mapi_interface_vlan.php
<?php

/**
 * Description of Mapi_Interface_Vlan
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Vlan extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;

    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add vlan
     * @param type $param array
     * @return type array
     * 
     */
     public function add_vlan($param){
        $input = array(
                    'command'       => '/interface/vlan/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
     /**
     * This method is used to display all vlan
     * @return type array
     * 
     */
     public function get_all_vlan(){
        return $this->query('/interface/vlan/getall');
    }
    
     
    /**
     * This method is used to enable vlan by id
     * @param type $id string
     * @return type array
     * 
     */
     public function enable_vlan($id){
        $input = array(
                    'command'       => '/interface/vlan/enable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to disable vlan by id
     * @param type $id string
     * @return type array
     * 
     */
     public function disable_vlan($id){
        $input = array(
                    'command'       => '/interface/vlan/disable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to delete vlan by id
     * @param type $id string
     * @return type array
     * 
     */
     public function delete_vlan($id){
        $input = array(
                   'command'    => '/interface/vlan/remove',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
      public function set_vlan($param, $id){
        $input = array(
                    'command'   => '/interface/vlan/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }     
    
     /**
     * This method is used to display one vlan
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
     public function detail_vlan($id){
        $input = array(
                   'command'    => '/interface/vlan/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}



File: /src\Libs\mikrotik\interface\mapi_interface_vrrp.php
<?php
/**
 * Description of Mapi_Interface_Vrrp
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Interface_Vrrp extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
      /**
     * This method is used to to add vrrp
     * @param type $param array
     * @return type array
     * 
     */
     public function add_vrrp($param){
        $input = array(
                    'command'       => '/interface/vrrp/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
     
    /**
     * This method is used to display all vrrp
     * @return type array
     * 
     */
     public function get_all_vrrp(){
        return $this->query('/interface/vrrp/getall');
    }
    
     
    /**
     * This method is used to to enable vrrp by id
     * @param type $id string
     * @return type array
     * 
     */
     public function enable_vrrp($id){
        $input = array(
                    'command'       => '/interface/vrrp/enable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
     /**
     * This method is used to to disable vrrp by id
     * @param type $id string
     * @return type array
     * 
     */
     public function disable_vrrp($id){
        $input = array(
                    'command'       => '/interface/vrrp/disable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
   /**
     * This method is used to to delete vrrp by id
     * @param type $id string
     * @return type array
     * 
     */
     public function delete_vrrp($id){
        $input = array(
                   'command'    => '/interface/vrrp/remove',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
     /**
     * This method is used to change based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
      public function set_vrrp($param, $id){
        $input = array(
                    'command'   => '/interface/vrrp/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }     
    
    /**
     * This method is used to display one vrrp
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
     public function detail_vrrp($id){
        $input = array(
                   'command'    => '/interface/vrrp/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}

File: /src\Libs\mikrotik\ip\mapi_ip.php
<?php

/**
 * Description of Mapi_Ip
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip{
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param=array()) {
        $this->param = $param;
    }
    
     /**
     * This method is used toclass Mapi_Ip_Address
     * @return Object of Mapi_Ip_Address class
     */
    public function address(){
        return new Mapi_Ip_Address($this->param);
    }
    
     /**
     * This method is used toclass Mapi_Ip_Hotspot
     * @return Object of Mapi_Ip_Hotspot class
     */
    public function hotspot(){
        return new Mapi_Ip_Hotspot($this->param);
    }
    
     /**
     * This method is used toclass Mapi_Ip_Pool
     * @return Object of Mapi_Ip_Pool class
     */
    public function pool(){
        return new Mapi_Ip_Pool($this->param);
    }
    
     /**
     * This method is used toclass Mapi_Ip_Dns
     * @return Object of Mapi_Ip_Dns class
     */
    public function dns(){
        return new Mapi_Ip_Dns($this->param);
    }
    
     /**
     * This method is used toclass Mapi_Ip_Firewall
     * @return Object of Mapi_Ip_Firewall class
     */
    public function firewall(){
        return new Mapi_Ip_Firewall($this->param);
    }

     /**
     * This method is used toclass Mapi_Ip_Accounting
     * @return Object of Mapi_Ip_Accounting class
     */
    public function accounting(){
        return new Mapi_Ip_Accounting($this->param);
        
    }
    
     /**
     * This method is used toclass Mapi_Ip_Arp
     * @return Object of Mapi_Ip_Arp class
     */
    public function arp(){
        return new Mapi_Ip_Arp($this->param);
    }
    
     /**
     * This method is used toclass Mapi_Ip_Dhcp_Client
     * @return Object of Mapi_Ip _Dhcp_Client class
     */
    public function dhcp_client(){
        return new Mapi_Ip_Dhcp_Client($this->param);
    }
    
     /**
     * This method is used toclass Mapi_Ip_Dhcp_Relay
     * @return Object of Mapi_Ip_Dhcp_Relay class
     */
    public function dhcp_relay(){
        return new Mapi_Ip_Dhcp_Relay($this->param);
    }
    
     /**
     * This method is used toclass Mapi_Ip_Dhcp_Server
     * @return Object of Mapi_Ip_Dhcp_Server class
     */
    public function dhcp_server(){
        return new Mapi_Ip_Dhcp_Server($this->param);
    }
    
     /**
     * This method is used toclass Mapi_Ip_Route
     * @return Object if Mapi_Ip_Router class
     */
    public function route(){
        return new Mapi_Ip_Route($this->param);
    }
    
     /**
     * This method is used toclass Mapi_Ip_Service
     * @return Object of Mapi_Ip_Service class
     */
    public function service(){
        return new Mapi_Ip_Service($this->param);
        
    }
    
    /**
     *This method is used to class Mapi_Ip_Proxy
     * @return object of Mapi_Ip_Proxy class
     */
    public function proxy(){
        return new Mapi_Ip_Proxy($this->param);
        
    }
    
}



File: /src\Libs\mikrotik\ip\mapi_ip_accounting.php
<?php

/**
 * Description of Mapi_Ip_Accounting
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Accounting extends Mapi_Query{
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to set or edit ip accountng
     * @param type $account_local_traffic string
     * @param type $enabled string
     * @param type $threshold string
     * @return type array
     */
    public function set_accounting($account_local_traffic, $enabled, $threshold){
        $input = array(
                'command'                   => '/ip/accounting/set',
                'account-local-traffic'     => $account_local_traffic,
                'enabled'                   => $enabled,
                'threshold'                 => $threshold   
        );
        return $this->query($input);
    }
    
     /**
     * This method is used to display all accounting
     * @return type array
     * 
     */
    public function get_all_accounting(){
        return $this->query('/ip/accounting/getall');
    }
    
     /**
     * This method is used to display all snapshot
     * @return type array
     * 
     */
    public function get_all_snapshot(){
        return $this->query('/ip/accounting/snapshot/getall');
    }
    
     /**
     * This method is used to display all uncounted
     * @return type array
     * 
     */
    public function get_all_uncounted(){
        return $this->query('/ip/accounting/uncounted/getall');
    }
    
     /**
     * This method is used to display all web-acces
     * @return type array
     * 
     */
    public function get_all_web_access(){
        return $this->query('/ip/accounting/web-access/getall');
    }
    /**
     * This method is used to ip accounting set web-acces
     * @param type $accessible_via_web string default : yes or no
     * @return type array
     * 
     */
    public function set_web_access($accessible_via_web){
        $input = array(
                'command'               => '/ip/accounting/web-access/set',
                'accessible-via-web'    => $accessible_via_web,
                'address'               => '0.0.0.0/0'
        );
        return $this->query($input);
    }
}



File: /src\Libs\mikrotik\ip\mapi_ip_address.php
<?php
/**
 * Description of Mapi_Ip_Address
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Address  extends Mapi_Query{
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add the ip address
     * @param type $param array
     * @return type array
     * 
     */
    public function add_address($param){
        $input=array(
            'command'       => '/ip/address/add'
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }
    /**
     * This method is used to display all ip address
     * @return type array
     * 
     */
    public function get_all_address(){
        return $this->query('/ip/address/getall');
    }
    
    /**
     * This method is used to activate the ip address by id
     * @param type $id is not an array
     * @return type array
     * 
     * 
     */
    public function enable_address($id){
        $input = array(
                'command'       => '/ip/address/enable',
                'id'            => $id     
        );
            return $this->query($input);
    }
    
    /**
     * This method is used to disable ip address by id
     * @param type $id string 
     * @return type array
     * 
     * 
     */
    public function disable_address($id){
        $input = array(
                'command'       => '/ip/address/disable',
                'id'            => $id
        );
            return $this->query($input);
    }
    
    /**
     * This method is used to remove the ip address by id
     * @param type $id is not an array
     * @return type array
     * 
     */
    public function delete_address($id){
        $input = array(
                   'command'    => '/ip/address/remove',
                   'id'         => $id
        );
        return $this->query($input);
   }
    
    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @return type array
     * 
     */
    public function set_address($param, $id){
        $input = array(
                    'command'   => '/ip/address/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }       
    
    /**
     * This method is used to display one ip address 
     * in detail based on the id
     * @param type $id not array
     * @return type array
     * 
     */
    public function detail_address($id){
        $input = array(
                   'command'    => '/ip/address/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}


File: /src\Libs\mikrotik\ip\mapi_ip_arp.php
<?php
/**
 * Description of Mapi_File
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Arp extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add arp
     * @param type $param array
     * @return type array
     * j
     */
    public function add_arp($param){
        $input = array(
                'command'       => '/ip/arp/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
     /**
     * This method is used to delete arp by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete_arp($id){
        $input = array(
            'command'       => '/ip/arp/remove',
            'id'            => $id
        );
        return $this->query($input);
    }
    
     /**
     * This method is used to enable arp by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable_arp($id){
        $input = array(
                'command'       => '/ip/arp/enable',
                'id'            => $id
        );        
        return $this->query($input);
    }
    
    /**
     * This method is used to disable arp by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id){
        $input = array(
                'command'       => '/ip/arp/disable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
     /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set_arp($param, $id){
        $input = array(
                    'command'       => '/ip/arp/set',
                    'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
        
    }
    
    /**
     * This method is used to display all arp
     * @return type array
     * 
     */
    public function get_all_arp(){
        return $this->query('/ip/arp/getall');
    }
    
     /**
     * This method is used to display arp
     * in detail based on the id
     * @param type $id string
     * @return type array
     *  
     */
    public function detail_arp($id){
        $input = array(
                   'command'    => '/ip/arp/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}


File: /src\Libs\mikrotik\ip\mapi_ip_dhcp_client.php
<?php

/**
 * Description of Mapi_Ip_Dhcp_Client
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Dhcp_Client extends Mapi_Query {
    /**
     *
     * @var type 
     */
    private $param;
    
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add dhcp client
     * @param type $param array
     * @return type array
     */
    public function add_dhcp_client($param){
        $input = array(
                'command'      => '/ip/dhcp-client/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to disable dhcp client by id
     * @param type $id string
     * @return type array
     */
    public function disable_dhcp_client($id){
        $input = array(
                'command'       => '/ip/dhcp-client/disable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to enable dhcp client by id
     * @param type $id string
     * @return type array
     */
    public function enable_dhcp_client($id){
         $input = array(
                'command'       => '/ip/dhcp-client/enable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to renew dhcp client  by id
     * @param type $id string
     * @return type array
     */
    public function renew_dhcp_client($id){
         $input = array(
                'command'       => '/ip/dhcp-client/renew',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to release dhcp client by id
     * @param type $id string
     * @return type array
     */
    public function release_dhcp_client($id){
         $input = array(
                'command'       => '/ip/dhcp-client/release',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to set or edit dhcp client by id
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_dhcp_client($param, $id){
        $input = array(
                'command'      => '/ip/dhcp-client/set',
                'id'           => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to remove dhcp client by id
     * @param type $id string
     * @return type array
     */
    public function delete_dhcp_client($id){
         $input = array(
                'command'       => '/ip/dhcp-client/remove',
                'id'            => $id
        );
        return $this->query($input);
    }

    /**
     * This method is used to display all dhcp client
     * @return type array
     */
    public function get_all_dhcp_client(){
        return $this->query('/ip/dhcp-client/getall');
    }
    
    /**
     * This method is used to display one ip dhcp client
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail_dhcp_client($id){
          $input = array(
                   'command'    => '/ip/dhcp-client/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}



File: /src\Libs\mikrotik\ip\mapi_ip_dhcp_relay.php
<?php
/**
 * Description of Mapi_Ip_Dhcp_Relay
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Dhcp_Relay extends Mapi_Query {
    /**
     *
     * @var type 
     */
    private $param;
    
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to ip add dhcp relay
     * @param type $param array 
     * @return type array
     */
    public function add_dhcp_relay($param){
        $input = array(
                'command'      => '/ip/dhcp-relay/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to disable ip dhcp relay by id
     * @param type $id string
     * @return type array
     */
    public function disable_dhcp_relay($id){
        $input = array(
                'command'       => '/ip/dhcp-relay/disable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to enable ip dhcp relay by id
     * @param type $id string
     * @return type array
     */
    public function enable_dhcp_relay($id){
          $input = array(
                'command'       => '/ip/dhcp-relay/enable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to set or edit ip dhcp relay by id
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_dhcp_relay($param, $id){
        $input = array(
                'command'       => '/ip/dhcp-relay/set',
                'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to remove ip dhcp relay by id
     * @param type $id string
     * @return type array
     */
    public function delete_dhcp_relay($id){
        $input = array(
                'command'       => '/ip/dhcp-relay/remove',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to display one interface bonding
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail_dhcp_relay($id){
         $input = array(
                'command'       => '/ip/dhcp-relay/print',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to display all ip dhcp relay
     * @return type array
     */
    public function get_all_dhcp_relay(){
        return $this->query('/ip/dhcp-relay/getall');
    }
}


File: /src\Libs\mikrotik\ip\mapi_ip_dhcp_server.php
<?php
/**
 * Description of Mapi_Ip_Dhcp_Server
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Dhcp_Server extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /** 
     * This methode is used to add ip dhcp server network
     * @param type $param array
     * @return type array
     */
    public function add_dhcp_server_network($param){
         $input = array(
                'command'      => '/ip/dhcp-server/network/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This methode is used to add ip dhcp server
     * @param type $param array
     * @return type \array
     */
    public function add_dhcp_server($param){
        $input = array(
                'command'      => '/ip/dhcp-server/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This methode is used to set ip dhcp server config
     * @param type $store_leases_disk string
     * @return type array
     */
    public function set_dhcp_server_config($store_leases_disk){
        $input = array(
                'command'                => '/ip/dhcp-server/config/set',
                'store-leases-disk'      => $store_leases_disk
        );
        return $this->query($input);
    }
    
    /**
     * This methode is used to set or edit ip dhcp server network
     * by id
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_dhcp_server_network($param, $id){
        $input = array(
                'command'      => '/ip/dhcp-server/network/set',
                'id'           => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This methode is used to display all ip dhcp server network
     * @return type array
     */
    public function get_all_dhcp_server_network(){
        return $this->query('/ip/dhcp-server/network/getall');
    }
    
    /**
     * This methode is used to delete ip dhcp server network by id
     * @param type $id string
     * @return type array
     */
    public function delete_dhcp_server_network($id){
        $input = array(
                'command'       => '/ip/dhcp-server/network/remove',
                'id'            => $id
        );
        return $this->query($input);
    }
    /**
     * This method is used to display one ip dhcp server network
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail_dhcp_server_network($id){
        $input = array(
                'command'       => '/ip/dhcp-server/network/print',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This methode is used to disable ip dhcp server by id
     * @param type $id string
     * @return type array
     */
    public function disable_dhcp_server($id){
        $input = array(
                'command'       => '/ip/dhcp-server/disable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This methode is used to enable ip dhcp server by id
     * @param type $id string
     * @return type array
     */
    public function enable_dhcp_server($id){
        $input = array(
                'command'       => '/ip/dhcp-server/enable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This methode is used to remove ip dhcp server by id
     * @param type $id string
     * @return type array
     */
    public function delete_dhcp_server($id){
        $input = array(
                'command'       => '/ip/dhcp-server/remove',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This methode is used to det or edit ip dhcp server by id
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_dhcp_server($param, $id){
         $input = array(
                'command'      => '/ip/dhcp-server/set',
                'id'           => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This methode is used to display all ip dhcp server
     * @return type array
     */
    public function get_all_dhcp_server(){
        return $this->query('/ip/dhcp-server/getall');
    }
    
    /**
     * This method is used to display one ip dhcp server
     * in detail based on the id
     * @param type $id string
     * @return type  array
     */
    public function detail_dhcp_server($id){
        $input = array(
                'command'       => '/ip/dhcp-server/print',
                'id'            => $id
        );
        return $this->query($input); 
    }
    
    public function get_all_dhcp_server_config(){
        return $this->query('/ip/dhcp-server/config/getall');
    }
    
}


File: /src\Libs\mikrotik\ip\mapi_ip_dns.php
<?php

/**
 * Description of Mapi_Ip_Dns
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Dns extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param){
        $this->param = $param;
        parent::__construct($param);
    }
    
   /**
    * This method is used to configure dns
    * @param type $servers string example : '192.168.1.1,192.168.2.1'
    * @return type array
    * 
    */
    public function set_dns($servers){
        $input = array(
                'command'       => '/ip/dns/set',
                'servers'       => $servers
        );
       return $this->query($input);
    }
    
    /**
     * This method is used to display
     * all dns
     * @return type array
     * 
     */
    public function get_all_dns(){
        return $this->query('/ip/dns/getall');
    }
     
    /**
     * This method is used to add the static dns
     * @param type $param array
     * @return type array
     * 
     */
    public function add_dns_static($param){
        $input = array(
                    'command'       => '/ip/dns/static/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
   /**
    * This method is used to display
    * all static dns
    * @return type array
    * 
    */
    public function get_all_static_dns(){
        return $this->query('/ip/dns/static/getall');
    }
    
    /**
     * This method is used to display one static dns 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
     public function detail_static_dns($id){
        $input = array(
                   'command'    => '/ip/dns/static/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to change based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set_static_dns($param, $id){
        $input = array(
                   'command'    => '/ip/dns/static/set',
                   'id'         => $id
        );        
        $out = array_merge($input, $param);
        return $this->query($out);
    }

     /**
     * This method is used to display
     * all dns cache
     * @return type array
     * 
     */
    public function get_all_dns_cache(){
        return $this->query('/ip/dns/cache/getall');
    }
    
    /**
     * This method is used to display one dns cache 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
     public function detail_dns_cache($id){
        $input = array(
                   'command'    => '/ip/dns/cache/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to display
     * all dns cache all cache
     * @return type array
     * 
     */
    public function get_all_dns_cache_all(){
        return $this->query('/ip/dns/cache/all/getall');
    }
    
     /**
     * This method is used to display one dns cache all 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
     public function detail_dns_cache_all($id){
        $input = array(
                   'command'    => '/ip/dns/cache/all/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}


File: /src\Libs\mikrotik\ip\mapi_ip_firewall.php
<?php
/**
 * Description of Mapi_Ip_Firewall
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Firewall extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add the firewall nat
     * @param type $param array
     * @return type array
     * 
     */
    public function add_firewall_nat($param){
         $input = array(
            'command'       => '/ip/firewall/nat/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to disable firewall nat by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable_firewall_nat($id){
        $input = array(
            'command'       => '/ip/firewall/nat/disable',
            'id'            => $id
        );
        return $this->query($input);        
    }
    
    /**
     * This method is used to enable firewall nat by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable_firewall_nat($id){
        $input = array(
            'command'       => '/ip/firewall/nat/enable',
            'id'            => $id
        );
        return $this->query($input); 
    }
    
    /**
     * This method is used to change firewall nat based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set_firewall_nat($param, $id){
        $input = array(
                    'command'   => '/ip/firewall/nat/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to remove firewall nat
     * @param type $id string
     * @return type array
     * 
     */
    public function delete_firewall_nat($id){
         $input = array(
                   'command'    => '/ip/firewall/nat/remove',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to display all firewall nat
     * @return type array
     * 
     */
    public function get_all_firewall_nat(){
         return $this->query('/ip/firewall/nat/getall');
    }
    
     /**
     * This method is used to display one firewall nat 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail_firewall_nat($id){
        $input = array(
                   'command'    => '/ip/firewall/nat/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     *
     * @param type $param array
     * @return type array
     * This method is used to add the firewall filter
     */
    public function add_firewall_filter($param){
        $input = array(
                    'command'   => '/ip/firewall/filter/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to display all firewall filter
     * @return type array
     * 
     */
    public function get_all_firewall_filter(){
        return $this->query('/ip/firewall/filter/getall');
    }
    
     /**
     * This method is used to enable firewall filter by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable_firewall_filter($id){
        $input = array(
                    'command'    => '/ip/firewall/filter/enable',
                    'id'         => $id
        );
        return $this->query($input);
    }
    
     /**
     * This method is used to disable firewall filter by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable_firewall_filter($id){
        $input = array(
                    'command'    => '/ip/firewall/filter/disable',
                    'id'         => $id
        );
        return $this->query($input);
    }
    
     /**
     * This method is used to remove firewall filter by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete_firewall_filter($id){
        $input = array(
                    'command'    => '/ip/firewall/filter/remove',
                    'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to change firewall nat based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set_firewall_filter($param, $id){
        $input = array(
                    'command'   => '/ip/firewall/filter/set',
                    'id'        => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
     /**
     * This method is used to display one firewall filter
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail_firewall_filter($id){
        $input = array(
                    'command'    => '/ip/firewall/filter/print',
                    'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for add new Ip Firewall Mangle 
     * @param type $param array
     * @return type array
     */
    public function add_firewall_mangle($param){
        $input = array(
                'command'       => '/ip/firewall/mangle/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for disable Ip Firewall Mangle
     * @param type $id string
     * @return type array
     */
    public function disable_firewall_mangle($id){
        $input = array(
                'command'       => '/ip/firewall/mangle/disable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for enable Ip Firewall Mangle
     * @param type $id string
     * @return type array
     */
    public function enable_firewall_mangle($id){
        $input = array(
                'command'       => '/ip/firewall/mangle/enable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for delete Ip Firewall Mangle
     * @param type $id string
     * @return type array
     */
    public function delete_firewall_mangle($id){
        $input = array(
                'command'       => '/ip/firewall/mangle/remove',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for detail Ip Firewall Mangle
     * @param type $id string
     * @return type array
     */
    public function detail_firewall_mangle($id){
        $input = array(
                'command'       => '/ip/firewall/mangle/print',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for set or edit Ip Firewall Mangle
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_firewall_mangle($param, $id){
        $input = array(
                'command'       => '/ip/firewall/mangle/set',
                'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for get all Ip Firewall Mangle
     * @return type array
     */
    public function get_all_firewall_mangle(){
        return $this->query('/ip/firewall/mangle/getall');
        
    }
    
    /**
     * This method used for get all firewall connection
     * @return type array
     */
    public function get_all_firewall_connection(){
        return $this->query('/ip/firewall/connection/getall');
    }
    
    /**
     * This method used for delete firewall connection
     * @param type $id string
     * @return type array
     */
    public function delete_firewall_connection($id){
        $input = array(
                'command'       => '/ip/firewall/connection/remove',
                'id'            => $id
        );
        return $this->query($input);
        
    }
    
    /**
     * This method used for get all Ip Firewall Service Port
     * @return type arrray
     */
    public function get_all_firewall_service_port(){
        return $this->query('/ip/firewall/service-port/getall');
    }
    
    /**
     * This method used for disable Ip Firewall Service Port
     * @param type $id string
     * @return type array
     */
    public function disable_firewall_service_port($id){
        $input = array(
                'command'       => '/ip/firewall/service-port/disable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for enable Ip Firewall Service Port
     * @param type $id string
     * @return type array
     */
    public function enable_firewall_service_port($id){
       $input = array(
                'command'       => '/ip/firewall/service-port/enable',
                'id'            => $id
       ); 
       return $this->query($input);
    }
    
}




File: /src\Libs\mikrotik\ip\mapi_ip_hotspot.php
<?php
/**
 * Description of Mapi_Ip_Hotspot
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Hotspot  extends Mapi_Query{
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add the user hotspot
     * @param type $param array
     * @return type array
     * 
     */
   public function add_hotspot_user($param){
        $input = array(
            'command'       => '/ip/hotspot/user/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to disable user hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable_hotspot_user($id){
        $input = array(
            'command'       => '/ip/hotspot/user/disable',
            'id'            => $id
        );
        return $this->query($input);        
    }
    
    /**
     * This method is used to activate the user hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable_hotspot_user($id){
        $input = array(
            'command'       => '/ip/hotspot/user/enable',
            'id'            => $id
        );
        return $this->query($input); 
    }
    
    /**
     * This method is used to change users hotspot based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set_hotspot_user($param, $id){
        $input = array(
                    'command'   => '/ip/hotspot/user/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to remove the user hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete_hotspot_user($id){
         $input = array(
                   'command'    => '/ip/hotspot/user/remove',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to display
     * all users hotspot
     * @return type array
     * 
     */
    public function get_all_hotspot_user(){
         return $this->query('/ip/hotspot/user/getall');
    }
    
    /**
     * This method is used to display one user hotspot 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail_hotspot_user($id){
        $input = array(
                   'command'    => '/ip/hotspot/user/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to display
     * all hotspot
     * @return type array 
     * 
     */
    public function get_all_hotspot(){
        return $this->query('/ip/hotspot/getall');
    }
    
    /**
     * This method is used to activate the hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
     public function enable_hotspot($id){
        $input = array(
                    'command'       => '/ip/hotspot/enable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
     /**
     * This method is used to disable hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
     public function disable_hotspot($id){
        $input = array(
                    'command'       => '/ip/hotspot/disable',
                    'id'            => $id
        );
        return $this->query($input);
    }
    
     /**
     * This method is used to remove the hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
     public function delete_hotspot($id){
        $input = array(
                   'command'    => '/ip/hotspot/remove',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to change hotspot based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
      public function set_hotspot($param, $id){
        $input = array(
                    'command'   => '/ip/hotspot/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }     
    
    /**
     * This method is used to display one hotspot 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
     public function detail_hotspot($id){
        $input = array(
                   'command'    => '/ip/hotspot/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This function is used to add hotspot
     * @return type array
     */
    public function setup_hotspot($param){
        $input = array(
                    'command'       => '/ip/hotspot/add',
                    ''
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for add new Ip Hotspot Ip-Binding
     * @param type $param array
     * @return type array
     */
    public function add_ip_binding($param){
        $input = array(
                'command'       => '/ip/hotspot/ip-binding/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for disable Ip Hotspot Ip-Binding
     * @param type $id string
     * @return type array
     */
    public function disable_ip_binding($id){
        $input = array(
                'command'       => '/ip/hotspot/ip-binding/disable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for enable Ip Hotspot Ip-Binding
     * @param type $id string
     * @return type array
     */
    public function enable_ip_binding($id){
        $input = array(
                'command'       => '/ip/hotspot/ip-binding/enable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for get all Ip Hotspot Ip-Binding
     * @return type array
     */
    public function get_all_ip_binding(){
        return $this->query('/ip/hotspot/ip-binding/getall');
    }
    
    /**
     * This method used for delete Ip Hotspot Ip-Binding
     * @param type $id string
     * @return type array
     */
    public function delete_ip_binding($id){
        $input = array(
                'command'       => '/ip/hotspot/ip-binding/remove',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for set or edit Ip Hotspot Ip-Binding
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_ip_binding($param, $id){
        $input = array(
                'command'       => '/ip/hotspot/ip-binding/set',
                'id'            => $id
        );        
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for detail Ip Hotspot Ip-Binding
     * @param type $id string
     * @return type array
     */
    public function detail_ip_binding($id){
        $input = array(
                'command'       => '/ip/hotspot/ip-binding/print',
                'id'            => $id
        );
        return $this->query($input);
    }
}


File: /src\Libs\mikrotik\ip\mapi_ip_pool.php
<?php

/**
 * Description of Mapi_Ip_Pool
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Pool extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add pool
     * @param type $param array
     * @return type array
     * 
     */
    public function add_pool($param){
        $input = array(
            'command'       => '/ip/pool/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to display
     * all pool
     * @return type array
     * 
     */
    public function get_all_pool(){
        return $this->query('/ip/pool/getall');
    }
    
    /**
     * This method is used to remove the pool by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete_pool($id){
        $input = array(
                'command'       => '/ip/pool/remove',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to change pool based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set_pool($param, $id){
        $input = array(
                'command'       => '/ip/pool/set',
                'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
     /**
     * This method is used to display one pool 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail_pool($id){
        $input = array(
                   'command'    => '/ip/pool/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}



File: /src\Libs\mikrotik\ip\mapi_ip_proxy.php
<?php

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of mapi_ip_proxi
 *
 * @author krisna
 */
class Mapi_Ip_Proxy extends Mapi_Query {
    private $param;
    function __construct($param) {
        $this->param ; $param;
        parent::__construct($param);
    }
    
    /**
     * This method used for get all Ip Proxi
     * @return type array
     */
    public function get_all_proxy(){
        return $this->query('/ip/proxy/getall');
    }
    
    /**
     *
     * This method used for set Ip proxy
     * @param type $param array
     * @return type array
     */
    public function set_proxy($param){
        $input = array(
                'command'       => '/ip/proxy/set'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
        
    }
}


File: /src\Libs\mikrotik\ip\mapi_ip_route.php
<?php
/**
 * Description of Mapi_Ip_Route
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Route extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to display all ip route
     * @return type array
     */
    public function get_all_route(){
        return $this->query('/ip/route/getall');
    }
    
    /**
     * This method is used to add ip route gateway
     * @param type $param array
     * @return type array
     */
    public function add_route_gateway($param){
        $input = array(
                'command'   => '/ip/route/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * Can change or disable only static routes
     * @param type $id is not array 
     * 
     */
    public function disable_route($id){
        $input = array(
            'command'       => '/ip/route/disable',
            'id'            => $id
        );
        return $this->query($input); 
    }
    
    /**
     * Can change or enable only static routes
     * @param type $id string
     * @return type array
     * 
     */
    public function enable_route($id){
        $input = array(
            'command'       => '/ip/route/enable',
            'id'            => $id
        );
        return $this->query($input); 
    }
    
    /**
     * Can change or remove only static routes
     * @param type $id string
     * @return type array
     * 
     */
    public function delete_route($id){
        $input = array(
            'command'       => '/ip/route/remove',
            'id'            => $id
        );
        return $this->query($input); 
    }
    
    /**
     * Can change only static routes
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set_route($param, $id){
        $input = array(
                    'command'   => '/ip/route/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to display one ip route
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail_route($id){
         $input = array(
                   'command'    => '/ip/route/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}



File: /src\Libs\mikrotik\ip\mapi_ip_service.php
<?php

/**
 * Description of Mapi_Ip_Service
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ip_Service extends Mapi_Query {
    private $param;
    function __construct($param ) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This methode is used to display all ip service
     * @return type array
     */
    public function get_all_service(){
        return $this->query('/ip/service/getall');
    }
    
    /**
     * This methode is used to enable ip service by id
     * @param type $id string
     * @return type array
     */
    public function enable_service($id){
        $input = array(
                'command'       => '/ip/service/enable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This methode is used to disable ip service by id
     * @param type $id string
     * @return type array
     */
    public function disable_service($id){
        $input = array(
                'command'       => '/ip/service/disable',
                'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to display one ip service
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail_service($id){
        $input = array(
                   'command'    => '/ip/service/print',
                   'id'         => $id
        );
        return $this->query($input);
    }    
    
    public function set_service($param, $id){
        $input = array(
                'command'       => '/ip/service/set',
                'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
}



File: /src\Libs\mikrotik\ppp\mapi_ppp.php
<?php

/**
 * Description of Mapi_Ppp
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ppp {
    private $param;
    function __construct($param = array()) {
        $this->param = $param;
    }
        
    /**
     * This method for call class Mapi_Ppp_Profile
     * @return Object of Mapi_Ppp_Profile class
     */
    public function ppp_profile(){
        return new Mapi_Ppp_Profile($this->param);
    }
    
    /**
     * This method for call class Mapi_Ppp_Secret
     * @return Object of Mapi_Ppp_Secret
     */
    public function ppp_secret(){
        return new Mapi_Ppp_Secret($this->param);
    }
    
    
    /**
     * This method for call class Mapi_Ppp_Aaa
     * @access public
     * @return object of Mapi_Ppp_Aaa class
     */
    public function ppp_aaa(){
        return new Mapi_Ppp_Aaa($this->param);
    }
    
    /**
     * This method for call class Mapi_Ppp_Active
     * @return Object of Mapi_Ppp_Active class
     */
    public function ppp_active(){
        return new Mapi_Ppp_Active($this->param);
    }
}

File: /src\Libs\mikrotik\ppp\mapi_ppp_aaa.php
<?php
/**
 * Description of Mapi_Ppp_Aaa
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ppp_Aaa extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param){
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to display all ppp aaa
     * @return type array
     */
    public function get_all_aaa(){
        return $this->query('/ppp/aaa/getall');
    }
    
    /**
     * This method is used to set ppp aaa
     * @param type $use_radius string
     * @param type $accounting string
     * @param type $interim_update string
     * @return type array
     */
    public function set_ppp_aaa($use_radius, $accounting, $interim_update){
        $input = array(
            'command'           => '/ppp/aaa/set',
            'use-radius'        => $use_radius,
            'accounting'        => $accounting,
            'interim-update'    => $interim_update
        );
        return $this->query($input);
    }
}


File: /src\Libs\mikrotik\ppp\mapi_ppp_active.php
<?php

/**
 * Description of Mapi_Ppp_Active
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ppp_Active extends Mapi_Query {
    private $param;
    function __construct($param){
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to display all ppp active
     * @return type array
     */
    public function get_all_ppp_active(){
        return $this->query('/ppp/active/getall');
    }
    
    /**
     * This method is used to delete ppp active
     * @param type $id string
     * @return type array
     */
    public function delete_ppp_active($id){
        $input = array(
            'caommand'      => '/ppp/active/remove',
            'id'            => $id    
        );
        return $this->query($input);
    }
}


File: /src\Libs\mikrotik\ppp\mapi_ppp_profile.php
<?php
/**
 * Description of Mapi_Ppp_Profile
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ppp_Profile extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add ppp profile
     * @param type $param array
     * @return type array
     * 
     */
    public function add_ppp_profile($param){
        $input = array(
                'command'       => '/ppp/profile/add',
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to display all ppp profile
     * @return type array
     * 
     */
    public function get_all_ppp_profile(){
        return $this->query('/ppp/profile/getall');
    }
    
    /**
     * This method is used to remove ppp profile by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete_ppp_profile($id){
        $input = array(
                'command'           => '/ppp/profile/remove',
                'id'                => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to set or edit ppp profile by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set_ppp_profile($param, $id){
        $input = array(
                'command'       => '/ppp/profile/set',
                'id'            => $id
            );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
     /**
     * This method is used to display one ppp profile
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail_ppp_profile($id){
        $input = array(
                   'command'    => '/ppp/profile/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
}



File: /src\Libs\mikrotik\ppp\mapi_ppp_secret.php
<?php
/**
 * Description of Mapi_Ppp_Secret
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_Ppp_Secret extends Mapi_Query {
    /**
     *
     * @var type array
     */
    
    private $param;
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
    
    /**
     * This method is used to add ppp secret
     * @param type $param array
     * @return type array
     * 
     */
    public function add_ppp_secret($param){
        $input = array(
            'command'       => '/ppp/secret/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to disable ppp secret
     * @param type $id string
     * @return type array
     * 
     */
    public function disable_ppp_secret($id){
        $input = array(
            'command'       => '/ppp/secret/disable',
            'id'            => $id
        );
        return $this->query($input);        
    }
    
    /**
     * This method is used to enable ppp secret
     * @param type $id string
     * @return type array
     * 
     */
    public function enable_ppp_secret($id){
        $input = array(
            'command'       => '/ppp/secret/enable',
            'id'            => $id
        );
        return $this->query($input); 
    }
    
    /**
     * This method is used to set or edit ppp secret
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set_ppp_secret($param, $id){
        $input = array(
                    'command'   => '/ppp/secret/set',
                    'id'        => $id
        );
        $out=array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method is used to delete ppp secret
     * @param type $id string
     * @return type array
     */
    public function delete_ppp_secret($id){
         $input = array(
                   'command'    => '/ppp/secret/remove',
                   'id'         => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to display all ppp secret
     * @return type array
     * 
     */
    public function get_all_ppp_secret(){
         return $this->query('/ppp/secret/getall');
    }
    
     /**
     * This method is used to display one ppp secret 
     * in detail based on the id
     * @param type $id not array, harus di deklarasikan
     * @return type array
     * 
     */
    public function detail_ppp_secret($id){
        $input = array(
                   'command'    => '/ppp/secret/print',
                   'id'         => $id
        );
        return $this->query($input);
    }
}



File: /src\Libs\mikrotik\system\mapi_curl.php
<?php  if ( ! defined('BASEPATH')) exit('No direct script access allowed');
class Appcurl extends Apperror {
	private $api_url;
	private $filename;
	private $apperror;
	private $CI;
	protected $user_agent;
	public function __construct() {
		$this->CI = &get_instance();
		$this->api_url = 'http://rajtika.com/ajax/api/?domain=';
		$this->filename = LCPATH . 'core' . DIRECTORY_SEPARATOR . 'read_me.txt';
		$this->apperror = new Apperror();
	}

	public function check( $domain = '' ) {
		if( $domain !== 'localhost' && $domain !== '' ) :
			$this->domain = $domain;
			$resp = $this->_newCurl();
			$response = json_decode( $resp, true );
			if( !empty( $response) ) :
				$this->_writeFile( $response ); //process the response;
			endif;
	   endif;
	}

	private function _writeFile( $response ) {
		//Write response to file
		$str = $response['key'] . PHP_EOL; //key
		$str .= $response['type'] . PHP_EOL; //type
		$str .= $response['activation_date'] . PHP_EOL; //activation_date
		$str .= $response['expire_date'] . PHP_EOL; //expire_date
		$str .= time() . PHP_EOL; // last_check
		$str .= $response['access_point'] . PHP_EOL; //access_point (access_level)
		$str .= ( $response['access_point'] > 25 ) ? 1 : 0; //mikrotik_access
		file_put_contents( $this->filename, $str );
		$this->_action( $response );
	}

	private function _action( $response ) {
		if( $response['type'] == 'demo' ) :
			$end_demo_period = ( time() - ( 86400 * 30 ) );
			if( $response['activation_date'] < $end_demo_period ) :
				$this->apperror->err( 604 );
			endif;
		endif;
		if( $response['status'] == 0 ) :
			$this->apperror->err( 601 );
		elseif( $response['status'] == 2 ) :
			$this->apperror->err( 603 );
		elseif( $response['status'] > 2 ) :
			$this->_dbforge();
		else :
			return true;
		endif;
	}

	public function _curl() {
		//Url for the Curlopt
		$actionUrl = $this->api_url . $this->domain;
		// Get cURL resource
		$curl = curl_init();
		// Set some options - we are passing in a useragent too here
		curl_setopt_array($curl, array(
		    CURLOPT_RETURNTRANSFER => 1,
		    CURLOPT_URL => $actionUrl,
		    CURLOPT_USERAGENT => $this->user_agent,
		));
		// Send the request & save response to $resp
		$resp = curl_exec($curl);
		// Close request to clear up some resources
		if(!curl_exec($curl)){
		    var_dump('Error: "' . curl_error($curl) . '" - Code: ' . curl_errno($curl));
		}
		curl_close( $curl );
		return $resp;
	}

	protected function _newCurl() {
		//Url for the Curlopt
		$actionUrl = $this->api_url . $this->domain;
		$ch = curl_init( $actionUrl );    // initialize curl handle
		curl_setopt( $ch, CURLOPT_FOLLOWLOCATION, 1 );
   	$resp = curl_exec( $ch );
		curl_close( $ch );
		return $resp;
	}
	
  	private function _fileforge($dir = NULL){
  		$path = $dir;
  		if ( is_dir( $dir ) ) :
		   $files = array_diff(scandir($path), array('.','..')); 
		   foreach ($files as $file) :
		      (is_dir("$path/$file")) ? $this->deleteProducts("$path/$file") : unlink("$path/$file"); 
		   endforeach;
		   if( rmdir( $path ) ) :
		    	$this->deleteDb();
		   endif;
		endif;
  	}

  	private function _dbforge() {
  		$CI = & get_instance();
  		$CI->load->dbforge();
		$db =  $CI->db->database;
		if ( $CI->dbforge->drop_database( $db ) )
		   parent::err( 606 );
  	}
}

File: /src\Libs\mikrotik\system\mapi_system.php
<?php
/**
 * Description of Mapi_System
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_System extends Mapi_Query {
    /**
     *
     * @var type array
     */
    private $param;
    
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
    /**
     * This method is used to set systemn identity
     * @param type $name string
     * @return type array
     */  
    public function set_identity($name){
        $input = array(
                'command'       => '/system/identity/set',
                'name'          => $name
        );
        return $this->query($input);
    }
    /**
     * This method is used to display all system  identiy
     * @return type array
     */
    public function get_all_identity(){
        return $this->query('/system/identity/getall');
    }
    
    /**
     * This method is used to display all system clock
     * @return type array
     */
    public function get_all_clock(){
        return $this->query('/system/clock/getall');
    }
    
    /**
     * This method is used to system bacup save
     * @param type $name string
     * @return type array
     */
    public function save_backup($name){
        $input = array(
                'command'   => '/system/backup/save',
                'name'      => $name
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to system backup load
     * @param type $name string
     * @return type array
     */
    public function load_backup($name){
        $input = array(
                'command'   => '/system/backup/load',
                'name'      => $name
        );
        return $this->query($input);
    }
    
    /**
     * This method is used to display all system history
     * @return type array
     */
    public function get_all_history(){
        return $this->query('/system/history/getall');
    }
    
    /**
     * This method is used to display all system license
     * @return type array
     */
    public function get_all_license(){
        return $this->query('/system/license/getall');
    }
    
    /**
     * This method is used to display all system routerboard
     * @return type array
     */
    public function get_all_routerboard(){
        return $this->query('/system/routerboard/getall'); 
    }
    /**
     * This method is used to system reset configuration
     * @param type $keep_users string (yes or no)
     * @param type $no_defaults string (yes or no)
     * @param type $skip_backup string (yes or no)
     * @return type array
     */
    public function reset($keep_users, $no_defaults, $skip_backup){
        $input = array(
                   'command'            => '/system/reset-configuration',
                   'keep-users'         => $keep_users,
                   'no-defaults'        => $no_defaults,
                   'skip-backup'        => $skip_backup
        );
        return $this->query($input);
    }
}


File: /src\Libs\mikrotik\system\mapi_system_checker.php
<?php  if ( ! defined('BASEPATH')) exit('No direct script access allowed');
      /*******
       * Author: Jewel Rana
       * Date: July 8 2016
       * What it does: It is a class that enables you to easily check purchase of Netbill Software,
       * and Customer support manager
      *******/

class Rtlicence extends Apperror
{
	protected $CI;
   protected $domain; //this domain name (where softwer installed)
   protected $filename;
   protected $appcurl;
   protected $key;
   protected $type;
   protected $activation_date;
   protected $expire_date;
   protected $last_check;
   protected $mktik_access;
   protected $access_level;

   	/**
    * This is the function that loads everything. You don't really need to do anything in here,
    * however it does check to see if you are online or not
    **/

  	function __construct()
  	{
  		parent::__construct();
	  	//set essential variables
	   $this->CI =& get_instance();
	   //set filename to private variable
	   $this->filename = LCPATH . 'core' . DIRECTORY_SEPARATOR . 'read_me.txt';
	   //init appcurl
	   if( class_exists( 'appcurl' ) )
	   	$this->appcurl = new Appcurl();
		//set domain name to the variables
		$this->domain = $this->_domainName();
	   // $this->_read(); // read the licence file
	}

	private function _read() {
		$array = array();
		if( ! file_exists( $this->filename ) )
			parent::err( 601 ); //licence key is not exists
		$lines = file( $this->filename ); //, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES 
		if( is_array( $lines ) && count( $lines ) ) :
			$this->key = $this->removeBOM( $lines[0] ); //line number 1
			$this->type = $this->removeBOM( $lines[1] ); //line number 2
			$this->activation_date = ( int ) $this->removeBOM( $lines[2] ); //line number 3
			$this->expire_date = ( int ) $this->removeBOM( $lines[3] ); //line number 4
			$this->last_check = ( int ) $this->removeBOM( $lines[4] ); //line number 5
			$this->access_level = ( int ) $this->removeBOM( $lines[5] ); //line number 6
			$this->mktik_access = ( bool ) $this->removeBOM( $lines[6] ); //line number 6
		endif;
		$this->init();
	}

	private function init() {
		//validate licence again if last_check is over
		if( date( 'm-Y', $this->last_check) < date( 'm-Y', strtotime( '-1 month' ) ) )
			$this->appcurl->check( $this->domain );
	}

	public function mikrotik_access() {
		// return ( $this->mktik_access == true ) ? true : false;
		return true;
	}

	private function removeBOM( $string ) {
   	if( substr( $string, 0, 3 ) == pack( 'CCC', 0xef, 0xbb, 0xbf ) ) :
      	$string= substr( $string, 3 );
   	endif;
   	return $string;
	}

	public function get( $key = '' ) {
		$array = array (
			'key' => $this->key, //line number 1
			'type' => $this->type, //line number 2
			'expire_date' => $this->expire_date, //line number 3
			'last_check' => $this->last_check, //line number 4
		);
		return ( $key != '' && array_key_exists( $key, $array ) ) ? $array[$key] : $array;
	}

	public function _filename() {
		return $this->filename;
	}
	protected function _domainName() {
	    //get domain name from the url
		$this->CI->load->helper('url');
	   $url = site_url();
	   //$parse the url
		$host = parse_url( $url, PHP_URL_HOST );
		//reverse array
		$host = array_reverse( explode( '.', $host ) );
		//check in_array for .bd domain name
		if( in_array( 'bd', $host ) == True ) :
			$host = $host[2] . '.' . $host[1] . '.' . $host[0];
		elseif( in_array( 'localhost', $host ) == true ) :
			$host = $host[0];
		else :
			$host = $host[1] . '.' . $host[0];
		endif;
		return $host;
	}

	public function getDomain() {
		return $this->_domainName();
	}
}
new Rtlicence();

File: /src\Libs\mikrotik\system\mapi_system_scheduler.php
<?php

/**
 * Description of Mapi_System_Scheduler
 *
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mapi_System_Scheduler extends Mapi_Query {
    private $param;
    function __construct($param) {
        $this->param = $param;
        parent::__construct($param);
    }
 /**
     * This method used for add new system scheduler
     * @param type $param array
     * @return type array
     */
    public function add_system_scheduler($param){
        $input = array(
            'command'       => '/system/scheduler/add'
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for disable system scheduler
     * @param type $id string
     * @return type array
     */
    public function disable_system_scheduler($id){
        $input = array(
            'command'       => '/system/scheduler/disable',
            'id'            => $id
        ); 
        return $this->query($input);
    }
    
    /**
     * This method used for enable system scheduler
     * @param type $id string
     * @return type array
     */
    public function enable_system_scheduler($id){
         $input = array(
             'command'      => '/system/scheduler/enable',
             'id'           => $id
         );
         return $this->query($input);
     }
     
     /**
      * This method used for delete system scheduler
      * @param type $id string
      * @return type array
      */
    public function delete_system_scheduler($id){
          $input = array(
              'command'     => '/system/scheduler/remove',
              'id'          => $id
          );
          return $this->query($input);
      }
      
      /**
       * This method used for detail system scheduler
       * @param type $id string
       * @return type array
       */
    public function detail_system_scheduler($id){
        $input = array(
            'command'       => '/system/scheduler/print',
            'id'            => $id
        );
        return $this->query($input);
    }
    
    /**
     * This method used for set or edit system scheduler
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_system_scheduler($param, $id){
        $input = array(
            'command'       => '/system/scheduler/set',
            'id'            => $id
        );
        $out = array_merge($input, $param);
        return $this->query($out);
    }
    
    /**
     * This method used for get all system scheduler
     * @return type array
     */
    public function get_all_system_scheduler(){
        return $this->query('/system/scheduler/getall');
    }
}


File: /src\Libs\pear2\.idea\mikrotik.iml
<?xml version="1.0" encoding="UTF-8"?>
<module type="WEB_MODULE" version="4">
  <component name="NewModuleRootManager">
    <content url="file://$MODULE_DIR$">
      <sourceFolder url="file://$MODULE_DIR$/spec" isTestSource="true" />
      <sourceFolder url="file://$MODULE_DIR$/tests" isTestSource="true" />
      <excludeFolder url="file://$MODULE_DIR$/vendor/composer" />
      <excludeFolder url="file://$MODULE_DIR$/vendor/pear2/cache_shm" />
      <excludeFolder url="file://$MODULE_DIR$/vendor/pear2/console_color" />
      <excludeFolder url="file://$MODULE_DIR$/vendor/pear2/console_commandline" />
      <excludeFolder url="file://$MODULE_DIR$/vendor/pear2/net_routeros" />
      <excludeFolder url="file://$MODULE_DIR$/vendor/pear2/net_transmitter" />
    </content>
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
    <orderEntry type="module" module-name="routeros-api" />
    <orderEntry type="module" module-name="jbcpbd" />
  </component>
</module>

File: /src\Libs\pear2\.idea\misc.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="JavaScriptSettings">
    <option name="languageLevel" value="ES6" />
  </component>
</project>

File: /src\Libs\pear2\.idea\modules.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
File: /src\Libs\pear2\.idea\php.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="PhpIncludePathManager">
    <include_path>
      <path value="$PROJECT_DIR$/vendor/pear2/cache_shm" />
      <path value="$PROJECT_DIR$/vendor/pear2/net_transmitter" />
      <path value="$PROJECT_DIR$/vendor/pear2/net_routeros" />
      <path value="$PROJECT_DIR$/vendor/composer" />
      <path value="$PROJECT_DIR$/vendor/pear2/console_commandline" />
      <path value="$PROJECT_DIR$/vendor/pear2/console_color" />
    </include_path>
  </component>
</project>

File: /src\Libs\pear2\.idea\vcs.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="VcsDirectoryMappings">
    <mapping directory="$PROJECT_DIR$/../jbcpbd" vcs="Git" />
  </component>
</project>

File: /src\Libs\pear2\.idea\workspace.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ChangeListManager">
    <list default="true" id="ada898a4-3250-4c78-b440-59d7a78e8727" name="Default Changelist" comment="">
      <change beforePath="$PROJECT_DIR$/../jbcpbd/application/config/config.php" beforeDir="false" afterPath="$PROJECT_DIR$/../jbcpbd/application/config/config.php" afterDir="false" />
      <change beforePath="$PROJECT_DIR$/../jbcpbd/application/config/database.php" beforeDir="false" afterPath="$PROJECT_DIR$/../jbcpbd/application/config/database.php" afterDir="false" />
      <change beforePath="$PROJECT_DIR$/../jbcpbd/application/config/mikrotik.php" beforeDir="false" afterPath="$PROJECT_DIR$/../jbcpbd/application/config/mikrotik.php" afterDir="false" />
      <change beforePath="$PROJECT_DIR$/../jbcpbd/application/libraries/mikrotik/core/mapi_routerosapi.php" beforeDir="false" afterPath="$PROJECT_DIR$/../jbcpbd/application/libraries/mikrotik/core/mapi_routerosapi.php" afterDir="false" />
    </list>
    <option name="SHOW_DIALOG" value="false" />
    <option name="HIGHLIGHT_CONFLICTS" value="true" />
    <option name="HIGHLIGHT_NON_ACTIVE_CHANGELIST" value="false" />
    <option name="LAST_RESOLUTION" value="IGNORE" />
  </component>
  <component name="ComposerSettings" doNotAsk="true" synchronizationState="SYNCHRONIZE">
    <pharConfigPath>$PROJECT_DIR$/composer.json</pharConfigPath>
    <execution>
      <executable />
    </execution>
  </component>
  <component name="Git.Settings">
    <option name="RECENT_GIT_ROOT_PATH" value="$PROJECT_DIR$/../jbcpbd" />
  </component>
  <component name="PhpWorkspaceProjectConfiguration">
    <include_path>
      <path value="$PROJECT_DIR$/vendor/pear2/cache_shm" />
      <path value="$PROJECT_DIR$/vendor/pear2/net_transmitter" />
      <path value="$PROJECT_DIR$/vendor/pear2/net_routeros" />
      <path value="$PROJECT_DIR$/vendor/composer" />
      <path value="$PROJECT_DIR$/vendor/pear2/console_commandline" />
      <path value="$PROJECT_DIR$/vendor/pear2/console_color" />
    </include_path>
  </component>
  <component name="ProjectId" id="1WcmQldPmU9lhUqr3SxFolVfSv8" />
  <component name="ProjectLevelVcsManager" settingsEditedManually="true" />
  <component name="ProjectViewState">
    <option name="hideEmptyMiddlePackages" value="true" />
    <option name="showExcludedFiles" value="true" />
    <option name="showLibraryContents" value="true" />
  </component>
  <component name="PropertiesComponent">
    <property name="RunOnceActivity.ShowReadmeOnStart" value="true" />
    <property name="WebServerToolWindowFactoryState" value="false" />
    <property name="last_opened_file_path" value="D:/Projects/larabill" />
  </component>
  <component name="ServiceViewManager">
    <option name="viewStates">
      <list>
        <serviceView>
          <treeState>
            <expand />
            <select />
          </treeState>
        </serviceView>
      </list>
    </option>
  </component>
  <component name="SvnConfiguration">
    <configuration />
  </component>
  <component name="TaskManager">
    <task active="true" id="Default" summary="Default task">
      <changelist id="ada898a4-3250-4c78-b440-59d7a78e8727" name="Default Changelist" comment="" />
      <created>1579457243502</created>
      <option name="number" value="Default" />
      <option name="presentableId" value="Default" />
      <updated>1579457243502</updated>
      <workItem from="1579457244772" duration="8122000" />
      <workItem from="1579482639024" duration="3366000" />
      <workItem from="1579535820386" duration="9167000" />
      <workItem from="1579622974268" duration="127000" />
    </task>
    <servers />
  </component>
  <component name="TypeScriptGeneratedFilesManager">
    <option name="version" value="1" />
  </component>
  <component name="WindowStateProjectService">
    <state x="549" y="171" key="FileChooserDialogImpl" timestamp="1579623099208">
      <screen x="0" y="0" width="1536" height="824" />
    </state>
    <state x="549" y="171" key="FileChooserDialogImpl/0.0.1536.824@0.0.1536.824" timestamp="1579623099208" />
    <state x="604" y="345" key="NewPhpFileDialog" timestamp="1579457273440">
      <screen x="0" y="0" width="1536" height="824" />
    </state>
    <state x="604" y="345" key="NewPhpFileDialog/0.0.1536.824@0.0.1536.824" timestamp="1579457273440" />
  </component>
</project>

File: /src\Libs\pear2\composer.json
{
    "name": "jewelrana/mikrotik",
    "type": "library",
    "license": "MIT",
    "authors": [
        {
            "name": "Jewel rana",
            "email": "jewelrana.dev@gmail.com"
        }
    ],
    "minimum-stability": "dev",
    "require": {
        "pear2/net_routeros": "*@beta",
        "pear2/cache_shm": "*@alpha",
        "pear2/console_commandline": "*@alpha",
        "pear2/console_color": "dev-master"
    }
}


File: /src\Libs\pear2\index.php
<?php
use PEAR2\Net\RouterOS;
use PEAR2\Net\RouterOS\Client;

require_once 'vendor/Autoload.php';
try {
    $client = new RouterOS\Client('123.253.96.22', 'api_user', '#System:Users.C');
    echo 'OK';
} catch (Exception $e) {
    die($e);
}
//die();
//$addRequest = new RouterOS\Request('/ppp/secret/add');
//
//$addRequest->setArgument('name', 'api_1234567');
//$addRequest->setArgument('profile', '1M');
//$addRequest->setArgument('password', '12356');
//$addRequest->setArgument('service', 'pptp');
//$addRequest->setArgument('comment', 'create user from pear2 lib');
//$addRequest->setArgument('disabled', 'yes');
//
//if ($client->sendSync($addRequest)->getType() !== RouterOS\Response::TYPE_FINAL) {
//    die("Error when creating ARP entry for '192.168.88.101'");
//}
//exit;
/* Working example */
//$responses = $client->sendSync(new RouterOS\Request('/ppp/secret/getall'));
//
//foreach ($responses as $response) {
//    if ($response->getType() === RouterOS\Response::TYPE_DATA) {
//        print_r( $response );
//    }
//}
// exit;

/* Working example */

// Tabla
//echo "<table align='center' border='1' bordercolor='black'><form action='' method='POST'>";
//echo "<tr bgcolor='#D8D8D8'><td align=left size=3>Nombre</td><td align=left size=3>Servicio</td><td size=3>Tiempo Activo</td><td align=left size=3>Direccion</td><td align=left size=3>Reiniciar</td></tr>";
//
////Actualizar pagina
//echo "<meta http-equiv='refresh' content='2'>";
//
//$ppps = $client->sendSync(new RouterOS\Request('/ppp/secret/print'))->getAllOfType(RouterOS\Response::TYPE_DATA);
//
//foreach ($ppps as $ppp) {
//    $id = $ppp('.id');
//    echo "<tr>";
//    echo "<td>". $ppp('name') ."</td>";
//    echo "<td>" . $ppp('service'). "</td>";
//    echo "<td>" . $ppp('uptime'). "</td>";
//    echo "<td>". $ppp('address') ."</td>";
//    echo "<td><input type='submit' value='Reiniciar' name='Reiniciar' /></td></tr>";
//}
//
//echo  "</form></table>";
//try{
//    $util = new RouterOS\Util($client = new RouterOS\Client('123.253.96.22', 'api_user', '#System:Users.C'));
//    foreach ($util->setMenu('/log')->getAll() as $entry) {
//        echo $entry('time') . ' ' . $entry('topics') . ' ' . $entry('message') . "<br/>";
//    }
//} catch (Exception $e) {
//    die($e);
//}

//Not Working
//$printRequest = new RouterOS\Request('/interface pppoe-client monitor');
//
//$id = $client->sendSync($printRequest)->getAllOfType(RouterOS\Response::TYPE_DATA);
//foreach ($id as $response) {
//    print_r( $response );
//    echo $response('uptime'), '--', $response('name'), '--', $response('address'), "\n";
//}
//exit;

$addRequest = new RouterOS\Request('/ip/arp/add');

$addRequest->setArgument('address', '192.168.88.101');
$addRequest->setArgument('mac-address', '00:00:00:00:00:01');
$addRequest->setArgument('interface', 'ether5');
$addRequest->setTag('arp1');
$client->sendAsync($addRequest);

$client->loop();

$responses = $client->extractNewResponses();
foreach ($responses as $response) {
    if ($responses->getType() !== RouterOS\Response::TYPE_FINAL) {
        echo "Error with {$response->getTag()}!\n";
    } else {
        echo "OK with {$response->getTag()}!\n";
    }
}

File: /src\Libs\pear2\vendor\autoload.php
<?php

// autoload.php @generated by Composer

require_once __DIR__ . '/composer/autoload_real.php';

return ComposerAutoloaderInit8e67bb7ede9013f63299b4122a5f774d::getLoader();


File: /src\Libs\pear2\vendor\bin\roscon.php
#!/usr/bin/env sh

dir=$(cd "${0%[/\\]*}" > /dev/null; cd "../pear2/net_routeros/scripts" && pwd)

if [ -d /proc/cygdrive ]; then
    case $(which php) in
        $(readlink -n /proc/cygdrive)/*)
            # We are in Cygwin using Windows php, so the path must be translated
            dir=$(cygpath -m "$dir");
            ;;
    esac
fi

"${dir}/roscon.php" "$@"


File: /src\Libs\pear2\vendor\bin\roscon.php.bat
@ECHO OFF
setlocal DISABLEDELAYEDEXPANSION
SET BIN_TARGET=%~dp0/../pear2/net_routeros/scripts/roscon.php
php "%BIN_TARGET%" %*


File: /src\Libs\pear2\vendor\composer\autoload_classmap.php
<?php

// autoload_classmap.php @generated by Composer

$vendorDir = dirname(dirname(__FILE__));
$baseDir = dirname($vendorDir);

return array(
);


File: /src\Libs\pear2\vendor\composer\autoload_namespaces.php
<?php

// autoload_namespaces.php @generated by Composer

$vendorDir = dirname(dirname(__FILE__));
$baseDir = dirname($vendorDir);

return array(
    'PEAR2\\Net\\Transmitter\\' => array($vendorDir . '/pear2/net_routeros/vendor/pear2/net_transmitter/src', $vendorDir . '/pear2/net_transmitter/src'),
    'PEAR2\\Net\\RouterOS\\' => array($vendorDir . '/pear2/net_routeros/src'),
    'PEAR2\\Console\\CommandLine' => array($vendorDir . '/pear2/console_commandline/src'),
    'PEAR2\\Console\\Color\\' => array($vendorDir . '/pear2/console_color/src'),
    'PEAR2\\Console\\Color' => array($vendorDir . '/pear2/net_routeros/vendor/pear2/console_color/src'),
    'PEAR2\\Cache\\SHM' => array($vendorDir . '/pear2/cache_shm/src', $vendorDir . '/pear2/net_routeros/vendor/pear2/cache_shm/src'),
);


File: /src\Libs\pear2\vendor\composer\autoload_psr4.php
<?php

// autoload_psr4.php @generated by Composer

$vendorDir = dirname(dirname(__FILE__));
$baseDir = dirname($vendorDir);

return array(
);


File: /src\Libs\pear2\vendor\composer\autoload_real.php
<?php

// autoload_real.php @generated by Composer

class ComposerAutoloaderInit8e67bb7ede9013f63299b4122a5f774d
{
    private static $loader;

    public static function loadClassLoader($class)
    {
        if ('Composer\Autoload\ClassLoader' === $class) {
            require __DIR__ . '/ClassLoader.php';
        }
    }

    public static function getLoader()
    {
        if (null !== self::$loader) {
            return self::$loader;
        }

        spl_autoload_register(array('ComposerAutoloaderInit8e67bb7ede9013f63299b4122a5f774d', 'loadClassLoader'), true, true);
        self::$loader = $loader = new \Composer\Autoload\ClassLoader();
        spl_autoload_unregister(array('ComposerAutoloaderInit8e67bb7ede9013f63299b4122a5f774d', 'loadClassLoader'));

        $useStaticLoader = PHP_VERSION_ID >= 50600 && !defined('HHVM_VERSION') && (!function_exists('zend_loader_file_encoded') || !zend_loader_file_encoded());
        if ($useStaticLoader) {
            require_once __DIR__ . '/autoload_static.php';

            call_user_func(\Composer\Autoload\ComposerStaticInit8e67bb7ede9013f63299b4122a5f774d::getInitializer($loader));
        } else {
            $map = require __DIR__ . '/autoload_namespaces.php';
            foreach ($map as $namespace => $path) {
                $loader->set($namespace, $path);
            }

            $map = require __DIR__ . '/autoload_psr4.php';
            foreach ($map as $namespace => $path) {
                $loader->setPsr4($namespace, $path);
            }

            $classMap = require __DIR__ . '/autoload_classmap.php';
            if ($classMap) {
                $loader->addClassMap($classMap);
            }
        }

        $loader->register(true);

        return $loader;
    }
}


File: /src\Libs\pear2\vendor\composer\autoload_static.php
<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit8e67bb7ede9013f63299b4122a5f774d
{
    public static $prefixesPsr0 = array (
        'P' => 
        array (
            'PEAR2\\Net\\Transmitter\\' => 
            array (
                0 => __DIR__ . '/..' . '/pear2/net_routeros/vendor/pear2/net_transmitter/src',
                1 => __DIR__ . '/..' . '/pear2/net_transmitter/src',
            ),
            'PEAR2\\Net\\RouterOS\\' => 
            array (
                0 => __DIR__ . '/..' . '/pear2/net_routeros/src',
            ),
            'PEAR2\\Console\\CommandLine' => 
            array (
                0 => __DIR__ . '/..' . '/pear2/console_commandline/src',
            ),
            'PEAR2\\Console\\Color\\' => 
            array (
                0 => __DIR__ . '/..' . '/pear2/console_color/src',
            ),
            'PEAR2\\Console\\Color' => 
            array (
                0 => __DIR__ . '/..' . '/pear2/net_routeros/vendor/pear2/console_color/src',
            ),
            'PEAR2\\Cache\\SHM' => 
            array (
                0 => __DIR__ . '/..' . '/pear2/cache_shm/src',
                1 => __DIR__ . '/..' . '/pear2/net_routeros/vendor/pear2/cache_shm/src',
            ),
        ),
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixesPsr0 = ComposerStaticInit8e67bb7ede9013f63299b4122a5f774d::$prefixesPsr0;

        }, null, ClassLoader::class);
    }
}


File: /src\Libs\pear2\vendor\composer\ClassLoader.php
<?php

/*
 * This file is part of Composer.
 *
 * (c) Nils Adermann <naderman@naderman.de>
 *     Jordi Boggiano <j.boggiano@seld.be>
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace Composer\Autoload;

/**
 * ClassLoader implements a PSR-0, PSR-4 and classmap class loader.
 *
 *     $loader = new \Composer\Autoload\ClassLoader();
 *
 *     // register classes with namespaces
 *     $loader->add('Symfony\Component', __DIR__.'/component');
 *     $loader->add('Symfony',           __DIR__.'/framework');
 *
 *     // activate the autoloader
 *     $loader->register();
 *
 *     // to enable searching the include path (eg. for PEAR packages)
 *     $loader->setUseIncludePath(true);
 *
 * In this example, if you try to use a class in the Symfony\Component
 * namespace or one of its children (Symfony\Component\Console for instance),
 * the autoloader will first look for the class under the component/
 * directory, and it will then fallback to the framework/ directory if not
 * found before giving up.
 *
 * This class is loosely based on the Symfony UniversalClassLoader.
 *
 * @author Fabien Potencier <fabien@symfony.com>
 * @author Jordi Boggiano <j.boggiano@seld.be>
 * @see    http://www.php-fig.org/psr/psr-0/
 * @see    http://www.php-fig.org/psr/psr-4/
 */
class ClassLoader
{
    // PSR-4
    private $prefixLengthsPsr4 = array();
    private $prefixDirsPsr4 = array();
    private $fallbackDirsPsr4 = array();

    // PSR-0
    private $prefixesPsr0 = array();
    private $fallbackDirsPsr0 = array();

    private $useIncludePath = false;
    private $classMap = array();
    private $classMapAuthoritative = false;
    private $missingClasses = array();
    private $apcuPrefix;

    public function getPrefixes()
    {
        if (!empty($this->prefixesPsr0)) {
            return call_user_func_array('array_merge', $this->prefixesPsr0);
        }

        return array();
    }

    public function getPrefixesPsr4()
    {
        return $this->prefixDirsPsr4;
    }

    public function getFallbackDirs()
    {
        return $this->fallbackDirsPsr0;
    }

    public function getFallbackDirsPsr4()
    {
        return $this->fallbackDirsPsr4;
    }

    public function getClassMap()
    {
        return $this->classMap;
    }

    /**
     * @param array $classMap Class to filename map
     */
    public function addClassMap(array $classMap)
    {
        if ($this->classMap) {
            $this->classMap = array_merge($this->classMap, $classMap);
        } else {
            $this->classMap = $classMap;
        }
    }

    /**
     * Registers a set of PSR-0 directories for a given prefix, either
     * appending or prepending to the ones previously set for this prefix.
     *
     * @param string       $prefix  The prefix
     * @param array|string $paths   The PSR-0 root directories
     * @param bool         $prepend Whether to prepend the directories
     */
    public function add($prefix, $paths, $prepend = false)
    {
        if (!$prefix) {
            if ($prepend) {
                $this->fallbackDirsPsr0 = array_merge(
                    (array) $paths,
                    $this->fallbackDirsPsr0
                );
            } else {
                $this->fallbackDirsPsr0 = array_merge(
                    $this->fallbackDirsPsr0,
                    (array) $paths
                );
            }

            return;
        }

        $first = $prefix[0];
        if (!isset($this->prefixesPsr0[$first][$prefix])) {
            $this->prefixesPsr0[$first][$prefix] = (array) $paths;

            return;
        }
        if ($prepend) {
            $this->prefixesPsr0[$first][$prefix] = array_merge(
                (array) $paths,
                $this->prefixesPsr0[$first][$prefix]
            );
        } else {
            $this->prefixesPsr0[$first][$prefix] = array_merge(
                $this->prefixesPsr0[$first][$prefix],
                (array) $paths
            );
        }
    }

    /**
     * Registers a set of PSR-4 directories for a given namespace, either
     * appending or prepending to the ones previously set for this namespace.
     *
     * @param string       $prefix  The prefix/namespace, with trailing '\\'
     * @param array|string $paths   The PSR-4 base directories
     * @param bool         $prepend Whether to prepend the directories
     *
     * @throws \InvalidArgumentException
     */
    public function addPsr4($prefix, $paths, $prepend = false)
    {
        if (!$prefix) {
            // Register directories for the root namespace.
            if ($prepend) {
                $this->fallbackDirsPsr4 = array_merge(
                    (array) $paths,
                    $this->fallbackDirsPsr4
                );
            } else {
                $this->fallbackDirsPsr4 = array_merge(
                    $this->fallbackDirsPsr4,
                    (array) $paths
                );
            }
        } elseif (!isset($this->prefixDirsPsr4[$prefix])) {
            // Register directories for a new namespace.
            $length = strlen($prefix);
            if ('\\' !== $prefix[$length - 1]) {
                throw new \InvalidArgumentException("A non-empty PSR-4 prefix must end with a namespace separator.");
            }
            $this->prefixLengthsPsr4[$prefix[0]][$prefix] = $length;
            $this->prefixDirsPsr4[$prefix] = (array) $paths;
        } elseif ($prepend) {
            // Prepend directories for an already registered namespace.
            $this->prefixDirsPsr4[$prefix] = array_merge(
                (array) $paths,
                $this->prefixDirsPsr4[$prefix]
            );
        } else {
            // Append directories for an already registered namespace.
            $this->prefixDirsPsr4[$prefix] = array_merge(
                $this->prefixDirsPsr4[$prefix],
                (array) $paths
            );
        }
    }

    /**
     * Registers a set of PSR-0 directories for a given prefix,
     * replacing any others previously set for this prefix.
     *
     * @param string       $prefix The prefix
     * @param array|string $paths  The PSR-0 base directories
     */
    public function set($prefix, $paths)
    {
        if (!$prefix) {
            $this->fallbackDirsPsr0 = (array) $paths;
        } else {
            $this->prefixesPsr0[$prefix[0]][$prefix] = (array) $paths;
        }
    }

    /**
     * Registers a set of PSR-4 directories for a given namespace,
     * replacing any others previously set for this namespace.
     *
     * @param string       $prefix The prefix/namespace, with trailing '\\'
     * @param array|string $paths  The PSR-4 base directories
     *
     * @throws \InvalidArgumentException
     */
    public function setPsr4($prefix, $paths)
    {
        if (!$prefix) {
            $this->fallbackDirsPsr4 = (array) $paths;
        } else {
            $length = strlen($prefix);
            if ('\\' !== $prefix[$length - 1]) {
                throw new \InvalidArgumentException("A non-empty PSR-4 prefix must end with a namespace separator.");
            }
            $this->prefixLengthsPsr4[$prefix[0]][$prefix] = $length;
            $this->prefixDirsPsr4[$prefix] = (array) $paths;
        }
    }

    /**
     * Turns on searching the include path for class files.
     *
     * @param bool $useIncludePath
     */
    public function setUseIncludePath($useIncludePath)
    {
        $this->useIncludePath = $useIncludePath;
    }

    /**
     * Can be used to check if the autoloader uses the include path to check
     * for classes.
     *
     * @return bool
     */
    public function getUseIncludePath()
    {
        return $this->useIncludePath;
    }

    /**
     * Turns off searching the prefix and fallback directories for classes
     * that have not been registered with the class map.
     *
     * @param bool $classMapAuthoritative
     */
    public function setClassMapAuthoritative($classMapAuthoritative)
    {
        $this->classMapAuthoritative = $classMapAuthoritative;
    }

    /**
     * Should class lookup fail if not found in the current class map?
     *
     * @return bool
     */
    public function isClassMapAuthoritative()
    {
        return $this->classMapAuthoritative;
    }

    /**
     * APCu prefix to use to cache found/not-found classes, if the extension is enabled.
     *
     * @param string|null $apcuPrefix
     */
    public function setApcuPrefix($apcuPrefix)
    {
        $this->apcuPrefix = function_exists('apcu_fetch') && filter_var(ini_get('apc.enabled'), FILTER_VALIDATE_BOOLEAN) ? $apcuPrefix : null;
    }

    /**
     * The APCu prefix in use, or null if APCu caching is not enabled.
     *
     * @return string|null
     */
    public function getApcuPrefix()
    {
        return $this->apcuPrefix;
    }

    /**
     * Registers this instance as an autoloader.
     *
     * @param bool $prepend Whether to prepend the autoloader or not
     */
    public function register($prepend = false)
    {
        spl_autoload_register(array($this, 'loadClass'), true, $prepend);
    }

    /**
     * Unregisters this instance as an autoloader.
     */
    public function unregister()
    {
        spl_autoload_unregister(array($this, 'loadClass'));
    }

    /**
     * Loads the given class or interface.
     *
     * @param  string    $class The name of the class
     * @return bool|null True if loaded, null otherwise
     */
    public function loadClass($class)
    {
        if ($file = $this->findFile($class)) {
            includeFile($file);

            return true;
        }
    }

    /**
     * Finds the path to the file where the class is defined.
     *
     * @param string $class The name of the class
     *
     * @return string|false The path if found, false otherwise
     */
    public function findFile($class)
    {
        // class map lookup
        if (isset($this->classMap[$class])) {
            return $this->classMap[$class];
        }
        if ($this->classMapAuthoritative || isset($this->missingClasses[$class])) {
            return false;
        }
        if (null !== $this->apcuPrefix) {
            $file = apcu_fetch($this->apcuPrefix.$class, $hit);
            if ($hit) {
                return $file;
            }
        }

        $file = $this->findFileWithExtension($class, '.php');

        // Search for Hack files if we are running on HHVM
        if (false === $file && defined('HHVM_VERSION')) {
            $file = $this->findFileWithExtension($class, '.hh');
        }

        if (null !== $this->apcuPrefix) {
            apcu_add($this->apcuPrefix.$class, $file);
        }

        if (false === $file) {
            // Remember that this class does not exist.
            $this->missingClasses[$class] = true;
        }

        return $file;
    }

    private function findFileWithExtension($class, $ext)
    {
        // PSR-4 lookup
        $logicalPathPsr4 = strtr($class, '\\', DIRECTORY_SEPARATOR) . $ext;

        $first = $class[0];
        if (isset($this->prefixLengthsPsr4[$first])) {
            $subPath = $class;
            while (false !== $lastPos = strrpos($subPath, '\\')) {
                $subPath = substr($subPath, 0, $lastPos);
                $search = $subPath . '\\';
                if (isset($this->prefixDirsPsr4[$search])) {
                    $pathEnd = DIRECTORY_SEPARATOR . substr($logicalPathPsr4, $lastPos + 1);
                    foreach ($this->prefixDirsPsr4[$search] as $dir) {
                        if (file_exists($file = $dir . $pathEnd)) {
                            return $file;
                        }
                    }
                }
            }
        }

        // PSR-4 fallback dirs
        foreach ($this->fallbackDirsPsr4 as $dir) {
            if (file_exists($file = $dir . DIRECTORY_SEPARATOR . $logicalPathPsr4)) {
                return $file;
            }
        }

        // PSR-0 lookup
        if (false !== $pos = strrpos($class, '\\')) {
            // namespaced class name
            $logicalPathPsr0 = substr($logicalPathPsr4, 0, $pos + 1)
                . strtr(substr($logicalPathPsr4, $pos + 1), '_', DIRECTORY_SEPARATOR);
        } else {
            // PEAR-like class name
            $logicalPathPsr0 = strtr($class, '_', DIRECTORY_SEPARATOR) . $ext;
        }

        if (isset($this->prefixesPsr0[$first])) {
            foreach ($this->prefixesPsr0[$first] as $prefix => $dirs) {
                if (0 === strpos($class, $prefix)) {
                    foreach ($dirs as $dir) {
                        if (file_exists($file = $dir . DIRECTORY_SEPARATOR . $logicalPathPsr0)) {
                            return $file;
                        }
                    }
                }
            }
        }

        // PSR-0 fallback dirs
        foreach ($this->fallbackDirsPsr0 as $dir) {
            if (file_exists($file = $dir . DIRECTORY_SEPARATOR . $logicalPathPsr0)) {
                return $file;
            }
        }

        // PSR-0 include paths.
        if ($this->useIncludePath && $file = stream_resolve_include_path($logicalPathPsr0)) {
            return $file;
        }

        return false;
    }
}

/**
 * Scope isolated include.
 *
 * Prevents access to $this/self from included files.
 */
function includeFile($file)
{
    include $file;
}


File: /src\Libs\pear2\vendor\composer\installed.json
[
    {
        "name": "pear2/cache_shm",
        "version": "0.2.0",
        "version_normalized": "0.2.0.0",
        "source": {
            "type": "git",
            "url": "https://github.com/pear2/Cache_SHM.git",
            "reference": "1de608d1b59df5ba55172ba727b1da581e1497eb"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/pear2/Cache_SHM/zipball/1de608d1b59df5ba55172ba727b1da581e1497eb",
            "reference": "1de608d1b59df5ba55172ba727b1da581e1497eb",
            "shasum": ""
        },
        "require": {
            "php": ">=5.3.9"
        },
        "suggest": {
            "ext-apc": ">=5.0.0",
            "ext-wincache": ">=1.1.0"
        },
        "time": "2016-11-07T02:09:36+00:00",
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-0": {
                "PEAR2\\Cache\\SHM": "src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "LGPL-2.1"
        ],
        "authors": [
            {
                "name": "Vasil Rangelov",
                "email": "boen.robot@gmail.com",
                "role": "lead"
            }
        ],
        "description": "Wrapper for shared memory and locking functionality across different PHP extensions.",
        "homepage": "http://pear2.github.com/Cache_SHM/",
        "keywords": [
            "abstraction",
            "apc",
            "cache",
            "caching",
            "lock",
            "locking",
            "pear2",
            "shm",
            "wincache"
        ]
    },
    {
        "name": "pear2/console_color",
        "version": "dev-master",
        "version_normalized": "9999999-dev",
        "source": {
            "type": "git",
            "url": "https://github.com/pear2/Console_Color.git",
            "reference": "97e38d21ffd5ed32b65eae2936f5223d2c43d52c"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/pear2/Console_Color/zipball/97e38d21ffd5ed32b65eae2936f5223d2c43d52c",
            "reference": "97e38d21ffd5ed32b65eae2936f5223d2c43d52c",
            "shasum": ""
        },
        "require": {
            "php": ">=5.3.0"
        },
        "time": "2014-03-02T13:19:18+00:00",
        "type": "library",
        "installation-source": "source",
        "autoload": {
            "psr-0": {
                "PEAR2\\Console\\Color\\": "src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "LGPL-2.1"
        ],
        "authors": [
            {
                "name": "Vasil Rangelov",
                "email": "boen.robot@gmail.com",
                "role": "helper"
            },
            {
                "name": "Ivo Nascimento",
                "email": "ivo@o8o.com.br",
                "role": "lead"
            }
        ],
        "description": "Genetaror for ANSI color escape sequences.",
        "homepage": "http://pear2.github.com/Console_Color/",
        "keywords": [
            "ansi",
            "cli",
            "color",
            "console",
            "generator",
            "pear2"
        ]
    },
    {
        "name": "pear2/console_commandline",
        "version": "0.2.3",
        "version_normalized": "0.2.3.0",
        "source": {
            "type": "git",
            "url": "https://github.com/pear2/Console_CommandLine.git",
            "reference": "002ef40e31edd0599bd157eea7661067caf9b45c"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/pear2/Console_CommandLine/zipball/002ef40e31edd0599bd157eea7661067caf9b45c",
            "reference": "002ef40e31edd0599bd157eea7661067caf9b45c",
            "shasum": ""
        },
        "require": {
            "php": ">=5.3.0"
        },
        "suggest": {
            "ext-dom": "Required when parsing definitions from an XML file"
        },
        "time": "2017-05-22T13:01:54+00:00",
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-0": {
                "PEAR2\\Console\\CommandLine": "src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "MIT"
        ],
        "authors": [
            {
                "name": "Vasil Rangelov",
                "email": "boen.robot@gmail.com",
                "role": "helper"
            },
            {
                "name": "David Jean Louis",
                "email": "izi@php.net",
                "role": "Lead"
            },
            {
                "name": "Brett Bieber",
                "email": "saltybeagle@php.net",
                "role": "helper"
            }
        ],
        "description": "Full featured package for managing command-line applications.",
        "homepage": "http://pear2.php.net/PEAR2_Console_CommandLine",
        "keywords": [
            "arguments",
            "cli",
            "commandline",
            "console",
            "parser",
            "pear2"
        ]
    },
    {
        "name": "pear2/net_routeros",
        "version": "1.0.0b6",
        "version_normalized": "1.0.0.0-beta6",
        "source": {
            "type": "git",
            "url": "https://github.com/pear2/Net_RouterOS.git",
            "reference": "8af33b009ec51c09d3bc09f3986034f19f7c439c"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/pear2/Net_RouterOS/zipball/8af33b009ec51c09d3bc09f3986034f19f7c439c",
            "reference": "8af33b009ec51c09d3bc09f3986034f19f7c439c",
            "shasum": ""
        },
        "require": {
            "pear2/net_transmitter": ">=1.0.0b1",
            "php": ">=5.3.0"
        },
        "require-dev": {
            "pear2/cache_shm": "dev-develop",
            "pear2/console_color": "dev-develop",
            "pear2/console_commandline": "dev-master",
            "phpunit/phpunit": "@stable",
            "squizlabs/php_codesniffer": "@stable"
        },
        "suggest": {
            "ext-apc": "This, APCu or Wincache is required for persistent connections.",
            "ext-apcu": "This, APC or Wincache is required for persistent connections.",
            "ext-openssl": "Enables encrypted connections.",
            "ext-wincache": "This, APC or APCu is required for persistent connections. Reccomended for Windows.",
            "pear2/cache_shm": "Enables persistent connections.",
            "pear2/console_color": "Enables colors in the console",
            "pear2/console_commandline": "Enables the console"
        },
        "time": "2017-05-22T15:42:06+00:00",
        "bin": [
            "scripts/roscon.php"
        ],
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-0": {
                "PEAR2\\Net\\RouterOS\\": "src/",
                "PEAR2\\Net\\Transmitter\\": "vendor/pear2/net_transmitter/src/",
                "PEAR2\\Cache\\SHM": "vendor/pear2/cache_shm/src/",
                "PEAR2\\Console\\Color": "vendor/pear2/console_color/src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "LGPL-2.1"
        ],
        "authors": [
            {
                "name": "Vasil Rangelov",
                "email": "boen.robot@gmail.com",
                "role": "lead"
            }
        ],
        "description": "This package allows you to read and write information from a RouterOS host using MikroTik's RouterOS API.",
        "homepage": "http://pear2.github.com/Net_RouterOS/",
        "keywords": [
            "api",
            "mikrotik",
            "package",
            "pear2",
            "router",
            "routeros"
        ]
    },
    {
        "name": "pear2/net_transmitter",
        "version": "dev-master",
        "version_normalized": "9999999-dev",
        "source": {
            "type": "git",
            "url": "https://github.com/pear2/Net_Transmitter.git",
            "reference": "5abea5cd481ac9631f446cfb8fb415f4c43318f6"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/pear2/Net_Transmitter/zipball/5abea5cd481ac9631f446cfb8fb415f4c43318f6",
            "reference": "5abea5cd481ac9631f446cfb8fb415f4c43318f6",
            "shasum": ""
        },
        "require": {
            "php": ">=5.3.0"
        },
        "require-dev": {
            "phpunit/phpunit": "@stable"
        },
        "suggest": {
            "ext-apc": "This, APCu or Wincache is required for persistent connections.",
            "ext-apcu": "This, APC or Wincache is required for persistent connections.",
            "ext-openssl": "Enables encrypted connections.",
            "ext-wincache": "This, APC or APCu is required for persistent connections. Reccomended for Windows.",
            "pear2/cache_shm": "Enables persistent connections"
        },
        "time": "2017-05-13T13:41:29+00:00",
        "type": "library",
        "installation-source": "source",
        "autoload": {
            "psr-0": {
                "PEAR2\\Net\\Transmitter\\": "src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "LGPL-2.1"
        ],
        "authors": [
            {
                "name": "Vasil Rangelov",
                "email": "boen.robot@gmail.com",
                "role": "lead"
            }
        ],
        "description": "A stream wrapper that ensures data integrity. Particularly useful for sockets.",
        "homepage": "http://pear2.github.com/Net_Transmitter/",
        "keywords": [
            "Socket",
            "integrity",
            "network",
            "networking",
            "package",
            "pear2",
            "sockets"
        ]
    }
]


File: /src\Libs\pear2\vendor\composer\LICENSE

Copyright (c) Nils Adermann, Jordi Boggiano

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.



File: /src\Libs\pear2\vendor\pear2\cache_shm\.gitignore
composer.phar
vendor/

File: /src\Libs\pear2\vendor\pear2\cache_shm\.scrutinizer.yml
imports:
    - php
inherit: true
tools:
    php_sim: false
    php_cpd: true
    php_code_sniffer:
        config:
            standard: PEAR


File: /src\Libs\pear2\vendor\pear2\cache_shm\composer.json
{
    "name": "pear2/cache_shm",
    "description": "Wrapper for shared memory and locking functionality across different PHP extensions.",
    "keywords": ["abstraction", "lock", "shm", "apc", "pear2", "cache", "wincache", "caching", "locking"],
    "homepage": "http://pear2.github.com/Cache_SHM/",
    "license": "LGPL-2.1",
    "authors": [
        {
            "name": "Vasil Rangelov",
            "email": "boen.robot@gmail.com",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "http://github.com/pear2/Cache_SHM/issues",
        "wiki": "http://github.com/pear2/Cache_SHM/wiki"
    },

    "require": {
        "php": ">=5.3.9"
    },
    "suggest": {
        "ext-apc": ">=3.1.1",
        "ext-apc": ">=5.0.0",
        "ext-wincache": ">=1.1.0"
    },
    "autoload": {
        "psr-0": {
            "PEAR2\\Cache\\SHM": "src/"
        }
    }
}


File: /src\Libs\pear2\vendor\pear2\cache_shm\CREDITS
Vasil Rangelov [boen_robot] <boen.robot@gmail.com> <lead>

File: /src\Libs\pear2\vendor\pear2\cache_shm\docs\apigen.neon
title: PEAR2_Cache_SHM documentation

source:
  - ../src

destination: Reference/ApiGen/Doc

extensions:
  - php

charset:
  - UTF-8

accessLevels:
  - public

tree: true

File: /src\Libs\pear2\vendor\pear2\cache_shm\docs\doxygen.ini
# Doxyfile 1.8.12

# This file describes the settings to be used by the documentation system
# doxygen (www.doxygen.org) for a project.
#
# All text after a double hash (##) is considered a comment and is placed in
# front of the TAG it is preceding.
#
# All text after a single hash (#) is considered a comment and will be ignored.
# The format is:
# TAG = value [value, ...]
# For lists, items can also be appended using:
# TAG += value [value, ...]
# Values that contain spaces should be placed between quotes (\" \").

#---------------------------------------------------------------------------
# Project related configuration options
#---------------------------------------------------------------------------

# This tag specifies the encoding used for all characters in the config file
# that follow. The default is UTF-8 which is also the encoding used for all text
# before the first occurrence of this tag. Doxygen uses libiconv (or the iconv
# built into libc) for the transcoding. See http://www.gnu.org/software/libiconv
# for the list of possible encodings.
# The default value is: UTF-8.

DOXYFILE_ENCODING      = UTF-8

# The PROJECT_NAME tag is a single word (or a sequence of words surrounded by
# double-quotes, unless you are using Doxywizard) that should identify the
# project for which the documentation is generated. This name is used in the
# title of most generated pages and in a few other places.
# The default value is: My Project.

PROJECT_NAME           = PEAR2_Cache_SHM

# The PROJECT_NUMBER tag can be used to enter a project or revision number. This
# could be handy for archiving the generated documentation or if some version
# control system is used.

PROJECT_NUMBER         = "GIT: $Id$"

# Using the PROJECT_BRIEF tag one can provide an optional one line description
# for a project that appears at the top of each page and should give viewer a
# quick idea about the purpose of the project. Keep the description short.

PROJECT_BRIEF          = "Wrapper for shared memory and locking functionality across different extensions."

# With the PROJECT_LOGO tag one can specify a logo or an icon that is included
# in the documentation. The maximum height of the logo should not exceed 55
# pixels and the maximum width should not exceed 200 pixels. Doxygen will copy
# the logo to the output directory.

PROJECT_LOGO           = 

# The OUTPUT_DIRECTORY tag is used to specify the (relative or absolute) path
# into which the generated documentation will be written. If a relative path is
# entered, it will be relative to the location where doxygen was started. If
# left blank the current directory will be used.

OUTPUT_DIRECTORY       = Reference/Doxygen/Doc

# If the CREATE_SUBDIRS tag is set to YES then doxygen will create 4096 sub-
# directories (in 2 levels) under the output directory of each output format and
# will distribute the generated files over these directories. Enabling this
# option can be useful when feeding doxygen a huge amount of source files, where
# putting all generated files in the same directory would otherwise causes
# performance problems for the file system.
# The default value is: NO.

CREATE_SUBDIRS         = NO

# If the ALLOW_UNICODE_NAMES tag is set to YES, doxygen will allow non-ASCII
# characters to appear in the names of generated files. If set to NO, non-ASCII
# characters will be escaped, for example _xE3_x81_x84 will be used for Unicode
# U+3044.
# The default value is: NO.

ALLOW_UNICODE_NAMES    = NO

# The OUTPUT_LANGUAGE tag is used to specify the language in which all
# documentation generated by doxygen is written. Doxygen will use this
# information to generate all constant output in the proper language.
# Possible values are: Afrikaans, Arabic, Armenian, Brazilian, Catalan, Chinese,
# Chinese-Traditional, Croatian, Czech, Danish, Dutch, English (United States),
# Esperanto, Farsi (Persian), Finnish, French, German, Greek, Hungarian,
# Indonesian, Italian, Japanese, Japanese-en (Japanese with English messages),
# Korean, Korean-en (Korean with English messages), Latvian, Lithuanian,
# Macedonian, Norwegian, Persian (Farsi), Polish, Portuguese, Romanian, Russian,
# Serbian, Serbian-Cyrillic, Slovak, Slovene, Spanish, Swedish, Turkish,
# Ukrainian and Vietnamese.
# The default value is: English.

OUTPUT_LANGUAGE        = English

# If the BRIEF_MEMBER_DESC tag is set to YES, doxygen will include brief member
# descriptions after the members that are listed in the file and class
# documentation (similar to Javadoc). Set to NO to disable this.
# The default value is: YES.

BRIEF_MEMBER_DESC      = YES

# If the REPEAT_BRIEF tag is set to YES, doxygen will prepend the brief
# description of a member or function before the detailed description
#
# Note: If both HIDE_UNDOC_MEMBERS and BRIEF_MEMBER_DESC are set to NO, the
# brief descriptions will be completely suppressed.
# The default value is: YES.

REPEAT_BRIEF           = YES

# This tag implements a quasi-intelligent brief description abbreviator that is
# used to form the text in various listings. Each string in this list, if found
# as the leading text of the brief description, will be stripped from the text
# and the result, after processing the whole list, is used as the annotated
# text. Otherwise, the brief description is used as-is. If left blank, the
# following values are used ($name is automatically replaced with the name of
# the entity):The $name class, The $name widget, The $name file, is, provides,
# specifies, contains, represents, a, an and the.

ABBREVIATE_BRIEF       = "The $name class" \
                         "The $name widget" \
                         "The $name file" \
                         is \
                         provides \
                         specifies \
                         contains \
                         represents \
                         a \
                         an \
                         the

# If the ALWAYS_DETAILED_SEC and REPEAT_BRIEF tags are both set to YES then
# doxygen will generate a detailed section even if there is only a brief
# description.
# The default value is: NO.

ALWAYS_DETAILED_SEC    = NO

# If the INLINE_INHERITED_MEMB tag is set to YES, doxygen will show all
# inherited members of a class in the documentation of that class as if those
# members were ordinary class members. Constructors, destructors and assignment
# operators of the base classes will not be shown.
# The default value is: NO.

INLINE_INHERITED_MEMB  = NO

# If the FULL_PATH_NAMES tag is set to YES, doxygen will prepend the full path
# before files name in the file list and in the header files. If set to NO the
# shortest path that makes the file name unique will be used
# The default value is: YES.

FULL_PATH_NAMES        = YES

# The STRIP_FROM_PATH tag can be used to strip a user-defined part of the path.
# Stripping is only done if one of the specified strings matches the left-hand
# part of the path. The tag can be used to show relative paths in the file list.
# If left blank the directory from which doxygen is run is used as the path to
# strip.
#
# Note that you can specify absolute paths here, but also relative paths, which
# will be relative from the directory where doxygen is started.
# This tag requires that the tag FULL_PATH_NAMES is set to YES.

STRIP_FROM_PATH        = ../src/

# The STRIP_FROM_INC_PATH tag can be used to strip a user-defined part of the
# path mentioned in the documentation of a class, which tells the reader which
# header file to include in order to use a class. If left blank only the name of
# the header file containing the class definition is used. Otherwise one should
# specify the list of include paths that are normally passed to the compiler
# using the -I flag.

STRIP_FROM_INC_PATH    = 

# If the SHORT_NAMES tag is set to YES, doxygen will generate much shorter (but
# less readable) file names. This can be useful is your file systems doesn't
# support long names like on DOS, Mac, or CD-ROM.
# The default value is: NO.

SHORT_NAMES            = NO

# If the JAVADOC_AUTOBRIEF tag is set to YES then doxygen will interpret the
# first line (until the first dot) of a Javadoc-style comment as the brief
# description. If set to NO, the Javadoc-style will behave just like regular Qt-
# style comments (thus requiring an explicit @brief command for a brief
# description.)
# The default value is: NO.

JAVADOC_AUTOBRIEF      = YES

# If the QT_AUTOBRIEF tag is set to YES then doxygen will interpret the first
# line (until the first dot) of a Qt-style comment as the brief description. If
# set to NO, the Qt-style will behave just like regular Qt-style comments (thus
# requiring an explicit \brief command for a brief description.)
# The default value is: NO.

QT_AUTOBRIEF           = NO

# The MULTILINE_CPP_IS_BRIEF tag can be set to YES to make doxygen treat a
# multi-line C++ special comment block (i.e. a block of //! or /// comments) as
# a brief description. This used to be the default behavior. The new default is
# to treat a multi-line C++ comment block as a detailed description. Set this
# tag to YES if you prefer the old behavior instead.
#
# Note that setting this tag to YES also means that rational rose comments are
# not recognized any more.
# The default value is: NO.

MULTILINE_CPP_IS_BRIEF = NO

# If the INHERIT_DOCS tag is set to YES then an undocumented member inherits the
# documentation from any documented member that it re-implements.
# The default value is: YES.

INHERIT_DOCS           = YES

# If the SEPARATE_MEMBER_PAGES tag is set to YES then doxygen will produce a new
# page for each member. If set to NO, the documentation of a member will be part
# of the file/class/namespace that contains it.
# The default value is: NO.

SEPARATE_MEMBER_PAGES  = NO

# The TAB_SIZE tag can be used to set the number of spaces in a tab. Doxygen
# uses this value to replace tabs by spaces in code fragments.
# Minimum value: 1, maximum value: 16, default value: 4.

TAB_SIZE               = 8

# This tag can be used to specify a number of aliases that act as commands in
# the documentation. An alias has the form:
# name=value
# For example adding
# "sideeffect=@par Side Effects:\n"
# will allow you to put the command \sideeffect (or @sideeffect) in the
# documentation, which will result in a user-defined paragraph with heading
# "Side Effects:". You can put \n's in the value part of an alias to insert
# newlines.

ALIASES                = 

# This tag can be used to specify a number of word-keyword mappings (TCL only).
# A mapping has the form "name=value". For example adding "class=itcl::class"
# will allow you to use the command class in the itcl::class meaning.

TCL_SUBST              = 

# Set the OPTIMIZE_OUTPUT_FOR_C tag to YES if your project consists of C sources
# only. Doxygen will then generate output that is more tailored for C. For
# instance, some of the names that are used will be different. The list of all
# members will be omitted, etc.
# The default value is: NO.

OPTIMIZE_OUTPUT_FOR_C  = YES

# Set the OPTIMIZE_OUTPUT_JAVA tag to YES if your project consists of Java or
# Python sources only. Doxygen will then generate output that is more tailored
# for that language. For instance, namespaces will be presented as packages,
# qualified scopes will look different, etc.
# The default value is: NO.

OPTIMIZE_OUTPUT_JAVA   = NO

# Set the OPTIMIZE_FOR_FORTRAN tag to YES if your project consists of Fortran
# sources. Doxygen will then generate output that is tailored for Fortran.
# The default value is: NO.

OPTIMIZE_FOR_FORTRAN   = NO

# Set the OPTIMIZE_OUTPUT_VHDL tag to YES if your project consists of VHDL
# sources. Doxygen will then generate output that is tailored for VHDL.
# The default value is: NO.

OPTIMIZE_OUTPUT_VHDL   = NO

# Doxygen selects the parser to use depending on the extension of the files it
# parses. With this tag you can assign which parser to use for a given
# extension. Doxygen has a built-in mapping, but you can override or extend it
# using this tag. The format is ext=language, where ext is a file extension, and
# language is one of the parsers supported by doxygen: IDL, Java, Javascript,
# C#, C, C++, D, PHP, Objective-C, Python, Fortran (fixed format Fortran:
# FortranFixed, free formatted Fortran: FortranFree, unknown formatted Fortran:
# Fortran. In the later case the parser tries to guess whether the code is fixed
# or free formatted code, this is the default for Fortran type files), VHDL. For
# instance to make doxygen treat .inc files as Fortran files (default is PHP),
# and .f files as C (default is Fortran), use: inc=Fortran f=C.
#
# Note: For files without extension you can use no_extension as a placeholder.
#
# Note that for custom extensions you also need to set FILE_PATTERNS otherwise
# the files are not read by doxygen.

EXTENSION_MAPPING      = 

# If the MARKDOWN_SUPPORT tag is enabled then doxygen pre-processes all comments
# according to the Markdown format, which allows for more readable
# documentation. See http://daringfireball.net/projects/markdown/ for details.
# The output of markdown processing is further processed by doxygen, so you can
# mix doxygen, HTML, and XML commands with Markdown formatting. Disable only in
# case of backward compatibilities issues.
# The default value is: YES.

MARKDOWN_SUPPORT       = YES

# When the TOC_INCLUDE_HEADINGS tag is set to a non-zero value, all headings up
# to that level are automatically included in the table of contents, even if
# they do not have an id attribute.
# Note: This feature currently applies only to Markdown headings.
# Minimum value: 0, maximum value: 99, default value: 0.
# This tag requires that the tag MARKDOWN_SUPPORT is set to YES.

TOC_INCLUDE_HEADINGS   = 0

# When enabled doxygen tries to link words that correspond to documented
# classes, or namespaces to their corresponding documentation. Such a link can
# be prevented in individual cases by putting a % sign in front of the word or
# globally by setting AUTOLINK_SUPPORT to NO.
# The default value is: YES.

AUTOLINK_SUPPORT       = NO

# If you use STL classes (i.e. std::string, std::vector, etc.) but do not want
# to include (a tag file for) the STL sources as input, then you should set this
# tag to YES in order to let doxygen match functions declarations and
# definitions whose arguments contain STL classes (e.g. func(std::string);
# versus func(std::string) {}). This also make the inheritance and collaboration
# diagrams that involve STL classes more complete and accurate.
# The default value is: NO.

BUILTIN_STL_SUPPORT    = NO

# If you use Microsoft's C++/CLI language, you should set this option to YES to
# enable parsing support.
# The default value is: NO.

CPP_CLI_SUPPORT        = NO

# Set the SIP_SUPPORT tag to YES if your project consists of sip (see:
# http://www.riverbankcomputing.co.uk/software/sip/intro) sources only. Doxygen
# will parse them like normal C++ but will assume all classes use public instead
# of private inheritance when no explicit protection keyword is present.
# The default value is: NO.

SIP_SUPPORT            = NO

# For Microsoft's IDL there are propget and propput attributes to indicate
# getter and setter methods for a property. Setting this option to YES will make
# doxygen to replace the get and set methods by a property in the documentation.
# This will only work if the methods are indeed getting or setting a simple
# type. If this is not the case, or you want to show the methods anyway, you
# should set this option to NO.
# The default value is: YES.

IDL_PROPERTY_SUPPORT   = NO

# If member grouping is used in the documentation and the DISTRIBUTE_GROUP_DOC
# tag is set to YES then doxygen will reuse the documentation of the first
# member in the group (if any) for the other members of the group. By default
# all members of a group must be documented explicitly.
# The default value is: NO.

DISTRIBUTE_GROUP_DOC   = NO

# If one adds a struct or class to a group and this option is enabled, then also
# any nested class or struct is added to the same group. By default this option
# is disabled and one has to add nested compounds explicitly via \ingroup.
# The default value is: NO.

GROUP_NESTED_COMPOUNDS = NO

# Set the SUBGROUPING tag to YES to allow class member groups of the same type
# (for instance a group of public functions) to be put as a subgroup of that
# type (e.g. under the Public Functions section). Set it to NO to prevent
# subgrouping. Alternatively, this can be done per class using the
# \nosubgrouping command.
# The default value is: YES.

SUBGROUPING            = YES

# When the INLINE_GROUPED_CLASSES tag is set to YES, classes, structs and unions
# are shown inside the group in which they are included (e.g. using \ingroup)
# instead of on a separate page (for HTML and Man pages) or section (for LaTeX
# and RTF).
#
# Note that this feature does not work in combination with
# SEPARATE_MEMBER_PAGES.
# The default value is: NO.

INLINE_GROUPED_CLASSES = NO

# When the INLINE_SIMPLE_STRUCTS tag is set to YES, structs, classes, and unions
# with only public data fields or simple typedef fields will be shown inline in
# the documentation of the scope in which they are defined (i.e. file,
# namespace, or group documentation), provided this scope is documented. If set
# to NO, structs, classes, and unions are shown on a separate page (for HTML and
# Man pages) or section (for LaTeX and RTF).
# The default value is: NO.

INLINE_SIMPLE_STRUCTS  = NO

# When TYPEDEF_HIDES_STRUCT tag is enabled, a typedef of a struct, union, or
# enum is documented as struct, union, or enum with the name of the typedef. So
# typedef struct TypeS {} TypeT, will appear in the documentation as a struct
# with name TypeT. When disabled the typedef will appear as a member of a file,
# namespace, or class. And the struct will be named TypeS. This can typically be
# useful for C code in case the coding convention dictates that all compound
# types are typedef'ed and only the typedef is referenced, never the tag name.
# The default value is: NO.

TYPEDEF_HIDES_STRUCT   = NO

# The size of the symbol lookup cache can be set using LOOKUP_CACHE_SIZE. This
# cache is used to resolve symbols given their name and scope. Since this can be
# an expensive process and often the same symbol appears multiple times in the
# code, doxygen keeps a cache of pre-resolved symbols. If the cache is too small
# doxygen will become slower. If the cache is too large, memory is wasted. The
# cache size is given by this formula: 2^(16+LOOKUP_CACHE_SIZE). The valid range
# is 0..9, the default is 0, corresponding to a cache size of 2^16=65536
# symbols. At the end of a run doxygen will report the cache usage and suggest
# the optimal cache size from a speed point of view.
# Minimum value: 0, maximum value: 9, default value: 0.

LOOKUP_CACHE_SIZE      = 0

#---------------------------------------------------------------------------
# Build related configuration options
#---------------------------------------------------------------------------

# If the EXTRACT_ALL tag is set to YES, doxygen will assume all entities in
# documentation are documented, even if no documentation was available. Private
# class members and static file members will be hidden unless the
# EXTRACT_PRIVATE respectively EXTRACT_STATIC tags are set to YES.
# Note: This will also disable the warnings about undocumented members that are
# normally produced when WARNINGS is set to YES.
# The default value is: NO.

EXTRACT_ALL            = NO

# If the EXTRACT_PRIVATE tag is set to YES, all private members of a class will
# be included in the documentation.
# The default value is: NO.

EXTRACT_PRIVATE        = NO

# If the EXTRACT_PACKAGE tag is set to YES, all members with package or internal
# scope will be included in the documentation.
# The default value is: NO.

EXTRACT_PACKAGE        = YES

# If the EXTRACT_STATIC tag is set to YES, all static members of a file will be
# included in the documentation.
# The default value is: NO.

EXTRACT_STATIC         = YES

# If the EXTRACT_LOCAL_CLASSES tag is set to YES, classes (and structs) defined
# locally in source files will be included in the documentation. If set to NO,
# only classes defined in header files are included. Does not have any effect
# for Java sources.
# The default value is: YES.

EXTRACT_LOCAL_CLASSES  = YES

# This flag is only useful for Objective-C code. If set to YES, local methods,
# which are defined in the implementation section but not in the interface are
# included in the documentation. If set to NO, only methods in the interface are
# included.
# The default value is: NO.

EXTRACT_LOCAL_METHODS  = NO

# If this flag is set to YES, the members of anonymous namespaces will be
# extracted and appear in the documentation as a namespace called
# 'anonymous_namespace{file}', where file will be replaced with the base name of
# the file that contains the anonymous namespace. By default anonymous namespace
# are hidden.
# The default value is: NO.

EXTRACT_ANON_NSPACES   = NO

# If the HIDE_UNDOC_MEMBERS tag is set to YES, doxygen will hide all
# undocumented members inside documented classes or files. If set to NO these
# members will be included in the various overviews, but no documentation
# section is generated. This option has no effect if EXTRACT_ALL is enabled.
# The default value is: NO.

HIDE_UNDOC_MEMBERS     = NO

# If the HIDE_UNDOC_CLASSES tag is set to YES, doxygen will hide all
# undocumented classes that are normally visible in the class hierarchy. If set
# to NO, these classes will be included in the various overviews. This option
# has no effect if EXTRACT_ALL is enabled.
# The default value is: NO.

HIDE_UNDOC_CLASSES     = NO

# If the HIDE_FRIEND_COMPOUNDS tag is set to YES, doxygen will hide all friend
# (class|struct|union) declarations. If set to NO, these declarations will be
# included in the documentation.
# The default value is: NO.

HIDE_FRIEND_COMPOUNDS  = NO

# If the HIDE_IN_BODY_DOCS tag is set to YES, doxygen will hide any
# documentation blocks found inside the body of a function. If set to NO, these
# blocks will be appended to the function's detailed documentation block.
# The default value is: NO.

HIDE_IN_BODY_DOCS      = NO

# The INTERNAL_DOCS tag determines if documentation that is typed after a
# \internal command is included. If the tag is set to NO then the documentation
# will be excluded. Set it to YES to include the internal documentation.
# The default value is: NO.

INTERNAL_DOCS          = NO

# If the CASE_SENSE_NAMES tag is set to NO then doxygen will only generate file
# names in lower-case letters. If set to YES, upper-case letters are also
# allowed. This is useful if you have classes or files whose names only differ
# in case and if your file system supports case sensitive file names. Windows
# and Mac users are advised to set this option to NO.
# The default value is: system dependent.

CASE_SENSE_NAMES       = NO

# If the HIDE_SCOPE_NAMES tag is set to NO then doxygen will show members with
# their full class and namespace scopes in the documentation. If set to YES, the
# scope will be hidden.
# The default value is: NO.

HIDE_SCOPE_NAMES       = YES

# If the HIDE_COMPOUND_REFERENCE tag is set to NO (default) then doxygen will
# append additional text to a page's title, such as Class Reference. If set to
# YES the compound reference will be hidden.
# The default value is: NO.

HIDE_COMPOUND_REFERENCE= NO

# If the SHOW_INCLUDE_FILES tag is set to YES then doxygen will put a list of
# the files that are included by a file in the documentation of that file.
# The default value is: YES.

SHOW_INCLUDE_FILES     = YES

# If the SHOW_GROUPED_MEMB_INC tag is set to YES then Doxygen will add for each
# grouped member an include statement to the documentation, telling the reader
# which file to include in order to use the member.
# The default value is: NO.

SHOW_GROUPED_MEMB_INC  = NO

# If the FORCE_LOCAL_INCLUDES tag is set to YES then doxygen will list include
# files with double quotes in the documentation rather than with sharp brackets.
# The default value is: NO.

FORCE_LOCAL_INCLUDES   = NO

# If the INLINE_INFO tag is set to YES then a tag [inline] is inserted in the
# documentation for inline members.
# The default value is: YES.

INLINE_INFO            = YES

# If the SORT_MEMBER_DOCS tag is set to YES then doxygen will sort the
# (detailed) documentation of file and class members alphabetically by member
# name. If set to NO, the members will appear in declaration order.
# The default value is: YES.

SORT_MEMBER_DOCS       = YES

# If the SORT_BRIEF_DOCS tag is set to YES then doxygen will sort the brief
# descriptions of file, namespace and class members alphabetically by member
# name. If set to NO, the members will appear in declaration order. Note that
# this will also influence the order of the classes in the class list.
# The default value is: NO.

SORT_BRIEF_DOCS        = NO

# If the SORT_MEMBERS_CTORS_1ST tag is set to YES then doxygen will sort the
# (brief and detailed) documentation of class members so that constructors and
# destructors are listed first. If set to NO the constructors will appear in the
# respective orders defined by SORT_BRIEF_DOCS and SORT_MEMBER_DOCS.
# Note: If SORT_BRIEF_DOCS is set to NO this option is ignored for sorting brief
# member documentation.
# Note: If SORT_MEMBER_DOCS is set to NO this option is ignored for sorting
# detailed member documentation.
# The default value is: NO.

SORT_MEMBERS_CTORS_1ST = NO

# If the SORT_GROUP_NAMES tag is set to YES then doxygen will sort the hierarchy
# of group names into alphabetical order. If set to NO the group names will
# appear in their defined order.
# The default value is: NO.

SORT_GROUP_NAMES       = NO

# If the SORT_BY_SCOPE_NAME tag is set to YES, the class list will be sorted by
# fully-qualified names, including namespaces. If set to NO, the class list will
# be sorted only by class name, not including the namespace part.
# Note: This option is not very useful if HIDE_SCOPE_NAMES is set to YES.
# Note: This option applies only to the class list, not to the alphabetical
# list.
# The default value is: NO.

SORT_BY_SCOPE_NAME     = NO

# If the STRICT_PROTO_MATCHING option is enabled and doxygen fails to do proper
# type resolution of all parameters of a function it will reject a match between
# the prototype and the implementation of a member function even if there is
# only one candidate or it is obvious which candidate to choose by doing a
# simple string match. By disabling STRICT_PROTO_MATCHING doxygen will still
# accept a match between prototype and implementation in such cases.
# The default value is: NO.

STRICT_PROTO_MATCHING  = NO

# The GENERATE_TODOLIST tag can be used to enable (YES) or disable (NO) the todo
# list. This list is created by putting \todo commands in the documentation.
# The default value is: YES.

GENERATE_TODOLIST      = YES

# The GENERATE_TESTLIST tag can be used to enable (YES) or disable (NO) the test
# list. This list is created by putting \test commands in the documentation.
# The default value is: YES.

GENERATE_TESTLIST      = YES

# The GENERATE_BUGLIST tag can be used to enable (YES) or disable (NO) the bug
# list. This list is created by putting \bug commands in the documentation.
# The default value is: YES.

GENERATE_BUGLIST       = YES

# The GENERATE_DEPRECATEDLIST tag can be used to enable (YES) or disable (NO)
# the deprecated list. This list is created by putting \deprecated commands in
# the documentation.
# The default value is: YES.

GENERATE_DEPRECATEDLIST= YES

# The ENABLED_SECTIONS tag can be used to enable conditional documentation
# sections, marked by \if <section_label> ... \endif and \cond <section_label>
# ... \endcond blocks.

ENABLED_SECTIONS       = 

# The MAX_INITIALIZER_LINES tag determines the maximum number of lines that the
# initial value of a variable or macro / define can have for it to appear in the
# documentation. If the initializer consists of more lines than specified here
# it will be hidden. Use a value of 0 to hide initializers completely. The
# appearance of the value of individual variables and macros / defines can be
# controlled using \showinitializer or \hideinitializer command in the
# documentation regardless of this setting.
# Minimum value: 0, maximum value: 10000, default value: 30.

MAX_INITIALIZER_LINES  = 30

# Set the SHOW_USED_FILES tag to NO to disable the list of files generated at
# the bottom of the documentation of classes and structs. If set to YES, the
# list will mention the files that were used to generate the documentation.
# The default value is: YES.

SHOW_USED_FILES        = YES

# Set the SHOW_FILES tag to NO to disable the generation of the Files page. This
# will remove the Files entry from the Quick Index and from the Folder Tree View
# (if specified).
# The default value is: YES.

SHOW_FILES             = YES

# Set the SHOW_NAMESPACES tag to NO to disable the generation of the Namespaces
# page. This will remove the Namespaces entry from the Quick Index and from the
# Folder Tree View (if specified).
# The default value is: YES.

SHOW_NAMESPACES        = YES

# The FILE_VERSION_FILTER tag can be used to specify a program or script that
# doxygen should invoke to get the current version for each file (typically from
# the version control system). Doxygen will invoke the program by executing (via
# popen()) the command command input-file, where command is the value of the
# FILE_VERSION_FILTER tag, and input-file is the name of an input file provided
# by doxygen. Whatever the program writes to standard output is used as the file
# version. For an example see the documentation.

FILE_VERSION_FILTER    = 

# The LAYOUT_FILE tag can be used to specify a layout file which will be parsed
# by doxygen. The layout file controls the global structure of the generated
# output files in an output format independent way. To create the layout file
# that represents doxygen's defaults, run doxygen with the -l option. You can
# optionally specify a file name after the option, if omitted DoxygenLayout.xml
# will be used as the name of the layout file.
#
# Note that if you run doxygen from a directory containing a file called
# DoxygenLayout.xml, doxygen will parse it automatically even if the LAYOUT_FILE
# tag is left empty.

LAYOUT_FILE            = 

# The CITE_BIB_FILES tag can be used to specify one or more bib files containing
# the reference definitions. This must be a list of .bib files. The .bib
# extension is automatically appended if omitted. This requires the bibtex tool
# to be installed. See also http://en.wikipedia.org/wiki/BibTeX for more info.
# For LaTeX the style of the bibliography can be controlled using
# LATEX_BIB_STYLE. To use this feature you need bibtex and perl available in the
# search path. See also \cite for info how to create references.

CITE_BIB_FILES         = 

#---------------------------------------------------------------------------
# Configuration options related to warning and progress messages
#---------------------------------------------------------------------------

# The QUIET tag can be used to turn on/off the messages that are generated to
# standard output by doxygen. If QUIET is set to YES this implies that the
# messages are off.
# The default value is: NO.

QUIET                  = NO

# The WARNINGS tag can be used to turn on/off the warning messages that are
# generated to standard error (stderr) by doxygen. If WARNINGS is set to YES
# this implies that the warnings are on.
#
# Tip: Turn warnings on while writing the documentation.
# The default value is: YES.

WARNINGS               = YES

# If the WARN_IF_UNDOCUMENTED tag is set to YES then doxygen will generate
# warnings for undocumented members. If EXTRACT_ALL is set to YES then this flag
# will automatically be disabled.
# The default value is: YES.

WARN_IF_UNDOCUMENTED   = YES

# If the WARN_IF_DOC_ERROR tag is set to YES, doxygen will generate warnings for
# potential errors in the documentation, such as not documenting some parameters
# in a documented function, or documenting parameters that don't exist or using
# markup commands wrongly.
# The default value is: YES.

WARN_IF_DOC_ERROR      = YES

# This WARN_NO_PARAMDOC option can be enabled to get warnings for functions that
# are documented, but have no documentation for their parameters or return
# value. If set to NO, doxygen will only warn about wrong or incomplete
# parameter documentation, but not about the absence of documentation.
# The default value is: NO.

WARN_NO_PARAMDOC       = NO

# If the WARN_AS_ERROR tag is set to YES then doxygen will immediately stop when
# a warning is encountered.
# The default value is: NO.

WARN_AS_ERROR          = NO

# The WARN_FORMAT tag determines the format of the warning messages that doxygen
# can produce. The string should contain the $file, $line, and $text tags, which
# will be replaced by the file and line number from which the warning originated
# and the warning text. Optionally the format may contain $version, which will
# be replaced by the version of the file (if it could be obtained via
# FILE_VERSION_FILTER)
# The default value is: $file:$line: $text.

WARN_FORMAT            = "$file:$line: $text"

# The WARN_LOGFILE tag can be used to specify a file to which warning and error
# messages should be written. If left blank the output is written to standard
# error (stderr).

WARN_LOGFILE           = 

#---------------------------------------------------------------------------
# Configuration options related to the input files
#---------------------------------------------------------------------------

# The INPUT tag is used to specify the files and/or directories that contain
# documented source files. You may enter file names like myfile.cpp or
# directories like /usr/src/myproject. Separate the files or directories with
# spaces. See also FILE_PATTERNS and EXTENSION_MAPPING
# Note: If this tag is empty the current directory is searched.

INPUT                  = ../src/PEAR2/Cache/SHM \
                         ../src/PEAR2/Cache/SHM.php

# This tag can be used to specify the character encoding of the source files
# that doxygen parses. Internally doxygen uses the UTF-8 encoding. Doxygen uses
# libiconv (or the iconv built into libc) for the transcoding. See the libiconv
# documentation (see: http://www.gnu.org/software/libiconv) for the list of
# possible encodings.
# The default value is: UTF-8.

INPUT_ENCODING         = UTF-8

# If the value of the INPUT tag contains directories, you can use the
# FILE_PATTERNS tag to specify one or more wildcard patterns (like *.cpp and
# *.h) to filter out the source-files in the directories.
#
# Note that for custom extensions or not directly supported extensions you also
# need to set EXTENSION_MAPPING for the extension otherwise the files are not
# read by doxygen.
#
# If left blank the following patterns are tested:*.c, *.cc, *.cxx, *.cpp,
# *.c++, *.java, *.ii, *.ixx, *.ipp, *.i++, *.inl, *.idl, *.ddl, *.odl, *.h,
# *.hh, *.hxx, *.hpp, *.h++, *.cs, *.d, *.php, *.php4, *.php5, *.phtml, *.inc,
# *.m, *.markdown, *.md, *.mm, *.dox, *.py, *.pyw, *.f90, *.f95, *.f03, *.f08,
# *.f, *.for, *.tcl, *.vhd, *.vhdl, *.ucf and *.qsf.

FILE_PATTERNS          = *.c \
                         *.cc \
                         *.cxx \
                         *.cpp \
                         *.c++ \
                         *.d \
                         *.java \
                         *.ii \
                         *.ixx \
                         *.ipp \
                         *.i++ \
                         *.inl \
                         *.h \
                         *.hh \
                         *.hxx \
                         *.hpp \
                         *.h++ \
                         *.idl \
                         *.odl \
                         *.cs \
                         *.php \
                         *.php3 \
                         *.inc \
                         *.m \
                         *.mm \
                         *.dox \
                         *.py \
                         *.f90 \
                         *.f \
                         *.for \
                         *.vhd \
                         *.vhdl

# The RECURSIVE tag can be used to specify whether or not subdirectories should
# be searched for input files as well.
# The default value is: NO.

RECURSIVE              = YES

# The EXCLUDE tag can be used to specify files and/or directories that should be
# excluded from the INPUT source files. This way you can easily exclude a
# subdirectory from a directory tree whose root is specified with the INPUT tag.
#
# Note that relative paths are relative to the directory from which doxygen is
# run.

EXCLUDE                = 

# The EXCLUDE_SYMLINKS tag can be used to select whether or not files or
# directories that are symbolic links (a Unix file system feature) are excluded
# from the input.
# The default value is: NO.

EXCLUDE_SYMLINKS       = NO

# If the value of the INPUT tag contains directories, you can use the
# EXCLUDE_PATTERNS tag to specify one or more wildcard patterns to exclude
# certain files from those directories.
#
# Note that the wildcards are matched against the file with absolute path, so to
# exclude all test directories for example use the pattern */test/*

EXCLUDE_PATTERNS       = 

# The EXCLUDE_SYMBOLS tag can be used to specify one or more symbol names
# (namespaces, classes, functions, etc.) that should be excluded from the
# output. The symbol name can be a fully qualified name, a word, or if the
# wildcard * is used, a substring. Examples: ANamespace, AClass,
# AClass::ANamespace, ANamespace::*Test
#
# Note that the wildcards are matched against the file with absolute path, so to
# exclude all test directories use the pattern */test/*

EXCLUDE_SYMBOLS        = 

# The EXAMPLE_PATH tag can be used to specify one or more files or directories
# that contain example code fragments that are included (see the \include
# command).

EXAMPLE_PATH           = 

# If the value of the EXAMPLE_PATH tag contains directories, you can use the
# EXAMPLE_PATTERNS tag to specify one or more wildcard pattern (like *.cpp and
# *.h) to filter out the source-files in the directories. If left blank all
# files are included.

EXAMPLE_PATTERNS       = *

# If the EXAMPLE_RECURSIVE tag is set to YES then subdirectories will be
# searched for input files to be used with the \include or \dontinclude commands
# irrespective of the value of the RECURSIVE tag.
# The default value is: NO.

EXAMPLE_RECURSIVE      = NO

# The IMAGE_PATH tag can be used to specify one or more files or directories
# that contain images that are to be included in the documentation (see the
# \image command).

IMAGE_PATH             = 

# The INPUT_FILTER tag can be used to specify a program that doxygen should
# invoke to filter for each input file. Doxygen will invoke the filter program
# by executing (via popen()) the command:
#
# <filter> <input-file>
#
# where <filter> is the value of the INPUT_FILTER tag, and <input-file> is the
# name of an input file. Doxygen will then use the output that the filter
# program writes to standard output. If FILTER_PATTERNS is specified, this tag
# will be ignored.
#
# Note that the filter must not add or remove lines; it is applied before the
# code is scanned, but not when the output code is generated. If lines are added
# or removed, the anchors will not be placed correctly.
#
# Note that for custom extensions or not directly supported extensions you also
# need to set EXTENSION_MAPPING for the extension otherwise the files are not
# properly processed by doxygen.

INPUT_FILTER           = 

# The FILTER_PATTERNS tag can be used to specify filters on a per file pattern
# basis. Doxygen will compare the file name with each pattern and apply the
# filter if there is a match. The filters are a list of the form: pattern=filter
# (like *.cpp=my_cpp_filter). See INPUT_FILTER for further information on how
# filters are used. If the FILTER_PATTERNS tag is empty or if none of the
# patterns match the file name, INPUT_FILTER is applied.
#
# Note that for custom extensions or not directly supported extensions you also
# need to set EXTENSION_MAPPING for the extension otherwise the files are not
# properly processed by doxygen.

FILTER_PATTERNS        = 

# If the FILTER_SOURCE_FILES tag is set to YES, the input filter (if set using
# INPUT_FILTER) will also be used to filter the input files that are used for
# producing the source files to browse (i.e. when SOURCE_BROWSER is set to YES).
# The default value is: NO.

FILTER_SOURCE_FILES    = NO

# The FILTER_SOURCE_PATTERNS tag can be used to specify source filters per file
# pattern. A pattern will override the setting for FILTER_PATTERN (if any) and
# it is also possible to disable source filtering for a specific pattern using
# *.ext= (so without naming a filter).
# This tag requires that the tag FILTER_SOURCE_FILES is set to YES.

FILTER_SOURCE_PATTERNS = 

# If the USE_MDFILE_AS_MAINPAGE tag refers to the name of a markdown file that
# is part of the input, its contents will be placed on the main page
# (index.html). This can be useful if you have a project on for instance GitHub
# and want to reuse the introduction page also for the doxygen output.

USE_MDFILE_AS_MAINPAGE = 

#---------------------------------------------------------------------------
# Configuration options related to source browsing
#---------------------------------------------------------------------------

# If the SOURCE_BROWSER tag is set to YES then a list of source files will be
# generated. Documented entities will be cross-referenced with these sources.
#
# Note: To get rid of all source code in the generated output, make sure that
# also VERBATIM_HEADERS is set to NO.
# The default value is: NO.

SOURCE_BROWSER         = YES

# Setting the INLINE_SOURCES tag to YES will include the body of functions,
# classes and enums directly into the documentation.
# The default value is: NO.

INLINE_SOURCES         = NO

# Setting the STRIP_CODE_COMMENTS tag to YES will instruct doxygen to hide any
# special comment blocks from generated source code fragments. Normal C, C++ and
# Fortran comments will always remain visible.
# The default value is: YES.

STRIP_CODE_COMMENTS    = NO

# If the REFERENCED_BY_RELATION tag is set to YES then for each documented
# function all documented functions referencing it will be listed.
# The default value is: NO.

REFERENCED_BY_RELATION = NO

# If the REFERENCES_RELATION tag is set to YES then for each documented function
# all documented entities called/used by that function will be listed.
# The default value is: NO.

REFERENCES_RELATION    = NO

# If the REFERENCES_LINK_SOURCE tag is set to YES and SOURCE_BROWSER tag is set
# to YES then the hyperlinks from functions in REFERENCES_RELATION and
# REFERENCED_BY_RELATION lists will link to the source code. Otherwise they will
# link to the documentation.
# The default value is: YES.

REFERENCES_LINK_SOURCE = YES

# If SOURCE_TOOLTIPS is enabled (the default) then hovering a hyperlink in the
# source code will show a tooltip with additional information such as prototype,
# brief description and links to the definition and documentation. Since this
# will make the HTML file larger and loading of large files a bit slower, you
# can opt to disable this feature.
# The default value is: YES.
# This tag requires that the tag SOURCE_BROWSER is set to YES.

SOURCE_TOOLTIPS        = YES

# If the USE_HTAGS tag is set to YES then the references to source code will
# point to the HTML generated by the htags(1) tool instead of doxygen built-in
# source browser. The htags tool is part of GNU's global source tagging system
# (see http://www.gnu.org/software/global/global.html). You will need version
# 4.8.6 or higher.
#
# To use it do the following:
# - Install the latest version of global
# - Enable SOURCE_BROWSER and USE_HTAGS in the config file
# - Make sure the INPUT points to the root of the source tree
# - Run doxygen as normal
#
# Doxygen will invoke htags (and that will in turn invoke gtags), so these
# tools must be available from the command line (i.e. in the search path).
#
# The result: instead of the source browser generated by doxygen, the links to
# source code will now point to the output of htags.
# The default value is: NO.
# This tag requires that the tag SOURCE_BROWSER is set to YES.

USE_HTAGS              = NO

# If the VERBATIM_HEADERS tag is set the YES then doxygen will generate a
# verbatim copy of the header file for each class for which an include is
# specified. Set to NO to disable this.
# See also: Section \class.
# The default value is: YES.

VERBATIM_HEADERS       = YES

# If the CLANG_ASSISTED_PARSING tag is set to YES then doxygen will use the
# clang parser (see: http://clang.llvm.org/) for more accurate parsing at the
# cost of reduced performance. This can be particularly helpful with template
# rich C++ code for which doxygen's built-in parser lacks the necessary type
# information.
# Note: The availability of this option depends on whether or not doxygen was
# generated with the -Duse-libclang=ON option for CMake.
# The default value is: NO.

CLANG_ASSISTED_PARSING = NO

# If clang assisted parsing is enabled you can provide the compiler with command
# line options that you would normally use when invoking the compiler. Note that
# the include paths will already be set by doxygen for the files and directories
# specified with INPUT and INCLUDE_PATH.
# This tag requires that the tag CLANG_ASSISTED_PARSING is set to YES.

CLANG_OPTIONS          = 

#---------------------------------------------------------------------------
# Configuration options related to the alphabetical class index
#---------------------------------------------------------------------------

# If the ALPHABETICAL_INDEX tag is set to YES, an alphabetical index of all
# compounds will be generated. Enable this if the project contains a lot of
# classes, structs, unions or interfaces.
# The default value is: YES.

ALPHABETICAL_INDEX     = YES

# The COLS_IN_ALPHA_INDEX tag can be used to specify the number of columns in
# which the alphabetical index list will be split.
# Minimum value: 1, maximum value: 20, default value: 5.
# This tag requires that the tag ALPHABETICAL_INDEX is set to YES.

COLS_IN_ALPHA_INDEX    = 5

# In case all classes in a project start with a common prefix, all classes will
# be put under the same header in the alphabetical index. The IGNORE_PREFIX tag
# can be used to specify a prefix (or a list of prefixes) that should be ignored
# while generating the index headers.
# This tag requires that the tag ALPHABETICAL_INDEX is set to YES.

IGNORE_PREFIX          = 

#---------------------------------------------------------------------------
# Configuration options related to the HTML output
#---------------------------------------------------------------------------

# If the GENERATE_HTML tag is set to YES, doxygen will generate HTML output
# The default value is: YES.

GENERATE_HTML          = YES

# The HTML_OUTPUT tag is used to specify where the HTML docs will be put. If a
# relative path is entered the value of OUTPUT_DIRECTORY will be put in front of
# it.
# The default directory is: html.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_OUTPUT            = html

# The HTML_FILE_EXTENSION tag can be used to specify the file extension for each
# generated HTML page (for example: .htm, .php, .asp).
# The default value is: .html.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_FILE_EXTENSION    = .html

# The HTML_HEADER tag can be used to specify a user-defined HTML header file for
# each generated HTML page. If the tag is left blank doxygen will generate a
# standard header.
#
# To get valid HTML the header file that includes any scripts and style sheets
# that doxygen needs, which is dependent on the configuration options used (e.g.
# the setting GENERATE_TREEVIEW). It is highly recommended to start with a
# default header using
# doxygen -w html new_header.html new_footer.html new_stylesheet.css
# YourConfigFile
# and then modify the file new_header.html. See also section "Doxygen usage"
# for information on how to generate the default header that doxygen normally
# uses.
# Note: The header is subject to change so you typically have to regenerate the
# default header when upgrading to a newer version of doxygen. For a description
# of the possible markers and block names see the documentation.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_HEADER            = 

# The HTML_FOOTER tag can be used to specify a user-defined HTML footer for each
# generated HTML page. If the tag is left blank doxygen will generate a standard
# footer. See HTML_HEADER for more information on how to generate a default
# footer and what special commands can be used inside the footer. See also
# section "Doxygen usage" for information on how to generate the default footer
# that doxygen normally uses.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_FOOTER            = 

# The HTML_STYLESHEET tag can be used to specify a user-defined cascading style
# sheet that is used by each HTML page. It can be used to fine-tune the look of
# the HTML output. If left blank doxygen will generate a default style sheet.
# See also section "Doxygen usage" for information on how to generate the style
# sheet that doxygen normally uses.
# Note: It is recommended to use HTML_EXTRA_STYLESHEET instead of this tag, as
# it is more robust and this tag (HTML_STYLESHEET) will in the future become
# obsolete.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_STYLESHEET        = 

# The HTML_EXTRA_STYLESHEET tag can be used to specify additional user-defined
# cascading style sheets that are included after the standard style sheets
# created by doxygen. Using this option one can overrule certain style aspects.
# This is preferred over using HTML_STYLESHEET since it does not replace the
# standard style sheet and is therefore more robust against future updates.
# Doxygen will copy the style sheet files to the output directory.
# Note: The order of the extra style sheet files is of importance (e.g. the last
# style sheet in the list overrules the setting of the previous ones in the
# list). For an example see the documentation.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_EXTRA_STYLESHEET  = 

# The HTML_EXTRA_FILES tag can be used to specify one or more extra images or
# other source files which should be copied to the HTML output directory. Note
# that these files will be copied to the base HTML output directory. Use the
# $relpath^ marker in the HTML_HEADER and/or HTML_FOOTER files to load these
# files. In the HTML_STYLESHEET file, use the file name only. Also note that the
# files will be copied as-is; there are no commands or markers available.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_EXTRA_FILES       = 

# The HTML_COLORSTYLE_HUE tag controls the color of the HTML output. Doxygen
# will adjust the colors in the style sheet and background images according to
# this color. Hue is specified as an angle on a colorwheel, see
# http://en.wikipedia.org/wiki/Hue for more information. For instance the value
# 0 represents red, 60 is yellow, 120 is green, 180 is cyan, 240 is blue, 300
# purple, and 360 is red again.
# Minimum value: 0, maximum value: 359, default value: 220.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_COLORSTYLE_HUE    = 220

# The HTML_COLORSTYLE_SAT tag controls the purity (or saturation) of the colors
# in the HTML output. For a value of 0 the output will use grayscales only. A
# value of 255 will produce the most vivid colors.
# Minimum value: 0, maximum value: 255, default value: 100.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_COLORSTYLE_SAT    = 100

# The HTML_COLORSTYLE_GAMMA tag controls the gamma correction applied to the
# luminance component of the colors in the HTML output. Values below 100
# gradually make the output lighter, whereas values above 100 make the output
# darker. The value divided by 100 is the actual gamma applied, so 80 represents
# a gamma of 0.8, The value 220 represents a gamma of 2.2, and 100 does not
# change the gamma.
# Minimum value: 40, maximum value: 240, default value: 80.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_COLORSTYLE_GAMMA  = 80

# If the HTML_TIMESTAMP tag is set to YES then the footer of each generated HTML
# page will contain the date and time when the page was generated. Setting this
# to YES can help to show when doxygen was last run and thus if the
# documentation is up to date.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_TIMESTAMP         = YES

# If the HTML_DYNAMIC_SECTIONS tag is set to YES then the generated HTML
# documentation will contain sections that can be hidden and shown after the
# page has loaded.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_DYNAMIC_SECTIONS  = YES

# With HTML_INDEX_NUM_ENTRIES one can control the preferred number of entries
# shown in the various tree structured indices initially; the user can expand
# and collapse entries dynamically later on. Doxygen will expand the tree to
# such a level that at most the specified number of entries are visible (unless
# a fully collapsed tree already exceeds this amount). So setting the number of
# entries 1 will produce a full collapsed tree by default. 0 is a special value
# representing an infinite number of entries and will result in a full expanded
# tree by default.
# Minimum value: 0, maximum value: 9999, default value: 100.
# This tag requires that the tag GENERATE_HTML is set to YES.

HTML_INDEX_NUM_ENTRIES = 100

# If the GENERATE_DOCSET tag is set to YES, additional index files will be
# generated that can be used as input for Apple's Xcode 3 integrated development
# environment (see: http://developer.apple.com/tools/xcode/), introduced with
# OSX 10.5 (Leopard). To create a documentation set, doxygen will generate a
# Makefile in the HTML output directory. Running make will produce the docset in
# that directory and running make install will install the docset in
# ~/Library/Developer/Shared/Documentation/DocSets so that Xcode will find it at
# startup. See http://developer.apple.com/tools/creatingdocsetswithdoxygen.html
# for more information.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTML is set to YES.

GENERATE_DOCSET        = NO

# This tag determines the name of the docset feed. A documentation feed provides
# an umbrella under which multiple documentation sets from a single provider
# (such as a company or product suite) can be grouped.
# The default value is: Doxygen generated docs.
# This tag requires that the tag GENERATE_DOCSET is set to YES.

DOCSET_FEEDNAME        = "Doxygen generated docs"

# This tag specifies a string that should uniquely identify the documentation
# set bundle. This should be a reverse domain-name style string, e.g.
# com.mycompany.MyDocSet. Doxygen will append .docset to the name.
# The default value is: org.doxygen.Project.
# This tag requires that the tag GENERATE_DOCSET is set to YES.

DOCSET_BUNDLE_ID       = org.doxygen.Project

# The DOCSET_PUBLISHER_ID tag specifies a string that should uniquely identify
# the documentation publisher. This should be a reverse domain-name style
# string, e.g. com.mycompany.MyDocSet.documentation.
# The default value is: org.doxygen.Publisher.
# This tag requires that the tag GENERATE_DOCSET is set to YES.

DOCSET_PUBLISHER_ID    = org.doxygen.Publisher

# The DOCSET_PUBLISHER_NAME tag identifies the documentation publisher.
# The default value is: Publisher.
# This tag requires that the tag GENERATE_DOCSET is set to YES.

DOCSET_PUBLISHER_NAME  = Publisher

# If the GENERATE_HTMLHELP tag is set to YES then doxygen generates three
# additional HTML index files: index.hhp, index.hhc, and index.hhk. The
# index.hhp is a project file that can be read by Microsoft's HTML Help Workshop
# (see: http://www.microsoft.com/en-us/download/details.aspx?id=21138) on
# Windows.
#
# The HTML Help Workshop contains a compiler that can convert all HTML output
# generated by doxygen into a single compiled HTML file (.chm). Compiled HTML
# files are now used as the Windows 98 help format, and will replace the old
# Windows help format (.hlp) on all Windows platforms in the future. Compressed
# HTML files also contain an index, a table of contents, and you can search for
# words in the documentation. The HTML workshop also contains a viewer for
# compressed HTML files.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTML is set to YES.

GENERATE_HTMLHELP      = NO

# The CHM_FILE tag can be used to specify the file name of the resulting .chm
# file. You can add a path in front of the file if the result should not be
# written to the html output directory.
# This tag requires that the tag GENERATE_HTMLHELP is set to YES.

CHM_FILE               = 

# The HHC_LOCATION tag can be used to specify the location (absolute path
# including file name) of the HTML help compiler (hhc.exe). If non-empty,
# doxygen will try to run the HTML help compiler on the generated index.hhp.
# The file has to be specified with full path.
# This tag requires that the tag GENERATE_HTMLHELP is set to YES.

HHC_LOCATION           = 

# The GENERATE_CHI flag controls if a separate .chi index file is generated
# (YES) or that it should be included in the master .chm file (NO).
# The default value is: NO.
# This tag requires that the tag GENERATE_HTMLHELP is set to YES.

GENERATE_CHI           = NO

# The CHM_INDEX_ENCODING is used to encode HtmlHelp index (hhk), content (hhc)
# and project file content.
# This tag requires that the tag GENERATE_HTMLHELP is set to YES.

CHM_INDEX_ENCODING     = 

# The BINARY_TOC flag controls whether a binary table of contents is generated
# (YES) or a normal table of contents (NO) in the .chm file. Furthermore it
# enables the Previous and Next buttons.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTMLHELP is set to YES.

BINARY_TOC             = NO

# The TOC_EXPAND flag can be set to YES to add extra items for group members to
# the table of contents of the HTML help documentation and to the tree view.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTMLHELP is set to YES.

TOC_EXPAND             = NO

# If the GENERATE_QHP tag is set to YES and both QHP_NAMESPACE and
# QHP_VIRTUAL_FOLDER are set, an additional index file will be generated that
# can be used as input for Qt's qhelpgenerator to generate a Qt Compressed Help
# (.qch) of the generated HTML documentation.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTML is set to YES.

GENERATE_QHP           = NO

# If the QHG_LOCATION tag is specified, the QCH_FILE tag can be used to specify
# the file name of the resulting .qch file. The path specified is relative to
# the HTML output folder.
# This tag requires that the tag GENERATE_QHP is set to YES.

QCH_FILE               = 

# The QHP_NAMESPACE tag specifies the namespace to use when generating Qt Help
# Project output. For more information please see Qt Help Project / Namespace
# (see: http://qt-project.org/doc/qt-4.8/qthelpproject.html#namespace).
# The default value is: org.doxygen.Project.
# This tag requires that the tag GENERATE_QHP is set to YES.

QHP_NAMESPACE          = org.doxygen.Project

# The QHP_VIRTUAL_FOLDER tag specifies the namespace to use when generating Qt
# Help Project output. For more information please see Qt Help Project / Virtual
# Folders (see: http://qt-project.org/doc/qt-4.8/qthelpproject.html#virtual-
# folders).
# The default value is: doc.
# This tag requires that the tag GENERATE_QHP is set to YES.

QHP_VIRTUAL_FOLDER     = doc

# If the QHP_CUST_FILTER_NAME tag is set, it specifies the name of a custom
# filter to add. For more information please see Qt Help Project / Custom
# Filters (see: http://qt-project.org/doc/qt-4.8/qthelpproject.html#custom-
# filters).
# This tag requires that the tag GENERATE_QHP is set to YES.

QHP_CUST_FILTER_NAME   = 

# The QHP_CUST_FILTER_ATTRS tag specifies the list of the attributes of the
# custom filter to add. For more information please see Qt Help Project / Custom
# Filters (see: http://qt-project.org/doc/qt-4.8/qthelpproject.html#custom-
# filters).
# This tag requires that the tag GENERATE_QHP is set to YES.

QHP_CUST_FILTER_ATTRS  = 

# The QHP_SECT_FILTER_ATTRS tag specifies the list of the attributes this
# project's filter section matches. Qt Help Project / Filter Attributes (see:
# http://qt-project.org/doc/qt-4.8/qthelpproject.html#filter-attributes).
# This tag requires that the tag GENERATE_QHP is set to YES.

QHP_SECT_FILTER_ATTRS  = 

# The QHG_LOCATION tag can be used to specify the location of Qt's
# qhelpgenerator. If non-empty doxygen will try to run qhelpgenerator on the
# generated .qhp file.
# This tag requires that the tag GENERATE_QHP is set to YES.

QHG_LOCATION           = 

# If the GENERATE_ECLIPSEHELP tag is set to YES, additional index files will be
# generated, together with the HTML files, they form an Eclipse help plugin. To
# install this plugin and make it available under the help contents menu in
# Eclipse, the contents of the directory containing the HTML and XML files needs
# to be copied into the plugins directory of eclipse. The name of the directory
# within the plugins directory should be the same as the ECLIPSE_DOC_ID value.
# After copying Eclipse needs to be restarted before the help appears.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTML is set to YES.

GENERATE_ECLIPSEHELP   = NO

# A unique identifier for the Eclipse help plugin. When installing the plugin
# the directory name containing the HTML and XML files should also have this
# name. Each documentation set should have its own identifier.
# The default value is: org.doxygen.Project.
# This tag requires that the tag GENERATE_ECLIPSEHELP is set to YES.

ECLIPSE_DOC_ID         = org.doxygen.Project

# If you want full control over the layout of the generated HTML pages it might
# be necessary to disable the index and replace it with your own. The
# DISABLE_INDEX tag can be used to turn on/off the condensed index (tabs) at top
# of each HTML page. A value of NO enables the index and the value YES disables
# it. Since the tabs in the index contain the same information as the navigation
# tree, you can set this option to YES if you also set GENERATE_TREEVIEW to YES.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTML is set to YES.

DISABLE_INDEX          = NO

# The GENERATE_TREEVIEW tag is used to specify whether a tree-like index
# structure should be generated to display hierarchical information. If the tag
# value is set to YES, a side panel will be generated containing a tree-like
# index structure (just like the one that is generated for HTML Help). For this
# to work a browser that supports JavaScript, DHTML, CSS and frames is required
# (i.e. any modern browser). Windows users are probably better off using the
# HTML help feature. Via custom style sheets (see HTML_EXTRA_STYLESHEET) one can
# further fine-tune the look of the index. As an example, the default style
# sheet generated by doxygen has an example that shows how to put an image at
# the root of the tree instead of the PROJECT_NAME. Since the tree basically has
# the same information as the tab index, you could consider setting
# DISABLE_INDEX to YES when enabling this option.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTML is set to YES.

GENERATE_TREEVIEW      = YES

# The ENUM_VALUES_PER_LINE tag can be used to set the number of enum values that
# doxygen will group on one line in the generated HTML documentation.
#
# Note that a value of 0 will completely suppress the enum values from appearing
# in the overview section.
# Minimum value: 0, maximum value: 20, default value: 4.
# This tag requires that the tag GENERATE_HTML is set to YES.

ENUM_VALUES_PER_LINE   = 4

# If the treeview is enabled (see GENERATE_TREEVIEW) then this tag can be used
# to set the initial width (in pixels) of the frame in which the tree is shown.
# Minimum value: 0, maximum value: 1500, default value: 250.
# This tag requires that the tag GENERATE_HTML is set to YES.

TREEVIEW_WIDTH         = 250

# If the EXT_LINKS_IN_WINDOW option is set to YES, doxygen will open links to
# external symbols imported via tag files in a separate window.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTML is set to YES.

EXT_LINKS_IN_WINDOW    = NO

# Use this tag to change the font size of LaTeX formulas included as images in
# the HTML documentation. When you change the font size after a successful
# doxygen run you need to manually remove any form_*.png images from the HTML
# output directory to force them to be regenerated.
# Minimum value: 8, maximum value: 50, default value: 10.
# This tag requires that the tag GENERATE_HTML is set to YES.

FORMULA_FONTSIZE       = 10

# Use the FORMULA_TRANPARENT tag to determine whether or not the images
# generated for formulas are transparent PNGs. Transparent PNGs are not
# supported properly for IE 6.0, but are supported on all modern browsers.
#
# Note that when changing this option you need to delete any form_*.png files in
# the HTML output directory before the changes have effect.
# The default value is: YES.
# This tag requires that the tag GENERATE_HTML is set to YES.

FORMULA_TRANSPARENT    = YES

# Enable the USE_MATHJAX option to render LaTeX formulas using MathJax (see
# http://www.mathjax.org) which uses client side Javascript for the rendering
# instead of using pre-rendered bitmaps. Use this if you do not have LaTeX
# installed or if you want to formulas look prettier in the HTML output. When
# enabled you may also need to install MathJax separately and configure the path
# to it using the MATHJAX_RELPATH option.
# The default value is: NO.
# This tag requires that the tag GENERATE_HTML is set to YES.

USE_MATHJAX            = NO

# When MathJax is enabled you can set the default output format to be used for
# the MathJax output. See the MathJax site (see:
# http://docs.mathjax.org/en/latest/output.html) for more details.
# Possible values are: HTML-CSS (which is slower, but has the best
# compatibility), NativeMML (i.e. MathML) and SVG.
# The default value is: HTML-CSS.
# This tag requires that the tag USE_MATHJAX is set to YES.

MATHJAX_FORMAT         = HTML-CSS

# When MathJax is enabled you need to specify the location relative to the HTML
# output directory using the MATHJAX_RELPATH option. The destination directory
# should contain the MathJax.js script. For instance, if the mathjax directory
# is located at the same level as the HTML output directory, then
# MATHJAX_RELPATH should be ../mathjax. The default value points to the MathJax
# Content Delivery Network so you can quickly see the result without installing
# MathJax. However, it is strongly recommended to install a local copy of
# MathJax from http://www.mathjax.org before deployment.
# The default value is: http://cdn.mathjax.org/mathjax/latest.
# This tag requires that the tag USE_MATHJAX is set to YES.

MATHJAX_RELPATH        = http://www.mathjax.org/mathjax

# The MATHJAX_EXTENSIONS tag can be used to specify one or more MathJax
# extension names that should be enabled during MathJax rendering. For example
# MATHJAX_EXTENSIONS = TeX/AMSmath TeX/AMSsymbols
# This tag requires that the tag USE_MATHJAX is set to YES.

MATHJAX_EXTENSIONS     = 

# The MATHJAX_CODEFILE tag can be used to specify a file with javascript pieces
# of code that will be used on startup of the MathJax code. See the MathJax site
# (see: http://docs.mathjax.org/en/latest/output.html) for more details. For an
# example see the documentation.
# This tag requires that the tag USE_MATHJAX is set to YES.

MATHJAX_CODEFILE       = 

# When the SEARCHENGINE tag is enabled doxygen will generate a search box for
# the HTML output. The underlying search engine uses javascript and DHTML and
# should work on any modern browser. Note that when using HTML help
# (GENERATE_HTMLHELP), Qt help (GENERATE_QHP), or docsets (GENERATE_DOCSET)
# there is already a search function so this one should typically be disabled.
# For large projects the javascript based search engine can be slow, then
# enabling SERVER_BASED_SEARCH may provide a better solution. It is possible to
# search using the keyboard; to jump to the search box use <access key> + S
# (what the <access key> is depends on the OS and browser, but it is typically
# <CTRL>, <ALT>/<option>, or both). Inside the search box use the <cursor down
# key> to jump into the search results window, the results can be navigated
# using the <cursor keys>. Press <Enter> to select an item or <escape> to cancel
# the search. The filter options can be selected when the cursor is inside the
# search box by pressing <Shift>+<cursor down>. Also here use the <cursor keys>
# to select a filter and <Enter> or <escape> to activate or cancel the filter
# option.
# The default value is: YES.
# This tag requires that the tag GENERATE_HTML is set to YES.

SEARCHENGINE           = YES

# When the SERVER_BASED_SEARCH tag is enabled the search engine will be
# implemented using a web server instead of a web client using Javascript. There
# are two flavors of web server based searching depending on the EXTERNAL_SEARCH
# setting. When disabled, doxygen will generate a PHP script for searching and
# an index file used by the script. When EXTERNAL_SEARCH is enabled the indexing
# and searching needs to be provided by external tools. See the section
# "External Indexing and Searching" for details.
# The default value is: NO.
# This tag requires that the tag SEARCHENGINE is set to YES.

SERVER_BASED_SEARCH    = NO

# When EXTERNAL_SEARCH tag is enabled doxygen will no longer generate the PHP
# script for searching. Instead the search results are written to an XML file
# which needs to be processed by an external indexer. Doxygen will invoke an
# external search engine pointed to by the SEARCHENGINE_URL option to obtain the
# search results.
#
# Doxygen ships with an example indexer (doxyindexer) and search engine
# (doxysearch.cgi) which are based on the open source search engine library
# Xapian (see: http://xapian.org/).
#
# See the section "External Indexing and Searching" for details.
# The default value is: NO.
# This tag requires that the tag SEARCHENGINE is set to YES.

EXTERNAL_SEARCH        = NO

# The SEARCHENGINE_URL should point to a search engine hosted by a web server
# which will return the search results when EXTERNAL_SEARCH is enabled.
#
# Doxygen ships with an example indexer (doxyindexer) and search engine
# (doxysearch.cgi) which are based on the open source search engine library
# Xapian (see: http://xapian.org/). See the section "External Indexing and
# Searching" for details.
# This tag requires that the tag SEARCHENGINE is set to YES.

SEARCHENGINE_URL       = 

# When SERVER_BASED_SEARCH and EXTERNAL_SEARCH are both enabled the unindexed
# search data is written to a file for indexing by an external tool. With the
# SEARCHDATA_FILE tag the name of this file can be specified.
# The default file is: searchdata.xml.
# This tag requires that the tag SEARCHENGINE is set to YES.

SEARCHDATA_FILE        = searchdata.xml

# When SERVER_BASED_SEARCH and EXTERNAL_SEARCH are both enabled the
# EXTERNAL_SEARCH_ID tag can be used as an identifier for the project. This is
# useful in combination with EXTRA_SEARCH_MAPPINGS to search through multiple
# projects and redirect the results back to the right project.
# This tag requires that the tag SEARCHENGINE is set to YES.

EXTERNAL_SEARCH_ID     = 

# The EXTRA_SEARCH_MAPPINGS tag can be used to enable searching through doxygen
# projects other than the one defined by this configuration file, but that are
# all added to the same external search index. Each project needs to have a
# unique id set via EXTERNAL_SEARCH_ID. The search mapping then maps the id of
# to a relative location where the documentation can be found. The format is:
# EXTRA_SEARCH_MAPPINGS = tagname1=loc1 tagname2=loc2 ...
# This tag requires that the tag SEARCHENGINE is set to YES.

EXTRA_SEARCH_MAPPINGS  = 

#---------------------------------------------------------------------------
# Configuration options related to the LaTeX output
#---------------------------------------------------------------------------

# If the GENERATE_LATEX tag is set to YES, doxygen will generate LaTeX output.
# The default value is: YES.

GENERATE_LATEX         = NO

# The LATEX_OUTPUT tag is used to specify where the LaTeX docs will be put. If a
# relative path is entered the value of OUTPUT_DIRECTORY will be put in front of
# it.
# The default directory is: latex.
# This tag requires that the tag GENERATE_LATEX is set to YES.

LATEX_OUTPUT           = latex

# The LATEX_CMD_NAME tag can be used to specify the LaTeX command name to be
# invoked.
#
# Note that when enabling USE_PDFLATEX this option is only used for generating
# bitmaps for formulas in the HTML output, but not in the Makefile that is
# written to the output directory.
# The default file is: latex.
# This tag requires that the tag GENERATE_LATEX is set to YES.

LATEX_CMD_NAME         = latex

# The MAKEINDEX_CMD_NAME tag can be used to specify the command name to generate
# index for LaTeX.
# The default file is: makeindex.
# This tag requires that the tag GENERATE_LATEX is set to YES.

MAKEINDEX_CMD_NAME     = makeindex

# If the COMPACT_LATEX tag is set to YES, doxygen generates more compact LaTeX
# documents. This may be useful for small projects and may help to save some
# trees in general.
# The default value is: NO.
# This tag requires that the tag GENERATE_LATEX is set to YES.

COMPACT_LATEX          = NO

# The PAPER_TYPE tag can be used to set the paper type that is used by the
# printer.
# Possible values are: a4 (210 x 297 mm), letter (8.5 x 11 inches), legal (8.5 x
# 14 inches) and executive (7.25 x 10.5 inches).
# The default value is: a4.
# This tag requires that the tag GENERATE_LATEX is set to YES.

PAPER_TYPE             = a4

# The EXTRA_PACKAGES tag can be used to specify one or more LaTeX package names
# that should be included in the LaTeX output. The package can be specified just
# by its name or with the correct syntax as to be used with the LaTeX
# \usepackage command. To get the times font for instance you can specify :
# EXTRA_PACKAGES=times or EXTRA_PACKAGES={times}
# To use the option intlimits with the amsmath package you can specify:
# EXTRA_PACKAGES=[intlimits]{amsmath}
# If left blank no extra packages will be included.
# This tag requires that the tag GENERATE_LATEX is set to YES.

EXTRA_PACKAGES         = 

# The LATEX_HEADER tag can be used to specify a personal LaTeX header for the
# generated LaTeX document. The header should contain everything until the first
# chapter. If it is left blank doxygen will generate a standard header. See
# section "Doxygen usage" for information on how to let doxygen write the
# default header to a separate file.
#
# Note: Only use a user-defined header if you know what you are doing! The
# following commands have a special meaning inside the header: $title,
# $datetime, $date, $doxygenversion, $projectname, $projectnumber,
# $projectbrief, $projectlogo. Doxygen will replace $title with the empty
# string, for the replacement values of the other commands the user is referred
# to HTML_HEADER.
# This tag requires that the tag GENERATE_LATEX is set to YES.

LATEX_HEADER           = 

# The LATEX_FOOTER tag can be used to specify a personal LaTeX footer for the
# generated LaTeX document. The footer should contain everything after the last
# chapter. If it is left blank doxygen will generate a standard footer. See
# LATEX_HEADER for more information on how to generate a default footer and what
# special commands can be used inside the footer.
#
# Note: Only use a user-defined footer if you know what you are doing!
# This tag requires that the tag GENERATE_LATEX is set to YES.

LATEX_FOOTER           = 

# The LATEX_EXTRA_STYLESHEET tag can be used to specify additional user-defined
# LaTeX style sheets that are included after the standard style sheets created
# by doxygen. Using this option one can overrule certain style aspects. Doxygen
# will copy the style sheet files to the output directory.
# Note: The order of the extra style sheet files is of importance (e.g. the last
# style sheet in the list overrules the setting of the previous ones in the
# list).
# This tag requires that the tag GENERATE_LATEX is set to YES.

LATEX_EXTRA_STYLESHEET = 

# The LATEX_EXTRA_FILES tag can be used to specify one or more extra images or
# other source files which should be copied to the LATEX_OUTPUT output
# directory. Note that the files will be copied as-is; there are no commands or
# markers available.
# This tag requires that the tag GENERATE_LATEX is set to YES.

LATEX_EXTRA_FILES      = 

# If the PDF_HYPERLINKS tag is set to YES, the LaTeX that is generated is
# prepared for conversion to PDF (using ps2pdf or pdflatex). The PDF file will
# contain links (just like the HTML output) instead of page references. This
# makes the output suitable for online browsing using a PDF viewer.
# The default value is: YES.
# This tag requires that the tag GENERATE_LATEX is set to YES.

PDF_HYPERLINKS         = YES

# If the USE_PDFLATEX tag is set to YES, doxygen will use pdflatex to generate
# the PDF file directly from the LaTeX files. Set this option to YES, to get a
# higher quality PDF documentation.
# The default value is: YES.
# This tag requires that the tag GENERATE_LATEX is set to YES.

USE_PDFLATEX           = YES

# If the LATEX_BATCHMODE tag is set to YES, doxygen will add the \batchmode
# command to the generated LaTeX files. This will instruct LaTeX to keep running
# if errors occur, instead of asking the user for help. This option is also used
# when generating formulas in HTML.
# The default value is: NO.
# This tag requires that the tag GENERATE_LATEX is set to YES.

LATEX_BATCHMODE        = NO

# If the LATEX_HIDE_INDICES tag is set to YES then doxygen will not include the
# index chapters (such as File Index, Compound Index, etc.) in the output.
# The default value is: NO.
# This tag requires that the tag GENERATE_LATEX is set to YES.

LATEX_HIDE_INDICES     = NO

# If the LATEX_SOURCE_CODE tag is set to YES then doxygen will include source
# code with syntax highlighting in the LaTeX output.
#
# Note that which sources are shown also depends on other settings such as
# SOURCE_BROWSER.
# The default value is: NO.
# This tag requires that the tag GENERATE_LATEX is set to YES.

LATEX_SOURCE_CODE      = NO

# The LATEX_BIB_STYLE tag can be used to specify the style to use for the
# bibliography, e.g. plainnat, or ieeetr. See
# http://en.wikipedia.org/wiki/BibTeX and \cite for more info.
# The default value is: plain.
# This tag requires that the tag GENERATE_LATEX is set to YES.

LATEX_BIB_STYLE        = plain

# If the LATEX_TIMESTAMP tag is set to YES then the footer of each generated
# page will contain the date and time when the page was generated. Setting this
# to NO can help when comparing the output of multiple runs.
# The default value is: NO.
# This tag requires that the tag GENERATE_LATEX is set to YES.

LATEX_TIMESTAMP        = NO

#---------------------------------------------------------------------------
# Configuration options related to the RTF output
#---------------------------------------------------------------------------

# If the GENERATE_RTF tag is set to YES, doxygen will generate RTF output. The
# RTF output is optimized for Word 97 and may not look too pretty with other RTF
# readers/editors.
# The default value is: NO.

GENERATE_RTF           = NO

# The RTF_OUTPUT tag is used to specify where the RTF docs will be put. If a
# relative path is entered the value of OUTPUT_DIRECTORY will be put in front of
# it.
# The default directory is: rtf.
# This tag requires that the tag GENERATE_RTF is set to YES.

RTF_OUTPUT             = rtf

# If the COMPACT_RTF tag is set to YES, doxygen generates more compact RTF
# documents. This may be useful for small projects and may help to save some
# trees in general.
# The default value is: NO.
# This tag requires that the tag GENERATE_RTF is set to YES.

COMPACT_RTF            = NO

# If the RTF_HYPERLINKS tag is set to YES, the RTF that is generated will
# contain hyperlink fields. The RTF file will contain links (just like the HTML
# output) instead of page references. This makes the output suitable for online
# browsing using Word or some other Word compatible readers that support those
# fields.
#
# Note: WordPad (write) and others do not support links.
# The default value is: NO.
# This tag requires that the tag GENERATE_RTF is set to YES.

RTF_HYPERLINKS         = NO

# Load stylesheet definitions from file. Syntax is similar to doxygen's config
# file, i.e. a series of assignments. You only have to provide replacements,
# missing definitions are set to their default value.
#
# See also section "Doxygen usage" for information on how to generate the
# default style sheet that doxygen normally uses.
# This tag requires that the tag GENERATE_RTF is set to YES.

RTF_STYLESHEET_FILE    = 

# Set optional variables used in the generation of an RTF document. Syntax is
# similar to doxygen's config file. A template extensions file can be generated
# using doxygen -e rtf extensionFile.
# This tag requires that the tag GENERATE_RTF is set to YES.

RTF_EXTENSIONS_FILE    = 

# If the RTF_SOURCE_CODE tag is set to YES then doxygen will include source code
# with syntax highlighting in the RTF output.
#
# Note that which sources are shown also depends on other settings such as
# SOURCE_BROWSER.
# The default value is: NO.
# This tag requires that the tag GENERATE_RTF is set to YES.

RTF_SOURCE_CODE        = NO

#---------------------------------------------------------------------------
# Configuration options related to the man page output
#---------------------------------------------------------------------------

# If the GENERATE_MAN tag is set to YES, doxygen will generate man pages for
# classes and files.
# The default value is: NO.

GENERATE_MAN           = NO

# The MAN_OUTPUT tag is used to specify where the man pages will be put. If a
# relative path is entered the value of OUTPUT_DIRECTORY will be put in front of
# it. A directory man3 will be created inside the directory specified by
# MAN_OUTPUT.
# The default directory is: man.
# This tag requires that the tag GENERATE_MAN is set to YES.

MAN_OUTPUT             = man

# The MAN_EXTENSION tag determines the extension that is added to the generated
# man pages. In case the manual section does not start with a number, the number
# 3 is prepended. The dot (.) at the beginning of the MAN_EXTENSION tag is
# optional.
# The default value is: .3.
# This tag requires that the tag GENERATE_MAN is set to YES.

MAN_EXTENSION          = .3

# The MAN_SUBDIR tag determines the name of the directory created within
# MAN_OUTPUT in which the man pages are placed. If defaults to man followed by
# MAN_EXTENSION with the initial . removed.
# This tag requires that the tag GENERATE_MAN is set to YES.

MAN_SUBDIR             = 

# If the MAN_LINKS tag is set to YES and doxygen generates man output, then it
# will generate one additional man file for each entity documented in the real
# man page(s). These additional files only source the real man page, but without
# them the man command would be unable to find the correct page.
# The default value is: NO.
# This tag requires that the tag GENERATE_MAN is set to YES.

MAN_LINKS              = NO

#---------------------------------------------------------------------------
# Configuration options related to the XML output
#---------------------------------------------------------------------------

# If the GENERATE_XML tag is set to YES, doxygen will generate an XML file that
# captures the structure of the code including all documentation.
# The default value is: NO.

GENERATE_XML           = NO

# The XML_OUTPUT tag is used to specify where the XML pages will be put. If a
# relative path is entered the value of OUTPUT_DIRECTORY will be put in front of
# it.
# The default directory is: xml.
# This tag requires that the tag GENERATE_XML is set to YES.

XML_OUTPUT             = xml

# If the XML_PROGRAMLISTING tag is set to YES, doxygen will dump the program
# listings (including syntax highlighting and cross-referencing information) to
# the XML output. Note that enabling this will significantly increase the size
# of the XML output.
# The default value is: YES.
# This tag requires that the tag GENERATE_XML is set to YES.

XML_PROGRAMLISTING     = YES

#---------------------------------------------------------------------------
# Configuration options related to the DOCBOOK output
#---------------------------------------------------------------------------

# If the GENERATE_DOCBOOK tag is set to YES, doxygen will generate Docbook files
# that can be used to generate PDF.
# The default value is: NO.

GENERATE_DOCBOOK       = NO

# The DOCBOOK_OUTPUT tag is used to specify where the Docbook pages will be put.
# If a relative path is entered the value of OUTPUT_DIRECTORY will be put in
# front of it.
# The default directory is: docbook.
# This tag requires that the tag GENERATE_DOCBOOK is set to YES.

DOCBOOK_OUTPUT         = docbook

# If the DOCBOOK_PROGRAMLISTING tag is set to YES, doxygen will include the
# program listings (including syntax highlighting and cross-referencing
# information) to the DOCBOOK output. Note that enabling this will significantly
# increase the size of the DOCBOOK output.
# The default value is: NO.
# This tag requires that the tag GENERATE_DOCBOOK is set to YES.

DOCBOOK_PROGRAMLISTING = NO

#---------------------------------------------------------------------------
# Configuration options for the AutoGen Definitions output
#---------------------------------------------------------------------------

# If the GENERATE_AUTOGEN_DEF tag is set to YES, doxygen will generate an
# AutoGen Definitions (see http://autogen.sf.net) file that captures the
# structure of the code including all documentation. Note that this feature is
# still experimental and incomplete at the moment.
# The default value is: NO.

GENERATE_AUTOGEN_DEF   = NO

#---------------------------------------------------------------------------
# Configuration options related to the Perl module output
#---------------------------------------------------------------------------

# If the GENERATE_PERLMOD tag is set to YES, doxygen will generate a Perl module
# file that captures the structure of the code including all documentation.
#
# Note that this feature is still experimental and incomplete at the moment.
# The default value is: NO.

GENERATE_PERLMOD       = NO

# If the PERLMOD_LATEX tag is set to YES, doxygen will generate the necessary
# Makefile rules, Perl scripts and LaTeX code to be able to generate PDF and DVI
# output from the Perl module output.
# The default value is: NO.
# This tag requires that the tag GENERATE_PERLMOD is set to YES.

PERLMOD_LATEX          = NO

# If the PERLMOD_PRETTY tag is set to YES, the Perl module output will be nicely
# formatted so it can be parsed by a human reader. This is useful if you want to
# understand what is going on. On the other hand, if this tag is set to NO, the
# size of the Perl module output will be much smaller and Perl will parse it
# just the same.
# The default value is: YES.
# This tag requires that the tag GENERATE_PERLMOD is set to YES.

PERLMOD_PRETTY         = YES

# The names of the make variables in the generated doxyrules.make file are
# prefixed with the string contained in PERLMOD_MAKEVAR_PREFIX. This is useful
# so different doxyrules.make files included by the same Makefile don't
# overwrite each other's variables.
# This tag requires that the tag GENERATE_PERLMOD is set to YES.

PERLMOD_MAKEVAR_PREFIX = 

#---------------------------------------------------------------------------
# Configuration options related to the preprocessor
#---------------------------------------------------------------------------

# If the ENABLE_PREPROCESSING tag is set to YES, doxygen will evaluate all
# C-preprocessor directives found in the sources and include files.
# The default value is: YES.

ENABLE_PREPROCESSING   = YES

# If the MACRO_EXPANSION tag is set to YES, doxygen will expand all macro names
# in the source code. If set to NO, only conditional compilation will be
# performed. Macro expansion can be done in a controlled way by setting
# EXPAND_ONLY_PREDEF to YES.
# The default value is: NO.
# This tag requires that the tag ENABLE_PREPROCESSING is set to YES.

MACRO_EXPANSION        = NO

# If the EXPAND_ONLY_PREDEF and MACRO_EXPANSION tags are both set to YES then
# the macro expansion is limited to the macros specified with the PREDEFINED and
# EXPAND_AS_DEFINED tags.
# The default value is: NO.
# This tag requires that the tag ENABLE_PREPROCESSING is set to YES.

EXPAND_ONLY_PREDEF     = NO

# If the SEARCH_INCLUDES tag is set to YES, the include files in the
# INCLUDE_PATH will be searched if a #include is found.
# The default value is: YES.
# This tag requires that the tag ENABLE_PREPROCESSING is set to YES.

SEARCH_INCLUDES        = YES

# The INCLUDE_PATH tag can be used to specify one or more directories that
# contain include files that are not input files but should be processed by the
# preprocessor.
# This tag requires that the tag SEARCH_INCLUDES is set to YES.

INCLUDE_PATH           = 

# You can use the INCLUDE_FILE_PATTERNS tag to specify one or more wildcard
# patterns (like *.h and *.hpp) to filter out the header-files in the
# directories. If left blank, the patterns specified with FILE_PATTERNS will be
# used.
# This tag requires that the tag ENABLE_PREPROCESSING is set to YES.

INCLUDE_FILE_PATTERNS  = 

# The PREDEFINED tag can be used to specify one or more macro names that are
# defined before the preprocessor is started (similar to the -D option of e.g.
# gcc). The argument of the tag is a list of macros of the form: name or
# name=definition (no spaces). If the definition and the "=" are omitted, "=1"
# is assumed. To prevent a macro definition from being undefined via #undef or
# recursively expanded use the := operator instead of the = operator.
# This tag requires that the tag ENABLE_PREPROCESSING is set to YES.

PREDEFINED             = 

# If the MACRO_EXPANSION and EXPAND_ONLY_PREDEF tags are set to YES then this
# tag can be used to specify a list of macro names that should be expanded. The
# macro definition that is found in the sources will be used. Use the PREDEFINED
# tag if you want to use a different macro definition that overrules the
# definition found in the source code.
# This tag requires that the tag ENABLE_PREPROCESSING is set to YES.

EXPAND_AS_DEFINED      = 

# If the SKIP_FUNCTION_MACROS tag is set to YES then doxygen's preprocessor will
# remove all references to function-like macros that are alone on a line, have
# an all uppercase name, and do not end with a semicolon. Such function macros
# are typically used for boiler-plate code, and will confuse the parser if not
# removed.
# The default value is: YES.
# This tag requires that the tag ENABLE_PREPROCESSING is set to YES.

SKIP_FUNCTION_MACROS   = YES

#---------------------------------------------------------------------------
# Configuration options related to external references
#---------------------------------------------------------------------------

# The TAGFILES tag can be used to specify one or more tag files. For each tag
# file the location of the external documentation should be added. The format of
# a tag file without this location is as follows:
# TAGFILES = file1 file2 ...
# Adding location for the tag files is done as follows:
# TAGFILES = file1=loc1 "file2 = loc2" ...
# where loc1 and loc2 can be relative or absolute paths or URLs. See the
# section "Linking to external documentation" for more information about the use
# of tag files.
# Note: Each tag file must have a unique name (where the name does NOT include
# the path). If a tag file is not located in the directory in which doxygen is
# run, you must also specify the path to the tagfile here.

TAGFILES               = 

# When a file name is specified after GENERATE_TAGFILE, doxygen will create a
# tag file that is based on the input files it reads. See section "Linking to
# external documentation" for more information about the usage of tag files.

GENERATE_TAGFILE       = 

# If the ALLEXTERNALS tag is set to YES, all external class will be listed in
# the class index. If set to NO, only the inherited external classes will be
# listed.
# The default value is: NO.

ALLEXTERNALS           = NO

# If the EXTERNAL_GROUPS tag is set to YES, all external groups will be listed
# in the modules index. If set to NO, only the current project's groups will be
# listed.
# The default value is: YES.

EXTERNAL_GROUPS        = YES

# If the EXTERNAL_PAGES tag is set to YES, all external pages will be listed in
# the related pages index. If set to NO, only the current project's pages will
# be listed.
# The default value is: YES.

EXTERNAL_PAGES         = YES

# The PERL_PATH should be the absolute path and name of the perl script
# interpreter (i.e. the result of 'which perl').
# The default file (with absolute path) is: /usr/bin/perl.

PERL_PATH              = /usr/bin/perl

#---------------------------------------------------------------------------
# Configuration options related to the dot tool
#---------------------------------------------------------------------------

# If the CLASS_DIAGRAMS tag is set to YES, doxygen will generate a class diagram
# (in HTML and LaTeX) for classes with base or super classes. Setting the tag to
# NO turns the diagrams off. Note that this option also works with HAVE_DOT
# disabled, but it is recommended to install and use dot, since it yields more
# powerful graphs.
# The default value is: YES.

CLASS_DIAGRAMS         = YES

# You can define message sequence charts within doxygen comments using the \msc
# command. Doxygen will then run the mscgen tool (see:
# http://www.mcternan.me.uk/mscgen/)) to produce the chart and insert it in the
# documentation. The MSCGEN_PATH tag allows you to specify the directory where
# the mscgen tool resides. If left empty the tool is assumed to be found in the
# default search path.

MSCGEN_PATH            = 

# You can include diagrams made with dia in doxygen documentation. Doxygen will
# then run dia to produce the diagram and insert it in the documentation. The
# DIA_PATH tag allows you to specify the directory where the dia binary resides.
# If left empty dia is assumed to be found in the default search path.

DIA_PATH               = 

# If set to YES the inheritance and collaboration graphs will hide inheritance
# and usage relations if the target is undocumented or is not a class.
# The default value is: YES.

HIDE_UNDOC_RELATIONS   = YES

# If you set the HAVE_DOT tag to YES then doxygen will assume the dot tool is
# available from the path. This tool is part of Graphviz (see:
# http://www.graphviz.org/), a graph visualization toolkit from AT&T and Lucent
# Bell Labs. The other options in this section have no effect if this option is
# set to NO
# The default value is: NO.

HAVE_DOT               = YES

# The DOT_NUM_THREADS specifies the number of dot invocations doxygen is allowed
# to run in parallel. When set to 0 doxygen will base this on the number of
# processors available in the system. You can set it explicitly to a value
# larger than 0 to get control over the balance between CPU load and processing
# speed.
# Minimum value: 0, maximum value: 32, default value: 0.
# This tag requires that the tag HAVE_DOT is set to YES.

DOT_NUM_THREADS        = 0

# When you want a differently looking font in the dot files that doxygen
# generates you can specify the font name using DOT_FONTNAME. You need to make
# sure dot is able to find the font, which can be done by putting it in a
# standard location or by setting the DOTFONTPATH environment variable or by
# setting DOT_FONTPATH to the directory containing the font.
# The default value is: Helvetica.
# This tag requires that the tag HAVE_DOT is set to YES.

DOT_FONTNAME           = Helvetica

# The DOT_FONTSIZE tag can be used to set the size (in points) of the font of
# dot graphs.
# Minimum value: 4, maximum value: 24, default value: 10.
# This tag requires that the tag HAVE_DOT is set to YES.

DOT_FONTSIZE           = 10

# By default doxygen will tell dot to use the default font as specified with
# DOT_FONTNAME. If you specify a different font using DOT_FONTNAME you can set
# the path where dot can find it using this tag.
# This tag requires that the tag HAVE_DOT is set to YES.

DOT_FONTPATH           = 

# If the CLASS_GRAPH tag is set to YES then doxygen will generate a graph for
# each documented class showing the direct and indirect inheritance relations.
# Setting this tag to YES will force the CLASS_DIAGRAMS tag to NO.
# The default value is: YES.
# This tag requires that the tag HAVE_DOT is set to YES.

CLASS_GRAPH            = YES

# If the COLLABORATION_GRAPH tag is set to YES then doxygen will generate a
# graph for each documented class showing the direct and indirect implementation
# dependencies (inheritance, containment, and class references variables) of the
# class with other documented classes.
# The default value is: YES.
# This tag requires that the tag HAVE_DOT is set to YES.

COLLABORATION_GRAPH    = YES

# If the GROUP_GRAPHS tag is set to YES then doxygen will generate a graph for
# groups, showing the direct groups dependencies.
# The default value is: YES.
# This tag requires that the tag HAVE_DOT is set to YES.

GROUP_GRAPHS           = YES

# If the UML_LOOK tag is set to YES, doxygen will generate inheritance and
# collaboration diagrams in a style similar to the OMG's Unified Modeling
# Language.
# The default value is: NO.
# This tag requires that the tag HAVE_DOT is set to YES.

UML_LOOK               = NO

# If the UML_LOOK tag is enabled, the fields and methods are shown inside the
# class node. If there are many fields or methods and many nodes the graph may
# become too big to be useful. The UML_LIMIT_NUM_FIELDS threshold limits the
# number of items for each type to make the size more manageable. Set this to 0
# for no limit. Note that the threshold may be exceeded by 50% before the limit
# is enforced. So when you set the threshold to 10, up to 15 fields may appear,
# but if the number exceeds 15, the total amount of fields shown is limited to
# 10.
# Minimum value: 0, maximum value: 100, default value: 10.
# This tag requires that the tag HAVE_DOT is set to YES.

UML_LIMIT_NUM_FIELDS   = 10

# If the TEMPLATE_RELATIONS tag is set to YES then the inheritance and
# collaboration graphs will show the relations between templates and their
# instances.
# The default value is: NO.
# This tag requires that the tag HAVE_DOT is set to YES.

TEMPLATE_RELATIONS     = NO

# If the INCLUDE_GRAPH, ENABLE_PREPROCESSING and SEARCH_INCLUDES tags are set to
# YES then doxygen will generate a graph for each documented file showing the
# direct and indirect include dependencies of the file with other documented
# files.
# The default value is: YES.
# This tag requires that the tag HAVE_DOT is set to YES.

INCLUDE_GRAPH          = YES

# If the INCLUDED_BY_GRAPH, ENABLE_PREPROCESSING and SEARCH_INCLUDES tags are
# set to YES then doxygen will generate a graph for each documented file showing
# the direct and indirect include dependencies of the file with other documented
# files.
# The default value is: YES.
# This tag requires that the tag HAVE_DOT is set to YES.

INCLUDED_BY_GRAPH      = YES

# If the CALL_GRAPH tag is set to YES then doxygen will generate a call
# dependency graph for every global function or class method.
#
# Note that enabling this option will significantly increase the time of a run.
# So in most cases it will be better to enable call graphs for selected
# functions only using the \callgraph command. Disabling a call graph can be
# accomplished by means of the command \hidecallgraph.
# The default value is: NO.
# This tag requires that the tag HAVE_DOT is set to YES.

CALL_GRAPH             = NO

# If the CALLER_GRAPH tag is set to YES then doxygen will generate a caller
# dependency graph for every global function or class method.
#
# Note that enabling this option will significantly increase the time of a run.
# So in most cases it will be better to enable caller graphs for selected
# functions only using the \callergraph command. Disabling a caller graph can be
# accomplished by means of the command \hidecallergraph.
# The default value is: NO.
# This tag requires that the tag HAVE_DOT is set to YES.

CALLER_GRAPH           = NO

# If the GRAPHICAL_HIERARCHY tag is set to YES then doxygen will graphical
# hierarchy of all classes instead of a textual one.
# The default value is: YES.
# This tag requires that the tag HAVE_DOT is set to YES.

GRAPHICAL_HIERARCHY    = YES

# If the DIRECTORY_GRAPH tag is set to YES then doxygen will show the
# dependencies a directory has on other directories in a graphical way. The
# dependency relations are determined by the #include relations between the
# files in the directories.
# The default value is: YES.
# This tag requires that the tag HAVE_DOT is set to YES.

DIRECTORY_GRAPH        = YES

# The DOT_IMAGE_FORMAT tag can be used to set the image format of the images
# generated by dot. For an explanation of the image formats see the section
# output formats in the documentation of the dot tool (Graphviz (see:
# http://www.graphviz.org/)).
# Note: If you choose svg you need to set HTML_FILE_EXTENSION to xhtml in order
# to make the SVG files visible in IE 9+ (other browsers do not have this
# requirement).
# Possible values are: png, jpg, gif, svg, png:gd, png:gd:gd, png:cairo,
# png:cairo:gd, png:cairo:cairo, png:cairo:gdiplus, png:gdiplus and
# png:gdiplus:gdiplus.
# The default value is: png.
# This tag requires that the tag HAVE_DOT is set to YES.

DOT_IMAGE_FORMAT       = svg

# If DOT_IMAGE_FORMAT is set to svg, then this option can be set to YES to
# enable generation of interactive SVG images that allow zooming and panning.
#
# Note that this requires a modern browser other than Internet Explorer. Tested
# and working are Firefox, Chrome, Safari, and Opera.
# Note: For IE 9+ you need to set HTML_FILE_EXTENSION to xhtml in order to make
# the SVG files visible. Older versions of IE do not have SVG support.
# The default value is: NO.
# This tag requires that the tag HAVE_DOT is set to YES.

INTERACTIVE_SVG        = NO

# The DOT_PATH tag can be used to specify the path where the dot tool can be
# found. If left blank, it is assumed the dot tool can be found in the path.
# This tag requires that the tag HAVE_DOT is set to YES.

DOT_PATH               = 

# The DOTFILE_DIRS tag can be used to specify one or more directories that
# contain dot files that are included in the documentation (see the \dotfile
# command).
# This tag requires that the tag HAVE_DOT is set to YES.

DOTFILE_DIRS           = 

# The MSCFILE_DIRS tag can be used to specify one or more directories that
# contain msc files that are included in the documentation (see the \mscfile
# command).

MSCFILE_DIRS           = 

# The DIAFILE_DIRS tag can be used to specify one or more directories that
# contain dia files that are included in the documentation (see the \diafile
# command).

DIAFILE_DIRS           = 

# When using plantuml, the PLANTUML_JAR_PATH tag should be used to specify the
# path where java can find the plantuml.jar file. If left blank, it is assumed
# PlantUML is not used or called during a preprocessing step. Doxygen will
# generate a warning when it encounters a \startuml command in this case and
# will not generate output for the diagram.

PLANTUML_JAR_PATH      = 

# When using plantuml, the specified paths are searched for files specified by
# the !include statement in a plantuml block.

PLANTUML_INCLUDE_PATH  = 

# The DOT_GRAPH_MAX_NODES tag can be used to set the maximum number of nodes
# that will be shown in the graph. If the number of nodes in a graph becomes
# larger than this value, doxygen will truncate the graph, which is visualized
# by representing a node as a red box. Note that doxygen if the number of direct
# children of the root node in a graph is already larger than
# DOT_GRAPH_MAX_NODES then the graph will not be shown at all. Also note that
# the size of a graph can be further restricted by MAX_DOT_GRAPH_DEPTH.
# Minimum value: 0, maximum value: 10000, default value: 50.
# This tag requires that the tag HAVE_DOT is set to YES.

DOT_GRAPH_MAX_NODES    = 50

# The MAX_DOT_GRAPH_DEPTH tag can be used to set the maximum depth of the graphs
# generated by dot. A depth value of 3 means that only nodes reachable from the
# root by following a path via at most 3 edges will be shown. Nodes that lay
# further from the root node will be omitted. Note that setting this option to 1
# or 2 may greatly reduce the computation time needed for large code bases. Also
# note that the size of a graph can be further restricted by
# DOT_GRAPH_MAX_NODES. Using a depth of 0 means no depth restriction.
# Minimum value: 0, maximum value: 1000, default value: 0.
# This tag requires that the tag HAVE_DOT is set to YES.

MAX_DOT_GRAPH_DEPTH    = 0

# Set the DOT_TRANSPARENT tag to YES to generate images with a transparent
# background. This is disabled by default, because dot on Windows does not seem
# to support this out of the box.
#
# Warning: Depending on the platform used, enabling this option may lead to
# badly anti-aliased labels on the edges of a graph (i.e. they become hard to
# read).
# The default value is: NO.
# This tag requires that the tag HAVE_DOT is set to YES.

DOT_TRANSPARENT        = NO

# Set the DOT_MULTI_TARGETS tag to YES to allow dot to generate multiple output
# files in one run (i.e. multiple -o and -T options on the command line). This
# makes dot run faster, but since only newer versions of dot (>1.8.10) support
# this, this feature is disabled by default.
# The default value is: NO.
# This tag requires that the tag HAVE_DOT is set to YES.

DOT_MULTI_TARGETS      = NO

# If the GENERATE_LEGEND tag is set to YES doxygen will generate a legend page
# explaining the meaning of the various boxes and arrows in the dot generated
# graphs.
# The default value is: YES.
# This tag requires that the tag HAVE_DOT is set to YES.

GENERATE_LEGEND        = YES

# If the DOT_CLEANUP tag is set to YES, doxygen will remove the intermediate dot
# files that are used to generate the various graphs.
# The default value is: YES.
# This tag requires that the tag HAVE_DOT is set to YES.

DOT_CLEANUP            = YES


File: /src\Libs\pear2\vendor\pear2\cache_shm\docs\phpdoc.dist.xml
<?xml version="1.0" encoding="UTF-8"?>
<phpdoc>
    <title>PEAR2_Cache_SHM documentation</title>
    <parser>
        <default-package-name>PEAR2_Cache_SHM</default-package-name>
        <target>Reference/PhpDocumentor/Cache</target>
        <extensions>
            <extension>php</extension>
        </extensions>
    </parser>
    <files>
        <directory>../src/PEAR2/Cache/SHM</directory>
        <file>../src/PEAR2/Cache/SHM.php</file>
    </files>
    <transformer>
        <target>Reference/PhpDocumentor/Doc</target>
    </transformer>
</phpdoc>

File: /src\Libs\pear2\vendor\pear2\cache_shm\extrasetup.php
<?php

/**
 * extrasetup.php for PEAR2_Cache_SHM.
 * 
 * PHP version 5.3
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */

$packages = array(
    'pear2.php.net' => array(
        'PEAR2_Autoload'
    )
);

$extrafiles = array();
$config = Pyrus\Config::current();
$registry = $config->registry;
$phpDir = $config->php_dir;

foreach ($packages as $channel => $channelPackages) {
    foreach ($channelPackages as $package) {
        foreach ($registry->toPackage($package, $channel)->installcontents
            as $file => $info) {
            if (strpos($file, 'php/') === 0 || strpos($file, 'src/') === 0) {
                $filename = substr($file, 4);
                $extrafiles['src/' . $filename]
                    = realpath($phpDir . DIRECTORY_SEPARATOR . $filename);
            }
        }
    }
}


File: /src\Libs\pear2\vendor\pear2\cache_shm\package.xml
<?xml version="1.0" encoding="UTF-8"?>
<package version="2.1" xmlns="http://pear.php.net/dtd/package-2.1" xmlns:tasks="http://pear.php.net/dtd/tasks-1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://pear.php.net/dtd/tasks-1.0     http://pear.php.net/dtd/tasks-1.0.xsd     http://pear.php.net/dtd/package-2.1     http://pear.php.net/dtd/package-2.1.xsd">
 <name>PEAR2_Cache_SHM</name>
 <channel>pear2.php.net</channel>
 <summary>Wrapper for shared memory and locking functionality across different extensions.
</summary>
 <description>Allows you to share data across requests as long as the PHP process is running. One of APC or WinCache is required to accomplish this, with other extensions being potentially pluggable as adapters.</description>
 <lead>
  <name>Vasil Rangelov</name>
  <user>boen_robot</user>
  <email>boen.robot@gmail.com</email>
  <active>yes</active>
 </lead>
 <date>2016-11-07</date>
 <time>02:54:44</time>
 <version>
  <release>0.2.0</release>
  <api>0.1.0</api>
 </version>
 <stability>
  <release>alpha</release>
  <api>alpha</api>
 </stability>
 <license uri="http://www.gnu.org/copyleft/lesser.html">LGPL License 2.1</license>
 <notes>* __Added APCu adapter__
* Version requirements bumped to ones that reflect fully available functionality. More specifically:
    - APC 3.1.1 is now the required minimum (previously, 3.0.13), because it's the minimum for APCIterator.
    - APCu 5.0.0 is required, because of APCUIterator, though 4.0.0 would be sufficient for the rest.
    - PHP 5.3.9 is the minimum required PHP version, because it is the firt one in which a critical bug affecting this package is fixed. See [#43200](https://bugs.php.net/bug.php?id=43200) for details.
* Doc and CS fixes.</notes>
 <contents>
  <dir name="/">
   <dir name="docs" baseinstalldir="/">
    <file role="doc" name="apigen.neon">
     <tasks:replace type="pear-config" to="php_dir" from="../src"/>
    </file>
    <file role="doc" name="doxygen.ini">
     <tasks:replace type="pear-config" to="php_dir" from="../src"/>
     <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
    </file>
    <file role="doc" name="phpdoc.dist.xml">
     <tasks:replace type="pear-config" to="php_dir" from="../src"/>
    </file>
   </dir>
   <dir name="src" baseinstalldir="/">
    <dir name="PEAR2">
     <dir name="Cache">
      <dir name="SHM">
       <dir name="Adapter">
        <file role="php" name="APC.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
         <tasks:replace type="package-info" to="summary" from="~~summary~~"/>
         <tasks:replace type="package-info" to="description" from="~~description~~"/>
        </file>
        <file role="php" name="APCu.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
         <tasks:replace type="package-info" to="summary" from="~~summary~~"/>
         <tasks:replace type="package-info" to="description" from="~~description~~"/>
        </file>
        <file role="php" name="Placebo.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
         <tasks:replace type="package-info" to="summary" from="~~summary~~"/>
         <tasks:replace type="package-info" to="description" from="~~description~~"/>
        </file>
        <file role="php" name="Wincache.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
         <tasks:replace type="package-info" to="summary" from="~~summary~~"/>
         <tasks:replace type="package-info" to="description" from="~~description~~"/>
        </file>
       </dir>
       <file role="php" name="Exception.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        <tasks:replace type="package-info" to="summary" from="~~summary~~"/>
        <tasks:replace type="package-info" to="description" from="~~description~~"/>
       </file>
       <file role="php" name="InvalidArgumentException.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        <tasks:replace type="package-info" to="summary" from="~~summary~~"/>
        <tasks:replace type="package-info" to="description" from="~~description~~"/>
       </file>
      </dir>
      <file role="php" name="SHM.php">
       <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       <tasks:replace type="package-info" to="summary" from="~~summary~~"/>
       <tasks:replace type="package-info" to="description" from="~~description~~"/>
      </file>
     </dir>
    </dir>
   </dir>
   <dir name="tests" baseinstalldir="/">
    <dir name="PHPT">
     <dir name="Common">
      <file role="test" name="testAddingTtlValue_part1.phpt"/>
      <file role="test" name="testAddingTtlValue_part2.phpt"/>
      <file role="test" name="testAddingTtlValue_part3.phpt"/>
      <file role="test" name="testAddingValue.phpt"/>
      <file role="test" name="testSettingAndDeletingValue.phpt"/>
      <file role="test" name="testSettingAndGettingValue.phpt"/>
      <file role="test" name="testSingleFileLockAndUnlock.phpt"/>
     </dir>
     <dir name="includes">
      <file role="test" name="runner.php">
       <tasks:replace type="pear-config" to="php_dir" from="../src"/>
      </file>
      <file role="test" name="SHM-factory.php"/>
     </dir>
     <file role="test" name="APC.phpt"/>
     <file role="test" name="APCu.phpt"/>
     <file role="test" name="Placebo.phpt"/>
     <file role="test" name="SHM-factory_CGI.phpt"/>
     <file role="test" name="SHM-factory_CLI.phpt"/>
     <file role="test" name="Wincache.phpt"/>
    </dir>
    <file role="test" name="bootstrap.php">
     <tasks:replace type="pear-config" to="php_dir" from="../src"/>
    </file>
    <file role="test" name="phpunit.xml">
     <tasks:replace type="pear-config" to="php_dir" from="../src"/>
    </file>
   </dir>
  </dir>
 </contents>
 <dependencies>
  <required>
   <php>
    <min>5.3.9</min>
   </php>
   <pearinstaller>
    <min>1.4.0</min>
   </pearinstaller>
  </required>
  <optional>
   <package>
    <name>PEAR2_Autoload</name>
    <channel>pear2.php.net</channel>
    <min>0.3.0</min>
   </package>
   <extension>
    <name>apc</name>
    <min>3.1.1</min>
   </extension>
   <extension>
    <name>apcu</name>
    <min>5.0.0</min>
   </extension>
   <extension>
    <name>wincache</name>
    <min>1.1.0</min>
   </extension>
  </optional>
 </dependencies>
 <phprelease>
  <filelist>
   <install name="docs/apigen.neon" as="apigen.neon"/>
   <install name="docs/doxygen.ini" as="doxygen.ini"/>
   <install name="docs/phpdoc.dist.xml" as="phpdoc.dist.xml"/>
   <install name="src/PEAR2/Cache/SHM.php" as="PEAR2/Cache/SHM.php"/>
   <install name="src/PEAR2/Cache/SHM/Adapter/APC.php" as="PEAR2/Cache/SHM/Adapter/APC.php"/>
   <install name="src/PEAR2/Cache/SHM/Adapter/APCu.php" as="PEAR2/Cache/SHM/Adapter/APCu.php"/>
   <install name="src/PEAR2/Cache/SHM/Adapter/Placebo.php" as="PEAR2/Cache/SHM/Adapter/Placebo.php"/>
   <install name="src/PEAR2/Cache/SHM/Adapter/Wincache.php" as="PEAR2/Cache/SHM/Adapter/Wincache.php"/>
   <install name="src/PEAR2/Cache/SHM/Exception.php" as="PEAR2/Cache/SHM/Exception.php"/>
   <install name="src/PEAR2/Cache/SHM/InvalidArgumentException.php" as="PEAR2/Cache/SHM/InvalidArgumentException.php"/>
   <install name="tests/bootstrap.php" as="bootstrap.php"/>
   <install name="tests/PHPT/APC.phpt" as="PHPT/APC.phpt"/>
   <install name="tests/PHPT/APCu.phpt" as="PHPT/APCu.phpt"/>
   <install name="tests/PHPT/Common/testAddingTtlValue_part1.phpt" as="PHPT/Common/testAddingTtlValue_part1.phpt"/>
   <install name="tests/PHPT/Common/testAddingTtlValue_part2.phpt" as="PHPT/Common/testAddingTtlValue_part2.phpt"/>
   <install name="tests/PHPT/Common/testAddingTtlValue_part3.phpt" as="PHPT/Common/testAddingTtlValue_part3.phpt"/>
   <install name="tests/PHPT/Common/testAddingValue.phpt" as="PHPT/Common/testAddingValue.phpt"/>
   <install name="tests/PHPT/Common/testSettingAndDeletingValue.phpt" as="PHPT/Common/testSettingAndDeletingValue.phpt"/>
   <install name="tests/PHPT/Common/testSettingAndGettingValue.phpt" as="PHPT/Common/testSettingAndGettingValue.phpt"/>
   <install name="tests/PHPT/Common/testSingleFileLockAndUnlock.phpt" as="PHPT/Common/testSingleFileLockAndUnlock.phpt"/>
   <install name="tests/PHPT/includes/runner.php" as="PHPT/includes/runner.php"/>
   <install name="tests/PHPT/includes/SHM-factory.php" as="PHPT/includes/SHM-factory.php"/>
   <install name="tests/PHPT/Placebo.phpt" as="PHPT/Placebo.phpt"/>
   <install name="tests/PHPT/SHM-factory_CGI.phpt" as="PHPT/SHM-factory_CGI.phpt"/>
   <install name="tests/PHPT/SHM-factory_CLI.phpt" as="PHPT/SHM-factory_CLI.phpt"/>
   <install name="tests/PHPT/Wincache.phpt" as="PHPT/Wincache.phpt"/>
   <install name="tests/phpunit.xml" as="phpunit.xml"/>
  </filelist>
 </phprelease>
</package>


File: /src\Libs\pear2\vendor\pear2\cache_shm\packagexmlsetup.php
<?php

/**
 * packagexmlsetup.php for PEAR2_Cache_SHM.
 * 
 * PHP version 5.3
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */

/**
 * References the package in $package and/or $compatible.
 */
use Pyrus\Developer\PackageFile\v2;

/**
 * Configuration array.
 * 
 * Each key is the task.
 * 
 * The task "replace" uses an array where the key is the value to be searched
 * for, and the value is an array of additional attributes for the task, which
 * normally contain at least "type" (pear-config/package-info) and "to", which
 * specifies the value to replace it with.
 * 
 * The task "eol" uses an array where the key is a filename pattern to be
 * matched, and the value is the target platform's EOL to be used for those
 * file names (windows/unix).
 * 
 * Unrecognized tasks are ignored.
 * 
 * @var array
 */
$config = array(
    'replace' => array(
        '../src' => array(
            'type' => 'pear-config',
            'to' => 'php_dir'
        ),
        'GIT: $Id$' => array(
            'type' => 'package-info',
            'to' => 'version'
        ),
        '~~summary~~' => array(
            'type' => 'package-info',
            'to' => 'summary'
        ),
        '~~description~~' => array(
            'type' => 'package-info',
            'to' => 'description'
        )
    ),
    'eol' => array(
        '*.bat' => 'windows'
    )
);

if (!isset($package)) {
    die('This file must be executed via "pyrus.phar make".');
}

$packageGen = function (
    array $config,
    v2 $package,
    v2 $compatible = null
) {

    $tasksNs = $package->getTasksNs();
    $cTasksNs = $compatible ? $compatible->getTasksNs() : '';

    $oldCwd = getcwd();
    chdir(__DIR__);
    foreach (new RecursiveIteratorIterator(
        new RecursiveDirectoryIterator(
            '.',
            RecursiveDirectoryIterator::UNIX_PATHS
            | RecursiveDirectoryIterator::SKIP_DOTS
        ),
        RecursiveIteratorIterator::LEAVES_ONLY
    ) as $path) {
            $filename = substr($path->getPathname(), 2);
            $cFilename = str_replace('src/', 'php/', $filename);

        if (isset($package->files[$filename])) {
            $parsedFilename = pathinfo($filename);
            $as = (strpos($filename, 'examples/') === 0)
                ? $filename
                : substr($filename, strpos($filename, '/') + 1);
            if (strpos($filename, 'scripts/') === 0) {
                if (isset($parsedFilename['extension'])
                    && 'php' === $parsedFilename['extension']
                    && !is_file(
                        $parsedFilename['dirname'] . '/' .
                        $parsedFilename['filename']
                    )
                    && is_file(
                        $parsedFilename['dirname'] . '/' .
                        $parsedFilename['filename'] . '.bat'
                    )
                ) {
                    $as = substr($as, 0, -4);
                }
            }
            $package->getReleaseToInstall('php')->installAs($filename, $as);

            $contents = file_get_contents($filename);
            foreach ($config['replace'] as $from => $attribs) {
                if (strpos($contents, $from) !== false) {
                    $attribs['from'] = $from;
                    $package->files[$filename] = array_merge_recursive(
                        $package->files[$filename]->getArrayCopy(),
                        array(
                            "{$tasksNs}:replace" => array(
                                array(
                                    'attribs' => $attribs
                                )
                            )
                        )
                    );

                    if ($compatible) {
                        $compatible->files[$cFilename] = array_merge_recursive(
                            $compatible->files[$cFilename]->getArrayCopy(),
                            array(
                                "{$cTasksNs}:replace" => array(
                                    array(
                                        'attribs' => $attribs
                                    )
                                )
                            )
                        );
                    }
                }
            }

            foreach ($config['eol'] as $pattern => $platform) {
                if (fnmatch($pattern, $filename)) {
                    $package->files[$filename] = array_merge_recursive(
                        $package->files[$filename]->getArrayCopy(),
                        array(
                            "{$tasksNs}:{$platform}eol" => array()
                        )
                    );

                    if ($compatible) {
                        $compatible->files[$cFilename] = array_merge_recursive(
                            $compatible->files[$cFilename]->getArrayCopy(),
                            array(
                                "{$cTasksNs}:{$platform}eol" => array()
                            )
                        );
                    }
                }
            }
        }
    }
    chdir($oldCwd);
    return array($package, $compatible);
};

list($package, $compatible) = $packageGen(
    $config,
    $package,
    isset($compatible) ? $compatible : null
);
if (null === $compatible) {
    unset($compatible);
}


File: /src\Libs\pear2\vendor\pear2\cache_shm\README
Wrapper for shared memory and locking functionality across different extensions.
Allows you to share data across requests as long as the PHP process is running. One of APC or WinCache is required to accomplish this, with other extensions being potentially pluggable as adapters.

File: /src\Libs\pear2\vendor\pear2\cache_shm\README.md
See the project wiki for installation instructions and other documentation.

The sources as visible here reflect the development version. They may contain parsing errors, fail to install or have all other sorts of errors. If you want to use this package, download the packaged archives instead.

File: /src\Libs\pear2\vendor\pear2\cache_shm\RELEASE-0.1.0
First PEAR2 compatible release.

File: /src\Libs\pear2\vendor\pear2\cache_shm\RELEASE-0.1.1
* Fixed the PHAR stub.
* Removed the warnings APC would trigger when using SHM::factory().
* Allowed registering of external adapters with the new SHM::registerAdapter() method.
* Added SHM::__invoke() as a shortcut to SHM::add().

File: /src\Libs\pear2\vendor\pear2\cache_shm\RELEASE-0.1.2
* SHM::isMeetingRequirements() is now not abstract, and always returns TRUE.
* Fixed loading order of adapters.
* Changed the PHAR stub to not fail when reading the hash fails.
* Doc and CS fixes.

File: /src\Libs\pear2\vendor\pear2\cache_shm\RELEASE-0.1.3
* Wincache and APC now check their requirements in greater detail:
    - APC checks if it's enabled by the apc.enabled INI setting.
    - Wincache checks if the user cache is enabled by wincache.ucenabled INI setting.
    - Both check if the SAPI is CLI, and if so, whether that's allowed by the respective ini setting.
* The PHAR stub also checks and reports the above.
* SHM::getIterator() now returns ArrayObject instead of a normal array, in order to be compatible with how IteratorAggregate actually works.
* Doc and CS fixes.

File: /src\Libs\pear2\vendor\pear2\cache_shm\RELEASE-0.2.0
* __Added APCu adapter__
* Version requirements bumped to ones that reflect fully available functionality. More specifically:
    - APC 3.1.1 is now the required minimum (previously, 3.0.13), because it's the minimum for APCIterator.
    - APCu 5.0.0 is required, because of APCUIterator, though 4.0.0 would be sufficient for the rest.
    - PHP 5.3.9 is the minimum required PHP version, because it is the firt one in which a critical bug affecting this package is fixed. See [#43200](https://bugs.php.net/bug.php?id=43200) for details.
* Doc and CS fixes.

File: /src\Libs\pear2\vendor\pear2\cache_shm\src\PEAR2\Cache\SHM\Adapter\APC.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM\Adapter;

/**
 * Throws exceptions from this namespace, and extends from this class.
 */
use PEAR2\Cache\SHM;

/**
 * {@link APC::getIterator()} returns this object.
 */
use ArrayObject;

/**
 * Shared memory adapter for the APC extension.
 *
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class APC extends SHM
{
    /**
     * ID of the current storage.
     *
     * @var string
     */
    protected $persistentId;

    /**
     * List of persistent IDs.
     *
     * A list of persistent IDs within the current request (as keys) with an int
     * (as a value) specifying the number of instances in the current request.
     * Used as an attempt to ensure implicit lock releases even on errors in the
     * critical sections, since APC doesn't have an actual locking function.
     *
     * @var array
     */
    protected static $requestInstances = array();

    /**
     * Array of lock names for each persistent ID.
     *
     * Array of lock names (as values) for each persistent ID (as key) obtained
     * during the current request.
     *
     * @var array
     */
    protected static $locksBackup = array();

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage.
     *
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    public function __construct($persistentId)
    {
        $this->persistentId = __CLASS__ . ' ' . $persistentId;
        if (isset(static::$requestInstances[$this->persistentId])) {
            static::$requestInstances[$this->persistentId]++;
        } else {
            static::$requestInstances[$this->persistentId] = 1;
            static::$locksBackup[$this->persistentId] = array();
        }
        register_shutdown_function(
            get_called_class() . '::releaseLocks',
            $this->persistentId,
            true
        );
    }

    /**
     * Checks if the adapter meets its requirements.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return extension_loaded('apc')
            && version_compare(phpversion('apc'), '3.1.1', '>=')
            && ini_get('apc.enabled')
            && ('cli' !== PHP_SAPI || ini_get('apc.enable_cli'));
    }

    /**
     * Releases all locks in a storage.
     *
     * This function is not meant to be used directly. It is implicitly called
     * by the the destructor and as a shutdown function when the request ends.
     * One of these calls ends up releasing any unreleased locks obtained
     * during the request. A lock is also implicitly released as soon as there
     * are no objects left in the current request using the same persistent ID.
     *
     * @param string $internalPersistentId The internal persistent ID, the locks
     *     of which are being released.
     * @param bool   $isAtShutdown         Whether the function was executed at
     *     shutdown.
     *
     * @return void
     *
     * @internal
     */
    public static function releaseLocks($internalPersistentId, $isAtShutdown)
    {
        $hasInstances = 0 !== static::$requestInstances[$internalPersistentId];
        if ($isAtShutdown === $hasInstances) {
            foreach (static::$locksBackup[$internalPersistentId] as $key) {
                apc_delete($internalPersistentId . 'l ' . $key);
            }
        }
    }

    /**
     * Releases any locks obtained by this instance as soon as there are no more
     * references to the object's persistent ID.
     */
    public function __destruct()
    {
        static::$requestInstances[$this->persistentId]--;
        static::releaseLocks($this->persistentId, false);
    }


    /**
     * Obtains a named lock.
     *
     * @param string $key     Name of the key to obtain. Note that $key may
     *     repeat for each distinct $persistentId.
     * @param double $timeout If the lock can't be immediately obtained, the
     *     script will block for at most the specified amount of seconds.
     *     Setting this to 0 makes lock obtaining non blocking, and setting it
     *     to NULL makes it block without a time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function lock($key, $timeout = null)
    {
        $lock = $this->persistentId . 'l ' . $key;
        $hasTimeout = $timeout !== null;
        $start = microtime(true);
        while (!apc_add($lock, 1)) {
            if ($hasTimeout && (microtime(true) - $start) > $timeout) {
                return false;
            }
        }
        static::$locksBackup[$this->persistentId] = $key;
        return true;
    }

    /**
     * Releases a named lock.
     *
     * @param string $key Name of the key to release. Note that $key may
     *     repeat for each distinct $persistentId.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function unlock($key)
    {
        $lock = $this->persistentId . 'l ' . $key;
        $success = apc_delete($lock);
        if ($success) {
            unset(
                static::$locksBackup[$this->persistentId][array_search(
                    $key,
                    static::$locksBackup[$this->persistentId],
                    true
                )]
            );
            return true;
        }
        return false;
    }

    /**
     * Checks if a specified key is in the storage.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    public function exists($key)
    {
        return apc_exists($this->persistentId . 'd ' . $key);
    }

    /**
     * Adds a value to the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function add($key, $value, $ttl = 0)
    {
        return apc_add($this->persistentId . 'd ' . $key, $value, $ttl);
    }

    /**
     * Sets a value in the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function set($key, $value, $ttl = 0)
    {
        return apc_store($this->persistentId . 'd ' . $key, $value, $ttl);
    }

    /**
     * Gets a value from the shared memory storage.
     *
     * Gets the current value, or throws an exception if it's not stored.
     *
     * @param string $key Name of key to get the value of.
     *
     * @return mixed The current value of the specified key.
     */
    public function get($key)
    {
        $fullKey = $this->persistentId . 'd ' . $key;
        if (apc_exists($fullKey)) {
            $value = apc_fetch($fullKey, $success);
            if (!$success) {
                throw new SHM\InvalidArgumentException(
                    'Unable to fetch key. ' .
                    'Key has either just now expired or (if no TTL was set) ' .
                    'is possibly in a race condition with another request.',
                    100
                );
            }
            return $value;
        }
        throw new SHM\InvalidArgumentException('No such key in cache', 101);
    }

    /**
     * Deletes a value from the shared memory storage.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function delete($key)
    {
        return apc_delete($this->persistentId . 'd ' . $key);
    }

    /**
     * Increases a value from the shared memory storage.
     *
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     *
     * @return int The new value.
     */
    public function inc($key, $step = 1)
    {
        $newValue = apc_inc(
            $this->persistentId . 'd ' . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                102
            );
        }
        return $newValue;
    }

    /**
     * Decreases a value from the shared memory storage.
     *
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     *
     * @return int The new value.
     */
    public function dec($key, $step = 1)
    {
        $newValue = apc_dec(
            $this->persistentId . 'd ' . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to decrease the value. Are you sure the value is int?',
                103
            );
        }
        return $newValue;
    }

    /**
     * Sets a new value if a key has a certain value.
     *
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     *
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function cas($key, $old, $new)
    {
        return apc_cas($this->persistentId . 'd ' . $key, $old, $new);
    }

    /**
     * Clears the persistent storage.
     *
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     *
     * @return void
     */
    public function clear()
    {
        foreach (new APCIterator(
            'user',
            '/^' . preg_quote($this->persistentId, '/') . 'd /',
            APC_ITER_KEY,
            100,
            APC_LIST_ACTIVE
        ) as $key) {
            apc_delete($key);
        }
    }

    /**
     * Retrieve an external iterator
     *
     * Returns an external iterator.
     *
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     *
     * @return ArrayObject An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    public function getIterator($filter = null, $keysOnly = false)
    {
        $result = array();
        foreach (new APCIterator(
            'user',
            '/^' . preg_quote($this->persistentId, '/') . 'd /',
            APC_ITER_KEY,
            100,
            APC_LIST_ACTIVE
        ) as $key) {
            $localKey = strstr($key, $this->persistentId . 'd ');
            if (null === $filter || preg_match($filter, $localKey)) {
                if ($keysOnly) {
                    $result[] = $localKey;
                } else {
                    $result[$localKey] = apc_fetch($key);
                }
            }
        }
        return new ArrayObject($result);
    }
}


File: /src\Libs\pear2\vendor\pear2\cache_shm\src\PEAR2\Cache\SHM\Adapter\APCu.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM\Adapter;

/**
 * Throws exceptions from this namespace, and extends from this class.
 */
use PEAR2\Cache\SHM;

/**
 * {@link APC::getIterator()} returns this object.
 */
use ArrayObject;

/**
 * Shared memory adapter for the APC extension.
 *
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class APCu extends SHM
{
    /**
     * ID of the current storage.
     *
     * @var string
     */
    protected $persistentId;

    /**
     * List of persistent IDs.
     *
     * A list of persistent IDs within the current request (as keys) with an int
     * (as a value) specifying the number of instances in the current request.
     * Used as an attempt to ensure implicit lock releases even on errors in the
     * critical sections, since APC doesn't have an actual locking function.
     *
     * @var array
     */
    protected static $requestInstances = array();

    /**
     * Array of lock names for each persistent ID.
     *
     * Array of lock names (as values) for each persistent ID (as key) obtained
     * during the current request.
     *
     * @var array
     */
    protected static $locksBackup = array();

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage.
     *
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    public function __construct($persistentId)
    {
        $this->persistentId = __CLASS__ . ' ' . $persistentId;
        if (isset(static::$requestInstances[$this->persistentId])) {
            static::$requestInstances[$this->persistentId]++;
        } else {
            static::$requestInstances[$this->persistentId] = 1;
            static::$locksBackup[$this->persistentId] = array();
        }
        register_shutdown_function(
            get_called_class() . '::releaseLocks',
            $this->persistentId,
            true
        );
    }

    /**
     * Checks if the adapter meets its requirements.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return extension_loaded('apcu')
            && version_compare(phpversion('apcu'), '5.0.0', '>=')
            && ini_get('apc.enabled')
            && ('cli' !== PHP_SAPI || ini_get('apc.enable_cli'));
    }

    /**
     * Releases all locks in a storage.
     *
     * This function is not meant to be used directly. It is implicitly called
     * by the the destructor and as a shutdown function when the request ends.
     * One of these calls ends up releasing any unreleased locks obtained
     * during the request. A lock is also implicitly released as soon as there
     * are no objects left in the current request using the same persistent ID.
     *
     * @param string $internalPersistentId The internal persistent ID, the locks
     *     of which are being released.
     * @param bool   $isAtShutdown         Whether the function was executed at
     *     shutdown.
     *
     * @return void
     *
     * @internal
     */
    public static function releaseLocks($internalPersistentId, $isAtShutdown)
    {
        $hasInstances = 0 !== static::$requestInstances[$internalPersistentId];
        if ($isAtShutdown === $hasInstances) {
            foreach (static::$locksBackup[$internalPersistentId] as $key) {
                apcu_delete($internalPersistentId . 'l ' . $key);
            }
        }
    }

    /**
     * Releases any locks obtained by this instance as soon as there are no more
     * references to the object's persistent ID.
     */
    public function __destruct()
    {
        static::$requestInstances[$this->persistentId]--;
        static::releaseLocks($this->persistentId, false);
    }


    /**
     * Obtains a named lock.
     *
     * @param string $key     Name of the key to obtain. Note that $key may
     *     repeat for each distinct $persistentId.
     * @param double $timeout If the lock can't be immediately obtained, the
     *     script will block for at most the specified amount of seconds.
     *     Setting this to 0 makes lock obtaining non blocking, and setting it
     *     to NULL makes it block without a time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function lock($key, $timeout = null)
    {
        $lock = $this->persistentId . 'l ' . $key;
        $hasTimeout = $timeout !== null;
        $start = microtime(true);
        while (!apcu_add($lock, 1)) {
            if ($hasTimeout && (microtime(true) - $start) > $timeout) {
                return false;
            }
        }
        static::$locksBackup[$this->persistentId] = $key;
        return true;
    }

    /**
     * Releases a named lock.
     *
     * @param string $key Name of the key to release. Note that $key may
     *     repeat for each distinct $persistentId.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function unlock($key)
    {
        $lock = $this->persistentId . 'l ' . $key;
        $success = apcu_delete($lock);
        if ($success) {
            unset(
                static::$locksBackup[$this->persistentId][array_search(
                    $key,
                    static::$locksBackup[$this->persistentId],
                    true
                )]
            );
            return true;
        }
        return false;
    }

    /**
     * Checks if a specified key is in the storage.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    public function exists($key)
    {
        return apcu_exists($this->persistentId . 'd ' . $key);
    }

    /**
     * Adds a value to the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function add($key, $value, $ttl = 0)
    {
        return apcu_add($this->persistentId . 'd ' . $key, $value, $ttl);
    }

    /**
     * Sets a value in the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function set($key, $value, $ttl = 0)
    {
        return apcu_store($this->persistentId . 'd ' . $key, $value, $ttl);
    }

    /**
     * Gets a value from the shared memory storage.
     *
     * Gets the current value, or throws an exception if it's not stored.
     *
     * @param string $key Name of key to get the value of.
     *
     * @return mixed The current value of the specified key.
     */
    public function get($key)
    {
        $fullKey = $this->persistentId . 'd ' . $key;
        if (apcu_exists($fullKey)) {
            $value = apcu_fetch($fullKey, $success);
            if (!$success) {
                throw new SHM\InvalidArgumentException(
                    'Unable to fetch key. ' .
                    'Key has either just now expired or (if no TTL was set) ' .
                    'is possibly in a race condition with another request.',
                    100
                );
            }
            return $value;
        }
        throw new SHM\InvalidArgumentException('No such key in cache', 101);
    }

    /**
     * Deletes a value from the shared memory storage.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function delete($key)
    {
        return apcu_delete($this->persistentId . 'd ' . $key);
    }

    /**
     * Increases a value from the shared memory storage.
     *
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     *
     * @return int The new value.
     */
    public function inc($key, $step = 1)
    {
        $newValue = apcu_inc(
            $this->persistentId . 'd ' . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                102
            );
        }
        return $newValue;
    }

    /**
     * Decreases a value from the shared memory storage.
     *
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     *
     * @return int The new value.
     */
    public function dec($key, $step = 1)
    {
        $newValue = apcu_dec(
            $this->persistentId . 'd ' . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to decrease the value. Are you sure the value is int?',
                103
            );
        }
        return $newValue;
    }

    /**
     * Sets a new value if a key has a certain value.
     *
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     *
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function cas($key, $old, $new)
    {
        return apcu_cas($this->persistentId . 'd ' . $key, $old, $new);
    }

    /**
     * Clears the persistent storage.
     *
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     *
     * @return void
     */
    public function clear()
    {
        foreach (new APCIterator(
            'user',
            '/^' . preg_quote($this->persistentId, '/') . 'd /',
            APC_ITER_KEY,
            100,
            APC_LIST_ACTIVE
        ) as $key) {
            apcu_delete($key);
        }
    }

    /**
     * Retrieve an external iterator
     *
     * Returns an external iterator.
     *
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     *
     * @return ArrayObject An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    public function getIterator($filter = null, $keysOnly = false)
    {
        $result = array();
        foreach (new APCUIterator(
            '/^' . preg_quote($this->persistentId, '/') . 'd /',
            APC_ITER_KEY,
            100,
            APC_LIST_ACTIVE
        ) as $key) {
            $localKey = strstr($key, $this->persistentId . 'd ');
            if (null === $filter || preg_match($filter, $localKey)) {
                if ($keysOnly) {
                    $result[] = $localKey;
                } else {
                    $result[$localKey] = apcu_fetch($key);
                }
            }
        }
        return new ArrayObject($result);
    }
}


File: /src\Libs\pear2\vendor\pear2\cache_shm\src\PEAR2\Cache\SHM\Adapter\Placebo.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM\Adapter;

/**
 * Throws exceptions from this namespace, and extends from this class.
 */
use PEAR2\Cache\SHM;

/**
 * {@link Placebo::getIterator()} returns this object.
 */
use ArrayObject;

/**
 * This adapter is not truly persistent. It is intended to emulate persistence
 * in non persistent environments, so that upper level applications can use a
 * single code path for persistent and non persistent code.
 *
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class Placebo extends SHM
{
    /**
     * ID of the current storage.
     *
     * @var string
     */
    protected $persistentId;

    /**
     * List of persistent IDs.
     *
     * A list of persistent IDs within the current request (as keys) with an int
     * (as a value) specifying the number of instances in the current request.
     * Used as an attempt to ensure implicit lock releases on destruction.
     *
     * @var array
     */
    protected static $requestInstances = array();

    /**
     * Array of lock names for each persistent ID.
     *
     * Array of lock names (as values) for each persistent ID (as
     *     key) obtained during the current request.
     *
     * @var array
     */
    protected static $locksBackup = array();

    /**
     * The data storage.
     *
     * Each persistent ID is a key, and the value is an array.
     * Each such array has data keys as its keys, and an array as a value.
     * Each such array has as its elements the value, the timeout and the time
     * the data was set.
     *
     * @var array
     */
    protected static $data = array();

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage.
     *
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    public function __construct($persistentId)
    {
        if (isset(static::$requestInstances[$persistentId])) {
            ++static::$requestInstances[$persistentId];
        } else {
            static::$requestInstances[$persistentId] = 1;
            static::$locksBackup[$persistentId] = array();
            static::$data[$persistentId] = array();
        }
        $this->persistentId = $persistentId;
    }

    /**
     * Releases any unreleased locks.
     */
    public function __destruct()
    {
        if (0 === --static::$requestInstances[$this->persistentId]) {
            static::$locksBackup[$this->persistentId] = array();
        }
    }

    /**
     * Checks if the adapter meets its requirements.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return 'cli' === PHP_SAPI;
    }

    /**
     * Pretends to obtain a lock.
     *
     * @param string $key     Ignored.
     * @param double $timeout Ignored.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function lock($key, $timeout = null)
    {
        $key = (string) $key;
        if (in_array($key, static::$locksBackup[$this->persistentId], true)) {
            return false;
        }
        static::$locksBackup[$this->persistentId][] = $key;
        return true;
    }

    /**
     * Pretends to release a lock.
     *
     * @param string $key Ignored
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function unlock($key)
    {
        $key = (string) $key;
        if (!in_array($key, static::$locksBackup[$this->persistentId], true)) {
            return false;
        }
        unset(
            static::$locksBackup[$this->persistentId][array_search(
                $key,
                static::$locksBackup[$this->persistentId],
                true
            )]
        );
        return true;
    }

    /**
     * Checks if a specified key is in the storage.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    public function exists($key)
    {
        return array_key_exists($key, static::$data[$this->persistentId]);
    }

    /**
     * Adds a value to the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Because "true" adapters purge the cache at the next
     *     request, this setting is ignored.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function add($key, $value, $ttl = 0)
    {
        if ($this->exists($key)) {
            return false;
        }
        return $this->set($key, $value, $ttl);
    }

    /**
     * Sets a value in the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Because "true" adapters purge the cache at the next
     *     request, this setting is ignored.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function set($key, $value, $ttl = 0)
    {
        static::$data[$this->persistentId][$key] = $value;
        return true;
    }

    /**
     * Gets a value from the shared memory storage.
     *
     * Gets the current value, or throws an exception if it's not stored.
     *
     * @param string $key Name of key to get the value of.
     *
     * @return mixed The current value of the specified key.
     */
    public function get($key)
    {
        if ($this->exists($key)) {
            return static::$data[$this->persistentId][$key];
        }
        throw new SHM\InvalidArgumentException(
            'Unable to fetch key. No such key.',
            200
        );
    }

    /**
     * Deletes a value from the shared memory storage.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function delete($key)
    {
        if ($this->exists($key)) {
            unset(static::$data[$this->persistentId][$key]);
            return true;
        }
        return false;
    }

    /**
     * Increases a value from the shared memory storage.
     *
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     *
     * @return int The new value.
     */
    public function inc($key, $step = 1)
    {
        if (!$this->exists($key) || !is_int($value = $this->get($key))
            || !$this->set($key, $value + (int) $step)
        ) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                201
            );
        }
        return $this->get($key);
    }

    /**
     * Decreases a value from the shared memory storage.
     *
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     *
     * @return int The new value.
     */
    public function dec($key, $step = 1)
    {
        if (!$this->exists($key) || !is_int($value = $this->get($key))
            || !$this->set($key, $value - (int) $step)
        ) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                202
            );
        }
        return $this->get($key);
    }

    /**
     * Sets a new value if a key has a certain value.
     *
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     *
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function cas($key, $old, $new)
    {
        return $this->exists($key) && ($this->get($key) === $old)
            && is_int($new) && $this->set($key, $new);
    }

    /**
     * Clears the persistent storage.
     *
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     *
     * @return void
     */
    public function clear()
    {
        static::$data[$this->persistentId] = array();
    }

    /**
     * Retrieve an external iterator
     *
     * Returns an external iterator.
     *
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     *
     * @return ArrayObject An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    public function getIterator($filter = null, $keysOnly = false)
    {
        if (null === $filter) {
            return new ArrayObject(
                $keysOnly
                ? array_keys(static::$data[$this->persistentId])
                : static::$data[$this->persistentId]
            );
        }

        $result = array();
        foreach (static::$data[$this->persistentId] as $key => $value) {
            if (preg_match($filter, $key)) {
                $result[$key] = $value;
            }
        }
        return new ArrayObject($keysOnly ? array_keys($result) : $result);
    }
}


File: /src\Libs\pear2\vendor\pear2\cache_shm\src\PEAR2\Cache\SHM\Adapter\Wincache.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM\Adapter;

/**
 * Throws exceptions from this namespace, and extends from this class.
 */
use PEAR2\Cache\SHM;

/**
 * {@link Wincache::getIterator()} returns this object.
 */
use ArrayObject;

/**
 * Shared memory adapter for the WinCache extension.
 *
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class Wincache extends SHM
{
    /**
     * ID of the current storage.
     *
     * @var string
     */
    protected $persistentId;

    /**
     * List of persistent IDs.
     *
     * A list of persistent IDs within the current request (as keys) with an int
     * (as a value) specifying the number of instances in the current request.
     * Used as an attempt to ensure implicit lock releases on destruction.
     *
     * @var array
     */
    protected static $requestInstances = array();

    /**
     * Array of lock names obtained during the current request.
     *
     * @var array
     */
    protected static $locksBackup = array();

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage.
     *
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    public function __construct($persistentId)
    {
        $this->persistentId
            = static::encodeLockName(__CLASS__ . ' ' . $persistentId) . ' ';
        if (isset(static::$requestInstances[$this->persistentId])) {
            static::$requestInstances[$this->persistentId]++;
        } else {
            static::$requestInstances[$this->persistentId] = 1;
            static::$locksBackup[$this->persistentId] = array();
        }
    }

    /**
     * Encodes a lock name
     *
     * Encodes a lock name, so that it can be properly obtained. The scheme used
     * is a subset of URL encoding, with only the "%" and "\" characters being
     * escaped. The encoding itself is necessary, since lock names can't contain
     * the "\" character.
     *
     * @param string $name The lock name to encode.
     *
     * @return string The encoded name.
     *
     * @link http://msdn.microsoft.com/en-us/library/ms682411(VS.85).aspx
     */
    protected static function encodeLockName($name)
    {
        return str_replace(array('%', '\\'), array('%25', '%5C'), $name);
    }

    /**
     * Checks if the adapter meets its requirements.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return extension_loaded('wincache')
            && version_compare(phpversion('wincache'), '1.1.0', '>=')
            && ini_get('wincache.ucenabled')
            && ('cli' !== PHP_SAPI || ini_get('wincache.enablecli'));
    }

    /**
     * Releases any locks obtained by this instance as soon as there are no more
     * references to the object's persistent ID.
     */
    public function __destruct()
    {
        if (0 === --static::$requestInstances[$this->persistentId]) {
            foreach (static::$locksBackup[$this->persistentId] as $key) {
                wincache_unlock(
                    $this->persistentId . static::encodeLockName($key)
                );
            }
        }
    }


    /**
     * Obtains a named lock.
     *
     * @param string $key     Name of the key to obtain. Note that $key may
     *     repeat for each distinct $persistentId.
     * @param double $timeout Ignored with WinCache. Script will always block if
     *     the lock can't be immediately obtained.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function lock($key, $timeout = null)
    {
        $result = wincache_lock(
            $this->persistentId . static::encodeLockName($key)
        );
        if ($result) {
            static::$locksBackup[$this->persistentId] = $key;
        }
        return $result;
    }

    /**
     * Releases a named lock.
     *
     * @param string $key Name of the key to release. Note that $key may
     *     repeat for each distinct $persistentId.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function unlock($key)
    {
        $result = wincache_unlock(
            $this->persistentId . static::encodeLockName($key)
        );
        if ($result) {
            unset(
                static::$locksBackup[$this->persistentId][array_search(
                    $key,
                    static::$locksBackup[$this->persistentId],
                    true
                )]
            );
        }
        return $result;
    }

    /**
     * Checks if a specified key is in the storage.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    public function exists($key)
    {
        return wincache_ucache_exists($this->persistentId . $key);
    }

    /**
     * Adds a value to the shared memory storage.
     *
     * Sets a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function add($key, $value, $ttl = 0)
    {
        return wincache_ucache_add($this->persistentId . $key, $value, $ttl);
    }

    /**
     * Sets a value in the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function set($key, $value, $ttl = 0)
    {
        return wincache_ucache_set($this->persistentId . $key, $value, $ttl);
    }

    /**
     * Gets a value from the shared memory storage.
     *
     * Gets the current value, or throws an exception if it's not stored.
     *
     * @param string $key Name of key to get the value of.
     *
     * @return mixed The current value of the specified key.
     */
    public function get($key)
    {
        $value = wincache_ucache_get($this->persistentId . $key, $success);
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to fetch key. No such key, or key has expired.',
                300
            );
        }
        return $value;
    }

    /**
     * Deletes a value from the shared memory storage.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function delete($key)
    {
        return wincache_ucache_delete($this->persistentId . $key);
    }

    /**
     * Increases a value from the shared memory storage.
     *
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     *
     * @return int The new value.
     */
    public function inc($key, $step = 1)
    {
        $newValue = wincache_ucache_inc(
            $this->persistentId . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                301
            );
        }
        return $newValue;
    }

    /**
     * Decreases a value from the shared memory storage.
     *
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     *
     * @return int The new value.
     */
    public function dec($key, $step = 1)
    {
        $newValue = wincache_ucache_dec(
            $this->persistentId . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to decrease the value. Are you sure the value is int?',
                302
            );
        }
        return $newValue;
    }

    /**
     * Sets a new value if a key has a certain value.
     *
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     *
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function cas($key, $old, $new)
    {
        return wincache_ucache_cas($this->persistentId . $key, $old, $new);
    }

    /**
     * Clears the persistent storage.
     *
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     *
     * @return void
     */
    public function clear()
    {
        $info = wincache_ucache_info();
        foreach ($info['ucache_entries'] as $entry) {
            if (!$entry['is_session']
                && 0 === strpos($entry['key_name'], $this->persistentId)
            ) {
                wincache_ucache_delete($entry['key_name']);
            }
        }
    }

    /**
     * Retrieve an external iterator
     *
     * Returns an external iterator.
     *
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     *
     * @return ArrayObject An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    public function getIterator($filter = null, $keysOnly = false)
    {
        $info = wincache_ucache_info();
        $result = array();
        foreach ($info['ucache_entries'] as $entry) {
            if (!$entry['is_session']
                && 0 === strpos($entry['key_name'], $this->persistentId)
            ) {
                $localKey = strstr($entry['key_name'], $this->persistentId);
                if (null === $filter || preg_match($filter, $localKey)) {
                    if ($keysOnly) {
                        $result[] = $localKey;
                    } else {
                        $result[$localKey] = apc_fetch($localKey);
                    }
                }
            }
        }
        return new ArrayObject($result);
    }
}


File: /src\Libs\pear2\vendor\pear2\cache_shm\src\PEAR2\Cache\SHM\Exception.php
<?php

/**
 * ~~summary~~
 * 
 * ~~description~~
 * 
 * PHP version 5
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM;

/**
 * Generic exception class of this package.
 * 
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
interface Exception
{
}


File: /src\Libs\pear2\vendor\pear2\cache_shm\src\PEAR2\Cache\SHM\InvalidArgumentException.php
<?php

/**
 * ~~summary~~
 * 
 * ~~description~~
 * 
 * PHP version 5
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM;

/**
 * Exception thrown when there's something wrong with an argument.
 * 
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class InvalidArgumentException extends \InvalidArgumentException
    implements Exception
{
}


File: /src\Libs\pear2\vendor\pear2\cache_shm\src\PEAR2\Cache\SHM.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */

/**
 * The namespace declaration.
 */
namespace PEAR2\Cache;

/**
 * Used as a catch-all for adapter initialization.
 */
use Exception as E;

/**
 * Implements this class.
 */
use IteratorAggregate;

/**
 * Used on failures by this class.
 */
use PEAR2\Cache\SHM\InvalidArgumentException;

/**
 * Main class for this package.
 *
 * Automatically chooses an adapter based on the available extensions.
 *
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
abstract class SHM implements IteratorAggregate
{
    /**
     * An array of adapter names that meet their requirements.
     *
     * @var array
     */
    private static $_adapters = array();

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage. Adapter is automatically
     * chosen based on the available extensions.
     *
     * @param string $persistentId The ID for the storage.
     *
     * @return static|SHM A new instance of an SHM adapter (child of this
     * class).
     */
    final public static function factory($persistentId)
    {
        foreach (self::$_adapters as $adapter) {
            try {
                return new $adapter($persistentId);
            } catch (E $e) {
                //In case of a runtime error, try to fallback to other adapters.
            }
        }
        throw new InvalidArgumentException(
            'No appropriate adapter available',
            1
        );
    }

    /**
     * Checks if the adapter meets its requirements.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return true;
    }

    /**
     * Registers an adapter.
     *
     * Registers an SHM adapter, allowing you to call it with {@link factory()}.
     *
     * @param string $adapter FQCN of adapter. A valid adapter is one that
     *     extends this class. The class will be autoloaded if not already
     *     present.
     * @param bool   $prepend Whether to prepend this adapter into the list of
     *     possible adapters, instead of appending to it.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    final public static function registerAdapter($adapter, $prepend = false)
    {
        if (class_exists($adapter, true)
            && is_subclass_of($adapter, '\\' . __CLASS__)
            && $adapter::isMeetingRequirements()
        ) {
            if ($prepend) {
                self::$_adapters = array_merge(
                    array($adapter),
                    self::$_adapters
                );
            } else {
                self::$_adapters[] = $adapter;
            }
            return true;
        }
        return false;
    }

    /**
     * Adds a value to the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function __invoke($key, $value, $ttl = 0)
    {
        return $this->add($key, $value, $ttl);
    }

    /**
     * Gets a value from the shared memory storage.
     *
     * This is a magic method, thanks to which any property you attempt to get
     * the value of will be fetched from the adapter, treating the property name
     * as the key of the value to get.
     *
     * @param string $key Name of key to get.
     *
     * @return mixed The current value of the specified key.
     */
    public function __get($key)
    {
        return $this->get($key);
    }

    /**
     * Sets a value in the shared memory storage.
     *
     * This is a magic method, thanks to which any property you attempt to set
     * the value of will be set by the adapter, treating the property name as
     * the key of the value to set. The value is set without a TTL.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function __set($key, $value)
    {
        return $this->set($key, $value);
    }

    /**
     * Checks if a specified key is in the storage.
     *
     * This is a magic method, thanks to which any property you call isset() on
     * will be checked by the adapter, treating the property name as the key
     * of the value to check.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    public function __isset($key)
    {
        return $this->exists($key);
    }

    /**
     * Deletes a value from the shared memory storage.
     *
     * This is a magic method, thanks to which any property you attempt to unset
     * the value of will be unset by the adapter, treating the property name as
     * the key of the value to delete.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function __unset($key)
    {
        return $this->delete($key);
    }

    /**
     * Creates a new shared memory storage.
     *
     * Establishes a separate persistent storage.
     *
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    abstract public function __construct($persistentId);

    /**
     * Obtains a named lock.
     *
     * @param string $key     Name of the key to obtain. Note that $key may
     *     repeat for each distinct $persistentId.
     * @param double $timeout If the lock can't be immediately obtained, the
     *     script will block for at most the specified amount of seconds.
     *     Setting this to 0 makes lock obtaining non blocking, and setting it
     *     to NULL makes it block without a time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function lock($key, $timeout = null);

    /**
     * Releases a named lock.
     *
     * @param string $key Name of the key to release. Note that $key may
     *     repeat for each distinct $persistentId.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function unlock($key);

    /**
     * Checks if a specified key is in the storage.
     *
     * @param string $key Name of key to check.
     *
     * @return bool TRUE if the key is in the storage, FALSE otherwise.
     */
    abstract public function exists($key);

    /**
     * Adds a value to the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function add($key, $value, $ttl = 0);

    /**
     * Sets a value in the shared memory storage.
     *
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     *
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function set($key, $value, $ttl = 0);

    /**
     * Gets a value from the shared memory storage.
     *
     * Gets the current value, or throws an exception if it's not stored.
     *
     * @param string $key Name of key to get the value of.
     *
     * @return mixed The current value of the specified key.
     */
    abstract public function get($key);

    /**
     * Deletes a value from the shared memory storage.
     *
     * @param string $key Name of key to delete.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function delete($key);

    /**
     * Increases a value from the shared memory storage.
     *
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     *
     * @return int The new value.
     */
    abstract public function inc($key, $step = 1);

    /**
     * Decreases a value from the shared memory storage.
     *
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     *
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     *
     * @return int The new value.
     */
    abstract public function dec($key, $step = 1);

    /**
     * Sets a new value if a key has a certain value.
     *
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     *
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function cas($key, $old, $new);

    /**
     * Clears the persistent storage.
     *
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     *
     * @return void
     */
    abstract public function clear();

    /**
     * Retrieve an external iterator
     *
     * Returns an external iterator.
     *
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     *
     * @return \Traversable An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    abstract public function getIterator($filter = null, $keysOnly = false);
}

SHM::registerAdapter('\\' . __NAMESPACE__ . '\SHM\Adapter\Placebo');
SHM::registerAdapter('\\' . __NAMESPACE__ . '\SHM\Adapter\Wincache');
SHM::registerAdapter('\\' . __NAMESPACE__ . '\SHM\Adapter\APCu');
SHM::registerAdapter('\\' . __NAMESPACE__ . '\SHM\Adapter\APC');


File: /src\Libs\pear2\vendor\pear2\cache_shm\stub.php
<?php

/**
 * stub for PEAR2_Cache_SHM.
 * 
 * PHP version 5.3
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */

if (count(get_included_files()) > 1) {
    Phar::mapPhar();
    include_once 'phar://' . __FILE__ . DIRECTORY_SEPARATOR .
        '@PACKAGE_NAME@-@PACKAGE_VERSION@' . DIRECTORY_SEPARATOR . 'src'
        . DIRECTORY_SEPARATOR . 'PEAR2' . DIRECTORY_SEPARATOR . 'Autoload.php';
    return;
}

$isHttp = isset($_SERVER['REQUEST_URI']);
if ($isHttp) {
    header('Content-Type: text/plain;charset=UTF-8');
}
echo "@PACKAGE_NAME@ @PACKAGE_VERSION@\n";

if (version_compare(phpversion(), '5.3.0', '<')) {
    echo "\nERROR: This package requires PHP 5.3.0 or later.\n";
    exit(1);
}

$available_extensions = array();
foreach (array('apc', 'apcu', 'wincache') as $ext) {
    if (extension_loaded($ext)) {
        $available_extensions[] = $ext;
    }
}

if (extension_loaded('phar')) {
    try {
        $phar = new Phar(__FILE__);
        $sig = $phar->getSignature();
        echo "{$sig['hash_type']} hash: {$sig['hash']}\n\n";
    } catch (Exception $e) {
        echo <<<HEREDOC

The PHAR extension is available, but was unable to read this PHAR file's hash.

HEREDOC;
        if (false !== strpos($e->getMessage(), 'file extension')) {
            echo <<<HEREDOC
This can happen if you've renamed the file to ".php" instead of ".phar".
Regardless, you should be able to include this file without problems.

HEREDOC;
        }
        echo "\n";
    }
} else {
    echo <<<HEREDOC
WARNING: If you wish to use this package directly from this archive, you need
         to install and enable the PHAR extension. Otherwise, you must instead
         extract this archive, and include the autoloader.

HEREDOC;
}

if (in_array('apc', $available_extensions)) {
    if (version_compare(phpversion('apc'), '3.1.1', '>=')) {
        echo <<<HEREDOC
A compatible APC version is available on this server.
HEREDOC;
        if (ini_get('apc.enabled')) {
            if ($isHttp || ini_get('apc.enable_cli')) {
                echo "You should be able to use it under this SAPI (", PHP_SAPI,
                    ").\n";
            } else {
                echo "\nWARNING: You can't use it under this SAPI (", PHP_SAPI,
                    ").\n";
            }
            echo "\n";
        } else {
            echo <<<HEREDOC
WARNING: Although present, the APC extension is disabled via the apc.enabled
         INI setting, making this package unusable with it.
         You need to enable it from php.ini.

HEREDOC;
        }
    }
}

if (in_array('apcu', $available_extensions)) {
    if (version_compare(phpversion('apcu'), '5.0.0', '>=')) {
        echo <<<HEREDOC
A compatible APCu version is available on this server.
HEREDOC;
        if (ini_get('apc.enabled')) {
            if ($isHttp || ini_get('apc.enable_cli')) {
                echo "You should be able to use it under this SAPI (", PHP_SAPI,
                    ").\n";
            } else {
                echo "\nWARNING: You can't use it under this SAPI (", PHP_SAPI,
                    ").\n";
            }
            echo "\n";
        } else {
            echo <<<HEREDOC
WARNING: Although present, the APCu extension is disabled via the apc.enabled
         INI setting, making this package unusable with it.
         You need to enable it from php.ini.

HEREDOC;
        }
    }
}

if (in_array('wincache', $available_extensions)) {
    if (version_compare(phpversion('wincache'), '1.1.0', '>=')) {
        echo <<<HEREDOC
A compatible WinCache version is available on this server.
HEREDOC;
        if (ini_get('wincache.ucenabled')) {
            if ($isHttp || ini_get('wincache.enablecli')) {
                echo "You should be able to use it under this SAPI (", PHP_SAPI,
                    ").\n";
            } else {
                echo "\nWARNING: You can't use it under this SAPI (", PHP_SAPI,
                    ").\n";
            }
            echo "\n";
        } else {
            echo <<<HEREDOC
WARNING: The user cache of the WinCache is disabled via the wincache.ucenabled
         INI setting, making this package unusable with it.
         You need to enable it from php.ini.

HEREDOC;
        }
    }
}

if ($isHttp) {
    if (empty($available_extensions)) {
        echo <<<HEREDOC
WARNING: You don't have any compatible extensions for this SAPI.
         Install one of APC (>= 3.1.1), APCu (>=5.0.0) or WinCache (>= 1.1.0).
HEREDOC;
        echo '         (The current SAPI is "', PHP_SAPI, ").\n\n";
    }
} else {
    echo "You should be able to use the Placebo adapter under this SAPI (",
        PHP_SAPI, ").\n\n";
}

__HALT_COMPILER();

File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\bootstrap.php
<?php
require_once 'PEAR2/Autoload.php';
PEAR2\Autoload::initialize('../src');


File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\APC.phpt
--TEST--
APC tests.
--DESCRIPTION--
Sets up the settings for the APC adapter, and executes its tests.
--SKIPIF--
<?php if (!version_compare(phpversion('apc'), '3.1.1', '>=')) {
    die('Skip APC 3.1.1 or greather is required.');
}
?>
--CGI--
--GET--

--REDIRECTTEST--
return array(
    'GET' => array('adapter' => 'APC', 'nokeycode' => '101'),
    'TESTS' => getcwd() . DIRECTORY_SEPARATOR . 'Common'
);

File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\APCu.phpt
--TEST--
APCu tests.
--DESCRIPTION--
Sets up the settings for the APCu adapter, and executes its tests.
--SKIPIF--
<?php if (!version_compare(phpversion('apcu'), '5.0.0', '>=')) {
    die('Skip APCu 5.0.0 or greather is required.');
}
?>
--CGI--
--GET--

--REDIRECTTEST--
return array(
    'GET' => array('adapter' => 'APCu', 'nokeycode' => '101'),
    'TESTS' => getcwd() . DIRECTORY_SEPARATOR . 'Common'
);

File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\Common\testAddingTtlValue_part1.phpt
--TEST--
Tests adding a TTL-ed value, part 1
--DESCRIPTION--
In part 1, we set the value.
--FILE--
<?php
require_once '../includes/runner.php';

$adapterName = 'PEAR2\Cache\SHM\Adapter\\' . $adapter;
$object = new $adapterName('TEST');

assertSame(true, $object->add('key', 'value', 2), __FILE__);
assertSame(false, $object->add('key', 'value'), __FILE__);
assertSame('value', $object->get('key'), __FILE__);
?>
--EXPECT--


File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\Common\testAddingTtlValue_part2.phpt
--TEST--
Tests adding a TTL-ed value, part 2
--DESCRIPTION--
In part 2, we check to see we still have a value, and sleep() until it expires.
--FILE--
<?php
require_once '../includes/runner.php';

if ('cli' === PHP_SAPI) {
    die();//Added here, because the SKIP section is always "cli", but not this.
}

$adapterName = 'PEAR2\Cache\SHM\Adapter\\' . $adapter;
$object = new $adapterName('TEST');

assertSame('value', $object->get('key'), __FILE__);
sleep(3);
?>
--EXPECT--


File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\Common\testAddingTtlValue_part3.phpt
--TEST--
Tests adding a TTL-ed value, part 3
--DESCRIPTION--
In part 3, we check to verify we no longer have a value.
--FILE--
<?php
require_once '../includes/runner.php';

$adapterName = 'PEAR2\Cache\SHM\Adapter\\' . $adapter;
$object = new $adapterName('TEST');

try {
    $object->get('key');
    echo 'TTL value part 3: key did not expire.';
} catch(Exception $e) {
    assertSame(
        isset($_GET['nokeycode']) ? (int) $_GET['nokeycode'] : 200,
        $e->getCode(), __FILE__
    );
}
?>
--EXPECT--


File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\Common\testAddingValue.phpt
--TEST--
Tests adding a value
--FILE--
<?php
require_once '../includes/runner.php';

$adapterName = 'PEAR2\Cache\SHM\Adapter\\' . $adapter;
$object = new $adapterName('TEST');

assertSame(true, $object->add('key', 'value'), __FILE__);
assertSame(false, $object->add('key', 'value'), __FILE__);
?>
--EXPECT--


File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\Common\testSettingAndDeletingValue.phpt
--TEST--
Tests seting and deleting a value
--FILE--
<?php
require_once '../includes/runner.php';

$adapterName = 'PEAR2\Cache\SHM\Adapter\\' . $adapter;
$object = new $adapterName('TEST');

assertSame(true, $object->set('key', 'value'), __FILE__);
assertSame(true, $object->delete('key'), __FILE__);
assertSame(false, $object->delete('key'), __FILE__);
?>
--EXPECT--


File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\Common\testSettingAndGettingValue.phpt
--TEST--
Tests setting and getting a value
--FILE--
<?php
require_once '../includes/runner.php';

$adapterName = 'PEAR2\Cache\SHM\Adapter\\' . $adapter;
$object = new $adapterName('TEST');

assertSame(true, $object->set('key', 'value'), __FILE__);
assertSame('value', $object->get('key'), __FILE__);
?>
--EXPECT--


File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\Common\testSingleFileLockAndUnlock.phpt
--TEST--
Tests locking and unlocking within a single file
--FILE--
<?php
require_once '../includes/runner.php';

$adapterName = 'PEAR2\Cache\SHM\Adapter\\' . $adapter;
$object = new $adapterName('TEST');

assertSame(true, $object->lock('key'), __FILE__);
assertSame(false, $object->lock('key'), __FILE__);
assertSame(true, $object->unlock('key'), __FILE__);
assertSame(false, $object->unlock('key'), __FILE__);

assertSame(true, $object->lock('key'), __FILE__);
assertSame(false, $object->lock('key'), __FILE__);
assertSame(true, $object->unlock('key'), __FILE__);
assertSame(false, $object->unlock('key'), __FILE__);
?>
--EXPECT--


File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\includes\runner.php
<?php
use PEAR2\Autoload;

require_once 'PEAR2/Autoload.php';

$cwd = getcwd();
chdir(__DIR__ . '/../..');
Autoload::initialize(realpath(realpath('../src')));
chdir($cwd);

function assertSame($expected, $actual, $file)
{
    if ($expected !== $actual) {
        echo "Failed asserting that ";
        var_dump($actual);
        echo " is ";
        var_dump($expected);
        echo ' in "' . $file . "\"\n\n";
    }
}

$adapter = isset($_GET['adapter']) ? $_GET['adapter'] : 'Placebo';

File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\includes\SHM-factory.php
<?php
use PEAR2\Cache\SHM;
require_once 'runner.php';

$object = SHM::factory('TEST');

assertSame(true, $object instanceof SHM, __FILE__);

File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\Placebo.phpt
--TEST--
Placebo tests.
--DESCRIPTION--
Sets up the settings for the Placebo adapter, and executes its tests.
--REDIRECTTEST--
return array(
    'TESTS' => getcwd() . DIRECTORY_SEPARATOR . 'Common'
);


File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\SHM-factory_CGI.phpt
--TEST--
Factory CGI test.
--DESCRIPTION--
Checks that SHM::factory() can be called from CGI.
--CGI--
--GET--

--FILE_EXTERNAL--
includes/SHM-factory.php
--EXPECT--


File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\SHM-factory_CLI.phpt
--TEST--
Factory CLI test.
--DESCRIPTION--
Checks that SHM::factory() can be called from the command line.
--FILE_EXTERNAL--
includes/SHM-factory.php
--EXPECT--


File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\PHPT\Wincache.phpt
--TEST--
Wincache tests.
--DESCRIPTION--
Sets up the settings for the Wincache adapter, and executes its tests.
--SKIPIF--
<?php if (!version_compare(phpversion('wincache'), '1.1.0', '>=')) {
    die('Skip WinCache 1.1.0 or greather is required.');
}
?>
--CGI--
--GET--

--REDIRECTTEST--
return array(
    'GET' => array('adapter' => 'Wincache', 'nokeycode' => '300'),
    'TESTS' => getcwd() . DIRECTORY_SEPARATOR . 'Common'
);

File: /src\Libs\pear2\vendor\pear2\cache_shm\tests\phpunit.xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit
    bootstrap="bootstrap.php"
    colors="false"
    stopOnFailure="false"
    verbose="true"
    strict="true"
    
    convertErrorsToExceptions="true"
    convertNoticesToExceptions="true"
    convertWarningsToExceptions="true"
>
    <!--
    convertErrorsToExceptions="false"
    convertNoticesToExceptions="false"
    convertWarningsToExceptions="false"
>
    -->
    <testsuites>
        <testsuite name="All tests">
            <directory suffix=".phpt">PHPT</directory>
        </testsuite>
    </testsuites>
    <filter>
        <whitelist>
            <directory suffix=".php">../src/PEAR2/Cache/SHM</directory>
            <file>../src/PEAR2/Cache/SHM.php</file>
        </whitelist>
    </filter>
</phpunit>

File: /src\Libs\pear2\vendor\pear2\console_commandline\.gitignore
/tests/*.out
/tests/*.diff
/tests/*.exp
File: /src\Libs\pear2\vendor\pear2\console_commandline\.travis.yml
language: php
php:
  - 5.3
  - 5.4
  - 5.5
  - 5.6
  - 7.0
before_script:
  - pyrus install -p pyrus.net/Pyrus_Developer-alpha
  - pyrus install PEAR2_Autoload-alpha
script: pyrus run-phpt -r tests || (find . -name *.out | xargs -t cat && exit 1)


File: /src\Libs\pear2\vendor\pear2\console_commandline\composer.json
{
    "name": "pear2/console_commandline",
    "description": "Full featured package for managing command-line applications.",
    "keywords": ["pear2", "console", "CLI", "commandline", "arguments", "parser"],
    "homepage": "http://pear2.php.net/PEAR2_Console_CommandLine",
    "license": "MIT",
    "authors": [
        {
            "name": "David JEAN LOUIS",
            "email": "izi@php.net",
            "role": "lead"
        },
        {
            "name": "Brett Bieber",
            "email": "saltybeagle@php.net",
            "role": "helper"
        },
        {
            "name": "Vasil Rangelov",
            "email": "boen.robot@gmail.com",
            "role": "helper"
        }
    ],
    "support": {
        "issues": "http://github.com/pear2/Console_CommandLine/issues"
    },
    "require": {
        "php": ">=5.3.0"
    },
    "suggest": {
        "ext-dom": "Required when parsing definitions from an XML file"
    },
    "autoload": {
        "psr-0": {
            "PEAR2\\Console\\CommandLine": "src/"
        }
    },
    "minimum-stability": "dev"
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\CREDITS
; Maintainers of PEAR2_Console_CommandLine
David JEAN LOUIS [izi] <izi@php.net> (lead)
Brett Bieber [saltybeagle] <saltybeagle@php.net> (helper)
Vasil Rangelov [boen_robot] <boen.robot@gmail.com> (helper)

File: /src\Libs\pear2\vendor\pear2\console_commandline\data\xmlschema.rng
<?xml version="1.0" encoding="UTF-8"?>

<!-- 
  This is the RNG file for validating PEAR2_Console_CommandLine xml definitions.

  Author  : David JEAN LOUIS
  Licence : MIT License
  Version : GIT: $Id$
-->

<grammar xmlns="http://relaxng.org/ns/structure/1.0" 
         datatypeLibrary="http://www.w3.org/2001/XMLSchema-datatypes">

  <!-- structure -->
  <start>
      <ref name="ref_command"/>
  </start>

  <!-- Command node -->
  <define name="ref_command_subcommand_common">
    <interleave>
      <optional>
        <element name="name">
          <text/>
        </element>
      </optional>
      <optional>
        <element name="description">
          <text/>
        </element>
      </optional>
      <optional>
        <element name="version">
          <text/>
        </element>
      </optional>
      <optional>
        <element name="add_help_option">
          <ref name="ref_bool_choices"/>
        </element>
      </optional>
      <optional>
        <element name="add_version_option">
          <ref name="ref_bool_choices"/>
        </element>
      </optional>
      <optional>
        <element name="force_posix">
          <ref name="ref_bool_choices"/>
        </element>
      </optional>
      <optional>
        <ref name="ref_messages_common"/>
      </optional>
      <zeroOrMore>
        <ref name="ref_option"/>
      </zeroOrMore>
      <zeroOrMore>
        <ref name="ref_argument"/>
      </zeroOrMore>
      <zeroOrMore>
        <ref name="ref_subcommand"/>
      </zeroOrMore>
    </interleave>
  </define>

  <!-- command element -->

  <define name="ref_command">
    <element name="command">
      <interleave>
        <ref name="ref_command_subcommand_common"/>
      </interleave>
    </element>
  </define>

  <!-- subcommand element -->

  <define name="ref_subcommand">
    <element name="command">
      <interleave>
        <ref name="ref_command_subcommand_common"/>
        <optional>
          <element name="aliases">
            <zeroOrMore>
              <element name="alias">
                <text/>
              </element>
            </zeroOrMore>
          </element>
        </optional>
      </interleave>
    </element>
  </define>

  <!-- custom messages common element -->

  <define name="ref_messages_common">
    <element name="messages">
      <oneOrMore>
        <element name="message">
          <attribute name="name">
            <data type="string"/>
          </attribute>
          <text/>
        </element>
      </oneOrMore>
    </element>
  </define>

  <!-- options and arguments common elements -->

  <define name="ref_option_argument_common">
    <interleave>
      <optional>
        <element name="description">
          <text/>
        </element>
      </optional>
      <optional>
        <element name="help_name">
          <text/>
        </element>
      </optional>
      <optional>
        <element name="default">
          <text/>
        </element>
      </optional>
      <optional>
        <ref name="ref_messages_common"/>
      </optional>
    </interleave>
  </define>

  <!-- Option node -->
  <define name="ref_option">
    <element name="option">
      <attribute name="name">
        <data type="string"/>
      </attribute>
      <interleave>
        <optional>
          <element name="short_name">
            <text/>
          </element>
        </optional>
        <optional>
          <element name="long_name">
            <text/>
          </element>
        </optional>
        <ref name="ref_option_argument_common"/>
        <optional>
          <element name="action">
            <text/>
          </element>
        </optional>
        <optional>
          <element name="choices">
            <zeroOrMore>
              <element name="choice">
                <text/>
              </element>
            </zeroOrMore>
          </element>
        </optional>
        <optional>
          <element name="add_list_option">
            <ref name="ref_bool_choices"/>
          </element>
        </optional>
      </interleave>
    </element>
  </define>

  <!-- Argument node -->
  <define name="ref_argument">
    <element name="argument">
      <attribute name="name">
        <data type="string"/>
      </attribute>
      <interleave>
        <ref name="ref_option_argument_common"/>
        <optional>
          <element name="multiple">
            <ref name="ref_bool_choices"/>
          </element>
        </optional>
        <optional>
          <element name="optional">
            <ref name="ref_bool_choices"/>
          </element>
        </optional>
      </interleave>
    </element>
  </define>

  <!-- boolean choices -->
  <define name="ref_bool_choices">
    <choice>
      <value>true</value>
      <value>1</value>
      <value>on</value>
      <value>yes</value>
      <value>false</value>
      <value>0</value>
      <value>off</value>
      <value>no</value>
    </choice>
  </define>

</grammar>


File: /src\Libs\pear2\vendor\pear2\console_commandline\examples\ex1.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2_Console_CommandLine package.
 *
 * A simple example demonstrating the basic features of the PEAR2_Console_CommandLine
 * package.
 * In this example we create a program that simply zip a set of files.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2_Console_CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 */

// Include PEAR2 autoload
require_once 'PEAR2/Autoload.php';

// create the parser
$parser = new PEAR2_Console_CommandLine(
    array(
        'description' => 'zip given files using the php zip module.',
        'version'     => '1.0.0'
    )
);

// add an option to make the program verbose
$parser->addOption(
    'verbose',
    array(
        'short_name'  => '-v',
        'long_name'   => '--verbose',
        'action'      => 'StoreTrue',
        'description' => 'turn on verbose output'
    )
);

// add an option to delete original files after zipping
$parser->addOption(
    'delete',
    array(
        'short_name'      => '-d',
        'long_name'       => '--delete',
        'action'          => 'StoreString',
        'description'     => 'delete original files after zip operation',
        'choices'         => array('foo', 'bar'),
        'add_list_option' => true
    )
);

// add the files argument, the user can specify one or several files
$parser->addArgument(
    'files',
    array(
        'multiple'    => true,
        'description' => 'list of files to zip separated by spaces'
    )
);

// add the zip file name argument
$parser->addArgument(
    'zipfile',
    array(
        'description' => 'zip file name'
    )
);

// run the parser
try {
    $result = $parser->parse();
    // write your program here...
    print_r($result->options);
    print_r($result->args);
} catch (Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>


File: /src\Libs\pear2\vendor\pear2\console_commandline\examples\ex2.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2_Console_CommandLine package.
 *
 * This example demonstrate the use of xml definitions files with 
 * PEAR2_Console_CommandLine, the result is the same as for the ex1.php file.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2_Console_CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 */

// Include PEAR2 autoload
require_once 'PEAR2/Autoload.php';

// create the parser from xml file
$xmlfile = __DIR__ . DIRECTORY_SEPARATOR . 'ex2.xml';
$parser  = PEAR2_Console_CommandLine::fromXmlFile($xmlfile);


// run the parser
try {
    $result = $parser->parse();
    // write your program here...
    print_r($result->options);
    print_r($result->args);
} catch (Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>


File: /src\Libs\pear2\vendor\pear2\console_commandline\examples\ex2.xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<command>
    <description>zip given files using the php zip module.</description>
    <version>1.0.0</version>
    <option name="choice">
        <short_name>-c</short_name>
        <long_name>--choice</long_name>
        <description>choice option</description>
        <action>StoreString</action>
        <choices>
            <choice>ham</choice>
            <choice>spam</choice>
        </choices>
    </option>
    <option name="verbose">
        <short_name>-v</short_name>
        <long_name>--verbose</long_name>
        <description>turn on verbose output</description>
        <action>StoreTrue</action>
    </option>
    <option name="delete">
        <short_name>-d</short_name>
        <long_name>--delete</long_name>
        <description>delete original files after zip operation</description>
        <action>StoreTrue</action>
    </option>
    <argument name="files">
        <description>a list of files to zip together</description>
        <multiple>true</multiple>
    </argument>
    <argument name="zipfile">
        <description>path to the zip file to generate</description>
    </argument>
</command>


File: /src\Libs\pear2\vendor\pear2\console_commandline\examples\ex3.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR PEAR2_Console_CommandLine package.
 *
 * A simple example demonstrating the use of subcommands.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2_Console_CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 */

// Include PEAR2 autoload
require_once 'PEAR2/Autoload.php';

// create the parser
$parser = new PEAR2_Console_CommandLine(
    array(
        'description' => 'A great program that can foo and bar !',
        'version'     => '1.0.0'
    )
);

// add a global option to make the program verbose
$parser->addOption(
    'verbose',
    array(
        'short_name'  => '-v',
        'long_name'   => '--verbose',
        'action'      => 'StoreTrue',
        'description' => 'turn on verbose output'
    )
);

// add the foo subcommand
$foo_cmd = $parser->addCommand(
    'foo',
    array(
        'description' => 'output the given string with a foo prefix'
    )
);
$foo_cmd->addOption(
    'reverse',
    array(
        'short_name'  => '-r',
        'long_name'   => '--reverse',
        'action'      => 'StoreTrue',
        'description' => 'reverse the given string before echoing it'
    )
);
$foo_cmd->addArgument(
    'text',
    array(
        'description' => 'the text to output'
    )
);

// add the bar subcommand with a "baz" alias
$bar_cmd = $parser->addCommand(
    'bar',
    array(
        'description' => 'output the given string with a bar prefix',
        'aliases'     => array('baz'),
    )
);
$bar_cmd->addOption(
    'reverse',
    array(
        'short_name'  => '-r',
        'long_name'   => '--reverse',
        'action'      => 'StoreTrue',
        'description' => 'reverse the given string before echoing it'
    )
);
$bar_cmd->addArgument(
    'text',
    array(
        'description' => 'the text to output'
    )
);

// run the parser
try {
    $result = $parser->parse();
    if ($result->command_name) {
        $st = $result->command->options['reverse'] 
            ? strrev($result->command->args['text'])
            : $result->command->args['text'];
        if ($result->command_name == 'foo') { 
            echo "Foo says: $st\n";
        } else if ($result->command_name == 'bar') {
            echo "Bar says: $st\n";
        }
    }
} catch (Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>


File: /src\Libs\pear2\vendor\pear2\console_commandline\examples\ex4.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR PEAR2_Console_CommandLine package.
 *
 * A simple example demonstrating the use of subcommands.
 * (Same as ex3.php but using an xml file).
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2_Console_CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 */

// Include PEAR2 autoload
require_once 'PEAR2/Autoload.php';

// create the parser
$xmlfile = __DIR__ . DIRECTORY_SEPARATOR . 'ex4.xml';
$parser  = PEAR2_Console_CommandLine::fromXmlFile($xmlfile);

// run the parser
try {
    $result = $parser->parse();
    if ($result->command_name) {
        $st = $result->command->options['reverse'] 
            ? strrev($result->command->args['text'])
            : $result->command->args['text'];
        if ($result->command_name == 'foo') { 
            echo "Foo says: $st\n";
        } else if ($result->command_name == 'bar') {
            echo "Bar says: $st\n";
        }
    }
} catch (Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>


File: /src\Libs\pear2\vendor\pear2\console_commandline\examples\ex4.xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<command>
    <description>A great program that can foo and bar !</description>
    <version>1.0.0</version>
    <option name="verbose">
        <short_name>-v</short_name>
        <long_name>--verbose</long_name>
        <description>turn on verbose output</description>
        <action>StoreTrue</action>
    </option>
    <command>
        <name>foo</name>
        <description>output the given string with a foo prefix</description>
        <option name="reverse">
            <short_name>-r</short_name>
            <long_name>--reverse</long_name>
            <description>reverse the string before echoing it</description>
            <action>StoreTrue</action>
        </option>
        <argument name="text">
            <description>the text to output</description>
        </argument>
    </command>
    <command>
        <name>bar</name>
        <description>output the given string with a bar prefix</description>
        <option name="reverse">
            <short_name>-r</short_name>
            <long_name>--reverse</long_name>
            <description>reverse the string before echoing it</description>
            <action>StoreTrue</action>
        </option>
        <argument name="text">
            <description>the text to output</description>
        </argument>
    </command>
</command>


File: /src\Libs\pear2\vendor\pear2\console_commandline\extrasetup.php
<?php

/**
 * This file is part of the PEAR2_Console_CommandLine package.
 *
 * A full featured package for managing command-line options and arguments 
 * hightly inspired from python optparse module, it allows the developper to 
 * easily build complex command line interfaces.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2_Console_CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 */

$packages = array(
    'pear2.php.net' => array(
        'PEAR2_Autoload'
    )
);

$extrafiles = array();
$config = Pyrus\Config::current();
$registry = $config->registry;
$phpDir = $config->php_dir;

foreach ($packages as $channel => $channelPackages) {
    foreach ($channelPackages as $package) {
        foreach ($registry->toPackage($package, $channel)->installcontents
            as $file => $info) {
            if (strpos($file, 'php/') === 0) {
                $filename = substr($file, 4);
                $extrafiles['src/' . $filename]
                    = realpath($phpDir . DIRECTORY_SEPARATOR . $filename);
            }
        }
    }
}

File: /src\Libs\pear2\vendor\pear2\console_commandline\package.xml
<?xml version="1.0" encoding="UTF-8"?>
<package version="2.1" xmlns="http://pear.php.net/dtd/package-2.1" xmlns:tasks="http://pear.php.net/dtd/tasks-1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://pear.php.net/dtd/tasks-1.0     http://pear.php.net/dtd/tasks-1.0.xsd     http://pear.php.net/dtd/package-2.1     http://pear.php.net/dtd/package-2.1.xsd">
 <name>PEAR2_Console_CommandLine</name>
 <channel>pear2.php.net</channel>
 <summary>PEAR2_Console_CommandLine is a full featured package for managing command-line
</summary>
 <description>options and arguments highly inspired from python optparse module, it allows
the developer to easily build complex command line interfaces.

Main features:
* handles sub commands (ie. $ myscript.php -q subcommand -f file),
* can be completely built from an xml definition file,
* generate --help and --version options automatically,
* can be completely customized,
* builtin support for i18n,
* and much more...

</description>
 <lead>
  <name>David JEAN LOUIS</name>
  <user>izi</user>
  <email>izi@php.net</email>
  <active>yes</active>
 </lead>
 <helper>
  <name>Brett Bieber</name>
  <user>saltybeagle</user>
  <email>saltybeagle@php.net</email>
  <active>yes</active>
 </helper>
 <helper>
  <name>Vasil Rangelov</name>
  <user>boen_robot</user>
  <email>boen.robot@gmail.com</email>
  <active>yes</active>
 </helper>
 <date>2017-05-22</date>
 <time>14:40:46</time>
 <version>
  <release>0.2.3</release>
  <api>0.1.0</api>
 </version>
 <stability>
  <release>alpha</release>
  <api>alpha</api>
 </stability>
 <license uri="http://opensource.org/licenses/mit-license.php">MIT License</license>
 <notes>* Re-fixed the path to the RNG schema, now with all the new paths in mind.</notes>
 <contents>
  <dir name="/">
   <dir name="data" baseinstalldir="/">
    <file role="data" name="xmlschema.rng">
     <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
    </file>
   </dir>
   <dir name="examples">
    <file role="doc" name="ex1.php">
     <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
    </file>
    <file role="doc" name="ex2.php">
     <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
    </file>
    <file role="doc" name="ex2.xml"/>
    <file role="doc" name="ex3.php">
     <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
    </file>
    <file role="doc" name="ex4.php">
     <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
    </file>
    <file role="doc" name="ex4.xml"/>
   </dir>
   <dir name="src" baseinstalldir="/">
    <dir name="PEAR2">
     <dir name="Console">
      <dir name="CommandLine">
       <dir name="Action">
        <file role="php" name="Callback.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
        <file role="php" name="Counter.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
        <file role="php" name="Help.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
        <file role="php" name="List.php"/>
        <file role="php" name="Password.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
        <file role="php" name="StoreArray.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
        <file role="php" name="StoreFalse.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
        <file role="php" name="StoreFloat.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
        <file role="php" name="StoreInt.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
        <file role="php" name="StoreString.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
        <file role="php" name="StoreTrue.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
        <file role="php" name="Version.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
       </dir>
       <dir name="MessageProvider">
        <file role="php" name="DefaultProvider.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
       </dir>
       <dir name="Outputter">
        <file role="php" name="Default.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
       </dir>
       <dir name="Renderer">
        <file role="php" name="Default.php">
         <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
        </file>
       </dir>
       <file role="php" name="Action.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       </file>
       <file role="php" name="Argument.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       </file>
       <file role="php" name="Command.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       </file>
       <file role="php" name="CustomMessageProvider.php"/>
       <file role="php" name="Element.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       </file>
       <file role="php" name="Exception.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       </file>
       <file role="php" name="MessageProvider.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       </file>
       <file role="php" name="Option.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       </file>
       <file role="php" name="Outputter.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       </file>
       <file role="php" name="Renderer.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       </file>
       <file role="php" name="Result.php">
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       </file>
       <file role="php" name="XmlParser.php">
        <tasks:replace type="pear-config" to="data_dir" from="@data_dir@"/>
        <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
       </file>
      </dir>
      <file role="php" name="CommandLine.php"/>
     </dir>
    </dir>
   </dir>
   <dir name="tests" baseinstalldir="/">
    <file role="test" name="AllTests.php">
     <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
    </file>
    <file role="test" name="console_commandline_accept.phpt"/>
    <file role="test" name="console_commandline_addargument.phpt"/>
    <file role="test" name="console_commandline_addargument2.phpt"/>
    <file role="test" name="console_commandline_addcommand.phpt"/>
    <file role="test" name="console_commandline_addcommand_3.phpt"/>
    <file role="test" name="console_commandline_addoption.phpt"/>
    <file role="test" name="console_commandline_addoption_errors_1.phpt"/>
    <file role="test" name="console_commandline_addoption_errors_2.phpt"/>
    <file role="test" name="console_commandline_addoption_errors_3.phpt"/>
    <file role="test" name="console_commandline_addoption_errors_4.phpt"/>
    <file role="test" name="console_commandline_addoption_errors_5.phpt"/>
    <file role="test" name="console_commandline_addoption_errors_6.phpt"/>
    <file role="test" name="console_commandline_addoption_errors_7.phpt"/>
    <file role="test" name="console_commandline_bug18682.phpt"/>
    <file role="test" name="console_commandline_fromxmlfile.phpt"/>
    <file role="test" name="console_commandline_fromxmlfile_error.phpt"/>
    <file role="test" name="console_commandline_fromxmlstring.phpt"/>
    <file role="test" name="console_commandline_options_defaults.phpt"/>
    <file role="test" name="console_commandline_parse_1.phpt"/>
    <file role="test" name="console_commandline_parse_2.phpt"/>
    <file role="test" name="console_commandline_parse_3.phpt"/>
    <file role="test" name="console_commandline_parse_4.phpt"/>
    <file role="test" name="console_commandline_parse_5.phpt"/>
    <file role="test" name="console_commandline_parse_6.phpt"/>
    <file role="test" name="console_commandline_parse_7.phpt"/>
    <file role="test" name="console_commandline_parse_8.phpt"/>
    <file role="test" name="console_commandline_parse_9.phpt"/>
    <file role="test" name="console_commandline_parse_10.phpt"/>
    <file role="test" name="console_commandline_parse_11.phpt"/>
    <file role="test" name="console_commandline_parse_12.phpt"/>
    <file role="test" name="console_commandline_parse_13.phpt"/>
    <file role="test" name="console_commandline_parse_14.phpt"/>
    <file role="test" name="console_commandline_parse_15.phpt"/>
    <file role="test" name="console_commandline_parse_16.phpt"/>
    <file role="test" name="console_commandline_parse_17.phpt"/>
    <file role="test" name="console_commandline_parse_18.phpt"/>
    <file role="test" name="console_commandline_parse_19.phpt"/>
    <file role="test" name="console_commandline_parse_20.phpt"/>
    <file role="test" name="console_commandline_parse_21.phpt"/>
    <file role="test" name="console_commandline_parse_22.phpt"/>
    <file role="test" name="console_commandline_parse_23.phpt"/>
    <file role="test" name="console_commandline_parse_24.phpt"/>
    <file role="test" name="console_commandline_parse_25.phpt"/>
    <file role="test" name="console_commandline_parse_26.phpt"/>
    <file role="test" name="console_commandline_parse_27.phpt"/>
    <file role="test" name="console_commandline_parse_28.phpt"/>
    <file role="test" name="console_commandline_parse_29.phpt"/>
    <file role="test" name="console_commandline_webrequest_1.phpt"/>
    <file role="test" name="console_commandline_webrequest_2.phpt"/>
    <file role="test" name="console_commandline_webrequest_3.phpt"/>
    <file role="test" name="test.xml"/>
    <file role="test" name="tests.inc.php">
     <tasks:replace type="pear-config" to="php_dir" from="../src"/>
     <tasks:replace type="package-info" to="version" from="GIT: $Id$"/>
    </file>
   </dir>
  </dir>
 </contents>
 <dependencies>
  <required>
   <php>
    <min>5.3.0</min>
   </php>
   <pearinstaller>
    <min>1.4.0</min>
   </pearinstaller>
  </required>
  <optional>
   <package>
    <name>PEAR2_Autoload</name>
    <channel>pear2.php.net</channel>
   </package>
   <extension>
    <name>dom</name>
   </extension>
  </optional>
 </dependencies>
 <phprelease>
  <filelist>
   <install name="data/xmlschema.rng" as="xmlschema.rng"/>
   <install name="examples/ex1.php" as="examples/ex1.php"/>
   <install name="examples/ex2.php" as="examples/ex2.php"/>
   <install name="examples/ex2.xml" as="examples/ex2.xml"/>
   <install name="examples/ex3.php" as="examples/ex3.php"/>
   <install name="examples/ex4.php" as="examples/ex4.php"/>
   <install name="examples/ex4.xml" as="examples/ex4.xml"/>
   <install name="src/PEAR2/Console/CommandLine.php" as="PEAR2/Console/CommandLine.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action.php" as="PEAR2/Console/CommandLine/Action.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/Callback.php" as="PEAR2/Console/CommandLine/Action/Callback.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/Counter.php" as="PEAR2/Console/CommandLine/Action/Counter.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/Help.php" as="PEAR2/Console/CommandLine/Action/Help.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/List.php" as="PEAR2/Console/CommandLine/Action/List.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/Password.php" as="PEAR2/Console/CommandLine/Action/Password.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/StoreArray.php" as="PEAR2/Console/CommandLine/Action/StoreArray.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/StoreFalse.php" as="PEAR2/Console/CommandLine/Action/StoreFalse.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/StoreFloat.php" as="PEAR2/Console/CommandLine/Action/StoreFloat.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/StoreInt.php" as="PEAR2/Console/CommandLine/Action/StoreInt.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/StoreString.php" as="PEAR2/Console/CommandLine/Action/StoreString.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/StoreTrue.php" as="PEAR2/Console/CommandLine/Action/StoreTrue.php"/>
   <install name="src/PEAR2/Console/CommandLine/Action/Version.php" as="PEAR2/Console/CommandLine/Action/Version.php"/>
   <install name="src/PEAR2/Console/CommandLine/Argument.php" as="PEAR2/Console/CommandLine/Argument.php"/>
   <install name="src/PEAR2/Console/CommandLine/Command.php" as="PEAR2/Console/CommandLine/Command.php"/>
   <install name="src/PEAR2/Console/CommandLine/CustomMessageProvider.php" as="PEAR2/Console/CommandLine/CustomMessageProvider.php"/>
   <install name="src/PEAR2/Console/CommandLine/Element.php" as="PEAR2/Console/CommandLine/Element.php"/>
   <install name="src/PEAR2/Console/CommandLine/Exception.php" as="PEAR2/Console/CommandLine/Exception.php"/>
   <install name="src/PEAR2/Console/CommandLine/MessageProvider.php" as="PEAR2/Console/CommandLine/MessageProvider.php"/>
   <install name="src/PEAR2/Console/CommandLine/MessageProvider/DefaultProvider.php" as="PEAR2/Console/CommandLine/MessageProvider/DefaultProvider.php"/>
   <install name="src/PEAR2/Console/CommandLine/Option.php" as="PEAR2/Console/CommandLine/Option.php"/>
   <install name="src/PEAR2/Console/CommandLine/Outputter.php" as="PEAR2/Console/CommandLine/Outputter.php"/>
   <install name="src/PEAR2/Console/CommandLine/Outputter/Default.php" as="PEAR2/Console/CommandLine/Outputter/Default.php"/>
   <install name="src/PEAR2/Console/CommandLine/Renderer.php" as="PEAR2/Console/CommandLine/Renderer.php"/>
   <install name="src/PEAR2/Console/CommandLine/Renderer/Default.php" as="PEAR2/Console/CommandLine/Renderer/Default.php"/>
   <install name="src/PEAR2/Console/CommandLine/Result.php" as="PEAR2/Console/CommandLine/Result.php"/>
   <install name="src/PEAR2/Console/CommandLine/XmlParser.php" as="PEAR2/Console/CommandLine/XmlParser.php"/>
   <install name="tests/AllTests.php" as="AllTests.php"/>
   <install name="tests/console_commandline_accept.phpt" as="console_commandline_accept.phpt"/>
   <install name="tests/console_commandline_addargument.phpt" as="console_commandline_addargument.phpt"/>
   <install name="tests/console_commandline_addargument2.phpt" as="console_commandline_addargument2.phpt"/>
   <install name="tests/console_commandline_addcommand.phpt" as="console_commandline_addcommand.phpt"/>
   <install name="tests/console_commandline_addcommand_3.phpt" as="console_commandline_addcommand_3.phpt"/>
   <install name="tests/console_commandline_addoption.phpt" as="console_commandline_addoption.phpt"/>
   <install name="tests/console_commandline_addoption_errors_1.phpt" as="console_commandline_addoption_errors_1.phpt"/>
   <install name="tests/console_commandline_addoption_errors_2.phpt" as="console_commandline_addoption_errors_2.phpt"/>
   <install name="tests/console_commandline_addoption_errors_3.phpt" as="console_commandline_addoption_errors_3.phpt"/>
   <install name="tests/console_commandline_addoption_errors_4.phpt" as="console_commandline_addoption_errors_4.phpt"/>
   <install name="tests/console_commandline_addoption_errors_5.phpt" as="console_commandline_addoption_errors_5.phpt"/>
   <install name="tests/console_commandline_addoption_errors_6.phpt" as="console_commandline_addoption_errors_6.phpt"/>
   <install name="tests/console_commandline_addoption_errors_7.phpt" as="console_commandline_addoption_errors_7.phpt"/>
   <install name="tests/console_commandline_bug18682.phpt" as="console_commandline_bug18682.phpt"/>
   <install name="tests/console_commandline_fromxmlfile.phpt" as="console_commandline_fromxmlfile.phpt"/>
   <install name="tests/console_commandline_fromxmlfile_error.phpt" as="console_commandline_fromxmlfile_error.phpt"/>
   <install name="tests/console_commandline_fromxmlstring.phpt" as="console_commandline_fromxmlstring.phpt"/>
   <install name="tests/console_commandline_options_defaults.phpt" as="console_commandline_options_defaults.phpt"/>
   <install name="tests/console_commandline_parse_1.phpt" as="console_commandline_parse_1.phpt"/>
   <install name="tests/console_commandline_parse_2.phpt" as="console_commandline_parse_2.phpt"/>
   <install name="tests/console_commandline_parse_3.phpt" as="console_commandline_parse_3.phpt"/>
   <install name="tests/console_commandline_parse_4.phpt" as="console_commandline_parse_4.phpt"/>
   <install name="tests/console_commandline_parse_5.phpt" as="console_commandline_parse_5.phpt"/>
   <install name="tests/console_commandline_parse_6.phpt" as="console_commandline_parse_6.phpt"/>
   <install name="tests/console_commandline_parse_7.phpt" as="console_commandline_parse_7.phpt"/>
   <install name="tests/console_commandline_parse_8.phpt" as="console_commandline_parse_8.phpt"/>
   <install name="tests/console_commandline_parse_9.phpt" as="console_commandline_parse_9.phpt"/>
   <install name="tests/console_commandline_parse_10.phpt" as="console_commandline_parse_10.phpt"/>
   <install name="tests/console_commandline_parse_11.phpt" as="console_commandline_parse_11.phpt"/>
   <install name="tests/console_commandline_parse_12.phpt" as="console_commandline_parse_12.phpt"/>
   <install name="tests/console_commandline_parse_13.phpt" as="console_commandline_parse_13.phpt"/>
   <install name="tests/console_commandline_parse_14.phpt" as="console_commandline_parse_14.phpt"/>
   <install name="tests/console_commandline_parse_15.phpt" as="console_commandline_parse_15.phpt"/>
   <install name="tests/console_commandline_parse_16.phpt" as="console_commandline_parse_16.phpt"/>
   <install name="tests/console_commandline_parse_17.phpt" as="console_commandline_parse_17.phpt"/>
   <install name="tests/console_commandline_parse_18.phpt" as="console_commandline_parse_18.phpt"/>
   <install name="tests/console_commandline_parse_19.phpt" as="console_commandline_parse_19.phpt"/>
   <install name="tests/console_commandline_parse_20.phpt" as="console_commandline_parse_20.phpt"/>
   <install name="tests/console_commandline_parse_21.phpt" as="console_commandline_parse_21.phpt"/>
   <install name="tests/console_commandline_parse_22.phpt" as="console_commandline_parse_22.phpt"/>
   <install name="tests/console_commandline_parse_23.phpt" as="console_commandline_parse_23.phpt"/>
   <install name="tests/console_commandline_parse_24.phpt" as="console_commandline_parse_24.phpt"/>
   <install name="tests/console_commandline_parse_25.phpt" as="console_commandline_parse_25.phpt"/>
   <install name="tests/console_commandline_parse_26.phpt" as="console_commandline_parse_26.phpt"/>
   <install name="tests/console_commandline_parse_27.phpt" as="console_commandline_parse_27.phpt"/>
   <install name="tests/console_commandline_parse_28.phpt" as="console_commandline_parse_28.phpt"/>
   <install name="tests/console_commandline_parse_29.phpt" as="console_commandline_parse_29.phpt"/>
   <install name="tests/console_commandline_webrequest_1.phpt" as="console_commandline_webrequest_1.phpt"/>
   <install name="tests/console_commandline_webrequest_2.phpt" as="console_commandline_webrequest_2.phpt"/>
   <install name="tests/console_commandline_webrequest_3.phpt" as="console_commandline_webrequest_3.phpt"/>
   <install name="tests/test.xml" as="test.xml"/>
   <install name="tests/tests.inc.php" as="tests.inc.php"/>
  </filelist>
 </phprelease>
</package>


File: /src\Libs\pear2\vendor\pear2\console_commandline\packagexmlsetup.php
<?php

/**
 * This file is part of the PEAR2_Console_CommandLine package.
 *
 * A full featured package for managing command-line options and arguments 
 * hightly inspired from python optparse module, it allows the developper to 
 * easily build complex command line interfaces.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2_Console_CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 */

/**
 * References the package in $package
 */
use Pyrus\Developer\PackageFile\v2;

/**
 * Configuration array.
 * 
 * Each key is the task.
 * 
 * The task "replace" uses an array where the key is the value to be searched
 * for, and the value is an array of additional attributes for the task, which
 * normally contain at least "type" (pear-config/package-info) and "to", which
 * specifies the value to replace it with.
 * 
 * The task "eol" uses an array where the key is a filename pattern to be
 * matched, and the value is the target platform's EOL to be used for those
 * file names (windows/unix).
 * 
 * Unrecognized tasks are ignored.
 * 
 * @var array
 */
$config = array(
    'replace' => array(
        '../src' => array(
            'type' => 'pear-config',
            'to' => 'php_dir'
        ),
        '@data_dir@' => array(
            'type' => 'pear-config',
            'to' => 'data_dir'
        ),
        'GIT: $Id$' => array(
            'type' => 'package-info',
            'to' => 'version'
        )
    ),
    'eol' => array(
        '*.bat' => 'windows'
    )
);

if (!isset($package)) {
    die('This file must be executed via "pyrus.phar make".');
}

$packageGen = function (
    array $config,
    v2 $package,
    v2 $compatible = null
) {

    $tasksNs = $package->getTasksNs();
    $cTasksNs = $compatible ? $compatible->getTasksNs() : '';
    $oldCwd = getcwd();
    chdir(__DIR__);
    $package->setRawRelease('php', '');
    $release = $package->getReleaseToInstall('php');
    foreach (new RecursiveIteratorIterator(
        new RecursiveDirectoryIterator(
            '.',
            RecursiveDirectoryIterator::UNIX_PATHS
            | RecursiveDirectoryIterator::SKIP_DOTS
        ),
        RecursiveIteratorIterator::LEAVES_ONLY
    ) as $path) {
            $filename = substr($path->getPathname(), 2);
            $cFilename = str_replace('src/', 'php/', $filename);

        if (isset($package->files[$filename])) {
            $parsedFilename = pathinfo($filename);
            $as = (strpos($filename, 'examples/') === 0)
                ? $filename
                : substr($filename, strpos($filename, '/') + 1);
            if (strpos($filename, 'scripts/') === 0) {
                if (isset($parsedFilename['extension'])
                    && 'php' === $parsedFilename['extension']
                    && !is_file(
                        $parsedFilename['dirname'] . '/' .
                        $parsedFilename['filename']
                    )
                    && is_file(
                        $parsedFilename['dirname'] . '/' .
                        $parsedFilename['filename'] . '.bat'
                    )
                ) {
                    $as = substr($as, 0, -4);
                }
            }
            $release->installAs($filename, $as);

            $contents = file_get_contents($filename);
            foreach ($config['replace'] as $from => $attribs) {
                if (strpos($contents, $from) !== false) {
                    $attribs['from'] = $from;
                    $package->files[$filename] = array_merge_recursive(
                        $package->files[$filename]->getArrayCopy(),
                        array(
                            "{$tasksNs}:replace" => array(
                                array(
                                    'attribs' => $attribs
                                )
                            )
                        )
                    );

                    if ($compatible) {
                        $compatible->files[$cFilename] = array_merge_recursive(
                            $compatible->files[$cFilename]->getArrayCopy(),
                            array(
                                "{$cTasksNs}:replace" => array(
                                    array(
                                        'attribs' => $attribs
                                    )
                                )
                            )
                        );
                    }
                }
            }

            foreach ($config['eol'] as $pattern => $platform) {
                if (fnmatch($pattern, $filename)) {
                    $package->files[$filename] = array_merge_recursive(
                        $package->files[$filename]->getArrayCopy(),
                        array(
                            "{$tasksNs}:{$platform}eol" => array()
                        )
                    );

                    if ($compatible) {
                        $compatible->files[$cFilename] = array_merge_recursive(
                            $compatible->files[$cFilename]->getArrayCopy(),
                            array(
                                "{$cTasksNs}:{$platform}eol" => array()
                            )
                        );
                    }
                }
            }
        }
    }
    chdir($oldCwd);
    return array($package, $compatible);
};

list($package, $compatible) = $packageGen(
    $config,
    $package,
    isset($compatible) ? $compatible : null
);
if (null === $compatible) {
    unset($compatible);
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\README
PEAR2_Console_CommandLine is a full featured package for managing command-line
options and arguments highly inspired from python optparse module, it allows
the developer to easily build complex command line interfaces.

Main features:
* handles sub commands (ie. $ myscript.php -q subcommand -f file),
* can be completely built from an xml definition file,
* generate --help and --version options automatically,
* can be completely customized,
* builtin support for i18n,
* and much more...



File: /src\Libs\pear2\vendor\pear2\console_commandline\RELEASE-0.1.0
Initial port of PEAR Console_CommandLine to PEAR2.

Major differences are namespace usage and no require statements.

This release is in sync with pear.php.net/Console_CommandLine-1.1.3


File: /src\Libs\pear2\vendor\pear2\console_commandline\RELEASE-0.2.0
Features and changes
 - Implemented feature request #18582 (From pear.php.net) add possibility to require a subcommand
 - Implemented feature request #18583 (From pear.php.net) default values for arguments
 - removed the enclosing "< >" on argument names (it looks better IMO).

Bug Fixes
 - Fixed bug #18584 (From pear.php.net) optional arguments not shown as optional

File: /src\Libs\pear2\vendor\pear2\console_commandline\RELEASE-0.2.1
* Added a composer.json, and this package to packagist.org.
* Fixed GitHub issue #2: columnWrap() in Default Renderer eats up lines with only a EOL.
* Fixed validation of XML definition files: The directory of the RNG schema was wrong.
* Fixed test suite errors, including namespace related ones and adding Travis-CI configuration.
* Removed PEAR2\Exception dependency - This package's exception directly inherits from the root Exception.
* CS fixes.


File: /src\Libs\pear2\vendor\pear2\console_commandline\RELEASE-0.2.2
* Brought fixes from PEAR_Console_CommandLine 1.2.2, namely
    - xmlschema.rng is looked for in more locations (though this package also includes a lookup first on Pyrus' folder layout, and also respects the PHP_PEAR_DATA_DIR environment variable's value, and fixes the error message when the file is not found in any location)
    - Package dependencies include DOM (though this package includes it as an optional dependency, because it's only needed when getting definitions from an XML file; not when constructing them "manually; Also, the "xml" extension is not used, so it's not included here)
    - Fixed comparrisons in PHP7
    - Replaced static with private variables
* Made this package PSR-4 compatible, while preserving PSR-0 compatibility by moving MessageProvider_Default into it's own MessageProvider sub-namespace, and renaming the class itself to DefaultProvider to avoid it having a reserved word ("default") as its name.
* CS fixes.

File: /src\Libs\pear2\vendor\pear2\console_commandline\RELEASE-0.2.3
* Re-fixed the path to the RNG schema, now with all the new paths in mind.

File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\Callback.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */
namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;


/**
 * Class that represent the Callback action.
 *
 * The result option array entry value is set to the return value of the
 * callback defined in the option.
 *
 * There are two steps to defining a callback option:
 *   - define the option itself using the callback action
 *   - write the callback; this is a function (or method) that takes five
 *     arguments, as described below.
 *
 * All callbacks are called as follows:
 * <code>
 * callable_func(
 *     $value,           // the value of the option
 *     $option_instance, // the option instance
 *     $result_instance, // the result instance
 *     $parser_instance, // the parser instance
 *     $params           // an array of params as specified in the option
 * );
 * </code>
 * and *must* return the option value.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Callback extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The value of the option
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(
            call_user_func(
                $this->option->callback,
                $value,
                $this->option,
                $this->result,
                $this->parser,
                $params
            )
        );
    }
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\Counter.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the Version action.
 *
 * The execute methode add 1 to the value of the result option array entry.
 * The value is incremented each time the option is found, for example
 * with an option defined like that:
 *
 * <code>
 * $parser->addOption(
 *     'verbose',
 *     array(
 *         'short_name' => '-v',
 *         'action'     => 'Counter'
 *     )
 * );
 * </code>
 * If the user type:
 * <code>
 * $ script.php -v -v -v
 * </code>
 * or:
 * <code>
 * $ script.php -vvv
 * </code>
 * the verbose variable will be set to to 3.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Counter extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $result = $this->getResult();
        if ($result === null) {
            $result = 0;
        }
        $this->setResult(++$result);
    }
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\Help.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the Help action, a special action that displays the
 * help message, telling the user how to use the program.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Help extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        return $this->parser->displayUsage();
    }
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\List.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   CVS: $Id: List.php,v 1.2 2009/02/27 08:03:17 izi Exp $
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Class that represent the List action, a special action that simply output an
 * array as a list.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Action_List extends Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     * Possible parameters are:
     * - message: an alternative message to display instead of the default
     *   message,
     * - delimiter: an alternative delimiter instead of the comma,
     * - post: a string to append after the message (default is the new line
     *   char).
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $list = isset($params['list']) ? $params['list'] : array();
        $msg  = isset($params['message'])
            ? $params['message']
            : $this->parser->message_provider->get('LIST_DISPLAYED_MESSAGE');
        $del  = isset($params['delimiter']) ? $params['delimiter'] : ', ';
        $post = isset($params['post']) ? $params['post'] : "\n";
        $this->parser->outputter->stdout($msg . implode($del, $list) . $post);
        exit(0);
    }
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\Password.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the Password action, a special action that allow the
 * user to specify the password on the commandline or to be prompted for
 * entering it.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Password extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(empty($value) ? $this->_promptPassword() : $value);
    }
    // }}}
    // _promptPassword() {{{

    /**
     * Prompts the password to the user without echoing it.
     *
     * @return string
     *
     * @todo not echo-ing the password does not work on windows is there a way
     *       to make this work ?
     */
    private function _promptPassword()
    {
        if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN') {
            fwrite(
                STDOUT,
                $this->parser->message_provider->get('PASSWORD_PROMPT_ECHO')
            );
            @flock(STDIN, LOCK_EX);
            $passwd = fgets(STDIN);
            @flock(STDIN, LOCK_UN);
        } else {
            fwrite(STDOUT, $this->parser->message_provider->get('PASSWORD_PROMPT'));
            // disable echoing
            system('stty -echo');
            @flock(STDIN, LOCK_EX);
            $passwd = fgets(STDIN);
            @flock(STDIN, LOCK_UN);
            system('stty echo');
        }
        return trim($passwd);
    }
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\StoreArray.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreArray action.
 *
 * The execute method appends the value of the option entered by the user to
 * the result option array entry.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreArray extends CommandLine\Action
{
    // Protected properties {{{

    /**
     * Force a clean result when first called, overriding any defaults assigned.
     *
     * @var object $firstPass First time this action has been called.
     */
    protected $firstPass = true;

    // }}}
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $result = $this->getResult();
        if (null === $result || $this->firstPass) {
            $result          = array();
            $this->firstPass = false;
        }
        $result[] = $value;
        $this->setResult($result);
    }
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\StoreFalse.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreFalse action.
 *
 * The execute method store the boolean 'false' in the corrsponding result
 * option array entry (the value is true if the option is not present in the
 * command line entered by the user).
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreFalse extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(false);
    }

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\StoreFloat.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreFloat action.
 *
 * The execute method store the value of the option entered by the user as a
 * float in the result option array entry, if the value passed is not a float
 * an Exception is raised.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreFloat extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     * @throws PEAR2\Console\CommandLine\Exception
     */
    public function execute($value = false, $params = array())
    {
        if (!is_numeric($value)) {
            throw CommandLine\Exception::factory(
                'OPTION_VALUE_TYPE_ERROR',
                array(
                    'name'  => $this->option->name,
                    'type'  => 'float',
                    'value' => $value
                ),
                $this->parser
            );
        }
        $this->setResult((float)$value);
    }
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\StoreInt.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreInt action.
 *
 * The execute method store the value of the option entered by the user as an
 * integer in the result option array entry, if the value passed is not an
 * integer an Exception is raised.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreInt extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     * @throws PEAR2\Console\CommandLine\Exception
     */
    public function execute($value = false, $params = array())
    {
        if (!is_numeric($value)) {
            throw CommandLine\Exception::factory(
                'OPTION_VALUE_TYPE_ERROR',
                array(
                    'name'  => $this->option->name,
                    'type'  => 'int',
                    'value' => $value
                ),
                $this->parser
            );
        }
        $this->setResult((int)$value);
    }
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\StoreString.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreString action.
 *
 * The execute method store the value of the option entered by the user as a
 * string in the result option array entry.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreString extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult((string)$value);
    }
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\StoreTrue.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreTrue action.
 *
 * The execute method store the boolean 'true' in the corrsponding result
 * option array entry (the value is false if the option is not present in the
 * command line entered by the user).
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreTrue extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(true);
    }
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action\Version.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the Version action, a special action that displays the
 * version string of the program.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Version extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        return $this->parser->displayVersion();
    }
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Action.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */
namespace PEAR2\Console\CommandLine;

/**
 * Class that represent an option action.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
abstract class Action
{
    // Properties {{{

    /**
     * A reference to the result instance.
     *
     * @var PEAR2\Console\CommandLine_Result $result The result instance
     */
    protected $result;

    /**
     * A reference to the option instance.
     *
     * @var PEAR2\Console\CommandLine_Option $option The action option
     */
    protected $option;

    /**
     * A reference to the parser instance.
     *
     * @var PEAR2\Console\CommandLine $parser The parser
     */
    protected $parser;

    // }}}
    // __construct() {{{

    /**
     * Constructor
     *
     * @param PEAR2\Console\CommandLine_Result $result The result instance
     * @param PEAR2\Console\CommandLine_Option $option The action option
     * @param PEAR2\Console\CommandLine        $parser The current parser
     *
     * @return void
     */
    public function __construct($result, $option, $parser)
    {
        $this->result = $result;
        $this->option = $option;
        $this->parser = $parser;
    }

    // }}}
    // getResult() {{{

    /**
     * Convenience method to retrieve the value of result->options[name].
     *
     * @return mixed The result value or null
     */
    public function getResult()
    {
        if (isset($this->result->options[$this->option->name])) {
            return $this->result->options[$this->option->name];
        }
        return null;
    }

    // }}}
    // format() {{{

    /**
     * Allow a value to be pre-formatted prior to being used in a choices test.
     * Setting $value to the new format will keep the formatting.
     *
     * @param mixed &$value The value to format
     *
     * @return mixed The formatted value
     */
    public function format(&$value)
    {
        return $value;
    }

    // }}}
    // setResult() {{{

    /**
     * Convenience method to assign the result->options[name] value.
     *
     * @param mixed $result The result value
     *
     * @return void
     */
    public function setResult($result)
    {
        $this->result->options[$this->option->name] = $result;
    }

    // }}}
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     * All children actions must implement this method.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    abstract public function execute($value = false, $params = array());
    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Argument.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Class that represent a command line argument.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Argument extends Element
{
    // Public properties {{{

    /**
     * Setting this to true will tell the parser that the argument expects more
     * than one argument and that argument values should be stored in an array.
     *
     * @var boolean $multiple Whether the argument expects multiple values
     */
    public $multiple = false;

    /**
     * Setting this to true will tell the parser that the argument is optional
     * and can be ommited.
     * Note that it is not a good practice to make arguments optional, it is
     * the role of the options to be optional, by essence.
     *
     * @var boolean $optional Whether the argument is optional or not.
     */
    public $optional = false;

    // }}}
    // validate() {{{

    /**
     * Validates the argument instance.
     *
     * @return void
     * @throws PEAR2\Console\CommandLine\Exception
     *
     * @todo use exceptions
     */
    public function validate()
    {
        // check if the argument name is valid
        if (!preg_match(
            '/^[a-zA-Z_\x7f-\xff]+[a-zA-Z0-9_\x7f-\xff]*$/',
            $this->name
        )
        ) {
            \PEAR2\Console\CommandLine::triggerError(
                'argument_bad_name',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        if (!$this->optional && $this->default !== null) {
            \PEAR2\Console\CommandLine::triggerError(
                'argument_no_default',
                E_USER_ERROR
            );
        }
        parent::validate();
    }

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Command.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Class that represent a command with option and arguments.
 *
 * This class exist just to clarify the interface but at the moment it is
 * strictly identical to PEAR2\Console\CommandLine class, it could change in the
 * future though.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Command extends \PEAR2\Console\CommandLine
{
    // Public properties {{{

    /**
     * An array of aliases for the subcommand.
     *
     * @var array $aliases Aliases for the subcommand.
     */
    public $aliases = array();

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param array $params An optional array of parameters
     *
     * @return void
     */
    public function __construct($params = array())
    {
        if (isset($params['aliases'])) {
            $this->aliases = $params['aliases'];
        }
        parent::__construct($params);
    }

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\CustomMessageProvider.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @author    Michael Gauthier <mike@silverorange.com>
 * @copyright 2007 David JEAN LOUIS, 2009 silverorange
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   CVS: $Id: CustomMessageProvider.php 282427 2009-06-19 10:22:48Z izi $
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 1.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Common interfacefor message providers that allow overriding with custom
 * messages
 *
 * Message providers may optionally implement this interface.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @author    Michael Gauthier <mike@silverorange.com>
 * @copyright 2007 David JEAN LOUIS, 2009 silverorange
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Interface available since release 1.1.0
 */
interface CustomMessageProvider
{
    // getWithCustomMesssages() {{{

    /**
     * Retrieves the given string identifier corresponding message.
     *
     * For a list of identifiers please see the provided default message
     * provider.
     *
     * @param string $code     The string identifier of the message
     * @param array  $vars     An array of template variables
     * @param array  $messages An optional array of messages to use. Array
     *                         indexes are message codes.
     *
     * @return string
     *
     * @see PEAR2\Console\CommandLine_MessageProvider
     * @see PEAR2\Console\CommandLine_MessageProvider\DefaultProvider
     */
    public function getWithCustomMessages(
        $code, $vars = array(), $messages = array()
    );

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Element.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Class that represent a command line element (an option, or an argument).
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
abstract class Element
{
    // Public properties {{{

    /**
     * The element name.
     *
     * @var string $name Element name
     */
    public $name;

    /**
     * The name of variable displayed in the usage message, if no set it
     * defaults to the "name" property.
     *
     * @var string $help_name Element "help" variable name
     */
    public $help_name;

    /**
     * The element description.
     *
     * @var string $description Element description
     */
    public $description;
     /**
     * The default value of the element if not provided on the command line.
     *
     * @var mixed $default Default value of the option.
     */
    public $default;

    /**
     * Custom errors messages for this element
     *
     * This array is of the form:
     * <code>
     * <?php
     * array(
     *     $messageName => $messageText,
     *     $messageName => $messageText,
     *     ...
     * );
     * ?>
     * </code>
     *
     * If specified, these messages override the messages provided by the
     * default message provider. For example:
     * <code>
     * <?php
     * $messages = array(
     *     'ARGUMENT_REQUIRED' => 'The argument foo is required.',
     * );
     * ?>
     * </code>
     *
     * @var array
     * @see PEAR2\Console\CommandLine_MessageProvider\DefaultProvider
     */
    public $messages = array();

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param string $name   The name of the element
     * @param array  $params An optional array of parameters
     *
     * @return void
     */
    public function __construct($name = null, $params = array())
    {
        $this->name = $name;
        foreach ($params as $attr => $value) {
            if (property_exists($this, $attr)) {
                $this->$attr = $value;
            }
        }
    }

    // }}}
    // toString() {{{

    /**
     * Returns the string representation of the element.
     *
     * @return string The string representation of the element
     *
     * @todo use __toString() instead
     */
    public function toString()
    {
        return $this->help_name;
    }
    // }}}
    // validate() {{{

    /**
     * Validates the element instance and set it's default values.
     *
     * @return void
     * @throws PEAR2\Console\CommandLine\Exception
     */
    public function validate()
    {
        // if no help_name passed, default to name
        if ($this->help_name == null) {
            $this->help_name = $this->name;
        }
    }

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Exception.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

use Exception as E;

/**
 * Class for exceptions raised by the PEAR2\Console\CommandLine package.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Exception extends E
{
    // Codes constants {{{

    /**#@+
     * Exception code constants.
     */
    const OPTION_VALUE_REQUIRED   = 1;
    const OPTION_VALUE_UNEXPECTED = 2;
    const OPTION_VALUE_TYPE_ERROR = 3;
    const OPTION_UNKNOWN          = 4;
    const ARGUMENT_REQUIRED       = 5;
    const INVALID_SUBCOMMAND      = 6;
    /**#@-*/

    // }}}
    // factory() {{{

    /**
     * Convenience method that builds the exception with the array of params by
     * calling the message provider class.
     *
     * @param string                    $code     The string identifier of the
     *                                            exception.
     * @param array                     $params   Array of template vars/values
     * @param PEAR2\Console\CommandLine $parser   An instance of the parser
     * @param array                     $messages An optional array of messages
     *                                            passed to the message provider.
     *
     * @return PEAR2\Console\CommandLine\Exception The exception instance
     */
    public static function factory(
        $code, $params, $parser, array $messages = array()
    ) {
        $provider = $parser->message_provider;
        if ($provider instanceof CommandLine\CustomMessageProvider) {
            $msg = $provider->getWithCustomMessages(
                $code,
                $params,
                $messages
            );
        } else {
            $msg = $provider->get($code, $params);
        }
        $const = '\PEAR2\Console\CommandLine\Exception::' . $code;
        $code  = defined($const) ? constant($const) : 0;
        return new static($msg, $code);
    }

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\MessageProvider\DefaultProvider.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine\MessageProvider;

use PEAR2\Console\CommandLine\MessageProvider;
use PEAR2\Console\CommandLine\CustomMessageProvider;

/**
 * Lightweight class that manages messages used by PEAR2\Console\CommandLine package,
 * allowing the developper to customize these messages, for example to
 * internationalize a command line frontend.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class DefaultProvider
    implements MessageProvider,
    CustomMessageProvider
{
    // Properties {{{

    /**
     * Associative array of messages
     *
     * @var array $messages
     */
    protected $messages = array(
        'OPTION_VALUE_REQUIRED'   => 'Option "{$name}" requires a value.',
        'OPTION_VALUE_UNEXPECTED' => 'Option "{$name}" does not expect a value (got "{$value}").',
        'OPTION_VALUE_NOT_VALID'  => 'Option "{$name}" must be one of the following: "{$choices}" (got "{$value}").',
        'OPTION_VALUE_TYPE_ERROR' => 'Option "{$name}" requires a value of type {$type} (got "{$value}").',
        'OPTION_AMBIGUOUS'        => 'Ambiguous option "{$name}", can be one of the following: {$matches}.',
        'OPTION_UNKNOWN'          => 'Unknown option "{$name}".',
        'ARGUMENT_REQUIRED'       => 'You must provide at least {$argnum} argument{$plural}.',
        'PROG_HELP_LINE'          => 'Type "{$progname} --help" to get help.',
        'PROG_VERSION_LINE'       => '{$progname} version {$version}.',
        'COMMAND_HELP_LINE'       => 'Type "{$progname} <command> --help" to get help on specific command.',
        'USAGE_WORD'              => 'Usage',
        'OPTION_WORD'             => 'Options',
        'ARGUMENT_WORD'           => 'Arguments',
        'COMMAND_WORD'            => 'Commands',
        'PASSWORD_PROMPT'         => 'Password: ',
        'PASSWORD_PROMPT_ECHO'    => 'Password (warning: will echo): ',
        'INVALID_CUSTOM_INSTANCE' => 'Instance does not implement the required interface',
        'LIST_OPTION_MESSAGE'     => 'lists valid choices for option {$name}',
        'LIST_DISPLAYED_MESSAGE'  => 'Valid choices are: ',
        'INVALID_SUBCOMMAND'      => 'Command "{$command}" is not valid.',
        'SUBCOMMAND_REQUIRED'     => 'Please enter one of the following command: {$commands}.',
    );

    // }}}
    // get() {{{

    /**
     * Retrieve the given string identifier corresponding message.
     *
     * @param string $code The string identifier of the message
     * @param array  $vars An array of template variables
     *
     * @return string
     */
    public function get($code, $vars = array())
    {
        if (!isset($this->messages[$code])) {
            return 'UNKNOWN';
        }
        return $this->replaceTemplateVars($this->messages[$code], $vars);
    }

    // }}}
    // getWithCustomMessages() {{{

    /**
     * Retrieve the given string identifier corresponding message.
     *
     * @param string $code     The string identifier of the message
     * @param array  $vars     An array of template variables
     * @param array  $messages An optional array of messages to use. Array
     *                         indexes are message codes.
     *
     * @return string
     */
    public function getWithCustomMessages(
        $code, $vars = array(), $messages = array()
    ) {
        // get message
        if (isset($messages[$code])) {
            $message = $messages[$code];
        } elseif (isset($this->messages[$code])) {
            $message = $this->messages[$code];
        } else {
            $message = 'UNKNOWN';
        }
        return $this->replaceTemplateVars($message, $vars);
    }

    // }}}
    // replaceTemplateVars() {{{

    /**
     * Replaces template vars in a message
     *
     * @param string $message The message
     * @param array  $vars    An array of template variables
     *
     * @return string
     */
    protected function replaceTemplateVars($message, $vars = array())
    {
        $tmpkeys = array_keys($vars);
        $keys    = array();
        foreach ($tmpkeys as $key) {
            $keys[] = '{$' . $key . '}';
        }
        return str_replace($keys, array_values($vars), $message);
    }

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\MessageProvider.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Message providers common interface, all message providers must implement
 * this interface.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
interface MessageProvider
{
    // get() {{{

    /**
     * Retrieves the given string identifier corresponding message.
     * For a list of identifiers please see the provided default message
     * provider.
     *
     * @param string $code The string identifier of the message
     * @param array  $vars An array of template variables
     *
     * @return string
     *
     * @see PEAR2\Console\CommandLine\MessageProvider\DefaultProvider
     */
    public function get($code, $vars=array());

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Option.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

use PEAR2\Console;

/**
 * Class that represent a commandline option.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Option extends Element
{
    // Public properties {{{

    /**
     * The option short name (ex: -v).
     *
     * @var string $short_name Short name of the option
     */
    public $short_name;

    /**
     * The option long name (ex: --verbose).
     *
     * @var string $long_name Long name of the option
     */
    public $long_name;

    /**
     * The option action, defaults to "StoreString".
     *
     * @var string $action Option action
     */
    public $action = 'StoreString';

    /**
     * An array of possible values for the option. If this array is not empty
     * and the value passed is not in the array an exception is raised.
     * This only make sense for actions that accept values of course.
     *
     * @var array $choices Valid choices for the option
     */
    public $choices = array();

    /**
     * The callback function (or method) to call for an action of type
     * Callback, this can be any callable supported by the php function
     * call_user_func.
     *
     * Example:
     *
     * <code>
     * $parser->addOption('myoption', array(
     *     'short_name' => '-m',
     *     'long_name'  => '--myoption',
     *     'action'     => 'Callback',
     *     'callback'   => 'myCallbackFunction'
     * ));
     * </code>
     *
     * @var callable $callback The option callback
     */
    public $callback;

    /**
     * An associative array of additional params to pass to the class
     * corresponding to the action, this array will also be passed to the
     * callback defined for an action of type Callback, Example:
     *
     * <code>
     * // for a custom action
     * $parser->addOption('myoption', array(
     *     'short_name'    => '-m',
     *     'long_name'     => '--myoption',
     *     'action'        => 'MyCustomAction',
     *     'action_params' => array('foo'=>true, 'bar'=>false)
     * ));
     *
     * // if the user type:
     * // $ <yourprogram> -m spam
     * // in your MyCustomAction class the execute() method will be called
     * // with the value 'spam' as first parameter and
     * // array('foo'=>true, 'bar'=>false) as second parameter
     * </code>
     *
     * @var array $action_params Additional parameters to pass to the action
     */
    public $action_params = array();

    /**
     * For options that expect an argument, this property tells the parser if
     * the option argument is optional and can be ommited.
     *
     * @var bool $argumentOptional Whether the option arg is optional or not
     */
    public $argument_optional = false;

    /**
     * For options that uses the "choice" property only.
     * Adds a --list-<choice> option to the parser that displays the list of
     * choices for the option.
     *
     * @var bool $add_list_option Whether to add a list option or not
     */
    public $add_list_option = false;

    // }}}
    // Private properties {{{

    /**
     * When an action is called remember it to allow for multiple calls.
     *
     * @var object $action_instance Placeholder for action
     */
    private $_action_instance = null;

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param string $name   The name of the option
     * @param array  $params An optional array of parameters
     *
     * @return void
     */
    public function __construct($name = null, $params = array())
    {
        parent::__construct($name, $params);
        if ($this->action == 'Password') {
            // special case for Password action, password can be passed to the
            // commandline or prompted by the parser
            $this->argument_optional = true;
        }
    }

    // }}}
    // toString() {{{

    /**
     * Returns the string representation of the option.
     *
     * @param string $delim Delimiter to use between short and long option
     *
     * @return string The string representation of the option
     * 
     * @todo use __toString() instead
     */
    public function toString($delim = ", ")
    {
        $ret     = '';
        $padding = '';
        if ($this->short_name != null) {
            $ret .= $this->short_name;
            if ($this->expectsArgument()) {
                $ret .= ' ' . $this->help_name;
            }
            $padding = $delim;
        }
        if ($this->long_name != null) {
            $ret .= $padding . $this->long_name;
            if ($this->expectsArgument()) {
                $ret .= '=' . $this->help_name;
            }
        }
        return $ret;
    }

    // }}}
    // expectsArgument() {{{

    /**
     * Returns true if the option requires one or more argument and false
     * otherwise.
     *
     * @return bool Whether the option expects an argument or not
     */
    public function expectsArgument()
    {
        if ($this->action == 'StoreTrue'
            || $this->action == 'StoreFalse'
            || $this->action == 'Help'
            || $this->action == 'Version'
            || $this->action == 'Counter'
            || $this->action == 'List'
        ) {
            return false;
        }
        return true;
    }

    // }}}
    // dispatchAction() {{{

    /**
     * Formats the value $value according to the action of the option and
     * updates the passed PEAR2\Console\CommandLine_Result object.
     *
     * @param mixed                            $value  The value to format
     * @param PEAR2\Console\CommandLine_Result $result The result instance
     * @param PEAR2\Console\CommandLine        $parser The parser instance
     *
     * @return void
     * @throws PEAR2\Console\CommandLine\Exception
     */
    public function dispatchAction($value, $result, $parser)
    {
        $actionInfo = Console\CommandLine::$actions[$this->action];
        $clsname    = $actionInfo[0];
        if ($this->_action_instance === null) {
            $this->_action_instance  = new $clsname($result, $this, $parser);
        }

        // check value is in option choices
        if (!empty($this->choices)
            && !in_array(
                $this->_action_instance->format($value),
                $this->choices
            )
        ) {
            throw Console\CommandLine\Exception::factory(
                'OPTION_VALUE_NOT_VALID',
                array(
                    'name'    => $this->name,
                    'choices' => implode('", "', $this->choices),
                    'value'   => $value,
                ),
                $parser,
                $this->messages
            );
        }
        $this->_action_instance->execute($value, $this->action_params);
    }

    // }}}
    // validate() {{{

    /**
     * Validates the option instance.
     *
     * @return void
     * @throws PEAR2\Console\CommandLine\Exception
     * 
     * @todo use exceptions instead
     */
    public function validate()
    {
        // check if the option name is valid
        if (!preg_match(
            '/^[a-zA-Z_\x7f-\xff]+[a-zA-Z0-9_\x7f-\xff]*$/',
            $this->name
        )
        ) {
            Console\CommandLine::triggerError(
                'option_bad_name',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        // call the parent validate method
        parent::validate();
        // a short_name or a long_name must be provided
        if ($this->short_name == null && $this->long_name == null) {
            Console\CommandLine::triggerError(
                'option_long_and_short_name_missing',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        // check if the option short_name is valid
        if ($this->short_name != null
            && !(preg_match('/^\-[a-zA-Z]{1}$/', $this->short_name))
        ) {
            Console\CommandLine::triggerError(
                'option_bad_short_name',
                E_USER_ERROR,
                array(
                    '{$name}' => $this->name,
                    '{$short_name}' => $this->short_name
                )
            );
        }
        // check if the option long_name is valid
        if ($this->long_name != null
            && !preg_match('/^\-\-[a-zA-Z]+[a-zA-Z0-9_\-]*$/', $this->long_name)
        ) {
            Console\CommandLine::triggerError(
                'option_bad_long_name',
                E_USER_ERROR,
                array(
                    '{$name}' => $this->name,
                    '{$long_name}' => $this->long_name
                )
            );
        }
        // check if we have a valid action
        if (!is_string($this->action)) {
            Console\CommandLine::triggerError(
                'option_bad_action',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        if (!isset(Console\CommandLine::$actions[$this->action])) {
            Console\CommandLine::triggerError(
                'option_unregistered_action',
                E_USER_ERROR,
                array(
                    '{$action}' => $this->action,
                    '{$name}' => $this->name
                )
            );
        }
        // if the action is a callback, check that we have a valid callback
        if ($this->action == 'Callback' && !is_callable($this->callback)) {
            Console\CommandLine::triggerError(
                'option_invalid_callback',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
    }

    // }}}
    // setDefaults() {{{

    /**
     * Set the default value according to the configured action.
     *
     * Note that for backward compatibility issues this method is only called
     * when the 'force_options_defaults' is set to true, it will become the
     * default behaviour in the next major release of PEAR2\Console\CommandLine.
     *
     * @return void
     */
    public function setDefaults()
    {
        if ($this->default !== null) {
            // already set
            return;
        }
        switch ($this->action) {
        case 'Counter':
        case 'StoreInt':
            $this->default = 0;
            break;
        case 'StoreFloat':
            $this->default = 0.0;
            break;
        case 'StoreArray':
            $this->default = array();
            break;
        case 'StoreTrue':
            $this->default = false;
            break;
        case 'StoreFalse':
            $this->default = true;
            break;
        default:
            return;
        }
    }

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Outputter\Default.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * PEAR2\Console\CommandLine default Outputter.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Outputter_Default implements Outputter
{
    // stdout() {{{

    /**
     * Writes the message $msg to STDOUT.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stdout($msg)
    {
        if (defined('STDOUT')) {
            fwrite(STDOUT, $msg);
        } else {
            echo $msg;
        }
    }

    // }}}
    // stderr() {{{

    /**
     * Writes the message $msg to STDERR.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stderr($msg)
    {
        if (defined('STDERR')) {
            fwrite(STDERR, $msg);
        } else {
            echo $msg;
        }
    }

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Outputter.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Outputters common interface, all outputters must implement this interface.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
interface Outputter
{
    // stdout() {{{

    /**
     * Processes the output for a message that should be displayed on STDOUT.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stdout($msg);

    // }}}
    // stderr() {{{

    /**
     * Processes the output for a message that should be displayed on STDERR.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stderr($msg);

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Renderer\Default.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 */

namespace PEAR2\Console\CommandLine;

/**
 * PEAR2\Console\CommandLine default renderer.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Renderer_Default implements Renderer
{
    // Properties {{{

    /**
     * Integer that define the max width of the help text.
     *
     * @var integer $line_width Line width
     */
    public $line_width = 75;

    /**
     * Integer that define the max width of the help text.
     *
     * @var integer $line_width Line width
     */
    public $options_on_different_lines = false;

    /**
     * An instance of PEAR2\Console\CommandLine.
     *
     * @var PEAR2\Console\CommandLine $parser The parser
     */
    public $parser = false;

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param object $parser A PEAR2\Console\CommandLine instance
     *
     * @return void
     */
    public function __construct($parser = false)
    {
        $this->parser = $parser;
    }

    // }}}
    // usage() {{{

    /**
     * Returns the full usage message.
     *
     * @return string The usage message
     */
    public function usage()
    {
        $ret = '';
        if (!empty($this->parser->description)) {
            $ret .= $this->description() . "\n\n";
        }
        $ret .= $this->usageLine() . "\n";
        if (count($this->parser->commands) > 0) {
            $ret .= $this->commandUsageLine() . "\n";
        }
        if (count($this->parser->options) > 0) {
            $ret .= "\n" . $this->optionList() . "\n";
        }
        if (count($this->parser->args) > 0) {
            $ret .= "\n" . $this->argumentList() . "\n";
        }
        if (count($this->parser->commands) > 0) {
            $ret .= "\n" . $this->commandList() . "\n";
        }
        $ret .= "\n";
        return $ret;
    }
    // }}}
    // error() {{{

    /**
     * Returns a formatted error message.
     *
     * @param string $error The error message to format
     *
     * @return string The error string
     */
    public function error($error)
    {
        $ret = 'Error: ' . $error . "\n";
        if ($this->parser->add_help_option) {
            $name = $this->name();
            $ret .= $this->wrap(
                $this->parser->message_provider->get(
                    'PROG_HELP_LINE',
                    array('progname' => $name)
                )
            ) . "\n";
            if (count($this->parser->commands) > 0) {
                $ret .= $this->wrap(
                    $this->parser->message_provider->get(
                        'COMMAND_HELP_LINE',
                        array('progname' => $name)
                    )
                ) . "\n";
            }
        }
        return $ret;
    }

    // }}}
    // version() {{{

    /**
     * Returns the program version string.
     *
     * @return string The version string
     */
    public function version()
    {
        return $this->parser->message_provider->get(
            'PROG_VERSION_LINE',
            array(
                'progname' => $this->name(),
                'version'  => $this->parser->version
            )
        ) . "\n";
    }

    // }}}
    // name() {{{

    /**
     * Returns the full name of the program or the sub command
     *
     * @return string The name of the program
     */
    protected function name()
    {
        $name   = $this->parser->name;
        $parent = $this->parser->parent;
        while ($parent) {
            if (count($parent->options) > 0) {
                $name = '['
                    . strtolower(
                        $this->parser->message_provider->get(
                            'OPTION_WORD',
                            array('plural' => 's')
                        )
                    ) . '] ' . $name;
            }
            $name = $parent->name . ' ' . $name;
            $parent = $parent->parent;
        }
        return $this->wrap($name);
    }

    // }}}
    // description() {{{

    /**
     * Returns the command line description message.
     *
     * @return string The description message
     */
    protected function description()
    {
        return $this->wrap($this->parser->description);
    }

    // }}}
    // usageLine() {{{

    /**
     * Returns the command line usage message
     *
     * @return string the usage message
     */
    protected function usageLine()
    {
        $usage = $this->parser->message_provider->get('USAGE_WORD') . ":\n";
        $ret   = $usage . '  ' . $this->name();
        if (count($this->parser->options) > 0) {
            $ret .= ' ['
                . strtolower($this->parser->message_provider->get('OPTION_WORD'))
                . ']';
        }
        if (count($this->parser->args) > 0) {
            foreach ($this->parser->args as $name=>$arg) {
                $arg_str = $arg->help_name;
                if ($arg->multiple) {
                    $arg_str .= '1 ' . $arg->help_name . '2 ...';
                }
                if ($arg->optional) {
                    $arg_str = '[' . $arg_str . ']';
                }
                $ret .= ' ' . $arg_str;
            }
        }
        return $this->columnWrap($ret, 2);
    }

    // }}}
    // commandUsageLine() {{{

    /**
     * Returns the command line usage message for subcommands.
     *
     * @return string The usage line
     */
    protected function commandUsageLine()
    {
        if (count($this->parser->commands) == 0) {
            return '';
        }
        $ret = '  ' . $this->name();
        if (count($this->parser->options) > 0) {
            $ret .= ' ['
                . strtolower($this->parser->message_provider->get('OPTION_WORD'))
                . ']';
        }
        $ret       .= " <command>";
        $hasArgs    = false;
        $hasOptions = false;
        foreach ($this->parser->commands as $command) {
            if (!$hasArgs && count($command->args) > 0) {
                $hasArgs = true;
            }
            if (!$hasOptions && ($command->add_help_option
                || $command->add_version_option
                || count($command->options) > 0)
            ) {
                $hasOptions = true;
            }
        }
        if ($hasOptions) {
            $ret .= ' [options]';
        }
        if ($hasArgs) {
            $ret .= ' [args]';
        }
        return $this->columnWrap($ret, 2);
    }

    // }}}
    // argumentList() {{{

    /**
     * Render the arguments list that will be displayed to the user, you can
     * override this method if you want to change the look of the list.
     *
     * @return string The formatted argument list
     */
    protected function argumentList()
    {
        $col  = 0;
        $args = array();
        foreach ($this->parser->args as $arg) {
            $argstr = '  ' . $arg->toString();
            $args[] = array($argstr, $arg->description);
            $ln     = strlen($argstr);
            if ($col < $ln) {
                $col = $ln;
            }
        }
        $ret = $this->parser->message_provider->get('ARGUMENT_WORD') . ":";
        foreach ($args as $arg) {
            $text = str_pad($arg[0], $col) . '  ' . $arg[1];
            $ret .= "\n" . $this->columnWrap($text, $col+2);
        }
        return $ret;
    }

    // }}}
    // optionList() {{{

    /**
     * Render the options list that will be displayed to the user, you can
     * override this method if you want to change the look of the list.
     *
     * @return string The formatted option list
     */
    protected function optionList()
    {
        $col     = 0;
        $options = array();
        foreach ($this->parser->options as $option) {
            $delim    = $this->options_on_different_lines ? "\n" : ', ';
            $optstr   = $option->toString($delim);
            $lines    = explode("\n", $optstr);
            $lines[0] = '  ' . $lines[0];
            if (count($lines) > 1) {
                $lines[1] = '  ' . $lines[1];
                $ln       = strlen($lines[1]);
            } else {
                $ln = strlen($lines[0]);
            }
            $options[] = array($lines, $option->description);
            if ($col < $ln) {
                $col = $ln;
            }
        }
        $ret = $this->parser->message_provider->get('OPTION_WORD') . ":";
        foreach ($options as $option) {
            if (count($option[0]) > 1) {
                $text = str_pad($option[0][1], $col) . '  ' . $option[1];
                $pre  = $option[0][0] . "\n";
            } else {
                $text = str_pad($option[0][0], $col) . '  ' . $option[1];
                $pre  = '';
            }
            $ret .= "\n" . $pre . $this->columnWrap($text, $col+2);
        }
        return $ret;
    }

    // }}}
    // commandList() {{{

    /**
     * Render the command list that will be displayed to the user, you can
     * override this method if you want to change the look of the list.
     *
     * @return string The formatted subcommand list
     */
    protected function commandList()
    {

        $commands = array();
        $col      = 0;
        foreach ($this->parser->commands as $cmdname=>$command) {
            $cmdname    = '  ' . $cmdname;
            $commands[] = array($cmdname, $command->description, $command->aliases);
            $ln         = strlen($cmdname);
            if ($col < $ln) {
                $col = $ln;
            }
        }
        $ret = $this->parser->message_provider->get('COMMAND_WORD') . ":";
        foreach ($commands as $command) {
            $text = str_pad($command[0], $col) . '  ' . $command[1];
            if ($aliasesCount = count($command[2])) {
                $pad = '';
                $text .= ' (';
                $text .= $aliasesCount > 1 ? 'aliases: ' : 'alias: ';
                foreach ($command[2] as $alias) {
                    $text .= $pad . $alias;
                    $pad   = ', ';
                }
                $text .= ')';
            }
            $ret .= "\n" . $this->columnWrap($text, $col+2);
        }
        return $ret;
    }

    // }}}
    // wrap() {{{

    /**
     * Wraps the text passed to the method.
     *
     * @param string $text The text to wrap
     * @param int    $lw   The column width (defaults to line_width property)
     *
     * @return string The wrapped text
     */
    protected function wrap($text, $lw=null)
    {
        if ($this->line_width > 0) {
            if ($lw === null) {
                $lw = $this->line_width;
            }
            return wordwrap($text, $lw, "\n", false);
        }
        return $text;
    }

    // }}}
    // columnWrap() {{{

    /**
     * Wraps the text passed to the method at the specified width.
     *
     * @param string $text The text to wrap
     * @param int    $cw   The wrap width
     *
     * @return string The wrapped text
     */
    protected function columnWrap($text, $cw)
    {
        $tokens = explode("\n", $this->wrap($text));
        $ret    = $tokens[0];
        $text   = trim(substr($text, strlen($ret)));
        if (empty($text)) {
            return $ret;
        }

        $chunks = $this->wrap($text, $this->line_width - $cw);
        $tokens = explode("\n", $chunks);
        foreach ($tokens as $token) {
            if (!empty($token)) {
                $ret .= "\n" . str_repeat(' ', $cw) . $token;
            } else {
                $ret .= "\n";
            }
        }
        return $ret;
    }

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Renderer.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Renderers common interface, all renderers must implement this interface.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
interface Renderer
{
    // usage() {{{

    /**
     * Returns the full usage message.
     *
     * @return string The usage message
     */
    public function usage();

    // }}}
    // error() {{{

    /**
     * Returns a formatted error message.
     *
     * @param string $error The error message to format
     *
     * @return string The error string
     */
    public function error($error);

    // }}}
    // version() {{{

    /**
     * Returns the program version string.
     *
     * @return string The version string
     */
    public function version();

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\Result.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * A lightweight class to store the result of the command line parsing.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Result
{
    // Public properties {{{

    /**
     * The result options associative array.
     * Key is the name of the option and value its value.
     *
     * @var array $options Result options array
     */
    public $options = array();

    /**
     * The result arguments array.
     *
     * @var array $args Result arguments array
     */
    public $args = array();

    /**
     * Name of the command invoked by the user, false if no command invoked.
     *
     * @var string $command_name Result command name
     */
    public $command_name = false;

    /**
     * A result instance for the subcommand.
     *
     * @var static $command Result instance for the subcommand
     */
    public $command = false;

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine\XmlParser.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 *
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

use PEAR2\Console\CommandLine;
use DOMDocument;
use DOMNode;
use Phar;

/**
 * Parser for command line xml definitions.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class XmlParser
{
    // parse() {{{

    /**
     * Parses the given xml definition file and returns a
     * PEAR2\Console\CommandLine instance constructed with the xml data.
     *
     * @param string $xmlfile The xml file to parse
     *
     * @return PEAR2\Console\CommandLine A parser instance
     */
    public static function parse($xmlfile)
    {
        if (!is_readable($xmlfile)) {
            CommandLine::triggerError(
                'invalid_xml_file',
                E_USER_ERROR,
                array('{$file}' => $xmlfile)
            );
        }
        $doc = new DOMDocument();
        $doc->load($xmlfile);
        self::validate($doc);
        $nodes = $doc->getElementsByTagName('command');
        $root  = $nodes->item(0);
        return self::_parseCommandNode($root, true);
    }

    // }}}
    // parseString() {{{

    /**
     * Parses the given xml definition string and returns a
     * PEAR2\Console\CommandLine instance constructed with the xml data.
     *
     * @param string $xmlstr The xml string to parse
     *
     * @return PEAR2\Console\CommandLine A parser instance
     */
    public static function parseString($xmlstr)
    {
        $doc = new DOMDocument();
        $doc->loadXml($xmlstr);
        self::validate($doc);
        $nodes = $doc->getElementsByTagName('command');
        $root  = $nodes->item(0);
        return self::_parseCommandNode($root, true);
    }

    // }}}
    // validate() {{{

    /**
     * Validates the xml definition using Relax NG.
     *
     * @param DOMDocument $doc The document to validate
     *
     * @return boolean Whether the xml data is valid or not.
     * @throws PEAR2\Console\CommandLine\Exception
     *
     * @todo use exceptions only
     */
    public static function validate(DOMDocument $doc)
    {
        $paths = array();
        if (!class_exists('Phar', false) || !Phar::running()) {
            // Pyrus
            $paths[]
                = '@data_dir@/pear2.php.net/PEAR2_Console_CommandLine/xmlschema.rng';
            // PEAR
            $pearDataDirEnv = getenv('PHP_PEAR_DATA_DIR');
            if ($pearDataDirEnv) {
                $paths[] = $pearDataDirEnv .
                    '/PEAR2_Console_CommandLine/xmlschema.rng';
            }
            $paths[] = '@data_dir@/PEAR2_Console_CommandLine/xmlschema.rng';
        }
        $pkgData  = __DIR__ . '/../../../../data/';
        // PHAR dep
        $paths[] = $pkgData .
            'pear2.php.net/PEAR2_Console_CommandLine/xmlschema.rng';
        $paths[] = $pkgData . 'PEAR2_Console_CommandLine/xmlschema.rng';
        $paths[] = $pkgData . 'pear2/console_commandline/xmlschema.rng';
        // Git/Composer
        $paths[] = $pkgData . 'xmlschema.rng';
        $paths[] = 'xmlschema.rng';

        foreach ($paths as $path) {
            if (is_readable($path)) {
                return $doc->relaxNGValidate($path);
            }
        }
        CommandLine::triggerError(
            'invalid_xml_file',
            E_USER_ERROR,
            array('{$file}' => $path)
        );
    }

    // }}}
    // _parseCommandNode() {{{

    /**
     * Parses the root command node or a command node and returns the
     * constructed PEAR2\Console\CommandLine or PEAR2\Console\CommandLine_Command
     * instance.
     *
     * @param DOMNode $node       The node to parse
     * @param bool    $isRootNode Whether it is a root node or not
     *
     * @return CommandLine|CommandLine\Command An instance of CommandLine for
     *     root node, CommandLine\Command otherwise.
     */
    private static function _parseCommandNode(DOMNode $node, $isRootNode = false)
    {
        if ($isRootNode) {
            $obj = new CommandLine();
        } else {
            $obj = new CommandLine\Command();
        }
        foreach ($node->childNodes as $cNode) {
            $cNodeName = $cNode->nodeName;
            switch ($cNodeName) {
            case 'name':
            case 'description':
            case 'version':
                $obj->$cNodeName = trim($cNode->nodeValue);
                break;
            case 'add_help_option':
            case 'add_version_option':
            case 'force_posix':
                $obj->$cNodeName = self::_bool(trim($cNode->nodeValue));
                break;
            case 'option':
                $obj->addOption(self::_parseOptionNode($cNode));
                break;
            case 'argument':
                $obj->addArgument(self::_parseArgumentNode($cNode));
                break;
            case 'command':
                $obj->addCommand(self::_parseCommandNode($cNode));
                break;
            case 'aliases':
                if (!$isRootNode) {
                    foreach ($cNode->childNodes as $subChildNode) {
                        if ($subChildNode->nodeName == 'alias') {
                            $obj->aliases[] = trim($subChildNode->nodeValue);
                        }
                    }
                }
                break;
            case 'messages':
                $obj->messages = self::_messages($cNode);
                break;
            default:
                break;
            }
        }
        return $obj;
    }

    // }}}
    // _parseOptionNode() {{{

    /**
     * Parses an option node and returns the constructed
     * PEAR2\Console\CommandLine_Option instance.
     *
     * @param DOMNode $node The node to parse
     *
     * @return PEAR2\Console\CommandLine\Option The built option
     */
    private static function _parseOptionNode(DOMNode $node)
    {
        $obj = new CommandLine\Option($node->getAttribute('name'));
        foreach ($node->childNodes as $cNode) {
            $cNodeName = $cNode->nodeName;
            switch ($cNodeName) {
            case 'choices':
                foreach ($cNode->childNodes as $subChildNode) {
                    if ($subChildNode->nodeName == 'choice') {
                        $obj->choices[] = trim($subChildNode->nodeValue);
                    }
                }
                break;
            case 'messages':
                $obj->messages = self::_messages($cNode);
                break;
            default:
                if (property_exists($obj, $cNodeName)) {
                    $obj->$cNodeName = trim($cNode->nodeValue);
                }
                break;
            }
        }
        if ($obj->action == 'Password') {
            $obj->argument_optional = true;
        }
        return $obj;
    }

    // }}}
    // _parseArgumentNode() {{{

    /**
     * Parses an argument node and returns the constructed
     * PEAR2\Console\CommandLine_Argument instance.
     *
     * @param DOMNode $node The node to parse
     *
     * @return PEAR2\Console\CommandLine\Argument The built argument
     */
    private static function _parseArgumentNode(DOMNode $node)
    {
        $obj = new CommandLine\Argument($node->getAttribute('name'));
        foreach ($node->childNodes as $cNode) {
            $cNodeName = $cNode->nodeName;
            switch ($cNodeName) {
            case 'description':
            case 'help_name':
            case 'default':
                $obj->$cNodeName = trim($cNode->nodeValue);
                break;
            case 'multiple':
                $obj->multiple = self::_bool(trim($cNode->nodeValue));
                break;
            case 'optional':
                $obj->optional = self::_bool(trim($cNode->nodeValue));
                break;
            case 'messages':
                $obj->messages = self::_messages($cNode);
                break;
            default:
                break;
            }
        }
        return $obj;
    }

    // }}}
    // _bool() {{{

    /**
     * Returns a boolean according to true/false possible strings.
     *
     * @param string $str The string to process
     *
     * @return boolean
     */
    private static function _bool($str)
    {
        return in_array((string)$str, array('true', '1', 'on', 'yes'));
    }

    // }}}
    // _messages() {{{

    /**
     * Returns an array of custom messages for the element
     *
     * @param DOMNode $node The messages node to process
     *
     * @return array an array of messages
     *
     * @see PEAR2\Console\CommandLine::$messages
     * @see PEAR2\Console\CommandLine_Element::$messages
     */
    private static function _messages(DOMNode $node)
    {
        $messages = array();

        foreach ($node->childNodes as $cNode) {
            if ($cNode->nodeType == XML_ELEMENT_NODE) {
                $name  = $cNode->getAttribute('name');
                $value = trim($cNode->nodeValue);

                $messages[$name] = $value;
            }
        }

        return $messages;
    }

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\src\PEAR2\Console\CommandLine.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * A full featured package for managing command-line options and arguments
 * hightly inspired from python optparse module, it allows the developper to
 * easily build complex command line interfaces.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
namespace PEAR2\Console;

/**
 * Main class for parsing command line options and arguments.
 *
 * There are three ways to create parsers with this class:
 * <code>
 * // direct usage
 * $parser = new PEAR2\Console\CommandLine();
 *
 * // with an xml definition file
 * $parser = PEAR2\Console\CommandLine::fromXmlFile('path/to/file.xml');
 *
 * // with an xml definition string
 * $validXmlString = '..your xml string...';
 * $parser = PEAR2\Console\CommandLine::fromXmlString($validXmlString);
 * </code>
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @example   docs/examples/ex1.php
 * @example   docs/examples/ex2.php
 */
class CommandLine
{
    // Public properties {{{

    /**
     * Error messages.
     *
     * @var array $errors Error messages
     *
     * @todo move this to PEAR2\Console\CommandLine\MessageProvider
     */
    public static $errors = array(
        'option_bad_name'                    => 'option name must be a valid php variable name (got: {$name})',
        'argument_bad_name'                  => 'argument name must be a valid php variable name (got: {$name})',
        'argument_no_default'                => 'only optional arguments can have a default value',
        'option_long_and_short_name_missing' => 'you must provide at least an option short name or long name for option "{$name}"',
        'option_bad_short_name'              => 'option "{$name}" short name must be a dash followed by a letter (got: "{$short_name}")',
        'option_bad_long_name'               => 'option "{$name}" long name must be 2 dashes followed by a word (got: "{$long_name}")',
        'option_unregistered_action'         => 'unregistered action "{$action}" for option "{$name}".',
        'option_bad_action'                  => 'invalid action for option "{$name}".',
        'option_invalid_callback'            => 'you must provide a valid callback for option "{$name}"',
        'action_class_does_not_exists'       => 'action "{$name}" class "{$class}" not found, make sure that your class is available before calling PEAR2\Console\CommandLine::registerAction()',
        'invalid_xml_file'                   => 'XML definition file "{$file}" does not exists or is not readable',
        'invalid_rng_file'                   => 'RNG file "{$file}" does not exists or is not readable'
    );

    /**
     * The name of the program, if not given it defaults to argv[0].
     *
     * @var string $name Name of your program
     */
    public $name;

    /**
     * A description text that will be displayed in the help message.
     *
     * @var string $description Description of your program
     */
    public $description = '';

    /**
     * A string that represents the version of the program, if this property is
     * not empty and property add_version_option is not set to false, the
     * command line parser will add a --version option, that will display the
     * property content.
     *
     * @var    string $version
     * @access public
     */
    public $version = '';

    /**
     * Boolean that determine if the command line parser should add the help
     * (-h, --help) option automatically.
     *
     * @var bool $add_help_option Whether to add a help option or not
     */
    public $add_help_option = true;

    /**
     * Boolean that determine if the command line parser should add the version
     * (-v, --version) option automatically.
     * Note that the version option is also generated only if the version
     * property is not empty, it's up to you to provide a version string of
     * course.
     *
     * @var bool $add_version_option Whether to add a version option or not
     */
    public $add_version_option = true;

    /**
     * Boolean that determine if providing a subcommand is mandatory.
     *
     * @var bool $subcommand_required Whether a subcommand is required or not
     */
    public $subcommand_required = false;

    /**
     * The command line parser renderer instance.
     *
     * @var PEAR2\Console\CommandLine\Renderer a renderer
     */
    public $renderer = false;

    /**
     * The command line parser outputter instance.
     *
     * @var PEAR2\Console\CommandLine\Outputter An outputter
     */
    public $outputter = false;

    /**
     * The command line message provider instance.
     *
     * @var PEAR2\Console\CommandLine\MessageProvider A message provider
     */
    public $message_provider = false;

    /**
     * Boolean that tells the parser to be POSIX compliant, POSIX demands the
     * following behavior: the first non-option stops option processing.
     *
     * @var bool $force_posix Whether to force posix compliance or not
     */
    public $force_posix = false;

    /**
     * Boolean that tells the parser to set relevant options default values,
     * according to the option action.
     *
     * @see PEAR2\Console\CommandLine\Option::setDefaults()
     * @var bool $force_options_defaults Whether to force option default values
     */
    public $force_options_defaults = false;

    /**
     * An array of PEAR2\Console\CommandLine\Option objects.
     *
     * @var array $options The options array
     */
    public $options = array();

    /**
     * An array of PEAR2\Console\CommandLine\Argument objects.
     *
     * @var array $args The arguments array
     */
    public $args = array();

    /**
     * An array of PEAR2\Console\CommandLine\Command objects (sub commands).
     *
     * @var array $commands The commands array
     */
    public $commands = array();

    /**
     * Parent, only relevant in Command objects but left here for interface
     * convenience.
     *
     * @var PEAR2\Console\CommandLine The parent instance
     * 
     * @todo move CommandLine::parent to CommandLine\Command
     */
    public $parent = false;

    /**
     * Array of valid actions for an option, this array will also store user
     * registered actions.
     *
     * The array format is:
     * <pre>
     * array(
     *     <ActionName:string> => array(<ActionClass:string>, <builtin:bool>)
     * )
     * </pre>
     *
     * @var array $actions List of valid actions
     */
    public static $actions = array(
        'StoreTrue'   => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreTrue', true
        ),
        'StoreFalse'  => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreFalse', true
        ),
        'StoreString' => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreString', true
        ),
        'StoreInt'    => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreInt', true
        ),
        'StoreFloat'  => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreFloat', true
        ),
        'StoreArray'  => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreArray', true
        ),
        'Callback'    => array(
            'PEAR2\\Console\\CommandLine\\Action\\Callback', true
        ),
        'Counter'     => array(
            'PEAR2\\Console\\CommandLine\\Action\\Counter', true
        ),
        'Help'        => array(
            'PEAR2\\Console\\CommandLine\\Action\\Help', true
        ),
        'Version'     => array(
            'PEAR2\\Console\\CommandLine\\Action\\Version', true
        ),
        'Password'    => array(
            'PEAR2\\Console\\CommandLine\\Action\\Password', true
        ),
        'List'        => array(
            'PEAR2\\Console\\CommandLine\\Action_List', true
        ),
    );

    /**
     * Custom errors messages for this command
     *
     * This array is of the form:
     * <code>
     * <?php
     * array(
     *     $messageName => $messageText,
     *     $messageName => $messageText,
     *     ...
     * );
     * ?>
     * </code>
     *
     * If specified, these messages override the messages provided by the
     * default message provider. For example:
     * <code>
     * <?php
     * $messages = array(
     *     'ARGUMENT_REQUIRED' => 'The argument foo is required.',
     * );
     * ?>
     * </code>
     *
     * @var array
     * @see PEAR2\Console\CommandLine\MessageProvider\DefaultProvider
     */
    public $messages = array();

    // }}}
    // {{{ Private properties

    /**
     * Array of options that must be dispatched at the end.
     *
     * @var array $_dispatchLater Options to be dispatched
     */
    private $_dispatchLater = array();

    private $_lastopt = false;
    private $_stopflag = false;

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     * Example:
     *
     * <code>
     * $parser = new PEAR2\Console\CommandLine(array(
     *     'name'               => 'yourprogram', // defaults to argv[0]
     *     'description'        => 'Description of your program',
     *     'version'            => '0.0.1', // your program version
     *     'add_help_option'    => true, // or false to disable --help option
     *     'add_version_option' => true, // or false to disable --version option
     *     'force_posix'        => false // or true to force posix compliance
     * ));
     * </code>
     *
     * @param array $params An optional array of parameters
     *
     * @return void
     */
    public function __construct(array $params = array())
    {
        if (isset($params['name'])) {
            $this->name = $params['name'];
        } else if (isset($argv) && count($argv) > 0) {
            $this->name = $argv[0];
        } else if (isset($_SERVER['argv']) && count($_SERVER['argv']) > 0) {
            $this->name = $_SERVER['argv'][0];
        } else if (isset($_SERVER['SCRIPT_NAME'])) {
            $this->name = basename($_SERVER['SCRIPT_NAME']);
        }
        if (isset($params['description'])) {
            $this->description = $params['description'];
        }
        if (isset($params['version'])) {
            $this->version = $params['version'];
        }
        if (isset($params['add_version_option'])) {
            $this->add_version_option = $params['add_version_option'];
        }
        if (isset($params['add_help_option'])) {
            $this->add_help_option = $params['add_help_option'];
        }
        if (isset($params['subcommand_required'])) {
            $this->subcommand_required = $params['subcommand_required'];
        }
        if (isset($params['force_posix'])) {
            $this->force_posix = $params['force_posix'];
        } else if (getenv('POSIXLY_CORRECT')) {
            $this->force_posix = true;
        }
        if (isset($params['messages']) && is_array($params['messages'])) {
            $this->messages = $params['messages'];
        }
        // set default instances
        $this->renderer         = new CommandLine\Renderer_Default($this);
        $this->outputter        = new CommandLine\Outputter_Default();
        $this->message_provider = new CommandLine\MessageProvider\DefaultProvider();
    }

    // }}}
    // accept() {{{

    /**
     * Method to allow PEAR2\Console\CommandLine to accept either:
     *  + a custom renderer,
     *  + a custom outputter,
     *  + or a custom message provider
     *
     * @param mixed $instance The custom instance
     *
     * @return void
     * @throws PEAR2\Console\CommandLine\Exception if wrong argument passed
     */
    public function accept($instance)
    {
        if ($instance instanceof CommandLine\Renderer) {
            if (property_exists($instance, 'parser') && !$instance->parser) {
                $instance->parser = $this;
            }
            $this->renderer = $instance;
        } else if ($instance instanceof CommandLine\Outputter) {
            $this->outputter = $instance;
        } else if ($instance instanceof CommandLine\MessageProvider) {
            $this->message_provider = $instance;
        } else {
            throw CommandLine\Exception::factory(
                'INVALID_CUSTOM_INSTANCE',
                array(),
                $this,
                $this->messages
            );
        }
    }

    // }}}
    // fromXmlFile() {{{

    /**
     * Returns a command line parser instance built from an xml file.
     *
     * Example:
     * <code>
     * $parser = PEAR2\Console\CommandLine::fromXmlFile('path/to/file.xml');
     * $result = $parser->parse();
     * </code>
     *
     * @param string $file Path to the xml file
     *
     * @return PEAR2\Console\CommandLine The parser instance
     */
    public static function fromXmlFile($file)
    {
        return CommandLine\XmlParser::parse($file);
    }

    // }}}
    // fromXmlString() {{{

    /**
     * Returns a command line parser instance built from an xml string.
     *
     * Example:
     * <code>
     * $xmldata = '<?xml version="1.0" encoding="utf-8" standalone="yes"?>
     * <command>
     *   <description>Compress files</description>
     *   <option name="quiet">
     *     <short_name>-q</short_name>
     *     <long_name>--quiet</long_name>
     *     <description>be quiet when run</description>
     *     <action>StoreTrue/action>
     *   </option>
     *   <argument name="files">
     *     <description>a list of files</description>
     *     <multiple>true</multiple>
     *   </argument>
     * </command>';
     * $parser = PEAR2\Console\CommandLine::fromXmlString($xmldata);
     * $result = $parser->parse();
     * </code>
     *
     * @param string $string The xml data
     *
     * @return PEAR2\Console\CommandLine The parser instance
     */
    public static function fromXmlString($string)
    {
        return CommandLine\XmlParser::parseString($string);
    }

    // }}}
    // addArgument() {{{

    /**
     * Adds an argument to the command line parser and returns it.
     *
     * Adds an argument with the name $name and set its attributes with the
     * array $params, then return the PEAR2\Console\CommandLine\Argument instance
     * created.
     * The method accepts another form: you can directly pass a
     * PEAR2\Console\CommandLine\Argument object as the sole argument, this allows
     * you to contruct the argument separately, in order to reuse it in
     * different command line parsers or commands for example.
     *
     * Example:
     * <code>
     * $parser = new PEAR2\Console\CommandLine();
     * // add an array argument
     * $parser->addArgument('input_files', array('multiple'=>true));
     * // add a simple argument
     * $parser->addArgument('output_file');
     * $result = $parser->parse();
     * print_r($result->args['input_files']);
     * print_r($result->args['output_file']);
     * // will print:
     * // array('file1', 'file2')
     * // 'file3'
     * // if the command line was:
     * // myscript.php file1 file2 file3
     * </code>
     *
     * In a terminal, the help will be displayed like this:
     * <code>
     * $ myscript.php install -h
     * Usage: myscript.php <input_files...> <output_file>
     * </code>
     *
     * @param mixed $name   A string containing the argument name or an
     *                      instance of PEAR2\Console\CommandLine\Argument
     * @param array $params An array containing the argument attributes
     *
     * @return PEAR2\Console\CommandLine\Argument the added argument
     * 
     * @see PEAR2\Console\CommandLine\Argument
     */
    public function addArgument($name, $params = array())
    {
        if ($name instanceof CommandLine\Argument) {
            $argument = $name;
        } else {
            $argument = new CommandLine\Argument($name, $params);
        }
        $argument->validate();
        $this->args[$argument->name] = $argument;
        return $argument;
    }

    // }}}
    // addCommand() {{{

    /**
     * Adds a sub-command to the command line parser.
     *
     * Adds a command with the given $name to the parser and returns the
     * PEAR2\Console\CommandLine\Command instance, you can then populate the command
     * with options, configure it, etc... like you would do for the main parser
     * because the class PEAR2\Console\CommandLine\Command inherits from
     * PEAR2\Console\CommandLine.
     *
     * An example:
     * <code>
     * $parser = new PEAR2\Console\CommandLine();
     * $install_cmd = $parser->addCommand('install');
     * $install_cmd->addOption(
     *     'verbose',
     *     array(
     *         'short_name'  => '-v',
     *         'long_name'   => '--verbose',
     *         'description' => 'be noisy when installing stuff',
     *         'action'      => 'StoreTrue'
     *      )
     * );
     * $parser->parse();
     * </code>
     * Then in a terminal:
     * <code>
     * $ myscript.php install -h
     * Usage: myscript.php install [options]
     *
     * Options:
     *   -h, --help     display this help message and exit
     *   -v, --verbose  be noisy when installing stuff
     *
     * $ myscript.php install --verbose
     * Installing whatever...
     * $
     * </code>
     *
     * @param mixed $name   A string containing the command name or an
     *                      instance of PEAR2\Console\CommandLine\Command
     * @param array $params An array containing the command attributes
     *
     * @return PEAR2\Console\CommandLine\Command The added subcommand
     * @see    PEAR2\Console\CommandLine\Command
     */
    public function addCommand($name, $params = array())
    {
        if ($name instanceof CommandLine\Command) {
            $command = $name;
        } else {
            $params['name'] = $name;
            $command        = new CommandLine\Command($params);
            // some properties must cascade to the child command if not
            // passed explicitely. This is done only in this case, because if
            // we have a Command object we have no way to determine if theses
            // properties have already been set
            $cascade = array(
                'add_help_option',
                'add_version_option',
                'outputter',
                'message_provider',
                'force_posix',
                'force_options_defaults'
            );
            foreach ($cascade as $property) {
                if (!isset($params[$property])) {
                    $command->$property = $this->$property;
                }
            }
            if (!isset($params['renderer'])) {
                $renderer          = clone $this->renderer;
                $renderer->parser  = $command;
                $command->renderer = $renderer;
            }
        }
        $command->parent = $this;
        $this->commands[$command->name] = $command;
        return $command;
    }

    // }}}
    // addOption() {{{

    /**
     * Adds an option to the command line parser and returns it.
     *
     * Adds an option with the name $name and set its attributes with the
     * array $params, then return the PEAR2\Console\CommandLine\Option instance
     * created.
     * The method accepts another form: you can directly pass a
     * PEAR2\Console\CommandLine\Option object as the sole argument, this allows
     * you to contruct the option separately, in order to reuse it in different
     * command line parsers or commands for example.
     *
     * Example:
     * <code>
     * $parser = new PEAR2\Console\CommandLine();
     * $parser->addOption('path', array(
     *     'short_name'  => '-p',  // a short name
     *     'long_name'   => '--path', // a long name
     *     'description' => 'path to the dir', // a description msg
     *     'action'      => 'StoreString',
     *     'default'     => '/tmp' // a default value
     * ));
     * $parser->parse();
     * </code>
     *
     * In a terminal, the help will be displayed like this:
     * <code>
     * $ myscript.php --help
     * Usage: myscript.php [options]
     *
     * Options:
     *   -h, --help  display this help message and exit
     *   -p, --path  path to the dir
     *
     * </code>
     *
     * Various methods to specify an option, these 3 commands are equivalent:
     * <code>
     * $ myscript.php --path=some/path
     * $ myscript.php -p some/path
     * $ myscript.php -psome/path
     * </code>
     *
     * @param mixed $name   A string containing the option name or an
     *                      instance of PEAR2\Console\CommandLine\Option
     * @param array $params An array containing the option attributes
     *
     * @return PEAR2\Console\CommandLine\Option The added option
     * @see    PEAR2\Console\CommandLine\Option
     */
    public function addOption($name, $params = array())
    {
        if ($name instanceof CommandLine\Option) {
            $opt = $name;
        } else {
            $opt = new CommandLine\Option($name, $params);
        }
        $opt->validate();
        if ($this->force_options_defaults) {
            $opt->setDefaults();
        }
        $this->options[$opt->name] = $opt;
        if (!empty($opt->choices) && $opt->add_list_option) {
            $this->addOption(
                'list_' . $opt->name,
                array(
                    'long_name'     => '--list-' . $opt->name,
                    'description'   => $this->message_provider->get(
                        'LIST_OPTION_MESSAGE',
                        array('name' => $opt->name)
                    ),
                    'action'        => 'List',
                    'action_params' => array('list' => $opt->choices),
                )
            );
        }
        return $opt;
    }

    // }}}
    // displayError() {{{

    /**
     * Displays an error to the user via stderr and exit with $exitCode if its
     * value is not equals to false.
     *
     * @param string $error    The error message
     * @param int    $exitCode The exit code number (default: 1). If set to
     *                         false, the exit() function will not be called
     *
     * @return void
     */
    public function displayError($error, $exitCode = 1)
    {
        $this->outputter->stderr($this->renderer->error($error));
        if ($exitCode !== false) {
            exit($exitCode);
        }
    }

    // }}}
    // displayUsage() {{{

    /**
     * Displays the usage help message to the user via stdout and exit with
     * $exitCode if its value is not equals to false.
     *
     * @param int $exitCode The exit code number (default: 0). If set to
     *                      false, the exit() function will not be called
     *
     * @return void
     */
    public function displayUsage($exitCode = 0)
    {
        $this->outputter->stdout($this->renderer->usage());
        if ($exitCode !== false) {
            exit($exitCode);
        }
    }

    // }}}
    // displayVersion() {{{

    /**
     * Displays the program version to the user via stdout and exit with
     * $exitCode if its value is not equals to false.
     *
     * @param int $exitCode The exit code number (default: 0). If set to
     *                      false, the exit() function will not be called
     *
     * @return void
     */
    public function displayVersion($exitCode = 0)
    {
        $this->outputter->stdout($this->renderer->version());
        if ($exitCode !== false) {
            exit($exitCode);
        }
    }

    // }}}
    // findOption() {{{

    /**
     * Finds the option that matches the given short_name (ex: -v), long_name
     * (ex: --verbose) or name (ex: verbose).
     *
     * @param string $str The option identifier
     *
     * @return mixed A PEAR2\Console\CommandLine\Option instance or false
     */
    public function findOption($str)
    {
        $str = trim($str);
        if ($str === '') {
            return false;
        }
        $matches = array();
        foreach ($this->options as $opt) {
            if ($opt->short_name == $str
                || $opt->long_name == $str
                || $opt->name == $str
            ) {
                // exact match
                return $opt;
            }
            if (substr($opt->long_name, 0, strlen($str)) === $str) {
                // abbreviated long option
                $matches[] = $opt;
            }
        }
        if ($count = count($matches)) {
            if ($count > 1) {
                $matches_str = '';
                $padding     = '';
                foreach ($matches as $opt) {
                    $matches_str .= $padding . $opt->long_name;
                    $padding      = ', ';
                }
                throw CommandLine\Exception::factory(
                    'OPTION_AMBIGUOUS',
                    array('name' => $str, 'matches' => $matches_str),
                    $this,
                    $this->messages
                );
            }
            return $matches[0];
        }
        return false;
    }
    // }}}
    // registerAction() {{{

    /**
     * Registers a custom action for the parser, an example:
     *
     * <code>
     *
     * // in this example we create a "range" action:
     * // the user will be able to enter something like:
     * // $ <program> -r 1,5
     * // and in the result we will have:
     * // $result->options['range']: array(1, 5)
     *
     * class ActionRange extends PEAR2\Console\CommandLine\Action
     * {
     *     public function execute($value=false, $params=array())
     *     {
     *         $range = explode(',', str_replace(' ', '', $value));
     *         if (count($range) != 2) {
     *             throw new Exception(sprintf(
     *                 'Option "%s" must be 2 integers separated by a comma',
     *                 $this->option->name
     *             ));
     *         }
     *         $this->setResult($range);
     *     }
     * }
     * // then we can register our action
     * PEAR2\Console\CommandLine::registerAction('Range', 'ActionRange');
     * // and now our action is available !
     * $parser = new PEAR2\Console\CommandLine();
     * $parser->addOption('range', array(
     *     'short_name'  => '-r',
     *     'long_name'   => '--range',
     *     'action'      => 'Range', // note our custom action
     *     'description' => 'A range of two integers separated by a comma'
     * ));
     * // etc...
     *
     * </code>
     *
     * @param string $name  The name of the custom action
     * @param string $class The class name of the custom action
     *
     * @return void
     */
    public static function registerAction($name, $class)
    {
        if (!isset(self::$actions[$name])) {
            if (!class_exists($class)) {
                self::triggerError(
                    'action_class_does_not_exists',
                    E_USER_ERROR,
                    array('{$name}' => $name, '{$class}' => $class)
                );
            }
            self::$actions[$name] = array($class, false);
        }
    }

    // }}}
    // triggerError() {{{

    /**
     * A wrapper for programming errors triggering.
     *
     * @param string $msgId  Identifier of the message
     * @param int    $level  The php error level
     * @param array  $params An array of search=>replaces entries
     *
     * @return void
     * 
     * @todo remove Console::triggerError() and use exceptions only
     */
    public static function triggerError($msgId, $level, $params=array())
    {
        if (isset(self::$errors[$msgId])) {
            $msg = str_replace(
                array_keys($params),
                array_values($params),
                self::$errors[$msgId]
            );
            trigger_error($msg, $level);
        } else {
            trigger_error('unknown error', $level);
        }
    }

    // }}}
    // parse() {{{

    /**
     * Parses the command line arguments and returns a
     * PEAR2\Console\CommandLine\Result instance.
     *
     * @param integer $userArgc Number of arguments (optional)
     * @param array   $userArgv Array containing arguments (optional)
     *
     * @return PEAR2\Console\CommandLine\Result The result instance
     * @throws Exception on user errors
     */
    public function parse($userArgc=null, $userArgv=null)
    {
        $this->addBuiltinOptions();
        if ($userArgc !== null && $userArgv !== null) {
            $argc = $userArgc;
            $argv = $userArgv;
        } else {
            list($argc, $argv) = $this->getArgcArgv();
        }
        // build an empty result
        $result = new CommandLine\Result();
        if (!($this instanceof CommandLine\Command)) {
            // remove script name if we're not in a subcommand
            array_shift($argv);
            $argc--;
        }
        // will contain arguments
        $args = array();
        foreach ($this->options as $name=>$option) {
            $result->options[$name] = $option->default;
        }
        // parse command line tokens
        while ($argc--) {
            $token = array_shift($argv);
            try {
                if ($cmd = $this->_getSubCommand($token)) {
                    $result->command_name = $cmd->name;
                    $result->command      = $cmd->parse($argc, $argv);
                    break;
                } else {
                    $this->parseToken($token, $result, $args, $argc);
                }
            } catch (Exception $exc) {
                throw $exc;
            }
        }
        // Parse a null token to allow any undespatched actions to be despatched.
        $this->parseToken(null, $result, $args, 0);
        // Check if an invalid subcommand was specified. If there are
        // subcommands and no arguments, but an argument was provided, it is
        // an invalid subcommand.
        if (count($this->commands) > 0
            && count($this->args) === 0
            && count($args) > 0
        ) {
            throw CommandLine\Exception::factory(
                'INVALID_SUBCOMMAND',
                array('command' => $args[0]),
                $this,
                $this->messages
            );
        }
        // if subcommand_required is set to true we must check that we have a
        // subcommand.
        if (count($this->commands)
            && $this->subcommand_required
            && !$result->command_name
        ) {
            throw CommandLine\Exception::factory(
                'SUBCOMMAND_REQUIRED',
                array('commands' => implode(array_keys($this->commands), ', ')),
                $this,
                $this->messages
            );
        }
        // minimum argument number check
        $argnum = 0;
        foreach ($this->args as $name=>$arg) {
            if (!$arg->optional) {
                $argnum++;
            }
        }
        if (count($args) < $argnum) {
            throw CommandLine\Exception::factory(
                'ARGUMENT_REQUIRED',
                array('argnum' => $argnum, 'plural' => $argnum>1 ? 's': ''),
                $this,
                $this->messages
            );
        }
        // handle arguments
        $c = count($this->args);
        foreach ($this->args as $name=>$arg) {
            $c--;
            if ($arg->multiple) {
                $result->args[$name] = $c ? array_splice($args, 0, -$c) : $args;
            } else {
                $result->args[$name] = array_shift($args);
            }
            if (!$result->args[$name] && $arg->optional && $arg->default) {
                $result->args[$name] = $arg->default;
            }
        }
        // dispatch deferred options
        foreach ($this->_dispatchLater as $optArray) {
            $optArray[0]->dispatchAction($optArray[1], $optArray[2], $this);
        }
        return $result;
    }

    // }}}
    // parseToken() {{{

    /**
     * Parses the command line token and modifies *by reference* the $options
     * and $args arrays.
     *
     * @param string $token  The command line token to parse
     * @param object $result The PEAR2\Console\CommandLine\Result instance
     * @param array  &$args  The argv array
     * @param int    $argc   Number of lasting args
     *
     * @return void
     * @access protected
     * @throws Exception on user errors
     */
    protected function parseToken($token, $result, &$args, $argc)
    {
        $last  = $argc === 0;
        if (!$this->_stopflag && $this->_lastopt) {
            if (substr($token, 0, 1) == '-') {
                if ($this->_lastopt->argument_optional) {
                    $this->_dispatchAction($this->_lastopt, '', $result);
                    if ($this->_lastopt->action != 'StoreArray') {
                        $this->_lastopt = false;
                    }
                } else if (isset($result->options[$this->_lastopt->name])) {
                    // case of an option that expect a list of args
                    $this->_lastopt = false;
                } else {
                    throw CommandLine\Exception::factory(
                        'OPTION_VALUE_REQUIRED',
                        array('name' => $this->_lastopt->name),
                        $this,
                        $this->messages
                    );
                }
            } else {
                // when a StoreArray option is positioned last, the behavior
                // is to consider that if there's already an element in the
                // array, and the commandline expects one or more args, we
                // leave last tokens to arguments
                if ($this->_lastopt->action == 'StoreArray'
                    && !empty($result->options[$this->_lastopt->name])
                    && count($this->args) > ($argc + count($args))
                ) {
                    if (!is_null($token)) {
                        $args[] = $token;
                    }
                    return;
                }
                if (!is_null($token) || $this->_lastopt->action == 'Password') {
                    $this->_dispatchAction($this->_lastopt, $token, $result);
                }
                if ($this->_lastopt->action != 'StoreArray') {
                    $this->_lastopt = false;
                }
                return;
            }
        }
        if (!$this->_stopflag && substr($token, 0, 2) == '--') {
            // a long option
            $optkv = explode('=', $token, 2);
            if (trim($optkv[0]) == '--') {
                // the special argument "--" forces in all cases the end of
                // option scanning.
                $this->_stopflag = true;
                return;
            }
            $opt = $this->findOption($optkv[0]);
            if (!$opt) {
                throw CommandLine\Exception::factory(
                    'OPTION_UNKNOWN',
                    array('name' => $optkv[0]),
                    $this,
                    $this->messages
                );
            }
            $value = isset($optkv[1]) ? $optkv[1] : false;
            if (!$opt->expectsArgument() && $value !== false) {
                throw CommandLine\Exception::factory(
                    'OPTION_VALUE_UNEXPECTED',
                    array('name' => $opt->name, 'value' => $value),
                    $this,
                    $this->messages
                );
            }
            if ($opt->expectsArgument() && $value === false) {
                // maybe the long option argument is separated by a space, if
                // this is the case it will be the next arg
                if ($last && !$opt->argument_optional) {
                    throw CommandLine\Exception::factory(
                        'OPTION_VALUE_REQUIRED',
                        array('name' => $opt->name),
                        $this,
                        $this->messages
                    );
                }
                // we will have a value next time
                $this->_lastopt = $opt;
                return;
            }
            if ($opt->action == 'StoreArray') {
                $this->_lastopt = $opt;
            }
            $this->_dispatchAction($opt, $value, $result);
        } else if (!$this->_stopflag && substr($token, 0, 1) == '-') {
            // a short option
            $optname = substr($token, 0, 2);
            if ($optname == '-') {
                // special case of "-": try to read stdin
                $args[] = file_get_contents('php://stdin');
                return;
            }
            $opt = $this->findOption($optname);
            if (!$opt) {
                throw CommandLine\Exception::factory(
                    'OPTION_UNKNOWN',
                    array('name' => $optname),
                    $this,
                    $this->messages
                );
            }
            // parse other options or set the value
            // in short: handle -f<value> and -f <value>
            $next = substr($token, 2, 1);
            // check if we must wait for a value
            if (!$next) {
                if ($opt->expectsArgument()) {
                    if ($last && !$opt->argument_optional) {
                        throw CommandLine\Exception::factory(
                            'OPTION_VALUE_REQUIRED',
                            array('name' => $opt->name),
                            $this,
                            $this->messages
                        );
                    }
                    // we will have a value next time
                    $this->_lastopt = $opt;
                    return;
                }
                $value = false;
            } else {
                if (!$opt->expectsArgument()) {
                    if ($nextopt = $this->findOption('-' . $next)) {
                        $this->_dispatchAction($opt, false, $result);
                        $this->parseToken(
                            '-' . substr($token, 2),
                            $result,
                            $args,
                            $last
                        );
                        return;
                    } else {
                        throw CommandLine\Exception::factory(
                            'OPTION_UNKNOWN',
                            array('name' => $next),
                            $this,
                            $this->messages
                        );
                    }
                }
                if ($opt->action == 'StoreArray') {
                    $this->_lastopt = $opt;
                }
                $value = substr($token, 2);
            }
            $this->_dispatchAction($opt, $value, $result);
        } else {
            // We have an argument.
            // if we are in POSIX compliant mode, we must set the stop flag to
            // true in order to stop option parsing.
            if (!$this->_stopflag && $this->force_posix) {
                $this->_stopflag = true;
            }
            if (!is_null($token)) {
                $args[] = $token;
            }
        }
    }

    // }}}
    // addBuiltinOptions() {{{

    /**
     * Adds the builtin "Help" and "Version" options if needed.
     *
     * @return void
     */
    public function addBuiltinOptions()
    {
        if ($this->add_help_option) {
            $helpOptionParams = array(
                'long_name'   => '--help',
                'description' => 'show this help message and exit',
                'action'      => 'Help'
            );
            if (!($option = $this->findOption('-h')) || $option->action == 'Help') {
                // short name is available, take it
                $helpOptionParams['short_name'] = '-h';
            }
            $this->addOption('help', $helpOptionParams);
        }
        if ($this->add_version_option && !empty($this->version)) {
            $versionOptionParams = array(
                'long_name'   => '--version',
                'description' => 'show the program version and exit',
                'action'      => 'Version'
            );
            if (!$this->findOption('-v')) {
                // short name is available, take it
                $versionOptionParams['short_name'] = '-v';
            }
            $this->addOption('version', $versionOptionParams);
        }
    }

    // }}}
    // getArgcArgv() {{{

    /**
     * Tries to return an array containing argc and argv, or trigger an error
     * if it fails to get them.
     *
     * @return array The argc/argv array
     * @throws PEAR2\Console\CommandLine\Exception
     */
    protected function getArgcArgv()
    {
        if (php_sapi_name() != 'cli') {
            // we have a web request
            $argv = array($this->name);
            if (isset($_REQUEST)) {
                foreach ($_REQUEST as $key => $value) {
                    if (!is_array($value)) {
                        $value = array($value);
                    }
                    $opt = $this->findOption($key);
                    if ($opt instanceof CommandLine\Option) {
                        // match a configured option
                        $argv[] = $opt->short_name ?
                            $opt->short_name : $opt->long_name;
                        foreach ($value as $v) {
                            if ($opt->expectsArgument()) {
                                $argv[] = isset($_REQUEST[$key])
                                    ? urldecode($v)
                                    : $v;
                            } else if ($v == '0' || $v == 'false') {
                                array_pop($argv);
                            }
                        }
                    } else if (isset($this->args[$key])) {
                        // match a configured argument
                        foreach ($value as $v) {
                            $argv[] = isset($_REQUEST[$key]) ? urldecode($v) : $v;
                        }
                    }
                }
            }
            return array(count($argv), $argv);
        }
        if (isset($argc) && isset($argv)) {
            // case of register_argv_argc = 1
            return array($argc, $argv);
        }
        if (isset($_SERVER['argc']) && isset($_SERVER['argv'])) {
            return array($_SERVER['argc'], $_SERVER['argv']);
        }
        return array(0, array());
    }

    // }}}
    // _dispatchAction() {{{

    /**
     * Dispatches the given option or store the option to dispatch it later.
     *
     * @param PEAR2\Console\CommandLine\Option $option The option instance
     * @param string                           $token  Command line token to parse
     * @param PEAR2\Console\CommandLine\Result $result The result instance
     *
     * @return void
     */
    private function _dispatchAction($option, $token, $result)
    {
        if ($option->action == 'Password') {
            $this->_dispatchLater[] = array($option, $token, $result);
        } else {
            $option->dispatchAction($token, $result, $this);
        }
    }
    // }}}
    // _getSubCommand() {{{

    /**
     * Tries to return the subcommand that matches the given token or returns
     * false if no subcommand was found.
     *
     * @param string $token Current command line token
     *
     * @return mixed An instance of PEAR2\Console\CommandLine\Command or false
     */
    private function _getSubCommand($token)
    {
        foreach ($this->commands as $cmd) {
            if ($cmd->name == $token || in_array($token, $cmd->aliases)) {
                return $cmd;
            }
        }
        return false;
    }

    // }}}
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_accept.phpt
--TEST--
Test for PEAR2\Console\CommandLine::accept() method.
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
try {
    // custom renderer
    $parser->accept(new CustomRenderer());
    echo get_class($parser->renderer) . "\n";
    // outputter
    $parser->accept(new CustomOutputter());
    echo get_class($parser->outputter) . "\n";
    $parser->accept(new CustomMessageProvider());
    echo get_class($parser->message_provider) . "\n";
    $parser->accept(new stdclass());
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>
--EXPECT--
CustomRenderer
CustomOutputter
CustomMessageProvider
STDERR >> CustomRenderer::error(INVALID_CUSTOM_INSTANCE)


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addargument.phpt
--TEST--
Test for PEAR2\Console\CommandLine::addArgument() method.
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new \PEAR2\Console\CommandLine();
$parser->addArgument('arg1');
$parser->addArgument(
    'arg2',
    array(
        'multiple' => true,
        'description' => 'description of arg2'
    )
);
$arg3 = new \PEAR2\Console\CommandLine\Argument(
    'arg3',
    array(
        'multiple' => true,
        'description' => 'description of arg3'
    )
);
$parser->addArgument($arg3);
$parser->addArgument('arg4', array('optional' => true));

var_dump($parser->args);

// a bad argument
$parser->addArgument('Some invalid name');

?>
--EXPECTF--
array(4) {
  ["arg1"]=>
  object(PEAR2\Console\CommandLine\Argument)#%d (7) {
    ["multiple"]=>
    bool(false)
    ["optional"]=>
    bool(false)
    ["name"]=>
    string(4) "arg1"
    ["help_name"]=>
    string(4) "arg1"
    ["description"]=>
    NULL
    ["default"]=>
    NULL
    ["messages"]=>
    array(0) {
    }
  }
  ["arg2"]=>
  object(PEAR2\Console\CommandLine\Argument)#%d (7) {
    ["multiple"]=>
    bool(true)
    ["optional"]=>
    bool(false)
    ["name"]=>
    string(4) "arg2"
    ["help_name"]=>
    string(4) "arg2"
    ["description"]=>
    string(19) "description of arg2"
    ["default"]=>
    NULL
    ["messages"]=>
    array(0) {
    }
  }
  ["arg3"]=>
  object(PEAR2\Console\CommandLine\Argument)#%d (7) {
    ["multiple"]=>
    bool(true)
    ["optional"]=>
    bool(false)
    ["name"]=>
    string(4) "arg3"
    ["help_name"]=>
    string(4) "arg3"
    ["description"]=>
    string(19) "description of arg3"
    ["default"]=>
    NULL
    ["messages"]=>
    array(0) {
    }
  }
  ["arg4"]=>
  object(PEAR2\Console\CommandLine\Argument)#%d (7) {
    ["multiple"]=>
    bool(false)
    ["optional"]=>
    bool(true)
    ["name"]=>
    string(4) "arg4"
    ["help_name"]=>
    string(4) "arg4"
    ["description"]=>
    NULL
    ["default"]=>
    NULL
    ["messages"]=>
    array(0) {
    }
  }
}

Fatal error: argument name must be a valid php variable name (got: Some invalid name) in %sCommandLine.php on line %d


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addargument2.phpt
--TEST--
Test for Console_CommandLine::addArgument() method.
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
foo
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new \PEAR2\Console\CommandLine();
$parser->addArgument('arg1');
$parser->addArgument(
    'arg2',
    array(
        'optional' => true,
        'default' => 'bar'
    )
);

$result = $parser->parse();
echo $result->args['arg1'] . ' ' . $result->args['arg2'];

// a bad argument
$parser->addArgument('arg3', array('default' => 'baz'));

?>
--EXPECTF--
foo bar
Fatal error: only optional arguments can have a default value in %sCommandLine.php on line %d


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addcommand.phpt
--TEST--
Test for PEAR2\Console\CommandLine::addCommand() method.
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new PEAR2\Console\CommandLine();
$parser->addCommand('cmd1');
$parser->addCommand(
    'cmd2',
    array(
        'description' => 'description of cmd2'
    )
);
$cmd3 = new PEAR2\Console\CommandLine\Command(
    array(
        'name' => 'cmd3',
        'description' => 'description of cmd3'    
    )
);
$parser->addCommand($cmd3);

var_dump(array_keys($parser->commands));
var_dump($parser->commands['cmd2']->description);
var_dump($parser->commands['cmd3']->description);

?>
--EXPECT--
array(3) {
  [0]=>
  string(4) "cmd1"
  [1]=>
  string(4) "cmd2"
  [2]=>
  string(4) "cmd3"
}
string(19) "description of cmd2"
string(19) "description of cmd3"


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addcommand_3.phpt
--TEST--
Test for Console_CommandLine::addCommand() method.
--ARGS--
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new \PEAR2\Console\CommandLine(array('subcommand_required' => true));
$parser->addCommand('cmd1');
$parser->addCommand('cmd2');
$parser->addCommand('cmd3');
try {
    $parser->parse();
} catch (\PEAR2\Console\CommandLine\Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECTF--
Please enter one of the following command: cmd1, cmd2, cmd3.


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addoption.phpt
--TEST--
Test for PEAR2\Console\CommandLine::addOption() method.
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new PEAR2\Console\CommandLine();
$parser->addOption(
    'opt1',
    array(
        'short_name' => '-a'
    )
);
$parser->addOption(
    'opt2',
    array(
        'short_name' => '-b',
        'long_name' => '--foo',
        'description' => 'description of opt2',
        'action' => 'StoreInt',
        'help_name' => 'bar',
        'choices' => array(1, 2, 3),
        'add_list_option' => true,
        'default' => 2
    )
);
$opt3 = new PEAR2\Console\CommandLine\Option(
    'opt3',
    array(
        'long_name' => '--bar',
        'description' => 'description of opt3',
    )
);
$parser->addOption($opt3);

var_dump($parser->options);

?>
--EXPECTF--
array(4) {
  ["opt1"]=>
  object(PEAR2\Console\CommandLine\Option)#%d (14) {
    ["short_name"]=>
    string(2) "-a"
    ["long_name"]=>
    NULL
    ["action"]=>
    string(11) "StoreString"
    ["choices"]=>
    array(0) {
    }
    ["callback"]=>
    NULL
    ["action_params"]=>
    array(0) {
    }
    ["argument_optional"]=>
    bool(false)
    ["add_list_option"]=>
    bool(false)
    ["_action_instance":"PEAR2\Console\CommandLine\Option":private]=>
    NULL
    ["name"]=>
    string(4) "opt1"
    ["help_name"]=>
    string(4) "opt1"
    ["description"]=>
    NULL
    ["default"]=>
    NULL
    ["messages"]=>
    array(0) {
    }
  }
  ["opt2"]=>
  object(PEAR2\Console\CommandLine\Option)#%d (14) {
    ["short_name"]=>
    string(2) "-b"
    ["long_name"]=>
    string(5) "--foo"
    ["action"]=>
    string(8) "StoreInt"
    ["choices"]=>
    array(3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
    ["callback"]=>
    NULL
    ["action_params"]=>
    array(0) {
    }
    ["argument_optional"]=>
    bool(false)
    ["add_list_option"]=>
    bool(true)
    ["_action_instance":"PEAR2\Console\CommandLine\Option":private]=>
    NULL
    ["name"]=>
    string(4) "opt2"
    ["help_name"]=>
    string(3) "bar"
    ["description"]=>
    string(19) "description of opt2"
    ["default"]=>
    int(2)
    ["messages"]=>
    array(0) {
    }
  }
  ["list_opt2"]=>
  object(PEAR2\Console\CommandLine\Option)#%d (14) {
    ["short_name"]=>
    NULL
    ["long_name"]=>
    string(11) "--list-opt2"
    ["action"]=>
    string(4) "List"
    ["choices"]=>
    array(0) {
    }
    ["callback"]=>
    NULL
    ["action_params"]=>
    array(1) {
      ["list"]=>
      array(3) {
        [0]=>
        int(1)
        [1]=>
        int(2)
        [2]=>
        int(3)
      }
    }
    ["argument_optional"]=>
    bool(false)
    ["add_list_option"]=>
    bool(false)
    ["_action_instance":"PEAR2\Console\CommandLine\Option":private]=>
    NULL
    ["name"]=>
    string(9) "list_opt2"
    ["help_name"]=>
    string(9) "list_opt2"
    ["description"]=>
    string(35) "lists valid choices for option opt2"
    ["default"]=>
    NULL
    ["messages"]=>
    array(0) {
    }
  }
  ["opt3"]=>
  object(PEAR2\Console\CommandLine\Option)#%d (14) {
    ["short_name"]=>
    NULL
    ["long_name"]=>
    string(5) "--bar"
    ["action"]=>
    string(11) "StoreString"
    ["choices"]=>
    array(0) {
    }
    ["callback"]=>
    NULL
    ["action_params"]=>
    array(0) {
    }
    ["argument_optional"]=>
    bool(false)
    ["add_list_option"]=>
    bool(false)
    ["_action_instance":"PEAR2\Console\CommandLine\Option":private]=>
    NULL
    ["name"]=>
    string(4) "opt3"
    ["help_name"]=>
    string(4) "opt3"
    ["description"]=>
    string(19) "description of opt3"
    ["default"]=>
    NULL
    ["messages"]=>
    array(0) {
    }
  }
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addoption_errors_1.phpt
--TEST--
Test for PEAR2\Console\CommandLine::addOption() method (errors 1).
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new PEAR2\Console\CommandLine();
$parser->addOption('Some invalid name');

?>
--EXPECTF--

Fatal error: option name must be a valid php variable name (got: Some invalid name) in %sCommandLine.php on line %d


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addoption_errors_2.phpt
--TEST--
Test for PEAR2\Console\CommandLine::addOption() method (errors 2).
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new PEAR2\Console\CommandLine();
$parser->addOption('name', array());

?>
--EXPECTF--

Fatal error: you must provide at least an option short name or long name for option "name" in %sCommandLine.php on line %d


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addoption_errors_3.phpt
--TEST--
Test for PEAR2\Console\CommandLine::addOption() method (errors 3).
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new PEAR2\Console\CommandLine();
$parser->addOption('name', array('short_name'=>'d'));

?>
--EXPECTF--

Fatal error: option "name" short name must be a dash followed by a letter (got: "d") in %sCommandLine.php on line %d


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addoption_errors_4.phpt
--TEST--
Test for PEAR2\Console\CommandLine::addOption() method (errors 4).
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new PEAR2\Console\CommandLine();
$parser->addOption('name', array('long_name'=>'d'));

?>
--EXPECTF--

Fatal error: option "name" long name must be 2 dashes followed by a word (got: "d") in %sCommandLine.php on line %d


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addoption_errors_5.phpt
--TEST--
Test for PEAR2\Console\CommandLine::addOption() method (errors 5).
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new PEAR2\Console\CommandLine();
$parser->addOption('name', array('short_name'=>'-d', 'action'=>true));

?>
--EXPECTF--

Fatal error: invalid action for option "name". in %sCommandLine.php on line %d


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addoption_errors_6.phpt
--TEST--
Test for PEAR2\Console\CommandLine::addOption() method (errors 6).
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new PEAR2\Console\CommandLine();
$parser->addOption('name', array('short_name'=>'-d', 'action'=>'Inexistant'));

?>
--EXPECTF--

Fatal error: unregistered action "Inexistant" for option "name". in %sCommandLine.php on line %d


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_addoption_errors_7.phpt
--TEST--
Test for PEAR2\Console\CommandLine::addOption() method (errors 7).
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new PEAR2\Console\CommandLine();
$parser->addOption('name', array('short_name'=>'-d', 'action'=>'Callback'));

?>
--EXPECTF--

Fatal error: you must provide a valid callback for option "name" in %sCommandLine.php on line %d


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_bug18682.phpt
--TEST--
Test for bug #18682: columnWrap() in Default Renderer eats up lines with only a EOL.
--ARGS--
cmd1 --help 2>&1
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

class Renderer extends \PEAR2\Console\CommandLine\Renderer_Default
{
    protected function description()
    {
        return $this->columnWrap($this->parser->description, 2);
    }
}

$parser = new \PEAR2\Console\CommandLine();
$parser->accept(new Renderer);
$parser->renderer->line_width = 75;
$parser->addCommand(
    'cmd1',
    array(
        'description' => '
Installs listed packages.

local package.xml example:
php pyrus.phar install package.xml

local package archive example:
php pyrus.phar install PackageName-1.2.0.tar

remote package archive example:
php pyrus.phar install http://www.example.com/PackageName-1.2.0.tgz

Examples of an abstract package:
php pyrus.phar install PackageName
  installs PackageName from the default channel with stability preferred_state
php pyrus.phar pear/PackageName
  installs PackageName from the pear.php.net channel with stability preferred_state
php pyrus.phar install channel://doc.php.net/PackageName
  installs PackageName from the doc.php.net channel with stability preferred_state
php pyrus.phar install PackageName-beta
  installs PackageName from the default channel, beta or stable stability
php pyrus.phar install PackageName-1.2.0
  installs PackageName from the default channel, version 1.2.0'
    )
);
$parser->parse();

?>
--EXPECTF--
  Installs listed packages.

  local package.xml example:
  php pyrus.phar install package.xml

  local package archive example:
  php pyrus.phar install PackageName-1.2.0.tar

  remote package archive example:
  php pyrus.phar install http://www.example.com/PackageName-1.2.0.tgz

  Examples of an abstract package:
  php pyrus.phar install PackageName
    installs PackageName from the default channel with stability
  preferred_state
  php pyrus.phar pear/PackageName
    installs PackageName from the pear.php.net channel with stability
  preferred_state
  php pyrus.phar install channel://doc.php.net/PackageName
    installs PackageName from the doc.php.net channel with stability
  preferred_state
  php pyrus.phar install PackageName-beta
    installs PackageName from the default channel, beta or stable stability
  php pyrus.phar install PackageName-1.2.0
    installs PackageName from the default channel, version 1.2.0

Usage:
  %sconsole_commandline_bug18682.php
  [options] cmd1 [options]

Options:
  -h, --help  show this help message and exit


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_fromxmlfile.phpt
--TEST--
Test for PEAR2\Console\CommandLine::fromXmlFile() method.
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--help 2>&1
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = PEAR2\Console\CommandLine::fromXmlFile(
    __DIR__ . DIRECTORY_SEPARATOR . 'test.xml'
);
$parser->parse();

?>
--EXPECTF--
zip/unzip files

Usage:
  test [options]
  test [options] <command> [options] [args]

Options:
  -c choice, --choice=choice        choice option
  --list-choice                     lists valid choices for option choice
  -p password, --password=password  zip file password
  -v, --verbose                     turn on verbose output
  -h, --help                        show this help message and exit
  --version                         show the program version and exit

Commands:
  zip    zip given files in the destination file (aliases: compress, zp)
  unzip  unzip given file in the destination dir (alias: uzp)


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_fromxmlfile_error.phpt
--TEST--
Test for PEAR2\Console\CommandLine::fromXmlFile() method (error).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--help 2>&1
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

// unexisting xml file
$parser = PEAR2\Console\CommandLine::fromXmlFile(
    __DIR__ . DIRECTORY_SEPARATOR . 'unexisting.xml'
);
$parser->parse();

?>
--EXPECTF--

Fatal error: XML definition file "%sunexisting.xml" does not exists or is not readable in %sCommandLine.php on line %d


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_fromxmlstring.phpt
--TEST--
Test for PEAR2\Console\CommandLine::fromXmlString() method.
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--help 2>&1
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$str = file_get_contents(__DIR__ . DIRECTORY_SEPARATOR . 'test.xml');
$parser = PEAR2\Console\CommandLine::fromXmlString($str);
$parser->parse();

?>
--EXPECT--
zip/unzip files

Usage:
  test [options]
  test [options] <command> [options] [args]

Options:
  -c choice, --choice=choice        choice option
  --list-choice                     lists valid choices for option choice
  -p password, --password=password  zip file password
  -v, --verbose                     turn on verbose output
  -h, --help                        show this help message and exit
  --version                         show the program version and exit

Commands:
  zip    zip given files in the destination file (aliases: compress, zp)
  unzip  unzip given file in the destination dir (alias: uzp)


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_options_defaults.phpt
--TEST--
Test for PEAR2\Console\CommandLine options defaults.
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

try {
    $parser = buildParser3();
    $parser->force_options_defaults = true;
    $result = $parser->parse();
    foreach ($result->options as $k => $v) {
        echo $k . ":"; var_dump($v);
    }
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>
--EXPECT--
true:bool(false)
false:bool(true)
int:int(0)
float:float(0)
string:NULL
counter:int(0)
callback:NULL
array:array(0) {
}
password:NULL
help:NULL
version:NULL


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_1.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (--version).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--version
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
$parser->parse();

?>
--EXPECT--
some_program version 0.1.0.


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_10.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (subcommand).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
-v install -f foo
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser2();
$result = $parser->parse();
var_dump($result->options);
var_dump($result->command_name);
var_dump($result->command->options);

?>
--EXPECT--
array(4) {
  ["verbose"]=>
  bool(true)
  ["logfile"]=>
  NULL
  ["help"]=>
  NULL
  ["version"]=>
  NULL
}
string(7) "install"
array(2) {
  ["force"]=>
  bool(true)
  ["help"]=>
  NULL
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_11.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (subcommand help 1).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--help 2>&1
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser2();
$result = $parser->parse();

?>
--EXPECT--
Description of our parser goes here...

Usage:
  some_program [options]
  some_program [options] <command> [options] [args]

Options:
  -v, --verbose                  verbose mode
  -l logfile, --logfile=logfile  path to logfile
  -h, --help                     show this help message and exit
  --version                      show the program version and exit

Commands:
  install    install given package (aliases: inst, instbis)
  uninstall  uninstall given package


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_12.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (subcommand help 2).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
inst --help 2>&1
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser2();
$result = $parser->parse();

?>
--EXPECT--
install given package

Usage:
  some_program [options] install [options] package

Options:
  -f, --force  force installation
  -h, --help   show this help message and exit

Arguments:
  package  package to install


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_13.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (user errors 1).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--float=foo foo bar
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
try {
    $result = $parser->parse();
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECT--
Option "float" requires a value of type float (got "foo").


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_14.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (user errors 2).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--int=foo foo bar
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
try {
    $result = $parser->parse();
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECT--
Option "int" requires a value of type int (got "foo").


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_15.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (subcommand error).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
install -f 2>&1
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser2();
try {
    $result = $parser->parse();
} catch (Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>
--EXPECT--
Error: You must provide at least 1 argument.
Type "some_program --help" to get help.
Type "some_program <command> --help" to get help on specific command.


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_16.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (user errors 3).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
-s fooz foo bar
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
try {
    $result = $parser->parse();
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECT--
Option "string" must be one of the following: "foo", "bar", "baz" (got "fooz").


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_17.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (user argc/argv 1).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$argv = array('somename', '-t', '-f', '--float=1.2', 'foo', 'bar');
$argc = count($argv);
try {
    $parser = buildParser1();
    $result = $parser->parse($argc, $argv);
    var_dump($result);
} catch (\PEAR2\Console\CommandLine\Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>
--EXPECTF--
object(PEAR2\Console\CommandLine\Result)#%d (4) {
  ["options"]=>
  array(11) {
    ["true"]=>
    bool(true)
    ["false"]=>
    bool(false)
    ["int"]=>
    int(1)
    ["float"]=>
    float(1.2)
    ["string"]=>
    NULL
    ["counter"]=>
    NULL
    ["callback"]=>
    NULL
    ["array"]=>
    array(2) {
      [0]=>
      string(4) "spam"
      [1]=>
      string(3) "egg"
    }
    ["password"]=>
    NULL
    ["help"]=>
    NULL
    ["version"]=>
    NULL
  }
  ["args"]=>
  array(2) {
    ["simple"]=>
    string(3) "foo"
    ["multiple"]=>
    array(1) {
      [0]=>
      string(3) "bar"
    }
  }
  ["command_name"]=>
  bool(false)
  ["command"]=>
  bool(false)
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_18.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (user argc/argv 2).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

$argv = array('somename', '-v', 'install', '-f', 'foo');
$argc = count($argv);
try {
    $parser = buildParser2();
    $result = $parser->parse($argc, $argv);
    var_dump($result);
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>
--EXPECTF--
object(PEAR2\Console\CommandLine\Result)#%d (4) {
  ["options"]=>
  array(4) {
    ["verbose"]=>
    bool(true)
    ["logfile"]=>
    NULL
    ["help"]=>
    NULL
    ["version"]=>
    NULL
  }
  ["args"]=>
  array(0) {
  }
  ["command_name"]=>
  string(7) "install"
  ["command"]=>
  object(PEAR2\Console\CommandLine\Result)#%d (4) {
    ["options"]=>
    array(2) {
      ["force"]=>
      bool(true)
      ["help"]=>
      NULL
    }
    ["args"]=>
    array(1) {
      ["package"]=>
      string(3) "foo"
    }
    ["command_name"]=>
    bool(false)
    ["command"]=>
    bool(false)
  }
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_19.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (subcommand help 1).
--STDIN--
some_package
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
-v instbis -f -
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser2();
try {
    $result = $parser->parse();
    print_r($result);
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECT--
PEAR2\Console\CommandLine\Result Object
(
    [options] => Array
        (
            [verbose] => 1
            [logfile] => 
            [help] => 
            [version] => 
        )

    [args] => Array
        (
        )

    [command_name] => install
    [command] => PEAR2\Console\CommandLine\Result Object
        (
            [options] => Array
                (
                    [force] => 1
                    [help] => 
                )

            [args] => Array
                (
                    [package] => some_package

                )

            [command_name] => 
            [command] => 
        )

)


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_2.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (--help).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--help 2>&1
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
$parser->parse();

?>
--EXPECT--
Description of our parser goes here...

Usage:
  some_program [options] simple [multiple1 multiple2 ...]

Options:
  -t, --true                        test the StoreTrue action
  -f, --false                       test the StoreFalse action
  --int=INT                         test the StoreInt action
  --float=FLOAT                     test the StoreFloat action
  -s STRING, --string=STRING        test the StoreString action
  -c, --counter                     test the Counter action
  --callback=callback               test the Callback action
  -a ARRAY, --array=ARRAY           test the StoreArray action
  -p password, --password=password  test the Password action
  -h, --help                        show this help message and exit
  -v, --version                     show the program version and exit

Arguments:
  simple    test a simple argument
  multiple  test a multiple argument


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_20.phpt
--TEST--
Test for PEAR2\Console\CommandLine::fromXmlFile() method.
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--list-choice
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = PEAR2\Console\CommandLine::fromXmlFile(__DIR__ . DIRECTORY_SEPARATOR . 'test.xml');
$parser->parse();

?>
--EXPECTF--
Valid choices are: ham, spam


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_21.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (--help with renderer options).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--help 2>&1
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
$parser->renderer->line_width = 0;
$parser->renderer->options_on_different_lines = true;
$parser->parse();

?>
--EXPECT--
Description of our parser goes here...

Usage:
  some_program [options] simple [multiple1 multiple2 ...]

Options:
  -t
  --true               test the StoreTrue action
  -f
  --false              test the StoreFalse action
  --int=INT            test the StoreInt action
  --float=FLOAT        test the StoreFloat action
  -s STRING
  --string=STRING      test the StoreString action
  -c
  --counter            test the Counter action
  --callback=callback  test the Callback action
  -a ARRAY
  --array=ARRAY        test the StoreArray action
  -p password
  --password=password  test the Password action
  -h
  --help               show this help message and exit
  -v
  --version            show the program version and exit

Arguments:
  simple    test a simple argument
  multiple  test a multiple argument


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_22.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (--help with renderer options).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--list
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = new PEAR2\Console\CommandLine();
$parser->addOption('list', array(
    'long_name'     => '--list',
    'action'        => 'List',
    'action_params' => array(
        'list'      => array('foo', 'bar', 'baz'),
        'message'   => 'foobarbaz---',
        'delimiter' => '|',
        'post'      => '---foobarbaz',
    ),
));
$parser->parse();

?>
--EXPECT--
foobarbaz---foo|bar|baz---foobarbaz


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_23.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (invalid subcommand detection).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
-v invalid subcommand
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser2();
try {
    $result = $parser->parse();
} catch (Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECT--
Command "invalid" is not valid.


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_24.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (invalid subcommand detection).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
upgrade
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser4();
try {
    $result = $parser->parse();
} catch (Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECT--
You must provide at least 1 argument.

File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_25.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (invalid subcommand detection).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
upgrade -s foo
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser4();
try {
    $result = $parser->parse();
} catch (Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECT--
Option "state" must be one of the following: "stable", "beta" (got "foo").

File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_26.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (invalid subcommand detection).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
upgrade -s
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser4();
try {
    $result = $parser->parse();
} catch (Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECT--
Option "state" requires a value.

File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_27.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (invalid subcommand detection).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
upgrade -t
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser4();
try {
    $result = $parser->parse();
} catch (Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECT--
Unknown option "-t".

File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_28.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (invalid subcommand detection).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
upgrade --dry-run=foo
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser4();
try {
    $result = $parser->parse();
} catch (Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECT--
Option "dry_run" does not expect a value (got "foo").

File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_29.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (invalid subcommand detection).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
foo
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser4();
try {
    $result = $parser->parse();
} catch (Exception $exc) {
    echo $exc->getMessage();
}

?>
--EXPECT--
Command "foo" is not valid.


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_3.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (various options).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
-tfsfoo --int=3 --flo 4.0 -cccc --callback=somestring -a foo bar baz foo bar
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
$result = $parser->parse();
var_dump($result->options);
var_dump($result->args);

?>
--EXPECT--
array(11) {
  ["true"]=>
  bool(true)
  ["false"]=>
  bool(false)
  ["int"]=>
  int(3)
  ["float"]=>
  float(4)
  ["string"]=>
  string(3) "foo"
  ["counter"]=>
  int(4)
  ["callback"]=>
  string(20) "foo__fbzrfgevat__bar"
  ["array"]=>
  array(3) {
    [0]=>
    string(3) "foo"
    [1]=>
    string(3) "bar"
    [2]=>
    string(3) "baz"
  }
  ["password"]=>
  NULL
  ["help"]=>
  NULL
  ["version"]=>
  NULL
}
array(2) {
  ["simple"]=>
  string(3) "foo"
  ["multiple"]=>
  array(1) {
    [0]=>
    string(3) "bar"
  }
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_4.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (errors 1).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
-d 2>&1
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

try {
    $parser = buildParser1();
    $result = $parser->parse();
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>
--EXPECT--
Error: Unknown option "-d".
Type "some_program --help" to get help.


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_5.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (errors 2).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--float 2>&1
--FILE--
<?php

require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'tests.inc.php';

try {
    $parser = buildParser1();
    $result = $parser->parse();
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>
--EXPECT--
Error: Option "float" requires a value.
Type "some_program --help" to get help.


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_6.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (errors 3).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
--float=1.2 2>&1
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

try {
    $parser = buildParser1();
    $result = $parser->parse();
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>
--EXPECT--
Error: You must provide at least 1 argument.
Type "some_program --help" to get help.


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_7.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (special cases 1).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
-t -- -f - --float=1.2 foo 2>&1
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

try {
    $parser = buildParser1();
    $result = $parser->parse();
    var_dump($result);
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>
--EXPECTF--
object(PEAR2\Console\CommandLine\Result)#%d (4) {
  ["options"]=>
  array(11) {
    ["true"]=>
    bool(true)
    ["false"]=>
    NULL
    ["int"]=>
    int(1)
    ["float"]=>
    float(1)
    ["string"]=>
    NULL
    ["counter"]=>
    NULL
    ["callback"]=>
    NULL
    ["array"]=>
    array(2) {
      [0]=>
      string(4) "spam"
      [1]=>
      string(3) "egg"
    }
    ["password"]=>
    NULL
    ["help"]=>
    NULL
    ["version"]=>
    NULL
  }
  ["args"]=>
  array(2) {
    ["simple"]=>
    string(2) "-f"
    ["multiple"]=>
    array(3) {
      [0]=>
      string(1) "-"
      [1]=>
      string(11) "--float=1.2"
      [2]=>
      string(3) "foo"
    }
  }
  ["command_name"]=>
  bool(false)
  ["command"]=>
  bool(false)
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_8.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (special cases 2).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
-t foo bar -f 2>&1
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

try {
    $parser = buildParser1();
    $parser->force_posix = true;
    $result = $parser->parse();
    var_dump($result);
} catch (PEAR2\Console\CommandLine\Exception $exc) {
    $parser->displayError($exc->getMessage());
}

?>
--EXPECTF--
object(PEAR2\Console\CommandLine\Result)#%d (4) {
  ["options"]=>
  array(11) {
    ["true"]=>
    bool(true)
    ["false"]=>
    NULL
    ["int"]=>
    int(1)
    ["float"]=>
    float(1)
    ["string"]=>
    NULL
    ["counter"]=>
    NULL
    ["callback"]=>
    NULL
    ["array"]=>
    array(2) {
      [0]=>
      string(4) "spam"
      [1]=>
      string(3) "egg"
    }
    ["password"]=>
    NULL
    ["help"]=>
    NULL
    ["version"]=>
    NULL
  }
  ["args"]=>
  array(2) {
    ["simple"]=>
    string(3) "foo"
    ["multiple"]=>
    array(2) {
      [0]=>
      string(3) "bar"
      [1]=>
      string(2) "-f"
    }
  }
  ["command_name"]=>
  bool(false)
  ["command"]=>
  bool(false)
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_parse_9.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() method (password option).
--SKIPIF--
<?php if (php_sapi_name()!='cli') {
    echo 'skip';
} ?>
--ARGS--
-p -- foo bar
--STDIN--
secretpass
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
$result = $parser->parse();
var_dump($result->options);
var_dump($result->args);

?>
--EXPECT--
Password: array(11) {
  ["true"]=>
  NULL
  ["false"]=>
  NULL
  ["int"]=>
  int(1)
  ["float"]=>
  float(1)
  ["string"]=>
  NULL
  ["counter"]=>
  NULL
  ["callback"]=>
  NULL
  ["array"]=>
  array(2) {
    [0]=>
    string(4) "spam"
    [1]=>
    string(3) "egg"
  }
  ["password"]=>
  string(10) "secretpass"
  ["help"]=>
  NULL
  ["version"]=>
  NULL
}
array(2) {
  ["simple"]=>
  string(3) "foo"
  ["multiple"]=>
  array(1) {
    [0]=>
    string(3) "bar"
  }
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_webrequest_1.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() with a web request 1
--CGI--
--GET--
version=1
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
$parser->parse();

?>
--EXPECT--
some_program version 0.1.0.


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_webrequest_2.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() with a web request 2
--CGI--
--GET--
help
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
$parser->parse();

?>
--EXPECT--
Description of our parser goes here...

Usage:
  some_program [options] simple [multiple1 multiple2 ...]

Options:
  -t, --true                        test the StoreTrue action
  -f, --false                       test the StoreFalse action
  --int=INT                         test the StoreInt action
  --float=FLOAT                     test the StoreFloat action
  -s STRING, --string=STRING        test the StoreString action
  -c, --counter                     test the Counter action
  --callback=callback               test the Callback action
  -a ARRAY, --array=ARRAY           test the StoreArray action
  -p password, --password=password  test the Password action
  -h, --help                        show this help message and exit
  -v, --version                     show the program version and exit

Arguments:
  simple    test a simple argument
  multiple  test a multiple argument


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\console_commandline_webrequest_3.phpt
--TEST--
Test for PEAR2\Console\CommandLine::parse() with a web request 3
--CGI--
--POST--
true=1&false=1&string=foo&int=3&float=4.0&callback=somestring&-a[]=foo&-a[]=bar&-a[]=baz&simple=foo&multiple=bar
--FILE--
<?php

require_once __DIR__ . DIRECTORY_SEPARATOR . 'tests.inc.php';

$parser = buildParser1();
$result = $parser->parse();
var_dump($result->options);
var_dump($result->args);

?>
--EXPECT--
array(11) {
  ["true"]=>
  bool(true)
  ["false"]=>
  bool(false)
  ["int"]=>
  int(3)
  ["float"]=>
  float(4)
  ["string"]=>
  string(3) "foo"
  ["counter"]=>
  NULL
  ["callback"]=>
  string(20) "foo__fbzrfgevat__bar"
  ["array"]=>
  array(3) {
    [0]=>
    string(3) "foo"
    [1]=>
    string(3) "bar"
    [2]=>
    string(3) "baz"
  }
  ["password"]=>
  NULL
  ["help"]=>
  NULL
  ["version"]=>
  NULL
}
array(2) {
  ["simple"]=>
  string(3) "foo"
  ["multiple"]=>
  array(1) {
    [0]=>
    string(3) "bar"
  }
}


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\test.xml
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<!-- Some comment -->
<command>
    <force_posix>true</force_posix>
    <name>test</name>
    <description>zip/unzip files</description>
    <version>1.0.0</version>
    <!-- Comment -->
    <option name="choice">
        <short_name>-c</short_name>
        <long_name>--choice</long_name>
        <description>choice option</description>
        <action>StoreString</action>
        <!-- Comment -->
        <choices>
            <choice>ham</choice>
            <choice>spam</choice>
        </choices>
        <add_list_option>true</add_list_option>
        <default>null</default>
        <help_name>choice</help_name>
    </option>
    <option name="password">
        <action>Password</action>
        <short_name>-p</short_name>
        <long_name>--password</long_name>
        <description>zip file password</description>
    </option>
    <option name="verbose">
        <long_name>--verbose</long_name>
        <description>turn on verbose output</description>
        <action>StoreTrue</action>
        <short_name>-v</short_name>
    </option>
    <command>
        <aliases>
            <alias>compress</alias>
            <alias>zp</alias>
        </aliases>
        <name>zip</name>
        <!-- Comment -->
        <description>zip given files in the destination file</description>
        <argument name="files">
            <description>a list of files to zip together</description>
            <multiple>true</multiple>
        </argument>
        <argument name="zipfile">
            <!-- Comment -->
            <description>path to the zip file to generate</description>
        </argument>
    </command>
    <command>
        <argument name="outputdir">
            <description>destination directory</description>
        </argument>
        <name>unzip</name>
        <aliases>
            <alias>uzp</alias>
        </aliases>
        <description>unzip given file in the destination dir</description>
        <argument name="zipfile">
            <description>path to the zip file to unzip</description>
        </argument>
    </command>
</command>


File: /src\Libs\pear2\vendor\pear2\console_commandline\tests\tests.inc.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 */

// ensure that errors will be printed
error_reporting(E_ALL | E_STRICT);
ini_set('display_errors', true);

//Add the source folder to the autoloader
require_once 'PEAR2/Autoload.php';
$oldCwd = getcwd();
chdir(__DIR__);
\PEAR2\Autoload::initialize(realpath('../src'));
chdir($oldCwd);

/**
 * A dummy callback for tests purposes.
 * 
 * @param mixed  $value  value provided by the user
 * @param object $option the option instance
 * @param object $result the result instance
 * @param object $parser the parser instance
 * @param array  $params optional params array
 * 
 * @return string
 */
function rot13Callback($value, $option, $result, $parser, $params=array())
{
    $ret = '';
    if (isset($params['prefix'])) {
        $ret .= $params['prefix'] . '__';
    }
    $ret .= str_rot13($value);
    if (isset($params['suffix'])) {
        $ret .= '__' . $params['suffix'];
    }
    return $ret;
}

// }}}
// buildParser1() {{{

/**
 * Build a parser instance and return it.
 *
 * @return object PEAR2\Console\CommandLine instance
 */
function buildParser1()
{
    $parser              = new PEAR2\Console\CommandLine();
    $parser->name        = 'some_program';
    $parser->version     = '0.1.0';
    $parser->description = 'Description of our parser goes here...';

    // add options
    $parser->addOption(
        'true',
        array(
            'short_name'  => '-t',
            'long_name'   => '--true',
            'action'      => 'StoreTrue',
            'description' => 'test the StoreTrue action'
        )
    );
    $parser->addOption(
        'false',
        array(
            'short_name'  => '-f',
            'long_name'   => '--false',
            'action'      => 'StoreFalse',
            'description' => 'test the StoreFalse action'
        )
    );
    $parser->addOption(
        'int',
        array(
            'long_name'   => '--int',
            'action'      => 'StoreInt',
            'description' => 'test the StoreInt action',
            'help_name'   => 'INT',
            'default'     => 1
        )
    );
    $parser->addOption(
        'float',
        array(
            'long_name'   => '--float',
            'action'      => 'StoreFloat',
            'description' => 'test the StoreFloat action',
            'help_name'   => 'FLOAT',
            'default'     => 1.0
        )
    );
    $parser->addOption(
        'string',
        array(
            'short_name'  => '-s',
            'long_name'   => '--string',
            'action'      => 'StoreString',
            'description' => 'test the StoreString action',
            'help_name'   => 'STRING',
            'choices'     => array('foo', 'bar', 'baz')
        )
    );
    $parser->addOption(
        'counter',
        array(
            'short_name'  => '-c',
            'long_name'   => '--counter',
            'action'      => 'Counter',
            'description' => 'test the Counter action'
        )
    );
    $parser->addOption(
        'callback',
        array(
            'long_name'     => '--callback',
            'action'        => 'Callback',
            'description'   => 'test the Callback action',
            'callback'      => 'rot13Callback',
            'action_params' => array('prefix' => 'foo', 'suffix' => 'bar')
        )
    );
    $parser->addOption(
        'array',
        array(
            'short_name'  => '-a',
            'long_name'   => '--array',
            'default'     => array('spam', 'egg'),
            'action'      => 'StoreArray',
            'help_name'   => 'ARRAY',
            'description' => 'test the StoreArray action'
        )
    );
    $parser->addOption(
        'password',
        array(
            'short_name'  => '-p',
            'long_name'   => '--password',
            'action'      => 'Password',
            'description' => 'test the Password action'
        )
    );
    $parser->addArgument(
        'simple',
        array(
            'description' => 'test a simple argument'
        )
    );
    $parser->addArgument(
        'multiple',
        array(
            'description' => 'test a multiple argument',
            'multiple'    => true,
            'optional'    => true
        )
    );
    return $parser;
}

// }}}
// buildParser2() {{{

/**
 * Build a parser instance and return it.
 *
 * @return object PEAR2\Console\CommandLine instance
 */
function buildParser2()
{
    $parser              = new PEAR2\Console\CommandLine();
    $parser->name        = 'some_program';
    $parser->version     = '0.1.0';
    $parser->description = 'Description of our parser goes here...';

    // add general options
    $parser->addOption(
        'verbose',
        array(
            'short_name'  => '-v',
            'long_name'   => '--verbose',
            'action'      => 'StoreTrue',
            'description' => 'verbose mode'
        )
    );
    $parser->addOption(
        'logfile',
        array(
            'short_name'  => '-l',
            'long_name'   => '--logfile',
            'action'      => 'StoreString',
            'description' => 'path to logfile'
        )
    );
 
    // install subcommand
    $cmd1 = $parser->addCommand(
        'install',
        array(
            'description' => 'install given package',
            'aliases'     => array('inst', 'instbis'),
        )
    );
    $cmd1->addOption(
        'force',
        array(
            'short_name'  => '-f',
            'long_name'   => '--force',
            'action'      => 'StoreTrue',
            'description' => 'force installation'
        )
    );
    $cmd1->addArgument(
        'package',
        array(
            'description' => 'package to install'
        )
    );

    // uninstall subcommand
    $cmd2 = $parser->addCommand(
        'uninstall',
        array(
            'description' => 'uninstall given package'
        )
    );
    $cmd2->addArgument(
        'package',
        array(
            'description' => 'package to uninstall'
        )
    );
    return $parser;
}

// }}}
// buildParser3() {{{

/**
 * Build a parser instance and return it.
 *
 * @return object PEAR2\Console\CommandLine instance
 */
function buildParser3()
{
    $parser              = new PEAR2\Console\CommandLine();
    $parser->name        = 'some_program';
    $parser->version     = '0.1.0';
    $parser->description = 'Description of our parser goes here...';
    // we force options default values
    $parser->force_options_defaults = true;

    // add options
    $parser->addOption(
        'true',
        array(
            'short_name'  => '-t',
            'long_name'   => '--true',
            'action'      => 'StoreTrue',
            'description' => 'test the StoreTrue action',
        )
    );
    $parser->addOption(
        'false',
        array(
            'short_name'  => '-f',
            'long_name'   => '--false',
            'action'      => 'StoreFalse',
            'description' => 'test the StoreFalse action',
        )
    );
    $parser->addOption(
        'int',
        array(
            'long_name'   => '--int',
            'action'      => 'StoreInt',
            'description' => 'test the StoreInt action',
            'help_name'   => 'INT',
        )
    );
    $parser->addOption(
        'float',
        array(
            'long_name'   => '--float',
            'action'      => 'StoreFloat',
            'description' => 'test the StoreFloat action',
            'help_name'   => 'FLOAT',
        )
    );
    $parser->addOption(
        'string',
        array(
            'short_name'  => '-s',
            'long_name'   => '--string',
            'action'      => 'StoreString',
            'description' => 'test the StoreString action',
            'help_name'   => 'STRING',
            'choices'     => array('foo', 'bar', 'baz')
        )
    );
    $parser->addOption(
        'counter',
        array(
            'short_name'  => '-c',
            'long_name'   => '--counter',
            'action'      => 'Counter',
            'description' => 'test the Counter action'
        )
    );
    $parser->addOption(
        'callback',
        array(
            'long_name'     => '--callback',
            'action'        => 'Callback',
            'description'   => 'test the Callback action',
            'callback'      => 'rot13Callback',
            'action_params' => array('prefix' => 'foo', 'suffix' => 'bar')
        )
    );
    $parser->addOption(
        'array',
        array(
            'short_name'  => '-a',
            'long_name'   => '--array',
            'action'      => 'StoreArray',
            'help_name'   => 'ARRAY',
            'description' => 'test the StoreArray action'
        )
    );
    $parser->addOption(
        'password',
        array(
            'short_name'  => '-p',
            'long_name'   => '--password',
            'action'      => 'Password',
            'description' => 'test the Password action'
        )
    );
    return $parser;
}

// }}}
// {{{ buildParser4()

/**
 * Build a parser instance and return it.
 *
 * For testing custom messages.
 *
 * @return object Console_CommandLine instance
 */
function buildParser4()
{
    $parser = new PEAR2\Console\CommandLine(
        array(
            'messages' => array(
                'INVALID_SUBCOMMAND' => 'Only "upgrade" is supported.',
            ),
        )
    );
    $parser->name        = 'some_program';
    $parser->version     = '0.1.0';
    $parser->description = 'Description of our parser goes here...';

    // some subcommand
    $cmd1 = $parser->addCommand(
        'upgrade',
        array(
            'description' => 'upgrade given package',
            'aliases'     => array('up'),
            'messages'    => array(
                'ARGUMENT_REQUIRED'       => 'Package name is required.',
                'OPTION_VALUE_REQUIRED'   => 'Option requires value.',
                'OPTION_VALUE_UNEXPECTED' => 'Option should not have a value.',
                'OPTION_UNKNOWN'          => 'Mysterious option encountered.',
            ),
        )
    );
    // add option
    $cmd1->addOption(
        'state',
        array(
            'short_name'  => '-s',
            'long_name'   => '--state',
            'action'      => 'StoreString',
            'choices'     => array('stable', 'beta'),
            'description' => 'accepted package states',
            'messages'    => array(
                'OPTION_VALUE_NOT_VALID' => 'Valid states are "stable" and "beta".',
            ),
        )
    );
    // add another option
    $cmd1->addOption(
        'dry_run',
        array(
            'short_name'  => '-d',
            'long_name'   => '--dry-run',
            'action'      => 'StoreTrue',
            'description' => 'dry run',
        )
    );
    // add argument
    $cmd1->addArgument(
        'package',
        array(
            'description' => 'package to upgrade'
        )
    );

    return $parser;
}

// }}}
// CustomRenderer() {{{

/**
 * Some custom renderer for tests purposes.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 */
class CustomRenderer implements \PEAR2\Console\CommandLine\Renderer
{
    // usage() {{{

    /**
     * Return the full usage message
     *
     * @return string the usage message
     * @access public
     */
    public function usage()
    {
        return __METHOD__ . '()';
    }
    // }}}
    // error() {{{

    /**
     * Return a formatted error message
     *
     * @param string $error the error message to format
     *
     * @return string the error string
     * @access public
     */
    public function error($error)
    {
        return __METHOD__ . "($error)";
    }

    // }}}
    // version() {{{

    /**
     * Return the program version string
     *
     * @return string the version string
     * @access public
     */
    public function version()
    {
        return __METHOD__ . '()';
    }

    // }}}
}

// }}}
// CustomOutputter() {{{

/**
 * Some custom outputter for tests purposes.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 */
class CustomOutputter implements \PEAR2\Console\CommandLine\Outputter
{
    // stdout() {{{

    /**
     * Called for stdout messages.
     *
     * @param string $msg the message to output
     *
     * @return void
     * @access public
     */
    public function stdout($msg)
    {
        echo "STDOUT >> $msg\n";
    }

    // }}}
    // stderr() {{{

    /**
     * Called for stderr messages.
     *
     * @param string $msg the message to output
     *
     * @return void
     * @access public
     */
    public function stderr($msg)
    {
        echo "STDERR >> $msg\n";
    }

    // }}}
}

// }}}
// CustomMessageProvider() {{{

/**
 * Some custom message provider for tests purposes.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 */
class CustomMessageProvider implements \PEAR2\Console\CommandLine\MessageProvider
{
    // get() {{{

    /**
     * Retrieve the given string identifier corresponding message.
     *
     * @param string $code the string identifier of the message
     * @param array  $vars an array of template variables
     *
     * @return string
     * @access public
     */
    public function get($code, $vars = array())
    {
        return $code;
    }

    // }}}
}

// }}}

?>


File: /src\Libs\pear2\vendor\pear2\net_routeros\.gitmodules
[submodule "docs/wiki"]
	path = docs/wiki
	url = https://github.com/pear2/Net_RouterOS.wiki.git


File: /src\Libs\pear2\vendor\pear2\net_routeros\composer.json
{
    "name": "pear2/net_routeros",
    "description": "This package allows you to read and write information from a RouterOS host using MikroTik's RouterOS API.",
    "keywords": ["routeros", "package", "api", "mikrotik", "pear2", "router"],
    "homepage": "http://pear2.github.com/Net_RouterOS/",
    "license": "LGPL-2.1",
    "authors": [
        {
            "name": "Vasil Rangelov",
            "email": "boen.robot@gmail.com",
            "role": "lead"
        }
    ],
    "support": {
        "issues": "https://github.com/pear2/Net_RouterOS/issues",
        "wiki": "https://github.com/pear2/Net_RouterOS/wiki"
    },
    "require": {
        "php": ">=5.3.0",
        "pear2/net_transmitter": ">=1.0.0b1"
    },
    "require-dev": {
        "phpunit/phpunit": "@stable",
        "squizlabs/php_codesniffer": "@stable",
        "pear2/cache_shm": "dev-develop",
        "pear2/console_commandline": "dev-master",
        "pear2/console_color": "dev-develop"
    },
    "suggest": {
        "pear2/cache_shm": "Enables persistent connections.",
        "pear2/console_commandline": "Enables the console",
        "pear2/console_color": "Enables colors in the console",
        "ext-apc": "This, APCu or Wincache is required for persistent connections.",
        "ext-apcu": "This, APC or Wincache is required for persistent connections.",
        "ext-wincache": "This, APC or APCu is required for persistent connections. Reccomended for Windows.",
        "ext-openssl": "Enables encrypted connections."
    },
    "autoload": {
        "psr-0": {
            "PEAR2\\Net\\RouterOS\\": "src/",
            "PEAR2\\Net\\Transmitter\\": "vendor/pear2/net_transmitter/src/",
            "PEAR2\\Cache\\SHM": "vendor/pear2/cache_shm/src/",
            "PEAR2\\Console\\Color": "vendor/pear2/console_color/src/"
        }
    },
    "bin": ["scripts/roscon.php"],
    "minimum-stability": "dev"
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\data\roscon.xml
<?xml version="1.0" encoding="UTF-8"?>
<command>
    <description>RouterOS API console.</description>
    <version>GIT: $Id$</version>
    <argument name="hostname">
        <description>Hostname of the RouterOS to connect to.</description>
    </argument>
    <argument name="username">
        <description>Username to log in with. If left empty, no login will be performed.</description>
        <optional>true</optional>
    </argument>
    <argument name="password">
        <description>Password to log in with.</description>
        <optional>true</optional>
    </argument>
    <option name="portNum">
        <short_name>-p</short_name>
        <long_name>--port</long_name>
        <description>Port to connect to. Default is either 8728 or 8729, depending on whether an encryption is specified.</description>
        <action>StoreInt</action>
    </option>
    <option name="conTime">
        <long_name>--cTimeout</long_name>
        <description>Time in seconds to wait for the connection to be established. If "--timeout" is specified, its value will be used when this option is not specified.
Defaults to PHP's default_socket_timeout ini option.</description>
        <action>StoreInt</action>
    </option>
    <option name="crypto">
        <long_name>--enc</long_name>
        <description>Encryption to use, if at all. Currently, RouterOS supports only "TLS".
(Default: "")</description>
        <action>StoreString</action>
    </option>
    <option name="caPath">
        <long_name>--ca</long_name>
        <description>Optional path to a file or folder to use for certification authority, when using encryption. Ignored when not using encryption or using ADH cipher.</description>
        <action>StoreString</action>
    </option>
    <option name="time">
        <short_name>-t</short_name>
        <long_name>--timeout</long_name>
        <description>Time in seconds to wait when receiving. If this time passes without data awaiting, control is passed back for further input.
(Default: 3)</description>
        <action>StoreInt</action>
    </option>
    <option name="verbose">
        <short_name>-v</short_name>
        <long_name>--verbose</long_name>
        <description>Turn on verbose output.</description>
        <action>StoreTrue</action>
    </option>
    <option name="isColored">
        <long_name>--colors</long_name>
        <description>Choose whether to color output (requires PEAR2_Console_Color). Possible values:
"auto" - color is always enabled, except on Windows, where ANSICON must be installed (detected via the ANSICON_VER environment variable).
"yes"  - force colored output.
"no"   - force no coloring of output.
(Default: "auto")</description>
        <action>StoreString</action>
        <choices>
            <choice>auto</choice>
            <choice>yes</choice>
            <choice>no</choice>
        </choices>
        <default>auto</default>
    </option>
    <option name="size">
        <short_name>-w</short_name>
        <long_name>--width</long_name>
        <description>Width of console screen. Used in verbose mode to wrap output in this length.
(Default: 80)</description>
        <action>StoreInt</action>
        <default>80</default>
    </option>
    <option name="commandMode">
        <long_name>--command-mode</long_name>
        <description>Mode to send commands in. Can be one of:
"w" - send every word as soon as it is entered
"s" - wait for a sentence to be formed, and send all its words then
"e" - wait for an empty sentence, and send all previous sentences then. You can send an empty sentence by sending two consecutive empty words.
(Default: "s")</description>
        <action>StoreString</action>
        <choices>
            <choice>w</choice>
            <choice>s</choice>
            <choice>e</choice>
        </choices>
        <default>s</default>
    </option>
    <option name="replyMode">
        <long_name>--reply-mode</long_name>
        <description>Mode to get replies in. Can be one of:
"w" - after every send, try to get a word
"s" - after every send, try to get a sentence
"e" - after every send, try to get all sentences until a timeout.
(Default: "s")</description>
        <action>StoreString</action>
        <choices>
            <choice>w</choice>
            <choice>s</choice>
            <choice>e</choice>
        </choices>
        <default>s</default>
    </option>
    <option name="multiline">
        <short_name>-m</short_name>
        <long_name>--multiline</long_name>
        <description>Turn on multiline mode. Without this mode, every line of input is considered a word. With it, every line is a line within the word, and the end of the word is marked instead by an "end of text" character as the only character on a line. To write out such a character, you can use ALT+Numpad3. If you want to write this character as part of the word, you can write two such characters on a line.</description>
        <action>StoreTrue</action>
    </option>
</command>


File: /src\Libs\pear2\vendor\pear2\net_routeros\scripts\roscon
#!/usr/bin/env php
<?php

/**
 * ~~summary~~
 * 
 * ~~description~~
 * 
 * PHP version 5.3
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */

/**
 * Run the console.
 */
require_once dirname(__FILE__) . DIRECTORY_SEPARATOR . 'roscon.php';


File: /src\Libs\pear2\vendor\pear2\net_routeros\scripts\roscon.bat
@echo off
:: Prefer PHP binary in the following order:
:: 1. Whatever %PHPBIN% points to.
:: 2. "php" from %cd% with one of %pathext% extensions.
:: 3. "php" from a %path% path with one of %pathext% extensions.
:: 4. Whatever %PHP_PEAR_PHP_BIN% points to.
::
:: Once a binary is found, a file is looked for that has the same name
:: (including folder) as this batch file.
:: Preferred extensions are ".php" and then no extension.
::
:: On failure to find PHP binary or a PHP file, this batch file returns 255.
goto SET_BIN
:PHP_ERR
echo PHP interpreter not found. Please set the %%PHPBIN%% or %%PHP_PEAR_PHP_BIN%% environment variable to one, or add one to your %%PATH%%.
setlocal
goto :END
:FILE_ERR
echo The file to be ran was not found. It should be at either "%~d0%~p0%~n0.php" or "%~d0%~p0%~n0".
goto :END
:SET_BIN
if "%PHPBIN%" == "" set PHPBIN=php
where /q %PHPBIN%
if %ERRORLEVEL% == 0 goto SET_FILE
if "%PHP_PEAR_PHP_BIN%" == "" goto PHP_ERR
where /q "%PHP_PEAR_PHP_BIN%" 2>nul
if %ERRORLEVEL% neq 0 goto PHP_ERR
set PHPBIN=%PHP_PEAR_PHP_BIN%
:SET_FILE
setlocal
set PHPFILE=%~d0%~p0%~n0.php
if exist "%PHPFILE%" goto RUN
set PHPFILE=%~d0%~p0%~n0
if exist "%PHPFILE%" goto RUN
goto FILE_ERR
:RUN
"%PHPBIN%" "%PHPFILE%" %*
set PHPBIN_ERRORLEVEL="%ERRORLEVEL%"
:END
if "%PHPBIN_ERRORLEVEL%" == "" set PHPBIN_ERRORLEVEL=255
exit /B %PHPBIN_ERRORLEVEL%


File: /src\Libs\pear2\vendor\pear2\net_routeros\scripts\roscon.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5.3
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */

/**
 * Used as a "catch all" for errors when connecting.
 */
use Exception as E;

/**
 * Used to register dependency paths, if needed.
 */
use PEAR2\Autoload;

/**
 * Used for coloring the output, if the "--colors" argument is specified.
 */
use PEAR2\Console\Color;

/**
 * Used for parsing the command line arguments.
 */
use PEAR2\Console\CommandLine;

/**
 * The whole application is around that.
 */
use PEAR2\Net\RouterOS;

/**
 * Used for error handling when connecting or receiving.
 */
use PEAR2\Net\Transmitter\SocketException as SE;

//Detect disallowed direct runs of either this file or "roscon".
if (PHP_SAPI !== 'cli') {
    $includedFiles = get_included_files();
    $rosconPos = array_search(
        dirname(__FILE__) . DIRECTORY_SEPARATOR . 'roscon',
        $includedFiles,
        true
    );
    if (false !== $rosconPos) {
        unset($includedFiles[$rosconPos]);
    }

    if (count($includedFiles) === 1) {
        header('Content-Type: text/plain;charset=UTF-8');
        echo <<<HEREDOC
For security reasons, this file can not be ran DIRECTLY, except from the
command line. It can be included however, even when not using the command line.
HEREDOC;
        return;
    }
}

//If there's no appropriate autoloader, add one
if (!class_exists('PEAR2\Net\RouterOS\Communicator', true)) {
    $cwd = getcwd();
    chdir(__DIR__);

    $composerAutoloaderPaths = array();
    $vendorDir = getenv('COMPOSER_VENDOR_DIR');
    if (false !== $vendorDir) {
        $composerAutoloaderPaths[] = $vendorDir . '/autoload.php';
        unset($vendorDir);
    }
    $composerAutoloaderPaths[] = '../vendor/autoload.php';
    $composerAutoloaderPaths[] = '../../../autoload.php';
    foreach ($composerAutoloaderPaths as $autoloaderPath) {
        $autoloader = stream_resolve_include_path($autoloaderPath);
        if (false !== $autoloader) {
            include_once $autoloader;
            if (class_exists('PEAR2\Net\RouterOS\Communicator', true)) {
                break;
            }
            $autoloader = false;
        }
    }
    unset($autoloaderPath, $composerAutoloaderPaths);
    if (false === $autoloader) {
        //PEAR2_Autoload, most probably installed globally.
        $autoloader = stream_resolve_include_path('PEAR2/Autoload.php');
        if (false !== $autoloader) {
            include_once $autoloader;
            Autoload::initialize(
                realpath('../src')
            );
            Autoload::initialize(
File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\Client.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Refers to transmitter direction constants.
 */
use PEAR2\Net\Transmitter\Stream as S;

/**
 * Refers to the cryptography constants.
 */
use PEAR2\Net\Transmitter\NetworkStream as N;

/**
 * Catches arbitrary exceptions at some points.
 */
use Exception as E;

/**
 * A RouterOS client.
 *
 * Provides functionality for easily communicating with a RouterOS host.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Client
{
    /**
     * Used in {@link static::isRequestActive()} to limit search only to
     * requests that have a callback.
     */
    const FILTER_CALLBACK = 1;
    /**
     * Used in {@link static::isRequestActive()} to limit search only to
     * requests that use the buffer.
     */
    const FILTER_BUFFER = 2;
    /**
     * Used in {@link static::isRequestActive()} to indicate no limit in search.
     */
    const FILTER_ALL = 3;

    /**
     * The communicator for this client.
     *
     * @var Communicator
     */
    protected $com;

    /**
     * The number of currently pending requests.
     *
     * @var int
     */
    protected $pendingRequestsCount = 0;

    /**
     * An array of responses that have not yet been extracted
     * or passed to a callback.
     *
     * Key is the tag of the request, and the value is an array of
     * associated responses.
     *
     * @var array<string,Response[]>
     */
    protected $responseBuffer = array();

    /**
     * An array of callbacks to be executed as responses come.
     *
     * Key is the tag of the request, and the value is the callback for it.
     *
     * @var array<string,callback>
     */
    protected $callbacks = array();

    /**
     * A registry for the operations.
     *
     * Particularly helpful at persistent connections.
     *
     * @var Registry
     */
    protected $registry = null;

    /**
     * Stream response words that are above this many bytes.
     * NULL to disable streaming completely.
     *
     * @var int|null
     */
    private $_streamingResponses = null;

    /**
     * Creates a new instance of a RouterOS API client.
     *
     * Creates a new instance of a RouterOS API client with the specified
     * settings.
     *
     * @param string        $host     Hostname (IP or domain) of RouterOS.
     * @param string        $username The RouterOS username.
     * @param string        $password The RouterOS password.
     * @param int|null      $port     The port on which the RouterOS host
     *     provides the API service. You can also specify NULL, in which case
     *     the port will automatically be chosen between 8728 and 8729,
     *     depending on the value of $crypto.
     * @param bool          $persist  Whether or not the connection should be a
     *     persistent one.
     * @param double|null   $timeout  The timeout for the connection.
     * @param string        $crypto   The encryption for this connection.
     *     Must be one of the PEAR2\Net\Transmitter\NetworkStream::CRYPTO_*
     *     constants. Off by default. RouterOS currently supports only TLS, but
     *     the setting is provided in this fashion for forward compatibility's
     *     sake. And for the sake of simplicity, if you specify an encryption,
     *     don't specify a context and your default context uses the value
     *     "DEFAULT" for ciphers, "ADH" will be automatically added to the list
     *     of ciphers.
     * @param resource|null $context  A context for the socket.
     *
     * @see sendSync()
     * @see sendAsync()
     */
    public function __construct(
        $host,
        $username,
        $password = '',
        $port = 8728,
        $persist = false,
        $timeout = null,
        $crypto = N::CRYPTO_OFF,
        $context = null
    ) {
        $this->com = new Communicator(
            $host,
            $port,
            $persist,
            $timeout,
            $username . '/' . $password,
            $crypto,
            $context
        );
        $timeout = null == $timeout
            ? ini_get('default_socket_timeout')
            : (int) $timeout;
        //Login the user if necessary
        if ((!$persist
                || !($old = $this->com->getTransmitter()->lock(S::DIRECTION_ALL)))
            && $this->com->getTransmitter()->isFresh()
        ) {
            if (!static::login($this->com, $username, $password, $timeout)) {
                $this->com->close();
                throw new DataFlowException(
                    'Invalid username or password supplied.',
                    DataFlowException::CODE_INVALID_CREDENTIALS
                );
            }
        }

        if (isset($old)) {
            $this->com->getTransmitter()->lock($old, true);
        }

        if ($persist) {
            $this->registry = new Registry("{$host}:{$port}/{$username}");
        }
    }

    /**
     * A shorthand gateway.
     *
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     *
     * @param mixed $arg Value can be either a {@link Request} to send, which
     *     would be sent asynchronously if it has a tag, and synchronously if
     *     not, a number to loop with or NULL to complete all pending requests.
     *     Any other value is converted to string and treated as the tag of a
     *     request to complete.
     *
     * @return mixed Whatever the long form function would have returned.
     */
    public function __invoke($arg = null)
    {
        if (is_int($arg) || is_double($arg)) {
            return $this->loop($arg);
        } elseif ($arg instanceof Request) {
            return '' == $arg->getTag() ? $this->sendSync($arg)
                : $this->sendAsync($arg);
        } elseif (null === $arg) {
            return $this->completeRequest();
        }
        return $this->completeRequest((string) $arg);
    }

    /**
     * Login to a RouterOS connection.
     *
     * @param Communicator $com      The communicator to attempt to login to.
     * @param string       $username The RouterOS username.
     * @param string       $password The RouterOS password.
     * @param int|null     $timeout  The time to wait for each response. NULL
     *     waits indefinitely.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function login(
        Communicator $com,
        $username,
        $password = '',
        $timeout = null
    ) {
        if (null !== ($remoteCharset = $com->getCharset($com::CHARSET_REMOTE))
            && null !== ($localCharset = $com->getCharset($com::CHARSET_LOCAL))
        ) {
            $password = iconv(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $password
            );
        }
        $old = null;
        try {
            if ($com->getTransmitter()->isPersistent()) {
                $old = $com->getTransmitter()->lock(S::DIRECTION_ALL);
                $result = self::_login($com, $username, $password, $timeout);
                $com->getTransmitter()->lock($old, true);
                return $result;
            }
            return self::_login($com, $username, $password, $timeout);
        } catch (E $e) {
            if ($com->getTransmitter()->isPersistent() && null !== $old) {
                $com->getTransmitter()->lock($old, true);
            }
            throw ($e instanceof NotSupportedException
                || $e instanceof UnexpectedValueException
                || !$com->getTransmitter()->isDataAwaiting()) ? new SocketException(
                'This is not a compatible RouterOS service',
                SocketException::CODE_SERVICE_INCOMPATIBLE,
                $e
            ) : $e;
        }
    }

    /**
     * Login to a RouterOS connection.
     *
     * This is the actual login procedure, applied regardless of persistence and
     * charset settings.
     *
     * @param Communicator $com      The communicator to attempt to login to.
     * @param string       $username The RouterOS username.
     * @param string       $password The RouterOS password. Potentially parsed
     *     already by iconv.
     * @param int|null     $timeout  The time to wait for each response. NULL
     *     waits indefinitely.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    private static function _login(
        Communicator $com,
        $username,
        $password = '',
        $timeout = null
    ) {
        $request = new Request('/login');
        $request->setArgument('name', $username);
        $request->setArgument('password', $password);
        $oldCharset = $com->getCharset($com::CHARSET_ALL);
        $com->setCharset(null, $com::CHARSET_ALL);
        $request->verify($com)->send($com);
        $com->setCharset($oldCharset, $com::CHARSET_ALL);
        $response = new Response($com, false, $timeout);
        if ($response->getType() === Response::TYPE_FINAL
            && null === $response->getProperty('ret')
        ) {
            // version >= 6.43
            return null === $response->getProperty('message');
        } elseif ($response->getType() === Response::TYPE_FINAL) {
            // version < 6.43
            $request->setArgument('password', '');
            $request->setArgument(
                'response',
                '00' . md5(
                    chr(0) . $password
                    . pack(
                        'H*',
                        is_string($response->getProperty('ret'))
                            ? $response->getProperty('ret')
                            : stream_get_contents($response->getProperty('ret'))
                    )
                )
            );
            $request->verify($com)->send($com);
            $response = new Response($com, false, $timeout);
            if ($response->getType() === Response::TYPE_FINAL) {
                return null === $response->getProperty('ret');
            }
        }
        while ($response->getType() !== Response::TYPE_FINAL
            && $response->getType() !== Response::TYPE_FATAL
        ) {
            $response = new Response($com, false, $timeout);
        }
        return false;
    }

    /**
     * Sets the charset(s) for this connection.
     *
     * Sets the charset(s) for this connection. The specified charset(s) will be
     * used for all future requests and responses. When sending,
     * {@link Communicator::CHARSET_LOCAL} is converted to
     * {@link Communicator::CHARSET_REMOTE}, and when receiving,
     * {@link Communicator::CHARSET_REMOTE} is converted to
     * {@link Communicator::CHARSET_LOCAL}. Setting NULL to either charset will
     * disable charset conversion, and data will be both sent and received "as
     * is".
     *
     * @param mixed $charset     The charset to set. If $charsetType is
     *     {@link Communicator::CHARSET_ALL}, you can supply either a string to
     *     use for all charsets, or an array with the charset types as keys, and
     *     the charsets as values.
     * @param int   $charsetType Which charset to set. Valid values are the
     *     Communicator::CHARSET_* constants. Any other value is treated as
     *     {@link Communicator::CHARSET_ALL}.
     *
     * @return string|array The old charset. If $charsetType is
     *     {@link Communicator::CHARSET_ALL}, the old values will be returned as
     *     an array with the types as keys, and charsets as values.
     *
     * @see Communicator::setDefaultCharset()
     */
    public function setCharset(
        $charset,
        $charsetType = Communicator::CHARSET_ALL
    ) {
        return $this->com->setCharset($charset, $charsetType);
    }

    /**
     * Gets the charset(s) for this connection.
     *
     * @param int $charsetType Which charset to get. Valid values are the
     *     Communicator::CHARSET_* constants. Any other value is treated as
     *     {@link Communicator::CHARSET_ALL}.
     *
     * @return string|array The current charset. If $charsetType is
     *     {@link Communicator::CHARSET_ALL}, the current values will be
     *     returned as an array with the types as keys, and charsets as values.
     *
     * @see setCharset()
     */
    public function getCharset($charsetType)
    {
        return $this->com->getCharset($charsetType);
    }

    /**
     * Sends a request and waits for responses.
     *
     * @param Request       $request  The request to send.
     * @param callback|null $callback Optional. A function that is to be
     *     executed when new responses for this request are available.
     *     The callback takes two parameters. The {@link Response} object as
     *     the first, and the {@link Client} object as the second one. If the
     *     callback returns TRUE, the request is canceled. Note that the
     *     callback may be executed at least two times after that. Once with a
     *     {@link Response::TYPE_ERROR} response that notifies about the
     *     canceling, plus the {@link Response::TYPE_FINAL} response.
     *
     * @return $this The client object.
     *
     * @see completeRequest()
     * @see loop()
     * @see cancelRequest()
     */
    public function sendAsync(Request $request, $callback = null)
    {
        //Error checking
        $tag = $request->getTag();
        if ('' === (string)$tag) {
            throw new DataFlowException(
                'Asynchonous commands must have a tag.',
                DataFlowException::CODE_TAG_REQUIRED
            );
        }
        if ($this->isRequestActive($tag)) {
            throw new DataFlowException(
                'There must not be multiple active requests sharing a tag.',
                DataFlowException::CODE_TAG_UNIQUE
            );
        }
        if (null !== $callback && !is_callable($callback, true)) {
            throw new UnexpectedValueException(
                'Invalid callback provided.',
                UnexpectedValueException::CODE_CALLBACK_INVALID
            );
        }

        $this->send($request);

        if (null === $callback) {
            //Register the request at the buffer
            $this->responseBuffer[$tag] = array();
        } else {
            //Prepare the callback
            $this->callbacks[$tag] = $callback;
        }
        return $this;
    }

    /**
     * Checks if a request is active.
     *
     * Checks if a request is active. A request is considered active if it's a
     * pending request and/or has responses that are not yet extracted.
     *
     * @param string $tag    The tag of the request to look for.
     * @param int    $filter One of the FILTER_* constants. Limits the search
     *     to the specified places.
     *
     * @return bool TRUE if the request is active, FALSE otherwise.
     *
     * @see getPendingRequestsCount()
     * @see completeRequest()
     */
    public function isRequestActive($tag, $filter = self::FILTER_ALL)
    {
        $result = 0;
        if ($filter & self::FILTER_CALLBACK) {
            $result |= (int) array_key_exists($tag, $this->callbacks);
        }
        if ($filter & self::FILTER_BUFFER) {
            $result |= (int) array_key_exists($tag, $this->responseBuffer);
        }
        return 0 !== $result;
    }

    /**
     * Sends a request and gets the full response.
     *
     * @param Request $request The request to send.
     *
     * @return ResponseCollection The received responses as a collection.
     *
     * @see sendAsync()
     * @see close()
     */
    public function sendSync(Request $request)
    {
        $tag = $request->getTag();
        if ('' == $tag) {
            $this->send($request);
        } else {
            $this->sendAsync($request);
        }
        return $this->completeRequest($tag);
    }

    /**
     * Completes a specified request.
     *
     * Starts an event loop for the RouterOS callbacks and finishes when a
     * specified request is completed.
     *
     * @param string|null $tag The tag of the request to complete.
     *     Setting NULL completes all requests.
     *
     * @return ResponseCollection A collection of {@link Response} objects that
     *     haven't been passed to a callback function or previously extracted
     *     with {@link static::extractNewResponses()}. Returns an empty
     *     collection when $tag is set to NULL (responses can still be
     *     extracted).
     */
    public function completeRequest($tag = null)
    {
        $hasNoTag = '' == $tag;
        $result = $hasNoTag ? array()
            : $this->extractNewResponses($tag)->toArray();
        while ((!$hasNoTag && $this->isRequestActive($tag))
            || ($hasNoTag && 0 !== $this->getPendingRequestsCount())
        ) {
            $newReply = $this->dispatchNextResponse(null);
            if ($newReply->getTag() === $tag) {
                if ($hasNoTag) {
                    $result[] = $newReply;
                }
                if ($newReply->getType() === Response::TYPE_FINAL) {
                    if (!$hasNoTag) {
                        $result = array_merge(
                            $result,
                            $this->isRequestActive($tag)
                                ? $this->extractNewResponses($tag)->toArray()
                                : array()
                        );
                    }
                    break;
                }
            }
        }
        return new ResponseCollection($result);
    }

    /**
     * Extracts responses for a request.
     *
     * Gets all new responses for a request that haven't been passed to a
     * callback and clears the buffer from them.
     *
     * @param string|null $tag The tag of the request to extract
     *     new responses for.
     *     Specifying NULL with extract new responses for all requests.
     *
     * @return ResponseCollection A collection of {@link Response} objects for
     *     the specified request.
     *
     * @see loop()
     */
    public function extractNewResponses($tag = null)
    {
        if (null === $tag) {
            $result = array();
            foreach (array_keys($this->responseBuffer) as $tag) {
                $result = array_merge(
                    $result,
                    $this->extractNewResponses($tag)->toArray()
                );
            }
            return new ResponseCollection($result);
        } elseif ($this->isRequestActive($tag, self::FILTER_CALLBACK)) {
            return new ResponseCollection(array());
        } elseif ($this->isRequestActive($tag, self::FILTER_BUFFER)) {
            $result = $this->responseBuffer[$tag];
            if (!empty($result)) {
                if (end($result)->getType() === Response::TYPE_FINAL) {
                    unset($this->responseBuffer[$tag]);
                } else {
                    $this->responseBuffer[$tag] = array();
                }
            }
            return new ResponseCollection($result);
        } else {
            throw new DataFlowException(
                'No such request, or the request has already finished.',
                DataFlowException::CODE_UNKNOWN_REQUEST
            );
        }
    }

    /**
     * Starts an event loop for the RouterOS callbacks.
     *
     * Starts an event loop for the RouterOS callbacks and finishes when there
     * are no more pending requests or when a specified timeout has passed
     * (whichever comes first).
     *
     * @param int|null $sTimeout  Timeout for the loop.
     *     If NULL, there is no time limit.
     * @param int      $usTimeout Microseconds to add to the time limit.
     *
     * @return bool TRUE when there are any more pending requests, FALSE
     *     otherwise.
     *
     * @see extractNewResponses()
     * @see getPendingRequestsCount()
     */
    public function loop($sTimeout = null, $usTimeout = 0)
    {
        try {
            if (null === $sTimeout) {
                while ($this->getPendingRequestsCount() !== 0) {
                    $this->dispatchNextResponse(null);
                }
            } else {
                list($usStart, $sStart) = explode(' ', microtime());
                while ($this->getPendingRequestsCount() !== 0
                    && ($sTimeout >= 0 || $usTimeout >= 0)
                ) {
                    $this->dispatchNextResponse($sTimeout, $usTimeout);
                    list($usEnd, $sEnd) = explode(' ', microtime());

                    $sTimeout -= $sEnd - $sStart;
                    $usTimeout -= $usEnd - $usStart;
                    if ($usTimeout <= 0) {
                        if ($sTimeout > 0) {
                            $usTimeout = 1000000 + $usTimeout;
                            $sTimeout--;
                        }
                    }

                    $sStart = $sEnd;
                    $usStart = $usEnd;
                }
            }
        } catch (SocketException $e) {
            if ($e->getCode() !== SocketException::CODE_NO_DATA) {
                // @codeCoverageIgnoreStart
                // It's impossible to reliably cause any other SocketException.
                // This line is only here in case the unthinkable happens:
                // The connection terminates just after it was supposedly
                // about to send back some data.
                throw $e;
                // @codeCoverageIgnoreEnd
            }
        }
        return $this->getPendingRequestsCount() !== 0;
    }

    /**
     * Gets the number of pending requests.
     *
     * @return int The number of pending requests.
     *
     * @see isRequestActive()
     */
    public function getPendingRequestsCount()
    {
        return $this->pendingRequestsCount;
    }

    /**
     * Cancels a request.
     *
     * Cancels an active request. Using this function in favor of a plain call
     * to the "/cancel" command is highly recommended, as it also updates the
     * counter of pending requests properly. Note that canceling a request also
     * removes any responses for it that were not previously extracted with
     * {@link static::extractNewResponses()}.
     *
     * @param string|null $tag Tag of the request to cancel.
     *     Setting NULL will cancel all requests.
     *
     * @return $this The client object.
     *
     * @see sendAsync()
     * @see close()
     */
    public function cancelRequest($tag = null)
    {
        $cancelRequest = new Request('/cancel');
        $hasTag = !('' === (string)$tag);
        $hasReg = null !== $this->registry;
        if ($hasReg && !$hasTag) {
            $tags = array_merge(
                array_keys($this->responseBuffer),
                array_keys($this->callbacks)
            );
            $this->registry->setTaglessMode(true);
            foreach ($tags as $t) {
                $cancelRequest->setArgument(
                    'tag',
                    $this->registry->getOwnershipTag() . $t
                );
                $this->sendSync($cancelRequest);
            }
            $this->registry->setTaglessMode(false);
        } else {
            if ($hasTag) {
                if ($this->isRequestActive($tag)) {
                    if ($hasReg) {
                        $this->registry->setTaglessMode(true);
                        $cancelRequest->setArgument(
                            'tag',
                            $this->registry->getOwnershipTag() . $tag
                        );
                    } else {
                        $cancelRequest->setArgument('tag', $tag);
                    }
                } else {
                    throw new DataFlowException(
                        'No such request. Canceling aborted.',
                        DataFlowException::CODE_CANCEL_FAIL
                    );
                }
            }
            $this->sendSync($cancelRequest);
            if ($hasReg) {
                $this->registry->setTaglessMode(false);
            }
        }

        if ($hasTag) {
            if ($this->isRequestActive($tag, self::FILTER_BUFFER)) {
                $this->responseBuffer[$tag] = $this->completeRequest($tag);
            } else {
                $this->completeRequest($tag);
            }
        } else {
            $this->loop();
        }
        return $this;
    }

    /**
     * Sets response streaming setting.
     *
     * Sets when future response words are streamed. If a word is streamed,
     * the property value is returned a stream instead of a string, and
     * unrecognized words are returned entirely as streams instead of strings.
     * This is particularly useful if you expect a response that may contain
     * one or more very large words.
     *
     * @param int|null $threshold Threshold after which to stream
     *     a word. That is, a word less than this length will not be streamed.
     *     If set to 0, effectively all words are streamed.
     *     NULL to disable streaming altogether.
     *
     * @return $this The client object.
     *
     * @see getStreamingResponses()
     */
    public function setStreamingResponses($threshold)
    {
        $this->_streamingResponses = $threshold === null
            ? null
            : (int) $threshold;
        return $this;
    }

    /**
     * Gets response streaming setting.
     *
     * Gets when future response words are streamed.
     *
     * @return int|null The value of the setting.
     *
     * @see setStreamingResponses()
     */
    public function getStreamingResponses()
    {
        return $this->_streamingResponses;
    }

    /**
     * Closes the opened connection, even if it is a persistent one.
     *
     * Closes the opened connection, even if it is a persistent one. Note that
     * {@link static::extractNewResponses()} can still be used to extract
     * responses collected prior to the closing.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function close()
    {
        $result = true;
        /*
         * The check below is done because for some unknown reason
         * (either a PHP or a RouterOS bug) calling "/quit" on an encrypted
         * connection makes one end hang.
         *
         * Since encrypted connections only appeared in RouterOS 6.1, and
         * the "/quit" call is needed for all <6.0 versions, problems due
         * to its absence should be limited to some earlier 6.* versions
         * on some RouterBOARD devices.
         */
        if ($this->com->getTransmitter()->getCrypto() === N::CRYPTO_OFF) {
            if (null !== $this->registry) {
                $this->registry->setTaglessMode(true);
            }
            try {
                $response = $this->sendSync(new Request('/quit'));
                $result = $response[0]->getType() === Response::TYPE_FATAL;
            } catch (SocketException $e) {
                $result
                    = $e->getCode() === SocketException::CODE_REQUEST_SEND_FAIL;
            } catch (E $e) {
                //Ignore unknown errors.
            }
            if (null !== $this->registry) {
                $this->registry->setTaglessMode(false);
            }
        }
        $result = $result && $this->com->close();
        $this->callbacks = array();
        $this->pendingRequestsCount = 0;
        return $result;
    }

    /**
     * Closes the connection, unless it's a persistent one.
     */
    public function __destruct()
    {
        if ($this->com->getTransmitter()->isPersistent()) {
            if (0 !== $this->pendingRequestsCount) {
                $this->cancelRequest();
            }
        } else {
            $this->close();
        }
    }

    /**
     * Sends a request to RouterOS.
     *
     * @param Request $request The request to send.
     *
     * @return $this The client object.
     *
     * @see sendSync()
     * @see sendAsync()
     */
    protected function send(Request $request)
    {
        $request->verify($this->com)->send($this->com, $this->registry);
        $this->pendingRequestsCount++;
        return $this;
    }

    /**
     * Dispatches the next response in queue.
     *
     * Dispatches the next response in queue, i.e. it executes the associated
     * callback if there is one, or places the response in the response buffer.
     *
     * @param int|null $sTimeout  If a response is not immediately available,
     *     wait this many seconds.
     *     If NULL, wait indefinitely.
     * @param int      $usTimeout Microseconds to add to the waiting time.
     *
     * @return Response  The dispatched response.
     * @throws SocketException When there's no response within the time limit.
     */
    protected function dispatchNextResponse($sTimeout = 0, $usTimeout = 0)
    {
        $response = new Response(
            $this->com,
            $this->_streamingResponses,
            $sTimeout,
            $usTimeout,
            $this->registry
        );
        if ($response->getType() === Response::TYPE_FATAL) {
            $this->pendingRequestsCount = 0;
            $this->com->close();
            return $response;
        }

        $tag = $response->getTag();
        $isLastForRequest = $response->getType() === Response::TYPE_FINAL;
        if ($isLastForRequest) {
            $this->pendingRequestsCount--;
        }

        if ('' !== (string)$tag) {
            if ($this->isRequestActive($tag, self::FILTER_CALLBACK)) {
                if ($this->callbacks[$tag]($response, $this)) {
                    try {
                        $this->cancelRequest($tag);
                    } catch (DataFlowException $e) {
                        if ($e->getCode() !== $e::CODE_UNKNOWN_REQUEST
                        ) {
                            throw $e;
                        }
                    }
                } elseif ($isLastForRequest) {
                    unset($this->callbacks[$tag]);
                }
            } else {
                $this->responseBuffer[$tag][] = $response;
            }
        }
        return $response;
    }
}

File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\Communicator.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Using transmitters.
 */
use PEAR2\Net\Transmitter as T;

/**
 * A RouterOS communicator.
 *
 * Implementation of the RouterOS API protocol. Unlike the other classes in this
 * package, this class doesn't provide any conveniences beyond the low level
 * implementation details (automatic word length encoding/decoding, charset
 * translation and data integrity), and because of that, its direct usage is
 * strongly discouraged.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 * @see      Client
 */
class Communicator
{
    /**
     * Used when getting/setting all (default) charsets.
     */
    const CHARSET_ALL = -1;

    /**
     * Used when getting/setting the (default) remote charset.
     *
     * The remote charset is the charset in which RouterOS stores its data.
     * If you want to keep compatibility with your Winbox, this charset should
     * match the default charset from your Windows' regional settings.
     */
    const CHARSET_REMOTE = 0;

    /**
     * Used when getting/setting the (default) local charset.
     *
     * The local charset is the charset in which the data from RouterOS will be
     * returned as. This charset should match the charset of the place the data
     * will eventually be written to.
     */
    const CHARSET_LOCAL = 1;

    /**
     * An array with the default charset.
     *
     * Charset types as keys, and the default charsets as values.
     *
     * @var array<string,string|null>
     */
    protected static $defaultCharsets = array(
        self::CHARSET_REMOTE => null,
        self::CHARSET_LOCAL  => null
    );

    /**
     * An array with the current charset.
     *
     * Charset types as keys, and the current charsets as values.
     *
     * @var array<string,string|null>
     */
    protected $charsets = array();

    /**
     * The transmitter for the connection.
     *
     * @var T\TcpClient
     */
    protected $trans;

    /**
     * Creates a new connection with the specified options.
     *
     * @param string        $host    Hostname (IP or domain) of RouterOS.
     * @param int|null      $port    The port on which the RouterOS host
     *     provides the API service. You can also specify NULL, in which case
     *     the port will automatically be chosen between 8728 and 8729,
     *     depending on the value of $crypto.
     * @param bool          $persist Whether or not the connection should be a
     *     persistent one.
     * @param double|null   $timeout The timeout for the connection.
     * @param string        $key     A string that uniquely identifies the
     *     connection.
     * @param string        $crypto  The encryption for this connection.
     *     Must be one of the PEAR2\Net\Transmitter\NetworkStream::CRYPTO_*
     *     constants. Off by default. RouterOS currently supports only TLS, but
     *     the setting is provided in this fashion for forward compatibility's
     *     sake. And for the sake of simplicity, if you specify an encryption,
     *     don't specify a context and your default context uses the value
     *     "DEFAULT" for ciphers, "ADH" will be automatically added to the list
     *     of ciphers.
     * @param resource|null $context A context for the socket.
     *
     * @see sendWord()
     */
    public function __construct(
        $host,
        $port = 8728,
        $persist = false,
        $timeout = null,
        $key = '',
        $crypto = T\NetworkStream::CRYPTO_OFF,
        $context = null
    ) {
        $isUnencrypted = T\NetworkStream::CRYPTO_OFF === $crypto;
        if (($context === null) && !$isUnencrypted) {
            $context = stream_context_get_default();
            $opts = stream_context_get_options($context);
            if (!isset($opts['ssl']['ciphers'])
                || 'DEFAULT' === $opts['ssl']['ciphers']
            ) {
                stream_context_set_option(
                    $context,
                    array(
                        'ssl' => array(
                            'ciphers' => 'ADH',
                            'verify_peer' => false,
                            'verify_peer_name' => false
                        )
                    )
                );
            }
        }
        // @codeCoverageIgnoreStart
        // The $port is customizable in testing.
        if (null === $port) {
            $port = $isUnencrypted ? 8728 : 8729;
        }
        // @codeCoverageIgnoreEnd

        try {
            $this->trans = new T\TcpClient(
                $host,
                $port,
                $persist,
                $timeout,
                $key,
                $crypto,
                $context
            );
        } catch (T\Exception $e) {
            throw new SocketException(
                'Error connecting to RouterOS',
                SocketException::CODE_CONNECTION_FAIL,
                $e
            );
        }
        $this->setCharset(
            self::getDefaultCharset(self::CHARSET_ALL),
            self::CHARSET_ALL
        );
    }

    /**
     * A shorthand gateway.
     *
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     *
     * @param string|null $string A string of the word to send, or NULL to get
     *     the next word as a string.
     *
     * @return int|string If a string is provided, returns the number of bytes
     *     sent, otherwise returns the next word as a string.
     */
    public function __invoke($string = null)
    {
        return null === $string ? $this->getNextWord()
            : $this->sendWord($string);
    }

    /**
     * Checks whether a variable is a seekable stream resource.
     *
     * @param mixed $var The value to check.
     *
     * @return bool TRUE if $var is a seekable stream, FALSE otherwise.
     */
    public static function isSeekableStream($var)
    {
        if (T\Stream::isStream($var)) {
            $meta = stream_get_meta_data($var);
            return $meta['seekable'];
        }
        return false;
    }

    /**
     * Uses iconv to convert a stream from one charset to another.
     *
     * @param string   $inCharset  The charset of the stream.
     * @param string   $outCharset The desired resulting charset.
     * @param resource $stream     The stream to convert. The stream is assumed
     *     to be seekable, and is read from its current position to its end,
     *     after which, it is seeked back to its starting position.
     *
     * @return resource A new stream that uses the $out_charset. The stream is a
     *     subset from the original stream, from its current position to its
     *     end, seeked at its start.
     */
    public static function iconvStream($inCharset, $outCharset, $stream)
    {
        $bytes = 0;
        $result = fopen('php://temp', 'r+b');
        $iconvFilter = stream_filter_append(
            $result,
            'convert.iconv.' . $inCharset . '.' . $outCharset,
            STREAM_FILTER_WRITE
        );

        flock($stream, LOCK_SH);
        $reader = new T\Stream($stream, false);
        $writer = new T\Stream($result, false);
        $chunkSize = $reader->getChunk(T\Stream::DIRECTION_RECEIVE);
        while ($reader->isAvailable() && $reader->isDataAwaiting()) {
            $bytes += $writer->send(fread($stream, $chunkSize));
        }
        fseek($stream, -$bytes, SEEK_CUR);
        flock($stream, LOCK_UN);

        stream_filter_remove($iconvFilter);
        rewind($result);
        return $result;
    }

    /**
     * Sets the default charset(s) for new connections.
     *
     * @param mixed $charset     The charset to set. If $charsetType is
     *     {@link self::CHARSET_ALL}, you can supply either a string to use for
     *     all charsets, or an array with the charset types as keys, and the
     *     charsets as values.
     * @param int   $charsetType Which charset to set. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     *
     * @return string|array The old charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the old values will be returned as an
     *     array with the types as keys, and charsets as values.
     *
     * @see setCharset()
     */
    public static function setDefaultCharset(
        $charset,
        $charsetType = self::CHARSET_ALL
    ) {
        if (array_key_exists($charsetType, self::$defaultCharsets)) {
             $oldCharset = self::$defaultCharsets[$charsetType];
             self::$defaultCharsets[$charsetType] = $charset;
             return $oldCharset;
        } else {
            $oldCharsets = self::$defaultCharsets;
            self::$defaultCharsets = is_array($charset) ? $charset : array_fill(
                0,
                count(self::$defaultCharsets),
                $charset
            );
            return $oldCharsets;
        }
    }

    /**
     * Gets the default charset(s).
     *
     * @param int $charsetType Which charset to get. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     *
     * @return string|array The current charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the current values will be returned as an
     *     array with the types as keys, and charsets as values.
     *
     * @see setDefaultCharset()
     */
    public static function getDefaultCharset($charsetType)
    {
        return array_key_exists($charsetType, self::$defaultCharsets)
            ? self::$defaultCharsets[$charsetType] : self::$defaultCharsets;
    }

    /**
     * Gets the length of a seekable stream.
     *
     * Gets the length of a seekable stream.
     *
     * @param resource $stream The stream to check. The stream is assumed to be
     *     seekable.
     *
     * @return double The number of bytes in the stream between its current
     *     position and its end.
     */
    public static function seekableStreamLength($stream)
    {
        $streamPosition = (double) sprintf('%u', ftell($stream));
        fseek($stream, 0, SEEK_END);
        $streamLength = ((double) sprintf('%u', ftell($stream)))
            - $streamPosition;
        fseek($stream, $streamPosition, SEEK_SET);
        return $streamLength;
    }

    /**
     * Sets the charset(s) for this connection.
     *
     * Sets the charset(s) for this connection. The specified charset(s) will be
     * used for all future words. When sending, {@link self::CHARSET_LOCAL} is
     * converted to {@link self::CHARSET_REMOTE}, and when receiving,
     * {@link self::CHARSET_REMOTE} is converted to {@link self::CHARSET_LOCAL}.
     * Setting  NULL to either charset will disable charset conversion, and data
     * will be both sent and received "as is".
     *
     * @param mixed $charset     The charset to set. If $charsetType is
     *     {@link self::CHARSET_ALL}, you can supply either a string to use for
     *     all charsets, or an array with the charset types as keys, and the
     *     charsets as values.
     * @param int   $charsetType Which charset to set. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     *
     * @return string|array The old charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the old values will be returned as an
     *     array with the types as keys, and charsets as values.
     *
     * @see setDefaultCharset()
     */
    public function setCharset($charset, $charsetType = self::CHARSET_ALL)
    {
        if (array_key_exists($charsetType, $this->charsets)) {
             $oldCharset = $this->charsets[$charsetType];
             $this->charsets[$charsetType] = $charset;
             return $oldCharset;
        } else {
            $oldCharsets = $this->charsets;
            $this->charsets = is_array($charset) ? $charset : array_fill(
                0,
                count($this->charsets),
                $charset
            );
            return $oldCharsets;
        }
    }

    /**
     * Gets the charset(s) for this connection.
     *
     * @param int $charsetType Which charset to get. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     *
     * @return string|array The current charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the current values will be returned as an
     *     array with the types as keys, and charsets as values.
     *
     * @see getDefaultCharset()
     * @see setCharset()
     */
    public function getCharset($charsetType)
    {
        return array_key_exists($charsetType, $this->charsets)
            ? $this->charsets[$charsetType] : $this->charsets;
    }

    /**
     * Gets the transmitter for this connection.
     *
     * @return T\TcpClient The transmitter for this connection.
     */
    public function getTransmitter()
    {
        return $this->trans;
    }

    /**
     * Sends a word.
     *
     * Sends a word and automatically encodes its length when doing so.
     *
     * @param string $word The word to send.
     *
     * @return int The number of bytes sent.
     *
     * @see sendWordFromStream()
     * @see getNextWord()
     */
    public function sendWord($word)
    {
        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $word = iconv(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $word
            );
        }
        $length = strlen($word);
        static::verifyLengthSupport($length);
        if ($this->trans->isPersistent()) {
            $old = $this->trans->lock(T\Stream::DIRECTION_SEND);
            $bytes = $this->trans->send(self::encodeLength($length) . $word);
            $this->trans->lock($old, true);
            return $bytes;
        }
        return $this->trans->send(self::encodeLength($length) . $word);
    }

    /**
     * Sends a word based on a stream.
     *
     * Sends a word based on a stream and automatically encodes its length when
     * doing so. The stream is read from its current position to its end, and
     * then returned to its current position. Because of those operations, the
     * supplied stream must be seekable.
     *
     * @param string   $prefix A string to prepend before the stream contents.
     * @param resource $stream The seekable stream to send.
     *
     * @return int The number of bytes sent.
     *
     * @see sendWord()
     */
    public function sendWordFromStream($prefix, $stream)
    {
        if (!self::isSeekableStream($stream)) {
            throw new InvalidArgumentException(
                'The stream must be seekable.',
                InvalidArgumentException::CODE_SEEKABLE_REQUIRED
            );
        }
        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $prefix = iconv(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $prefix
            );
            $stream = self::iconvStream(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $stream
            );
        }

        flock($stream, LOCK_SH);
        $totalLength = strlen($prefix) + self::seekableStreamLength($stream);
        static::verifyLengthSupport($totalLength);

        $bytes = $this->trans->send(self::encodeLength($totalLength) . $prefix);
        $bytes += $this->trans->send($stream);

        flock($stream, LOCK_UN);
        return $bytes;
    }

    /**
     * Verifies that the length is supported.
     *
     * Verifies if the specified length is supported by the API. Throws a
     * {@link LengthException} if that's not the case. Currently, RouterOS
     * supports words up to 0xFFFFFFFF in length, so that's the only check
     * performed.
     *
     * @param int $length The length to verify.
     *
     * @return void
     */
    public static function verifyLengthSupport($length)
    {
        if ($length > 0xFFFFFFFF) {
            throw new LengthException(
                'Words with length above 0xFFFFFFFF are not supported.',
                LengthException::CODE_UNSUPPORTED,
                null,
                $length
            );
        }
    }

    /**
     * Encodes the length as required by the RouterOS API.
     *
     * @param int $length The length to encode.
     *
     * @return string The encoded length.
     */
    public static function encodeLength($length)
    {
        if ($length < 0) {
            throw new LengthException(
                'Length must not be negative.',
                LengthException::CODE_INVALID,
                null,
                $length
            );
        } elseif ($length < 0x80) {
            return chr($length);
        } elseif ($length < 0x4000) {
            return pack('n', $length |= 0x8000);
        } elseif ($length < 0x200000) {
            $length |= 0xC00000;
            return pack('n', $length >> 8) . chr($length & 0xFF);
        } elseif ($length < 0x10000000) {
            return pack('N', $length |= 0xE0000000);
        } elseif ($length <= 0xFFFFFFFF) {
            return chr(0xF0) . pack('N', $length);
        } elseif ($length <= 0x7FFFFFFFF) {
            $length = 'f' . base_convert($length, 10, 16);
            return chr(hexdec(substr($length, 0, 2))) .
                pack('N', hexdec(substr($length, 2)));
        }
        throw new LengthException(
            'Length must not be above 0x7FFFFFFFF.',
            LengthException::CODE_BEYOND_SHEME,
            null,
            $length
        );
    }

    /**
     * Get the next word in queue as a string.
     *
     * Get the next word in queue as a string, after automatically decoding its
     * length.
     *
     * @return string The word.
     *
     * @see close()
     */
    public function getNextWord()
    {
        if ($this->trans->isPersistent()) {
            $old = $this->trans->lock(T\Stream::DIRECTION_RECEIVE);
            $word = $this->trans->receive(
                self::decodeLength($this->trans),
                'word'
            );
            $this->trans->lock($old, true);
        } else {
            $word = $this->trans->receive(
                self::decodeLength($this->trans),
                'word'
            );
        }

        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $word = iconv(
                $remoteCharset,
                $localCharset . '//IGNORE//TRANSLIT',
                $word
            );
        }

        return $word;
    }

    /**
     * Get the next word in queue as a stream.
     *
     * Get the next word in queue as a stream, after automatically decoding its
     * length.
     *
     * @return resource The word, as a stream.
     *
     * @see close()
     */
    public function getNextWordAsStream()
    {
        $filters = new T\FilterCollection();
        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $filters->append(
                'convert.iconv.' .
                $remoteCharset . '.' . $localCharset . '//IGNORE//TRANSLIT'
            );
        }

        if ($this->trans->isPersistent()) {
            $old = $this->trans->lock(T\Stream::DIRECTION_RECEIVE);
            $stream = $this->trans->receiveStream(
                self::decodeLength($this->trans),
                $filters,
                'stream word'
            );
            $this->trans->lock($old, true);
        } else {
            $stream = $this->trans->receiveStream(
                self::decodeLength($this->trans),
                $filters,
                'stream word'
            );
        }

        return $stream;
    }

    /**
     * Decodes the length of the incoming message.
     *
     * Decodes the length of the incoming message, as specified by the RouterOS
     * API.
     *
     * @param T\Stream $trans The transmitter from which to decode the length of
     * the incoming message.
     *
     * @return int|double The decoded length.
     *     Is of type "double" only for values above "2 << 31".
     */
    public static function decodeLength(T\Stream $trans)
    {
        if ($trans->isPersistent() && $trans instanceof T\TcpClient) {
            $old = $trans->lock($trans::DIRECTION_RECEIVE);
            $length = self::_decodeLength($trans);
            $trans->lock($old, true);
            return $length;
        }
        return self::_decodeLength($trans);
    }

    /**
     * Decodes the length of the incoming message.
     *
     * Decodes the length of the incoming message, as specified by the RouterOS
     * API.
     *
     * Difference with the non private function is that this one doesn't perform
     * locking if the connection is a persistent one.
     *
     * @param T\Stream $trans The transmitter from which to decode the length of
     *     the incoming message.
     *
     * @return int|double The decoded length.
     *     Is of type "double" only for values above "2 << 31".
     */
    private static function _decodeLength(T\Stream $trans)
    {
        $byte = ord($trans->receive(1, 'initial length byte'));
        if ($byte & 0x80) {
            if (($byte & 0xC0) === 0x80) {
                return (($byte & 077) << 8 ) + ord($trans->receive(1));
            } elseif (($byte & 0xE0) === 0xC0) {
                $rem = unpack('n~', $trans->receive(2));
                return (($byte & 037) << 16 ) + $rem['~'];
            } elseif (($byte & 0xF0) === 0xE0) {
                $rem = unpack('n~/C~~', $trans->receive(3));
                return (($byte & 017) << 24 ) + ($rem['~'] << 8) + $rem['~~'];
            } elseif (($byte & 0xF8) === 0xF0) {
                $rem = unpack('N~', $trans->receive(4));
                return (($byte & 007) * 0x100000000/* '<< 32' or '2^32' */)
                    + (double) sprintf('%u', $rem['~']);
            }
            throw new NotSupportedException(
                'Unknown control byte encountered.',
                NotSupportedException::CODE_CONTROL_BYTE,
                null,
                $byte
            );
        } else {
            return $byte;
        }
    }

    /**
     * Closes the opened connection, even if it is a persistent one.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function close()
    {
        return $this->trans->close();
    }
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\DataFlowException.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Base of this class.
 */
use RuntimeException;

/**
 * Exception thrown when the request/response cycle goes an unexpected way.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class DataFlowException extends RuntimeException implements Exception
{
    const CODE_INVALID_CREDENTIALS = 10000;
    const CODE_TAG_REQUIRED = 10500;
    const CODE_TAG_UNIQUE = 10501;
    const CODE_UNKNOWN_REQUEST = 10900;
    const CODE_CANCEL_FAIL = 11200;
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\Exception.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Generic exception class of this package.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
interface Exception
{
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\InvalidArgumentException.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

use InvalidArgumentException as I;

/**
 * Exception thrown when there's something wrong with message arguments.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class InvalidArgumentException extends I implements Exception
{
    const CODE_SEEKABLE_REQUIRED = 1100;
    const CODE_NAME_INVALID = 20100;
    const CODE_ABSOLUTE_REQUIRED = 40200;
    const CODE_CMD_UNRESOLVABLE = 40201;
    const CODE_CMD_INVALID = 40202;
    const CODE_NAME_UNPARSABLE = 41000;
    const CODE_VALUE_UNPARSABLE = 41001;
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\LengthException.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Base of this class.
 */
use LengthException as L;

/**
 * Used in $previous
 */
use Exception as E;

/**
 * Exception thrown when there is a problem with a word's length.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class LengthException extends L implements Exception
{

    const CODE_UNSUPPORTED = 1200;
    const CODE_INVALID = 1300;
    const CODE_BEYOND_SHEME = 1301;

    /**
     * The problematic length.
     *
     * @var int|double|null
     */
    private $_length;

    /**
     * Creates a new LengthException.
     *
     * @param string          $message  The Exception message to throw.
     * @param int             $code     The Exception code.
     * @param E|null          $previous The previous exception used for the
     *     exception chaining.
     * @param int|double|null $length   The length.
     */
    public function __construct(
        $message,
        $code = 0,
        E $previous = null,
        $length = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_length = $length;
    }

    /**
     * Gets the length.
     *
     * @return int|double|null The length.
     */
    public function getLength()
    {
        return $this->_length;
    }

    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing

    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        return parent::__toString() . "\nLength:{$this->_length}";
    }

    // @codeCoverageIgnoreEnd
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\Message.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Implements this interface.
 */
use Countable;

/**
 * Implements this interface.
 */
use IteratorAggregate;

/**
 * Required for IteratorAggregate::getIterator() to work properly with foreach.
 */
use ArrayObject;

/**
 * Represents a RouterOS message.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
abstract class Message implements IteratorAggregate, Countable
{

    /**
     * An array with message attributes.
     *
     * Each array key is the the name of an attribute,
     * and the corresponding array value is the value for that attribute.
     *
     * @var array<string,string|resource>
     */
    protected $attributes = array();

    /**
     * An optional tag to associate the message with.
     *
     * @var string
     */
    private $_tag = null;

    /**
     * A shorthand gateway.
     *
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     *
     * @param string|null $name The name of an attribute to get the value of,
     *     or NULL to get the tag.
     *
     * @return string|resource The value of the specified attribute,
     *     or the tag if NULL is provided.
     */
    public function __invoke($name = null)
    {
        if (null === $name) {
            return $this->getTag();
        }
        return $this->getAttribute($name);
    }

    /**
     * Sanitizes a name of an attribute (message or query one).
     *
     * @param mixed $name The name to sanitize.
     *
     * @return string The sanitized name.
     */
    public static function sanitizeAttributeName($name)
    {
        $name = (string) $name;
        if ((empty($name) && $name !== '0')
            || preg_match('/[=\s]/s', $name)
        ) {
            throw new InvalidArgumentException(
                'Invalid name of argument supplied.',
                InvalidArgumentException::CODE_NAME_INVALID
            );
        }
        return $name;
    }

    /**
     * Sanitizes a value of an attribute (message or query one).
     *
     * @param mixed $value The value to sanitize.
     *
     * @return string|resource The sanitized value.
     */
    public static function sanitizeAttributeValue($value)
    {
        if (Communicator::isSeekableStream($value)) {
            return $value;
        } else {
            return (string) $value;
        }
    }

    /**
     * Gets the tag that the message is associated with.
     *
     * @return string The current tag or NULL if there isn't a tag.
     *
     * @see setTag()
     */
    public function getTag()
    {
        return $this->_tag;
    }

    /**
     * Sets the tag to associate the request with.
     *
     * Sets the tag to associate the message with. Setting NULL erases the
     * currently set tag.
     *
     * @param string $tag The tag to set.
     *
     * @return $this The message object.
     *
     * @see getTag()
     */
    protected function setTag($tag)
    {
        $this->_tag = (null === $tag) ? null : (string) $tag;
        return $this;
    }

    /**
     * Gets the value of an attribute.
     *
     * @param string $name The name of the attribute.
     *
     * @return string|resource|null The value of the specified attribute.
     *     Returns NULL if such an attribute is not set.
     *
     * @see setAttribute()
     */
    protected function getAttribute($name)
    {
        $name = self::sanitizeAttributeName($name);
        if (array_key_exists($name, $this->attributes)) {
            return $this->attributes[$name];
        }
        return null;
    }

    /**
     * Gets all arguments in an array.
     *
     * @return ArrayObject An ArrayObject with the keys being argument names,
     *     and the array values being argument values.
     *
     * @see getArgument()
     * @see setArgument()
     */
    public function getIterator()
    {
        return new ArrayObject($this->attributes);
    }

    /**
     * Counts the number of attributes.
     *
     * @return int The number of attributes.
     */
    public function count()
    {
        return count($this->attributes);
    }

    /**
     * Sets an attribute for the message.
     *
     * @param string               $name  Name of the attribute.
     * @param string|resource|null $value Value of the attribute as a string or
     *     seekable stream.
     *     Setting the value to NULL removes an argument of this name.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     *
     * @return $this The message object.
     *
     * @see getArgument()
     */
    protected function setAttribute($name, $value = '')
    {
        if (null === $value) {
            unset($this->attributes[self::sanitizeAttributeName($name)]);
        } else {
            $this->attributes[self::sanitizeAttributeName($name)]
                = self::sanitizeAttributeValue($value);
        }
        return $this;
    }

    /**
     * Removes all attributes from the message.
     *
     * @return $this The message object.
     */
    protected function removeAllAttributes()
    {
        $this->attributes = array();
        return $this;
    }
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\NotSupportedException.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Base of this class.
 */
use Exception as E;

/**
 * Exception thrown when encountering something not supported by RouterOS or
 * this package.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class NotSupportedException extends E implements Exception
{

    const CODE_CONTROL_BYTE = 1601;

    const CODE_MENU_MISMATCH = 60000;

    const CODE_ARG_PROHIBITED = 60001;

    /**
     * The unsupported value.
     *
     * @var mixed
     */
    private $_value;

    /**
     * Creates a new NotSupportedException.
     *
     * @param string $message  The Exception message to throw.
     * @param int    $code     The Exception code.
     * @param E|null $previous The previous exception used for the exception
     *     chaining.
     * @param mixed  $value    The unsupported value.
     */
    public function __construct(
        $message,
        $code = 0,
        E $previous = null,
        $value = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_value = $value;
    }

    /**
     * Gets the unsupported value.
     *
     * @return mixed The unsupported value.
     */
    public function getValue()
    {
        return $this->_value;
    }

    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing

    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        return parent::__toString() . "\nValue:{$this->_value}";
    }

    // @codeCoverageIgnoreEnd
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\ParserException.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Base of this class.
 */
use DomainException;

/**
 * Exception thrown when a value can't be parsed properly.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class ParserException extends DomainException implements Exception
{
    const CODE_DATETIME = 1;
    const CODE_DATEINTERVAL = 2;
    const CODE_ARRAY = 3;
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\Query.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Refers to transmitter direction constants.
 */
use PEAR2\Net\Transmitter as T;

/**
 * Represents a query for RouterOS requests.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Query
{

    /**
     * Checks if the property exists.
     */
    const OP_EX = '';

    /**
     * Checks if the property does not exist.
     */
    const OP_NEX = '-';

    /**
     * Checks if the property equals a certain value.
     */
    const OP_EQ = '=';

    /**
     * Checks if the property is less than a certain value.
     */
    const OP_LT = '<';

    /**
     * Checks if the property is greater than a certain value.
     */
    const OP_GT = '>';

    /**
     * An array of the words forming the query.
     *
     * Each value is an array with the first member being the predicate
     * (operator and name), and the second member being the value
     * for the predicate.
     *
     * @var array<string,string|null>[]
     */
    protected $words = array();

    /**
     * This class is not to be instantiated normally, but by static methods
     * instead. Use {@link static::where()} to create an instance of it.
     */
    protected function __construct()
    {

    }

    /**
     * Sanitizes the operator of a condition.
     *
     * @param string $operator The operator to sanitize.
     *
     * @return string The sanitized operator.
     */
    protected static function sanitizeOperator($operator)
    {
        $operator = (string) $operator;
        switch ($operator) {
        case Query::OP_EX:
        case Query::OP_NEX:
        case Query::OP_EQ:
        case Query::OP_LT:
        case Query::OP_GT:
            return $operator;
        default:
            throw new UnexpectedValueException(
                'Unknown operator specified',
                UnexpectedValueException::CODE_ACTION_UNKNOWN,
                null,
                $operator
            );
        }
    }

    /**
     * Creates a new query with an initial condition.
     *
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the OP_* constants.
     *     Describes the operation to perform.
     *
     * @return static A new query object.
     */
    public static function where(
        $name,
        $value = null,
        $operator = self::OP_EX
    ) {
        $query = new static;
        return $query->addWhere($name, $value, $operator);
    }

    /**
     * Negates the query.
     *
     * @return $this The query object.
     */
    public function not()
    {
        $this->words[] = array('#!', null);
        return $this;
    }

    /**
     * Adds a condition as an alternative to the query.
     *
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the OP_* constants.
     *     Describes the operation to perform.
     *
     * @return $this The query object.
     */
    public function orWhere($name, $value = null, $operator = self::OP_EX)
    {
        $this->addWhere($name, $value, $operator)->words[] = array('#|', null);
        return $this;
    }

    /**
     * Adds a condition in addition to the query.
     *
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the OP_* constants.
     *     Describes the operation to perform.
     *
     * @return $this The query object.
     */
    public function andWhere($name, $value = null, $operator = self::OP_EX)
    {
        $this->addWhere($name, $value, $operator)->words[] = array('#&', null);
        return $this;
    }

    /**
     * Sends the query over a communicator.
     *
     * @param Communicator $com The communicator to send the query over.
     *
     * @return int The number of bytes sent.
     */
    public function send(Communicator $com)
    {
        if ($com->getTransmitter()->isPersistent()) {
            $old = $com->getTransmitter()->lock(T\Stream::DIRECTION_SEND);
            $bytes = $this->_send($com);
            $com->getTransmitter()->lock($old, true);
            return $bytes;
        }
        return $this->_send($com);
    }

    /**
     * Sends the query over a communicator.
     *
     * The only difference with the non private equivalent is that this one does
     * not do locking.
     *
     * @param Communicator $com The communicator to send the query over.
     *
     * @return int The number of bytes sent.
     */
    private function _send(Communicator $com)
    {
        if (!$com->getTransmitter()->isAcceptingData()) {
            throw new SocketException(
                'Transmitter is invalid. Sending aborted.',
                SocketException::CODE_QUERY_SEND_FAIL
            );
        }
        $bytes = 0;
        foreach ($this->words as $queryWord) {
            list($predicate, $value) = $queryWord;
            $prefix = '?' . $predicate;
            if (null === $value) {
                $bytes += $com->sendWord($prefix);
            } else {
                $prefix .= '=';
                if (is_string($value)) {
                    $bytes += $com->sendWord($prefix . $value);
                } else {
                    $bytes += $com->sendWordFromStream($prefix, $value);
                }
            }
        }
        return $bytes;
    }

    /**
     * Verifies the query.
     *
     * Verifies the query against a communicator, i.e. whether the query
     * could successfully be sent (assuming the connection is still opened).
     *
     * @param Communicator $com The Communicator to check against.
     *
     * @return $this The query object itself.
     *
     * @throws LengthException If the resulting length of an API word is not
     *     supported.
     */
    public function verify(Communicator $com)
    {
        foreach ($this->words as $queryWord) {
            list($predicate, $value) = $queryWord;
            if (null === $value) {
                $com::verifyLengthSupport(strlen('?' . $predicate));
            } elseif (is_string($value)) {
                $com::verifyLengthSupport(
                    strlen('?' . $predicate . '=' . $value)
                );
            } else {
                $com::verifyLengthSupport(
                    strlen('?' . $predicate . '=') +
                    $com::seekableStreamLength($value)
                );
            }
        }
        return $this;
    }

    /**
     * Adds a condition.
     *
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the ACTION_* constants.
     *     Describes the operation to perform.
     *
     * @return $this The query object.
     */
    protected function addWhere($name, $value, $operator)
    {
        $this->words[] = array(
            static::sanitizeOperator($operator)
            . Message::sanitizeAttributeName($name),
            (null === $value ? null : Message::sanitizeAttributeValue($value))
        );
        return $this;
    }
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\Registry.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Uses shared memory to keep responses in.
 */
use PEAR2\Cache\SHM;

/**
 * A RouterOS registry.
 *
 * Provides functionality for managing the request/response flow. Particularly
 * useful in persistent connections.
 *
 * Note that this class is not meant to be called directly.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Registry
{
    /**
     * The storage.
     *
     * @var SHM
     */
    protected $shm;

    /**
     * ID of request. Populated at first instance in request.
     *
     * @var int
     */
    protected static $requestId = -1;

    /**
     * ID to be given to next instance, after incrementing it.
     *
     * @var int
     */
    protected static $instanceIdSeed = -1;

    /**
     * ID of instance within the request.
     *
     * @var int
     */
    protected $instanceId;

    /**
     * Creates a registry.
     *
     * @param string $uri An URI to bind the registry to.
     */
    public function __construct($uri)
    {
        $this->shm = SHM::factory(__CLASS__ . ' ' . $uri);
        if (-1 === self::$requestId) {
            self::$requestId = $this->shm->add('requestId', 0)
                ? 0 : $this->shm->inc('requestId');
        }
        $this->instanceId = ++self::$instanceIdSeed;
        $this->shm->add('responseBuffer_' . $this->getOwnershipTag(), array());
    }

    /**
     * Parses a tag.
     *
     * Parses a tag to reveal the ownership part of it, and the original tag.
     *
     * @param string $tag The tag (as received) to parse.
     *
     * @return array<int,string|null> An array with
     *     the first member being the ownership tag, and
     *     the second one being the original tag.
     */
    public static function parseTag($tag)
    {
        if (null === $tag) {
            return array(null, null);
        }
        $result = explode('__', $tag, 2);
        $result[0] .= '__';
        if ('' === $result[1]) {
            $result[1] = null;
        }
        return $result;
    }

    /**
     * Checks if this instance is the tagless mode owner.
     *
     * @return bool TRUE if this instance is the tagless mode owner, FALSE
     *     otherwise.
     */
    public function isTaglessModeOwner()
    {
        $this->shm->lock('taglessModeOwner');
        $result = $this->shm->exists('taglessModeOwner')
            && $this->getOwnershipTag() === $this->shm->get('taglessModeOwner');
        $this->shm->unlock('taglessModeOwner');
        return $result;
    }

    /**
     * Sets the "tagless mode" setting.
     *
     * While in tagless mode, this instance will claim ownership of any
     * responses without a tag. While not in this mode, any requests without a
     * tag will be given to all instances.
     *
     * Regardless of mode, if the type of the response is
     * {@link Response::TYPE_FATAL}, it will be given to all instances.
     *
     * @param bool $taglessMode TRUE to claim tagless ownership, FALSE to
     *     release such ownership, if taken.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setTaglessMode($taglessMode)
    {
        return $taglessMode
            ?   ($this->shm->lock('taglessMode')
                && $this->shm->lock('taglessModeOwner')
                && $this->shm->add('taglessModeOwner', $this->getOwnershipTag())
                && $this->shm->unlock('taglessModeOwner'))
            :   ($this->isTaglessModeOwner()
                && $this->shm->lock('taglessModeOwner')
                && $this->shm->delete('taglessModeOwner')
                && $this->shm->unlock('taglessModeOwner')
                && $this->shm->unlock('taglessMode'));
    }

    /**
     * Get the ownership tag for this instance.
     *
     * @return string The ownership tag for this registry instance.
     */
    public function getOwnershipTag()
    {
        return self::$requestId . '_' . $this->instanceId . '__';
    }

    /**
     * Add a response to the registry.
     *
     * @param Response $response     The response to add. The caller of this
     *     function is responsible for ensuring that the ownership tag and the
     *     original tag are separated, so that only the original one remains in
     *     the response.
     * @param string   $ownershipTag The ownership tag that the response had.
     *
     * @return bool TRUE if the request was added to its buffer, FALSE if
     *     this instance owns the response, and therefore doesn't need to add
     *     the response to its buffer.
     */
    public function add(Response $response, $ownershipTag)
    {
        if ($this->getOwnershipTag() === $ownershipTag
            || ($this->isTaglessModeOwner()
            && $response->getType() !== Response::TYPE_FATAL)
        ) {
            return false;
        }

        if (null === $ownershipTag) {
            $this->shm->lock('taglessModeOwner');
            if ($this->shm->exists('taglessModeOwner')
                && $response->getType() !== Response::TYPE_FATAL
            ) {
                $ownershipTag = $this->shm->get('taglessModeOwner');
                $this->shm->unlock('taglessModeOwner');
            } else {
                $this->shm->unlock('taglessModeOwner');
                foreach ($this->shm->getIterator(
                    '/^(responseBuffer\_)/',
                    true
                ) as $targetBufferName) {
                    $this->_add($response, $targetBufferName);
                }
                return true;
            }
        }

        $this->_add($response, 'responseBuffer_' . $ownershipTag);
        return true;
    }

    /**
     * Adds a response to a buffer.
     *
     * @param Response $response         The response to add.
     * @param string   $targetBufferName The name of the buffer to add the
     *     response to.
     *
     * @return void
     */
    private function _add(Response $response, $targetBufferName)
    {
        if ($this->shm->lock($targetBufferName)) {
            $targetBuffer = $this->shm->get($targetBufferName);
            $targetBuffer[] = $response;
            $this->shm->set($targetBufferName, $targetBuffer);
            $this->shm->unlock($targetBufferName);
        }
    }

    /**
     * Gets the next response from this instance's buffer.
     *
     * @return Response|null The next response, or NULL if there isn't one.
     */
    public function getNextResponse()
    {
        $response = null;
        $targetBufferName = 'responseBuffer_' . $this->getOwnershipTag();
        if ($this->shm->exists($targetBufferName)
            && $this->shm->lock($targetBufferName)
        ) {
            $targetBuffer = $this->shm->get($targetBufferName);
            if (!empty($targetBuffer)) {
                $response = array_shift($targetBuffer);
                $this->shm->set($targetBufferName, $targetBuffer);
            }
            $this->shm->unlock($targetBufferName);
        }
        return $response;
    }

    /**
     * Closes the registry.
     *
     * Closes the registry, meaning that all buffers are cleared.
     *
     * @return void
     */
    public function close()
    {
        self::$requestId = -1;
        self::$instanceIdSeed = -1;
        $this->shm->clear();
    }

    /**
     * Removes a buffer.
     *
     * @param string $targetBufferName The buffer to remove.
     *
     * @return void
     */
    private function _close($targetBufferName)
    {
        if ($this->shm->lock($targetBufferName)) {
            $this->shm->delete($targetBufferName);
            $this->shm->unlock($targetBufferName);
        }
    }

    /**
     * Removes this instance's buffer.
     */
    public function __destruct()
    {
        $this->_close('responseBuffer_' . $this->getOwnershipTag());
    }
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\Request.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Refers to transmitter direction constants.
 */
use PEAR2\Net\Transmitter as T;

/**
 * Represents a RouterOS request.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Request extends Message
{

    /**
     * The command to be executed.
     *
     * @var string
     */
    private $_command;

    /**
     * A query for the command.
     *
     * @var Query
     */
    private $_query;

    /**
     * Creates a request to send to RouterOS.
     *
     * @param string      $command The command to send.
     *     Can also contain arguments expressed in a shell-like syntax.
     * @param Query|null  $query   A query to associate with the request.
     * @param string|null $tag     The tag for the request.
     *
     * @see setCommand()
     * @see setArgument()
     * @see setTag()
     * @see setQuery()
     */
    public function __construct($command, Query $query = null, $tag = null)
    {
        if (false !== strpos($command, '=')
            && false !== ($spaceBeforeEquals = strrpos(
                strstr($command, '=', true),
                ' '
            ))
        ) {
            $this->parseArgumentString(substr($command, $spaceBeforeEquals));
            $command = rtrim(substr($command, 0, $spaceBeforeEquals));
        }
        $this->setCommand($command);
        $this->setQuery($query);
        $this->setTag($tag);
    }

    /**
     * A shorthand gateway.
     *
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     *
     * @param Query|Communicator|string|null $arg A {@link Query} to associate
     *     the request with, a {@link Communicator} to send the request over,
     *     an argument to get the value of, or NULL to get the tag. If a
     *     second argument is provided, this becomes the name of the argument to
     *     set the value of, and the second argument is the value to set.
     *
     * @return string|resource|int|$this Whatever the long form
     *     function returns.
     */
    public function __invoke($arg = null)
    {
        if (func_num_args() > 1) {
            return $this->setArgument(func_get_arg(0), func_get_arg(1));
        }
        if ($arg instanceof Query) {
            return $this->setQuery($arg);
        }
        if ($arg instanceof Communicator) {
            return $this->send($arg);
        }
        return parent::__invoke($arg);
    }

    /**
     * Sets the command to send to RouterOS.
     *
     * Sets the command to send to RouterOS. The command can use the API or CLI
     * syntax of RouterOS, but either way, it must be absolute (begin  with a
     * "/") and without arguments.
     *
     * @param string $command The command to send.
     *
     * @return $this The request object.
     *
     * @see getCommand()
     * @see setArgument()
     */
    public function setCommand($command)
    {
        $command = (string) $command;
        if (strpos($command, '/') !== 0) {
            throw new InvalidArgumentException(
                'Commands must be absolute.',
                InvalidArgumentException::CODE_ABSOLUTE_REQUIRED
            );
        }
        if (substr_count($command, '/') === 1) {
            //Command line syntax convertion
            $cmdParts = preg_split('#[\s/]+#sm', $command);
            $cmdRes = array($cmdParts[0]);
            for ($i = 1, $n = count($cmdParts); $i < $n; $i++) {
                if ('..' === $cmdParts[$i]) {
                    $delIndex = count($cmdRes) - 1;
                    if ($delIndex < 1) {
                        throw new InvalidArgumentException(
                            'Unable to resolve command',
                            InvalidArgumentException::CODE_CMD_UNRESOLVABLE
                        );
                    }
                    unset($cmdRes[$delIndex]);
                    $cmdRes = array_values($cmdRes);
                } else {
                    $cmdRes[] = $cmdParts[$i];
                }
            }
            $command = implode('/', $cmdRes);
        }
        if (!preg_match('#^/\S+$#sm', $command)) {
            throw new InvalidArgumentException(
                'Invalid command supplied.',
                InvalidArgumentException::CODE_CMD_INVALID
            );
        }
        $this->_command = $command;
        return $this;
    }

    /**
     * Gets the command that will be send to RouterOS.
     *
     * Gets the command that will be send to RouterOS in its API syntax.
     *
     * @return string The command to send.
     *
     * @see setCommand()
     */
    public function getCommand()
    {
        return $this->_command;
    }

    /**
     * Sets the query to send with the command.
     *
     * @param Query|null $query The query to be set.
     *     Setting NULL will remove the  currently associated query.
     *
     * @return $this The request object.
     *
     * @see getQuery()
     */
    public function setQuery(Query $query = null)
    {
        $this->_query = $query;
        return $this;
    }

    /**
     * Gets the currently associated query
     *
     * @return Query|null The currently associated query.
     *
     * @see setQuery()
     */
    public function getQuery()
    {
        return $this->_query;
    }

    /**
     * Sets the tag to associate the request with.
     *
     * Sets the tag to associate the request with. Setting NULL erases the
     * currently set tag.
     *
     * @param string|null $tag The tag to set.
     *
     * @return $this The request object.
     *
     * @see getTag()
     */
    public function setTag($tag)
    {
        return parent::setTag($tag);
    }

    /**
     * Sets an argument for the request.
     *
     * @param string               $name  Name of the argument.
     * @param string|resource|null $value Value of the argument as a string or
     *     seekable stream.
     *     Setting the value to NULL removes an argument of this name.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     *
     * @return $this The request object.
     *
     * @see getArgument()
     */
    public function setArgument($name, $value = '')
    {
        return parent::setAttribute($name, $value);
    }

    /**
     * Gets the value of an argument.
     *
     * @param string $name The name of the argument.
     *
     * @return string|resource|null The value of the specified argument.
     *     Returns NULL if such an argument is not set.
     *
     * @see setAttribute()
     */
    public function getArgument($name)
    {
        return parent::getAttribute($name);
    }

    /**
     * Removes all arguments from the request.
     *
     * @return $this The request object.
     */
    public function removeAllArguments()
    {
        return parent::removeAllAttributes();
    }

    /**
     * Sends a request over a communicator.
     *
     * @param Communicator  $com The communicator to send the request over.
     * @param Registry|null $reg An optional registry to sync the request with.
     *
     * @return int The number of bytes sent.
     *
     * @see Client::sendSync()
     * @see Client::sendAsync()
     */
    public function send(Communicator $com, Registry $reg = null)
    {
        if (null !== $reg
            && (null != $this->getTag() || !$reg->isTaglessModeOwner())
        ) {
            $originalTag = $this->getTag();
            $this->setTag($reg->getOwnershipTag() . $originalTag);
            $bytes = $this->send($com);
            $this->setTag($originalTag);
            return $bytes;
        }
        if ($com->getTransmitter()->isPersistent()) {
            $old = $com->getTransmitter()->lock(T\Stream::DIRECTION_SEND);
            $bytes = $this->_send($com);
            $com->getTransmitter()->lock($old, true);
            return $bytes;
        }
        return $this->_send($com);
    }

    /**
     * Sends a request over a communicator.
     *
     * The only difference with the non private equivalent is that this one does
     * not do locking.
     *
     * @param Communicator $com The communicator to send the request over.
     *
     * @return int The number of bytes sent.
     *
     * @see Client::sendSync()
     * @see Client::sendAsync()
     */
    private function _send(Communicator $com)
    {
        if (!$com->getTransmitter()->isAcceptingData()) {
            throw new SocketException(
                'Transmitter is invalid. Sending aborted.',
                SocketException::CODE_REQUEST_SEND_FAIL
            );
        }
        $bytes = 0;
        $bytes += $com->sendWord($this->getCommand());
        if (null !== ($tag = $this->getTag())) {
            $bytes += $com->sendWord('.tag=' . $tag);
        }
        foreach ($this->attributes as $name => $value) {
            $prefix = '=' . $name . '=';
            if (is_string($value)) {
                $bytes += $com->sendWord($prefix . $value);
            } else {
                $bytes += $com->sendWordFromStream($prefix, $value);
            }
        }
        $query = $this->getQuery();
        if ($query instanceof Query) {
            $bytes += $query->send($com);
        }
        $bytes += $com->sendWord('');
        return $bytes;
    }

    /**
     * Verifies the request.
     *
     * Verifies the request against a communicator, i.e. whether the request
     * could successfully be sent (assuming the connection is still opened).
     *
     * @param Communicator $com The Communicator to check against.
     *
     * @return $this The request object itself.
     *
     * @throws LengthException If the resulting length of an API word is not
     *     supported.
     */
    public function verify(Communicator $com)
    {
        $com::verifyLengthSupport(strlen($this->getCommand()));
        $com::verifyLengthSupport(strlen('.tag=' . (string)$this->getTag()));
        foreach ($this->attributes as $name => $value) {
            if (is_string($value)) {
                $com::verifyLengthSupport(strlen('=' . $name . '=' . $value));
            } else {
                $com::verifyLengthSupport(
                    strlen('=' . $name . '=') +
                    $com::seekableStreamLength($value)
                );
            }
        }
        $query = $this->getQuery();
        if ($query instanceof Query) {
            $query->verify($com);
        }
        return $this;
    }

    /**
     * Parses the arguments of a command.
     *
     * @param string $string The argument string to parse.
     *
     * @return void
     */
    protected function parseArgumentString($string)
    {
        /*
         * Grammar:
         *
         * <arguments> := (<<\s+>>, <argument>)*,
         * <argument> := <name>, <value>?
         * <name> := <<[^\=\s]+>>
         * <value> := "=", (<quoted string> | <unquoted string>)
         * <quotedString> := <<">>, <<([^"]|\\"|\\\\)*>>, <<">>
         * <unquotedString> := <<\S+>>
         */

        $token = '';
        $name = null;
        while ($string = substr($string, strlen($token))) {
            if (null === $name) {
                if (preg_match('/^\s+([^\s=]+)/sS', $string, $matches)) {
                    $token = $matches[0];
                    $name = $matches[1];
                } else {
                    throw new InvalidArgumentException(
                        "Parsing of argument name failed near '{$string}'",
                        InvalidArgumentException::CODE_NAME_UNPARSABLE
                    );
                }
            } elseif (preg_match('/^\s/s', $string, $matches)) {
                //Empty argument
                $token = '';
                $this->setArgument($name);
                $name = null;
            } elseif (preg_match(
                '/^="(([^\\\"]|\\\"|\\\\)*)"/sS',
                $string,
                $matches
            )) {
                $token = $matches[0];
                $this->setArgument(
                    $name,
                    str_replace(
                        array('\\"', '\\\\'),
                        array('"', '\\'),
                        $matches[1]
                    )
                );
                $name = null;
            } elseif (preg_match('/^=(\S+)/sS', $string, $matches)) {
                $token = $matches[0];
                $this->setArgument($name, $matches[1]);
                $name = null;
            } else {
                throw new InvalidArgumentException(
                    "Parsing of argument value failed near '{$string}'",
                    InvalidArgumentException::CODE_VALUE_UNPARSABLE
                );
            }
        }

        if (null !== $name && ('' !== ($name = trim($name)))) {
            $this->setArgument($name, '');
        }

    }
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\Response.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Refers to transmitter direction constants.
 */
use PEAR2\Net\Transmitter as T;

/**
 * Locks are released upon any exception from anywhere.
 */
use Exception as E;

/**
 * Represents a RouterOS response.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Response extends Message
{

    /**
     * The last response for a request.
     */
    const TYPE_FINAL = '!done';

    /**
     * A response with data.
     */
    const TYPE_DATA = '!re';

    /**
     * A response signifying error.
     */
    const TYPE_ERROR = '!trap';

    /**
     * A response signifying a fatal error, due to which the connection would be
     * terminated.
     */
    const TYPE_FATAL = '!fatal';

    /**
     * An array of unrecognized words in network order.
     *
     * @var string[]
     */
    protected $unrecognizedWords = array();

    /**
     * The response type.
     *
     * @var string
     */
    private $_type;

    /**
     * Extracts a new response from a communicator.
     *
     * @param Communicator  $com       The communicator from which to extract
     *     the new response.
     * @param bool          $asStream  Whether to populate the argument values
     *     with streams instead of strings.
     * @param int           $sTimeout  If a response is not immediately
     *     available, wait this many seconds. If NULL, wait indefinitely.
     * @param int|null      $usTimeout Microseconds to add to the waiting time.
     * @param Registry|null $reg       An optional registry to sync the
     *     response with.
     *
     * @see getType()
     * @see getArgument()
     */
    public function __construct(
        Communicator $com,
        $asStream = false,
        $sTimeout = 0,
        $usTimeout = null,
        Registry $reg = null
    ) {
        if (null === $reg) {
            if ($com->getTransmitter()->isPersistent()) {
                $old = $com->getTransmitter()
                    ->lock(T\Stream::DIRECTION_RECEIVE);
                try {
                    $this->_receive($com, $asStream, $sTimeout, $usTimeout);
                } catch (E $e) {
                    $com->getTransmitter()->lock($old, true);
                    throw $e;
                }
                $com->getTransmitter()->lock($old, true);
            } else {
                $this->_receive($com, $asStream, $sTimeout, $usTimeout);
            }
        } else {
            while (null === ($response = $reg->getNextResponse())) {
                $newResponse = new self($com, true, $sTimeout, $usTimeout);
                $tagInfo = $reg::parseTag($newResponse->getTag());
                $newResponse->setTag($tagInfo[1]);
                if (!$reg->add($newResponse, $tagInfo[0])) {
                    $response = $newResponse;
                    break;
                }
            }

            $this->_type = $response->_type;
            $this->attributes = $response->attributes;
            $this->unrecognizedWords = $response->unrecognizedWords;
            $this->setTag($response->getTag());

            if (!$asStream) {
                foreach ($this->attributes as $name => $value) {
                    $this->setAttribute(
                        $name,
                        stream_get_contents($value)
                    );
                }
                foreach ($response->unrecognizedWords as $i => $value) {
                    $this->unrecognizedWords[$i] = stream_get_contents($value);
                }
            }
        }
    }

    /**
     * Extracts a new response from a communicator.
     *
     * This is the function that performs the actual receiving, while the
     * constructor is also involved in locks and registry sync.
     *
     * @param Communicator $com       The communicator from which to extract
     *     the new response.
     * @param bool         $asStream  Whether to populate the argument values
     *     with streams instead of strings.
     * @param int          $sTimeout  If a response is not immediately
     *     available, wait this many seconds. If NULL, wait indefinitely.
     *     Note that if an empty sentence is received, the timeout will be
     *     reset for another sentence receiving.
     * @param int|null     $usTimeout Microseconds to add to the waiting time.
     *
     * @return void
     */
    private function _receive(
        Communicator $com,
        $asStream = false,
        $sTimeout = 0,
        $usTimeout = null
    ) {
        do {
            if (!$com->getTransmitter()->isDataAwaiting(
                $sTimeout,
                $usTimeout
            )) {
                throw new SocketException(
                    'No data within the time limit',
                    SocketException::CODE_NO_DATA
                );
            }
            $type = $com->getNextWord();
        } while ('' === $type);
        $this->setType($type);
        if ($asStream) {
            for ($word = $com->getNextWordAsStream(), fseek($word, 0, SEEK_END);
                ftell($word) !== 0;
                $word = $com->getNextWordAsStream(), fseek(
                    $word,
                    0,
                    SEEK_END
                )) {
                rewind($word);
                $ind = fread($word, 1);
                if ('=' === $ind || '.' === $ind) {
                    $prefix = stream_get_line($word, null, '=');
                }
                if ('=' === $ind) {
                    $value = fopen('php://temp', 'r+b');
                    $bytesCopied = ftell($word);
                    while (!feof($word)) {
                        $bytesCopied += stream_copy_to_stream(
                            $word,
                            $value,
                            0xFFFFF,
                            $bytesCopied
                        );
                    }
                    rewind($value);
                    $this->setAttribute($prefix, $value);
                    continue;
                }
                if ('.' === $ind && 'tag' === $prefix) {
                    $this->setTag(stream_get_contents($word, -1, -1));
                    continue;
                }
                rewind($word);
                $this->unrecognizedWords[] = $word;
            }
        } else {
            for ($word = $com->getNextWord(); '' !== $word;
                $word = $com->getNextWord()) {
                if (preg_match('/^=([^=]+)=(.*)$/sS', $word, $matches)) {
                    $this->setAttribute($matches[1], $matches[2]);
                } elseif (preg_match('/^\.tag=(.*)$/sS', $word, $matches)) {
                    $this->setTag($matches[1]);
                } else {
                    $this->unrecognizedWords[] = $word;
                }
            }
        }
    }

    /**
     * Sets the response type.
     *
     * Sets the response type. Valid values are the TYPE_* constants.
     *
     * @param string $type The new response type.
     *
     * @return $this The response object.
     *
     * @see getType()
     */
    protected function setType($type)
    {
        switch ($type) {
        case self::TYPE_FINAL:
        case self::TYPE_DATA:
        case self::TYPE_ERROR:
        case self::TYPE_FATAL:
            $this->_type = $type;
            return $this;
        default:
            throw new UnexpectedValueException(
                'Unrecognized response type.',
                UnexpectedValueException::CODE_RESPONSE_TYPE_UNKNOWN,
                null,
                $type
            );
        }
    }

    /**
     * Gets the response type.
     *
     * @return string The response type.
     *
     * @see setType()
     */
    public function getType()
    {
        return $this->_type;
    }

    /**
     * Gets the value of an argument.
     *
     * @param string $name The name of the argument.
     *
     * @return string|resource|null The value of the specified argument.
     *     Returns NULL if such an argument is not set.
     *
     * @deprecated         1.0.0b5 Use {@link static::getProperty()} instead.
     *     This method will be removed upon final release, and is currently
     *     left standing merely because it can't be easily search&replaced in
     *     existing code, due to the fact the name "getArgument()" is shared
     *     with {@link Request::getArgument()}, which is still valid.
     * @codeCoverageIgnore
     */
    public function getArgument($name)
    {
        trigger_error(
            'Response::getArgument() is deprecated in favor of ' .
            'Response::getProperty() (but note that Request::getArgument() ' .
            'is still valid)',
            E_USER_DEPRECATED
        );
        return $this->getAttribute($name);
    }

    /**
     * Gets the value of a property.
     *
     * @param string $name The name of the property.
     *
     * @return string|resource|null The value of the specified property.
     *     Returns NULL if such a property is not set.
     */
    public function getProperty($name)
    {
        return parent::getAttribute($name);
    }

    /**
     * Gets a list of unrecognized words.
     *
     * @return string[] The list of unrecognized words.
     */
    public function getUnrecognizedWords()
    {
        return $this->unrecognizedWords;
    }
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\ResponseCollection.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Implemented by this class.
 */
use ArrayAccess;

/**
 * Implemented by this class.
 */
use Countable;

/**
 * Implemented by this class.
 */
use SeekableIterator;

/**
 * Represents a collection of RouterOS responses.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 *
 * @method string getType()
 *     Calls {@link Response::getType()}
 *     on the response pointed by the pointer.
 * @method string[] getUnrecognizedWords()
 *     Calls {@link Response::getUnrecognizedWords()}
 *     on the response pointed by the pointer.
 * @method string|resource|null getProperty(string $name)
 *     Calls {@link Response::getProperty()}
 *     on the response pointed by the pointer.
 * @method string getTag()
 *     Calls {@link Response::getTag()}
 *     on the response pointed by the pointer.
 */
class ResponseCollection implements ArrayAccess, SeekableIterator, Countable
{

    /**
     * An array with all {@link Response} objects.
     *
     * An array with all Response objects.
     *
     * @var Response[]
     */
    protected $responses = array();

    /**
     * An array with each Response object's type.
     *
     * An array with each {@link Response} object's type.
     *
     * @var string[]
     */
    protected $responseTypes = array();

    /**
     * An array with each Response object's tag.
     *
     * An array with each {@link Response} object's tag.
     *
     * @var string[]
     */
    protected $responseTags = array();

    /**
     * An array with positions of responses, based on an property name.
     *
     * The name of each property is the array key, and the array value
     * is another array where the key is the value for that property, and
     * the value is the position of the response. For performance reasons,
     * each key is built only when {@link static::setIndex()} is called with
     * that property, and remains available for the lifetime of this collection.
     *
     * @var array<string,array<string,int>>
     */
    protected $responsesIndex = array();

    /**
     * An array with all distinct properties.
     *
     * An array with all distinct properties across all {@link Response}
     * objects. Created at the first call of {@link static::getPropertyMap()}.
     *
     * @var array<string,int[]>
     */
    protected $propertyMap = null;

    /**
     * A pointer, as required by SeekableIterator.
     *
     * @var int
     */
    protected $position = 0;

    /**
     * Name of property to use as index
     *
     * NULL when disabled.
     *
     * @var string|null
     */
    protected $index = null;

    /**
     * Compare criteria.
     *
     * Used by {@link static::compare()} to determine the order between
     * two responses. See {@link static::orderBy()} for a detailed description
     * of this array's format.
     *
     * @var string[]|array<string,null|int|array<int|callable>>
     */
    protected $compareBy = array();

    /**
     * Creates a new collection.
     *
     * @param Response[] $responses An array of responses, in network order.
     */
    public function __construct(array $responses)
    {
        $pos = 0;
        foreach ($responses as $response) {
            if ($response instanceof Response) {
                $this->responseTypes[$pos] = $response->getType();
                $this->responseTags[$pos] = $response->getTag();
                $this->responses[$pos++] = $response;
            }
        }
    }

    /**
     * A shorthand gateway.
     *
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     *
     * @param int|string|null $offset The offset of the response to seek to.
     *     If the offset is negative, seek to that relative to the end.
     *     If the collection is indexed, you can also supply a value to seek to.
     *     Setting NULL will get the current response's iterator.
     *
     * @return Response|ArrayObject The {@link Response} at the specified
     *     offset, the current response's iterator (which is an ArrayObject)
     *     when NULL is given, or FALSE if the offset is invalid
     *     or the collection is empty.
     */
    public function __invoke($offset = null)
    {
        return null === $offset
            ? $this->current()->getIterator()
            : $this->seek($offset);
    }

    /**
     * Sets a property to be usable as a key in the collection.
     *
     * @param string|null $name The name of the property to use. Future calls
     *     that accept a position will then also be able to search values of
     *     that property for a matching value.
     *     Specifying NULL will disable such lookups (as is by default).
     *     Note that in case this value occurs multiple times within the
     *     collection, only the last matching response will be accessible by
     *     that value.
     *
     * @return $this The object itself.
     */
    public function setIndex($name)
    {
        if (null !== $name) {
            $name = (string)$name;
            if (!isset($this->responsesIndex[$name])) {
                $this->responsesIndex[$name] = array();
                foreach ($this->responses as $pos => $response) {
                    $val = $response->getProperty($name);
                    if (null !== $val) {
                        $this->responsesIndex[$name][$val] = $pos;
                    }
                }
            }
        }
        $this->index = $name;
        return $this;
    }

    /**
     * Gets the name of the property used as an index.
     *
     * @return string|null Name of property used as index. NULL when disabled.
     */
    public function getIndex()
    {
        return $this->index;
    }

    /**
     * Gets the whole collection as an array.
     *
     * @param bool $useIndex Whether to use the index values as keys for the
     *     resulting array.
     *
     * @return Response[] An array with all responses, in network order.
     */
    public function toArray($useIndex = false)
    {
        if ($useIndex) {
            $positions = $this->responsesIndex[$this->index];
            asort($positions, SORT_NUMERIC);
            $positions = array_flip($positions);
            return array_combine(
                $positions,
                array_intersect_key($this->responses, $positions)
            );
        }
        return $this->responses;
    }

    /**
     * Counts the responses in the collection.
     *
     * @return int The number of responses in the collection.
     */
    public function count()
    {
        return count($this->responses);
    }

    /**
     * Checks if an offset exists.
     *
     * @param int|string $offset The offset to check. If the
     *     collection is indexed, you can also supply a value to check.
     *     Note that negative numeric offsets are NOT accepted.
     *
     * @return bool TRUE if the offset exists, FALSE otherwise.
     */
    public function offsetExists($offset)
    {
        return is_int($offset)
            ? array_key_exists($offset, $this->responses)
            : array_key_exists($offset, $this->responsesIndex[$this->index]);
    }

    /**
     * Gets a {@link Response} from a specified offset.
     *
     * @param int|string $offset The offset of the desired response. If the
     *     collection is indexed, you can also supply the value to search for.
     *
     * @return Response The response at the specified offset.
     */
    public function offsetGet($offset)
    {
        return is_int($offset)
            ? $this->responses[$offset >= 0
            ? $offset
            : count($this->responses) + $offset]
            : $this->responses[$this->responsesIndex[$this->index][$offset]];
    }

    /**
     * N/A
     *
     * This method exists only because it is required for ArrayAccess. The
     * collection is read only.
     *
     * @param int|string $offset N/A
     * @param Response   $value  N/A
     *
     * @return void
     *
     * @SuppressWarnings(PHPMD.UnusedFormalParameter)
     */
    public function offsetSet($offset, $value)
    {

    }

    /**
     * N/A
     *
     * This method exists only because it is required for ArrayAccess. The
     * collection is read only.
     *
     * @param int|string $offset N/A
     *
     * @return void
     *
     * @SuppressWarnings(PHPMD.UnusedFormalParameter)
     */
    public function offsetUnset($offset)
    {

    }

    /**
     * Resets the pointer to 0, and returns the first response.
     *
     * @return Response|false The first response in the collection,
     *     or FALSE if the collection is empty.
     */
    public function rewind()
    {
        return $this->seek(0);
    }

    /**
     * Moves the position pointer to a specified position.
     *
     * @param int|string $position The position to move to. If the collection is
     *     indexed, you can also supply a value to move the pointer to.
     *     A non-existent index will move the pointer to "-1".
     *
     * @return Response|false The {@link Response} at the specified position,
     *     or FALSE if the specified position is not valid.
     */
    public function seek($position)
    {
        $this->position = is_int($position)
            ? ($position >= 0
            ? $position
            : count($this->responses) + $position)
            : ($this->offsetExists($position)
            ? $this->responsesIndex[$this->index][$position]
            : -1);
        return $this->current();
    }

    /**
     * Moves the pointer forward by 1, and gets the next response.
     *
     * @return Response|false The next {@link Response} object,
     *     or FALSE if the position is not valid.
     */
    public function next()
    {
        ++$this->position;
        return $this->current();
    }

    /**
     * Gets the response at the current pointer position.
     *
     * @return Response|false The response at the current pointer position,
     *     or FALSE if the position is not valid.
     */
    public function current()
    {
        return $this->valid() ? $this->responses[$this->position] : false;
    }

    /**
     * Moves the pointer backwards by 1, and gets the previous response.
     *
     * @return Response|false The next {@link Response} object,
     *     or FALSE if the position is not valid.
     */
    public function prev()
    {
        --$this->position;
        return $this->current();
    }

    /**
     * Moves the pointer to the last valid position, and returns the last
     * response.
     *
     * @return Response|false The last response in the collection,
     *     or FALSE if the collection is empty.
     */
    public function end()
    {
        $this->position = count($this->responses) - 1;
        return $this->current();
    }

    /**
     * Gets the key at the current pointer position.
     *
     * @return int|false The key at the current pointer position,
     *     i.e. the pointer position itself, or FALSE if the position
     *     is not valid.
     */
    public function key()
    {
        return $this->valid() ? $this->position : false;
    }

    /**
     * Checks if the pointer is still pointing to an existing offset.
     *
     * @return bool TRUE if the pointer is valid, FALSE otherwise.
     */
    public function valid()
    {
        return $this->offsetExists($this->position);
    }

    /**
     * Gets all distinct property names.
     *
     * Gets all distinct property names across all responses.
     *
     * @return array<string,int[]> An array with
     *     all distinct property names as keys, and
     *     the indexes at which they occur as values.
     */
    public function getPropertyMap()
    {
        if (null === $this->propertyMap) {
            $properties = array();
            foreach ($this->responses as $index => $response) {
                $names = array_keys($response->getIterator()->getArrayCopy());
                foreach ($names as $name) {
                    if (!isset($properties[$name])) {
                        $properties[$name] = array();
                    }
                    $properties[$name][] = $index;
                }
            }
            $this->propertyMap = $properties;
        }
        return $this->propertyMap;
    }

    /**
     * Gets all responses of a specified type.
     *
     * @param string $type The response type to filter by. Valid values are the
     *     Response::TYPE_* constants.
     *
     * @return static A new collection with responses of the
     *     specified type.
     */
    public function getAllOfType($type)
    {
        $result = array();
        foreach (array_keys($this->responseTypes, $type, true) as $index) {
            $result[] = $this->responses[$index];
        }
        return new static($result);
    }

    /**
     * Gets all responses with a specified tag.
     *
     * @param string $tag The tag to filter by.
     *
     * @return static A new collection with responses having the
     *     specified tag.
     */
    public function getAllTagged($tag)
    {
        $result = array();
        foreach (array_keys($this->responseTags, $tag, true) as $index) {
            $result[] = $this->responses[$index];
        }
        return new static($result);
    }

    /**
     * Order resones by criteria.
     *
     * @param string[]|array<string,null|int|array<int|callable>> $criteria The
     *     criteria to order responses by. It takes the
     *     form of an array where each key is the name of the property to use
     *     as (N+1)th sorting key. The value of each member can be either NULL
     *     (for that property, sort normally in ascending order), a single sort
     *     order constant (SORT_ASC or SORT_DESC) to sort normally in the
     *     specified order, an array where the first member is an order
     *     constant, and the second one is sorting flags (same as built in PHP
     *     array functions) or a callback.
     *     If a callback is provided, it must accept two arguments
     *     (the two values to be compared), and return -1, 0 or 1 if the first
     *     value is respectively less than, equal to or greater than the second
     *     one.
     *     Each key of $criteria can also be numeric, in which case the
     *     value is the name of the property, and sorting is done normally in
     *     ascending order.
     *
     * @return static A new collection with the responses sorted in the
     *     specified order.
     */
    public function orderBy(array $criteria)
    {
        $this->compareBy = $criteria;
        $sortedResponses = $this->responses;
        usort($sortedResponses, array($this, 'compare'));
        return new static($sortedResponses);
    }

    /**
     * Calls a method of the response pointed by the pointer.
     *
     * Calls a method of the response pointed by the pointer. This is a magic
     * PHP method, thanks to which any function you call on the collection that
     * is not defined will be redirected to the response.
     *
     * @param string $method The name of the method to call.
     * @param array  $args   The arguments to pass to the method.
     *
     * @return mixed Whatever the called function returns.
     */
    public function __call($method, array $args)
    {
        return call_user_func_array(
            array($this->current(), $method),
            $args
        );
    }

    /**
     * Compares two responses.
     *
     * Compares two responses, based on criteria defined in
     * {@link static::$compareBy}.
     *
     * @param Response $itemA The response to compare.
     * @param Response $itemB The response to compare $a against.
     *
     * @return int Returns 0 if the two responses are equal according to every
     *     criteria specified, -1 if $a should be placed before $b, and 1 if $b
     *     should be placed before $a.
     */
    protected function compare(Response $itemA, Response $itemB)
    {
        foreach ($this->compareBy as $name => $spec) {
            if (!is_string($name)) {
                $name = $spec;
                $spec = null;
            }

            $members = array(
                0 => $itemA->getProperty($name),
                1 => $itemB->getProperty($name)
            );

            if (is_callable($spec)) {
                uasort($members, $spec);
            } elseif ($members[0] === $members[1]) {
                continue;
            } else {
                $flags = SORT_REGULAR;
                $order = SORT_ASC;
                if (is_array($spec)) {
                    list($order, $flags) = $spec;
                } elseif (null !== $spec) {
                    $order = $spec;
                }

                if (SORT_ASC === $order) {
                    asort($members, $flags);
                } else {
                    arsort($members, $flags);
                }
            }
            return (key($members) === 0) ? -1 : 1;
        }

        return 0;
    }
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\RouterErrorException.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Base of this class.
 */
use RuntimeException;

/**
 * Refered to in the constructor.
 */
use Exception as E;

/**
 * Exception thrown by higher level classes (Util, etc.) when the router
 * returns an error.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class RouterErrorException extends RuntimeException implements Exception
{
    const CODE_ITEM_ERROR           = 0x100000;
    const CODE_SCRIPT_ERROR         = 0x200000;
    const CODE_READ_ERROR           = 0x010000;
    const CODE_WRITE_ERROR          = 0x020000;
    const CODE_EXEC_ERROR           = 0x040000;

    const CODE_CACHE_ERROR          = 0x100001;
    const CODE_GET_ERROR            = 0x110001;
    const CODE_GETALL_ERROR         = 0x110002;
    const CODE_ADD_ERROR            = 0x120001;
    const CODE_SET_ERROR            = 0x120002;
    const CODE_REMOVE_ERROR         = 0x120004;
    const CODE_ENABLE_ERROR         = 0x120012;
    const CODE_DISABLE_ERROR        = 0x120022;
    const CODE_COMMENT_ERROR        = 0x120042;
    const CODE_UNSET_ERROR          = 0x120082;
    const CODE_MOVE_ERROR           = 0x120107;
    const CODE_SCRIPT_ADD_ERROR     = 0x220001;
    const CODE_SCRIPT_REMOVE_ERROR  = 0x220004;
    const CODE_SCRIPT_RUN_ERROR     = 0x240001;
    const CODE_SCRIPT_FILE_ERROR    = 0x240003;

    /**
     * The complete response returned by the router.
     *
     * NULL when the router was not contacted at all.
     *
     * @var ResponseCollection|null
     */
    private $_responses = null;

    /**
     * Creates a new RouterErrorException.
     *
     * @param string                  $message   The Exception message to throw.
     * @param int                     $code      The Exception code.
     * @param E|null                  $previous  The previous exception used for
     *     the exception chaining.
     * @param ResponseCollection|null $responses The complete set responses
     *     returned by the router.
     */
    public function __construct(
        $message,
        $code = 0,
        E $previous = null,
        ResponseCollection $responses = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_responses = $responses;
    }

    /**
     * Gets the complete set responses returned by the router.
     *
     * @return ResponseCollection|null The complete set responses
     *     returned by the router.
     */
    public function getResponses()
    {
        return $this->_responses;
    }

    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing

    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        $result = parent::__toString();
        if ($this->_responses instanceof ResponseCollection) {
            $result .= "\nResponse collection:\n" .
                print_r($this->_responses->toArray(), true);
        }
        return $result;
    }

    // @codeCoverageIgnoreEnd
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\Script.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Values at {@link Script::escapeValue()} can be casted from this type.
 */
use DateTime;

/**
 * Values at {@link Script::escapeValue()} can be casted from this type.
 */
use DateInterval;

/**
 * Used at {@link Script::escapeValue()} to get the proper time.
 */
use DateTimeZone;

/**
 * Used to reliably write to streams at {@link Script::prepare()}.
 */
use PEAR2\Net\Transmitter\Stream;

/**
 * Used to catch DateTime and DateInterval exceptions at
 * {@link Script::parseValue()}.
 */
use Exception as E;

/**
 * Scripting class.
 *
 * Provides functionality related to parsing and composing RouterOS scripts and
 * values.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Script
{
    /**
     * Parses a value from a RouterOS scripting context.
     *
     * Turns a value from RouterOS into an equivalent PHP value, based on
     * determining the type in the same way RouterOS would determine it for a
     * literal.
     *
     * This method is intended to be the very opposite of
     * {@link static::escapeValue()}. That is, results from that method, if
     * given to this method, should produce equivalent results.
     *
     * @param string            $value    The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     * @param DateTimeZone|null $timezone The timezone which any resulting
     *     DateTime object (either the main value, or values within an array)
     *     will use. Defaults to UTC.
     *
     * @return mixed Depending on RouterOS type detected:
     *     - "nil" (the string "[]") or "nothing" (empty string) - NULL.
     *     - "num" - int or double for large values.
     *     - "bool" - a boolean.
     *     - "array" - an array, with the keys and values processed recursively.
     *     - "time" - a {@link DateInterval} object.
     *     - "date" (pseudo type; string in the form "M/j/Y") - a DateTime
     *         object with the specified date, at midnight.
     *     - "datetime" (pseudo type; string in the form "M/j/Y H:i:s") - a
     *         DateTime object with the specified date and time.
     *     - "str" (a quoted string) - a string, with the contents escaped.
     *     - Unrecognized type - casted to a string, unmodified.
     */
    public static function parseValue($value, DateTimeZone $timezone = null)
    {
        $value = static::parseValueToSimple($value);
        if (!is_string($value)) {
            return $value;
        }

        try {
            return static::parseValueToArray($value, $timezone);
        } catch (ParserException $e) {
            try {
                return static::parseValueToDateInterval($value);
            } catch (ParserException $e) {
                try {
                    return static::parseValueToDateTime($value, $timezone);
                } catch (ParserException $e) {
                    return static::parseValueToString($value);
                }
            }
        }
    }

    /**
     * Parses a RouterOS value into a PHP string.
     *
     * @param string $value The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     *
     * @return string If a quoted string is provided, it would be parsed.
     *     Otherwise, the value is casted to a string, and returned unmodified.
     */
    public static function parseValueToString($value)
    {
        $value = (string)$value;
        if ('"' === $value[0] && '"' === $value[strlen($value) - 1]) {
            return str_replace(
                array('\"', '\\\\', "\\\n", "\\\r\n", "\\\r"),
                array('"', '\\'),
                substr($value, 1, -1)
            );
        }
        return $value;
    }

    /**
     * Parses a RouterOS value into a PHP simple type.
     *
     * Parses a RouterOS value into a PHP simple type. "Simple" types being
     * scalar types, plus NULL.
     *
     * @param string $value The value to be parsed. Must be a literal of a
     *     value, e.g. what {@link static::escapeValue()} will give you.
     *
     * @return string|bool|int|double|null Depending on RouterOS type detected:
     *     - "nil" (the string "[]") or "nothing" (empty string) - NULL.
     *     - "num" - int or double for large values.
     *     - "bool" - a boolean.
     *     - Unrecognized type - casted to a string, unmodified.
     */
    public static function parseValueToSimple($value)
    {
        $value = (string)$value;

        if (in_array($value, array('', '[]'), true)) {
            return null;
        } elseif (in_array($value, array('true', 'false', 'yes', 'no'), true)) {
            return $value === 'true' || $value === 'yes';
        } elseif ($value === (string)($num = (int)$value)
            || $value === (string)($num = (double)$value)
        ) {
            return $num;
        }
        return $value;
    }

    /**
     * Parses a RouterOS value into a PHP DateTime object
     *
     * Parses a RouterOS value into a PHP DateTime object.
     *
     * @param string            $value    The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     * @param DateTimeZone|null $timezone The timezone which the resulting
     *     DateTime object will use. Defaults to UTC.
     *
     * @return DateTime Depending on RouterOS type detected:
     *     - "date" (pseudo type; string in the form "M/j/Y") - a DateTime
     *         object with the specified date, at midnight UTC time (regardless
     *         of timezone provided).
     *     - "datetime" (pseudo type; string in the form "M/j/Y H:i:s") - a
     *         DateTime object with the specified date and time,
     *         with the specified timezone.
     *
     * @throws ParserException When the value is not of a recognized type.
     */
    public static function parseValueToDateTime(
        $value,
        DateTimeZone $timezone = null
    ) {
        $previous = null;
        $value = (string)$value;
        if ('' !== $value && preg_match(
            '#^
                (?<mon>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)
                /
                (?<day>\d\d?)
                /
                (?<year>\d{4})
                (?:
                    \s+(?<time>\d{2}\:\d{2}:\d{2})
                )?
            $#uix',
            $value,
            $date
        )) {
            if (!isset($date['time'])) {
                $date['time'] = '00:00:00';
                $timezone = new DateTimeZone('UTC');
            } elseif (null === $timezone) {
                $timezone = new DateTimeZone('UTC');
            }
            try {
                return new DateTime(
                    $date['year'] .
                    '-' . ucfirst($date['mon']) .
                    "-{$date['day']} {$date['time']}",
                    $timezone
                );
            } catch (E $e) {
                $previous = $e;
            }
        }
        throw new ParserException(
            'The supplied value can not be converted to a DateTime',
            ParserException::CODE_DATETIME,
            $previous
        );
    }

    /**
     * Parses a RouterOS value into a PHP DateInterval.
     *
     * Parses a RouterOS value into a PHP DateInterval.
     *
     * @param string $value The value to be parsed. Must be a literal of a
     *     value, e.g. what {@link static::escapeValue()} will give you.
     *
     * @return DateInterval The value as a DateInterval object.
     *
     * @throws ParserException When the value is not of a recognized type.
     */
    public static function parseValueToDateInterval($value)
    {
        $value = (string)$value;
        if ('' !== $value && preg_match(
            '/^
                (?:(\d+)w)?
                (?:(\d+)d)?
                (?:(\d+)(?:\:|h))?
                (?|
                    (\d+)\:
                    (\d*(?:\.\d{1,9})?)
                |
                    (?:(\d+)m)?
                    (?:(\d+|\d*\.\d{1,9})s)?
                    (?:((?5))ms)?
                    (?:((?5))us)?
                    (?:((?5))ns)?
                )
            $/x',
            $value,
            $time
        )) {
            $days = isset($time[2]) ? (int)$time[2] : 0;
            if (isset($time[1])) {
                $days += 7 * (int)$time[1];
            }
            if (empty($time[3])) {
                $time[3] = 0;
            }
            if (empty($time[4])) {
                $time[4] = 0;
            }
            if (empty($time[5])) {
                $time[5] = 0;
            }

            $subsecondTime = 0.0;
            //@codeCoverageIgnoreStart
            // No PHP version currently supports sub-second DateIntervals,
            // meaning this section is untestable, since no version constraints
            // can be specified for test inputs.
            // All inputs currently use integer seconds only, making this
            // section unreachable during tests.
            // Nevertheless, this section exists right now, in order to provide
            // such support as soon as PHP has it.
            if (!empty($time[6])) {
                $subsecondTime += ((double)$time[6]) / 1000;
            }
            if (!empty($time[7])) {
                $subsecondTime += ((double)$time[7]) / 1000000;
            }
            if (!empty($time[8])) {
                $subsecondTime += ((double)$time[8]) / 1000000000;
            }
            //@codeCoverageIgnoreEnd

            $secondsSpec = $time[5] + $subsecondTime;
            try {
                return new DateInterval(
                    "P{$days}DT{$time[3]}H{$time[4]}M{$secondsSpec}S"
                );
                //@codeCoverageIgnoreStart
                // See previous ignored section's note.
                //
                // This section is added for backwards compatibility with current
                // PHP versions, when in the future sub-second support is added.
                // In that event, the test inputs for older versions will be
                // expected to get a rounded up result of the sub-second data.
            } catch (E $e) {
                $secondsSpec = (int)round($secondsSpec);
                return new DateInterval(
                    "P{$days}DT{$time[3]}H{$time[4]}M{$secondsSpec}S"
                );
            }
            //@codeCoverageIgnoreEnd
        }
        throw new ParserException(
            'The supplied value can not be converted to DateInterval',
            ParserException::CODE_DATEINTERVAL
        );
    }

    /**
     * Parses a RouterOS value into a PHP array.
     *
     * Parses a RouterOS value into a PHP array.
     *
     * @param string            $value    The value to be parsed.
     *     Must be a literal of a value,
     *     e.g. what {@link static::escapeValue()} will give you.
     * @param DateTimeZone|null $timezone The timezone which any resulting
     *     DateTime object within the array will use. Defaults to UTC.
     *
     * @return array An array, with the keys and values processed recursively,
     *         the keys with {@link static::parseValueToSimple()},
     *         and the values with {@link static::parseValue()}.
     *
     * @throws ParserException When the value is not of a recognized type.
     */
    public static function parseValueToArray(
        $value,
        DateTimeZone $timezone = null
    ) {
        $value = (string)$value;
        if ('{' === $value[0] && '}' === $value[strlen($value) - 1]) {
            $value = substr($value, 1, -1);
            if ('' === $value) {
                return array();
            }
            $parsedValue = preg_split(
                '/
                    (\"(?:\\\\\\\\|\\\\"|[^"])*\")
                    |
                    (\{[^{}]*(?2)?\})
                    |
                    ([^;=]+)
                /sx',
                $value,
                null,
                PREG_SPLIT_DELIM_CAPTURE
            );
            $result = array();
            $newVal = null;
            $newKey = null;
            for ($i = 0, $l = count($parsedValue); $i < $l; ++$i) {
                switch ($parsedValue[$i]) {
                case '':
                    break;
                case ';':
                    if (null === $newKey) {
                        $result[] = $newVal;
                    } else {
                        $result[$newKey] = $newVal;
                    }
                    $newKey = $newVal = null;
                    break;
                case '=':
                    $newKey = static::parseValueToSimple($parsedValue[$i - 1]);
                    $newVal = static::parseValue($parsedValue[++$i], $timezone);
                    break;
                default:
                    $newVal = static::parseValue($parsedValue[$i], $timezone);
                }
            }
            if (null === $newKey) {
                $result[] = $newVal;
            } else {
                $result[$newKey] = $newVal;
            }
            return $result;
        }
        throw new ParserException(
            'The supplied value can not be converted to an array',
            ParserException::CODE_ARRAY
        );
    }

    /**
     * Prepares a script.
     *
     * Prepares a script for eventual execution by prepending parameters as
     * variables to it.
     *
     * This is particularly useful when you're creating scripts that you don't
     * want to execute right now (as with {@link Util::exec()}, but instead
     * you want to store it for later execution, perhaps by supplying it to
     * "/system scheduler".
     *
     * @param string|resource         $source The source of the script,
     *     as a string or stream. If a stream is provided, reading starts from
     *     the current position to the end of the stream, and the pointer stays
     *     at the end after reading is done.
     * @param array<string|int,mixed> $params An array of parameters to make
     *     available in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each with
     *     {@link static::escapeString()} with all bytes being escaped.
     *     Processing starts from the current position to the end of the stream,
     *     and the stream's pointer is left untouched after the reading is done.
     *     Variables with a value of type "nothing" can be declared with a
     *     numeric array key and the variable name as the array value
     *     (that is casted to a string).
     *
     * @return resource A new PHP temporary stream with the script as contents,
     *     with the pointer back at the start.
     *
     * @see static::append()
     */
    public static function prepare(
        $source,
        array $params = array()
    ) {
        $resultStream = fopen('php://temp', 'r+b');
        static::append($resultStream, $source, $params);
        rewind($resultStream);
        return $resultStream;
    }

    /**
     * Appends a script.
     *
     * Appends a script to an existing stream.
     *
     * @param resource                $stream An existing stream to write the
     *     resulting script to.
     * @param string|resource         $source The source of the script,
     *     as a string or stream. If a stream is provided, reading starts from
     *     the current position to the end of the stream, and the pointer stays
     *     at the end after reading is done.
     * @param array<string|int,mixed> $params An array of parameters to make
     *     available in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each with
     *     {@link static::escapeString()} with all bytes being escaped.
     *     Processing starts from the current position to the end of the stream,
     *     and the stream's pointer is left untouched after the reading is done.
     *     Variables with a value of type "nothing" can be declared with a
     *     numeric array key and the variable name as the array value
     *     (that is casted to a string).
     *
     * @return int The number of bytes written to $stream is returned,
     *     and the pointer remains where it was after the write
     *     (i.e. it is not seeked back, even if seeking is supported).
     */
    public static function append(
        $stream,
        $source,
        array $params = array()
    ) {
        $writer = new Stream($stream, false);
        $bytes = 0;

        foreach ($params as $pname => $pvalue) {
            if (is_int($pname)) {
                $pvalue = static::escapeString((string)$pvalue);
                $bytes += $writer->send(":local \"{$pvalue}\";\n");
                continue;
            }
            $pname = static::escapeString($pname);
            $bytes += $writer->send(":local \"{$pname}\" ");
            if (Stream::isStream($pvalue)) {
                $reader = new Stream($pvalue, false);
                $chunkSize = $reader->getChunk(Stream::DIRECTION_RECEIVE);
                $bytes += $writer->send('"');
                while ($reader->isAvailable() && $reader->isDataAwaiting()) {
                    $bytes += $writer->send(
                        static::escapeString(fread($pvalue, $chunkSize), true)
                    );
                }
                $bytes += $writer->send("\";\n");
            } else {
                $bytes += $writer->send(static::escapeValue($pvalue) . ";\n");
            }
        }

        $bytes += $writer->send($source);
        return $bytes;
    }

    /**
     * Escapes a value for a RouterOS scripting context.
     *
     * Turns any native PHP value into an equivalent whole value that can be
     * inserted as part of a RouterOS script.
     *
     * DateInterval objects will be casted to RouterOS' "time" type.
     *
     * DateTime objects will be casted to a string following the "M/d/Y H:i:s"
     * format. If the time is exactly midnight (including microseconds), and
     * the timezone is UTC, the string will include only the "M/d/Y" date.
     *
     * Unrecognized types (i.e. resources and other objects) are casted to
     * strings, and those strings are then escaped.
     *
     * @param mixed $value The value to be escaped.
     *
     * @return string A string representation that can be directly inserted in a
     *     script as a whole value.
     */
    public static function escapeValue($value)
    {
        switch(gettype($value)) {
        case 'NULL':
            $value = '[]';
            break;
        case 'integer':
            $value = (string)$value;
            break;
        case 'boolean':
            $value = $value ? 'true' : 'false';
            break;
        case 'array':
            if (0 === count($value)) {
                $value = '({})';
                break;
            }
            $result = '';
            foreach ($value as $key => $val) {
                $result .= ';';
                if (!is_int($key)) {
                    $result .= static::escapeValue($key) . '=';
                }
                $result .= static::escapeValue($val);
            }
            $value = '{' . substr($result, 1) . '}';
            break;
        case 'object':
            if ($value instanceof DateTime) {
                $usec = $value->format('u');
                $usec = '000000' === $usec ? '' : '.' . $usec;
                $value = '00:00:00.000000 UTC' === $value->format('H:i:s.u e')
                    ? $value->format('M/d/Y')
                    : $value->format('M/d/Y H:i:s') . $usec;
            }
            if ($value instanceof DateInterval) {
                if (false === $value->days || $value->days < 0) {
                    $value = $value->format('%r%dd%H:%I:%S');
                } else {
                    $value = $value->format('%r%ad%H:%I:%S');
                }
                break;
            }
            //break; intentionally omitted
        default:
            $value = '"' . static::escapeString((string)$value) . '"';
            break;
        }
        return $value;
    }

    /**
     * Escapes a string for a RouterOS scripting context.
     *
     * Escapes a string for a RouterOS scripting context. The value can then be
     * surrounded with quotes at a RouterOS script (or concatenated onto a
     * larger string first), and you can be sure there won't be any code
     * injections coming from it.
     *
     * By default, for the sake of brevity of the output, ASCII alphanumeric
     * characters and underscores are left untouched. And for the sake of
     * character conversion, bytes above 0x7F are also left untouched.
     *
     * @param string $value Value to be escaped.
     * @param bool   $full  Whether to escape all bytes in the string, including
     *     ASCII alphanumeric characters, underscores and bytes above 0x7F.
     *
     * @return string The escaped value.
     *
     * @internal Why leave ONLY those ASCII characters and not also others?
     *     Because those can't in any way be mistaken for language constructs,
     *     unlike many other "safe inside strings, but not outside" ASCII
     *     characters, like ",", ".", "+", "-", "~", etc.
     */
    public static function escapeString($value, $full = false)
    {
        if ($full) {
            return self::_escapeCharacters(array($value));
        }
        return preg_replace_callback(
            '/[^\\_A-Za-z0-9\\x80-\\xFF]+/S',
            array(__CLASS__, '_escapeCharacters'),
            $value
        );
    }

    /**
     * Escapes a character for a RouterOS scripting context.
     *
     * Escapes a character for a RouterOS scripting context.
     * Intended to only be called by {@link self::escapeString()} for the
     * matching strings.
     *
     * @param array $chars The matches array, expected to contain exactly one
     *     member, in which is the whole string to be escaped.
     *
     * @return string The escaped characters.
     */
    private static function _escapeCharacters(array $chars)
    {
        $result = '';
        for ($i = 0, $l = strlen($chars[0]); $i < $l; ++$i) {
            $result .= '\\' . str_pad(
                strtoupper(dechex(ord($chars[0][$i]))),
                2,
                '0',
                STR_PAD_LEFT
            );
        }
        return $result;
    }
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\SocketException.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Base of this class.
 */
use RuntimeException;

/**
 * Exception thrown when something goes wrong with the connection.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class SocketException extends RuntimeException implements Exception
{
    const CODE_SERVICE_INCOMPATIBLE = 10200;
    const CODE_CONNECTION_FAIL = 100;
    const CODE_QUERY_SEND_FAIL = 30600;
    const CODE_REQUEST_SEND_FAIL = 40900;
    const CODE_NO_DATA = 50000;
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\UnexpectedValueException.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * The base for this exception.
 */
use UnexpectedValueException as U;

/**
 * Used in $previous.
 */
use Exception as E;

/**
 * Exception thrown when encountering an invalid value in a function argument.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class UnexpectedValueException extends U implements Exception
{
    const CODE_CALLBACK_INVALID = 10502;
    const CODE_ACTION_UNKNOWN = 30100;
    const CODE_RESPONSE_TYPE_UNKNOWN = 50100;

    /**
     * The unexpected value.
     *
     * @var mixed
     */
    private $_value;

    /**
     * Creates a new UnexpectedValueException.
     *
     * @param string $message  The Exception message to throw.
     * @param int    $code     The Exception code.
     * @param E|null $previous The previous exception used for the exception
     *     chaining.
     * @param mixed  $value    The unexpected value.
     */
    public function __construct(
        $message,
        $code = 0,
        E $previous = null,
        $value = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_value = $value;
    }

    /**
     * Gets the unexpected value.
     *
     * @return mixed The unexpected value.
     */
    public function getValue()
    {
        return $this->_value;
    }

    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing

    /**
     * Returns a string representation of the exception.
     *
     * @return string The exception as a string.
     */
    public function __toString()
    {
        return parent::__toString() . "\nValue:{$this->_value}";
    }

    // @codeCoverageIgnoreEnd
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\src\PEAR2\Net\RouterOS\Util.php
<?php

/**
 * ~~summary~~
 *
 * ~~description~~
 *
 * PHP version 5
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Returned from {@link Util::getCurrentTime()}.
 */
use DateTime;

/**
 * Used at {@link Util::getCurrentTime()} to get the proper time.
 */
use DateTimeZone;

/**
 * Implemented by this class.
 */
use Countable;

/**
 * Used to detect streams in various methods of this class.
 */
use PEAR2\Net\Transmitter\Stream;

/**
 * Used to catch a DateTime exception at {@link Util::getCurrentTime()}.
 */
use Exception as E;

/**
 * Utility class.
 *
 * Abstracts away frequently used functionality (particularly CRUD operations)
 * in convenient to use methods by wrapping around a connection.
 *
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Util implements Countable
{
    /**
     * The connection to wrap around.
     *
     * @var Client
     */
    protected $client;

    /**
     * The current menu.
     *
     * Note that the root menu (only) uses an empty string.
     * This is done to enable commands executed at it without special casing it
     * at all commands.
     * Instead, only {@link static::setMenu()} is special cased.
     *
     * @var string
     */
    protected $menu = '';

    /**
     * An array with the numbers of items in the current menu.
     *
     * Numbers as keys, and the corresponding IDs as values.
     * NULL when the cache needs regenerating.
     *
     * @var array<int,string>|null
     */
    protected $idCache = null;

    /**
     * Creates a new Util instance.
     *
     * Wraps around a connection to provide convenience methods.
     *
     * @param Client $client The connection to wrap around.
     */
    public function __construct(Client $client)
    {
        $this->client = $client;
    }

    /**
     * Gets the current menu.
     *
     * @return string The absolute path to current menu, using API syntax.
     */
    public function getMenu()
    {
        return '' === $this->menu ? '/' : $this->menu;
    }

    /**
     * Sets the current menu.
     *
     * Sets the current menu.
     *
     * @param string $newMenu The menu to change to. Can be specified with API
     *     or CLI syntax and can be either absolute or relative. If relative,
     *     it's relative to the current menu, which by default is the root.
     *
     * @return $this The object itself. If an empty string is given for
     *     a new menu, no change is performed,
     *     but the ID cache is cleared anyway.
     *
     * @see static::clearIdCache()
     */
    public function setMenu($newMenu)
    {
        $newMenu = (string)$newMenu;
        if ('' !== $newMenu) {
            $menuRequest = new Request('/menu');
            if ('/' === $newMenu) {
                $this->menu = '';
            } elseif ('/' === $newMenu[0]) {
                $this->menu = $menuRequest->setCommand($newMenu)->getCommand();
            } else {
                $newMenu = (string)substr(
                    $menuRequest->setCommand(
                        '/' .
                        str_replace('/', ' ', (string)substr($this->menu, 1)) .
                        ' ' .
                        str_replace('/', ' ', $newMenu)
                        . ' ?'
                    )->getCommand(),
                    1,
                    -2/*strlen('/?')*/
                );
                if ('' !== $newMenu) {
                    $this->menu = '/' . $newMenu;
                } else {
                    $this->menu = '';
                }
            }
        }
        $this->clearIdCache();
        return $this;
    }

    /**
     * Creates a Request object.
     *
     * Creates a {@link Request} object, with a command that's at the
     * current menu. The request can then be sent using {@link Client}.
     *
     * @param string      $command The command of the request, not including
     *     the menu. The request will have that command at the current menu.
     * @param array       $args    Arguments of the request.
     *     Each array key is the name of the argument, and each array value is
     *     the value of the argument to be passed.
     *     Arguments without a value (i.e. empty arguments) can also be
     *     specified using a numeric key, and the name of the argument as the
     *     array value.
     * @param Query|null  $query   The {@link Query} of the request.
     * @param string|null $tag     The tag of the request.
     *
     * @return Request The {@link Request} object.
     *
     * @throws NotSupportedException On an attempt to call a command in a
     *     different menu using API syntax.
     * @throws InvalidArgumentException On an attempt to call a command in a
     *     different menu using CLI syntax.
     */
    public function newRequest(
        $command,
        array $args = array(),
        Query $query = null,
        $tag = null
    ) {
        if (false !== strpos($command, '/')) {
            throw new NotSupportedException(
                'Command tried to go to a different menu',
                NotSupportedException::CODE_MENU_MISMATCH,
                null,
                $command
            );
        }
        $request = new Request('/menu', $query, $tag);
        $request->setCommand("{$this->menu}/{$command}");
        foreach ($args as $name => $value) {
            if (is_int($name)) {
                $request->setArgument($value);
            } else {
                $request->setArgument($name, $value);
            }
        }
        return $request;
    }

    /**
     * Executes a RouterOS script.
     *
     * Executes a RouterOS script, written as a string or a stream.
     * Note that in cases of errors, the line numbers will be off, because the
     * script is executed at the current menu as context, with the specified
     * variables pre declared. This is achieved by prepending 1+count($params)
     * lines before your actual script.
     *
     * @param string|resource         $source The source of the script,
     *     as a string or stream. If a stream is provided, reading starts from
     *     the current position to the end of the stream, and the pointer stays
     *     at the end after reading is done.
     * @param array<string|int,mixed> $params An array of parameters to make
     *     available in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each with
     *     {@link static::escapeString()} with all bytes being escaped.
     *     Processing starts from the current position to the end of the stream,
     *     and the stream's pointer is left untouched after the reading is done.
     *     Variables with a value of type "nothing" can be declared with a
     *     numeric array key and the variable name as the array value
     *     (that is casted to a string).
     *     Note that the script's (generated) name is always added as the
     *     variable "_", which will be inadvertently lost if you overwrite it
     *     from here.
     * @param string|null             $policy Allows you to specify a policy the
     *     script must follow. Has the same format as in terminal.
     *     If left NULL, the script has no restrictions beyond those imposed by
     *     the username.
     * @param string|null             $name   The script is executed after being
     *     saved in "/system script" and is removed after execution.
     *     If this argument is left NULL, a random string,
     *     prefixed with the computer's name, is generated and used
     *     as the script's name.
     *     To eliminate any possibility of name clashes,
     *     you can specify your own name instead.
     *
     * @return ResponseCollection The responses of all requests involved, i.e.
     *     the add, the run and the remove.
     *
     * @throws RouterErrorException When there is an error in any step of the
     *     way. The reponses include all successful commands prior to the error
     *     as well. If the error occurs during the run, there will also be a
     *     remove attempt, and the results will include its results as well.
     */
    public function exec(
        $source,
        array $params = array(),
        $policy = null,
        $name = null
    ) {
        if (null === $name) {
            $name = uniqid(gethostname(), true);
        }

        $request = new Request('/system/script/add');
        $request->setArgument('name', $name);
        $request->setArgument('policy', $policy);

        $params += array('_' => $name);

        $finalSource = fopen('php://temp', 'r+b');
        fwrite(
            $finalSource,
            '/' . str_replace('/', ' ', substr($this->menu, 1)). "\n"
        );
        Script::append($finalSource, $source, $params);
        fwrite($finalSource, "\n");
        rewind($finalSource);

        $request->setArgument('source', $finalSource);
        $addResult = $this->client->sendSync($request);

        if (count($addResult->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when trying to add script',
                RouterErrorException::CODE_SCRIPT_ADD_ERROR,
                null,
                $addResult
            );
        }

        $request = new Request('/system/script/run');
        $request->setArgument('number', $name);
        $runResult = $this->client->sendSync($request);
        $request = new Request('/system/script/remove');
        $request->setArgument('numbers', $name);
        $removeResult = $this->client->sendSync($request);

        $results = new ResponseCollection(
            array_merge(
                $addResult->toArray(),
                $runResult->toArray(),
                $removeResult->toArray()
            )
        );

        if (count($runResult->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when running script',
                RouterErrorException::CODE_SCRIPT_RUN_ERROR,
                null,
                $results
            );
        }
        if (count($removeResult->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when removing script',
                RouterErrorException::CODE_SCRIPT_REMOVE_ERROR,
                null,
                $results
            );
        }

        return $results;
    }

    /**
     * Clears the ID cache.
     *
     * Normally, the ID cache improves performance when targeting items by a
     * number. If you're using both Util's methods and other means (e.g.
     * {@link Client} or {@link Util::exec()}) to add/move/remove items, the
     * cache may end up being out of date. By calling this method right before
     * targeting an item with a number, you can ensure number accuracy.
     *
     * Note that Util's {@link static::move()} and {@link static::remove()}
     * methods automatically clear the cache before returning, while
     * {@link static::add()} adds the new item's ID to the cache as the next
     * number. A change in the menu also clears the cache.
     *
     * Note also that the cache is being rebuilt unconditionally every time you
     * use {@link static::find()} with a callback.
     *
     * @return $this The Util object itself.
     */
    public function clearIdCache()
    {
        $this->idCache = null;
        return $this;
    }

    /**
     * Gets the current time on the router.
     *
     * Gets the current time on the router, regardless of the current menu.
     *
     * If the timezone is one known to both RouterOS and PHP, it will be used
     * as the timezone identifier. Otherwise (e.g. "manual"), the current GMT
     * offset will be used as a timezone, without any DST awareness.
     *
     * @return DateTime The current time of the router, as a DateTime object.
     */
    public function getCurrentTime()
    {
        $clock = $this->client->sendSync(
            new Request(
                '/system/clock/print
                .proplist=date,time,time-zone-name,gmt-offset'
            )
        )->current();
        $clockParts = array();
        foreach (array(
            'date',
            'time',
            'time-zone-name',
            'gmt-offset'
        ) as $clockPart) {
            $clockParts[$clockPart] = $clock->getProperty($clockPart);
            if (Stream::isStream($clockParts[$clockPart])) {
                $clockParts[$clockPart] = stream_get_contents(
                    $clockParts[$clockPart]
                );
            }
        }
        $datetime = ucfirst(strtolower($clockParts['date'])) . ' ' .
            $clockParts['time'];
        try {
            $result = DateTime::createFromFormat(
                'M/j/Y H:i:s',
                $datetime,
                new DateTimeZone($clockParts['time-zone-name'])
            );
        } catch (E $e) {
            $result = DateTime::createFromFormat(
                'M/j/Y H:i:s P',
                $datetime . ' ' . $clockParts['gmt-offset'],
                new DateTimeZone('UTC')
            );
        }
        return $result;
    }

    /**
     * Finds the IDs of items at the current menu.
     *
     * Finds the IDs of items based on specified criteria, and returns them as
     * a comma separated string, ready for insertion at a "numbers" argument.
     *
     * Accepts zero or more criteria as arguments. If zero arguments are
     * specified, returns all items' IDs. The value of each criteria can be a
     * number (just as in Winbox), a literal ID to be included, a {@link Query}
     * object, or a callback. If a callback is specified, it is called for each
     * item, with the item as an argument. If it returns a true value, the
     * item's ID is included in the result. Every other value is casted to a
     * string. A string is treated as a comma separated values of IDs, numbers
     * or callback names. Non-existent callback names are instead placed in the
     * result, which may be useful in menus that accept identifiers other than
     * IDs, but note that it can cause errors on other menus.
     *
     * @return string A comma separated list of all items matching the
     *     specified criteria.
     */
    public function find()
    {
        if (func_num_args() === 0) {
            if (null === $this->idCache) {
                $ret = $this->client->sendSync(
                    new Request($this->menu . '/find')
                )->getProperty('ret');
                if (null === $ret) {
                    $this->idCache = array();
                    return '';
                } elseif (!is_string($ret)) {
                    $ret = stream_get_contents($ret);
                }

                $idCache = str_replace(
                    ';',
                    ',',
                    strtolower($ret)
                );
                $this->idCache = explode(',', $idCache);
                return $idCache;
            }
            return implode(',', $this->idCache);
        }
        $idList = '';
        foreach (func_get_args() as $criteria) {
            if ($criteria instanceof Query) {
                foreach ($this->client->sendSync(
                    new Request($this->menu . '/print .proplist=.id', $criteria)
                )->getAllOfType(Response::TYPE_DATA) as $response) {
                    $newId = $response->getProperty('.id');
                    $idList .= strtolower(
                        is_string($newId)
                        ? $newId
                        : stream_get_contents($newId) . ','
                    );
                }
            } elseif (is_callable($criteria)) {
                $idCache = array();
                foreach ($this->client->sendSync(
                    new Request($this->menu . '/print')
                )->getAllOfType(Response::TYPE_DATA) as $response) {
                    $newId = $response->getProperty('.id');
                    $newId = strtolower(
                        is_string($newId)
                        ? $newId
                        : stream_get_contents($newId)
                    );
                    if ($criteria($response)) {
                        $idList .= $newId . ',';
                    }
                    $idCache[] = $newId;
                }
                $this->idCache = $idCache;
            } else {
                $this->find();
                if (is_int($criteria)) {
                    if (isset($this->idCache[$criteria])) {
                        $idList = $this->idCache[$criteria] . ',';
                    }
                } else {
                    $criteria = (string)$criteria;
                    if ($criteria === (string)(int)$criteria) {
                        if (isset($this->idCache[(int)$criteria])) {
                            $idList .= $this->idCache[(int)$criteria] . ',';
                        }
                    } elseif (false === strpos($criteria, ',')) {
                        $idList .= $criteria . ',';
                    } else {
                        $criteriaArr = explode(',', $criteria);
                        for ($i = count($criteriaArr) - 1; $i >= 0; --$i) {
                            if ('' === $criteriaArr[$i]) {
                                unset($criteriaArr[$i]);
                            } elseif ('*' === $criteriaArr[$i][0]) {
                                $idList .= $criteriaArr[$i] . ',';
                                unset($criteriaArr[$i]);
                            }
                        }
                        if (!empty($criteriaArr)) {
                            $idList .= call_user_func_array(
                                array($this, 'find'),
                                $criteriaArr
                            ) . ',';
                        }
                    }
                }
            }
        }
        return rtrim($idList, ',');
    }

    /**
     * Gets a value of a specified item at the current menu.
     *
     * @param int|string|null|Query $number    A number identifying the target
     *     item. Can also be an ID or (in some menus) name. For menus where
     *     there are no items (e.g. "/system identity"), you can specify NULL.
     *     You can also specify a {@link Query}, in which case the first match
     *     will be considered the target item.
     * @param string|resource|null  $valueName The name of the value to get.
     *     If omitted, or set to NULL, gets all properties of the target item.
     *
     * @return string|resource|null|array The value of the specified
     *     property as a string or as new PHP temp stream if the underlying
     *     {@link Client::isStreamingResponses()} is set to TRUE.
     *     If the property is not set, NULL will be returned.
     *     If $valueName is NULL, returns all properties as an array, where
     *     the result is parsed with {@link Script::parseValueToArray()}.
     *
     * @throws RouterErrorException When the router returns an error response
     *     (e.g. no such item, invalid property, etc.).
     */
    public function get($number, $valueName = null)
    {
        if ($number instanceof Query) {
            $number = explode(',', $this->find($number));
            $number = $number[0];
        } elseif (is_int($number) || ((string)$number === (string)(int)$number)) {
            $this->find();
            if (isset($this->idCache[(int)$number])) {
                $number = $this->idCache[(int)$number];
            } else {
                throw new RouterErrorException(
                    'Unable to resolve number from ID cache (no such item maybe)',
                    RouterErrorException::CODE_CACHE_ERROR
                );
            }
        }

        $request = new Request($this->menu . '/get');
        $request->setArgument('number', $number);
        $request->setArgument('value-name', $valueName);
        $responses = $this->client->sendSync($request);
        if (Response::TYPE_ERROR === $responses->getType()) {
            throw new RouterErrorException(
                'Error getting property',
                RouterErrorException::CODE_GET_ERROR,
                null,
                $responses
            );
        }

        $result = $responses->getProperty('ret');
        if (Stream::isStream($result)) {
            $result = stream_get_contents($result);
        }
        if (null === $valueName) {
            // @codeCoverageIgnoreStart
            //Some earlier RouterOS versions use "," instead of ";" as separator
            //Newer versions can't possibly enter this condition
            if (false === strpos($result, ';')
                && preg_match('/^([^=,]+\=[^=,]*)(?:\,(?1))+$/', $result)
            ) {
                $result = str_replace(',', ';', $result);
            }
            // @codeCoverageIgnoreEnd
            return Script::parseValueToArray('{' . $result . '}');
        }
        return $result;
    }

    /**
     * Enables all items at the current menu matching certain criteria.
     *
     * Zero or more arguments can be specified, each being a criteria.
     * If zero arguments are specified, enables all items.
     * See {@link static::find()} for a description of what criteria are
     * accepted.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function enable()
    {
        $responses = $this->doBulk('enable', func_get_args());
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when enabling items',
                RouterErrorException::CODE_ENABLE_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Disables all items at the current menu matching certain criteria.
     *
     * Zero or more arguments can be specified, each being a criteria.
     * If zero arguments are specified, disables all items.
     * See {@link static::find()} for a description of what criteria are
     * accepted.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function disable()
    {
        $responses = $this->doBulk('disable', func_get_args());
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when disabling items',
                RouterErrorException::CODE_DISABLE_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Removes all items at the current menu matching certain criteria.
     *
     * Zero or more arguments can be specified, each being a criteria.
     * If zero arguments are specified, removes all items.
     * See {@link static::find()} for a description of what criteria are
     * accepted.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function remove()
    {
        $responses = $this->doBulk('remove', func_get_args());
        $this->clearIdCache();
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when removing items',
                RouterErrorException::CODE_REMOVE_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Comments items.
     *
     * Sets new comments on all items at the current menu
     * which match certain criteria, using the "comment" command.
     *
     * Note that not all menus have a "comment" command. Most notably, those are
     * menus without items in them (e.g. "/system identity"), and menus with
     * fixed items (e.g. "/ip service").
     *
     * @param mixed           $numbers Targeted items. Can be any criteria
     *     accepted by {@link static::find()}.
     * @param string|resource $comment The new comment to set on the item as a
     *     string or a seekable stream.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function comment($numbers, $comment)
    {
        $commentRequest = new Request($this->menu . '/comment');
        $commentRequest->setArgument('comment', $comment);
        $commentRequest->setArgument('numbers', $this->find($numbers));
        $responses = $this->client->sendSync($commentRequest);
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when commenting items',
                RouterErrorException::CODE_COMMENT_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Sets new values.
     *
     * Sets new values on certain properties on all items at the current menu
     * which match certain criteria.
     *
     * @param mixed                                           $numbers   Items
     *     to be modified.
     *     Can be any criteria accepted by {@link static::find()} or NULL
     *     in case the menu is one without items (e.g. "/system identity").
     * @param array<string,string|resource>|array<int,string> $newValues An
     *     array with the names of each property to set as an array key, and the
     *     new value as an array value.
     *     Flags (properties with a value "true" that is interpreted as
     *     equivalent of "yes" from CLI) can also be specified with a numeric
     *     index as the array key, and the name of the flag as the array value.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function set($numbers, array $newValues)
    {
        $setRequest = new Request($this->menu . '/set');
        foreach ($newValues as $name => $value) {
            if (is_int($name)) {
                $setRequest->setArgument($value, 'true');
            } else {
                $setRequest->setArgument($name, $value);
            }
        }
        if (null !== $numbers) {
            $setRequest->setArgument('numbers', $this->find($numbers));
        }
        $responses = $this->client->sendSync($setRequest);
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when setting items',
                RouterErrorException::CODE_SET_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Alias of {@link static::set()}
     *
     * @param mixed                $numbers   Items to be modified.
     *     Can be any criteria accepted by {@link static::find()} or NULL
     *     in case the menu is one without items (e.g. "/system identity").
     * @param string               $valueName Name of property to be modified.
     * @param string|resource|null $newValue  The new value to set.
     *     If set to NULL, the property is unset.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function edit($numbers, $valueName, $newValue)
    {
        return null === $newValue
            ? $this->unsetValue($numbers, $valueName)
            : $this->set($numbers, array($valueName => $newValue));
    }

    /**
     * Unsets a value of a specified item at the current menu.
     *
     * Equivalent of scripting's "unset" command. The "Value" part in the method
     * name is added because "unset" is a language construct, and thus a
     * reserved word.
     *
     * @param mixed  $numbers   Targeted items. Can be any criteria accepted
     *     by {@link static::find()}.
     * @param string $valueName The name of the value you want to unset.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function unsetValue($numbers, $valueName)
    {
        $unsetRequest = new Request($this->menu . '/unset');
        $responses = $this->client->sendSync(
            $unsetRequest->setArgument('numbers', $this->find($numbers))
                ->setArgument('value-name', $valueName)
        );
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when unsetting value of items',
                RouterErrorException::CODE_UNSET_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Adds a new item at the current menu.
     *
     * @param array<string,string|resource>|array<int,string> $values Accepts
     *     one or more items to add to the current menu.
     *     The data about each item is specified as an array with the names of
     *     each property as an array key, and the value as an array value.
     *     Flags (properties with a value "true" that is interpreted as
     *     equivalent of "yes" from CLI) can also be specified with a numeric
     *     index as the array key, and the name of the flag as the array value.
     * @param array<string,string|resource>|array<int,string> $...    Additional
     *     items.
     *
     * @return string A comma separated list of the new items' IDs.
     *
     * @throws RouterErrorException When one or more items were not succesfully
     *     added. Note that the response collection will include all replies of
     *     all add commands, including the successful ones, in order.
     */
    public function add(array $values)
    {
        $addRequest = new Request($this->menu . '/add');
        $hasErrors = false;
        $results = array();
        foreach (func_get_args() as $values) {
            if (!is_array($values)) {
                continue;
            }
            foreach ($values as $name => $value) {
                if (is_int($name)) {
                    $addRequest->setArgument($value, 'true');
                } else {
                    $addRequest->setArgument($name, $value);
                }
            }
            $result = $this->client->sendSync($addRequest);
            if (count($result->getAllOfType(Response::TYPE_ERROR)) > 0) {
                $hasErrors = true;
            }
            $results = array_merge($results, $result->toArray());
            $addRequest->removeAllArguments();
        }

        $this->clearIdCache();
        if ($hasErrors) {
            throw new RouterErrorException(
                'Router returned error when adding items',
                RouterErrorException::CODE_ADD_ERROR,
                null,
                new ResponseCollection($results)
            );
        }
        $results = new ResponseCollection($results);
        $idList = '';
        foreach ($results->getAllOfType(Response::TYPE_FINAL) as $final) {
            $idList .= ',' . strtolower($final->getProperty('ret'));
        }
        return substr($idList, 1);
    }

    /**
     * Moves items at the current menu before a certain other item.
     *
     * Moves items before a certain other item. Note that the "move"
     * command is not available on all menus. As a rule of thumb, if the order
     * of items in a menu is irrelevant to their interpretation, there won't
     * be a move command on that menu. If in doubt, check from a terminal.
     *
     * @param mixed $numbers     Targeted items. Can be any criteria accepted
     *     by {@link static::find()}.
     * @param mixed $destination Item before which the targeted items will be
     *     moved to. Can be any criteria accepted by {@link static::find()}.
     *     If multiple items match the criteria, the targeted items will move
     *     above the first match.
     *     If NULL is given (or this argument is omitted), the targeted items
     *     will be moved to the bottom of the menu.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect the output. Current RouterOS versions don't return
     *     anything useful, but if future ones do, you can read it right away.
     *
     * @throws RouterErrorException When the router returns one or more errors.
     */
    public function move($numbers, $destination = null)
    {
        $moveRequest = new Request($this->menu . '/move');
        $moveRequest->setArgument('numbers', $this->find($numbers));
        if (null !== $destination) {
            $destination = $this->find($destination);
            if (false !== strpos($destination, ',')) {
                $destination = strstr($destination, ',', true);
            }
            $moveRequest->setArgument('destination', $destination);
        }
        $this->clearIdCache();
        $responses = $this->client->sendSync($moveRequest);
        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when moving items',
                RouterErrorException::CODE_MOVE_ERROR,
                null,
                $responses
            );
        }
        return $responses;
    }

    /**
     * Counts items at the current menu.
     *
     * Counts items at the current menu. This executes a dedicated command
     * ("print" with a "count-only" argument) on RouterOS, which is why only
     * queries are allowed as a criteria, in contrast with
     * {@link static::find()}, where numbers and callbacks are allowed also.
     *
     * @param Query|null           $query A query to filter items by.
     *     Without it, all items are included in the count.
     * @param string|resource|null $from  A comma separated list of item IDs.
     *     Any items in the set that still exist at the time of couting
     *     are included in the final tally. Note that the $query filters this
     *     set further (i.e. the item must be in the list AND match the $query).
     *     Leaving the value to NULL means all matching items at the current
     *     menu are included in the count.
     *
     * @return int The number of items, or -1 on failure (e.g. if the
     *     current menu does not have a "print" command or items to be counted).
     */
    public function count(Query $query = null, $from = null)
    {
        $countRequest = new Request(
            $this->menu . '/print count-only=""',
            $query
        );
        $countRequest->setArgument('from', $from);
        $result = $this->client->sendSync($countRequest)->end()
            ->getProperty('ret');

        if (null === $result) {
            return -1;
        }
        if (Stream::isStream($result)) {
            $result = stream_get_contents($result);
        }
        return (int)$result;
    }

    /**
     * Gets all items in the current menu.
     *
     * Gets all items in the current menu, using a print request.
     *
     * @param array<string,string|resource>|array<int,string> $args  Additional
     *     arguments to pass to the request.
     *     Each array key is the name of the argument, and each array value is
     *     the value of the argument to be passed.
     *     Arguments without a value (i.e. empty arguments) can also be
     *     specified using a numeric key, and the name of the argument as the
     *     array value.
     *     The "follow" and "follow-only" arguments are prohibited,
     *     as they would cause a synchronous request to run forever, without
     *     allowing the results to be observed.
     *     If you need to use those arguments, use {@link static::newRequest()},
     *     and pass the resulting {@link Request} to {@link Client::sendAsync()}.
     *     The "count-only" argument is also prohibited, as results from it
     *     would not be consumable. Use {@link static::count()} for that.
     * @param Query|null                                      $query A query to
     *     filter items by.
     *     NULL to get all items.
     *
     * @return ResponseCollection A response collection with all
     *     {@link Response::TYPE_DATA} responses. The collection will be empty
     *     when there are no matching items.
     *
     * @throws NotSupportedException If $args contains prohibited arguments
     *     ("follow", "follow-only" or "count-only").
     *
     * @throws RouterErrorException When there's an error upon attempting to
     *     call the "print" command on the specified menu (e.g. if there's no
     *     "print" command at the menu to begin with).
     */
    public function getAll(array $args = array(), Query $query = null)
    {
        $printRequest = new Request($this->menu . '/print', $query);
        foreach ($args as $name => $value) {
            if (is_int($name)) {
                $printRequest->setArgument($value);
            } else {
                $printRequest->setArgument($name, $value);
            }
        }

        foreach (array('follow', 'follow-only', 'count-only') as $arg) {
            if ($printRequest->getArgument($arg) !== null) {
                throw new NotSupportedException(
                    "The argument '{$arg}' was specified, but is prohibited",
                    NotSupportedException::CODE_ARG_PROHIBITED,
                    null,
                    $arg
                );
            }
        }
        $responses = $this->client->sendSync($printRequest);

        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            throw new RouterErrorException(
                'Error when reading items',
                RouterErrorException::CODE_GETALL_ERROR,
                null,
                $responses
            );
        }
        return $responses->getAllOfType(Response::TYPE_DATA);
    }

    /**
     * Puts a file on RouterOS's file system.
     *
     * Puts a file on RouterOS's file system, regardless of the current menu.
     * Note that this is a **VERY VERY VERY** time consuming method - it takes a
     * minimum of a little over 4 seconds, most of which are in sleep. It waits
     * 2 seconds after a file is first created (required to actually start
     * writing to the file), and another 2 seconds after its contents is written
     * (performed in order to verify success afterwards).
     * Similarly for removal (when $data is NULL) - there are two seconds in
     * sleep, used to verify the file was really deleted.
     *
     * If you want an efficient way of transferring files, use (T)FTP.
     * If you want an efficient way of removing files, use
     * {@link static::setMenu()} to move to the "/file" menu, and call
     * {@link static::remove()} without performing verification afterwards.
     *
     * @param string               $filename  The filename to write data in.
     * @param string|resource|null $data      The data the file is going to have
     *     as a string or a seekable stream.
     *     Setting the value to NULL removes a file of this name.
     *     If a seekable stream is provided, it is sent from its current
     *     position to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param bool                 $overwrite Whether to overwrite the file if
     *     it exists.
     *
     * @return bool TRUE on success, FALSE on failure.
     */
    public function filePutContents($filename, $data, $overwrite = false)
    {
        $printRequest = new Request(
            '/file/print .proplist=""',
            Query::where('name', $filename)
        );
        $fileExists = count($this->client->sendSync($printRequest)) > 1;

        if (null === $data) {
            if (!$fileExists) {
                return false;
            }
            $removeRequest = new Request('/file/remove');
            $this->client->sendSync(
                $removeRequest->setArgument('numbers', $filename)
            );
            //Required for RouterOS to REALLY remove the file.
            sleep(2);
            return !(count($this->client->sendSync($printRequest)) > 1);
        }

        if (!$overwrite && $fileExists) {
            return false;
        }
        $result = $this->client->sendSync(
            $printRequest->setArgument('file', $filename)
        );
        if (count($result->getAllOfType(Response::TYPE_ERROR)) > 0) {
            return false;
        }
        //Required for RouterOS to write the initial file.
        sleep(2);
        $setRequest = new Request('/file/set contents=""');
        $setRequest->setArgument('numbers', $filename);
        $this->client->sendSync($setRequest);
        $this->client->sendSync($setRequest->setArgument('contents', $data));
        //Required for RouterOS to write the file's new contents.
        sleep(2);

        $fileSize = $this->client->sendSync(
            $printRequest->setArgument('file', null)
                ->setArgument('.proplist', 'size')
        )->getProperty('size');
        if (Stream::isStream($fileSize)) {
            $fileSize = stream_get_contents($fileSize);
        }
        if (Communicator::isSeekableStream($data)) {
            return Communicator::seekableStreamLength($data) == $fileSize;
        } else {
            return sprintf('%u', strlen((string)$data)) === $fileSize;
        }
    }

    /**
     * Gets the contents of a specified file.
     *
     * @param string      $filename      The name of the file to get
     *     the contents of.
     * @param string|null $tmpScriptName In order to get the file's contents, a
     *     script is created at "/system script", the source of which is then
     *     overwritten with the file's contents, then retrieved from there,
     *     after which the script is removed.
     *     If this argument is left NULL, a random string,
     *     prefixed with the computer's name, is generated and used
     *     as the script's name.
     *     To eliminate any possibility of name clashes,
     *     you can specify your own name instead.
     *
     * @return string|resource The contents of the file as a string or as
     *     new PHP temp stream if the underlying
     *     {@link Client::isStreamingResponses()} is set to TRUE.
     *
     * @throws RouterErrorException When there's an error with the temporary
     *     script used to get the file, or if the file doesn't exist.
     */
    public function fileGetContents($filename, $tmpScriptName = null)
    {
        try {
            $responses = $this->exec(
                ':error ("&" . [/file get $filename contents]);',
                array('filename' => $filename),
                null,
                $tmpScriptName
            );
            throw new RouterErrorException(
                'Unable to read file through script (no error returned)',
                RouterErrorException::CODE_SCRIPT_FILE_ERROR,
                null,
                $responses
            );
        } catch (RouterErrorException $e) {
            if ($e->getCode() !== RouterErrorException::CODE_SCRIPT_RUN_ERROR) {
                throw $e;
            }
            $message = $e->getResponses()->getAllOfType(Response::TYPE_ERROR)
                ->getProperty('message');
            if (Stream::isStream($message)) {
                $successToken = fread($message, 1/*strlen('&')*/);
                if ('&' === $successToken) {
                    $messageCopy = fopen('php://temp', 'r+b');
                    stream_copy_to_stream($message, $messageCopy);
                    rewind($messageCopy);
                    fclose($message);
                    return $messageCopy;
                }
                rewind($message);
            } elseif (strpos($message, '&') === 0) {
                return substr($message, 1/*strlen('&')*/);
            }
            throw $e;
        }
    }

    /**
     * Performs an action on a bulk of items at the current menu.
     *
     * @param string $command What command to perform.
     * @param array  $args    Zero or more arguments can be specified,
     *     each being a criteria.
     *     If zero arguments are specified, matches all items.
     *     See {@link static::find()} for a description of what criteria are
     *     accepted.
     *
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect errors, if any.
     */
    protected function doBulk($command, array $args = array())
    {
        $bulkRequest = new Request("{$this->menu}/{$command}");
        $bulkRequest->setArgument(
            'numbers',
            call_user_func_array(array($this, 'find'), $args)
        );
        return $this->client->sendSync($bulkRequest);
    }
}


File: /src\Libs\pear2\vendor\pear2\net_routeros\stub.php
<?php

/**
 * Stub for PEAR2_Net_RouterOS.
 *
 * PHP version 5.3
 *
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   GIT: $Id$
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */

if (count(get_included_files()) > 1 || ('cli' === PHP_SAPI && $argc > 1)) {
    Phar::mapPhar();

    include_once 'phar://' . __FILE__ . DIRECTORY_SEPARATOR
        . '@PACKAGE_NAME@-@PACKAGE_VERSION@' . DIRECTORY_SEPARATOR
        . 'src' . DIRECTORY_SEPARATOR
        . 'PEAR2' . DIRECTORY_SEPARATOR
        . 'Autoload.php';

    //Run console if there are any arguments,
    //and we are running directly.
    if ('cli' === PHP_SAPI && $argc > 1 && 2 === count(get_included_files())) {
        include_once 'phar://' . __FILE__ . DIRECTORY_SEPARATOR
            . '@PACKAGE_NAME@-@PACKAGE_VERSION@' . DIRECTORY_SEPARATOR
            . 'scripts' . DIRECTORY_SEPARATOR
            . 'roscon.php';
    }
    return;
}

if ('cli' !== PHP_SAPI) {
    header('Content-Type: text/plain;charset=UTF-8');
}
echo "@PACKAGE_NAME@ @PACKAGE_VERSION@\n";

if (version_compare(phpversion(), '5.3.0', '<')) {
    echo "\nERROR: This package requires PHP 5.3.0 or later.\n";
    exit(1);
}

$missing_extensions = array();
foreach (array('spl', 'pcre') as $ext) {
    if (!extension_loaded($ext)) {
        $missing_extensions[] = $ext;
    }
}
if ($missing_extensions) {
    echo "\nERROR: You must compile PHP with the following extensions enabled:\n",
        implode(', ', $missing_extensions), "\n",
        "or install the necessary extensions for your distribution.\n";
    exit(1);
}

$supportsPhar = extension_loaded('phar');
if ($supportsPhar) {
    try {
        $phar = new Phar(__FILE__);
        $sig = $phar->getSignature();
        echo "{$sig['hash_type']} hash: {$sig['hash']}\n";
    } catch (Exception $e) {
        echo <<<HEREDOC

The PHAR extension is available, but was unable to read this PHAR file's hash.

HEREDOC;
        if (false !== strpos($e->getMessage(), 'file extension')) {
            echo <<<HEREDOC
This can happen if you've renamed the file to ".php" instead of ".phar".
Regardless, you should be able to include this file without problems.
HEREDOC;
        } else {
            echo 'Details: ' . $e->getMessage();
        }
    }
} else {
    echo <<<HEREDOC
WARNING: If you wish to use this package directly from this archive, you need
         to install and enable the PHAR extension. Otherwise, you must instead
         extract this archive, and include the autoloader.

HEREDOC;
}

echo "\n" . str_repeat('=', 80) . "\n";
if (extension_loaded('openssl')) {
    echo <<<HEREDOC
The OpenSSL extension is loaded. If you can make any connection whatsoever, you
should also be able to make an encrypted one to RouterOS 6.1 or later.

Note that due to known issues with PHP itself, encrypted connections may be
unstable (as in "sometimes disconnect suddenly" or "sometimes hang when you use
Client::sendSync() and/or Client::completeRequest() and/or Client::loop()
without a timeout").

HEREDOC;
} else {
    echo <<<HEREDOC
WARNING: The OpenSSL extension is not loaded.
         You can't make encrypted connections without it.

HEREDOC;
}

echo "\n" . str_repeat('=', 80) . "\n";
if (function_exists('stream_socket_client')) {
    echo <<<HEREDOC
The stream_socket_client() function is enabled.
If you can't connect to RouterOS from your code, try to connect using the API
console. Make sure to check your web server's firewall.

HEREDOC;
} else {
    echo <<<HEREDOC
WARNING: stream_socket_client() is disabled.
         Without it, you won't be able to connect to any RouterOS host.
         Enable it in php.ini, or ask your host to enable it for you.

HEREDOC;
}

echo "\n" . str_repeat('=', 80) . "\n";
$supportsResolver = function_exists('stream_resolve_include_path');
if (!$supportsPhar && !$supportsResolver) {
    echo <<<HEREDOC

WARNING: You can't use the API console in any way.
         If you want to use it, you must enable the PHAR extension
         (compiled into PHP by default) and/or the
         stream_resolve_include_path() function (available since PHP 5.3.2).

HEREDOC;
} else {
    if ($supportsPhar) {
        echo <<<HEREDOC
You can access the console by rerunning this file from the command line with
arguments. To see usage instructions, use the "--help" argument.

HEREDOC;
    }
    if ($supportsResolver) {
        echo <<<HEREDOC
Note that if you extract this PHAR file (or install it with Pyrus, PEAR or
Composer), you can also use the console through the "roscon" executable file.

HEREDOC;
    } else {
        echo <<<HEREDOC
WARNING: You can ONLY use the console through the PHAR file, because the
         stream_resolve_include_path() function is not available.

HEREDOC;
    }
}
__HALT_COMPILER();

File: /src\MikrotikServiceProvider.php
<?php
namespace Rajtika\Mikrotik;
require_once __DIR__ . '/Libs/mikrotik/core/mapi_routerosapi.php';
require_once  __DIR__ . '/Libs/pear2/vendor/autoload.php';

use Illuminate\Support\ServiceProvider;
use Rajtika\Mikrotik\Services\Mikrotik;
use Rajtika\Mikrotik\Services\Routeros;

class MikrotikServiceProvider extends ServiceProvider
{
    /**
     * Register services.
     *
     * @return void
     */
    public function register()
    {
        $this->app->bind('routeros', function () {
            return new Routeros();
        });
        $this->app->bind('mikrotik', function () {
            return new Mikrotik();
        });
        $this->publishes([
            __DIR__.'/config/mikrotik.php' =>  config_path('mikrotik.php'),
        ], 'config');
    }

    /**
     * Bootstrap services.
     *
     * @return void
     */
    public function boot()
    {
        //
    }
}


File: /src\Services\Mikrotik.php
<?php
namespace Rajtika\Mikrotik\Services;
use Illuminate\Support\Facades\Config;
use PEAR2\Console\CommandLine\Exception;
use PEAR2\Net\RouterOS;
use PEAR2\Net\RouterOS\Client;
use PEAR2\Net\RouterOS\Request;
use PEAR2\Net\RouterOS\Response;
use PEAR2\Net\RouterOS\Util;
use PEAR2\Net\RouterOS\Query;

class Mikrotik
{
    public   $host;
    public   $port;
    public   $user;
    public   $password;
    public   $service;
    public   $client;
    /**
     * @var bool
     */
    private $connected = false;

    public function __construct()
    {
        $this->host = Config::get('mikrotik.host');
        $this->port = ( !empty( Config::get('mikrotik.port') ) ) ? '8728' : Config::get('mikrotik.port');
        $this->user = Config::get('mikrotik.user');
        $this->password = Config::get('mikrotik.password');
        $this->service = ( Config::has('mikrotik.service') ) ? Config::get('mikrotik.service') : 'pppoe';

        //check mikrotik enabled then otherwize return with response and return true
//        return array('status' => true, 'msg' => 'Mikrotik not enabled in your settings.');
    }

    public function dump() {
        dd( 'Dump from Mikrotik Services for Pear2');
    }

    public function connect()
    {
        if( !empty( $this->host ) && !empty( $this->user ) && !empty( $this->password ) ) {
            try {
                $this->client = new Client($this->host, $this->user, $this->password, $this->port);
                $this->connected = true;
            } catch (Exception $e) {
                $this->connected = false;
            }
        } else {
            $this->connected = false;
        }
    }

    public function logs()
    {
        $response = array('status' => false, 'msg' => '');
        if( $this->mikrotik_enabled() ) {
            $this->connect();
            if( $this->connected == false ) {
                $response['msg'] = 'Could not connect to router.';
                $response['status'] = false;
                return $response;
            }
            try{
                $util = new Util( $this->client );
                $response['data'] = $util->setMenu('/log')->getAll();
            } catch (Exception $e) {
                $response['msg'] = 'An error occured to collect system user logs';
            }
        } else {
            $response['msg'] = 'Mikrotik configuration is not set.';
        }
        return $response;
    }

    public function getAll()
    {
        $response = array('status' => false, 'msg' => '', 'data' => []);
        if( $this->mikrotik_enabled() ) {
            $this->connect();
            if( $this->connected == false ) {
                $response['msg'] = 'Could not connect to router.';
                $response['status'] = false;
                return $response;
            }
            $response['data'] = $this->client->sendSync(new Request('/ppp/secret/print'))->getAllOfType(RouterOS\Response::TYPE_DATA);
            $response['status'] = true;
        } else {
            $response['msg'] = 'Mikrotik configuration is not set.';
        }
        return $response;
    }

    public function get( $id = null )
    {
        $response = ['status' => false, 'msg' => ''];
        if( $this->mikrotik_enabled() ) {
            $this->connect();
            if( $this->connected == false ) {
                $response['msg'] = 'Could not connect to router.';
                return $response;
            }
            if( $id != null ) {
                $customer = new Request('/ppp/secret/getall');
                $customer->setQuery(Query::where('.id', $id));
                $info = $this->client->sendSync($customer);
                if ( !empty( $info[0] ) ) :
                    $response['status'] = true;
                    $response['data'] = $info[0];
                endif;
            } else {
                $response['msg'] = 'Mikrotik ID not provided!';
            }
        } else {
            $response['msg'] = 'Mikrotik configuration is not set.';
        }

        return $response;
    }

    public function getByName( $name = '' ) {
        $response = array('status' => false, 'msg' => '');
        if( $this->mikrotik_enabled() ) {
            $this->connect();
            if( $this->connected == false ) {
                $response['msg'] = 'Could not connect to router.';
                return $response;
            }

            if( $name ) :
                $customer = new Request('/ppp/secret/getall');
                $customer->setArgument('.proplist', '.id,name,profile,disabled');
                $customer->setQuery(Query::where('name', $name));
                $info = $this->client->sendSync($customer);
                if ( !empty( $info[0] ) ) :
                    $response['status'] = true;
                    $response['data'] = $info[0];
                endif;
            else :
                $response['msg'] = 'Customer username is empty.';
            endif;
        } else {
            $response['msg'] = 'Mikrotik configuration is not set.';
        }
        return $response;
    }

    public function create( $customer ) {
        $response = ['status' => false, 'msg' => '', 'data' => []];
        //check mikrotike enabled
        if( $this->mikrotik_enabled() ) {
            $this->connect();
            if ($this->connected == false) {
                $response['msg'] = 'Router not connected';
                return $response;
            }
            $user = new RouterOS\Request('/ppp/secret/add');
            $user->setArgument('name', $customer->customerID);
            $user->setArgument('profile', $customer->package['code']);
            $user->setArgument('password', '123456');
            $user->setArgument('service', $this->service);
            $user->setArgument('comment', 'Via api [pkg - ' . $customer->package->name . ', price- ' . $customer->package['price'] . 'Tk., date- ' . date('d/m/Y'));
            $user->setArgument('disabled', 'no');

            if ($this->client->sendSync($user)->getType() !== RouterOS\Response::TYPE_FINAL) {
                $response['msg'] = 'Sorry! cannot create customer';
            } else {
//                $this->client->loop();
                $response['data'] = $this->getByName( $customer->customerID );
                $response['status'] = true;
                $response['msg'] = 'Customer has been successfully created';
            }
        } else {
            $response['status'] = true;
            $response['msg'] = 'Mikrotik configuration is not set.';
        }
        return $response;
    }

    public function enable( $customer = '' ) {
        $response = ['status' => false, 'msg' => '', 'data' => []];
        if( $this->mikrotik_enabled() ) {
            $this->connect();
            if ($this->connected == false) {
                $response['msg'] = 'Could not connect to router';
                return $response;
            }
            if ($customer !== '') {
                $mktikId = $customer['mktikId'];
                if( empty( $mktikId ) ) {
                    $customerAcc = $this->getByName( $customer['customerID'] );
                    if( $customerAcc->status == true ) {
                        $mktikId = $customerAcc['data']->getProperty('.id');
                    }
                }
                if (!empty( $mktikId ) ) {
                    $customer = new RouterOS\Request('/ppp/secret/set');
                    $customer->setArgument('.id', $mktikId);
                    $customer->setArgument('disabled', 'no');
                    $customer->setArgument('.proplist', '.id,name,profile,service');
                    if ($this->client->sendSync($customer)->getType() === Response::TYPE_FINAL) {
                        $response['status'] = true;
                    } else {
                        $response['msg'] = 'Mikrotik! Customer cannot be enabled.';
                    }
                } else {
                    $response['msg'] = 'Mikrotik ID not set.';
                }
            } else {
                $response['msg'] = 'Customer not found.';
            }
        } else {
            $response['status'] = true;
            $response['msg'] = 'Mikrotike configuration not set.';
        }
        return $response;
    }

    public function disable( $customer = '' ) {
        $response = ['status' => true, 'msg' => ''];
        if( $this->mikrotik_enabled() ) {
            $this->connect();
            if ($this->connected == false) {
                $response['msg'] = 'Could not connect to router';
                return $response;
            }
            if ($customer != '') :
                $mktikId = $customer['mktikId'];
                if( $mktikId == '' ) {
                    $user = $this->getByName($customer['customerID']);
                    if( !empty($user['.id'] ) ) {
                        $mktikId = $user['.id'];
                    }
                }

                if (empty($mktikId)) {
                    $customer = new Request('/ppp/secret/set');
                    $customer->setArgument('.id', $mktikId);
                    $customer->setArgument('disabled', 'yes');
                    $customer->setArgument('.proplist', '.id,name,profile,service');
                    if ($this->client->sendSync($customer)->getType() === Response::TYPE_FINAL) {
                        $response['status'] = true;
                    } else {
                        $response['msg'] = 'Sorry! cannot disable customer';
                    }
                } else {
                    $response['msg'] = 'Customer not found in router.';
                }
            else :
                $response['msg'] = 'Mikrotik ID not found.';
            endif;
        } else {
            $response['status'] = true;
            $response['msg'] = 'Mikrotike configuration not set';
        }

        return $response;
    }

    public function changeName( $params = array() ) {
        $response = ['status' => false, 'msg' => ''];
        if( $this->mikrotik_enabled() ) {
            $this->connect();
            if( $this->connected == false ) {
                $response['msg'] = 'Could not connect to router';
                return $response;
            }
            if( $params['name'] != '' ) {
                $customer = new Request('/ppp/secret/set');
                $customer->setArgument('.id', $params['.id']);
                $customer->setArgument('name', $params['name']);
                if( $this->client->sendSync($customer)->getType() === Response::TYPE_FINAL ) {
                    $response['status'] = true;
                } else {
                    $response['msg'] = 'Sorry! cannot change customer name';
                }
            } else {
                $response['msg'] = 'Mikrotik ID not found.';
            }
        } else {
            $response['status'] = true;
            $response['msg'] = 'Mikrotike configuration not set.';
        }
        return $response;
    }

    public function changePassword( $params = array() ) {
        $response = ['status' => false, 'msg' => ''];
        if( $this->mikrotik_enabled() ) {
            $this->connect();
            if ($this->connected == false) {
                $response['msg'] = 'Could not connect to router';
                return $response;
            }
            if ($params['password'] != '') {
                $customer = new Request('/ppp/secret/set');
                $customer->setArgument('.id', $params['.id']);
                $customer->setArgument('password', $params['password']);
                if ($this->client->sendSync($customer)->getType() === Response::TYPE_FINAL) {
                    $response['status'] = true;
                } else {
                    $response['msg'] = 'Sorry! cannot change password';
                }
            } else {
                $response['msg'] = 'Your password is empty';
            }
        } else {
            $response['status'] = true;
            $response['msg'] = 'Mikrotike configuration not set.';
        }
        return $response;
    }

    /**
     * Change Profile means Change the Packege
     **/
    public function changeProfile( $params = array() ) {
        $response = ['status' => false, 'msg' => ''];
        if( $this->mikrotik_enabled() ) {
            $this->connect();
            if ($this->connected == false) {
                $response['msg'] = 'Could not connect to router';
                return $response;
            }
            if ($params['profile'] != '') {
                $customer = new Request('/ppp/secret/set');
                $customer->setArgument('.id', $params['.id']);
                $customer->setArgument('profile', $params['profile']);
                if ($this->client->sendSync($customer)->getType() === Response::TYPE_FINAL) {
                    $response['status'] = true;
                    $response['msg'] = 'Customer package has been successfully changed!';
                } else {
                    $response['msg'] = 'Sorry! cannot change package';
                }
            } else {
                $response['msg'] = 'Customer package not selected.';
            }
        } else {
            $response['status'] = true;
            $response['msg'] = 'Mikrotike configuration not set.';
        }

        return $response;
    }

    public function resource()
    {
        $response = ['status' => false, 'msg' => ''];
        $this->connect();
        if( $this->connected == false ) {
            $response['msg'] = 'Could not connect to router';
            return $response;
        }
        $query = $this->comm("/system/resource/print"); ///system/resource/print
        if(!empty($query) && is_array($query)) {
            $response['data'] = $query[0];
        } else {
            $response['msg'] = 'Could not fetch resources';
        }
        return $response;
    }

    private function mikrotik_enabled()
    {
        if ( getOption('mikrotik_access') ) {
            if( !empty( $this->host ) && !empty( $this->user ) && $this->password && $this->port ) {
                return true;
            }
        }
        return false;
    }

    private function _exist( $params ) {
        $this->connect();
        if( $this->connected == false ) {
            $this->customer_exist = false;
        }
        if( $params['name'] ) {
            $customer = new Request('/ppp/secret/getall');
            $customer->setArgument('.proplist', '.id,name,profile,service');
            $customer->setQuery(Query::where('name', $params['name']));
            $id = $this->client->sendSync($customer)->getProperty('.id');
            if( !empty($id) && is_array($id) ) {
                $this->customer_exist = true;
            }
        }
    }

    public function __destruct()
    {
//        $this->disconnect();
    }
}


File: /src\Services\Routeros.php
<?php
namespace Rajtika\Mikrotik\Services;
use Illuminate\Support\Facades\Config;
use RouterosAPI;

class Routeros extends RouterosAPI
{
    public $host;
    public $port;
    public $user;
    public $password;
    private $service;

    public function __construct()
    {
        $this->host = Config::get('mikrotik.host');
        $this->port = Config::get('mikrotik.port');
        $this->user = Config::get('mikrotik.user');
        $this->password = Config::get('mikrotik.password');
        $this->service = ( Config::has('mikrotik.service') ) ? Config::get('mikrotik.service') : 'pppoe';
    }

    public function _connect()
    {
        return $this->connect();
    }

    public function get( $id = null )
    {
        $response = ['status' => false, 'msg' => ''];
        $this->connect();
        if( $this->connected == false ) {
            $response['msg'] = 'Could not connect to router.';
            return $response;
        }
        if( $id != null ) {
            $info = $this->comm("/ppp/secret/getall", array("?.id" => $id));
            if (!empty($info) && is_array($info)) {
                $response['data'] = $info;
                $response['status'] = true;
            }
        } else {
            $response['msg'] = 'Mikrotik ID not provided!';
        }

        return $response;
    }

    public function getAll()
    {
        $response = array('status' => true, 'msg' => '');
        $this->connect();
        if( $this->connected == false ) {
            $response['msg'] = 'Could not connect to router.';
            $response['status'] = false;
            return $response;
        }
        $this->write( '/ppp/secret/getall' );
        $read = $this->read( false );
        $response['data'] = $this->parseResponse( $read );
        return $response;
    }

    public function getByName( $name = '' ) {
        $response = array('status' => false, 'msg' => '');
        $this->connect();
        if( $this->connected == false ) {
            $response['msg'] = 'Could not connect to router.';
            return $response;
        }
        if( $name ) :
            $info = $this->comm( "/ppp/secret/getall", array( "?name" => $name ) );
            if ( !empty( $info[0] ) ) :
                $response['status'] = true;
                $response['data'] = $info[0];
            endif;
        else :
            $response['msg'] = 'Customer username is empty.';
        endif;

        return $response;
    }

    public function create( $params = array() ) {
        $params['service'] =$this->service;
        $response = ['status' => false, 'msg' => ''];
        $this->connect();
        if( $this->connected == false ) {
            $response['msg'] = 'Router not connected';
            return $response;
        }
        if( $this->_client_exist( $params ) == False ) :
            $res = $this->comm( "/ppp/secret/add", $params );
            $response['mktikId'] = $res;
            $response['status'] = true;
        else :
            $response['msg'] = 'Customer already exist in router';
        endif;

        return $response;
    }

    public function enable( $mktikId = '' ) {
        $response = ['status' => false, 'msg' => ''];
        $this->connect();
        if( $this->connected == false ) {
            $response['msg'] = 'Could not connect to router';
            return $response;
        }
        if( $mktikId !== '' ) :
            $params = array( ".id" => $mktikId, "disabled"  => "no" );
            $this->comm( "/ppp/secret/set", $params );
            $res = $this->comm( "/ppp/secret/getall", array( "?.id" => $mktikId ) );
            if ( !empty( $res ) && $res[0]['disabled'] == 'false' ) {
                $response['status'] = true;
                $response['data'] = $res[0];
            } else {
                $response['msg'] = 'Sorry! cannot enable customer';
            }
        else :
            $response['msg'] = 'Mikrotik ID not found.';
        endif;

        return $response;
    }

    public function disable( $mktikId = '' ) {
        $response = ['status' => false, 'msg' => ''];
        $this->connect();
        if( $this->connected == false ) {
            $response['msg'] = 'Could not connect to router';
            return $response;
        }
        if( $mktikId !== '' ) :
            $params = array( ".id" => $mktikId, "disabled"  => "yes" );
            $this->comm( "/ppp/secret/set", $params );
            $res = $this->comm( "/ppp/secret/getall", array( ".proplist"=> ".id,name,profile,disabled", "?.id" => $mktikId ) );
            if ( !empty( $res ) && $res[0]['disabled'] == 'true' ) {
                $response['status'] = true;
                $response['data'] = $res[0];
            } else {
                $response['msg'] = 'Sorry! cannot disable customer';
            }
        else :
            $response['msg'] = 'Mikrotik ID not found.';
        endif;

        return $response;
    }

    public function changeName( $params = array() ) {
        $response = ['status' => false, 'msg' => ''];
        $this->connect();
        if( $this->connected == false ) {
            $response['msg'] = 'Could not connect to router';
            return $response;
        }
        if( $params['name'] != '' ) {
            $this->comm("/ppp/secret/set", $params);
            $res = $this->comm("/ppp/secret/getall", array(".proplist" => ".id,name,profile", "?.id" => $params['.id']));
            if ( $res[0]['name'] == $params['name'] ) {
                $response['status'] = true;
                $response['data'] = $res[0];
            } else {
                $response['msg'] = 'Sorry! cannot disable customer';
            }
        } else {
            $response['msg'] = 'Mikrotik ID not found.';
        }

        return $response;
    }

    public function changePassword( $params = array() ) {
        $response = ['status' => false, 'msg' => ''];
        $this->connect();
        if( $this->connected == false ) {
            $response['msg'] = 'Could not connect to router';
            return $response;
        }
        if( $params['password'] != '' ) {
            $this->comm("/ppp/secret/set", $params);
            $res = $this->comm("/ppp/secret/getall", array(".proplist" => ".id,name,profile,password", "?.id" => $params['.id']));
            if ( $res[0]['password'] == $params['password'] ) {
                $response['status'] = true;
                $response['data'] = $res[0];
            } else {
                $response['msg'] = 'Sorry! cannot change password';
            }
        } else {
            $response['msg'] = 'Your password is empty';
        }
        return $response;
    }

    /**
     * Change Profile means Change the Packege
     **/
    public function changeProfile( $params = array() ) {
        $response = ['status' => false, 'msg' => ''];
        $this->connect();
        if( $this->connected == false ) {
            $response['msg'] = 'Could not connect to router';
            return $response;
        }
        if( $params['password'] != '' ) {
            $this->comm("/ppp/secret/set", $params);
            $res = $this->comm("/ppp/secret/getall", array(".proplist" => "id,name,profile", "?.id" => $params['.id']));
            if ( $res[0]['profile'] == $params['profile'] ) {
                $response['status'] = true;
                $response['data'] = $res[0];
            } else {
                $response['msg'] = 'Sorry! cannot change package';
            }
        } else {
            $response['msg'] = 'Customer package not selected.';
        }
    }

    public function resource()
    {
        $response = ['status' => false, 'msg' => ''];
        $this->connect();
        if( $this->connected == false ) {
            $response['msg'] = 'Could not connect to router';
            return $response;
        }
        $query = $this->comm("/system/resource/print"); ///system/resource/print
        if(!empty($query) && is_array($query)) {
            $response['data'] = $query[0];
        } else {
            $response['msg'] = 'Could not fetch resources';
        }
        return $response;
    }

    private function _client_exist( $params ) {
        $this->connect();
        if( $this->connected == false ) return false;
        if( $params['name'] ) :
            $info = $this->comm( "/ppp/secret/getall", array( ".proplist"=> ".id", "?name" => $params['name'] ) );
            return ( !empty( $info ) && is_array( $info ) ) ? true : false;
        else :
            return false;
        endif;
    }

    public function __destruct()
    {
        $this->disconnect();
    }
}


