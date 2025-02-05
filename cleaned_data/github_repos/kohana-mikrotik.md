# Repository Information
Name: kohana-mikrotik

# Directory Structure
Directory structure:
└── github_repos/kohana-mikrotik/
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
    │   │       ├── pack-e1423e58c7527bd54011ff9b036c19de5ddcefc4.idx
    │   │       └── pack-e1423e58c7527bd54011ff9b036c19de5ddcefc4.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── classes/
    │   └── mikrotik.php
    ├── config/
    │   └── mikrotik.php
    ├── init.php
    ├── README.md
    └── vendor/
        └── mikrotik/
            ├── mikrotik/
            │   ├── core/
            │   │   ├── mapi_core.php
            │   │   └── mapi_query.php
            │   ├── file/
            │   │   └── mapi_file.php
            │   ├── interface/
            │   │   ├── mapi_interfaces.php
            │   │   ├── mapi_interface_bonding.php
            │   │   ├── mapi_interface_bridge.php
            │   │   ├── mapi_interface_eoip.php
            │   │   ├── mapi_interface_ethernet.php
            │   │   ├── mapi_interface_ipip.php
            │   │   ├── mapi_interface_l2tp_client.php
            │   │   ├── mapi_interface_l2tp_server.php
            │   │   ├── mapi_interface_pppoe_client.php
            │   │   ├── mapi_interface_pppoe_server.php
            │   │   ├── mapi_interface_ppp_client.php
            │   │   ├── mapi_interface_ppp_server.php
            │   │   ├── mapi_interface_pptp_client.php
            │   │   ├── mapi_interface_pptp_server.php
            │   │   ├── mapi_interface_vlan.php
            │   │   └── mapi_interface_vrrp.php
            │   ├── ip/
            │   │   ├── mapi_ip.php
            │   │   ├── mapi_ip_accounting.php
            │   │   ├── mapi_ip_address.php
            │   │   ├── mapi_ip_arp.php
            │   │   ├── mapi_ip_dhcp_client.php
            │   │   ├── mapi_ip_dhcp_relay.php
            │   │   ├── mapi_ip_dhcp_server.php
            │   │   ├── mapi_ip_dns.php
            │   │   ├── mapi_ip_firewall.php
            │   │   ├── mapi_ip_hotspot.php
            │   │   ├── mapi_ip_pool.php
            │   │   ├── mapi_ip_proxy.php
            │   │   ├── mapi_ip_route.php
            │   │   └── mapi_ip_service.php
            │   ├── ppp/
            │   │   ├── mapi_ppp.php
            │   │   ├── mapi_ppp_aaa.php
            │   │   ├── mapi_ppp_active.php
            │   │   ├── mapi_ppp_profile.php
            │   │   └── mapi_ppp_secret.php
            │   └── system/
            │       ├── mapi_system.php
            │       └── mapi_system_scheduler.php
            └── mikrotik_api.php


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
	url = https://github.com/ricardocasares/kohana-mikrotik.git
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
0000000000000000000000000000000000000000 32245ca2c08deb7b9cb9372d18f431c5b3e59d38 vivek-dodia <vivek.dodia@icloud.com> 1738606343 -0500	clone: from https://github.com/ricardocasares/kohana-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 32245ca2c08deb7b9cb9372d18f431c5b3e59d38 vivek-dodia <vivek.dodia@icloud.com> 1738606343 -0500	clone: from https://github.com/ricardocasares/kohana-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 32245ca2c08deb7b9cb9372d18f431c5b3e59d38 vivek-dodia <vivek.dodia@icloud.com> 1738606343 -0500	clone: from https://github.com/ricardocasares/kohana-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
32245ca2c08deb7b9cb9372d18f431c5b3e59d38 refs/remotes/origin/master


File: /.git\refs\heads\master
32245ca2c08deb7b9cb9372d18f431c5b3e59d38


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /classes\mikrotik.php
<?php defined('SYSPATH') or die('No direct script access.');

class Mikrotik extends Mikrotik_Api{
	function __construct()
	{	// Load config file
		$config = Kohana::$config->load('mikrotik');
		$params = $config->get('mikrotik');
		// Initiliaze parent with params
		parent::__construct($params);
	}
}

File: /config\mikrotik.php
<?php defined('SYSPATH') or die('No direct access allowed.');

return array(
	'mikrotik' => array(
		'host'     => '192.168.1.1',
		'port'     => '8728',
		'username' => 'admin',
		'password' => 'password',
		'debug'    => FALSE,
		'attempts' => 5,
		'delay'    => 2,
		'timeout'  => 2
	)
);

File: /init.php
<?php defined('SYSPATH') or die('No direct script access.');

include Kohana::find_file('vendor/mikrotik', 'mikrotik_api');

File: /README.md
kohana-mikrotik
===============

Mikrotik module for Kohana 3.2

This module is a fork from [Mikrotik Api Codeigniter Spark](http://getsparks.org/packages/mikrotik_api/show) with a few tweaks to work with Kohana.

## Installation

Clone the repo to your modules folder
	
    git clone https://github.com/ricardocasares/kohana-mikrotik.git modules/kohana-mikrotik
or manually download and extract to your modules folder

Create a new config/mikrotik.php in your application folder, or edit the one in kohana-mikrotik/config with your mikrotik access details.

Add the module to your application's bootstrap.php file
    
    Kohana::modules(array(
        'kohana-mikrotik' => MODPATH.'kohana-mikrotik'
    ));

## Usage

From your application:

    $mk = new Mikrotik();
    $address = $mk->ip->address->get_all_address();
    var_dump($address);

Will output something like

    Array
    (
        [0] => Array
            (
                [.id] => *2
                [address] => 192.168.1.1/24
                [network] => 192.168.1.0
                [interface] => ether1
                [actual-interface] => ether1
                [invalid] => false
                [dynamic] => false
                [disabled] => false
            )

    )

Make sure the Mikrotik IP Service API is enabled

File: /vendor\mikrotik\mikrotik\core\mapi_core.php
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



File: /vendor\mikrotik\mikrotik\core\mapi_query.php
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

File: /vendor\mikrotik\mikrotik\file\mapi_file.php
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


File: /vendor\mikrotik\mikrotik\interface\mapi_interfaces.php
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



File: /vendor\mikrotik\mikrotik\interface\mapi_interface_bonding.php
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

File: /vendor\mikrotik\mikrotik\interface\mapi_interface_bridge.php
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



File: /vendor\mikrotik\mikrotik\interface\mapi_interface_eoip.php
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


File: /vendor\mikrotik\mikrotik\interface\mapi_interface_ethernet.php
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


File: /vendor\mikrotik\mikrotik\interface\mapi_interface_ipip.php
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

File: /vendor\mikrotik\mikrotik\interface\mapi_interface_l2tp_client.php
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



File: /vendor\mikrotik\mikrotik\interface\mapi_interface_l2tp_server.php
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




File: /vendor\mikrotik\mikrotik\interface\mapi_interface_pppoe_client.php
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




File: /vendor\mikrotik\mikrotik\interface\mapi_interface_pppoe_server.php
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



File: /vendor\mikrotik\mikrotik\interface\mapi_interface_ppp_client.php
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



File: /vendor\mikrotik\mikrotik\interface\mapi_interface_ppp_server.php
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


File: /vendor\mikrotik\mikrotik\interface\mapi_interface_pptp_client.php
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




File: /vendor\mikrotik\mikrotik\interface\mapi_interface_pptp_server.php
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


File: /vendor\mikrotik\mikrotik\interface\mapi_interface_vlan.php
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



File: /vendor\mikrotik\mikrotik\interface\mapi_interface_vrrp.php
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

File: /vendor\mikrotik\mikrotik\ip\mapi_ip.php
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



File: /vendor\mikrotik\mikrotik\ip\mapi_ip_accounting.php
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



File: /vendor\mikrotik\mikrotik\ip\mapi_ip_address.php
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


File: /vendor\mikrotik\mikrotik\ip\mapi_ip_arp.php
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


File: /vendor\mikrotik\mikrotik\ip\mapi_ip_dhcp_client.php
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



File: /vendor\mikrotik\mikrotik\ip\mapi_ip_dhcp_relay.php
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


File: /vendor\mikrotik\mikrotik\ip\mapi_ip_dhcp_server.php
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


File: /vendor\mikrotik\mikrotik\ip\mapi_ip_dns.php
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


File: /vendor\mikrotik\mikrotik\ip\mapi_ip_firewall.php
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




File: /vendor\mikrotik\mikrotik\ip\mapi_ip_hotspot.php
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


File: /vendor\mikrotik\mikrotik\ip\mapi_ip_pool.php
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



File: /vendor\mikrotik\mikrotik\ip\mapi_ip_proxy.php
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


File: /vendor\mikrotik\mikrotik\ip\mapi_ip_route.php
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



File: /vendor\mikrotik\mikrotik\ip\mapi_ip_service.php
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



File: /vendor\mikrotik\mikrotik\ppp\mapi_ppp.php
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

File: /vendor\mikrotik\mikrotik\ppp\mapi_ppp_aaa.php
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


File: /vendor\mikrotik\mikrotik\ppp\mapi_ppp_active.php
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


File: /vendor\mikrotik\mikrotik\ppp\mapi_ppp_profile.php
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



File: /vendor\mikrotik\mikrotik\ppp\mapi_ppp_secret.php
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



File: /vendor\mikrotik\mikrotik\system\mapi_system.php
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


File: /vendor\mikrotik\mikrotik\system\mapi_system_scheduler.php
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


File: /vendor\mikrotik\mikrotik_api.php
<?php

//load parent class
require 'mikrotik/core/mapi_core.php';
require 'mikrotik/core/mapi_query.php';

//load child class interface
require 'mikrotik/interface/mapi_interface_ethernet.php';
require 'mikrotik/interface/mapi_interface_pppoe_client.php';
require 'mikrotik/interface/mapi_interface_pppoe_server.php';
require 'mikrotik/interface/mapi_interface_eoip.php';
require 'mikrotik/interface/mapi_interface_ipip.php';
require 'mikrotik/interface/mapi_interface_vlan.php';
require 'mikrotik/interface/mapi_interface_vrrp.php';
require 'mikrotik/interface/mapi_interface_bonding.php';
require 'mikrotik/interface/mapi_interface_bridge.php';
require 'mikrotik/interface/mapi_interface_l2tp_client.php';
require 'mikrotik/interface/mapi_interface_l2tp_server.php';
require 'mikrotik/interface/mapi_interface_ppp_client.php';
require 'mikrotik/interface/mapi_interface_ppp_server.php';
require 'mikrotik/interface/mapi_interface_pptp_client.php';
require 'mikrotik/interface/mapi_interface_pptp_server.php';
require 'mikrotik/interface/mapi_interfaces.php';

//load child class ip
require 'mikrotik/ip/mapi_ip.php';
require 'mikrotik/ip/mapi_ip_dhcp_client.php';
require 'mikrotik/ip/mapi_ip_dhcp_relay.php';
require 'mikrotik/ip/mapi_ip_dhcp_server.php';
require 'mikrotik/ip/mapi_ip_route.php';
require 'mikrotik/ip/mapi_ip_service.php';
require 'mikrotik/ip/mapi_ip_address.php';
require 'mikrotik/ip/mapi_ip_hotspot.php';
require 'mikrotik/ip/mapi_ip_dns.php';
require 'mikrotik/ip/mapi_ip_accounting.php';
require 'mikrotik/ip/mapi_ip_arp.php';
require 'mikrotik/ip/mapi_ip_pool.php';
require 'mikrotik/ip/mapi_ip_firewall.php';
require 'mikrotik/ip/mapi_ip_proxy.php';

//load child class ppp
require 'mikrotik/ppp/mapi_ppp.php';
require 'mikrotik/ppp/mapi_ppp_profile.php';
require 'mikrotik/ppp/mapi_ppp_secret.php';
require 'mikrotik/ppp/mapi_ppp_aaa.php';
require 'mikrotik/ppp/mapi_ppp_active.php';

//load child class system
require 'mikrotik/system/mapi_system.php';
require 'mikrotik/system/mapi_system_scheduler.php';

//load child class file
require 'mikrotik/file/mapi_file.php';

/**
 * Description of Mikrotik_Api
 * @author      Virtual Think Team vthinkteam@gmail.com <http://vthink.web.id>
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @author      Krisna Pranata krisna.pranata@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Mikrotik_Api {

    /**
     * Instantiation of Class Mikrotik_Api
     * @access private
     * @var type array
     */
    private $param;
    
    function __construct($param=array()) {
        $this->param = $param;
    }
    
    /**
     * This method for call class Mapi IP
     * @access public
     * @return Object of Mapi_Ip 
     */
    public function ip(){
        return new Mapi_Ip($this->param);
    }
    
    /**
     * This method for call class Mapi Interface
     * @access public
     * @return Object of Mapi_Interface 
     */
    public function interfaces(){
        return new Mapi_Interfaces($this->param); 
    }
    
    /**
     * This method for call class Mapi Ppp
     * @access public
     * @return Object of Mapi_Ppp
     */
    public function ppp(){
        return new Mapi_Ppp($this->param);
    }
    
    /**
     * This method for call class Mapi_System
     * @access public
     * @return Mapi_System 
     */
    public function system(){
        return new Mapi_System($this->param);
    }
    
    /**
     * This method for call class Mapi_File
     * @access public
     * @return Mapi_File 
     */
    public function file(){
        return new Mapi_File($this->param);
    }
    
    /**
     * This metod used call class Mapi_System_Scheduler 
     * @return Mapi_System_Scheduler
     */
    public function system_scheduler(){
        return new Mapi_System_Scheduler($this->param);
    }
}



