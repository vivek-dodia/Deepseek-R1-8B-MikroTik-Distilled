# Repository Information
Name: mikrotik-api

# Directory Structure
Directory structure:
└── github_repos/mikrotik-api/
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
    │   │       ├── pack-37d1ebe8ee3f28e817736f92f952092e9a167b9b.idx
    │   │       └── pack-37d1ebe8ee3f28e817736f92f952092e9a167b9b.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── composer.json
    ├── LICENSE
    ├── nbproject/
    │   ├── project.properties
    │   └── project.xml
    ├── README.md
    ├── src/
    │   └── MikrotikAPI/
    │       ├── Commands/
    │       │   ├── File/
    │       │   │   └── File.php
    │       │   ├── Interfaces/
    │       │   │   ├── Bonding.php
    │       │   │   ├── Bridge.php
    │       │   │   ├── EoIP.php
    │       │   │   ├── Ethernet.php
    │       │   │   ├── Interfaces.php
    │       │   │   ├── IPTunnel.php
    │       │   │   ├── L2TPClient.php
    │       │   │   ├── L2TPServer.php
    │       │   │   ├── PPPClient.php
    │       │   │   ├── PPPoEClient.php
    │       │   │   ├── PPPoEServer.php
    │       │   │   ├── PPPServer.php
    │       │   │   ├── PPTPClient.php
    │       │   │   ├── PPTPServer.php
    │       │   │   ├── VLAN.php
    │       │   │   └── VRRP.php
    │       │   ├── IP/
    │       │   │   ├── Accounting.php
    │       │   │   ├── Address.php
    │       │   │   ├── ARP.php
    │       │   │   ├── DHCPClient.php
    │       │   │   ├── DHCPRelay.php
    │       │   │   ├── DHCPServer.php
    │       │   │   ├── DNS.php
    │       │   │   ├── Firewall/
    │       │   │   │   ├── Firewall.php
    │       │   │   │   ├── FirewallAddressList.php
    │       │   │   │   ├── FirewallConnection.php
    │       │   │   │   ├── FirewallFilter.php
    │       │   │   │   ├── FirewallLayer7Protocol.php
    │       │   │   │   ├── FirewallMangle.php
    │       │   │   │   ├── FirewallNAT.php
    │       │   │   │   └── FirewallServicePort.php
    │       │   │   ├── Hotspot/
    │       │   │   │   ├── Hotspot.php
    │       │   │   │   ├── HotspotActive.php
    │       │   │   │   ├── HotspotCookies.php
    │       │   │   │   ├── HotspotHosts.php
    │       │   │   │   ├── HotspotIPBindings.php
    │       │   │   │   ├── HotspotServer.php
    │       │   │   │   ├── HotspotServerProfiles.php
    │       │   │   │   ├── HotspotUserProfiles.php
    │       │   │   │   └── HotspotUsers.php
    │       │   │   ├── IP.php
    │       │   │   ├── Pool.php
    │       │   │   ├── Route.php
    │       │   │   ├── Service.php
    │       │   │   └── WebProxy.php
    │       │   ├── PPP/
    │       │   │   ├── AAA.php
    │       │   │   ├── Active.php
    │       │   │   ├── PPP.php
    │       │   │   ├── Profile.php
    │       │   │   └── Secret.php
    │       │   └── System/
    │       │       ├── System.php
    │       │       └── SystemScheduler.php
    │       ├── Core/
    │       │   ├── Connector.php
    │       │   ├── StreamReciever.php
    │       │   └── StreamSender.php
    │       ├── Entity/
    │       │   ├── Attribute.php
    │       │   └── Auth.php
    │       ├── MikrotikAPI.php
    │       ├── Talker/
    │       │   ├── Talker.php
    │       │   ├── TalkerReciever.php
    │       │   └── TalkerSender.php
    │       └── Util/
    │           ├── DebugDumper.php
    │           ├── ResultUtil.php
    │           ├── SentenceUtil.php
    │           └── Util.php
    ├── test/
    │   └── test.php
    └── vendor/
        ├── autoload.php
        └── composer/
            ├── autoload_classmap.php
            ├── autoload_namespaces.php
            ├── autoload_real.php
            └── ClassLoader.php


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
	url = https://github.com/nunenuh/mikrotik-api.git
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
0000000000000000000000000000000000000000 82ad5e43e8d06fb534508d66d161705ee258bf46 vivek-dodia <vivek.dodia@icloud.com> 1738605811 -0500	clone: from https://github.com/nunenuh/mikrotik-api.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 82ad5e43e8d06fb534508d66d161705ee258bf46 vivek-dodia <vivek.dodia@icloud.com> 1738605811 -0500	clone: from https://github.com/nunenuh/mikrotik-api.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 82ad5e43e8d06fb534508d66d161705ee258bf46 vivek-dodia <vivek.dodia@icloud.com> 1738605811 -0500	clone: from https://github.com/nunenuh/mikrotik-api.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
82ad5e43e8d06fb534508d66d161705ee258bf46 refs/remotes/origin/master


File: /.git\refs\heads\master
82ad5e43e8d06fb534508d66d161705ee258bf46


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
/nbproject/private/

File: /composer.json
{
    "name": "nunenuh/mikrotik-api",
    "description": "Mikrotik API PHP Library for working with RouterOS API",
    "version": "0.8.0",
    "type": "library",
    "time": "2013-12-03",
    "keywords": ["API", "Mikrotik","RouterOS"],
    "license": "MIT",
    "authors": [
        {
            "name": "Lalu Erfandi Maula Yusnu",
            "email": "nunenuh@gmail.com",
            "homepage": "http://nunenuh.web.id"
        }
    ],
    "autoload": {
        "psr-0": {
            "MikrotikAPI": "src/",
            "MikrotikAPITest": "test/"
        }
    },
    "require": {
        "php": ">=5.3.3"
    }
}


File: /LICENSE
The MIT License (MIT)

Copyright (c) 2013 Lalu Erfandi Maula Yusnu

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


File: /nbproject\project.properties
include.path=${php.global.include.path}
php.version=PHP_53
source.encoding=UTF-8
src.dir=.
tags.asp=false
tags.short=false
web.root=.


File: /nbproject\project.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://www.netbeans.org/ns/project/1">
    <type>org.netbeans.modules.php.project</type>
    <configuration>
        <data xmlns="http://www.netbeans.org/ns/php-project/1">
            <name>mikrotik-api</name>
        </data>
    </configuration>
</project>


File: /src\MikrotikAPI\Commands\File\File.php
<?php

namespace MikrotikAPI\Commands\File;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Mapi_File
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class File {

    /**
     * @access private
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to display all file in mikrotik RouterOs
     * @return type array
     */
    public function get_all_file() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/file/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No File";
        }
    }

    /**
     * This method is used to display one file 
     * in detail based on the id
     * @param type $id string 
     * @return type array
     */
    public function detail_file($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/file/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No File With This id = " . $id;
        }
    }

    /**
     * This method is used to delete file by id
     * @param type $id string
     * @return type array
     */
    public function delete_file($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/file/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\Bonding.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Mapi_interface_Bonding
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class Bonding {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
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
     * $this->mikrotik_api->interfaces()->bonding()->add($param);
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
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bonding/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all interface bonding
     * 
     * Example :
     * 
     * print_r($this->mikrotik_api->interfaces()->bonding()->get_all());
     * @return type array
     */
    public function get_all() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/bonding/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface Bonding To Set, Please Your Add Interface Bonding";
        }
    }

    /**
     * This method is used to enable interface bonding by id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->bonding()->enable('*1');
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bonding/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable interface bonding by id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->bonding()->disable('*1');
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bonding/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
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
     * $this->mikrotik_api->interfaces()->bonding()->set($param, '*1');
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
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bonding/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one interface bonding
     * in detail based on the id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->bonding()->detail('*1');
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/bonding/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface Bonding With This id = " . $id;
        }
    }

    /**
     * This method is used to delete interface bonding by id
     * 
     * $this->mikrotik_api->interfaces()->bonding()->delete('*1');
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bonding/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\Bridge.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Mapi_interface_Bridge
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class Bridge {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for add new interface bridge
     * @param type $param array
     * @return type array
     */
    public function add_bridge($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bridge/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for disable interface bridge
     * @param type $id string
     * @return type array
     */
    public function disable_bridge($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bridge/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for enable interface bridge
     * @param type $id string
     * @return type array
     */
    public function enable_bridge($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bridge/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for delete interface bridge
     * @param type $id string
     * @return type array
     */
    public function delete_bridge($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bridge/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for get all interface bridge
     * @return type array
     */
    public function get_all_bridge() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/bridge/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface Bridge To Set, Please Your Add Interface Bridge";
        }
    }

    /**
     * This method used for set or edit interface bridge
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_bridge($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bridge/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for detail interface bridge
     * @param type $id string
     * @return type array
     */
    public function detail_bridge($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/bridge/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface Bridge With This id = " . $id;
        }
    }

    public function add_bridge_nat($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bridge/nat/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for disable interface bridge
     * @param type $id string
     * @return type array
     */
    public function disable_bridge_nat($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bridge/nat/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for enable interface bridge
     * @param type $id string
     * @return type array
     */
    public function enable_bridge_nat($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bridge/nat/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for delete interface bridge
     * @param type $id string
     * @return type array
     */
    public function delete_bridge_nat($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bridge/nat/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for get all interface bridge
     * @return type array
     */
    public function get_all_bridge_nat() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/bridge/nat/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface Bridge NAT To Set, Please Your Add Interface Bridge NAT";
        }
    }

    /**
     * This method used for set or edit interface bridge
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_bridge_nat($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/bridge/nat/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for detail interface bridge
     * @param type $id string
     * @return type array
     */
    public function detail_bridge_nat($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/bridge/nat/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface Bridge NAT With This id = " . $id;
        }
    }

    /**
     * This method used for set interface Bridge Settings
     * @param type $use_ip_firewall string (default : yes or no)
     * @param type $use_ip_firewall_for_vlan string (default : yes or no)
     * @param type $use_ip_firewall_for_pppoe string (default : yes or no)
     * @return type array
     */
    public function set_bridge_settings($use_ip_firewall, $use_ip_firewall_for_vlan, $use_ip_firewall_for_pppoe) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/bridge/settings/set");
        $sentence->setAttribute("use-ip-firewall", $use_ip_firewall);
        $sentence->setAttribute("use-ip-firewall-for-vlan", $use_ip_firewall_for_vlan);
        $sentence->setAttribute("use-ip-firewall-for-pppoe", $use_ip_firewall_for_pppoe);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for get all interface Bridge Settings
     * @return type array
     */
    public function get_all_bridge_settings() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/bridge/settings/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface Bridge Settings To Set, Please Your Add Interface Bridge Settings";
        }
        return $this->query('');
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\EoIP.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of EoIP
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class EoIP {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
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
     * $this->mikrotik_api->interfaces()->eoip()->add($param);
     * 
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/eoip/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all interface eoip
     * 
     * Example :
     * 
     * print_r($this->mikrotik_api->interfaces()->eoip()->get_all());
     * @return type array
     */
    public function get_all() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/eoip/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface EOIP To Set, Please Your Add Interface EOIP";
        }
    }

    /**
     * This method is used to enable interface eoip by id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->eoip()->enable('*1');
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/eoip/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable interface eoip by id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->eoip()->disable('*1');
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/eoip/disable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to remove interface eoip by id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->eoip()->delete('*1');
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/eoip/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
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
     *  $this->mikrotik_api->interfaces()->eoip()->set($param, '*1');
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/eoip/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one interface eoip 
     * in detail based on the id
     * 
     * Example :
     * 
     * $this->mikrotik_api->interfaces()->eoip()->detail($param, '*1');
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/eoip/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface EOIP With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\Ethernet.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Ethernet
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Ethernet {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to display all interface
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        return $rs->getResultArray();
    }

    /**
     * This method is used to display one interface  
     * in detail based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable interface by id
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable interface by id
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/disable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one interafce 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface Ethernet With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\Interfaces.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Talker\Talker;
use MikrotikAPI\Commands\Interfaces\Bonding,
    MikrotikAPI\Commands\Interfaces\EoIP,
    MikrotikAPI\Commands\Interfaces\Ethernet,
    MikrotikAPI\Commands\Interfaces\IPTunnel,
    MikrotikAPI\Commands\Interfaces\L2TPClient,
    MikrotikAPI\Commands\Interfaces\L2TPServer,
    MikrotikAPI\Commands\Interfaces\PPPClient,
    MikrotikAPI\Commands\Interfaces\PPPServer,
    MikrotikAPI\Commands\Interfaces\PPPoEClient,
    MikrotikAPI\Commands\Interfaces\PPPoEServer,
    MikrotikAPI\Commands\Interfaces\PPTPClient,
    MikrotikAPI\Commands\Interfaces\PPTPServer,
    MikrotikAPI\Commands\Interfaces\VLAN,
    MikrotikAPI\Commands\Interfaces\VRRP;

/**
 * Description of Mapi_Interfaces
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Interfaces {

    /**
     *
     * @var Talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to call class Ethetrnet
     * @return Mapi_Ip 
     */
    public function ethernet() {
        return new Ethernet($this->talker);
    }

    /**
     * This method is used to call class Pppoe_Client
     * @return Mapi_Ip 
     */
    public function PPPoEClient() {
        return new PPPoEClient($this->talker);
    }

    /**
     * This method is used to call class Pppoe_Server
     * @return Mapi_Ip 
     */
    public function PPPoEServer() {
        return new PPPoEServer($this->talker);
    }

    /**
     * This method is used to call class Eoip
     * @return Mapi_Ip 
     */
    public function EoIP() {
        return new EoIP($this->talker);
    }

    /**
     * This method is used to call class Ipip
     * @return Mapi_Ip 
     */
    public function IPTunnel() {
        return new IPTunnel($this->talker);
    }

    /**
     * This method is used to call class Vlan
     * @return Mapi_Ip 
     */
    public function VLAN() {
        return new VLAN($this->talker);
    }

    /**
     * This method is used to call class Vrrp
     * @return Mapi_Ip 
     */
    public function VRRP() {
        return new VRRP($this->talker);
    }

    /**
     * This method is used to call class Bonding
     * @return Mapi_Ip 
     */
    public function bonding() {
        return new Bonding($this->talker);
    }

    /**
     * This method for used call class Bridge
     * @return Mapi_Ip
     */
    public function bridge() {
        return new Bridge($this->talker);
    }

    /**
     * This method used call class L2tp_Client 
     * @return Mapi_Ip
     */
    public function L2TPClient() {
        return new L2TPClient($this->talker);
    }

    /**
     * This method used call class L2tp_Server 
     * @return Mapi_Ip
     */
    public function L2TPServer() {
        return new L2TPServer($this->talker);
    }

    /**
     * This method used call class Ppp_Client 
     * @return Mapi_Ip
     */
    public function PPPClient() {
        return new PPPClient($this->talker);
    }

    /**
     * This method used call class Ppp_Server 
     * @return Mapi_Ip
     */
    public function PPPServer() {
        return new PPPServer($this->talker);
    }

    /**
     * This method used call class Pptp_Client 
     * @return Mapi_Ip
     */
    public function PPTPClient() {
        return new PPTPClient($this->talker);
    }

    /**
     * This method used call class Pptp_Server 
     * @return Mapi_Ip
     */
    public function PPTPServer() {
        return new PPTPServer($this->talker);
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\IPTunnel.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of IPTunnel
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class IPTunnel {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to add interface ipip
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ipip/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all interface ipip
     * @return type array
     */
    public function get_all() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/ipip/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface IPIP To Set, Please Your Add Interface IPIP";
        }
    }

    /**
     * This method is used to enable interface ipip by id
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ipip/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable interface ipip by id
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ipip/disable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to remove interface ipip
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ipip/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit interface ipip by id
     * @param type $param array
     * @param type $id string
     * @return type 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ipip/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one interface ipip 
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/ipip/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface IPIP With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\L2TPClient.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of L2TPClients
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class L2TPClient {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for add new l2tp client
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/l2tp-client/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for disable l2tp client
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/l2tp-client/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for enable l2tp client
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/l2tp-client/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for delete l2tp client
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/l2tp-client/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for detail l2tp client
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/l2tp-client/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface L2TP Client With This id = " . $id;
        }
    }

    /**
     * This method used for set or edit l2tp client
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/l2tp-client/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for get all l2tp client
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/l2tp-client/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface L2TP Client To Set, Please Your Add Interface L2TP Client";
        }
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\L2TPServer.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of L2TPServer
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class L2TPServer {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for add new l2tp server
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/l2tp-server/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for disable l2tp server
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/l2tp-server/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for enable l2tp server
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/l2tp-server/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for delete l2tp server
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/l2tp-server/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for detail l2tp server
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/l2tp-server/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface L2TP Server With This id = " . $id;
        }
    }

    /**
     * This method used for set or edit l2tp server
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/l2tp-server/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for get all l2tp server
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/l2tp-server/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface L2TP Server To Set, Please Your Add Interface L2TP Server";
        }
    }

    /**
     * This method used for get all l2tp server server
     * @return type array
     */
    public function getAllServer() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/l2tp-server/server/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface L2TP Server Server To Set, Please Your Add Interface L2TP Server Server";
        }
    }

    /**
     * This method used for set l2tp server server
     * @param type $param array
     * @return type array
     */
    public function setServer($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/l2tp-server/server/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\PPPClient.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of PPPClient
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class PPPClient {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for add new interface ppp-client
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ppp-client/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for disable interface ppp-client
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ppp-client/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for enable interface ppp-client
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ppp-client/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for delete interface ppp-client
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ppp-client/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for detail interface ppp-client
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/ppp-client/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPP Client With This id = " . $id;
        }
    }

    /**
     * This method used for set or edit interface ppp-client
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ppp-client/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for get all interface ppp-client
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/ppp-client/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPP Client To Set, Please Your Add Interface PPP Client";
        }
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\PPPoEClient.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of PPPoEClient
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class PPPoEClient {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to add pppoe-client
     * @param type $param array
     * @return type array
     * 
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pppoe-client/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all pppoe-client 
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/pppoe-client/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPPoE-Client To Set, Please Your Add PPPoE-Client";
        }
    }

    /**
     * This method is used to enable pppoe-client by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pppoe-client/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable pppoe-client by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pppoe-client/disable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to delete pppoe-client by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pppoe-client/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pppoe-client/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one pppoe-client
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/pppoe-client/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPPoE-Client With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\PPPoEServer.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Mapi_Interface_Pppoe_Server
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class PPPoEServer {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to add pppoe-server
     * @param type $param array
     * @return type array
     * 
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pppoe-server/server/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable pppoe-server by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pppoe-server/server/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable pppoe-server by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pppoe-server/server/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pppoe-server/server/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to delete pppoe-server by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pppoe-server/server/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all pppoe-server
     * @return type array
     * 
     */
    public function get_all() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/pppoe-server/server/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPPoE-Server Server To Set, Please Your Add Interface PPPoE-Server Server";
        }
    }

    /**
     * This method is used to display one pppoe-server 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/pppoe-server/server/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPPoE-Server Server With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\PPPServer.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of PPPServer
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class PPPServer {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for add new interface ppp-sever
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ppp-server/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for disable interface ppp-sever
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ppp-server/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for enable interface ppp-sever
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ppp-server/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for delete interface ppp-sever
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ppp-server/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for detail interface ppp-sever
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/ppp-server/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPP Server With This id = " . $id;
        }
    }

    /**
     * This method used for set or edit interface ppp-sever
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/ppp-server/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for get all interface ppp-sever
     * @return array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/ppp-server/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPP Server To Set, Please Your Add Interface PPP Server";
        }
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\PPTPClient.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Mapi_interface
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class PPTPClient {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for add new interface pptp-client
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pptp-client/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for disable interface pptp-client
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pptp-client/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for enable interface pptp-client
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pptp-client/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for delete interface pptp-client
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pptp-client/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for detail interface pptp-client
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/pptp-client/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPTP Client With This id = " . $id;
        }
    }

    /**
     * This method used for set or edit interface pptp-client
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pptp-client/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for get all interface pptp-client
     * @return type array
     */
    public function get_all() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/pptp-client/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPTP Client To Set, Please Your Add Interface PPTP Client";
        }
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\PPTPServer.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Mapi_Interface_Pptp_Server
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class PPTPServer {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for add new interface pptp-server
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pptp-server/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for disable interface pptp-server
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pptp-server/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for enable interface pptp-server
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pptp-server/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for delete interface pptp-server
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pptp-server/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for detail interface pptp-server
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/pptp-server/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPTP Server With This id = " . $id;
        }
    }

    /**
     * This method used for set or edit interface pptp-server
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pptp-server/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for get all interface pptp-server
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/pptp-server/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPTP Server To Set, Please Your Add Interface PPTP Server";
        }
    }

    /**
     * This method used for get all pptp-server server
     * @return type array
     */
    public function getAllServer() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("//interface/pptp-server/server/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface PPTP Server Server To Set, Please Your Add Interface PPTP Server Server";
        }
    }

    /**
     * This method used for set pptp-server server
     * @param type $param array
     * @return type array
     */
    public function setServer($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/pptp-server/server/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\VLAN.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of VLAN
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class VLAN {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to add vlan
     * @param type $param array
     * @return type array
     * 
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/vlan/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all vlan
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/vlan/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface VLAN To Set, Please Your Add Interface VLAN";
        }
    }

    /**
     * This method is used to enable vlan by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/vlan/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable vlan by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/vlan/disable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to delete vlan by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/vlan/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/vlan/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one vlan
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/vlan/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface VLAN With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\Interfaces\VRRP.php
<?php

namespace MikrotikAPI\Commands\Interfaces;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Mapi_Interface_Vrrp
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class VRRP {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to to add vrrp
     * @param type $param array
     * @return type array
     * 
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/vrrp/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all vrrp
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/vrrp/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface VRRP To Set, Please Your Add Interface VRRP";
        }
    }

    /**
     * This method is used to to enable vrrp by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/vrrp/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to to disable vrrp by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/vrrp/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to to delete vrrp by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/vrrp/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to change based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/interface/vrrp/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one vrrp
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/interface/vrrp/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Interface VRRP With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Accounting.php
<?php

namespace MikrotikAPI\Commands\IP;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Mapi_Ip_Accounting
 * 
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Accounting {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to set or edit ip accountng
     * @param type $account_local_traffic string
     * @param type $enabled string
     * @param type $threshold string
     * @return type array
     */
    public function setAccounting($account_local_traffic, $enabled, $threshold) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/accounting/set");
        $sentence->setAttribute("account-local-traffic", $account_local_traffic);
        $sentence->setAttribute("enabled", $enabled);
        $sentence->setAttribute("threshold", $threshold);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all accounting
     * @return type array
     * 
     */
    public function getAll_accounting() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand('/ip/accounting/getall');
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Accounting To Set, Please Your Add Ip Accounting";
        }
    }

    /**
     * This method is used to display all snapshot
     * @return type array
     * 
     */
    public function get_all_snapshot() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand('/ip/accounting/snapshot/getall');
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Accounting Snapshot To Set, Please Your Add Ip Accounting Snapshot";
        }
    }

    /**
     * This method is used to display all uncounted
     * @return type array
     * 
     */
    public function get_all_uncounted() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand('/ip/accounting/uncounted/getall');
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Accounting Uncounted To Set, Please Your Add Ip Accounting Uncounted";
        }
    }

    /**
     * This method is used to display all web-acces
     * @return type array
     * 
     */
    public function get_all_web_access() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand('/ip/accounting/web-access/getall');
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Accounting web-access To Set, Please Your Add Ip Accounting web-access";
        }
    }

    /**
     * This method is used to ip accounting set web-acces
     * @param type $accessible_via_web string default : yes or no
     * @return type array
     * 
     */
    public function set_web_access($accessible_via_web) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/accounting/web-access/set");
        $sentence->setAttribute("accessible-via-web", $accessible_via_web);
        $sentence->setAttribute("address", "0.0.0.0/0");
        $this->talker->send($sentence);
        return "Sucsess";
    }

}


File: /src\MikrotikAPI\Commands\IP\Address.php
<?php

namespace MikrotikAPI\Commands\IP;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Address
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Address {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to add the ip address
     * @param type $address string
     * @param type $interface string
     * @param type $comment string
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/address/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all ip address
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/address/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Address To Set, Please Your Add Ip Address";
        }
    }

    /**
     * This method is used to activate the ip address by id
     * @param type $id is not an array
     * @return type array
     * 
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/address/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable ip address by id
     * @param type $id string 
     * @return type array
     * 
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/address/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to remove the ip address by id
     * @param type $id is not an array
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/address/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/address/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one ip address 
     * in detail based on the id
     * @param type $id not string
     * @return type array
     * 
     */
    public function detail_address($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/address/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Address With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\ARP.php
<?php

namespace MikrotikAPI\Commands\IP;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of ARP
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class ARP {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to add arp
     * @param type $param array
     * @return type array
     * j
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/arp/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to delete arp by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/arp/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable arp by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/arp/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable arp by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/arp/disable");
        $sentence->where(".id", "=", $id);
        $disable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/arp/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all arp
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/arp/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip ARP To Set, Please Your Add Ip ARP";
        }
    }

    /**
     * This method is used to display arp
     * in detail based on the id
     * @param type $id string
     * @return type array
     *  
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/arp/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip ARP With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\DHCPClient.php
<?php

namespace MikrotikAPI\Commands\IP;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Mapi_Ip_Dhcp_Client
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 * @property talker $talker
 */
class DHCPClient {

    /**
     *
     * @var type 
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to add dhcp client
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-client/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable dhcp client by id
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-client/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable dhcp client by id
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-client/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to renew dhcp client  by id
     * @param type $id string
     * @return type array
     */
    public function renew_dhcp_client($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-client/renew");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to release dhcp client by id
     * @param type $id string
     * @return type array
     */
    public function release_dhcp_client($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-client/release");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit dhcp client by id
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set_dhcp_client($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-client/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to remove dhcp client by id
     * @param type $id string
     * @return type array
     */
    public function delete_dhcp_client($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-client/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all dhcp client
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dhcp-client/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Dhcp-Client To Set, Please Your Add Ip Dhcp-Client";
        }
    }

    /**
     * This method is used to display one ip dhcp client
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dhcp-client/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Dhcp-Client With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\DHCPRelay.php
<?php

namespace MikrotikAPI\Commands\IP;

use Mikrotik\API\Talker\Talker,
    Mikrotik\API\Util\SentenceUtil;

/**
 * Description of DHCPRelay
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class DHCPRelay {

    /**
     *
     * @var \MikrotikAPI\Talker\Talker 
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to ip add dhcp relay
     * @param type $param array 
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-relay/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable ip dhcp relay by id
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-relay/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable ip dhcp relay by id
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-relay/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit ip dhcp relay by id
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-relay/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to remove ip dhcp relay by id
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-relay/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one interface bonding
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dhcp-relay/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Dhcp-Relay With This id = " . $id;
        }
    }

    /**
     * This method is used to display all ip dhcp relay
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dhcp-relay/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Dhcp-Relay To Set, Please Your Add Ip Dhcp-Relay";
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\DHCPServer.php
<?php

namespace MikrotikAPI\Commands\IP;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Mapi_Ip_Dhcp_Server
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class DHCPServer {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This methode is used to add ip dhcp server network
     * @param type $param array
     * @return type array
     */
    public function addNetwork($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-server/network/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This methode is used to add ip dhcp server
     * @param type $param array
     * @return type \array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-server/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This methode is used to set ip dhcp server config
     * @param type $store_leases_disk string
     * @return type array
     */
    public function setConfig($store_leases_disk) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-server/config/set");
        $sentence->setAttribute("store-leases-disk", $store_leases_disk);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This methode is used to set or edit ip dhcp server network
     * by id
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function setNetwork($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-server/network/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This methode is used to display all ip dhcp server network
     * @return type array
     */
    public function getAllNetwork() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dhcp-server/network/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Dhcp-Server Network To Set, Please Your Add Ip Dhcp-Server Network";
        }
    }

    /**
     * This methode is used to delete ip dhcp server network by id
     * @param type $id string
     * @return type array
     */
    public function deleteNetwork($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-server/network/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one ip dhcp server network
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dhcp-server/network/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Dhcp-Server Network With This id = " . $id;
        }
    }

    /**
     * This methode is used to disable ip dhcp server by id
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-server/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This methode is used to enable ip dhcp server by id
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-server/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This methode is used to remove ip dhcp server by id
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-server/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This methode is used to det or edit ip dhcp server by id
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dhcp-server/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This methode is used to display all ip dhcp server
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dhcp-server/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Dhcp-Server To Set, Please Your Add Ip Dhcp-Server";
        }
    }

    /**
     * This method is used to display one ip dhcp server
     * in detail based on the id
     * @param type $id string
     * @return type  array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dhcp-server/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Dhcp-Server With This id = " . $id;
        }
    }

    public function getAllConfig() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dhcp-server/config/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Dhcp-Server Config To Set, Please Your Add Ip Dhcp-Server Config";
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\DNS.php
<?php

namespace MikrotikAPI\Commands\IP;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Mapi_Ip_Dns
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class DNS{
    /**
     *
     * @var type array
     */
    private $talker;
    
    function __construct(Talker $talker){
        $this->talker = $talker;
    }
    
   /**
    * This method is used to configure dns
    * @param type $servers string example : '192.168.1.1,192.168.2.1'
    * @return type array
    * 
    */
    public function set($servers){
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dns/set");
        $sentence->setAttribute("servers", $servers);
        $this->talker->send($sentence);
        return "Sucsess";
    }
    
    /**
     * This method is used to display
     * all dns
     * @return type array
     * 
     */
    public function getAll(){
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dns/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()){
            return $rs->getResultArray();
        }else{
            return "No Ip DNS To Set, Please Your Add Ip DNS";
        }
    }
     
    /**
     * This method is used to add the static dns
     * @param type $param array
     * @return type array
     * 
     */
    public function addStatic($param){
       $sentence = new SentenceUtil();
       $sentence->addCommand("/ip/dns/static/add");
       foreach ($param as $name => $value){
               $sentence->setAttribute($name, $value);
       }       
       $this->talker->send($sentence);
       return "Sucsess";
    }
   /**
    * This method is used to display
    * all static dns
    * @return type array
    * 
    */
    public function getAllStatic(){
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dns/static/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()){
            return $rs->getResultArray();
        }else{
            return "No Ip Static DNS To Set, Please Your Add Ip Static DNS";
        }
    }
    
    /**
     * This method is used to display one static dns 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
     public function detailStatic($id){
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dns/static/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0 ;
        if ($i < $rs->size()){
            return $rs->getResultArray();
        }  else {
            return "No Ip Static DNS With This Id = ".$id;
        }
    }
    
    /**
     * This method is used to change based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function setStatic($param, $id){
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/dns/static/set");
        foreach ($param as $name => $value){
                $sentence->setAttribute($name, $value);
         }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

     /**
     * This method is used to display
     * all dns cache
     * @return array || string
     * 
     */
    public function getAllCache(){
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dns/cache/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()){
            return $rs->getResultArray();
        }else{
            return "No Ip DNS Cache To Set, Please Your Add Ip DNS Cache";
        }
    }
    
    /**
     * This method is used to display one dns cache 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
     public function detailCache($id){
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dns/cache/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0 ;
        if ($i < $rs->size()){
            return $rs->getResultArray();
        }  else {
            return "No Ip DNS Cache With This Id = ".$id;
        }
    }
    
    /**
     * This method is used to display
     * all dns cache all cache
     * @return type array
     * 
     */
    public function getAllCacheAll(){
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dns/cache/all/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()){
            return $rs->getResultArray();
        }else{
            return "No Ip DNS Cache All To Set, Please Your Add Ip DNS Cache All";
        }
    }
    
     /**
     * This method is used to display one dns cache all 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
     public function detailCacheAll($id){
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/dns/cache/all/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0 ;
        if ($i < $rs->size()){
            return $rs->getResultArray();
        }  else {
            return "No Ip DNS Cache All With This Id = ".$id;
        }
    }
}


File: /src\MikrotikAPI\Commands\IP\Firewall\Firewall.php
<?php

namespace MikrotikAPI\Commands\IP\Firewall;

use MikrotikAPI\Talker\Talker;
use MikrotikAPI\Commands\IP\Firewall\Filter,
    MikrotikAPI\Commands\IP\Firewall\NAT,
    MikrotikAPI\Commands\IP\Firewall\Mangle,
    MikrotikAPI\Commands\IP\Firewall\ServicePort,
    MikrotikAPI\Commands\IP\Firewall\Connection,
    MikrotikAPI\Commands\IP\Firewall\AddressList,
    MikrotikAPI\Commands\IP\Firewall\Layer7Protocol;

/**
 * Description of Firewall
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class Firewall {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Firewall\Filter
     */
    public function filter() {
        return new Filter($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Firewall\NAT
     */
    public function NAT() {
        return new NAT($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Firewall\Mangle
     */
    public function mangle() {
        return new Mangle($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Firewall\ServicePort
     */
    public function servicePort() {
        return new ServicePort($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Firewall\Connection
     */
    public function connection() {
        return new Connection($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Firewall\AddressList
     */
    public function addressList() {
        return new AddressList($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Firewall\Layer7Protocol
     */
    public function layer7Protocol() {
        return new Layer7Protocol($this->talker);
    }

}


File: /src\MikrotikAPI\Commands\IP\Firewall\FirewallAddressList.php
<?php

namespace MikrotikAPI\Commands\IP\Firewall;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of AddressList
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyrigh Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class FirewallAddressList {

    /**
     *
     * @var Talker $talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     *
     * @param type $param array
     * @return type array
     * This method is used to add address list
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/address-list/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all firewall filter
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/address-list/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Firewall Address List To Set, Please Your Add IP Firewall Address List ";
        }
    }

    /**
     * This method is used to enable firewall filter by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/address-list/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable firewall filter by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/address-list/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to remove firewall filter by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/address-list/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to change firewall nat based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/address-list/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one firewall filter
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/address-list/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Firewall Address List With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Firewall\FirewallConnection.php
<?php

namespace MikrotikAPI\Commands\IP\Firewall;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Connection
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class FirewallConnection {

    /**
     *
     * @var Talker $talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for get all firewall connection
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/connection/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Firewall Connection To Set, Please Your Add Ip Firewall Connection";
        }
    }

    /**
     * This method used for delete firewall connection
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/connection/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

}


File: /src\MikrotikAPI\Commands\IP\Firewall\FirewallFilter.php
<?php

namespace MikrotikAPI\Commands\IP\Firewall;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Filter
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class FirewallFilter {

    /**
     *
     * @var Talker $talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     *
     * @param type $param array
     * @return type array
     * This method is used to add the firewall filter
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/filter/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all firewall filter
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/filter/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Firewall Filter To Set, Please Your Add Ip Firewall Filter";
        }
    }

    /**
     * This method is used to enable firewall filter by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/filter/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable firewall filter by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/filter/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to remove firewall filter by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/filter/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to change firewall nat based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/filter/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one firewall filter
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/filter/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Firewall Filter With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Firewall\FirewallLayer7Protocol.php
<?php

namespace MikrotikAPI\Commands\IP\Firewall;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Layer7Protocol
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class FirewallLayer7Protocol {

    /**
     *
     * @var Talker $talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     *
     * @param type $param array
     * @return type array
     * This method is used to add layer7 protocol
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/layer7-protocol/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all layer7 protocol
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/layer7-protocol/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Firewall Address List To Set, "
                    . "Please Your Add IP Firewall Layer7 Protocol ";
        }
    }

    /**
     * This method is used to enable firewall layer7 protocol by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/layer7-protocol/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable firewall layer7 protocol by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/layer7-protocol/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to remove firewall layer7 protocol by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/layer7-protocol/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to change firewall layer7 protocol based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/layer7-protocol/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one layer7 protocol
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/layer7-protocol/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Firewall Layer7 Protocol With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Firewall\FirewallMangle.php
<?php

namespace MikrotikAPI\Commands\IP\Firewall;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Mangle
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 * 
 */
class FirewallMangle {

    /**
     *
     * @var Talker $talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for add new Ip Firewall Mangle 
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/mangle/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for disable Ip Firewall Mangle
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/mangle/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for enable Ip Firewall Mangle
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/mangle/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for delete Ip Firewall Mangle
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/mangle/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for detail Ip Firewall Mangle
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/mangle/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Firewall Mangle With This id = " . $id;
        }
    }

    /**
     * This method used for set or edit Ip Firewall Mangle
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/mangle/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for get all Ip Firewall Mangle
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/mangle/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Firewall Mangle To Set, Please Your Add Ip Firewall Mangle";
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Firewall\FirewallNAT.php
<?php

namespace MikrotikAPI\Commands\IP\Firewall;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of NAT
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 * 
 */
class FirewallNAT {

    /**
     *
     * @var Talker $talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to add the firewall nat
     * @param type $param array
     * @return type array
     * 
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/nat/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable firewall nat by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/nat/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable firewall nat by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/nat/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to change firewall nat based on the id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/nat/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to remove firewall nat
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/nat/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all firewall nat
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/nat/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Firewall NAT To Set, Please Your Add Ip Firewall NAT";
        }
    }

    /**
     * This method is used to display one firewall nat 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/nat/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Firewall NAT With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Firewall\FirewallServicePort.php
<?php

namespace MikrotikAPI\Commands\IP\Firewall;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of ServicePort
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class FirewallServicePort {

    /**
     *
     * @var Talker $talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for get all Ip Firewall Service Port
     * @return array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/service-port/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Firewall service-port To Set, Please Your Add Ip Firewall service-port";
        }
    }

    /**
     * This method used for disable Ip Firewall Service Port
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/service-port/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for enable Ip Firewall Service Port
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/firewall/service-port/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     *
     * @param type $id string 
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/firewall/service-port/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Firewall Service-Port With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Hotspot\Hotspot.php
<?php

namespace MikrotikAPI\Commands\IP\Hotspot;

use MikrotikAPI\Talker\Talker;
use MikrotikAPI\Commands\IP\Hotspot\Server,
    MikrotikAPI\Commands\IP\Hotspot\ServerProfiles,
    MikrotikAPI\Commands\IP\Hotspot\Users,
    MikrotikAPI\Commands\IP\Hotspot\UserProfile,
    MikrotikAPI\Commands\IP\Hotspot\Hosts,
    MikrotikAPI\Commands\IP\Hotspot\Active,
    MikrotikAPI\Commands\IP\Hotspot\IPBindings,
    MikrotikAPI\Commands\IP\Hotspot\Cookie;

/**
 * Description of Hotspot
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class Hotspot {

    /**
     *
     * @var Talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Hotspot\Server
     */
    public function server() {
        return new Server($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Hotspot\ServerProfiles
     */
    public function serverProfiles() {
        return new ServerProfiles($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Hotspot\Users
     */
    public function users() {
        return new Users($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Hotspot\UserProfile
     */
    public function userProfiles() {
        return new UserProfile($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Hotspot\Active
     */
    public function active() {
        return new Active($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Hotspot\Hosts
     */
    public function hosts() {
        return new Hosts($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Hotspot\IPBindings
     */
    public function IPBinding() {
        return new IPBindings($this->talker);
    }

    /**
     * 
     * @return \MikrotikAPI\Commands\IP\Hotspot\Cookie
     */
    public function cookie() {
        return new Cookie($this->talker);
    }

}


File: /src\MikrotikAPI\Commands\IP\Hotspot\HotspotActive.php
<?php

namespace Mikrotik\Commands\IP\Hotspot;

use Mikrotik\API\Talker\Talker,
    Mikrotik\API\Util\SentenceUtil;

/**
 * Description of Active
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class HotspotActive {

    /**
     *
     * @var Talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This function is used to add active
     * @return array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/active/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to delete hotspot by id
     * @param string $id 
     * @return array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/active/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all hotspot
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/active/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot Active To Set, Please Your Add IP Hotspot Active";
        }
    }

    /**
     * This method is used to display hotspot
     * in detail based on the id
     * @param string $id
     * @return type array
     *  
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/active/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot Active With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Hotspot\HotspotCookies.php
<?php

namespace Mikrotik\Commands\IP\Hotspot;

use Mikrotik\API\Talker\Talker,
    Mikrotik\API\Util\SentenceUtil;

/**
 * Description of Cookie
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category name
 */
class HotspotCookie {

    /**
     *
     * @var Talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to delete hotspot cookie by id
     * @param string $id
     * @return string
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/cookie/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all cookie on hotspot
     * @return array or string
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/cookie/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot Cookie To Set, Please Your Add IP Hotspot Cookie";
        }
    }

    /**
     * This method is used to display hotspot cookie
     * in detail based on the id
     * @param string $id 
     * @return  array
     *  
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/cookie/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot Cookie With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Hotspot\HotspotHosts.php
<?php

namespace Mikrotik\Commands\IP\Hotspot;

use Mikrotik\API\Talker\Talker,
    Mikrotik\API\Util\SentenceUtil;

/**
 * Description of Hosts
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class HotspotHosts {

    /**
     *
     * @var Talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to delete hotspot by id
     * @param string $id 
     * @return array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/host/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all hotspot
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/host/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot Host To Set, Please Your Add IP Hotspot Host";
        }
    }

    /**
     * This method is used to display hotspot host
     * in detail based on the id
     * @param string $id
     * @return type array
     *  
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/host/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot Host With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Hotspot\HotspotIPBindings.php
<?php

namespace Mikrotik\Commands\IP\Hotspot;

use Mikrotik\API\Talker\Talker,
    Mikrotik\API\Util\SentenceUtil;

/**
 * Description of IPBindings
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category name
 */
class HotspotIPBindings {

    /**
     *
     * @var Talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This function is used to add hotspot ip binding
     * @return string
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/ip-binding/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to delete hotspot ip binding by id
     * @param string $id
     * @return string
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/ip-binding/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable hotspot ip binding by id
     * @param type $id string
     * @return string
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/ip-binding/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable hotspot ip binding by id
     * @param string $id
     * @return string
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/ip-binding/disable");
        $sentence->where(".id", "=", $id);
        $disable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit by id
     * @param array $param
     * @param string $id
     * @return string
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/ip-binding/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all ip binding on hotspot
     * @return array or string
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/ip-binding/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot IP Binding To Set, Please Your Add IP Hotspot IP Binding";
        }
    }

    /**
     * This method is used to display hotspot ip binding
     * in detail based on the id
     * @param string $id 
     * @return  array
     *  
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/ip-binding/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot IP Binding With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Hotspot\HotspotServer.php
<?php

namespace Mikrotik\Commands\IP\Hotspot;

use Mikrotik\API\Talker\Talker,
    Mikrotik\API\Util\SentenceUtil;

/**
 * Description of Server
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class HotspotServer {

    /**
     *
     * @var Talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This function is used to add hotspot
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to delete hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/disable");
        $sentence->where(".id", "=", $id);
        $disable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all hotspot
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot To Set, Please Your Add IP Hotspot";
        }
    }

    /**
     * This method is used to display hotspot
     * in detail based on the id
     * @param type $id string
     * @return type array
     *  
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Hotspot\HotspotServerProfiles.php
<?php

namespace Mikrotik\Commands\IP\Hotspot;

use Mikrotik\API\Talker\Talker,
    Mikrotik\API\Util\SentenceUtil;

/**
 * Description of ServerProfiles
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class HotspotServerProfiles {

    /**
     *
     * @var Talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This function is used to add hotspot profile
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/profile/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to delete hotspot profile by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/profile/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable hotspot profile by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/profile/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable hotspot profile by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/profile/disable");
        $sentence->where(".id", "=", $id);
        $disable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/profile/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all hotspot profile
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/profile/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot Profile To Set, Please Your Add IP Hotspot Profile";
        }
    }

    /**
     * This method is used to display hotspot
     * in detail based on the id
     * @param type $id string
     * @return type array
     *  
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/profile/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot Profile With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Hotspot\HotspotUserProfiles.php
<?php

namespace Mikrotik\Commands\IP\Hotspot;

use Mikrotik\API\Talker\Talker,
    Mikrotik\API\Util\SentenceUtil;

/**
 * Description of UsersProfile
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category name
 */
class HotspotUserProfile {

    /**
     *
     * @var Talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This function is used to add hotspot user p
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/user/profile/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to delete hotspot user profile by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/user/profile/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable hotspot user profile by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/user/profile/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable hotspot user profile by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/user/profile/disable");
        $sentence->where(".id", "=", $id);
        $disable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/user/profile/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all hotspot user profile
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/user/profile/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot User Profile To Set, Please Your Add IP Hotspot User Profile";
        }
    }

    /**
     * This method is used to display hotspot user profile
     * in detail based on the id
     * @param string $id
     * @return array
     *  
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/user/profile/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot User Profile With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Hotspot\HotspotUsers.php
<?php

namespace Mikrotik\Commands\IP\Hotspot;

use Mikrotik\API\Talker\Talker,
    Mikrotik\API\Util\SentenceUtil;

/**
 * Description of Users
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category name
 */
class HotspotUsers {

    /**
     *
     * @var Talker
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This function is used to add hotspot
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/user/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to delete hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/user/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/user/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/user/disable");
        $sentence->where(".id", "=", $id);
        $disable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to reset uptime and trafic counters for hotspot by id
     * @param type $id string
     * @return type array
     * 
     */
    public function resetCounter($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/user/reset-counter");
        $sentence->where(".id", "=", $id);
        $disable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/hotspot/user/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all hotspot
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/user/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot User To Set, Please Your Add IP Hotspot User";
        }
    }

    /**
     * This method is used to display hotspot
     * in detail based on the id
     * @param type $id string
     * @return type array
     *  
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/hotspot/user/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Hotspot User With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\IP.php
<?php

namespace MikrotikAPI\Commands\IP;

use MikrotikAPI\Talker\Talker;
use MikrotikAPI\Commands\IP\Address,
    MikrotikAPI\Commands\IP\Hotspot\Hotspot,
    MikrotikAPI\Commands\IP\Pool,
    MikrotikAPI\Commands\IP\DNS,
    MikrotikAPI\Commands\IP\Firewall\Firewall,
    MikrotikAPI\Commands\IP\Accounting,
    MikrotikAPI\Commands\IP\ARP,
    MikrotikAPI\Commands\IP\DHCPClient,
    MikrotikAPI\Commands\IP\DHCPServer,
    MikrotikAPI\Commands\IP\DHCPRelay,
    MikrotikAPI\Commands\IP\Route,
    MikrotikAPI\Commands\IP\Service,
    MikrotikAPI\Commands\IP\WebProxy;

/**
 * Description of IP
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	 Libraries
 */
class IP {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\Address
     * @return \MikrotikAPI\Commands\IP\Address
     */
    public function address() {
        return new Address($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\Hotspot\Hotspot
     * @return \MikrotikAPI\Commands\IP\Hotspot\Hotspot
     */
    public function hotspot() {
        return new Hotspot($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\Pool
     * @return \MikrotikAPI\Commands\IP\Pool
     */
    public function pool() {
        return new Pool($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\DNS
     * @return \MikrotikAPI\Commands\IP\DNS
     */
    public function DNS() {
        return new DNS($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\Firewall\Firewall
     * @return \MikrotikAPI\Commands\IP\Firewall\Firewall
     */
    public function firewall() {
        return new Firewall($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\Accounting
     * @return \MikrotikAPI\Commands\IP\Accounting
     */
    public function accounting() {
        return new Accounting($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\ARP
     * @return \MikrotikAPI\Commands\IP\ARP
     */
    public function ARP() {
        return new ARP($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\DHCPClient
     * @return \MikrotikAPI\Commands\IP\DHCPClient
     */
    public function DHCPClient() {
        return new DHCPClient($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\DHCPRelay
     * @return \MikrotikAPI\Commands\IP\DHCPRelay
     */
    public function DHCPRelay() {
        return new DHCPRelay($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\DHCPServer
     * @return \MikrotikAPI\Commands\IP\DHCPServer
     */
    public function DHCPServer() {
        return new DHCPServer($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\Route
     * @return \MikrotikAPI\Commands\IP\Route
     */
    public function route() {
        return new Route($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\Service
     * @return \MikrotikAPI\Commands\IP\Service
     */
    public function service() {
        return new Service($this->talker);
    }

    /**
     * This method is use for call instantiate object of class
     * \MikrotikAPI\Commands\IP\WebProxy
     * @return \MikrotikAPI\Commands\IP\WebProxy
     */
    public function proxy() {
        return new WebProxy($this->talker);
    }

}


File: /src\MikrotikAPI\Commands\IP\Pool.php
<?php

namespace MikrotikAPI\Commands\IP;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Pool
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class Pool {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to add pool
     * @param array $param 
     * @return array
     * 
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/pool/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display
     * all pool
     * @return array or string
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand('/ip/pool/getall');
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No IP Pool To Set, Please Your Add Ip Pool";
        }
    }

    /**
     * This method is used to remove the pool by id
     * @param string $id
     * @return array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/pool/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to change pool based on the id
     * @param array $param
     * @param string $id
     * @return array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/pool/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one pool 
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/pool/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Pool With This Id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Route.php
<?php

namespace MikrotikAPI\Commands\IP;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Route
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Route {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to display all ip route
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/route/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Route To Set, Please Your Add Ip Route";
        }
        return $this->query('');
    }

    /**
     * This method is used to add ip route gateway
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/route/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * Can change or disable only static routes
     * @param type $id is not array 
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/route/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * Can change or enable only static routes
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/route/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * Can change or remove only static routes
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/route/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * Can change only static routes
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/route/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one ip route
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/route/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Route With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\IP\Service.php
<?php

namespace MikrotikAPI\Commands\IP;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/**
 * Description of Service
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class Service {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This methode is used to display all ip service
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/service/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Service To Set, Please Your Add Ip Service";
        }
    }

    /**
     * This methode is used to enable ip service by id
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/service/enable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This methode is used to disable ip service by id
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/service/disable");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one ip service
     * in detail based on the id
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/service/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Service With This id = " . $id;
        }
    }

    /**
     * 
     * @param array $param
     * @param string $id
     * @return string
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/service/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

}


File: /src\MikrotikAPI\Commands\IP\WebProxy.php
<?php

namespace MikrotikAPI\Commands\IP;

use MikrotikAPI\Talker\Talker,
    MikrotikAPI\Util\SentenceUtil;

/* Description of WebProxy
 * 
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */

class WebProxy {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for get all web proxy config
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ip/proxy/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No Ip Proxy To Set, Please Your Add Ip Proxy";
        }
    }

    /**
     *
     * This method used for set Web Proxy configuration
     * @param array $param
     * @return array
     */
    public function set($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/proxy/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

}


File: /src\MikrotikAPI\Commands\PPP\AAA.php
<?php

namespace MikrotikAPI\Commands\PPP;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description  AAA
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class AAA {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to display all ppp aaa
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ppp/aaa/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No PPP AAA To Set, Please Your Add PPP AAA";
        }
    }

    /**
     * This method is used to set ppp aaa
     * @param type $use_radius string
     * @param type $accounting string
     * @param type $interim_update string
     * @return type array
     */
    public function set($use_radius, $accounting, $interim_update) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ppp/aaa/set");
        $sentence->setAttribute("use-radius", $use_radius);
        $sentence->setAttribute("accounting", $accounting);
        $sentence->setAttribute("interim-update", $interim_update);
        $this->talker->send($sentence);
        return "Sucsess";
    }

}


File: /src\MikrotikAPI\Commands\PPP\Active.php
<?php

namespace MikrotikAPI\Commands\PPP;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Active
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Active {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to display all ppp active
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ppp/active/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No PPP Active To Set, Please Your Add PPP Active";
        }
    }

    /**
     * This method is used to delete ppp active
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ppp/active/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

}


File: /src\MikrotikAPI\Commands\PPP\PPP.php
<?php

namespace MikrotikAPI\Commands\PPP;

use MikrotikAPI\Talker\Talker;
use MikrotikAPI\Commands\PPP\Active,
    MikrotikAPI\Commands\PPP\Secret,
    MikrotikAPI\Commands\PPP\AAA,
    MikrotikAPI\Commands\PPP\Profile;

/**
 * Description of Mapi_Ppp
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class PPP {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method for call class Profile
     * @return Object of Profile class
     */
    public function profile() {
        return new Profile($this->talker);
    }

    /**
     * This method for call class Secret
     * @return Object of Secret
     */
    public function secret() {
        return new Secret($this->talker);
    }

    /**
     * This method for call class Aaa
     * @access public
     * @return object of Aaa class
     */
    public function AAA() {
        return new AAA($this->talker);
    }

    /**
     * This method for call class Active
     * @return Object of Active class
     */
    public function active() {
        return new Active($this->talker);
    }

}


File: /src\MikrotikAPI\Commands\PPP\Profile.php
<?php

namespace MikrotikAPI\Commands\PPP;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Mapi_Ppp_Profile
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Profile {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to add ppp profile
     * @param type $param array
     * @return type array
     * 
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ppp/profile/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all ppp profile
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ppp/profile/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No PPP Profile To Set, Please Your Add PPP Profile";
        }
    }

    /**
     * This method is used to remove ppp profile by id
     * @param type $id string
     * @return type array
     * 
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ppp/profile/remove");
        $sentence->where(".id", "=", $id);
        $enable = $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit ppp profile by id
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ppp/profile/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display one ppp profile
     * in detail based on the id
     * @param type $id string
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ppp/profile/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No PPP Profile With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\PPP\Secret.php
<?php

namespace MikrotikAPI\Commands\PPP;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Mapi_Ppp_Secret
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class Secret {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to add ppp secret
     * @param type $param array
     * @return type array
     * 
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ppp/secret/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to disable ppp secret
     * @param type $id string
     * @return type array
     * 
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ppp/secret/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to enable ppp secret
     * @param type $id string
     * @return type array
     * 
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ppp/secret/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to set or edit ppp secret
     * @param type $param array
     * @param type $id string
     * @return type array
     * 
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ppp/secret/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to delete ppp secret
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ppp/secret/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all ppp secret
     * @return type array
     * 
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ppp/secret/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No PPP Secret To Set, Please Your Add PPP Secret";
        }
    }

    /**
     * This method is used to display one ppp secret 
     * in detail based on the id
     * @param type $id not array, harus di deklarasikan
     * @return type array
     * 
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/ppp/secret/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No PPP Secret With This id = " . $id;
        }
    }

}


File: /src\MikrotikAPI\Commands\System\System.php
<?php

namespace MikrotikAPI\Commands\System;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Mapi_System
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class System {

    /**
     *
     * @var type array
     */
    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method is used to set systemn identity
     * @param type $name string
     * @return type array
     */
    public function set_identity($name) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/system/identity/set");
        $sentence->setAttribute("name", $name);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all system  identiy
     * @return type array
     */
    public function get_all_identity() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/system/identity/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        return $rs->getResultArray();
    }

    /**
     * This method is used to display all system clock
     * @return type array
     */
    public function get_all_clock() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/system/clock/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        }
    }

    /**
     * This method is used to system bacup save
     * @param type $name string
     * @return type array
     */
    public function save_backup($name) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/system/backup/save");
        $sentence->setAttribute("name", $name);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to system backup load
     * @param type $name string
     * @return type array
     */
    public function load_backup($name) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/system/backup/load");
        $sentence->setAttribute("name", $name);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method is used to display all system history
     * @return type array
     */
    public function get_all_history() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/system/history/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No History";
        }
    }

    /**
     * This method is used to display all system license
     * @return type array
     */
    public function get_all_license() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/system/license/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        }
    }

    /**
     * This method is used to display all system routerboard
     * @return type array
     */
    public function get_all_routerboard() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/system/routerboard/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        }
    }

    /**
     * This method is used to system reset configuration
     * @param type $keep_users string (yes or no)
     * @param type $no_defaults string (yes or no)
     * @param type $skip_backup string (yes or no)
     * @return type array
     */
    public function reset($keep_users, $no_defaults, $skip_backup) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/ip/address/add");
        $sentence->setAttribute("keep-users", $keep_users);
        $sentence->setAttribute("no-defaults", $no_defaults);
        $sentence->setAttribute("skip-backup", $skip_backup);
        $this->talker->send($sentence);
        return "Sucsess";
    }

}


File: /src\MikrotikAPI\Commands\System\SystemScheduler.php
<?php

namespace MikrotikAPI\Commands\System;

use MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Talker\Talker;

/**
 * Description of Mapi_System_Scheduler
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class SystemScheduler {

    private $talker;

    function __construct(Talker $talker) {
        $this->talker = $talker;
    }

    /**
     * This method used for add new system scheduler
     * @param type $param array
     * @return type array
     */
    public function add($param) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/system/scheduler/add");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for disable system scheduler
     * @param type $id string
     * @return type array
     */
    public function disable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/system/scheduler/disable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for enable system scheduler
     * @param type $id string
     * @return type array
     */
    public function enable($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/system/scheduler/enable");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for delete system scheduler
     * @param type $id string
     * @return type array
     */
    public function delete($id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/system/scheduler/remove");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for detail system scheduler
     * @param type $id string
     * @return type array
     */
    public function detail($id) {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/system/scheduler/print");
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No System Scheduler With This id = " . $id;
        }
    }

    /**
     * This method used for set or edit system scheduler
     * @param type $param array
     * @param type $id string
     * @return type array
     */
    public function set($param, $id) {
        $sentence = new SentenceUtil();
        $sentence->addCommand("/system/scheduler/set");
        foreach ($param as $name => $value) {
            $sentence->setAttribute($name, $value);
        }
        $sentence->where(".id", "=", $id);
        $this->talker->send($sentence);
        return "Sucsess";
    }

    /**
     * This method used for get all system scheduler
     * @return type array
     */
    public function getAll() {
        $sentence = new SentenceUtil();
        $sentence->fromCommand("/system/scheduler/getall");
        $this->talker->send($sentence);
        $rs = $this->talker->getResult();
        $i = 0;
        if ($i < $rs->size()) {
            return $rs->getResultArray();
        } else {
            return "No System Scheduler To Set, Please Your Add System Scheduler";
        }
    }

}


File: /src\MikrotikAPI\Core\Connector.php
<?php

namespace MikrotikAPI\Core;

use MikrotikAPI\Core\StreamReciever,
    MikrotikAPI\Core\StreamSender,
    MikrotikAPI\Util\Util;

/**
 * Description of Connector
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 * @property StreamSender $sender
 * @property StreamReciever $reciever
 */
class Connector {

    private $socket;
    private $sender;
    private $reciever;
    private $host;
    private $port;
    private $username;
    private $password;
    private $connected = FALSE;
    private $login = FALSE;

    public function __construct($host, $port, $username, $password) {
        $this->host = $host;
        $this->port = $port;
        $this->username = $username;
        $this->password = $password;
        $this->initStream();
    }

    public function isConnected() {
        return $this->connected;
    }

    public function isLogin() {
        return $this->login;
    }

    private function initStream() {
        $this->socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
        $this->sender = new StreamSender($this->socket);
        $this->reciever = new StreamReciever($this->socket);
    }

    public function sendStream($command) {
        return $this->sender->send($command);
    }

    public function recieveStream() {
        return $this->reciever->reciever();
    }

    private function challanger($username, $password, $challange) {
        $chal = md5(chr(0) . $this->password . pack('H*', $challange));
        $login = "/login\n=name=" . $this->username . "\n=response=00" . $chal;
        return $login;
    }

    public function connect() {
        if (socket_connect($this->socket, $this->host, $this->port)) {
            $this->sendStream("/login");
            $rec = $this->recieveStream();
            if (!Util::contains($rec, "!trap") && strlen($rec) > 0) {
                $word = explode("\n", $rec);
                if (count($word) > 1) {
                    $split = explode("=ret=", $word[2]);
                    $challange = $split[1];
                    $challanger = $this->challanger($this->username, $this->password, $challange);
                    $this->sendStream($challanger);
                    $res = $this->recieveStream();
                    if (Util::contains($res, "!done") && !Util::contains($res, "!trap")) {
                        $this->login = TRUE;
                    }
                }
            }
            $this->connected = TRUE;
        } else {
            $this->connected = FALSE;
        }
    }

}


File: /src\MikrotikAPI\Core\StreamReciever.php
<?php

namespace MikrotikAPI\Core;

/**
 * Description of StreamReciever
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class StreamReciever {

    private $closed = false;
    private $socket;

    function __construct($socket) {
        $this->socket = $socket;
    }

    public function isClosed() {
        return $this->closed;
    }

    private function protocolWordDecoder() {
        return $this->streamReciever($this->protocolLengthDecoder());
    }

    private function streamReciever($length) {
        $recieved = "";
        while (strlen($recieved) < $length) {
            $len = $length - strlen($recieved);
            $str = socket_read($this->socket, $len);
            if ($str == '') {
                $this->closed = TRUE;
                echo socket_last_error($this->socket);
                break;
            }
            $recieved = $recieved . $str;
        }
        return $recieved;
    }

    private function protocolLengthDecoder() {
        $byte = ord($this->streamReciever(1));
        if (($byte & 0x80) == 0x00) {
            $byte = $byte;
        } else if (($byte & 0xC0) == 0x80) {
            $byte &= ~0xC0;
            $byte <<= 8;
            $byte += ord($this->streamReciever(1));
        } else if (($byte & 0xE0) == 0xC0) {
            $byte &= ~0xE0;
            $byte <<= 8;
            $byte += ord($this->streamReciever(1));
            $byte <<= 8;
            $byte += ord($this->streamReciever(1));
        } else if (($byte & 0xF0) == 0xE0) {
            $byte &= ~0xF0;
            $byte <<= 8;
            $byte += ord($this->streamReciever(1));
            $byte <<= 8;
            $byte += ord($this->streamReciever(1));
            $byte <<= 8;
            $byte += ord($this->streamReciever(1));
        } else if (($byte & 0xF8) == 0x0F0) {
            $byte = ord($this->streamReciever(1));
            $byte <<= 8;
            $byte += ord($this->streamReciever(1));
            $byte <<= 8;
            $byte += ord($this->streamReciever(1));
            $byte <<= 8;
            $byte += ord($this->streamReciever(1));
        }
        return $byte;
    }

    public function reciever() {
        $out = "";
        $i = 0;
        while (true) {
            $word = $this->protocolWordDecoder();
            if (strlen($word) != 0 && strlen($word) > 0) {
                $out = $out . "\n" . $word;
            } else {
                break;
            }
            $i++;
        }
        return $out;
    }

    private function getSocketStatus() {
        return socket_get_status($this->socket);
    }

}


File: /src\MikrotikAPI\Core\StreamSender.php
<?php

namespace MikrotikAPI\Core;

/**
 * Description of StreamSender
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, NuneNuh.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class StreamSender {

    private $socket;

    function __construct($socket) {
        $this->socket = $socket;
    }

    private function protocolLengthEncoder($command) {
        $length = strlen($command);
        switch ($length) {
            case $length < 0x80 :
                $this->streamSender(chr($length));
                break;
            case $length < 0x4000:
                $length |= 0x8000;
                $this->streamSender(chr(($length >> 8 ) & 0xFF));
                $this->streamSender(chr($length & 0xFF));
                break;
            case $length < 0x200000:
                $length |= 0xC00000;
                $this->streamSender(chr(($length >> 16) & 0xFF));
                $this->streamSender(chr(($length >> 8 ) & 0xFF));
                $this->streamSender(chr($length & 0xFF));
                break;
            case $length < 0x10000000:
                $length |= 0xE0000000;
                $this->streamSender(chr(($length >> 24 ) & 0xFF));
                $this->streamSender(chr(($length >> 16 ) & 0xFF));
                $this->streamSender(chr(($length >> 8 ) & 0xFF));
                $this->streamSender(chr($length & 0xFF));
                break;
            case $length >= 0x10000000:
                $this->streamSender(chr(0xF0));
                $this->streamSender(chr(($length >> 24) & 0x0FF));
                $this->streamSender(chr(($length >> 16) & 0x0FF));
                $this->streamSender(chr(($length >> 8 ) & 0x0FF));
                $this->streamSender(chr($length & 0x0FF));
                break;
        }
    }

    private function streamSender($command) {
        $i = 0;
        $out = 0;
        while ($i < strlen($command)) {
            $out = socket_write($this->socket, $command);
            if ($out == 0) {
                echo "Connection closed";
                echo socket_last_error($this->socket);
                break;
            }
            $i += $out;
        }
    }

    private function protocolWordEncoder($command) {
        $this->protocolLengthEncoder($command);
        $this->streamSender($command);
    }

    public function send($command) {
        $com_array = explode("\n", $command);
        if (count($com_array) > 2) {
            $ret = NULL;
            foreach ($com_array as $data) {
                $com = $data;
                $ret = $this->protocolWordEncoder($com);
            }
            $ret = $this->protocolWordEncoder('');
            return $ret;
        } else {
            $com = $com_array[0];
            $ret = $this->protocolWordEncoder($com);
            $ret = $this->protocolWordEncoder('');
        }
    }

}


File: /src\MikrotikAPI\Entity\Attribute.php
<?php

namespace MikrotikAPI\Entity;

/**
 * Description of Attribute
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class Attribute {

    private $clause;
    private $name;
    private $value;

    public function __construct($clause = '', $name = '', $value = '') {
        $this->clause = $clause;
        $this->name = $name;
        $this->value = $value;
    }

    public function setClause($clause) {
        $this->clause = $clause;
    }

    public function getClause() {
        return $this->clause;
    }

    public function setName($name) {
        $this->name = $name;
    }

    public function getName() {
        return $this->name;
    }

    public function setValue($value) {
        $this->value = $value;
    }

    public function getValue() {
        return $this->value;
    }

}


File: /src\MikrotikAPI\Entity\Auth.php
<?php

namespace MikrotikAPI\Entity;

/**
 * Description of Auth
 *
 * @author nunenuh
 */
class Auth {

    /**
     *
     * @var string
     */
    private $host;

    /**
     *
     * @var int 
     */
    private $port = 8728;

    /**
     *
     * @var string
     */
    private $username;

    /**
     *
     * @var string 
     */
    private $password;

    /**
     *
     * @var boolean 
     */
    private $debug = FALSE;

    /**
     *
     * @var int
     */
    private $attempts = 5;

    /**
     *
     * @var int
     */
    private $delay = 2;

    /**
     *
     * @var int
     */
    private $timeout = 2;

    function __construct() {
        
    }

    public function set($host, $port, $username, $password, $debug, $attempts, $delay, $timeout) {
        $this->host = $host;
        $this->port = $port;
        $this->username = $username;
        $this->password = $password;
        $this->debug = $debug;
        $this->attempts = $attempts;
        $this->delay = $delay;
        $this->timeout = $timeout;
    }

    public function getHost() {
        return $this->host;
    }

    public function getPort() {
        return $this->port;
    }

    public function getUsername() {
        return $this->username;
    }

    public function getPassword() {
        return $this->password;
    }

    public function getDebug() {
        return $this->debug;
    }

    public function getAttempts() {
        return $this->attempts;
    }

    public function getDelay() {
        return $this->delay;
    }

    public function getTimeout() {
        return $this->timeout;
    }

    public function setHost($host) {
        $this->host = $host;
    }

    public function setPort($port) {
        $this->port = $port;
    }

    public function setUsername($username) {
        $this->username = $username;
    }

    public function setPassword($password) {
        $this->password = $password;
    }

    public function setDebug($debug) {
        $this->debug = $debug;
    }

    public function setAttempts($attempts) {
        $this->attempts = $attempts;
    }

    public function setDelay($delay) {
        $this->delay = $delay;
    }

    public function setTimeout($timeout) {
        $this->timeout = $timeout;
    }

}


File: /src\MikrotikAPI\MikrotikAPI.php
<?php

namespace MikrotikAPI;

/**
 * Description of Mikrotik_Api
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class MikrotikAPI {

    /**
     * @access private
     * @var type Object
     */
    private $CI;

    /**
     * Instantiation of Class Mikrotik_Api
     * @access private
     * @var type array
     */
    private $param;
    
    
    /**
     *
     * @var Talker\Talker
     */
    private $talker;

    function __construct($param = array()) {
        $this->CI = & get_instance();
        $param_config = $this->CI->config->item('mikrotik');
        if (isset($param_config) && is_array($param_config)) {
            $this->param = $param_config;
        } else {
            $this->param = $param;
        }
        $this->talker = new Talker($this->param['host'], $this->param['port'], $this->param['username'], $this->param['password']);
    }

    /**
     * This method for call class Mapi IP
     * @access public
     * @return Object of Mapi_Ip 
     */
    public function IP() {
        return new Mapi_Ip($this->talker);
    }

    /**
     * This method for call class Mapi Interface
     * @access public
     * @return Object of Mapi_Interface 
     */
    public function interfaces() {
        return new Mapi_Interfaces($this->talker);
    }

    /**
     * This method for call class Mapi Ppp
     * @access public
     * @return Object of Mapi_Ppp
     */
    public function ppp() {
        return new Mapi_Ppp($this->talker);
    }

    /**
     * This method for call class Mapi_System
     * @access public
     * @return Mapi_System 
     */
    public function system() {
        return new Mapi_System($this->talker);
    }

    /**
     * This method for call class Mapi_File
     * @access public
     * @return Mapi_File 
     */
    public function file() {
        return new Mapi_File($this->talker);
    }

    /**
     * This metod used call class Mapi_System_Scheduler 
     * @return Mapi_Ip
     */
    public function system_scheduler() {
        return new Mapi_System_Scheduler($this->talker);
    }

    /**
     * 
     * @return \Talker
     */
    public function buildCommand() {
        return new Talker($this->param['host'], $this->param['port'], $this->param['username'], $this->param['password']);
    }

}


File: /src\MikrotikAPI\Talker\Talker.php
<?php

namespace MikrotikAPI\Talker;

use MikrotikAPI\Entity\Auth;
use MikrotikAPI\Core\Connector;

/**
 * Description of Talker
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 * @property TalkerReciever
 * @property TalkerSender
 */
class Talker {

    private $sender;
    private $reciever;
    private $auth;
    private $connector;

//        private $param;


    public function __construct(Auth $auth) {
//        parent::__construct($auth->getHost(), $auth->getPort(), $auth->getUsername(), $auth->getPassword());
//        parent::connect();
        $this->auth = $auth;
        $this->connector = new Connector($auth->getHost(), $auth->getPort(), $auth->getUsername(), $auth->getPassword());
        $this->connector->connect();
        $this->sender = new TalkerSender($this->connector);
        $this->reciever = new TalkerReciever($this->connector);
    }

    /**
     * 
     * @return type
     */
    public function isLogin() {
//        return parent::isLogin();
    }

    /**
     * 
     * @return type
     */
    public function isConnected() {
//        return parent::isConnected();
    }

    /**
     * 
     * @return type
     */
    public function isDebug() {
        return $this->auth->getDebug();
    }

    /**
     * 
     * @param type $boolean
     */
    public function setDebug($boolean) {
        $this->auth->setDebug($boolean);
        $this->sender->setDebug($boolean);
        $this->reciever->setDebug($boolean);
    }

    /**
     * 
     * @return type
     */
    public function isTrap() {
        return $this->reciever->isTrap();
    }

    /**
     * 
     * @return type
     */
    public function isDone() {
        return $this->reciever->isDone();
    }

    /**
     * 
     * @return type
     */
    public function isData() {
        return $this->reciever->isData();
    }

    /**
     * 
     * @param type $sentence
     */
    public function send($sentence) {
        $this->sender->send($sentence);
        $this->reciever->doRecieving();
    }

    /**
     * 
     * @return type
     */
    public function getResult() {
        return $this->reciever->getResult();
    }

}


File: /src\MikrotikAPI\Talker\TalkerReciever.php
<?php

namespace MikrotikAPI\Talker;

use MikrotikAPI\Core\Connector,
    MikrotikAPI\Util\ResultUtil,
    MikrotikAPI\Util\Util,
    MikrotikAPI\Entity\Attribute,
    MikrotikAPI\Util\DebugDumper;

/**
 * Description of TalkerReciever
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class TalkerReciever {

    private $con;
    private $result;
    private $trap = FALSE;
    private $done = FALSE;
    private $re = FALSE;
    private $debug = FALSE;

    public function __construct(Connector $con) {
        $this->con = $con;
        $this->result = new ResultUtil();
    }

    public function isTrap() {
        return $this->trap;
    }

    public function isDone() {
        return $this->done;
    }

    public function isData() {
        return $this->re;
    }

    public function isDebug() {
        return $this->debug;
    }

    public function setDebug($boolean) {
        $this->debug = $boolean;
    }

    private function parseRawToList($raw) {
        $raw = trim($raw);
        if (!empty($raw)) {
            $list = new \ArrayObject();
            $token = explode("\n", $raw);
            $a = 1;
            while ($a < count($token)) {
                next($token);
                $attr = new Attribute();
                if (!(current($token) == "!re") && !(current($token) == "!trap")) {
                    $split = explode("=", current($token));
                    $attr->setName($split[1]);
                    if (count($split) == 3) {
                        $attr->setValue($split[2]);
                    } else {
                        $attr->setValue(NULL);
                    }
                    $list->append($attr);
                }
                $a++;
            }
            if ($list->count() != 0)
                $this->result->add($list);
        }
    }

    public function getResult() {
        return $this->result;
    }

    public function doRecieving() {
        $this->run();
    }

    private function runDebugger($string) {
        if ($this->isDebug()) {
            DebugDumper::dump($string);
        }
    }

    private function run() {
        $s = "";
        while (true) {
            $s = $this->con->recieveStream();
            if (Util::contains($s, "!re")) {
                $this->parseRawToList($s);
                $this->runDebugger($s);
                $this->re = TRUE;
            }

            if (Util::contains($s, "!trap")) {
                $this->runDebugger($s);
                $this->trap = TRUE;
                break;
            }

            if (Util::contains($s, "!done")) {
                $this->runDebugger($s);
                $this->done = TRUE;
                break;
            }
        }
    }

}


File: /src\MikrotikAPI\Talker\TalkerSender.php
<?php

namespace MikrotikAPI\Talker;

use MikrotikAPI\Core\Connector,
    MikrotikAPI\Util\SentenceUtil,
    MikrotikAPI\Entity\Attribute,
    MikrotikAPI\Util\Util,
    MikrotikAPI\Util\DebugDumper;

/**
 * Description of TalkerSender
 *
 * @author Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright Copyright (c) 2011, Virtual Think Team.
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category Libraries
 */
class TalkerSender {

    private $debug = FALSE;
    private $con;

    public function __construct(Connector $con) {
        $this->con = $con;
    }

    public function send(SentenceUtil $sentence) {
        $cmd = $this->createSentence($sentence);
        $this->con->sendStream($cmd);
    }

    public function isDebug() {
        return $this->debug;
    }

    public function setDebug($boolean) {
        $this->debug = $boolean;
    }

    public function runDebugger($str) {
        if ($this->isDebug()) {
            DebugDumper::dump($str);
        }
    }

    private function sentenceWrapper(SentenceUtil $sentence) {
        $it = $sentence->getBuildCommand()->getIterator();

        $attr = new Attribute();
        while ($it->valid()) {
            if (Util::contains($it->current()->getClause(), "commandPrint") ||
                    Util::contains($it->current()->getClause(), "commandReguler")) {
                $attr = $it->current();
            }
            $it->next();
        }

        $it->rewind();

        $out = new \ArrayObject();
        $out->append($attr);
        while ($it->valid()) {
            if (!Util::contains($it->current()->getClause(), "commandPrint") &&
                    !Util::contains($it->current()->getClause(), "commandReguler")) {
                $out->append($it->current());
            }
            $it->next();
        }
        return $out;
    }

    private function createSentence(SentenceUtil $sentence) {
        $build = "";
        $sentence = $this->sentenceWrapper($sentence);
        $it = $sentence->getIterator();
        $cmd = "";

        while ($it->valid()) {
            $clause = $it->current()->getClause();
            $name = $it->current()->getName();
            $value = $it->current()->getValue();

            if (Util::contains($clause, "commandPrint")) {
                $build = $build . $value;
                $cmd = "print";
            } else if (Util::contains($clause, "commandReguler")) {
                $build = $build . $value;
                $cmd = "reguler";
            } else {
                if (Util::contains($name, "proplist") || Util::contains($name, "tag")) {
                    $build = $build . "=." . $name . "=" . $value;
                }

                if ($clause == "where" && $cmd == "print") {
                    $build = $build . "?" . $name . $value;
                }

                if ($clause == "where" && $cmd == "reguler") {
                    $build = $build . $name . $value;
                }

                if ($clause == "whereNot" || $clause == "orWhere" ||
                        $clause == "orWhereNot" || $clause == "andWhere" ||
                        $clause == "andWhereNot") {
                    $build = $build . $name . $value;
                }

                if ($clause == "setAttribute") {
                    $build = $build . "=" . $name . "=" . $value;
                }
            }
            if ($it->valid())
                $build = $build . "\n";
            $it->next();
        }
        $this->runDebugger($build);
        return $build;
    }

}


File: /src\MikrotikAPI\Util\DebugDumper.php
<?php

namespace MikrotikAPI\Util;

/**
 * Description of Debug
 *
 * @author nunenuh
 */
class DebugDumper {

    public static function dump($var, $detail = false) {
        if (is_array($var)) {
            if ($detail == false) {
                echo "<pre>";
                print_r($var);
                echo "</pre>";
            } else {
                echo "<pre>";
                var_dump($var);
                echo "</pre>";
            }
        } else {
            if ($detail == false) {
                echo "<pre>";
                echo $var;
                echo "</pre>";
            } else {
                echo "<pre>";
                var_dump($var);
                echo "</pre>";
            }
        }
    }

}


File: /src\MikrotikAPI\Util\ResultUtil.php
<?php

namespace MikrotikAPI\Util;

/**
 * Description of ResultUtil
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class ResultUtil {

    private $list;
    private $listAttr;
    private $itList;

    public function __construct() {
        $this->list = new \ArrayObject();
        $this->listAttr = new \ArrayObject();
    }

    public function getResult($mixed = '') {
        $value = NULL;
        if (gettype($mixed) == "string") {
            $it = $this->listAttr->getIterator();
            while ($it->valid()) {
                if ($it->current()->getName() == $mixed) {
                    $value = $it->current()->getValue();
                }
                $it->next();
            }
        } else if (gettype($mixed) == "integer") {
            $it = $this->listAttr->getIterator();
            $value = $it->offsetGet($mixed)->getValue();
        } else {
            $value = NULL;
        }
        return $value;
    }

    public function getResultArray() {
        $ar = new \ArrayObject();

        while ($this->next()) {
            $it = $this->listAttr->getIterator();
            while ($it->valid()) {
                $tmpAr[$it->current()->getName()] = $it->current()->getValue();
                $it->next();
            }
            $ar->append($tmpAr);
        }

        return $ar->getArrayCopy();
    }

    private function fireOnChange() {
        $this->itList = $this->list->getIterator();
        $this->listAttr = $this->itList->current();
    }

    public function hasNext() {
        return $this->itList->valid();
    }

    public function next() {
        if ($this->hasNext()) {
            $this->listAttr = $this->itList->current();
            $this->itList->next();
            return TRUE;
        } else {
            return FALSE;
        }
    }

    public function size() {
        return $this->list->count();
    }

    public function add(\ArrayObject $object) {
        $this->list->append($object);
        $this->fireOnChange();
    }

}


File: /src\MikrotikAPI\Util\SentenceUtil.php
<?php

namespace MikrotikAPI\Util;

use MikrotikAPI\Entity\Attribute;

/**
 * Description of SentenceUtil
 *
 * @author      Lalu Erfandi Maula Yusnu nunenuh@gmail.com <http://vthink.web.id>
 * @copyright   Copyright (c) 2011, Virtual Think Team.
 * @license     http://opensource.org/licenses/gpl-license.php GNU Public License
 * @category	Libraries
 */
class SentenceUtil {

    private $list;

    public function __construct() {
        $this->list = new \ArrayObject();
    }

    public function select($attributeName) {
        $name = "";
        if (Util::contains($attributeName, " ")) {
            $token = explode(" ", $attributeName);
            $a = 0;
            while ($a < count($token)) {
                $name = $name . current($token);
                next($token);
                $a++;
            }
        } else {
            $name = $attributeName;
        }

        $this->list->append(new Attribute("select", "proplist", $name));
    }

    public function where($name, $operand, $value) {
        if ($operand == "-" || $operand == "=" || $operand == "<" || $operand == ">") {
            $build = trim($operand) . trim($name) . "=";
            $this->list->append(new Attribute("where", $build, trim($value)));
        } else {
            return FALSE;
        }
    }

    public function whereNot($name, $operand, $value) {
        if ($operand == "-" || $operand == "=" || $operand == "<" || $operand == ">") {
            $build = "?" . trim($operand) . trim($name) . "=";
            $this->list->append(new Attribute("whereNot", $build, trim($value)));
            $this->list->append(new Attribute("whereNot", "?#", "!"));
            return TRUE;
        } else {
            return FALSE;
        }
    }

    public function orWhere($name, $operand, $value) {
        if ($operand == "-" || $operand == "=" || $operand == "<" || $operand == ">") {
            $build = "?" . trim($operand) . trim($name) . "=";
            $this->list->append(new Attribute("whereNot", $build, trim($value)));
            $this->list->append(new Attribute("whereNot", "?#", "|"));
            return TRUE;
        } else {
            return FALSE;
        }
    }

    public function orWhereNot($name, $operand, $value) {
        if ($operand == "-" || $operand == "=" || $operand == "<" || $operand == ">") {
            $build = "?" . trim($operand) . trim($name) . "=";
            $this->list->append(new Attribute("whereNot", $build, trim($value)));
            $this->list->append(new Attribute("whereNot", "?#", "!"));
            $this->list->append(new Attribute("whereNot", "?#", "|"));
            return TRUE;
        } else {
            return FALSE;
        }
    }

    public function andWhere($name, $operand, $value) {
        if ($operand == "-" || $operand == "=" || $operand == "<" || $operand == ">") {
            $build = "?" . trim($operand) . trim($name) . "=";
            $this->list->append(new Attribute("whereNot", $build, trim($value)));
            $this->list->append(new Attribute("whereNot", "?#", "&"));
            return TRUE;
        } else {
            return FALSE;
        }
    }

    public function andWhereNot($name, $operand, $value) {
        if ($operand == "-" || $operand == "=" || $operand == "<" || $operand == ">") {
            $build = "?" . trim($operand) . trim($name) . "=";
            $this->list->append(new Attribute("whereNot", $build, trim($value)));
            $this->list->append(new Attribute("whereNot", "?#", "!"));
            $this->list->append(new Attribute("whereNot", "?#", "&"));
            return TRUE;
        } else {
            return FALSE;
        }
    }

    public function fromCommand($command) {
        $this->list->append(new Attribute("commandPrint", "command", $command));
    }

    public function addCommand($command) {
        $this->list->append(new Attribute("commandReguler", "command", $command));
    }

    public function setAttribute($name, $value) {
        $this->list->append(new Attribute("setAttribute", $name, $value));
    }

    public function getBuildCommand() {
        return $this->list;
    }

    public function add(Attribute $attr) {
        $this->list->append($attr);
    }

}


File: /src\MikrotikAPI\Util\Util.php
<?php

namespace MikrotikAPI\Util;

class Util {

    public static function contains($string, $needle) {
        $pos = strpos($string, $needle);
        if (!($pos === FALSE)) {
            return TRUE;
        } else {
            return FALSE;
        }
    }

}


File: /test\test.php
<?php

require '../vendor/autoload.php';

use MikrotikAPI\Talker\Talker;
use \MikrotikAPI\Entity\Auth;
use MikrotikAPI\Commands\IP\Address;
use MikrotikAPI\Commands\IP\Firewall\FirewallFilter;


$auth = new Auth();
$auth->setHost("172.18.1.254");
$auth->setUsername("admin");
$auth->setPassword("1261");
$auth->setDebug(true);


$talker = new Talker($auth);
//$filter = new FirewallFilter($talker);
//$a = $filter->getAll();


$ipaddr = new Address($talker);
$listIP = $ipaddr->getAll();


MikrotikAPI\Util\DebugDumper::dump($listIP);


File: /vendor\autoload.php
<?php

// autoload.php @generated by Composer

require_once __DIR__ . '/composer' . '/autoload_real.php';

return ComposerAutoloaderInit6e58d18ab647c55b3f15c6772ec323c7::getLoader();


File: /vendor\composer\autoload_classmap.php
<?php

// autoload_classmap.php @generated by Composer

$vendorDir = dirname(dirname(__FILE__));
$baseDir = dirname($vendorDir);

return array(
);


File: /vendor\composer\autoload_namespaces.php
<?php

// autoload_namespaces.php @generated by Composer

$vendorDir = dirname(dirname(__FILE__));
$baseDir = dirname($vendorDir);

return array(
    'MikrotikAPITest' => array($baseDir . '/test'),
    'MikrotikAPI' => array($baseDir . '/src'),
);


File: /vendor\composer\autoload_real.php
<?php

// autoload_real.php @generated by Composer

class ComposerAutoloaderInit6e58d18ab647c55b3f15c6772ec323c7
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

        spl_autoload_register(array('ComposerAutoloaderInit6e58d18ab647c55b3f15c6772ec323c7', 'loadClassLoader'), true, true);
        self::$loader = $loader = new \Composer\Autoload\ClassLoader();
        spl_autoload_unregister(array('ComposerAutoloaderInit6e58d18ab647c55b3f15c6772ec323c7', 'loadClassLoader'));

        $vendorDir = dirname(__DIR__);
        $baseDir = dirname($vendorDir);

        $map = require __DIR__ . '/autoload_namespaces.php';
        foreach ($map as $namespace => $path) {
            $loader->set($namespace, $path);
        }

        $classMap = require __DIR__ . '/autoload_classmap.php';
        if ($classMap) {
            $loader->addClassMap($classMap);
        }

        $loader->register(true);

        return $loader;
    }
}


File: /vendor\composer\ClassLoader.php
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
 * ClassLoader implements a PSR-0 class loader
 *
 * See https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0.md
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
 */
class ClassLoader
{
    private $prefixes = array();
    private $fallbackDirs = array();
    private $useIncludePath = false;
    private $classMap = array();

    public function getPrefixes()
    {
        return call_user_func_array('array_merge', $this->prefixes);
    }

    public function getFallbackDirs()
    {
        return $this->fallbackDirs;
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
     * Registers a set of classes, merging with any others previously set.
     *
     * @param string       $prefix  The classes prefix
     * @param array|string $paths   The location(s) of the classes
     * @param bool         $prepend Prepend the location(s)
     */
    public function add($prefix, $paths, $prepend = false)
    {
        if (!$prefix) {
            if ($prepend) {
                $this->fallbackDirs = array_merge(
                    (array) $paths,
                    $this->fallbackDirs
                );
            } else {
                $this->fallbackDirs = array_merge(
                    $this->fallbackDirs,
                    (array) $paths
                );
            }

            return;
        }

        $first = $prefix[0];
        if (!isset($this->prefixes[$first][$prefix])) {
            $this->prefixes[$first][$prefix] = (array) $paths;

            return;
        }
        if ($prepend) {
            $this->prefixes[$first][$prefix] = array_merge(
                (array) $paths,
                $this->prefixes[$first][$prefix]
            );
        } else {
            $this->prefixes[$first][$prefix] = array_merge(
                $this->prefixes[$first][$prefix],
                (array) $paths
            );
        }
    }

    /**
     * Registers a set of classes, replacing any others previously set.
     *
     * @param string       $prefix The classes prefix
     * @param array|string $paths  The location(s) of the classes
     */
    public function set($prefix, $paths)
    {
        if (!$prefix) {
            $this->fallbackDirs = (array) $paths;

            return;
        }
        $this->prefixes[substr($prefix, 0, 1)][$prefix] = (array) $paths;
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
            include $file;

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
        // work around for PHP 5.3.0 - 5.3.2 https://bugs.php.net/50731
        if ('\\' == $class[0]) {
            $class = substr($class, 1);
        }

        if (isset($this->classMap[$class])) {
            return $this->classMap[$class];
        }

        if (false !== $pos = strrpos($class, '\\')) {
            // namespaced class name
            $classPath = strtr(substr($class, 0, $pos), '\\', DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR;
            $className = substr($class, $pos + 1);
        } else {
            // PEAR-like class name
            $classPath = null;
            $className = $class;
        }

        $classPath .= strtr($className, '_', DIRECTORY_SEPARATOR) . '.php';

        $first = $class[0];
        if (isset($this->prefixes[$first])) {
            foreach ($this->prefixes[$first] as $prefix => $dirs) {
                if (0 === strpos($class, $prefix)) {
                    foreach ($dirs as $dir) {
                        if (file_exists($dir . DIRECTORY_SEPARATOR . $classPath)) {
                            return $dir . DIRECTORY_SEPARATOR . $classPath;
                        }
                    }
                }
            }
        }

        foreach ($this->fallbackDirs as $dir) {
            if (file_exists($dir . DIRECTORY_SEPARATOR . $classPath)) {
                return $dir . DIRECTORY_SEPARATOR . $classPath;
            }
        }

        if ($this->useIncludePath && $file = stream_resolve_include_path($classPath)) {
            return $file;
        }

        return $this->classMap[$class] = false;
    }
}


