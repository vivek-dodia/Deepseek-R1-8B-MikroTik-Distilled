# Repository Information
Name: Scripts-MikroTik

# Directory Structure
Directory structure:
└── github_repos/Scripts-MikroTik/
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
    │   │       │   └── main
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-cdf5994a46499b0eca4d977881fec9d131037434.idx
    │   │       └── pack-cdf5994a46499b0eca4d977881fec9d131037434.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── Check LOCAL_IP_GATEWAY_WIREGUARD_HEADQUARTER Through Tunnel on MikroTik Router.txt
    ├── How to Install Wireguard VPN Server on Ubuntu Server 22.04.2.txt
    ├── Mikrotik RouterOS Cloudflare Dynamic DNS Script and API Command for List Cloudflare Record ID.txt
    ├── OpenVPN Config File.ovpn
    ├── PCC Load Balancing (2 WAN PPPoE) + VLAN + FailOver Netwatch.rsc
    ├── PCC Load Balancing (2 WAN PPPoE).txt
    ├── PCC Load Balancing (DHCP 2 WAN).txt
    ├── README.md
    ├── Securing Your MikroTik Router.txt
    ├── WAN Monitoring with VPN via LINE Notify.txt
    ├── [Cloudflare] Configuring DoH Server on MikroTik RouterOS 7.8 (with certificates).txt
    ├── [Script -MikroTik] 2 PPPoE WAN Connection and Failover using Netwatch Tool and Scripts.txt
    ├── [Script-MikroTik] 1 DHCP Client WAN Connection (Dynamic IP from ISP) + Auto Fail Over + Recursive Routing.txt
    ├── [Script-MikroTik] 2 PPPoE WAN Connection (Dynamic IP from ISP) + Auto Fail Over + Recursive Routing (RouterOS7).txt
    ├── [Script-MikroTik] 2 PPPoE WAN Connection (Dynamic IP from ISP) + Auto Fail Over + Recursive Routing.txt
    ├── [Script-MikroTik] Accept Important ICMP Types.txt
    ├── [Script-MikroTik] Block Bogon IP Addresses on MikroTik Firewall.txt
    ├── [Script-MikroTik] Blocking Facebook on RouterOS using Address-Lists.txt
    ├── [Script-MikroTik] Blocking Facebook on RouterOS using TLS Host.txt
    ├── [Script-MikroTik] Blocking LINE on RouterOS using Address-Lists.txt
    ├── [Script-MikroTik] Blocking Netflix traffic using RouterOS.txt
    ├── [Script-MikroTik] Blocking PUBG Mobile traffic using RouterOS.txt
    ├── [Script-MikroTik] Blocking RoV mobile traffic using RouterOS.txt
    ├── [Script-MikroTik] Blocking Steam on RouterOS using Address-Lists.txt
    ├── [Script-MikroTik] Blocking TikTok using RouterOS.txt
    ├── [Script-MikroTik] Blocking Twitter on RouterOS using Address-Lists.txt
    ├── [Script-MikroTik] Blocking Youtube on RouterOS using TLS Host.txt
    ├── [Script-MikroTik] Drop Port Scan Attacks using MikroTik Firewall.txt
    ├── [Script-MikroTik] Dynamic IP problem with manual created routes (DHCP-Client).txt
    ├── [Script-MikroTik] Hairpin NAT.txt
    ├── [Script-MikroTik] NO-IP.COM DDNS Update.txt
    ├── [Script-MikroTik] Port Knocking Security.txt
    ├── [Script-MikroTik] Preventing Brute Force Attack.txt
    ├── [Script-MikroTik] Preventing ICMP Smurf Attack.txt
    ├── [Script-MikroTik] Preventing Port Scanner.txt
    ├── [Script-MikroTik] Preventing TCP SYN Attack.txt
    ├── [Script-MikroTik] Preventing UDP Flood Attack.txt
    ├── [Script-MikroTik] Setting the Bandwidth Priority in the  Microsoft Teams Application on MikroTik RouterOS.txt
    └── [Script-MikroTik] Setting the Bandwidth Priority in the Zoom Video Conferencing Application on MikroTik RouterOS.txt


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
	url = https://github.com/misterkrittin/Scripts-MikroTik.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main


File: /.git\description
Unnamed repository; edit this file 'description' to name the repository.


File: /.git\HEAD
ref: refs/heads/main


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
0000000000000000000000000000000000000000 21e22da78add7710a3f49146306c25f308dd622a vivek-dodia <vivek.dodia@icloud.com> 1738605787 -0500	clone: from https://github.com/misterkrittin/Scripts-MikroTik.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 21e22da78add7710a3f49146306c25f308dd622a vivek-dodia <vivek.dodia@icloud.com> 1738605787 -0500	clone: from https://github.com/misterkrittin/Scripts-MikroTik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 21e22da78add7710a3f49146306c25f308dd622a vivek-dodia <vivek.dodia@icloud.com> 1738605787 -0500	clone: from https://github.com/misterkrittin/Scripts-MikroTik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
21e22da78add7710a3f49146306c25f308dd622a refs/remotes/origin/main


File: /.git\refs\heads\main
21e22da78add7710a3f49146306c25f308dd622a


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /Check LOCAL_IP_GATEWAY_WIREGUARD_HEADQUARTER Through Tunnel on MikroTik Router.txt
1. System > Scripts
Press "+"
Name: ToggleWGPeer
Policy: ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
Source:
-------------------------------------------------------

:local wgcheckip LOCAL_IP_GATEWAY_WIREGUARD_HEADQUARTER
:local endpointip xxxyyy.sn.mynetname.net
#:log info "wg check-ip $wgcheckip "
:if ([/ping $wgcheckip interval=1 count=5] =0) do={
  :log info "WG down $wgcheckip"
  /interface/wireguard/peers/disable [find endpoint-address=$endpointip];
  :delay 60
  /interface/wireguard/peers/enable [find endpoint-address=$endpointip];
  :log info "WG up again $wgcheckip"
}

-------------------------------------------------------

2. System > Scheduler
Press "+"
Name: ScheduleWGToggle
Start Time: startup
Interval: 00:02:00 (Run this as a scheduled script perhaps every 2 minutes)
Policy: ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
On Event: /system script run ToggleWGPeer

File: /How to Install Wireguard VPN Server on Ubuntu Server 22.04.2.txt
[How to Install Wireguard VPN Server on Ubuntu Server 22.04.2]

Server configuration

(1) -- Installing WireGuard --

sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install wireguard

(2) -- IP forwarding --

sudo nano /etc/sysctl.conf (Delete # symbol on line "net.ipv4.ip_forward=1")
sudo sysctl -p

(3) -- Configuring firewall rules --
sudo apt install ufw
sudo ufw allow ssh
sudo ufw allow 51820/udp
sudo ufw enable
sudo ufw status

(4) -- Generating private and public keys --

cd /etc/wireguard
ls
umask 077
wg genkey | tee privatekey | wg pubkey > publickey
sudo cat /etc/wireguard/publickey
sudo cat /etc/wireguard/privatekey
* Copy publickey and privatekry into Notepad *

(5) -- Generating server config --
sudo nano /etc/wireguard/wg0

######################################################
[Interface]
PrivateKey = <contents-of-server-privatekey>
Address = 10.0.0.1/24
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o ens33 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o ens33 -j MASQUERADE
ListenPort = 51820

[Peer]
PublicKey = <contents-of-client-publickey>
AllowedIPs = 10.0.0.2/32
######################################################

(6) -- Start Wireguard --
wg-quick up wg0

(7) -- Check Wireguard Config --
wg show

(8) -- Enable Automatic Start --
systemctl enable wg-quick@wg0

(9) -- Update Server --
sudo apt-get update && sudo apt-get upgrade -y


Client configuration

For Windows

(1) Download Wireguard Client: https://www.wireguard.com/install/
(2) Click "Add empty tunnel..."

######################################################
[Interface]
Address = 10.0.0.2/32
PrivateKey = <contents-of-client-privatekey>
DNS = 1.1.1.1

[Peer]
PublicKey = <contents-of-server-publickey>
Endpoint = <server-public-ip>:51820
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 10
######################################################

File: /Mikrotik RouterOS Cloudflare Dynamic DNS Script and API Command for List Cloudflare Record ID.txt
# Cloudflare Dynamic DNS update script
# Required policy: read, write, test, policy
# Add this script to scheduler
# Install DigiCert root CA or disable check-certificate
# Configuration ---------------------------------------------------------------------

:local TOKEN "__APITOKEN__"
:local ZONEID "__ZONEIDENTIFIER__"
:local RECORDID "__RECORDIDENTIFIER__"
:local RECORDNAME "__DNSRECORD__"
:local WANIF "__WANINTERFACE__"

#------------------------------------------------------------------------------------

:global IP4NEW
:global IP4CUR

:local url "https://api.cloudflare.com/client/v4/zones/$ZONEID/dns_records/$RECORDID/"

:if ([/interface get $WANIF value-name=running]) do={
# Get the current public IP
    :local requestip [tool fetch url="https://ipv4.icanhazip.com" mode=https check-certificate=no output=user as-value]
    :set IP4NEW [:pick ($requestip->"data") 0 ([:len ($requestip->"data")]-1)]
# Check if IP has changed
    :if ($IP4NEW != $IP4CUR) do={
        :log info "CF-DDNS: Public IP changed to $IP4NEW, updating"
        :local cfapi [/tool fetch http-method=put mode=https url=$url check-certificate=no output=user as-value \
            http-header-field="Authorization: Bearer $TOKEN,Content-Type: application/json" \
            http-data="{\"type\":\"A\",\"name\":\"$RECORDNAME\",\"content\":\"$IP4NEW\",\"ttl\":120,\"proxied\":false}"]
        :set IP4CUR $IP4NEW
        :log info "CF-DDNS: Host $RECORDNAME updated with IP $IP4CUR"
    }  else={
        :log info "CF-DDNS: Previous IP $IP4NEW not changed, quitting"
    }
} else={
    :log info "CF-DDNS: $WANIF is not currently running, quitting"
}


* [API Command for List Cloudflare Record ID] *

curl -X GET "https://api.cloudflare.com/client/v4/zones/ZONE_ID/dns_records?name=SUB_DOMAIN" \
     -H "X-Auth-Email: user@example.com" \
     -H "X-Auth-Key: YOUR_API_KEY" \
     -H "Content-Type: application/json"

File: /OpenVPN Config File.ovpn
client
dev tun
proto tcp
remote example.com 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
cipher AES-256-CBC
auth SHA1
auth-user-pass
auth-nocache
route destination_network subnet_mask
verb 3
<ca>
-----BEGIN CERTIFICATE-----
*** Paste CA Cert Text Here ***
-----END CERTIFICATE-----

</ca>
<cert>
-----BEGIN CERTIFICATE-----
*** Paste Your client.crt Text Here ***
-----END CERTIFICATE-----

</cert>
<key>
-----BEGIN RSA PRIVATE KEY-----
*** Paste your client.key Here ***
-----END RSA PRIVATE KEY-----

</key>


File: /PCC Load Balancing (2 WAN PPPoE) + VLAN + FailOver Netwatch.rsc
# jul/22/2023 13:22:28 by RouterOS 7.9.2
# software id = 
#
/interface bridge
add name=Bridge-VLAN-TRUNKs
/interface pppoe-client
add disabled=no interface=ether1 name=pppoe-out1 user=ppp1
add disabled=no interface=ether2 name=pppoe-out2 user=ppp2
/interface vlan
add interface=Bridge-VLAN-TRUNKs name=vlan10 vlan-id=10
add interface=Bridge-VLAN-TRUNKs name=vlan20 vlan-id=20
/disk
set slot1 slot=slot1 type=hardware
/interface list
add name=Bridge-LAN
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=dhcp_pool0 ranges=192.168.88.2-192.168.88.254
add name=dhcp_pool1 ranges=10.10.10.2-10.10.10.254
add name=dhcp_pool2 ranges=10.20.20.2-10.20.20.254
/ip dhcp-server
add address-pool=dhcp_pool0 interface=Bridge-VLAN-TRUNKs lease-time=1d name=\
    dhcp1
add address-pool=dhcp_pool1 interface=vlan10 lease-time=1d name=dhcp2
add address-pool=dhcp_pool2 interface=vlan20 lease-time=1d name=dhcp3
/port
set 0 name=serial0
/routing table
add disabled=no fib name=via-ISP1
add disabled=no fib name=via-ISP2
/interface bridge port
add bridge=Bridge-VLAN-TRUNKs interface=ether5
/interface list member
add interface=Bridge-VLAN-TRUNKs list=Bridge-LAN
add interface=vlan10 list=Bridge-LAN
add interface=vlan20 list=Bridge-LAN
/ip address
add address=192.168.88.1/24 interface=Bridge-VLAN-TRUNKs network=192.168.88.0
add address=10.10.10.1/24 interface=vlan10 network=10.10.10.0
add address=10.20.20.1/24 interface=vlan20 network=10.20.20.0
/ip dhcp-server network
add address=10.10.10.0/24 dns-server=10.10.10.1 gateway=10.10.10.1
add address=10.20.20.0/24 dns-server=10.20.20.1 gateway=10.20.20.1
add address=192.168.88.0/24 dns-server=192.168.88.1 gateway=192.168.88.1
/ip dns
set allow-remote-requests=yes servers=1.1.1.1,1.0.0.1
/ip firewall address-list
add address=192.168.88.0/24 list=LAN
add address=10.10.10.0/24 list=LAN
add address=10.20.20.0/24 list=LAN
/ip firewall mangle
add action=accept chain=prerouting in-interface=pppoe-out1
add action=accept chain=prerouting in-interface=pppoe-out2
add action=accept chain=prerouting dst-address-list=LAN
add action=mark-connection chain=prerouting in-interface-list=Bridge-LAN \
    new-connection-mark=ISP1_Conn passthrough=yes per-connection-classifier=\
    both-addresses:2/0
add action=mark-routing chain=prerouting connection-mark=ISP1_Conn \
    in-interface-list=Bridge-LAN new-routing-mark=via-ISP1 passthrough=no
add action=mark-connection chain=prerouting in-interface-list=Bridge-LAN \
    new-connection-mark=ISP2_Conn passthrough=yes per-connection-classifier=\
    both-addresses:2/1
add action=mark-routing chain=prerouting connection-mark=ISP2_Conn \
    in-interface-list=Bridge-LAN new-routing-mark=via-ISP2 passthrough=no
add action=mark-connection chain=prerouting in-interface=pppoe-out1 \
    new-connection-mark=ISP1_Conn passthrough=yes
add action=mark-routing chain=output connection-mark=ISP1_Conn \
    new-routing-mark=via-ISP1 passthrough=no
add action=mark-connection chain=prerouting in-interface=pppoe-out2 \
    new-connection-mark=ISP2_Conn passthrough=yes
add action=mark-routing chain=output connection-mark=ISP2_Conn \
    new-routing-mark=via-ISP2 passthrough=no
/ip firewall nat
add action=masquerade chain=srcnat out-interface=pppoe-out1
add action=masquerade chain=srcnat out-interface=pppoe-out2
/ip route
add comment=via-ISP1_To_ISP1 disabled=no distance=1 dst-address=0.0.0.0/0 \
    gateway=pppoe-out1 pref-src="" routing-table=via-ISP1 scope=30 \
    suppress-hw-offload=no target-scope=10
add comment=via-ISP2_To_ISP2 disabled=no distance=1 dst-address=0.0.0.0/0 \
    gateway=pppoe-out2 pref-src="" routing-table=via-ISP2 scope=30 \
    suppress-hw-offload=no target-scope=10
add comment="Redirect via-ISP1 To ISP2" disabled=no distance=2 dst-address=\
    0.0.0.0/0 gateway=pppoe-out2 pref-src="" routing-table=via-ISP1 scope=30 \
    suppress-hw-offload=no target-scope=10
add comment="Redirect via-ISP2 To ISP1" disabled=no distance=2 dst-address=\
    0.0.0.0/0 gateway=pppoe-out1 pref-src="" routing-table=via-ISP2 scope=30 \
    suppress-hw-offload=no target-scope=10
add comment=To-ISP1 disabled=no distance=1 dst-address=0.0.0.0/0 gateway=\
    pppoe-out1 pref-src="" routing-table=main scope=30 suppress-hw-offload=no \
    target-scope=10
add comment=To-ISP2 disabled=no distance=2 dst-address=0.0.0.0/0 gateway=\
    pppoe-out2 pref-src="" routing-table=main scope=30 suppress-hw-offload=no \
    target-scope=10
add comment="Netwatch ISP1 (Quad9 DNS)" disabled=no distance=1 dst-address=\
    9.9.9.9/32 gateway=pppoe-out1 pref-src="" routing-table=main scope=30 \
    suppress-hw-offload=no target-scope=10
add comment="Netwatch ISP2 (Google DNS)" disabled=no distance=1 dst-address=\
    8.8.8.8/32 gateway=pppoe-out2 pref-src="" routing-table=main scope=30 \
    suppress-hw-offload=no target-scope=10
/system identity
set name=R1
/system note
set show-at-login=no
/tool netwatch
add comment=ISP1 disabled=no down-script="ip route disable [find comment=To-IS\
    P1]\r\
    \nip route disable [find comment=via-ISP1_To_ISP1]\r\
    \n:log warning \"ISP1 is down\"\r\
    \n/ip firewall connection remove [find]" host=9.9.9.9 http-codes="" \
    interval=10s test-script="" timeout=800ms type=simple up-script="ip route \
    enable [find comment=To-ISP1]\r\
    \nip route enable [find comment=via-ISP1_To_ISP1]\r\
    \n:log warning \"ISP1 is up\""
add comment=ISP2 disabled=no down-script="ip route disable [find comment=To-IS\
    P2]\r\
    \nip route disable [find comment=via-ISP2_To_ISP2]\r\
    \n:log warning \"ISP1 is down\"\r\
    \n/ip firewall connection remove [find]" host=8.8.8.8 http-codes="" \
    interval=10s test-script="" timeout=800ms type=simple up-script="ip route \
    enable [find comment=To-ISP2]\r\
    \nip route enable [find comment=via-ISP2_To_ISP2]\r\
    \n:log warning \"ISP2 is up\""


File: /PCC Load Balancing (2 WAN PPPoE).txt
PCC Load Balancing (2 WAN PPPoE)
ISP1 - Download Speed: 1000 Mbps, Upload Speed: 500 Mbps
ISP2 - Download Speed: 1000 Mbps, Upload Speed: 500 Mbps

VLAN10 (10.10.10.0/24) 
VLAN20 (10.20.20.0/24) 

# 1. ALL LAN Address Lists
/ip firewall address-list
add address=10.10.10.0/24 list=LAN
add address=10.20.20.0/24 list=LAN

# 2. Create Route tables
  2.1. Routing > Tables
    For via-ISP1,
     - Press "+"
     - Name: via-ISP1
     - FIB: Check
     - Press "OK"
  2.2 Routing > Tables
    For via-ISP1,
     - Press "+"
     - Name: via-ISP1
     - FIB: Check
     - Press "OK"

# 3. Script PCC Load Balancing (2 WAN PPPoE)

/ip firewall mangle
add action=mark-routing chain=prerouting dst-address-list=!LAN new-routing-mark=via-ISP1 passthrough=yes per-connection-classifier=both-addresses-and-ports:2/0 src-address-list=LAN
add action=mark-routing chain=prerouting dst-address-list=!LAN new-routing-mark=via-ISP2 passthrough=yes per-connection-classifier=both-addresses-and-ports:2/1 src-address-list=LAN

OR

/ip firewall mangle
add action=mark-routing chain=prerouting dst-address-type=!local new-routing-mark=via-ISP1 passthrough=yes per-connection-classifier=both-addresses-and-ports:2/0 src-address-list=LAN
add action=mark-routing chain=prerouting dst-address-type=!local new-routing-mark=via-ISP2 passthrough=yes per-connection-classifier=both-addresses-and-ports:2/1 src-address-list=LAN

# 4. Create 2 routes to ISP1 and ISP2 with the mark routing that you have just created

File: /PCC Load Balancing (DHCP 2 WAN).txt
###########################################################################
# PCC Load Balancing (DHCP 2 WAN)
# This script is suitable for the same internet speed of both ISPs such as 
# ISP1 -> Download Speed: 300 Mbps, Upload Speed: 200 Mbps
# ISP2 -> Download Speed: 300 Mbps, Upload Speed: 200 Mbps
###########################################################################

# Model: hAP ac², RouterOS 7.3.1 (Stable)

# Ether1 -> Connect To ISP1 using DHCP-Client medthod (ISP GW: 192.168.12.1)
# Ether2 -> Connect To ISP2 using DHCP-Client medthod (ISP GW: 192.168.21.1)
# Ether3 - Ether5 -> Give IP Address to PC-Client 172.16.0.0/24

# 1. Create Bridge and assign ports to the bridge
/interface bridge
add name=Bridge-ALL-PORTs

/interface bridge port
add bridge=Bridge-ALL-PORTs interface=ether4
add bridge=Bridge-ALL-PORTs interface=ether3
add bridge=Bridge-ALL-PORTs interface=ether5
#############################################

# 2. Assign IP Gateway to Interface
# IP > Addresses > Press "+"
# Address: 172.16.0.1/24
# network: 172.16.0.0
# Interface: Bridge-ALL-PORTs
#############################################

# 3. Assign DNS Server to MikroTik Router
# IP > DNS
# 1.1.1.1, 1.0.0.1
# Make sure to uncheck "Allow remote request"
# Press "Apply" and "OK"
#############################################

# 4. Connected To ISP
# IP > DHCP-Client
# For Connect To ISP1,
#  Press "+"
#  Interface: ether1
#  Uncheck "Use peer DNS"
#  Uncheck "Use peer NTP"
#  Add Default Route: no
#
# For Connect to ISP2,
#  Press "+"
#  Interface: ether2
#  Uncheck "Use peer DNS"
#  Uncheck "Use peer NTP"
#  Add Default Route: no
#############################################

# 5. Create DHCP Server to Bridge
# IP > DHCP Server > Press "DHCP Setup"
# DHCP Server Interface: Bridge-ALL-PORTs 
# And press the next button until finished
#############################################

# 6. Make NAT
# IP > Firewall > NAT
# For make NAT ISP1,
#  Press "+"
#  Chain: srcnat
#  Src. Address: 172.16.0.0/24
#  Out. Interface: ether1
#  Action: masquerade
#
# For make NAT ISP2,
#  Press "+"
#  Chain: srcnat
#  Src. Address: 172.16.0.0/24
#  Out. Interface: ether2
#  Action: masquerade
#############################################

# 7. Create Tables Routing
# Routing > Tables
# For table routing ISP1
#  Press "+"
#  Name: via-ISP1
#  Make sure to check "FIB"
#  Press "OK"
#
# For table routing ISP2
#  Press "+"
#  Name: via-ISP2
#  Make sure to check "FIB"
#  Press "OK"
#############################################

# 8. Script PCC Load Balancing

/ip firewall mangle
add action=accept chain=prerouting dst-address=192.168.12.0/24
add action=accept chain=prerouting dst-address=192.168.21.0/24
add action=accept chain=prerouting dst-address=172.16.0.0/24
add action=mark-connection chain=prerouting in-interface=Bridge-ALL-PORTs new-connection-mark=ISP1-Conn passthrough=yes per-connection-classifier=both-addresses:2/0
add action=mark-connection chain=prerouting in-interface=Bridge-ALL-PORTs new-connection-mark=ISP2-Conn passthrough=yes per-connection-classifier=both-addresses:2/1
add action=mark-routing chain=prerouting connection-mark=ISP1-Conn in-interface=Bridge-ALL-PORTs new-routing-mark=via-ISP1 passthrough=no
add action=mark-routing chain=prerouting connection-mark=ISP2-Conn in-interface=Bridge-ALL-PORTs new-routing-mark=via-ISP2 passthrough=no
add action=mark-connection chain=prerouting in-interface=ether1 new-connection-mark=ISP1-Conn passthrough=yes
add action=mark-connection chain=prerouting in-interface=ether2 new-connection-mark=ISP2-Conn passthrough=yes
add action=mark-routing chain=output connection-mark=ISP1-Conn new-routing-mark=via-ISP1 passthrough=no
add action=mark-routing chain=output connection-mark=ISP2-Conn new-routing-mark=via-ISP2 passthrough=no

#############################################

# 9. Create 2 routes to ISP1 and ISP2 with the mark routing that you have just created

/ip route
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=192.168.12.1 pref-src="" routing-table=via-ISP1 scope=30 suppress-hw-offload=no target-scope=10
add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=192.168.21.1 pref-src="" routing-table=via-ISP2 scope=30 suppress-hw-offload=no target-scope=10

#############################################

# 10. For failover, create a route to ISP1 with the mark via-ISP2 and give it a distance of 2

/ip route
add disabled=no distance=2 dst-address=0.0.0.0/0 gateway=192.168.12.1 pref-src="" routing-table=via-ISP2 scope=30 suppress-hw-offload=no target-scope=10

#############################################

# 11. For failover, create a route to ISP2 with the mark via-ISP1 and give it a distance of 2

/ip route
add disabled=no distance=2 dst-address=0.0.0.0/0 gateway=192.168.21.1 pref-src="" routing-table=via-ISP1 scope=30 suppress-hw-offload=no target-scope=10

#############################################

# 12. Set NTP-Client to MikroTik Router
# System > NTP Client > check Enabled
# NTP Servers: Input IP Address of NTP Server (Up to you choose)
#############################################

File: /README.md
# 🧑‍Introduce myself
Hello everyone. My name is Krittin Srithong with a short experience in the IT sector. I studied bachelor in Computer Enginnering from Thailand. You can visit my <a href="https://medium.com/techblogclub">Web blogs</a> as well as my <a href="https://github.com/misterkrittin/Scripts-MikroTik">GitHub</a>. I work as a freelance about communication network and I hold the following certificates: MTCNA, MTCUME, and MTCSE. Finally, I hope you will enjoy using my scripts.

# ☎ Contact for work (In Thailand Only)
✉ swd.xpong@gmail.com

# 💰 Donation
If this project help you reduce time to develop, you can give me a cup of coffee :)
<p align="center">
  <h2>Donate via Paypal (เพย์พาว)</h2>
  <a href="https://www.paypal.com/paypalme/misterkrittin"><img width="256" height="256" src="https://www.julianmills.co.uk/wp-content/uploads/2021/02/icon-256x256-1.png"></a>
</p>
<p align="center">
  <h2>Donate via QR Code PromptPay (พร้อมเพย์)</h2>
  <img src="https://promptpay.io/0836598795.png">
</p>


File: /Securing Your MikroTik Router.txt
- Access to a router
  Change default username admin to different name, custom name helps to protect access to your rotuer, if anybody got direct access to your router.
   /user add name=**myname** password=**mypassword** group=full
   /user remove admin
   
  Change password
   /password

- Access by IP address
  Besides the fact that default firewall protects your router from unauthorized access from outer networks, it is possible to restrict username access for the specific IP address
   /user set 0 allowed-address=x.x.x.x/yy
    x.x.x.x/yy - your IP or network subnet that is allowed to access your router.

- Disable services on RouterOS
  /ip service disable telnet,ftp,www,www-ssl,api,api-ssl
  /ip service print 

- Changing the Default SSH Port
  /ip service set ssh port=2200
  /ip service print

- Restrict access by IP Address
  /ip service set winbox address=192.168.50.0/24
  /ip service set ssh address=192.168.50.0/24

- RouterOS MAC-access
  MAC-Telnet
  Disable mac-telnet services,
   /tool mac-server set allowed-interface-list=none
   /tool mac-server print

  MAC-Winbox
  Disable mac-winbox services,
   /tool mac-server mac-winbox set allowed-interface-list=none
   /tool mac-server mac-winbox print

  MAC-Ping
  Disable mac-ping service,
   /tool mac-server ping set enabled=no
   /tool mac-server ping print

- Bandwidth Test
  /tool bandwidth-server set enabled=no

- DNS cache
  /ip dns set allow-remote-requests=no

- Other clients services
  Disable MikroTik caching proxy,
   /ip proxy set enabled=no

  Disable MikroTik socks proxy,
   /ip socks set enabled=no

  Disable MikroTik UPNP service,
   /ip upnp set enabled=no

  Disable MikroTik dynamic name service or ip cloud,
   /ip cloud set ddns-enabled=no update-time=no

- More Secure SSH access
  /ip ssh set strong-crypto=yes
  /ip ssh print
  /ip ssh regenerate-host-key
	This will regenerate current SSH host keys, yes? [y/N]: y
  /system reboot
	Reboot, yes? [y/N]: y

File: /WAN Monitoring with VPN via LINE Notify.txt
## Create Instance AWS Cloud and Install MikroTik CHR on AWS Cloud: https://console.aws.amazon.com/
## Buy license key For MikroTik CHR: https://mikrotik.com/
## Create LINE Token: https://notify-bot.line.me/en/
## Encode Thai message For LINE notify: https://meyerweb.com/eric/tools/dencoder/

## MikroTik CHR (Run on AWS Cloud) ##

1.Enable L2TP Server
2.Create Secrets User, Password and set "Local Address" and "Remote Address"
3.Go to Tools > Netwatch
  3.1) Press +
       Host: Enter "Remote Address"
       Interval: 00:00:10
       Timeout: 800
  3.2) Go to Up tab,
       On Up:

:local token;
:local message;
:set token "Insert your LINE Token";
:set message "Internet is Up";

/tool fetch http-method=post http-header-field="Authorization:Bearer $token" http-data="message=$message" output=none https://notify-api.line.me/api/notify

  3.3) Go to Down tab,
       On Down:

:local token;
:local message;
:set token "Insert your LINE Token";
:set message "Internet is Down";

/tool fetch http-method=post http-header-field="Authorization:Bearer $token" http-data="message=$message" output=none https://notify-api.line.me/api/notify

  3.4) Press Apply and OK

######################################


## MikroTik Site (For Check WAN interface is up or down) ##
1. Go to PPP
   1.1) Press + and Choose L2TP Client
   1.2) Go to Dial Out tab,
        Connect To: Insert Public IP of AWS Cloud (MikroTik CHR)
        User: Insert User of VPN
        Password: Insert Password of VPN
   1.3) Press Apply and OK

######################################

File: /[Cloudflare] Configuring DoH Server on MikroTik RouterOS 7.8 (with certificates).txt
Encrypt your DNS requests with MikroTik (RouterOS 7.8 Stable)

(1) Quick command line setup for Cloudflare:

# Temporarily add a normal upstream DNS resolver
1. /ip dns set servers=1.1.1.1,1.0.0.1

# CA certificates extracted from DigiCert
2. /tool fetch https://cacerts.digicert.com/DigiCertGlobalRootCA.crt.pem

# Import CA to ca-store
3. /certificate import file-name=DigiCertGlobalRootCA.crt.pem passphrase=""

# Set the DoH resolver to cloudflare
4. /ip dns set use-doh-server=https://1.1.1.1/dns-query verify-doh-cert=yes allow-remote-requests=yes

# Remove the old upstream DNS resolvers
5. /ip dns set servers=""

Reminder: Uncheck "user-peer-dns" from dhcp-client (WAN) or pppoe-out1 (WAN)

#########################################################################
(2) Redirect DNS queries to router:

/ip firewall nat add chain=dstnat protocol=tcp dst-port=53 action=redirect to-ports=53
/ip firewall nat add chain=dstnat protocol=udp dst-port=53 action=redirect to-ports=53

#########################################################################
(3) Script for updating certificates

System > Scripts

Name: Update-Cert
Policy: ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
Source:

/tool fetch https://cacerts.digicert.com/DigiCertGlobalRootCA.crt.pem
:delay 10s
/certificate import file-name=DigiCertGlobalRootCA.crt.pem passphrase=""

#########################################################################
(4) Scheduler for run "Update-Cert" in every 1 week

Name: Update-Cert
policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
Start Time: 00:00:00
Interval: 7d 00:00:00
On Event: /system script run Update-Cert

#########################################################################








File: /[Script -MikroTik] 2 PPPoE WAN Connection and Failover using Netwatch Tool and Scripts.txt
#################################
# 2 PPPoE WAN Connection and Failover using Netwatch Tool and Scripts
#################################

### ISP1 - PPPoE WAN Connection (pppoe-out1) ###
PPP > Go to pppoe-out1 interface and uncheck Add Default Route.

/ip route
add comment="To ISP1" distance=1 gateway=pppoe-out1
add comment="Netwatch ISP1 (Google DNS)" distance=1 dst-address=8.8.8.8/32 gateway=pppoe-out1

Go to Tools > Netwatch
1.1 Press +
1.2 In (Host) tab
    -> Host: 8.8.8.8
    -> Interval: 00:00:10
    -> Timeout: 800
1.3 In (Up) tab
    -> On up:

ip route enable [find dst-address=0.0.0.0/0 gateway=pppoe-out1]
:log warning "ISP1 is up"

1.4 In (Down) tab
    -> On down:

ip route disable [find dst-address=0.0.0.0/0 gateway=pppoe-out1]
:log error "ISP1 is down"
/ip firewall connection remove [find]

1.5 Press Apply and OK.
###################################


### ISP2 - PPPoE WAN Connection (pppoe-out2) ###
PPP > Go to pppoe-out2 interface and uncheck Add Default Route.

/ip route
add comment="To ISP2" distance=2 gateway=pppoe-out2
add comment="Netwatch ISP2 (Quad9 DNS)" distance=1 dst-address=9.9.9.9/32 gateway=pppoe-out2

Go to Tools > Netwatch
1.1 Press +
1.2 In (Host) tab
    -> Host: 9.9.9.9
    -> Interval: 00:00:10
    -> Timeout: 800
1.3 In (Up) tab
    -> On up:

ip route enable [find dst-address=0.0.0.0/0 gateway=pppoe-out2]
:log warning "ISP2 is up"

1.4 In (Down) tab
    -> On down:

ip route disable [find dst-address=0.0.0.0/0 gateway=pppoe-out2]
:log error "ISP2 is down"
/ip firewall connection remove [find]

1.5 Press Apply and OK.
###################################

File: /[Script-MikroTik] 1 DHCP Client WAN Connection (Dynamic IP from ISP) + Auto Fail Over + Recursive Routing.txt
####################################################################################
## 1 DHCP Client WAN Connection (Dynamic IP from ISP) + Auto Fail Over + Recursive Routing      													   
####################################################################################

###################################################################################
## [Edit script]
## /ip route add distance=1 gateway=$"gateway-address" dst-address="8.8.8.8" scope=30  target-scope=10  comment="ISP2" <<<-- Edit only your dst-address (DNS Server for Check Recursive) and do not edit comment!!!
## /ip route add distance=2 gateway="8.8.8.8" check-gateway=ping scope=30  target-scope=30 comment="ISP2" <<<-- Edit only your distance (For do FailOver), gateway(DNS Server for Check Recursive) and do not edit comment!!!
###################################################################################

####################################################################################
## [How To Set-up]
## IP > DHCP Client > Select WAN Interface > Add Default Route: no
## IP > DHCP Client > Select WAN Interface > Advance Tabs > Script: Paste Script
####################################################################################

:if ($bound=1) do={
	/ip route add distance=1 gateway=$"gateway-address" dst-address="8.8.8.8" scope=30  target-scope=10  comment="ISP2"
        /ip route add distance=2 gateway="8.8.8.8" check-gateway=ping scope=30  target-scope=30 comment="ISP2"
} else={
	/ip route remove [/ip route find comment="ISP2"]
}

File: /[Script-MikroTik] 2 PPPoE WAN Connection (Dynamic IP from ISP) + Auto Fail Over + Recursive Routing (RouterOS7).txt
################################################################################################
## 2 PPPoE WAN Connection (Dynamic IP from ISP) + Auto Fail Over + Recursive Routing (RouterOS7)
## Credit : @Ton(y)Dev พ่อมดไอที													   
################################################################################################

### PPP > Profiles > Name Profile1 (New Profile) > Scripts > On Up: ###

:local createRoute do={
  /log/info message="Add route $remoteAddress"
  /ip/route/add dst-address=$dstAddress gateway=$remoteAddress scope=10 target-scope=10 distance=$distance comment=("D".$wan)
  /ip/route/add dst-address=0.0.0.0/0 gateway=$gateway scope=30 target-scope=11 distance=$distance check-gateway=ping routing-table=main suppress-hw-offload=no comment=("D".$wan)
}

:local wanConf {
  {
  "remoteAddress"=$"remote-address";
  "dstAddress"=1.1.1.1/32;
  "gateway"=1.1.1.1;
  "distance"=1;
  "wan"="pppoe-out1"
  };
  {
  "remoteAddress"=$"remote-address";
  "dstAddress"=8.8.8.8/32;
  "gateway"=8.8.8.8;
  "distance"=2;
  "wan"="pppoe-out2"
  };
}

:local getInterface [/interface/get $interface];

:foreach w in=$wanConf do={
 :local wan ($w->"wan");
 :if ($wan = ($getInterface->"name")) do={
  :if ([:len [/ip/route/print as-value where comment=("D".$wan)]] > 0) do={
   /log/info message="Remove route D$wan"
   /ip/route/remove [find comment=("D".$wan)]
  }
  
  $createRoute remoteAddress=($w->"remoteAddress") dstAddress=($w->"dstAddress") gateway=($w->"gateway") distance=($w->"distance") wan=$wan
 }
}

##########[Completed PPP UP]##########


### PPP > Profiles > Name Profile1 (New Profile) > Scripts > On Down: ###

:local removeRoute do={ 
 /ip/route/remove [find comment=$wan]
}

:local gw [/ip/route/print as-value where gateway=$"remote-address"];

:if (($gw->0->"comment") != "") do={
 $removeRoute wan=($gw->0->"comment")
}

##########[Completed PPP DOWN]##########

File: /[Script-MikroTik] 2 PPPoE WAN Connection (Dynamic IP from ISP) + Auto Fail Over + Recursive Routing.txt
####################################################################################
## 2 PPPoE WAN Connection (Dynamic IP from ISP) + Auto Fail Over + Recursive Routing      													   
####################################################################################

### PPP > Profiles > Name Profile1 (New Profile) > Scripts > On Up: ###

:local createRoute do={
 /log info message="Add route $remoteAddress"
 /ip route add dst-address=$dstAddress gateway=$remoteAddress scope=30 target-scope=10 comment=("D".$wan)
 /ip route add dst-address=0.0.0.0/0 gateway=$gateway scope=30 target-scope=30 distance=$distance check-gateway=ping comment=("D".$wan)
}

:local wanArr {
 {
  "remoteAddress"=$"remote-address";
  "dstAddress"=1.1.1.1/32;
  "gateway"=1.1.1.1;
  "distance"=1;
  "wan"="pppoe-out1"
 };
 {
  "remoteAddress"=$"remote-address";
  "dstAddress"=8.8.8.8/32;
  "gateway"=8.8.8.8;
  "distance"=2;
  "wan"="pppoe-out2"
 };
}

:local intf1 [/interface get $interface];
:foreach w in=$wanArr do={
 if (($w->"wan") = ($intf1->"name")) do={
  $createRoute remoteAddress=($w->"remoteAddress") dstAddress=($w->"dstAddress") gateway=($w->"gateway") distance=($w->"distance") wan=($w->"wan")
 }
}

##########[Completed PPP UP]##########


### PPP > Profiles > Name Profile1 (New Profile) > Scripts > On Down: ###

:local removeRoute do={ 
 /ip route remove [find comment=$wan]
}

:local gw [/ip route print as-value where gateway=$"remote-address"];
:if (($gw->0->"comment") != "") do={
 $removeRoute wan=($gw->0->"comment")
}

##########[Completed PPP DOWN]##########

File: /[Script-MikroTik] Accept Important ICMP Types.txt
/ip firewall filter
add action=jump chain=forward comment="Accept Important ICMP Types" jump-target=ICMP protocol=icmp
add action=jump chain=input jump-target=ICMP protocol=icmp
add action=accept chain=ICMP comment="Echo Reply" icmp-options=0:0 protocol=icmp
add action=accept chain=ICMP comment="Allow Echo Request" icmp-options=8:0 protocol=icmp
add action=accept chain=ICMP comment="Allow Time Exceeded" icmp-options=11:0 protocol=icmp
add action=accept chain=ICMP comment="Net Unreachable" icmp-options=3:0 protocol=icmp
add action=accept chain=ICMP comment="Port Unreachable" icmp-options=3:3 protocol=icmp
add action=accept chain=ICMP comment="Host Unreachable Fragmentation Required" icmp-options=3:4 protocol=icmp
add action=return chain=ICMP protocol=icmp
add action=drop chain=forward comment="Deny All Other Types" protocol=icmp
add action=drop chain=input comment="Deny All Other Types" protocol=icmp

File: /[Script-MikroTik] Block Bogon IP Addresses on MikroTik Firewall.txt
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

/ip firewall filter
add action=drop chain=forward comment="Block Bogon IP Addresses" in-interface=pppoe-out1 src-address-list=BOGONS

File: /[Script-MikroTik] Blocking Facebook on RouterOS using Address-Lists.txt
/ip firewall filter
add action=drop chain=forward dst-address-list=Facebook src-address=192.168.50.0/24 comment="Blocking Facebook on RouterOS using Address-Lists"

/ip firewall address-list
add address=146.88.59.0/24 list=Facebook
add address=74.119.76.0/22 list=Facebook
add address=45.64.40.0/22 list=Facebook
add address=69.63.176.0/20 list=Facebook
add address=31.13.64.0/18 list=Facebook
add address=66.220.144.0/20 list=Facebook
add address=69.171.224.0/19 list=Facebook
add address=103.4.96.0/22 list=Facebook
add address=173.252.64.0/19 list=Facebook
add address=173.252.96.0/19 list=Facebook
add address=179.60.192.0/22 list=Facebook
add address=204.15.20.0/22 list=Facebook
add address=31.13.24.0/21 list=Facebook
add address=199.201.64.0/22 list=Facebook
add address=185.60.216.0/22 list=Facebook
add address=157.240.0.0/16 list=Facebook
add address=129.205.94.0/23 list=Facebook

File: /[Script-MikroTik] Blocking Facebook on RouterOS using TLS Host.txt
/ip firewall filter
add action=drop chain=forward dst-address-list=Facebook src-address=192.168.50.0/24 comment="Blocking Facebook on RouterOS using TLS Host"

/ip firewall mangle
add action=add-dst-to-address-list address-list=Facebook address-list-timeout=4w2d chain=prerouting dst-port=443 protocol=tcp tls-host=*.facebook.com comment="Detecting IP Addresses Facebook"


After putting the script on RouterOS. Please do this before using it.
1. Clear Traffic Connections on RouterOS.
   - IP -> Firewall -> Connections
   - Delete All Connections (Shortcut key: CTRL + A And Click remove button)
2. Clear Cache on your web browser.


File: /[Script-MikroTik] Blocking LINE on RouterOS using Address-Lists.txt
/ip firewall filter
add action=drop chain=forward dst-address-list=LINE src-address=192.168.50.0/24 comment="Blocking LINE on RouterOS using Address-Lists"

/ip firewall address-list add list=LINE address=203.104.158.0/24
/ip firewall address-list add list=LINE address=203.104.157.0/24
/ip firewall address-list add list=LINE address=203.104.156.0/24
/ip firewall address-list add list=LINE address=203.104.156.0/23
/ip firewall address-list add list=LINE address=203.104.155.0/24
/ip firewall address-list add list=LINE address=203.104.154.0/24
/ip firewall address-list add list=LINE address=203.104.153.0/24
/ip firewall address-list add list=LINE address=203.104.152.0/24
/ip firewall address-list add list=LINE address=203.104.152.0/22
/ip firewall address-list add list=LINE address=203.104.151.0/24
/ip firewall address-list add list=LINE address=203.104.150.0/24
/ip firewall address-list add list=LINE address=203.104.149.0/24
/ip firewall address-list add list=LINE address=203.104.148.0/24
/ip firewall address-list add list=LINE address=203.104.147.0/24
/ip firewall address-list add list=LINE address=203.104.146.0/24
/ip firewall address-list add list=LINE address=203.104.145.0/24
/ip firewall address-list add list=LINE address=203.104.144.0/24
/ip firewall address-list add list=LINE address=203.104.144.0/21
/ip firewall address-list add list=LINE address=203.104.143.0/24
/ip firewall address-list add list=LINE address=203.104.142.0/24
/ip firewall address-list add list=LINE address=203.104.141.0/24
/ip firewall address-list add list=LINE address=203.104.140.0/24
/ip firewall address-list add list=LINE address=203.104.139.0/24
/ip firewall address-list add list=LINE address=203.104.138.0/24
/ip firewall address-list add list=LINE address=203.104.137.0/24
/ip firewall address-list add list=LINE address=203.104.136.0/24
/ip firewall address-list add list=LINE address=203.104.135.0/24
/ip firewall address-list add list=LINE address=203.104.134.0/24
/ip firewall address-list add list=LINE address=203.104.133.0/24
/ip firewall address-list add list=LINE address=203.104.132.0/24
/ip firewall address-list add list=LINE address=203.104.131.0/24
/ip firewall address-list add list=LINE address=203.104.130.0/24
/ip firewall address-list add list=LINE address=203.104.129.0/24
/ip firewall address-list add list=LINE address=203.104.128.0/24
/ip firewall address-list add list=LINE address=203.104.128.0/20
/ip firewall address-list add list=LINE address=147.92.248.0/21
/ip firewall address-list add list=LINE address=147.92.247.0/24
/ip firewall address-list add list=LINE address=147.92.226.0/24
/ip firewall address-list add list=LINE address=147.92.200.0/21
/ip firewall address-list add list=LINE address=147.92.188.0/24
/ip firewall address-list add list=LINE address=147.92.169.0/24
/ip firewall address-list add list=LINE address=147.92.164.0/22
/ip firewall address-list add list=LINE address=147.92.135.0/24
/ip firewall address-list add list=LINE address=147.92.134.0/24
/ip firewall address-list add list=LINE address=147.92.133.0/24
/ip firewall address-list add list=LINE address=147.92.132.0/24
/ip firewall address-list add list=LINE address=147.92.131.0/24
/ip firewall address-list add list=LINE address=147.92.130.0/24
/ip firewall address-list add list=LINE address=147.92.129.0/24
/ip firewall address-list add list=LINE address=147.92.128.0/24
/ip firewall address-list add list=LINE address=147.92.128.0/17
/ip firewall address-list add list=LINE address=119.235.237.0/24
/ip firewall address-list add list=LINE address=119.235.236.0/24
/ip firewall address-list add list=LINE address=119.235.236.0/23
/ip firewall address-list add list=LINE address=119.235.235.0/24
/ip firewall address-list add list=LINE address=119.235.232.0/24
/ip firewall address-list add list=LINE address=119.235.224.0/24
/ip firewall address-list add list=LINE address=103.2.31.0/24
/ip firewall address-list add list=LINE address=103.2.30.0/24
/ip firewall address-list add list=LINE address=103.2.30.0/23
/ip firewall address-list add list=LINE address=103.2.28.0/24

File: /[Script-MikroTik] Blocking Netflix traffic using RouterOS.txt
/ip firewall filter
add action=drop chain=forward dst-address-list=Netflix src-address=192.168.50.0/24 comment="Blocking Netflix traffic using RouterOS"

/ip firewall mangle
add action=add-dst-to-address-list address-list=Netflix address-list-timeout=4w2d chain=prerouting content=nflxvideo.net src-address=192.168.50.0/24 comment="Detecting IP Addresses Netflix"

File: /[Script-MikroTik] Blocking PUBG Mobile traffic using RouterOS.txt
/ip firewall filter
add action=drop chain=forward dst-address-list=PUBGM src-address=192.168.50.0/24 comment="Blocking PUBG Mobile traffic using RouterOS"

/ip firewall mangle
add action=add-dst-to-address-list address-list=PUBGM address-list-timeout=4d chain=prerouting dst-port=10012,17500 protocol=tcp comment="Detecting IP Addresses PUBG Mobile"
add action=add-dst-to-address-list address-list=PUBGM address-list-timeout=4d chain=prerouting dst-port=10000-30000 protocol=udp

File: /[Script-MikroTik] Blocking RoV mobile traffic using RouterOS.txt
/ip firewall filter
add action=drop chain=forward dst-address-list=RoV src-address=192.168.50.0/24 comment="Blocking Garena RoV traffic using RouterOS"

/ip firewall mangle
add action=add-dst-to-address-list address-list=RoV address-list-timeout=4d chain=prerouting dst-port=20000 protocol=tcp comment="Detecting IP Addresses Garena RoV (Sv.TH)"

File: /[Script-MikroTik] Blocking Steam on RouterOS using Address-Lists.txt
/ip firewall filter
add action=drop chain=forward dst-address-list=Steam src-address=192.168.50.0/24 comment="Blocking Steam on RouterOS using Address-Lists"

/ip firewall address-list
add address=45.121.184.0/23 list=Steam
add address=45.121.186.0/23 list=Steam
add address=103.10.124.0/24 list=Steam
add address=103.10.125.0/24 list=Steam
add address=103.28.54.0/23 list=Steam
add address=146.66.152.0/23 list=Steam
add address=146.66.154.0/24 list=Steam
add address=146.66.155.0/24 list=Steam
add address=146.66.156.0/23 list=Steam
add address=146.66.158.0/23 list=Steam
add address=153.254.86.0/24 list=Steam
add address=155.133.224.0/23 list=Steam
add address=155.133.227.0/24 list=Steam
add address=155.133.228.0/23 list=Steam
add address=155.133.230.0/23 list=Steam
add address=155.133.232.0/24 list=Steam
add address=155.133.233.0/24 list=Steam
add address=155.133.234.0/24 list=Steam
add address=155.133.235.0/24 list=Steam
add address=155.133.236.0/23 list=Steam
add address=155.133.238.0/24 list=Steam
add address=155.133.239.0/24 list=Steam
add address=155.133.240.0/23 list=Steam
add address=155.133.242.0/23 list=Steam
add address=155.133.244.0/24 list=Steam
add address=155.133.245.0/24 list=Steam
add address=155.133.246.0/23 list=Steam
add address=155.133.248.0/24 list=Steam
add address=155.133.249.0/24 list=Steam
add address=155.133.250.0/24 list=Steam
add address=155.133.252.0/24 list=Steam
add address=155.133.253.0/24 list=Steam
add address=155.133.254.0/24 list=Steam
add address=155.133.255.0/24 list=Steam
add address=162.254.192.0/24 list=Steam
add address=162.254.193.0/24 list=Steam
add address=162.254.194.0/23 list=Steam
add address=162.254.196.0/24 list=Steam
add address=162.254.197.0/24 list=Steam
add address=162.254.198.0/24 list=Steam
add address=162.254.199.0/24 list=Steam
add address=185.25.180.0/23 list=Steam
add address=185.25.182.0/24 list=Steam
add address=185.25.183.0/24 list=Steam
add address=190.216.121.0/24 list=Steam
add address=190.217.33.0/24 list=Steam
add address=192.69.96.0/23 list=Steam
add address=205.185.194.0/24 list=Steam
add address=205.196.6.0/24 list=Steam
add address=208.64.200.0/24 list=Steam
add address=208.64.201.0/24 list=Steam
add address=208.64.202.0/24 list=Steam
add address=208.64.203.0/24 list=Steam
add address=208.78.164.0/23 list=Steam
add address=208.78.166.0/24 list=Steam
add address=208.78.167.0/24 list=Steam

File: /[Script-MikroTik] Blocking TikTok using RouterOS.txt
/ip firewall filter
add action=drop chain=forward dst-address-list=TikTok src-address=192.168.50.0/24 comment="Blocking TikTok using RouterOS"

/ip firewall mangle
add action=add-dst-to-address-list address-list=TikTok address-list-timeout=4w2d chain=prerouting content=.tiktok.com src-address=192.168.50.0/24 comment="Detecting IP Addresses TikTok"
add action=add-dst-to-address-list address-list=TikTok address-list-timeout=4w2d chain=prerouting content=.tiktokv.com src-address=192.168.50.0/24
add action=add-dst-to-address-list address-list=TikTok address-list-timeout=4w2d chain=prerouting content=.tiktokcdn.com src-address=192.168.50.0/24
add action=add-dst-to-address-list address-list=TikTok address-list-timeout=4w2d chain=prerouting content=.byteoversea.com src-address=192.168.50.0/24
add action=add-dst-to-address-list address-list=TikTok address-list-timeout=4w2d chain=prerouting content=.ibyteimg.com src-address=192.168.50.0/24
add action=add-dst-to-address-list address-list=TikTok address-list-timeout=4w2d chain=prerouting content=.ibytedtos.com src-address=192.168.50.0/24
add action=add-dst-to-address-list address-list=TikTok address-list-timeout=4w2d chain=prerouting content=.myqcloud.com src-address=192.168.50.0/24

File: /[Script-MikroTik] Blocking Twitter on RouterOS using Address-Lists.txt
/ip firewall filter
add action=drop chain=forward dst-address-list=Twitter src-address=192.168.50.0/24 comment="Blocking Twitter on RouterOS using Address-Lists"

/ip firewall address-list add list=Twitter address=8.25.196.0/23
/ip firewall address-list add list=Twitter address=8.25.194.0/23
/ip firewall address-list add list=Twitter address=69.195.188.0/24
/ip firewall address-list add list=Twitter address=69.195.187.0/24
/ip firewall address-list add list=Twitter address=69.195.186.0/24
/ip firewall address-list add list=Twitter address=69.195.185.0/24
/ip firewall address-list add list=Twitter address=69.195.182.0/24
/ip firewall address-list add list=Twitter address=69.195.181.0/24
/ip firewall address-list add list=Twitter address=69.195.180.0/24
/ip firewall address-list add list=Twitter address=69.195.179.0/24
/ip firewall address-list add list=Twitter address=69.195.178.0/24
/ip firewall address-list add list=Twitter address=69.195.177.0/24
/ip firewall address-list add list=Twitter address=69.195.176.0/24
/ip firewall address-list add list=Twitter address=69.195.175.0/24
/ip firewall address-list add list=Twitter address=69.195.174.0/24
/ip firewall address-list add list=Twitter address=69.195.171.0/24
/ip firewall address-list add list=Twitter address=69.195.169.0/24
/ip firewall address-list add list=Twitter address=69.195.168.0/24
/ip firewall address-list add list=Twitter address=69.195.166.0/24
/ip firewall address-list add list=Twitter address=69.195.165.0/24
/ip firewall address-list add list=Twitter address=69.195.164.0/24
/ip firewall address-list add list=Twitter address=69.195.163.0/24
/ip firewall address-list add list=Twitter address=69.195.162.0/24
/ip firewall address-list add list=Twitter address=69.195.160.0/24
/ip firewall address-list add list=Twitter address=69.12.63.0/24
/ip firewall address-list add list=Twitter address=69.12.62.0/24
/ip firewall address-list add list=Twitter address=69.12.61.0/24
/ip firewall address-list add list=Twitter address=69.12.56.0/21
/ip firewall address-list add list=Twitter address=64.63.33.0/24
/ip firewall address-list add list=Twitter address=64.63.0.0/18
/ip firewall address-list add list=Twitter address=209.237.221.0/24
/ip firewall address-list add list=Twitter address=209.237.220.0/24
/ip firewall address-list add list=Twitter address=209.237.218.0/24
/ip firewall address-list add list=Twitter address=209.237.217.0/24
/ip firewall address-list add list=Twitter address=209.237.216.0/24
/ip firewall address-list add list=Twitter address=209.237.215.0/24
/ip firewall address-list add list=Twitter address=209.237.214.0/24
/ip firewall address-list add list=Twitter address=209.237.213.0/24
/ip firewall address-list add list=Twitter address=209.237.210.0/24
/ip firewall address-list add list=Twitter address=209.237.209.0/24
/ip firewall address-list add list=Twitter address=209.237.201.0/24
/ip firewall address-list add list=Twitter address=209.237.200.0/24
/ip firewall address-list add list=Twitter address=209.237.199.0/24
/ip firewall address-list add list=Twitter address=209.237.198.0/24
/ip firewall address-list add list=Twitter address=209.237.197.0/24
/ip firewall address-list add list=Twitter address=209.237.196.0/24
/ip firewall address-list add list=Twitter address=209.237.195.0/24
/ip firewall address-list add list=Twitter address=209.237.194.0/24
/ip firewall address-list add list=Twitter address=209.237.193.0/24
/ip firewall address-list add list=Twitter address=209.237.192.0/24
/ip firewall address-list add list=Twitter address=202.160.131.0/24
/ip firewall address-list add list=Twitter address=202.160.130.0/24
/ip firewall address-list add list=Twitter address=202.160.129.0/24
/ip firewall address-list add list=Twitter address=202.160.128.0/24
/ip firewall address-list add list=Twitter address=199.96.62.0/23
/ip firewall address-list add list=Twitter address=199.96.61.0/24
/ip firewall address-list add list=Twitter address=199.96.60.0/24
/ip firewall address-list add list=Twitter address=199.96.60.0/23
/ip firewall address-list add list=Twitter address=199.96.58.0/23
/ip firewall address-list add list=Twitter address=199.96.57.0/24
/ip firewall address-list add list=Twitter address=199.96.56.0/24
/ip firewall address-list add list=Twitter address=199.96.56.0/23
/ip firewall address-list add list=Twitter address=199.59.148.0/22
/ip firewall address-list add list=Twitter address=199.16.156.0/23
/ip firewall address-list add list=Twitter address=199.16.156.0/22
/ip firewall address-list add list=Twitter address=192.48.237.0/24
/ip firewall address-list add list=Twitter address=192.48.236.0/24
/ip firewall address-list add list=Twitter address=192.48.236.0/23
/ip firewall address-list add list=Twitter address=192.133.78.0/23
/ip firewall address-list add list=Twitter address=192.133.76.0/23
/ip firewall address-list add list=Twitter address=192.133.76.0/22
/ip firewall address-list add list=Twitter address=188.64.224.0/21
/ip firewall address-list add list=Twitter address=185.45.6.0/23
/ip firewall address-list add list=Twitter address=185.45.5.0/24
/ip firewall address-list add list=Twitter address=185.45.4.0/24
/ip firewall address-list add list=Twitter address=185.45.4.0/23
/ip firewall address-list add list=Twitter address=104.244.47.0/24
/ip firewall address-list add list=Twitter address=104.244.46.0/24
/ip firewall address-list add list=Twitter address=104.244.45.0/24
/ip firewall address-list add list=Twitter address=104.244.44.0/24
/ip firewall address-list add list=Twitter address=104.244.43.0/24
/ip firewall address-list add list=Twitter address=104.244.42.0/24
/ip firewall address-list add list=Twitter address=104.244.41.0/24
/ip firewall address-list add list=Twitter address=104.244.40.0/24

File: /[Script-MikroTik] Blocking Youtube on RouterOS using TLS Host.txt
/ip firewall filter
add action=drop chain=forward comment="Blocking Youtube on RouterOS using TLS Host" dst-address-list=Youtube src-address=192.168.50.0/24

/ip firewall mangle
add action=add-dst-to-address-list address-list=Youtube address-list-timeout=4w2d chain=prerouting comment="Detecting IP Addresses Youtube" protocol=tcp tls-host=*.youtube.com
add action=add-dst-to-address-list address-list=Youtube address-list-timeout=4w2d chain=prerouting protocol=tcp tls-host=*youtube*



File: /[Script-MikroTik] Drop Port Scan Attacks using MikroTik Firewall.txt
/ip firewall filter
add action=add-src-to-address-list address-list="Port Scan" address-list-timeout=4w2d chain=forward comment="Preventing Port Scan" protocol=tcp psd=21,3s,3,1
add action=add-src-to-address-list address-list="Port Scan" address-list-timeout=4w2d chain=input protocol=tcp psd=21,3s,3,1
add action=drop chain=forward src-address-list="Port Scan"
add action=drop chain=input src-address-list="Port Scan"

File: /[Script-MikroTik] Dynamic IP problem with manual created routes (DHCP-Client).txt
IP > DHCP Client > Select Interface > Advance Tabs > Script:

################################################################################################
:if ($bound=1) do={
	/ip route add distance=1 gateway=$"gateway-address" routing-mark=via-ISP2 comment="ISP2"
} else={
	/ip route remove [/ip route find comment="ISP2"]
}
################################################################################################

File: /[Script-MikroTik] Hairpin NAT.txt
#TechBlogClub by Krittin Srithong

/ip firewall address-list
add address=192.168.50.0/24 list=LAN

/ip firewall nat
add action=masquerade chain=srcnat comment="Internel Hairpin NAT" dst-address=!192.168.50.1 src-address-list=LAN
add action=dst-nat chain=dstnat dst-address-type=local dst-port=80 protocol=tcp src-address-list=LAN to-addresses=192.168.50.100 to-ports=80
add action=dst-nat chain=dstnat comment="External Port Forwarding" dst-port=80 in-interface=WAN1 protocol=tcp to-addresses=192.168.50.100 to-ports=80

File: /[Script-MikroTik] NO-IP.COM DDNS Update.txt
# No-IP, Dynamic DNS Updater
# TechBlogClub by Krittin Srithong

#--------------- Change your information here ------------------

:local noipuser "enterNOIPUsername"
:local noippass "enterNOIPPassword"
:local noiphost "enterYOURhostname.ddns.net"
:local inetinterface "pppoe-out1"

#---------------------------------------------------------------

:if ([/interface get $inetinterface value-name=running]) do={
# Get the current IP on the interface
  :local currentIP [/ip address get [find interface="$inetinterface" disabled=no] address]

# Strip the net mask off the IP address
  :for i from=( [:len $currentIP] - 1) to=0 do={
     :if ( [:pick $currentIP $i] = "/") do={ 
        :set currentIP [:pick $currentIP 0 $i]
     } 
  }

# The update URL. Note the "\3F" is hex for question mark (?). Required since ? is a special character in commands.
  :local url "http://dynupdate.no-ip.com/nic/update\3Fmyip=$currentIP"
  :local noiphostarray
  :set noiphostarray [:toarray $noiphost]
  
  :foreach host in=$noiphostarray do={
    # Check 1 - resolved IP
    :local resolvedIP [:resolve $host];

    # Check 2 - Saved response from NO-IP
    :local filename ("no-ip_ddns_update-" . $host . ".txt")
    :local savedMatch -1
    :local savedIP "No File";

    if ( [:len [/file find name=$filename]] > 0 ) do={
      :set savedIP [/file get $filename contents]
      :set savedMatch [:find $savedIP $currentIP -1]
    }

    # If either check fails, update IP	
    :if (($currentIP = $resolvedIP) && ($savedMatch >= 0)) do={
      :log info "No-IP: Host $host already on No-IP with IP $resolvedIP"
    } else={
      :log info "No-IP: Sending update for $host - $resolvedIP saved as $savedIP"
      /tool fetch url=($url . "&hostname=$host") user=$noipuser password=$noippass mode=http dst-path=$filename
      :log info "No-IP: Host $host updated on No-IP with IP $currentIP"
    }
  }
} else={
  :log info "No-IP: $inetinterface is not currently running, so therefore will not update."
}

File: /[Script-MikroTik] Port Knocking Security.txt
/ip firewall filter
add action=accept chain=input comment="Port Knocking Security" connection-state=established,related
add action=add-src-to-address-list address-list=Temporary address-list-timeout=1m chain=input dst-port=1234 protocol=tcp
add action=add-src-to-address-list address-list=Valid address-list-timeout=1m chain=input dst-port=4321 protocol=tcp src-address-list=Temporary
add action=accept chain=input src-address-list=Valid
add action=drop chain=input

File: /[Script-MikroTik] Preventing Brute Force Attack.txt
/ip firewall filter
add action=drop chain=input comment="Drop anyone in Black List (SSH)" src-address-list="Black List (SSH)"
add action=jump chain=input comment="Jump to Black List (SSH) Chain" dst-port=22 jump-target="Black List (SSH) Chain" protocol=tcp
add action=add-src-to-address-list address-list="Black List (SSH)" address-list-timeout=4w2d chain="Black List (SSH) Chain" comment="Transfer repeated attempts from Black List (SSH) Stage 3 to Black List (SSH)" connection-state=new src-address-list="Black List (SSH) Stage 3"
add action=add-src-to-address-list address-list="Black List (SSH) Stage 3" address-list-timeout=1m chain="Black List (SSH) Chain" comment="Add Successive attempts to Black List (SSH) Stage 3" connection-state=new src-address-list="Black List (SSH) Stage 2"
add action=add-src-to-address-list address-list="Black List (SSH) Stage 2" address-list-timeout=1m chain="Black List (SSH) Chain" comment="Add Successive attempts to Black List (SSH) Stage 2" connection-state=new src-address-list="Black List (SSH) Stage 1"
add action=add-src-to-address-list address-list="Black List (SSH) Stage 1" address-list-timeout=1m chain="Black List (SSH) Chain" comment="Add initial attempt to Black List (SSH) Stage 1" connection-state=new
add action=return chain="Black List (SSH) Chain" comment="Return from Black List (SSH) chain"

File: /[Script-MikroTik] Preventing ICMP Smurf Attack.txt
/ip firewall raw
add action=drop chain=prerouting comment="Preventing ICMP Smurf Attack" dst-address-type=broadcast protocol=icmp
/ip firewall filter
add action=drop chain=input comment="Block Ping (ICMP) From WAN" in-interface=pppoe-out1 protocol=icmp

File: /[Script-MikroTik] Preventing Port Scanner.txt
/ip firewall filter
add chain=input src-address-list="port scanners" action=drop comment="dropping port scanners" disabled=no
add chain=input protocol=tcp psd=21,3s,3,1 action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="Port scanners to list " disabled=no
add chain=input protocol=tcp tcp-flags=fin,!syn,!rst,!psh,!ack,!urg action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="NMAP FIN Stealth scan"
add chain=input protocol=tcp tcp-flags=fin,syn action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="SYN/FIN scan"
add chain=input protocol=tcp tcp-flags=syn,rst action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="SYN/RST scan"
add chain=input protocol=tcp tcp-flags=fin,psh,urg,!syn,!rst,!ack action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="FIN/PSH/URG scan"
add chain=input protocol=tcp tcp-flags=fin,syn,rst,psh,ack,urg action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="ALL/ALL scan"
add chain=input protocol=tcp tcp-flags=!fin,!syn,!rst,!psh,!ack,!urg action=add-src-to-address-list address-list="port scanners" address-list-timeout=2w comment="NMAP NULL scan"

File: /[Script-MikroTik] Preventing TCP SYN Attack.txt
/ip firewall filter add chain=input protocol=tcp connection-limit=200,32 action=add-src-to-address-list  address-list=blocked-addr address-list-timeout=1d 
/ip firewall filter add chain=input protocol=tcp src-address-list=blocked-addr connection-limit=3,32 action=tarpit 
/ip firewall filter add chain=forward protocol=tcp tcp-flags=syn connection-state=new action=jump jump-target=SYN-Protect comment="SYN Flood protect" disabled=no
/ip firewall filter add chain=SYN-Protect protocol=tcp tcp-flags=syn limit=400,5 connection-state=new action=accept comment="" disabled=no
/ip firewall filter add chain=SYN-Protect protocol=tcp tcp-flags=syn connection-state=new action=drop comment="" disabled=no
/ip settings set tcp-syncookies=yes

File: /[Script-MikroTik] Preventing UDP Flood Attack.txt
/ip firewall raw
add action=drop chain=prerouting comment="Preventing UDP Flood Attack" dst-port=53 in-interface=pppoe-out1 protocol=udp
add action=accept chain=prerouting dst-port=53 in-interface=!pppoe-out1 limit=100,5:packet protocol=udp
add action=drop chain=prerouting dst-port=53 in-interface=!pppoe-out1 protocol=udp


Go to IP > DNS and disable "Allow Remote Requests"

File: /[Script-MikroTik] Setting the Bandwidth Priority in the  Microsoft Teams Application on MikroTik RouterOS.txt
/ip firewall mangle
add action=mark-connection chain=prerouting comment="Mark MicrosoftTeams Application Connection" dst-address-list=MicrosoftTeams dst-port=3478,3479,3480,3481 new-connection-mark=MicrosoftTeams-Connection passthrough=yes protocol=tcp
add action=mark-connection chain=prerouting dst-address-list=MicrosoftTeams dst-port=3478,3479,3480,3481 new-connection-mark=MicrosoftTeams-Connection passthrough=yes protocol=udp
add action=mark-connection chain=prerouting comment="Mark MicrosoftTeams Web App Connections" dst-address-list=MicrosoftTeams dst-port=80,443 new-connection-mark=MicrosoftTeams-Connection passthrough=yes protocol=tcp
add action=mark-packet chain=prerouting comment="Mark All MicrosoftTeams Packets" connection-mark=MicrosoftTeams-Connection new-packet-mark=MicrosoftTeams-Packet passthrough=no

/queue simple
add comment="Internet Package (Upload Speed: 300 Mbps, Download Speed: 300 Mbps)" max-limit=300M/300M name=Parent_Queue target=192.168.50.0/24
add comment="Share Speed  to MicrosoftTeams (Upload Speed: 20Mbps, Download Speed: 20Mbps)" max-limit=20M/20M name=Queue_MicrosoftTeams packet-marks=MicrosoftTeams-Packet parent=Parent_Queue priority=1/1 target=192.168.50.0/24
add comment="Share Speed For General Working (Upload Speed: 280 Mbps, Download Speed: 280Mbps)" max-limit=280M/280M name=Queue_Other packet-marks=no-mark parent=Parent_Queue target=192.168.50.0/24

/ip firewall address-list
add address=13.107.64.0/18 list=MicrosoftTeams
add address=52.112.0.0/14 list=MicrosoftTeams
add address=52.120.0.0/14 list=MicrosoftTeams
add address=52.238.119.141/32 list=MicrosoftTeams
add address=52.244.160.207/32 list=MicrosoftTeams

File: /[Script-MikroTik] Setting the Bandwidth Priority in the Zoom Video Conferencing Application on MikroTik RouterOS.txt
/ip firewall mangle
add action=mark-connection chain=prerouting comment="Mark Zoom Application Connections" dst-address-list=Zoom dst-port=3478,3479,5090,5091,8801-8810 new-connection-mark=Zoom-Connection passthrough=yes protocol=tcp
add action=mark-connection chain=prerouting dst-address-list=Zoom dst-port=3478,3479,5090,5091,8801-8810 new-connection-mark=Zoom-Connection passthrough=yes protocol=udp
add action=mark-connection chain=prerouting comment="Mark Zoom Web App Connections" dst-address-list=Zoom dst-port=80,443 new-connection-mark=Zoom-Connection passthrough=yes protocol=tcp
add action=mark-packet chain=prerouting comment="Mark All Zoom Packets" connection-mark=Zoom-Connection new-packet-mark=Zoom-Packet passthrough=no

/queue simple
add comment="Internet Package (Upload Speed: 300 Mbps, Download Speed: 300 Mbps)" max-limit=300M/300M name=Parent_Queue target=192.168.50.0/24
add comment="Share Speed  to Zoom (Upload Speed: 20Mbps, Download Speed: 20Mbps)" max-limit=20M/20M name=Queue_Zoom packet-marks=Zoom-Packet parent=Parent_Queue priority=1/1 target=192.168.50.0/24
add comment="Share Speed For General Working (Upload Speed: 280 Mbps, Download Speed: 280Mbps)" max-limit=280M/280M name=Queue_Other packet-marks=no-mark parent=Parent_Queue target=192.168.50.0/24

/ip firewall address-list
add address=3.7.35.0/25	list=Zoom
add address=3.21.137.128/25 list=Zoom
add address=3.22.11.0/24 list=Zoom
add address=3.23.93.0/24 list=Zoom
add address=3.25.41.128/25 list=Zoom
add address=3.25.42.0/25 list=Zoom
add address=3.25.49.0/24 list=Zoom
add address=3.80.20.128/25 list=Zoom
add address=3.96.19.0/24 list=Zoom
add address=3.101.32.128/25 list=Zoom
add address=3.101.52.0/25 list=Zoom
add address=3.104.34.128/25 list=Zoom
add address=3.120.121.0/25 list=Zoom
add address=3.127.194.128/25 list=Zoom
add address=3.208.72.0/25 list=Zoom
add address=3.211.241.0/25 list=Zoom
add address=3.235.69.0/25 list=Zoom
add address=3.235.82.0/23 list=Zoom
add address=3.235.71.128/25 list=Zoom
add address=3.235.72.128/25 list=Zoom
add address=3.235.73.0/25 list=Zoom
add address=3.235.96.0/23 list=Zoom
add address=4.34.125.128/25 list=Zoom
add address=4.35.64.128/25 list=Zoom
add address=8.5.128.0/23 list=Zoom
add address=13.52.6.128/25 list=Zoom
add address=13.52.146.0/25 list=Zoom
add address=18.157.88.0/24 list=Zoom
add address=18.205.93.128/25 list=Zoom
add address=20.203.158.80/28 list=Zoom
add address=20.203.190.192/26 list=Zoom
add address=50.239.202.0/23 list=Zoom
add address=50.239.204.0/24 list=Zoom
add address=52.61.100.128/25 list=Zoom
add address=52.202.62.192/26 list=Zoom
add address=52.215.168.0/25 list=Zoom
add address=64.125.62.0/24 list=Zoom
add address=64.211.144.0/24 list=Zoom
add address=64.224.32.0/19 list=Zoom
add address=65.39.152.0/24 list=Zoom
add address=69.174.57.0/24 list=Zoom
add address=69.174.108.0/22 list=Zoom
add address=99.79.20.0/25 list=Zoom
add address=101.36.167.0/24 list=Zoom
add address=103.122.166.0/23 list=Zoom
add address=111.33.115.0/25 list=Zoom
add address=111.33.181.0/25 list=Zoom
add address=115.110.154.192/26 list=Zoom
add address=115.114.56.192/26 list=Zoom
add address=115.114.115.0/26 list=Zoom
add address=115.114.131.0/26 list=Zoom
add address=120.29.148.0/24 list=Zoom
add address=129.151.0.0/19 list=Zoom
add address=129.151.40.0/22 list=Zoom
add address=129.151.48.0/20 list=Zoom
add address=129.159.0.0/20 list=Zoom
add address=129.159.160.0/19 list=Zoom
add address=129.159.208.0/20 list=Zoom
add address=130.61.164.0/22 list=Zoom
add address=134.224.0.0/16 list=Zoom
add address=140.238.128.0/24 list=Zoom
add address=140.238.232.0/22 list=Zoom
add address=144.195.0.0/16 list=Zoom
add address=147.124.96.0/19 list=Zoom
add address=149.137.0.0/17 list=Zoom
add address=150.230.224.0/21 list=Zoom
add address=152.67.20.0/24 list=Zoom
add address=152.67.118.0/24 list=Zoom
add address=152.67.168.0/22 list=Zoom
add address=152.67.180.0/24 list=Zoom
add address=152.67.184.0/22 list=Zoom
add address=152.67.240.0/21 list=Zoom
add address=152.70.224.0/21 list=Zoom
add address=156.45.0.0/17 list=Zoom
add address=158.101.64.0/24 list=Zoom
add address=158.101.184.0/22 list=Zoom
add address=160.1.56.128/25 list=Zoom
add address=161.199.136.0/22 list=Zoom
add address=162.12.232.0/22 list=Zoom
add address=162.255.36.0/22 list=Zoom
add address=165.254.88.0/23 list=Zoom
add address=166.108.64.0/18 list=Zoom
add address=168.138.16.0/22 list=Zoom
add address=168.138.48.0/24 list=Zoom
add address=168.138.56.0/21 list=Zoom
add address=168.138.72.0/24 list=Zoom
add address=168.138.74.0/25 list=Zoom
add address=168.138.80.0/21 list=Zoom
add address=168.138.96.0/22 list=Zoom
add address=168.138.116.0/22 list=Zoom
add address=168.138.244.0/24 list=Zoom
add address=170.114.0.0/16 list=Zoom
add address=173.231.80.0/20 list=Zoom
add address=192.204.12.0/22 list=Zoom
add address=193.122.16.0/20 list=Zoom
add address=193.122.32.0/20 list=Zoom
add address=193.122.208.0/20 list=Zoom
add address=193.122.224.0/20 list=Zoom
add address=193.122.240.0/20 list=Zoom
add address=193.123.0.0/19 list=Zoom
add address=193.123.40.0/21 list=Zoom
add address=193.123.128.0/19 list=Zoom
add address=193.123.168.0/21 list=Zoom
add address=193.123.192.0/19 list=Zoom
add address=198.251.128.0/17 list=Zoom
add address=202.177.207.128/27 list=Zoom
add address=204.80.104.0/21 list=Zoom
add address=204.141.28.0/22 list=Zoom
add address=206.247.0.0/16 list=Zoom
add address=207.226.132.0/24 list=Zoom
add address=209.9.211.0/24 list=Zoom
add address=209.9.215.0/24 list=Zoom
add address=213.19.144.0/24 list=Zoom
add address=213.19.153.0/24 list=Zoom
add address=213.244.140.0/24 list=Zoom
add address=221.122.88.64/27 list=Zoom
add address=221.122.88.128/25 list=Zoom
add address=221.122.89.128/25 list=Zoom
add address=221.123.139.192/27 list=Zoom


