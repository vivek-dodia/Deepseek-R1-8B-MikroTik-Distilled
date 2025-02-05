# Repository Information
Name: mikrotik-qos

# Directory Structure
Directory structure:
└── github_repos/mikrotik-qos/
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
    │   │       ├── pack-1d9b9e03f9310c56bf688c744b74cad00db6882d.idx
    │   │       └── pack-1d9b9e03f9310c56bf688c744b74cad00db6882d.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── addtl-rules-fr-forums/
    │   ├── AccessPoint.rsc
    │   ├── FirewallCustom.rsc
    │   ├── README.md
    │   ├── router.rsc
    │   ├── RouterSwitchAP.rsc
    │   └── switch.rsc
    ├── anti-dhcp-starvation-attack.rsc
    ├── blacklist-bruteforce.rsc
    ├── bogons.rsc
    ├── dhcp-lease-script.rsc
    ├── firewall-mangle.rsc
    ├── initial-config.rsc
    ├── ip-settings.rsc
    ├── lease-script
    ├── queue-tree.rsc
    ├── README.md
    ├── ros-telegram-alert.rsc
    ├── scripts/
    │   ├── pihole-disable
    │   ├── pihole-enable
    │   └── timed-disable-device
    ├── ssh-tunnel.md
    └── syslog-trigger/
        ├── 00-vcode.conf
        ├── vcode.bash
        └── vcode.php


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
	url = https://github.com/dillagr/mikrotik-qos.git
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
0000000000000000000000000000000000000000 68f0046b1ce607b6e99ca3062aad0d2c3e314751 vivek-dodia <vivek.dodia@icloud.com> 1738606003 -0500	clone: from https://github.com/dillagr/mikrotik-qos.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 68f0046b1ce607b6e99ca3062aad0d2c3e314751 vivek-dodia <vivek.dodia@icloud.com> 1738606003 -0500	clone: from https://github.com/dillagr/mikrotik-qos.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 68f0046b1ce607b6e99ca3062aad0d2c3e314751 vivek-dodia <vivek.dodia@icloud.com> 1738606003 -0500	clone: from https://github.com/dillagr/mikrotik-qos.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
68f0046b1ce607b6e99ca3062aad0d2c3e314751 refs/remotes/origin/master


File: /.git\refs\heads\master
68f0046b1ce607b6e99ca3062aad0d2c3e314751


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /addtl-rules-fr-forums\AccessPoint.rsc
###############################################################################
# Topic:		Using RouterOS to VLAN your network
# Example:		Access Point
# Web:			https://forum.mikrotik.com/viewtopic.php?t=143620
# RouterOS:		6.43.13
# Date:			Mar 31, 2019
# Notes:		Start with a reset (/system reset-configuration)
# Thanks:		mkx, sindy
###############################################################################

#######################################
# Naming
#######################################

# name the device being configured
/system identity set name="AccessPoint"


#######################################
# VLAN Overview
#######################################

# 10 = BLUE
# 20 = GREEN
# 30 = RED
# 99 = BASE (MGMT) VLAN


#######################################
# WIFI Setup
#
# Example wireless settings only. Do
# NOT use in production!
#######################################

# Blue SSID
/interface wireless security-profiles set [ find default=yes ] authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key="password"
/interface wireless set [ find default-name=wlan1 ] ssid=BLUE_SSID frequency=auto mode=ap-bridge disabled=no

# Green SSID
/interface wireless security-profiles add name=GREEN_PROFILE authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key="password"
/interface wireless add name=wlan2 ssid=GREEN_SSID master-interface=wlan1 security-profile=GREEN_PROFILE disabled=no

# Red SSID
/interface wireless security-profiles add name=RED_PROFILE authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key="password"
/interface wireless add name=wlan3 ssid=RED_SSID master-interface=wlan1 security-profile=RED_PROFILE disabled=no


#######################################
# Bridge
#######################################

# create one bridge, set VLAN mode off while we configure
/interface bridge add name=BR1 protocol-mode=none vlan-filtering=no


#######################################
#
# -- Access Ports --
#
#######################################

# ingress behavior
/interface bridge port

# Blue, Green, Red VLAN
add bridge=BR1 interface=wlan1 pvid=10
add bridge=BR1 interface=wlan2 pvid=20
add bridge=BR1 interface=wlan3 pvid=30

# egress behavior
/interface bridge vlan

# Blue, Green, Red VLAN
add bridge=BR1 untagged=wlan1 vlan-ids=10
add bridge=BR1 untagged=wlan2 vlan-ids=20
add bridge=BR1 untagged=wlan3 vlan-ids=30


#######################################
#
# -- Trunk Ports --
#
#######################################

# ingress behavior
/interface bridge port

# Purple Trunk. Leave pvid set to default of 1
add bridge=BR1 interface=ether1

# egress behavior
/interface bridge vlan

# Purple Trunk. L2 switching only, Bridge not needed as tagged member (except BASE_VLAN)
set bridge=BR1 tagged=ether1 [find vlan-ids=10]
set bridge=BR1 tagged=ether1 [find vlan-ids=20]
set bridge=BR1 tagged=ether1 [find vlan-ids=30]
add bridge=BR1 tagged=BR1,ether1 vlan-ids=99


#######################################
# IP Addressing & Routing
#######################################

# LAN facing AP's Private IP address on a BASE_VLAN
/interface vlan add interface=BR1 name=BASE_VLAN vlan-id=99
/ip address add address=192.168.0.3/24 interface=BASE_VLAN

# The Router's IP this AP will use
/ip route add distance=1 gateway=192.168.0.1


#######################################
# IP Services
#######################################

# We have a router that will handle this. Nothing to set here.
# Attach this AP to a router configured as shown under the "RoaS" example.


#######################################
# VLAN Security
#######################################

# Only allow ingress packets without tags on Access Ports
/interface bridge port
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=wlan1]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=wlan2]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=wlan3]

# Only allow ingress packets WITH tags on Trunk Ports
/interface bridge port set bridge=BR1 ingress-filtering=yes frame-types=admit-only-vlan-tagged [find interface=ether1]


#######################################
# MAC Server settings
#######################################

# Ensure only visibility and availability from BASE_VLAN, the MGMT network
/interface list add name=BASE
/interface list member add interface=BASE_VLAN list=BASE
/ip neighbor discovery-settings set discover-interface-list=BASE
/tool mac-server mac-winbox set allowed-interface-list=BASE
/tool mac-server set allowed-interface-list=BASE


#######################################
# Turn on VLAN mode
#######################################
/interface bridge set BR1 vlan-filtering=yes



File: /addtl-rules-fr-forums\FirewallCustom.rsc
###############################################################################
# Topic:		Using RouterOS to VLAN your network
# Example:		Public VLAN, Printer & Server
# Web:			https://forum.mikrotik.com/viewtopic.php?t=143620
# RouterOS:		6.43.12
# Date:			Mar 28, 2019
# Notes:		Small changes made to our "RoaS" router firewall example.
# Thanks:		mkx, sindy
###############################################################################


##########################################
# Firewalling
#
# Here we show the small changes made
# to accomodate a Public VLAN or
# other shared resource (like a server)
##########################################

# Use MikroTik's "list" feature for easy rule matchmaking.

/interface list add name=WAN
/interface list add name=VLAN

/interface list member
add interface=ether1     list=WAN
add interface=BASE_VLAN  list=VLAN
add interface=BLUE_VLAN  list=VLAN
add interface=GREEN_VLAN list=VLAN
add interface=RED_VLAN   list=VLAN
add interface=BASE_VLAN  list=BASE


# VLAN aware firewall. Order is important.
/ip firewall filter


##################
# INPUT CHAIN
##################
add chain=input action=accept connection-state=established,related comment="Allow Estab & Related"

# Allow VLANs to access router services like DNS, Winbox. Naturally, you SHOULD make it more granular.
add chain=input action=accept in-interface-list=VLAN comment="Allow VLAN"

# Allow BASE_VLAN full access to the device for Winbox, etc.
add chain=input action=accept in-interface=BASE_VLAN comment="Allow Base_Vlan Full Access"

add chain=input action=drop comment="Drop"

##################
# FORWARD CHAIN
##################
add chain=forward action=accept connection-state=established,related comment="Allow Estab & Related"

# Optional: Disallow the Red VLAN from having Internet access:
# add chain=forward action=drop in-interface=RED_VLAN out-interface-list=WAN comment="Drop Red from Internet"

# Optional: Allow all VLANs to access the Internet AND each other
# add chain=forward action=accept connection-state=new in-interface-list=VLAN comment="VLAN inter-VLAN routing"

# Optional: Allow all VLANs to access a server (or printer) listening on Port 80 in the RED_VLAN
# add chain=forward action=accept connection-state=new in-interface-list=VLAN out-interface=RED_VLAN dst-port=80 protocol=tcp comment="Allow access to Server on RED_VLAN"

# Optional: Allow RED_VLAN to become a Public VLAN
add chain=forward action=accept connection-state=new in-interface-list=VLAN out-interface=RED_VLAN comment="Allow RED_VLAN to be the Public VLAN"

# Allow all VLANs to access the Internet only, NOT each other
add chain=forward action=accept connection-state=new in-interface-list=VLAN out-interface-list=WAN comment="VLAN Internet Access only"

add chain=forward action=drop comment="Drop"



File: /addtl-rules-fr-forums\README.md
## _Notes:_
These configuration(s) taken from the Mikrotik forums (needs login). Not mine.

More details here:
* [Using RouterOS to VLAN your network](https://forum.mikrotik.com/viewtopic.php?t=143620).
* [Using RouterOS to QoS your network](https://forum.mikrotik.com/viewtopic.php?t=73214)


File: /addtl-rules-fr-forums\router.rsc
###############################################################################
# Topic:		Using RouterOS to VLAN your network
# Example:		Switch with a separate router (RoaS)
# Web:			https://forum.mikrotik.com/viewtopic.php?t=143620
# RouterOS:		6.43.12
# Date:			Mar 28, 2019
# Notes:		Start with a reset (/system reset-configuration)
# Thanks:		mkx, sindy
###############################################################################

#######################################
# Naming
#######################################

# name the device being configured
/system identity set name="Router"


#######################################
# VLAN Overview
#######################################

# 10 = BLUE
# 20 = GREEN
# 30 = RED
# 99 = BASE (MGMT) VLAN


#######################################
# Bridge
#######################################

# create one bridge, set VLAN mode off while we configure
/interface bridge add name=BR1 protocol-mode=none vlan-filtering=no


#######################################
#
# -- Trunk Ports --
#
#######################################

# ingress behavior
/interface bridge port

# Purple Trunk. Leave pvid set to default of 1
add bridge=BR1 interface=ether2
add bridge=BR1 interface=ether3
add bridge=BR1 interface=ether4
add bridge=BR1 interface=ether5
add bridge=BR1 interface=ether6
add bridge=BR1 interface=ether7
add bridge=BR1 interface=sfp1

# egress behavior
/interface bridge vlan

# Purple Trunk. These need IP Services (L3), so add Bridge as member
add bridge=BR1 tagged=BR1,ether2,ether3,ether4,ether5,ether6,ether7,sfp1 vlan-ids=10
add bridge=BR1 tagged=BR1,ether2,ether3,ether4,ether5,ether6,ether7,sfp1 vlan-ids=20
add bridge=BR1 tagged=BR1,ether2,ether3,ether4,ether5,ether6,ether7,sfp1 vlan-ids=30
add bridge=BR1 tagged=BR1,ether2,ether3,ether4,ether5,ether6,ether7,sfp1 vlan-ids=99


#######################################
# IP Addressing & Routing
#######################################

# LAN facing router's IP address on the BASE_VLAN
/interface vlan add interface=BR1 name=BASE_VLAN vlan-id=99
/ip address add address=192.168.0.1/24 interface=BASE_VLAN

# DNS server, set to cache for LAN
/ip dns set allow-remote-requests=yes servers="9.9.9.9"

# Yellow WAN facing port with IP Address provided by ISP
/ip address add interface=ether1 address=a.a.a.a/aa network=a.a.a.0

# router's gateway provided by ISP
/ip route add distance=1 gateway=b.b.b.b


#######################################
# IP Services
#######################################

# Blue VLAN interface creation, IP assignment, and DHCP service
/interface vlan add interface=BR1 name=BLUE_VLAN vlan-id=10
/ip address add interface=BLUE_VLAN address=10.0.10.1/24
/ip pool add name=BLUE_POOL ranges=10.0.10.2-10.0.10.254
/ip dhcp-server add address-pool=BLUE_POOL interface=BLUE_VLAN name=BLUE_DHCP disabled=no
/ip dhcp-server network add address=10.0.10.0/24 dns-server=192.168.0.1 gateway=10.0.10.1

# Green VLAN interface creation, IP assignment, and DHCP service
/interface vlan add interface=BR1 name=GREEN_VLAN vlan-id=20
/ip address add interface=GREEN_VLAN address=10.0.20.1/24
/ip pool add name=GREEN_POOL ranges=10.0.20.2-10.0.20.254
/ip dhcp-server add address-pool=GREEN_POOL interface=GREEN_VLAN name=GREEN_DHCP disabled=no
/ip dhcp-server network add address=10.0.20.0/24 dns-server=192.168.0.1 gateway=10.0.20.1

# Red VLAN interface creation, IP assignment, and DHCP service
/interface vlan add interface=BR1 name=RED_VLAN vlan-id=30
/ip address add interface=RED_VLAN address=10.0.30.1/24
/ip pool add name=RED_POOL ranges=10.0.30.2-10.0.30.254
/ip dhcp-server add address-pool=RED_POOL interface=RED_VLAN name=RED_DHCP disabled=no
/ip dhcp-server network add address=10.0.30.0/24 dns-server=192.168.0.1 gateway=10.0.30.1

# Optional: Create a DHCP instance for BASE_VLAN. Convenience feature for an admin.
# /ip pool add name=BASE_POOL ranges=192.168.0.10-192.168.0.254
# /ip dhcp-server add address-pool=BASE_POOL interface=BASE_VLAN name=BASE_DHCP disabled=no
# /ip dhcp-server network add address=192.168.0.0/24 dns-server=192.168.0.1 gateway=192.168.0.1


#######################################
# Firewalling & NAT
# A good firewall for WAN. Up to you
# about how you want LAN to behave.
#######################################

# Use MikroTik's "list" feature for easy rule matchmaking.

/interface list add name=WAN
/interface list add name=VLAN
/interface list add name=BASE

/interface list member
add interface=ether1     list=WAN
add interface=BASE_VLAN  list=VLAN
add interface=BLUE_VLAN  list=VLAN
add interface=GREEN_VLAN list=VLAN
add interface=RED_VLAN   list=VLAN
add interface=BASE_VLAN  list=BASE

# VLAN aware firewall. Order is important.
/ip firewall filter


##################
# INPUT CHAIN
##################
add chain=input action=accept connection-state=established,related comment="Allow Estab & Related"

# Allow VLANs to access router services like DNS, Winbox. Naturally, you SHOULD make it more granular.
add chain=input action=accept in-interface-list=VLAN comment="Allow VLAN"

# Allow BASE_VLAN full access to the device for Winbox, etc.
add chain=input action=accept in-interface=BASE_VLAN comment="Allow Base_Vlan Full Access"

add chain=input action=drop comment="Drop"


##################
# FORWARD CHAIN
##################
add chain=forward action=accept connection-state=established,related comment="Allow Estab & Related"

# Allow all VLANs to access the Internet only, NOT each other
add chain=forward action=accept connection-state=new in-interface-list=VLAN out-interface-list=WAN comment="VLAN Internet Access only"

add chain=forward action=drop comment="Drop"


##################
# NAT
##################
/ip firewall nat add chain=srcnat action=masquerade out-interface-list=WAN comment="Default masquerade"


#######################################
# VLAN Security
#######################################

# Only allow packets with tags over the Trunk Ports
/interface bridge port
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-vlan-tagged [find interface=ether2]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-vlan-tagged [find interface=ether3]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-vlan-tagged [find interface=ether4]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-vlan-tagged [find interface=ether5]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-vlan-tagged [find interface=ether6]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-vlan-tagged [find interface=ether7]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-vlan-tagged [find interface=sfp1]


#######################################
# MAC Server settings
#######################################

# Ensure only visibility and availability from BASE_VLAN, the MGMT network
/ip neighbor discovery-settings set discover-interface-list=BASE
/tool mac-server mac-winbox set allowed-interface-list=BASE
/tool mac-server set allowed-interface-list=BASE


#######################################
# Turn on VLAN mode
#######################################
/interface bridge set BR1 vlan-filtering=yes



File: /addtl-rules-fr-forums\RouterSwitchAP.rsc
###############################################################################
# Topic:		Using RouterOS to VLAN your network
# Example:		Router-Switch-AP all in one device
# Web:			https://forum.mikrotik.com/viewtopic.php?t=143620
# RouterOS:		6.43.12
# Date:			Mar 28, 2019
# Notes:		Start with a reset (/system reset-configuration)
# Thanks:		mkx, sindy
###############################################################################

#######################################
# Naming
#######################################

# name the device being configured
/system identity set name="RouterSwitchAP"


#######################################
# VLAN Overview
#######################################

# 10 = BLUE
# 20 = GREEN
# 99 = BASE (MGMT) VLAN


#######################################
# WIFI Setup
#
# Example wireless settings only. Do
# NOT use in production!
#######################################

# Blue SSID
/interface wireless security-profiles set [ find default=yes ] authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key="password"
/interface wireless set [ find default-name=wlan1 ] ssid=BLUE frequency=auto mode=ap-bridge disabled=no

# Green SSID
/interface wireless security-profiles add name=guest authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key="password"
/interface wireless add name=wlan2 ssid=GREEN master-interface=wlan1 security-profile=guest disabled=no

# Optional: BASE SSID, admin level access to Winbox the device. Use a local ethernet port if preferred.
/interface wireless security-profiles add name=Base authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key="password"
/interface wireless add name=wlan3 ssid=BASE master-interface=wlan1 security-profile=Base disabled=no


#######################################
# Bridge
#######################################

# create one bridge, set VLAN mode off while we configure
/interface bridge add name=BR1 protocol-mode=none vlan-filtering=no


#######################################
#
# -- Access Ports --
#
#######################################

# ingress behavior
/interface bridge port

# Blue VLAN
add bridge=BR1 interface=ether2 pvid=10
add bridge=BR1 interface=ether3 pvid=10
add bridge=BR1 interface=wlan1  pvid=10

# Green VLAN
add bridge=BR1 interface=ether4 pvid=20
add bridge=BR1 interface=wlan2  pvid=20

# BASE_VLAN
add bridge=BR1 interface=wlan3 pvid=99

#
# egress behavior
#
/interface bridge vlan

# Blue, Green, & BASE VLAN
add bridge=BR1 untagged=ether2,ether3,wlan1 vlan-ids=10
add bridge=BR1 untagged=ether4,wlan2 vlan-ids=20
add bridge=BR1 untagged=wlan3 vlan-ids=99

# L3 switching so Bridge must be a tagged member
set bridge=BR1 tagged=BR1 [find vlan-ids=10]
set bridge=BR1 tagged=BR1 [find vlan-ids=20]
set bridge=BR1 tagged=BR1 [find vlan-ids=99]


#######################################
# IP Addressing & Routing
#######################################

# LAN facing router's IP address on the BASE_VLAN
/interface vlan add interface=BR1 name=BASE_VLAN vlan-id=99
/ip address add address=192.168.0.1/24 interface=BASE_VLAN

# DNS server, set to cache for LAN
/ip dns set allow-remote-requests=yes servers="9.9.9.9"

# Yellow WAN facing port with IP Address provided by ISP
/ip address add interface=ether1 address=a.a.a.a/aa network=a.a.a.0

# router's gateway provided by ISP
/ip route add distance=1 gateway=b.b.b.b


#######################################
# IP Services
#######################################

# Blue VLAN interface creation, IP assignment, and DHCP service
/interface vlan add interface=BR1 name=BLUE_VLAN vlan-id=10
/ip address add interface=BLUE_VLAN address=10.0.10.1/24
/ip pool add name=BLUE_POOL ranges=10.0.10.2-10.0.10.254
/ip dhcp-server add address-pool=BLUE_POOL interface=BLUE_VLAN name=BLUE_DHCP disabled=no
/ip dhcp-server network add address=10.0.10.0/24 dns-server=192.168.0.1 gateway=10.0.10.1

# Green VLAN interface creation, IP assignment, and DHCP service
/interface vlan add interface=BR1 name=GREEN_VLAN vlan-id=20
/ip address add interface=GREEN_VLAN address=10.0.20.1/24
/ip pool add name=GREEN_POOL ranges=10.0.20.2-10.0.20.254
/ip dhcp-server add address-pool=GREEN_POOL interface=GREEN_VLAN name=GREEN_DHCP disabled=no
/ip dhcp-server network add address=10.0.20.0/24 dns-server=192.168.0.1 gateway=10.0.20.1

# Optional: Create a DHCP instance for BASE_VLAN. Convenience feature for an admin.
# /ip pool add name=BASE_POOL ranges=192.168.0.10-192.168.0.254
# /ip dhcp-server add address-pool=BASE_POOL interface=BASE_VLAN name=BASE_DHCP disabled=no
# /ip dhcp-server network add address=192.168.0.0/24 dns-server=192.168.0.1 gateway=192.168.0.1


#######################################
# Firewalling & NAT
# A good firewall for WAN. Up to you
# about how you want LAN to behave.
#######################################

# Use MikroTik's "list" feature for easy rule matchmaking.

/interface list add name=WAN
/interface list add name=VLAN
/interface list add name=BASE

/interface list member
add interface=ether1     list=WAN
add interface=BASE_VLAN  list=VLAN
add interface=BLUE_VLAN  list=VLAN
add interface=GREEN_VLAN list=VLAN
add interface=BASE_VLAN  list=BASE

# VLAN aware firewall. Order is important.
/ip firewall filter


##################
# INPUT CHAIN
##################
add chain=input action=accept connection-state=established,related comment="Allow Estab & Related"

# Allow VLANs to access router services like DNS, Winbox. Naturally, you SHOULD make it more granular.
add chain=input action=accept in-interface-list=VLAN comment="Allow VLAN"

# Allow BASE_VLAN full access to the device for Winbox, etc.
add chain=input action=accept in-interface=BASE_VLAN comment="Allow Base_Vlan Full Access"

add chain=input action=drop comment="Drop"

##################
# FORWARD CHAIN
##################
add chain=forward action=accept connection-state=established,related comment="Allow Estab & Related"

# Allow all VLANs to access the Internet only, NOT each other
add chain=forward action=accept connection-state=new in-interface-list=VLAN out-interface-list=WAN comment="VLAN Internet Access only"

add chain=forward action=drop comment="Drop"

##################
# NAT
##################
/ip firewall nat add chain=srcnat action=masquerade out-interface-list=WAN comment="Default masquerade"


#######################################
# VLAN Security
#######################################

# Only allow ingress packets without tags on Access Ports
/interface bridge port
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether2]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether3]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether4]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=wlan1]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=wlan2]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=wlan3]


#######################################
# MAC Server settings
#######################################

# Ensure only visibility and availability from BASE_VLAN, the MGMT network
/ip neighbor discovery-settings set discover-interface-list=BASE
/tool mac-server mac-winbox set allowed-interface-list=BASE
/tool mac-server set allowed-interface-list=BASE


#######################################
# Turn on VLAN mode
#######################################
/interface bridge set BR1 vlan-filtering=yes



File: /addtl-rules-fr-forums\switch.rsc
###############################################################################
# Topic:		Using RouterOS to VLAN your network
# Example:		Switch with a separate router (RoaS)
# Web:			https://forum.mikrotik.com/viewtopic.php?t=143620
# RouterOS:		6.43.13
# Date:			Mar 31, 2019
# Notes:		Start with a reset (/system reset-configuration)
# Thanks:		mkx, sindy
###############################################################################

#######################################
# Naming
#######################################

# name the device being configured
/system identity set name="Switch"


#######################################
# VLAN Overview
#######################################

# 10 = BLUE
# 20 = GREEN
# 30 = RED
# 99 = BASE (MGMT) VLAN


#######################################
# Bridge
#######################################

# create one bridge, set VLAN mode off while we configure
/interface bridge add name=BR1 protocol-mode=none vlan-filtering=no


#######################################
#
# -- Access Ports --
#
#######################################

# ingress behavior
/interface bridge port

# Blue VLAN
add bridge=BR1 interface=ether1 pvid=10
add bridge=BR1 interface=ether2 pvid=10
add bridge=BR1 interface=ether3 pvid=10
add bridge=BR1 interface=ether4 pvid=10
add bridge=BR1 interface=ether5 pvid=10
add bridge=BR1 interface=ether6 pvid=10
add bridge=BR1 interface=ether7 pvid=10
add bridge=BR1 interface=ether8 pvid=10

# Green VLAN
add bridge=BR1 interface=ether9  pvid=20
add bridge=BR1 interface=ether10 pvid=20
add bridge=BR1 interface=ether11 pvid=20
add bridge=BR1 interface=ether12 pvid=20
add bridge=BR1 interface=ether13 pvid=20
add bridge=BR1 interface=ether14 pvid=20
add bridge=BR1 interface=ether15 pvid=20
add bridge=BR1 interface=ether16 pvid=20

# Red VLAN
add bridge=BR1 interface=ether17 pvid=30
add bridge=BR1 interface=ether18 pvid=30
add bridge=BR1 interface=ether19 pvid=30
add bridge=BR1 interface=ether20 pvid=30
add bridge=BR1 interface=ether21 pvid=30
add bridge=BR1 interface=ether22 pvid=30
add bridge=BR1 interface=ether23 pvid=30
add bridge=BR1 interface=ether24 pvid=30

# egress behavior
/interface bridge vlan

# Blue, Green, Red VLAN
add bridge=BR1 untagged=ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8 vlan-ids=10
add bridge=BR1 untagged=ether9,ether10,ether11,ether12,ether13,ether14,ether15,ether16 vlan-ids=20
add bridge=BR1 untagged=ether17,ether18,ether19,ether20,ether21,ether22,ether23,ether24 vlan-ids=30


#######################################
#
# -- Trunk Ports --
#
#######################################

# ingress behavior
/interface bridge port

# Purple Trunk. Leave pvid set to default of 1
add bridge=BR1 interface=sfp1
add bridge=BR1 interface=sfp2

# egress behavior
/interface bridge vlan

# Purple Trunk. L2 switching only, Bridge not needed as tagged member (except BASE_VLAN)
set bridge=BR1 tagged=sfp1,sfp2 [find vlan-ids=10]
set bridge=BR1 tagged=sfp1,sfp2 [find vlan-ids=20]
set bridge=BR1 tagged=sfp1,sfp2 [find vlan-ids=30]
add bridge=BR1 tagged=BR1,sfp1,sfp2 vlan-ids=99


#######################################
# IP Addressing & Routing
#######################################

# LAN facing Switch's IP address on a BASE_VLAN
/interface vlan add interface=BR1 name=BASE_VLAN vlan-id=99
/ip address add address=192.168.0.2/24 interface=BASE_VLAN

# The Router's IP this switch will use
/ip route add distance=1 gateway=192.168.0.1


#######################################
# IP Services
#######################################
# We have a router that will handle this. Nothing to set here.


#######################################
# VLAN Security
#######################################

# Only allow ingress packets without tags on Access Ports
/interface bridge port
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether1]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether2]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether3]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether4]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether5]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether6]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether7]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether8]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether9]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether10]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether11]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether12]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether13]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether14]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether15]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether16]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether17]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether18]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether19]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether20]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether21]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether22]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether23]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged [find interface=ether24]

# Only allow ingress packets WITH tags on Trunk Ports
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-vlan-tagged [find interface=sfp1]
set bridge=BR1 ingress-filtering=yes frame-types=admit-only-vlan-tagged [find interface=sfp2]


#######################################
# MAC Server settings
#######################################

# Ensure only visibility and availability from BASE_VLAN, the MGMT network
/interface list add name=BASE
/interface list member add interface=BASE_VLAN list=BASE
/ip neighbor discovery-settings set discover-interface-list=BASE
/tool mac-server mac-winbox set allowed-interface-list=BASE
/tool mac-server set allowed-interface-list=BASE


#######################################
# Turn on VLAN mode
#######################################
/interface bridge set BR1 vlan-filtering=yes




File: /anti-dhcp-starvation-attack.rsc
##
## NOTES:
## because port-security cannot be fully implemented in a hotspot interface/port
## due to its dynamic nature, dhcp-starvation could not be truly mitigated but
## slowing it down makes the dhcp-offers expire, freeing previously offered IP addresses
##
## MANIFESTATION:
## <IDENTITY> dhcp-hotspot failed to give out IP address: pool <hs-pool> is empty
##

## 1-packet/second, 2-burst (adjust as necessary)
/interface bridge filter
add action=jump chain=input jump-target=dhcp-filter packet-mark=dhcp-packet packet-type=broadcast \
  comment=dhcp-starvation-attack
add action=return chain=dhcp-filter limit=1,2
add action=drop chain=dhcp-filter

## mark dhcp-request packets
/ip firewall mangle
add action=mark-packet chain=prerouting dst-port=67 in-interface=bridge-hotspot \
	new-packet-mark=dhcp-packet passthrough=yes protocol=udp src-port=68 \
	comment=dhcp-starvation-attack
  


File: /blacklist-bruteforce.rsc
## use the raw filter to conserve CPU cycles
/ip firewall raw
add chain=prerouting src-address-list=_bruteforce_blacklist action=drop comment="Bruteforce Blacklist" disabled=yes

## catch 5 failure attempts every 2-minutes
## move these before the DROP rule of the OUTPUT chain

/ip firewall filter

## (hotspot) LOG: invalid username or password
add chain=output action=accept protocol=tcp content="invalid username or password" dst-limit=2/1m,3,dst-address/2m comment="bruteforce-blacklist" disabled=yes
add chain=output action=add-dst-to-address-list protocol=tcp content="invalid username or password" address-list=_bruteforce_blacklist address-list-timeout=15m disabled=yes



File: /bogons.rsc
## NOTES:
## * these are IP addresses that are private or reserved and should not be coming from the internet
## * this adds the addresses to the address-list "BOGONS", no further actions done
## * TO-DO: create a firewall rule that drops these packets

/ip firewall address-list
add list="BOGONS" address=0.0.0.0/8
add list="BOGONS" address=10.0.0.0/8
add list="BOGONS" address=100.64.0.0/10
add list="BOGONS" address=127.0.0.0/8
add list="BOGONS" address=169.254.0.0/16
add list="BOGONS" address=172.16.0.0/12
add list="BOGONS" address=192.0.0.0/24
add list="BOGONS" address=192.0.2.0/24
add list="BOGONS" address=192.168.0.0/16
add list="BOGONS" address=198.18.0.0/15
add list="BOGONS" address=198.51.100.0/24
add list="BOGONS" address=203.0.113.0/24
add list="BOGONS" address=224.0.0.0/3


File: /dhcp-lease-script.rsc
:local queueName "Hotspot - $leaseActMAC";
:if (($leaseBound=1) && ($leaseActIP>"192.168.11.9")) do {
    /queue simple add name=$queueName target=($leaseActIP . "/32") parent=hotspot max-limit=1M/3M \
    comment=[/ip dhcp-server lease get [find where active-mac-address=$leaseActMAC && active-address=$leaseActIP] host-name];
}
:if (($leaseBound=0) && ($leaseActIP>"192.168.11.9")) do {
    /queue simple remove $queueName
}


File: /firewall-mangle.rsc
/ip firewall mangle
add action=mark-connection chain=prerouting comment=">>>>> INTRANET TRAFFIC" disabled=yes new-connection-mark=no-mark
add action=jump chain=forward dst-address=10.0.0.0/8 jump-target=local-net src-address=10.0.0.0/8
add action=mark-connection chain=local-net new-connection-mark=local-net passthrough=yes
add action=fasttrack-connection chain=local-net connection-mark=local-net add action=accept chain=local-net connection-mark=local-net
add action=return chain=local-net
add action=accept chain=prerouting comment=">>>>> SEPARATOR (DO NOT ENABLE)" disabled=yes
add action=mark-packet chain=prerouting in-interface=all-ethernet new-packet-mark=dnld_pr4_beff
add action=mark-packet chain=postrouting new-packet-mark=upld_pr4_beff out-interface=all-ethernet
add action=accept chain=prerouting comment=">>>>> SEPARATOR (DO NOT ENABLE)" disabled=yes
add action=jump chain=prerouting comment="NEW CONNECTIONS" connection-state=new in-interface=all-ethernet jump-target=crit-dnld-pr1
add action=jump chain=postrouting connection-state=new jump-target=crit-upld-pr1 out-interface=all-ethernet
add action=jump chain=prerouting jump-target=crit-dnld-pr1 port=53 protocol=udp
add action=jump chain=prerouting comment="BIG BYTES (IN)" connection-bytes=2500000-0 \
 connection-rate=2500-1G in-interface=ether1 jump-target=beff-bulk-download protocol=tcp
add action=mark-packet chain=beff-bulk-download new-packet-mark=dnld_pr8_beff passthrough=no
add action=return chain=beff-bulk-download
add action=jump chain=postrouting comment="BIG BYTES (OUT)" connection-bytes=2500000-0 \
 connection-rate=2500-1G jump-target=beff-bulk-upload out-interface=ether1 protocol=tcp
add action=mark-packet chain=beff-bulk-upload new-packet-mark=upld_pr8_beff passthrough=no
add action=return chain=beff-bulk-upload
add action=jump chain=prerouting comment="WEB TRAFFIC - INBOUND" in-interface=ether1 jump-target=beff-http-down port=80,443 protocol=tcp
add action=jump chain=prerouting in-interface=ether1 jump-target=beff-http-down port=80,443 protocol=udp
add action=jump chain=beff-http-down connection-bytes=2500000-0 jump-target=beff-bulk-download protocol=tcp
add action=mark-packet chain=beff-http-down new-packet-mark=dnld_pr6_beff passthrough=no
add action=return chain=beff-http-down
add action=jump chain=prerouting comment="SYN PACKETS" in-interface=ether1 jump-target=crit-dnld-pr2 protocol=tcp tcp-flags=syn
add action=jump chain=postrouting jump-target=crit-upld-pr2 out-interface=ether1 protocol=tcp tcp-flags=syn
add action=jump chain=forward comment="PR1 - RTP conn/packet" jump-target=crit-dnld-pr1 port=10000-20000 protocol=udp
add action=jump chain=forward comment="PR1 -- FACETIME" jump-target=crit-dnld-pr2 port=5223,4080,3478 protocol=tcp
add action=mark-connection chain=forward comment="DSCP 46 (VoIP)" connection-mark=no-mark dscp=46 new-connection-mark=VoIP-conn \
 passthrough=yes
add action=jump chain=prerouting comment="PR2 -- SIP (VoIP)" jump-target=crit-dnld-pr1 port=5060-5061 protocol=tcp
add action=jump chain=prerouting jump-target=crit-dnld-pr1 port=5060-5061 protocol=udp
add action=jump chain=forward comment="PR8 -- P2P conn/packet" jump-target=beff-p2p p2p=all-p2p src-address=10.0.0.0/8
add action=mark-packet chain=beff-p2p new-packet-mark=dnld_pr8_lmtd passthrough=no
add action=return chain=beff-p2p
add action=accept chain=prerouting comment=">>>>> SEPARATOR (DO NOT ENABLE)" disabled=yes
add action=mark-packet chain=crit-dnld-pr1 new-packet-mark=dnld_pr1_crit passthrough=no
add action=return chain=crit-dnld-pr1
add action=mark-packet chain=crit-dnld-pr2 new-packet-mark=dnld_pr2_crit passthrough=no
add action=return chain=crit-dnld-pr2
add action=mark-packet chain=crit-upld-pr1 new-packet-mark=upld_pr1_crit passthrough=no
add action=return chain=crit-upld-pr1
add action=mark-packet chain=crit-upld-pr2 new-packet-mark=upld_pr2_crit passthrough=no
add action=return chain=crit-upld-pr2


File: /initial-config.rsc
# 
# credits: http://www.pimp-my-rig.com/2016/12/initial-configuration-mikrotik-virtual-router.html
# 
# NOTES:
# 1.1.1.2/30 is to be provided by your ISP
#
/ip address 
  add address=1.1.1.2/30 network=1.1.1.0 comment=WAN-PRI interface=ether1

/user 
  # change PASSWORD your own password for the default user: admin
  set admin password=PASSWORD address=127.0.0.1/32

  # change pimp-my-rig with your own custom username
  #   and PASSWORD with your own password
  add name=pimp-my-rig password=PASSWORD group=full address=192.168.0.0/16

# turn off custom services or make them available from the LAN-side only
/ip service
  set telnet address=192.168.0.0/16 disabled=yes
  set ftp address=192.168.0.0/16 disabled=yes
  set www address=192.168.0.0/16 disabled=yes
  set ssh address=192.168.0.0/16
  set www-ssl address=192.168.0.0/16 disabled=yes
  set api address=192.168.0.0/16 disabled=yes
  set winbox address=192.168.0.0/16
  set api-ssl address=192.168.0.0/16 disabled=yes

# secure the router from external access
/ip firewall filter
  add chain=input action=tarpit protocol=tcp in-interface=!ether3 \
   comment="TARPIT connections not coming from LAN (ETH3)"
  add chain=input action=drop in-interface=!ether3 \
   comment="DROP other traffic not comming from LAN (ETH3)"


File: /ip-settings.rsc
;; protect your router against ip-spoofing
;; protect your router against DDoS and SYN flood attacks

/ip settings
set rp-filter=strict tcp-syncookies=yes
set rp-filter=strict


File: /lease-script
## what is this?
## whenever a lease is made, the script runs and logs the "hostname" of the device

## ip dhcp-server lease-script
:if ($leaseBound = "1") do={
	:log info ($leaseServerName . " assigned " . $leaseActIP . " to " . $leaseActMAC . " (" . ([/ip dhcp-server lease get [find active-address=$leaseActIP] host-name]) . ")" )
}


File: /queue-tree.rsc
/queue tree
add comment="----- uploads -----" max-limit=25M name=UPLDQ parent=global priority=1 queue=ethernet-default
add comment="----- best effort -----" limit-at=15M max-limit=25M name=UPLD_BEFF parent=UPLDQ priority=5 queue=ethernet-default
add comment="---- critical -----" limit-at=3M max-limit=25M name= UPLD_CRIT parent=UPLDQ priority=1 queue=ethernet-default
add name=W1UPPR1_CRIT packet-mark=W1UPPR1_CRIT parent=UPLD_CRIT priority=1 queue=ethernet-default
add name=W1UPPR2_CRIT packet-mark=W1UPPR2_CRIT parent=UPLD_CRIT riority=2 queue=ethernet-default
add name=W1UPPR7_CRIT packet-mark=W1UPPR7_CRIT parent=UPLD_CRIT priority=7 queue=ethernet-default
add name=W1UPPR1_BEFF packet-mark=W1UPPR1_BEFF parent=UPLD_BEFF priority=1 queue=ethernet-default
add name=W1UPPR2_BEFF packet-mark=W1UPPR2_BEFF parent=UPLD_BEFF priority=2 queue=ethernet-default
add name=W1UPPR4_BEFF packet-mark=W1UPPR4_BEFF parent=UPLD_BEFF priority=4 queue=ethernet-default
add name=W1UPPR6_BEFF packet-mark=W1UPPR6_BEFF parent=UPLD_BEFF priority=6 queue=ethernet-default
add name=W1UPPR7_BEFF packet-mark=W1UPPR7_BEFF parent=UPLD_BEFF priority=7 queue=ethernet-default
add name=W1UPPR8_BEFF packet-mark=W1UPPR8_BEFF parent=UPLD_BEFF queue=ethernet-default
add max-limit=6M name=W1UPPR8_LMTD packet-mark=W1UPPR8_LMTD parent=UPLD_BEFF queue=ethernet-default
add comment="----- downloads -----" max-limit=25M name=DNLDQ parent=global priority=1 queue=ethernet-default
add comment="----- best effort ----" limit-at=15M max-limit=25M name=DNLD_BEFF parent=DNLDQ priority=5 queue=ethernet-default
add comment="---- critical ----" limit-at=3M max-limit=25M name=DNLD_CRIT parent=DNLDQ priority=1 queue=ethernet-default
add name=W1DNPR1_CRIT packet-mark=W1DNPR1_CRIT parent=DNLD_CRIT priority=1 queue=ethernet-default
add name=W1DNPR2_CRIT packet-mark=W1DNPR2_CRIT parent=DNLD_CRIT priority=2 queue=ethernet-default
add name=W1DNPR7_CRIT packet-mark=W1DNPR7_CRIT parent=DNLD_CRIT priority=7 queue=ethernet-default
add name=W1DNPR1_BEFF packet-mark=W1DNPR1_BEFF parent=DNLD_BEFF priority=1 queue=ethernet-default
add name=W1DNPR2_BEFF packet-mark=W1DNPR2_BEFF parent=DNLD_BEFF priority=2 queue=ethernet-default
add name=W1DNPR4_BEFF packet-mark=W1DNPR4_BEFF parent=DNLD_BEFF priority=4 queue=ethernet-default
add name=W1DNPR6_BEFF packet-mark=W1DNPR6_BEFF parent=DNLD_BEFF priority=6 queue=ethernet-default
add name=W1DNPR7_BEFF packet-mark=W1DNPR7_BEFF parent=DNLD_BEFF priority=7 queue=ethernet-default
add name=W1DNPR8_BEFF packet-mark=W1DNPR8_BEFF parent=DNLD_BEFF queue=ethernet-default
add max-limit=6M name=W1DNPR8_LMTD packet-mark=W1DNPR8_LMTD parent=DNLD_BEFF queue=ethernet-default


File: /README.md
# _Mikrotik QoS_
QoS configuration for Mikrotik Router

## Notes:
These configuration(s) are tested to work on a Virtual Machine (ESXi). It may apply to bare-metal Mikrotik hardware.

More details are [found in my blog](https://www.pimp-my-rig.com/search/label/mikrotik).

### Trainings
* [MikroTik LABs for Beginners](https://bit.ly/2MJgiw1)
* [MikroTik Traffic Control with LABs](https://bit.ly/30NYHJM)
* [MikroTik RouterOS Hardening LABs](https://bit.ly/2WPn2xV)
* [MikroTik Network Associate with LABs](https://bit.ly/3f8vHC9)
* [MikroTik Security Engineer with LABs](https://bit.ly/2ZYjkUF)
* [Starting an ISP with MikroTik](https://bit.ly/2WQDUEo)
* [MikroTik Network Management with LABs](https://bit.ly/2CLh7mE)
* [VLAN on MikroTik with LABs](https://bit.ly/2ZWxZ2w)
* [OSPF on MikroTik with LABs](https://bit.ly/3jDo1ej)



File: /ros-telegram-alert.rsc
:local TOKEN "CHAT-WITH-BOTFATHER:TO-GET-TOKEN";
:local CHATID "YOUR-TELEGRAM-UID";
:local MESSAGE "YOUR-MESSAGE-HERE";

/tool fetch url="https://api.telegram.org/bot$TOKEN/sendMessage\?chat_id=$CHATID&text=$MESSAGE" keep-result=no;


File: /scripts\pihole-disable
:local dnsdnat [/ip firewall nat get value-name=disabled [find comment="pihole"]]
:local adguard [:ping 10.1.1.111 count=3]

:if ( $dnsdnat=false ) do={
  /ip firewall nat set [find comment="pihole"] disabled=yes; 
}


File: /scripts\pihole-enable
:local dnsdnat [/ip firewall nat get value-name=disabled [find comment="pihole"]]
:local adguard [:ping 10.1.1.111 count=2]

:if ( ($dnsdnat=true) and ($adguard = 0) ) do={
  /ip firewall nat set [find comment="pihole"] disabled=no; 
}


File: /scripts\timed-disable-device
:local ADDRS [/ip dhcp-server lease find host-name="DESKTOP-7OD801I"]

foreach ADDR in=$ADDRS do={
  :local ASTR [/ip dhcp-server lease get $ADDR address]
  /ip firewall address-list add list=_blocked-device-list address=$ASTR timeout=30m
  }


File: /ssh-tunnel.md
## _SSH Tunnel to Winbox_

    ssh -L 0.0.0.0:8291:IP.ADDRESS.OF.MIKROTIK:8291 localhost


File: /syslog-trigger\00-vcode.conf
module(load="omprog")

#TEMPLATE
template(
    name="MsgOnly"
    type="string"
    string="%msg:::drop-last-lf%\n"
)

$ActionFileDefaultTemplate MsgOnly

#WHAT-WE-CARE-ABOUT
:msg, contains, "no more sessions" {
    action(
        type="omprog"
        name="Mikrotik"
        binary="/some/path/vcode.bash"
        #confirmMessages="on"
        killUnresponsive="on"
        template="MsgOnly"
        output="/var/tmp/mikrotik.log"
    )
    stop
}


File: /syslog-trigger\vcode.bash
#!/usr/bin/env bash
while read line ; do
    ( cd /path/to/script ; ./vcode.php $line )
    done < "${1:-/dev/stdin}"


File: /syslog-trigger\vcode.php
#!/usr/bin/env php
<?php

require('routeros_api.class.php');

$API = new RouterosAPI();
// $API->debug = true;

// $argv[1] or nothing!
( ! isset($argv[1] )) ? exit("ERROR: No arguments (voucher code) parsed!\n"):
    print_r("[DEBUG] Voucher code is: $argv[1]");

// EXECUTE!
if ($API->connect('10.1.1.1', 'username', 'password')) {

    // RETRIEVE USERS &COOKIES
    $API->write('/ip/hotspot/active/getall');
    $AREAD = $API->read();
    $API->write('/ip/hotspot/cookie/getall');
    $CREAD = $API->read();

    // preg_match('/user (\w+) logged in from.* via api/', $LINE["message"], $match);
    $VCODE = $argv[1];
    foreach ( $AREAD as $ACTIVE => $USER ) {
        #print_r($USER);

        if ( $USER["user"] == $VCODE ) {
            #print_r($USER[".id"]);
            $API->comm("/ip/hotspot/active/remove", array( ".id" => $USER[".id"] ));

            // REMOVE COOKIES!!
            foreach ( $CREAD as $CREAX => $COOKIE ) {
                if ( $COOKIE["user"] == $VCODE ) {
                    $API->comm("/ip/hotspot/cookie/remove", array( ".id" => $COOKIE[".id"] ));
                }
           }
       }
   }

   // WE'RE DONE HERE
   $API->disconnect();

}

?>


