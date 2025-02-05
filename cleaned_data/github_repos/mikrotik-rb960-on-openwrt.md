# Repository Information
Name: mikrotik-rb960-on-openwrt

# Directory Structure
Directory structure:
└── github_repos/mikrotik-rb960-on-openwrt/
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
    │   │       ├── pack-9fc0023ac69a00fd7b4fb1223a04791404888a97.idx
    │   │       └── pack-9fc0023ac69a00fd7b4fb1223a04791404888a97.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── rb960pgs-and-mtpoe-ctrl.patch
    └── README.md


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
	url = https://github.com/adron-s/mikrotik-rb960-on-openwrt.git
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
0000000000000000000000000000000000000000 09b5bbf7b8fb60303894e20683dcfd124fd27550 vivek-dodia <vivek.dodia@icloud.com> 1738606325 -0500	clone: from https://github.com/adron-s/mikrotik-rb960-on-openwrt.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 09b5bbf7b8fb60303894e20683dcfd124fd27550 vivek-dodia <vivek.dodia@icloud.com> 1738606325 -0500	clone: from https://github.com/adron-s/mikrotik-rb960-on-openwrt.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 09b5bbf7b8fb60303894e20683dcfd124fd27550 vivek-dodia <vivek.dodia@icloud.com> 1738606325 -0500	clone: from https://github.com/adron-s/mikrotik-rb960-on-openwrt.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
09b5bbf7b8fb60303894e20683dcfd124fd27550 refs/remotes/origin/master


File: /.git\refs\heads\master
09b5bbf7b8fb60303894e20683dcfd124fd27550


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /rb960pgs-and-mtpoe-ctrl.patch
commit 48d2d2204b9f976c2bf7c052fc9fc56e7693b127
Author: Sergey Sergeev <adron@yapic.net>
Date:   Fri Apr 3 16:17:16 2020 +0300

    rb71xx: adds support for Mikrotiks RB960PGS. also this patch do the following:
    - changes that is necessary for mtpoe_ctrl(spidev #3) work
    - some improvements for the RB962(ethernet switch and sfp port) and RB750(swaps eth0/eth1)
    
    Signed-off-by: Sergey Sergeev <adron@yapic.net>

diff --git a/target/linux/ar71xx/base-files/etc/board.d/01_leds b/target/linux/ar71xx/base-files/etc/board.d/01_leds
index ba9e68a..ad1c421 100755
--- a/target/linux/ar71xx/base-files/etc/board.d/01_leds
+++ b/target/linux/ar71xx/base-files/etc/board.d/01_leds
@@ -653,6 +653,9 @@ rb-952ui-5ac2nd)
 	ucidef_set_led_switch "port5" "port5" "rb:green:port5" "switch0" "0x02"
 	ucidef_set_led_wlan "wlan" "WLAN" "rb:blue:wlan" "phy0tpt"
 	;;
+rb-960pgs)
+	ucidef_set_led_timer "user" "USER" "rb:green:act" "1000" "1000"
+	;;
 rb-962uigs-5hact2hnt)
 	ucidef_set_led_timer "user" "USER/SFP" "rb:green:act" "1000" "1000"
 	;;
diff --git a/target/linux/ar71xx/base-files/etc/board.d/02_network b/target/linux/ar71xx/base-files/etc/board.d/02_network
index befa032..bca624e 100755
--- a/target/linux/ar71xx/base-files/etc/board.d/02_network
+++ b/target/linux/ar71xx/base-files/etc/board.d/02_network
@@ -198,6 +198,7 @@ ar71xx_setup_interfaces()
 	rb-750gl|\
 	rb-751g|\
 	rb-951g-2hnd|\
+	rb-960pgs|\
 	rb-962uigs-5hact2hnt|\
 	wlr8100|\
 	wzr-hp-g450h)
diff --git a/target/linux/ar71xx/base-files/etc/diag.sh b/target/linux/ar71xx/base-files/etc/diag.sh
index e8df560..0b8302a 100644
--- a/target/linux/ar71xx/base-files/etc/diag.sh
+++ b/target/linux/ar71xx/base-files/etc/diag.sh
@@ -372,6 +372,7 @@ get_status_led() {
 	rb-941-2nd|\
 	rb-951ui-2nd|\
 	rb-952ui-5ac2nd|\
+	rb-960pgs|\
 	rb-962uigs-5hact2hnt|\
 	rb-lhg-5nd|\
 	rb-map-2nd|\
diff --git a/target/linux/ar71xx/base-files/lib/ar71xx.sh b/target/linux/ar71xx/base-files/lib/ar71xx.sh
index 4ba5005..e8a6a23 100755
--- a/target/linux/ar71xx/base-files/lib/ar71xx.sh
+++ b/target/linux/ar71xx/base-files/lib/ar71xx.sh
@@ -507,6 +507,9 @@ mikrotik_board_detect() {
 	*"952Ui-5ac2nD")
 		name="rb-952ui-5ac2nd"
 		;;
+	*"960PGS")
+		name="rb-960pgs"
+		;;
 	*"962UiGS-5HacT2HnT")
 		name="rb-962uigs-5hact2hnt"
 		;;
diff --git a/target/linux/ar71xx/base-files/lib/upgrade/platform.sh b/target/linux/ar71xx/base-files/lib/upgrade/platform.sh
index 8558fde..8bd9c46 100755
--- a/target/linux/ar71xx/base-files/lib/upgrade/platform.sh
+++ b/target/linux/ar71xx/base-files/lib/upgrade/platform.sh
@@ -709,6 +709,7 @@ platform_check_image() {
 	rb-941-2nd|\
 	rb-951ui-2nd|\
 	rb-952ui-5ac2nd|\
+	rb-960pgs|\
 	rb-962uigs-5hact2hnt|\
 	rb-lhg-5nd|\
 	rb-map-2nd|\
@@ -735,6 +736,7 @@ platform_pre_upgrade() {
 	rb-941-2nd|\
 	rb-951ui-2nd|\
 	rb-952ui-5ac2nd|\
+	rb-960pgs|\
 	rb-962uigs-5hact2hnt|\
 	rb-lhg-5nd|\
 	rb-map-2nd|\
diff --git a/target/linux/ar71xx/files/arch/mips/ath79/mach-rbspi.c b/target/linux/ar71xx/files/arch/mips/ath79/mach-rbspi.c
index f8800f5..96e1395 100644
--- a/target/linux/ar71xx/files/arch/mips/ath79/mach-rbspi.c
+++ b/target/linux/ar71xx/files/arch/mips/ath79/mach-rbspi.c
@@ -9,6 +9,8 @@
  *  - MikroTik RouterBOARD 951Ui-2nD
  *  - MikroTik RouterBOARD 952Ui-5ac2nD
  *  - MikroTik RouterBOARD 962UiGS-5HacT2HnT
+ *  - Mikrotik RouterBOARD 960PGS (hEX PoE)
+ *  - MikroTik RouterBOARD 962UiGS-5HacT2HnT
  *  - MikroTik RouterBOARD 750UP r2
  *  - MikroTik RouterBOARD 750P-PBr2
  *  - MikroTik RouterBOARD 750 r2
@@ -25,6 +27,7 @@
  *  Copyright (C) 2017 Thibaut VARENE <varenet@parisc-linux.org>
  *  Copyright (C) 2016 David Hutchison <dhutchison@bluemesh.net>
  *  Copyright (C) 2017 Ryan Mounce <ryan@mounce.com.au>
+ *  Copyright (C) 2017-2020 Sergey Sergeev <adron@mstnt.com>
  *
  *  This program is free software; you can redistribute it and/or modify it
  *  under the terms of the GNU General Public License version 2 as published
@@ -72,8 +75,9 @@
 #define RBSPI_HAS_WAN4		BIT(3)	/* has WAN port on PHY4 */
 #define RBSPI_HAS_SSR		BIT(4)	/* has an SSR on SPI bus 0 */
 #define RBSPI_HAS_POE		BIT(5)
-#define RBSPI_HAS_MDIO1		BIT(6)
-#define RBSPI_HAS_PCI		BIT(7)
+#define RBSPI_HAS_POE_MK BIT(6) /* has a smart PoE micro-controller on SPI bus 0 */
+#define RBSPI_HAS_MDIO1		BIT(7)
+#define RBSPI_HAS_PCI		BIT(8)
 
 #define RB_ROUTERBOOT_OFFSET    0x0000
 #define RB_BIOS_SIZE            0x1000
@@ -219,6 +223,10 @@ static struct gpio_led rbhapl_leds[] __initdata = {
 #define RB952_GPIO_LED_LAN5	RBSPI_SSR_GPIO(RB952_SSR_BIT_LED_LAN5)
 #define RB952_GPIO_LED_WLAN	RBSPI_SSR_GPIO(RB952_SSR_BIT_LED_WLAN)
 
+/* RB 750-r2(HB) with POE v2 */
+#define RB750R2_ATTINY_CS			12
+#define RB750R2_ATTINY_RESET	14
+
 static struct gpio_led rb952_leds[] __initdata = {
 	{
 		.name = "rb:green:user",
@@ -252,22 +260,28 @@ static struct gpio_led rb952_leds[] __initdata = {
 };
 
 
-/* RB 962UiGS-5HacT2HnT gpios */
-#define RB962_GPIO_POE_STATUS	2
-#define RB962_GPIO_POE_POWER	3
-#define RB962_GPIO_LED_USER	12
-#define RB962_GPIO_USB_POWER	13
-#define RB962_GPIO_BTN_RESET	20
+/* RB960PGS/RB962(hEX PoE) gpios */
+#define RB96X_GPIO_LED_SFP		2
+#define RB96X_GPIO_POE_PWR		3
+#define RB96X_GPIO_SPEAKER		4
+#define RB96X_GPIO_LED_USER		12
+#define RB96X_GPIO_USB_PWR		13
+#define RB96X_GPIO_BTN_RESET	20
 
-static struct gpio_led rb962_leds_gpio[] __initdata = {
+static struct gpio_led rb96x_leds_gpio[] __initdata = {
 	{
+		.name		= "rb:green:sfp",
+		.gpio		= RB96X_GPIO_LED_SFP,
+		.active_low	= 1,
+		.default_state  = LEDS_GPIO_DEFSTATE_ON, /* гасим sfp лампочку */
+	}, {
 		.name		= "rb:green:act",
-		.gpio		= RB962_GPIO_LED_USER,
+		.gpio		= RB96X_GPIO_LED_USER, /* для 962-го это sfp лампочка */
 		.active_low	= 1,
-	},
+	}
 };
 
-static const struct ar8327_led_info rb962_leds_ar8327[] = {
+static const struct ar8327_led_info rb96x_leds_ar8327[] = {
 		AR8327_LED_INFO(PHY0_0, HW, "rb:green:port1"),
 		AR8327_LED_INFO(PHY1_0, HW, "rb:green:port2"),
 		AR8327_LED_INFO(PHY2_0, HW, "rb:green:port3"),
@@ -275,7 +289,7 @@ static const struct ar8327_led_info rb962_leds_ar8327[] = {
 		AR8327_LED_INFO(PHY4_0, HW, "rb:green:port5"),
 };
 
-static struct ar8327_pad_cfg rb962_ar8327_pad0_cfg = {
+static struct ar8327_pad_cfg rb96x_ar8327_pad0_cfg = {
 		.mode = AR8327_PAD_MAC_RGMII,
 		.txclk_delay_en = true,
 		.rxclk_delay_en = true,
@@ -284,14 +298,16 @@ static struct ar8327_pad_cfg rb962_ar8327_pad0_cfg = {
 		.mac06_exchange_dis = true,
 };
 
-static struct ar8327_pad_cfg rb962_ar8327_pad6_cfg = {
+/* 6-й порт свитча через RSGMII подключен к SFP и процессору. Пока что еще одна
+	 связка с процессором мне не нужна. Достаточно RGMII к 0-му порту */
+//static struct ar8327_pad_cfg rb96x_ar8327_pad6_cfg = {
 		/* Use SGMII interface for GMAC6 of the AR8337 switch */
-		.mode = AR8327_PAD_MAC_SGMII,
+/*		.mode = AR8327_PAD_MAC_SGMII,
 		.rxclk_delay_en = true,
 		.rxclk_delay_sel = AR8327_CLK_DELAY_SEL0,
-};
+};*/
 
-static struct ar8327_led_cfg rb962_ar8327_led_cfg = {
+static struct ar8327_led_cfg rb96x_ar8327_led_cfg = {
 		.led_ctrl0 = 0xc737c737,
 		.led_ctrl1 = 0x00000000,
 		.led_ctrl2 = 0x00000000,
@@ -299,9 +315,9 @@ static struct ar8327_led_cfg rb962_ar8327_led_cfg = {
 		.open_drain = false,
 };
 
-static struct ar8327_platform_data rb962_ar8327_data = {
-		.pad0_cfg = &rb962_ar8327_pad0_cfg,
-		.pad6_cfg = &rb962_ar8327_pad6_cfg,
+static struct ar8327_platform_data rb96x_ar8327_data = {
+		.pad0_cfg = &rb96x_ar8327_pad0_cfg,
+		//.pad6_cfg = &rb96x_ar8327_pad6_cfg,
 		.port0_cfg = {
 				.force_link = 1,
 				.speed = AR8327_PORT_SPEED_1000,
@@ -309,23 +325,24 @@ static struct ar8327_platform_data rb962_ar8327_data = {
 				.txpause = 1,
 				.rxpause = 1,
 		},
-		.port6_cfg = {
+		/*.port6_cfg = {
 				.force_link = 1,
 				.speed = AR8327_PORT_SPEED_1000,
 				.duplex = 1,
 				.txpause = 1,
 				.rxpause = 1,
-		},
-		.led_cfg = &rb962_ar8327_led_cfg,
-		.num_leds = ARRAY_SIZE(rb962_leds_ar8327),
-		.leds = rb962_leds_ar8327,
+		},*/
+		.led_cfg = &rb96x_ar8327_led_cfg,
+		.num_leds = ARRAY_SIZE(rb96x_leds_ar8327),
+		.leds = rb96x_leds_ar8327,
 };
 
-static struct mdio_board_info rb962_mdio0_info[] = {
+/* описание mdio шины идущей к QCA8337 свитчу */
+static struct mdio_board_info rb96x_mdio0_info[] = {
 		{
 				.bus_id = "ag71xx-mdio.0",
 				.phy_addr = 0,
-				.platform_data = &rb962_ar8327_data,
+				.platform_data = &rb96x_ar8327_data,
 		},
 };
 
@@ -567,6 +584,7 @@ static struct gen_74x164_chip_platform_data rbspi_ssr_data = {
 static int rbspi_spi_cs_gpios[] = {
 	-ENOENT,	/* CS0 is always -ENOENT: natively handled */
 	-ENOENT,	/* CS1 can be updated by the code as necessary */
+	-ENOENT,	/* CS2 can be updated by the code as necessary */
 };
 
 static struct ath79_spi_platform_data rbspi_ath79_spi_data = {
@@ -591,6 +609,11 @@ static struct spi_board_info rbspi_spi_info[] = {
 		.max_speed_hz	= 25000000,
 		.modalias	= "74x164",
 		.platform_data	= &rbspi_ssr_data,
+	}, {
+		.bus_num = 0, /* PoE micro-controller */
+		.chip_select = 2,
+		.max_speed_hz = 2000000,
+		.modalias = "spidev",
 	}
 };
 
@@ -649,12 +672,12 @@ static __init const struct rb_info *rbspi_platform_setup(void)
  */
 static void __init rbspi_peripherals_setup(u32 flags)
 {
-	unsigned spi_n;
+	unsigned spi_n = 1;     /* only one device on bus0 */
 
 	if (flags & RBSPI_HAS_SSR)
-		spi_n = ARRAY_SIZE(rbspi_spi_info);
-	else
-		spi_n = 1;     /* only one device on bus0 */
+		spi_n = 2;
+	if (flags & RBSPI_HAS_POE_MK)
+		spi_n = 3;
 
 	rbspi_ath79_spi_data.num_chipselect = spi_n;
 	rbspi_ath79_spi_data.cs_gpios = rbspi_spi_cs_gpios;
@@ -679,6 +702,13 @@ static void __init rbspi_network_setup(u32 flags, int gmac1_offset,
 	if (flags & RBSPI_HAS_MDIO1)
 		ath79_register_mdio(1, 0x0);
 
+  /* !!! сначала LAN. он будет eth0 !!! */
+	/* init GMAC1 */
+	ath79_init_mac(ath79_eth1_data.mac_addr, ath79_mac_base, gmac1_offset);
+	ath79_eth1_data.phy_if_mode = PHY_INTERFACE_MODE_GMII;
+	ath79_register_eth(1);
+
+  /* теперь WAN. он будет eth1 */
 	if (flags & RBSPI_HAS_WAN4) {
 		ath79_setup_ar934x_eth_cfg(0);
 
@@ -701,11 +731,6 @@ static void __init rbspi_network_setup(u32 flags, int gmac1_offset,
 		ath79_setup_ar934x_eth_cfg(AR934X_ETH_CFG_SW_ONLY_MODE);
 	}
 
-	/* init GMAC1 */
-	ath79_init_mac(ath79_eth1_data.mac_addr, ath79_mac_base, gmac1_offset);
-	ath79_eth1_data.phy_if_mode = PHY_INTERFACE_MODE_GMII;
-	ath79_register_eth(1);
-
 	if (flags & RBSPI_HAS_WLAN0)
 		rbspi_wlan_init(0, wmac0_offset);
 
@@ -782,6 +807,8 @@ static void __init rbspi_952_750r2_setup(u32 flags)
 {
 	if (flags & RBSPI_HAS_SSR)
 		rbspi_spi_cs_gpios[1] = RB952_GPIO_SSR_CS;
+	if (flags & RBSPI_HAS_POE_MK)
+		rbspi_spi_cs_gpios[2] = RB750R2_ATTINY_CS; /* ATtiny PoE v2 */
 
 	rbspi_peripherals_setup(flags);
 
@@ -851,44 +878,59 @@ static void __init rb750upr2_setup(void)
 
 	/* differentiate the hEX lite from the hEX PoE lite */
 	if (strstr(mips_get_machine_name(), "750UP r2"))
-		flags |= RBSPI_HAS_USB | RBSPI_HAS_POE;
+		flags |= RBSPI_HAS_USB | RBSPI_HAS_POE_MK;
 
 	/* differentiate the Powerbox from the hEX lite */
 	else if (strstr(mips_get_machine_name(), "750P r2"))
-		flags |= RBSPI_HAS_POE;
+		flags |= RBSPI_HAS_POE_MK;
 
 	rbspi_952_750r2_setup(flags);
 }
 
 /*
- * Init the hAP ac / 962UiGS-5HacT2HnT hardware (QCA9558).
- * The hAP ac has 5 ethernet ports provided by an AR8337 switch. Port 1 is
+ * Init the hEX POE / RB960PGS and hAP ac / 962UiGS-5HacT2HnT hardware (QCA9558).
+ * The RB960PGS has 5 ethernet ports provided by an AR8337 switch. Port 1 is
  * assigned to WAN, ports 2-5 are assigned to LAN. Port 0 is connected to the
  * SoC, ports 1-5 of the switch are connected to physical ports 1-5 in order.
- * The SFP cage is not assigned by default on RouterOS. Extra work is required
- * to support this interface as it is directly connected to the SoC (eth1).
- * Wireless is provided by a 2.4GHz radio on the SoC (WLAN1) and a 5GHz radio
- * attached via PCI (QCA9880). Red and green WLAN LEDs are populated however
- * they are not attached to GPIOs, extra work is required to support these.
+ * The SFP cage is directly connected to the SoC (eth1).
  * PoE and USB output power control is supported.
+ *
+ * hAP ac / 962UiGS-5HacT2HnT has the same hardware (QCA9558) and additionally
+ * wireless. It is provided by a 2.4GHz radio on the SoC (WLAN1) and a 5GHz radio
+ * attached via PCI (QCA9880). Red and green WLAN LEDs are populated and uses
+ * QCA9880 internal GPIOs.
  */
-static void __init rb962_setup(void)
+static void __init rb96x_setup(void)
 {
-	u32 flags = RBSPI_HAS_USB | RBSPI_HAS_POE | RBSPI_HAS_PCI;
+	u32 flags = RBSPI_HAS_USB;
+
+	/* на всякий случай вместо "74x164" запишем туда "spidev".
+		 фактически там никакого устройства нет. */
+	memcpy(&rbspi_spi_info[1], &rbspi_spi_info[2], sizeof(rbspi_spi_info[2]));
+	rbspi_spi_info[1].chip_select = 1;
 
 	if (!rbspi_platform_setup())
 		return;
 
+	/* differentiate the RB962 from the RB960 */
+	if (strstr(mips_get_machine_name(), "962UiGS")) { /* RB962 */
+		flags |= RBSPI_HAS_POE; /* Simple GPIO PoE */
+		flags |= RBSPI_HAS_WLAN1 | RBSPI_HAS_PCI; /* 5Ghz WiFi */
+	} else { /* RB960 */
+		flags |= RBSPI_HAS_POE_MK; /* SPI micro-controller PoE */
+	}
+
 	rbspi_peripherals_setup(flags);
 
+	/* !!! сначала LAN. он будет eth0 !!! */
 	/* Do not call rbspi_network_setup as we have a discrete switch chip */
 	ath79_eth0_pll_data.pll_1000 = 0xae000000;
 	ath79_eth0_pll_data.pll_100 = 0xa0000101;
 	ath79_eth0_pll_data.pll_10 = 0xa0001313;
 
 	ath79_register_mdio(0, 0x0);
-	mdiobus_register_board_info(rb962_mdio0_info,
-					ARRAY_SIZE(rb962_mdio0_info));
+	mdiobus_register_board_info(rb96x_mdio0_info,
+					ARRAY_SIZE(rb96x_mdio0_info));
 
 	ath79_setup_qca955x_eth_cfg(QCA955X_ETH_CFG_RGMII_EN);
 
@@ -898,26 +940,36 @@ static void __init rb962_setup(void)
 	ath79_eth0_data.mii_bus_dev = &ath79_mdio0_device.dev;
 	ath79_register_eth(0);
 
+	/* SFP будет eth1 */
+	/* GMAC1 is connected to the SGMII interface */
+	ath79_init_mac(ath79_eth1_data.mac_addr, ath79_mac_base, 5);
+	ath79_eth1_data.phy_if_mode = PHY_INTERFACE_MODE_SGMII;
+	ath79_eth1_data.speed = SPEED_1000;
+	ath79_eth1_data.duplex = DUPLEX_FULL;
+	ath79_eth1_pll_data.pll_1000 = 0x03000101;
+	ath79_register_eth(1);
+
 	/* WLAN1 MAC is HW MAC + 7 */
-	rbspi_wlan_init(1, 7);
+	if(flags & RBSPI_HAS_WLAN1)
+		rbspi_wlan_init(1, 7); //wlan1 - internal 2.4Ghz WiFI
 
 	if (flags & RBSPI_HAS_USB)
-		gpio_request_one(RB962_GPIO_USB_POWER,
+		gpio_request_one(RB96X_GPIO_USB_PWR,
 				GPIOF_OUT_INIT_HIGH | GPIOF_EXPORT_DIR_FIXED,
 				"USB power");
 
 	/* PoE output GPIO is inverted, set GPIOF_ACTIVE_LOW for consistency */
 	if (flags & RBSPI_HAS_POE)
-		gpio_request_one(RB962_GPIO_POE_POWER,
+		gpio_request_one(RB96X_GPIO_POE_PWR,
 				GPIOF_OUT_INIT_HIGH | GPIOF_ACTIVE_LOW |
 					GPIOF_EXPORT_DIR_FIXED,
 				"POE power");
 
-	ath79_register_leds_gpio(-1, ARRAY_SIZE(rb962_leds_gpio),
-				rb962_leds_gpio);
+	ath79_register_leds_gpio(-1, ARRAY_SIZE(rb96x_leds_gpio),
+				rb96x_leds_gpio);
 
 	/* This device has a single reset button as gpio 20 */
-	rbspi_register_reset_button(RB962_GPIO_BTN_RESET);
+	rbspi_register_reset_button(RB96X_GPIO_BTN_RESET);
 }
 
 /*
@@ -1112,7 +1164,8 @@ MIPS_MACHINE_NONAME(ATH79_MACH_RB_MAPL, "map-hb", rbmapl_setup);
 MIPS_MACHINE_NONAME(ATH79_MACH_RB_941, "H951L", rbhapl_setup);
 MIPS_MACHINE_NONAME(ATH79_MACH_RB_911L, "911L", rb911l_setup);
 MIPS_MACHINE_NONAME(ATH79_MACH_RB_952, "952-hb", rb952_setup);
-MIPS_MACHINE_NONAME(ATH79_MACH_RB_962, "962", rb962_setup);
+MIPS_MACHINE_NONAME(ATH79_MACH_RB_960, "960", rb96x_setup);
+MIPS_MACHINE_NONAME(ATH79_MACH_RB_962, "962", rb96x_setup);
 MIPS_MACHINE_NONAME(ATH79_MACH_RB_750UPR2, "750-hb", rb750upr2_setup);
 MIPS_MACHINE_NONAME(ATH79_MACH_RB_LHG5, "lhg", rblhg_setup);
 MIPS_MACHINE_NONAME(ATH79_MACH_RB_WAP, "wap-hb", rbwap_setup);
diff --git a/target/linux/ar71xx/files/arch/mips/ath79/machtypes.h b/target/linux/ar71xx/files/arch/mips/ath79/machtypes.h
index 80f6e1d..65367ba 100644
--- a/target/linux/ar71xx/files/arch/mips/ath79/machtypes.h
+++ b/target/linux/ar71xx/files/arch/mips/ath79/machtypes.h
@@ -217,6 +217,7 @@ enum ath79_mach_type {
 	ATH79_MACH_RB_951G,			/* Mikrotik RouterBOARD 951G */
 	ATH79_MACH_RB_951U,			/* Mikrotik RouterBOARD 951Ui-2HnD */
 	ATH79_MACH_RB_952,			/* MikroTik RouterBOARD 951Ui-2nD / 952Ui-5ac2nD */
+	ATH79_MACH_RB_960,			/* MikroTik RouterBOARD 960PGS */
 	ATH79_MACH_RB_962,			/* MikroTik RouterBOARD 962UiGS-5HacT2HnT */
 	ATH79_MACH_RB_CAP,			/* Mikrotik RouterBOARD cAP2nD */
 	ATH79_MACH_RB_LHG5,			/* Mikrotik RouterBOARD LHG5 */
diff --git a/target/linux/ar71xx/image/mikrotik.mk b/target/linux/ar71xx/image/mikrotik.mk
index dc0066d..7ec1e8c 100644
--- a/target/linux/ar71xx/image/mikrotik.mk
+++ b/target/linux/ar71xx/image/mikrotik.mk
@@ -40,7 +40,7 @@ define Device/rb-nor-flash-16M
   LOADER_TYPE := elf
   KERNEL_INSTALL := 1
   KERNEL := kernel-bin | lzma | loader-kernel
-  SUPPORTED_DEVICES := rb-750-r2 rb-750up-r2 rb-750p-pbr2 rb-911-2hn rb-911-5hn rb-941-2nd rb-951ui-2nd rb-952ui-5ac2nd rb-962uigs-5hact2hnt rb-lhg-5nd rb-map-2nd rb-mapl-2nd rb-wap-2nd
+  SUPPORTED_DEVICES := rb-750-r2 rb-750up-r2 rb-750p-pbr2 rb-911-2hn rb-911-5hn rb-941-2nd rb-951ui-2nd rb-952ui-5ac2nd rb-960pgs rb-962uigs-5hact2hnt rb-lhg-5nd rb-map-2nd rb-mapl-2nd rb-wap-2nd
   IMAGE/sysupgrade.bin := append-kernel | kernel2minor -s 1024 -e | pad-to $$$$(BLOCKSIZE) | \
 	append-rootfs | pad-rootfs | append-metadata | check-size $$$$(IMAGE_SIZE)
 endef


File: /README.md
# mikrotik-rb960-on-openwrt
This patch adds support for Mikrotiks **RB960PGS**.
Also this patch do the following:
- changes that is necessary for **[mtpoe_ctrl](https://github.com/adron-s/mtpoe_ctrl)**(spidev #3) work
- some improvements for the **RB962**(ethernet switch and sfp port) and RB750(swaps eth0/eth1)


