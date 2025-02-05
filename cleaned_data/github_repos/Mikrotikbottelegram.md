# Repository Information
Name: Mikrotikbottelegram

# Directory Structure
Directory structure:
└── github_repos/Mikrotikbottelegram/
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
    │   │       ├── pack-ee43bdfcbc65d1ee2008704ab0bc85bb6ab25a9c.idx
    │   │       └── pack-ee43bdfcbc65d1ee2008704ab0bc85bb6ab25a9c.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── data.json
    ├── formatbytesbites.php
    ├── LICENSE
    ├── mikrotik.php
    ├── README.md
    ├── routeros_api.class.php
    └── src/
        ├── Bot.php
        └── FrameBot.php


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
	url = https://github.com/BangAchil/Mikrotikbottelegram.git
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
0000000000000000000000000000000000000000 04c4c8a4b57b39b6f962a173885fe7e0007bc63b vivek-dodia <vivek.dodia@icloud.com> 1738606063 -0500	clone: from https://github.com/BangAchil/Mikrotikbottelegram.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 04c4c8a4b57b39b6f962a173885fe7e0007bc63b vivek-dodia <vivek.dodia@icloud.com> 1738606063 -0500	clone: from https://github.com/BangAchil/Mikrotikbottelegram.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 04c4c8a4b57b39b6f962a173885fe7e0007bc63b vivek-dodia <vivek.dodia@icloud.com> 1738606063 -0500	clone: from https://github.com/BangAchil/Mikrotikbottelegram.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
04c4c8a4b57b39b6f962a173885fe7e0007bc63b refs/remotes/origin/master


File: /.git\refs\heads\master
04c4c8a4b57b39b6f962a173885fe7e0007bc63b


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /data.json
{
    "ipaddress": "IPROUTER",
    "user": "USER",
    "password": "PASSWORD"
}

File: /formatbytesbites.php

   <!-- 
	░▀░ █▀▀ █▀▀█ █▀▀█ █▀▀ 　 █▀▀█ █░░ █░░█ █▀▀ █▀▀ 　 █▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ █░░█ 
	▀█▀ █░░ █░░█ █▄▄▀ █▀▀ 　 █░░█ █░░ █░░█ ▀▀█ █▀▀ 　 █░░█ █░░█ █░░█ █▀▀ █▄▄▀ ░░█░░ █▄▄█ 
	▀▀▀ ▀▀▀ ▀▀▀▀ ▀░▀▀ ▀▀▀ 　 █▀▀▀ ▀▀▀ ░▀▀▀ ▀▀▀ ▀▀▀ 　 █▀▀▀ ▀▀▀▀ █▀▀▀ ▀▀▀ ▀░▀▀ ░░▀░░ ▄▄▄█  -->
   <!-- ICORE DESAIN -->




<?php
// function  format bytes
function formatBytes($size, $decimals = 0){
$unit = array(
'0' => 'Byte',
'1' => 'KiB',
'2' => 'MiB',
'3' => 'GiB',
'4' => 'TiB',
'5' => 'PiB',
'6' => 'EiB',
'7' => 'ZiB',
'8' => 'YiB'
);

for($i = 0; $size >= 1024 && $i <= count($unit); $i++){
$size = $size/1024;
}

return round($size, $decimals).' '.$unit[$i];
}

// function  format bytes2
function formatBytes2($size, $decimals = 0){
$unit = array(
'0' => 'Byte',
'1' => 'KB',
'2' => 'MB',
'3' => 'GB',
'4' => 'TB',
'5' => 'PB',
'6' => 'EB',
'7' => 'ZB',
'8' => 'YB'
);

for($i = 0; $size >= 1000 && $i <= count($unit); $i++){
$size = $size/1000;
}

return round($size, $decimals).''.$unit[$i];
}


// function  format bites
function formatBites($size, $decimals = 0){
$unit = array(
'0' => 'bps',
'1' => 'kbps',
'2' => 'Mbps',
'3' => 'Gbps',
'4' => 'Tbps',
'5' => 'Pbps',
'6' => 'Ebps',
'7' => 'Zbps',
'8' => 'Ybps'
);

for($i = 0; $size >= 1000 && $i <= count($unit); $i++){
$size = $size/1000;
}

return round($size, $decimals).' '.$unit[$i];
}
?>

File: /LICENSE
                  GNU LESSER GENERAL PUBLIC LICENSE
                       Version 2.1, February 1999

 Copyright (C) 1991, 1999 Free Software Foundation, Inc.
 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

[This is the first released version of the Lesser GPL.  It also counts
 as the successor of the GNU Library Public License, version 2, hence
 the version number 2.1.]

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
Licenses are intended to guarantee your freedom to share and change
free software--to make sure the software is free for all its users.

  This license, the Lesser General Public License, applies to some
specially designated software packages--typically libraries--of the
Free Software Foundation and other authors who decide to use it.  You
can use it too, but we suggest you first think carefully about whether
this license or the ordinary General Public License is the better
strategy to use in any particular case, based on the explanations below.

  When we speak of free software, we are referring to freedom of use,
not price.  Our General Public Licenses are designed to make sure that
you have the freedom to distribute copies of free software (and charge
for this service if you wish); that you receive source code or can get
it if you want it; that you can change the software and use pieces of
it in new free programs; and that you are informed that you can do
these things.

  To protect your rights, we need to make restrictions that forbid
distributors to deny you these rights or to ask you to surrender these
rights.  These restrictions translate to certain responsibilities for
you if you distribute copies of the library or if you modify it.

  For example, if you distribute copies of the library, whether gratis
or for a fee, you must give the recipients all the rights that we gave
you.  You must make sure that they, too, receive or can get the source
code.  If you link other code with the library, you must provide
complete object files to the recipients, so that they can relink them
with the library after making changes to the library and recompiling
it.  And you must show them these terms so they know their rights.

  We protect your rights with a two-step method: (1) we copyright the
library, and (2) we offer you this license, which gives you legal
permission to copy, distribute and/or modify the library.

  To protect each distributor, we want to make it very clear that
there is no warranty for the free library.  Also, if the library is
modified by someone else and passed on, the recipients should know
that what they have is not the original version, so that the original
author's reputation will not be affected by problems that might be
introduced by others.

  Finally, software patents pose a constant threat to the existence of
any free program.  We wish to make sure that a company cannot
effectively restrict the users of a free program by obtaining a
restrictive license from a patent holder.  Therefore, we insist that
any patent license obtained for a version of the library must be
consistent with the full freedom of use specified in this license.

  Most GNU software, including some libraries, is covered by the
ordinary GNU General Public License.  This license, the GNU Lesser
General Public License, applies to certain designated libraries, and
is quite different from the ordinary General Public License.  We use
this license for certain libraries in order to permit linking those
libraries into non-free programs.

  When a program is linked with a library, whether statically or using
a shared library, the combination of the two is legally speaking a
combined work, a derivative of the original library.  The ordinary
General Public License therefore permits such linking only if the
entire combination fits its criteria of freedom.  The Lesser General
Public License permits more lax criteria for linking other code with
the library.

  We call this license the "Lesser" General Public License because it
does Less to protect the user's freedom than the ordinary General
Public License.  It also provides other free software developers Less
of an advantage over competing non-free programs.  These disadvantages
are the reason we use the ordinary General Public License for many
libraries.  However, the Lesser license provides advantages in certain
special circumstances.

  For example, on rare occasions, there may be a special need to
encourage the widest possible use of a certain library, so that it becomes
a de-facto standard.  To achieve this, non-free programs must be
allowed to use the library.  A more frequent case is that a free
library does the same job as widely used non-free libraries.  In this
case, there is little to gain by limiting the free library to free
software only, so we use the Lesser General Public License.

  In other cases, permission to use a particular library in non-free
programs enables a greater number of people to use a large body of
free software.  For example, permission to use the GNU C Library in
non-free programs enables many more people to use the whole GNU
operating system, as well as its variant, the GNU/Linux operating
system.

  Although the Lesser General Public License is Less protective of the
users' freedom, it does ensure that the user of a program that is
linked with the Library has the freedom and the wherewithal to run
that program using a modified version of the Library.

  The precise terms and conditions for copying, distribution and
modification follow.  Pay close attention to the difference between a
"work based on the library" and a "work that uses the library".  The
former contains code derived from the library, whereas the latter must
be combined with the library in order to run.

                  GNU LESSER GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License Agreement applies to any software library or other
program which contains a notice placed by the copyright holder or
other authorized party saying it may be distributed under the terms of
this Lesser General Public License (also called "this License").
Each licensee is addressed as "you".

  A "library" means a collection of software functions and/or data
prepared so as to be conveniently linked with application programs
(which use some of those functions and data) to form executables.

  The "Library", below, refers to any such software library or work
which has been distributed under these terms.  A "work based on the
Library" means either the Library or any derivative work under
copyright law: that is to say, a work containing the Library or a
portion of it, either verbatim or with modifications and/or translated
straightforwardly into another language.  (Hereinafter, translation is
included without limitation in the term "modification".)

  "Source code" for a work means the preferred form of the work for
making modifications to it.  For a library, complete source code means
all the source code for all modules it contains, plus any associated
interface definition files, plus the scripts used to control compilation
and installation of the library.

  Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running a program using the Library is not restricted, and output from
such a program is covered only if its contents constitute a work based
on the Library (independent of the use of the Library in a tool for
writing it).  Whether that is true depends on what the Library does
and what the program that uses the Library does.

  1. You may copy and distribute verbatim copies of the Library's
complete source code as you receive it, in any medium, provided that
you conspicuously and appropriately publish on each copy an
appropriate copyright notice and disclaimer of warranty; keep intact
all the notices that refer to this License and to the absence of any
warranty; and distribute a copy of this License along with the
Library.

  You may charge a fee for the physical act of transferring a copy,
and you may at your option offer warranty protection in exchange for a
fee.

  2. You may modify your copy or copies of the Library or any portion
of it, thus forming a work based on the Library, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) The modified work must itself be a software library.

    b) You must cause the files modified to carry prominent notices
    stating that you changed the files and the date of any change.

    c) You must cause the whole of the work to be licensed at no
    charge to all third parties under the terms of this License.

    d) If a facility in the modified Library refers to a function or a
    table of data to be supplied by an application program that uses
    the facility, other than as an argument passed when the facility
    is invoked, then you must make a good faith effort to ensure that,
    in the event an application does not supply such function or
    table, the facility still operates, and performs whatever part of
    its purpose remains meaningful.

    (For example, a function in a library to compute square roots has
    a purpose that is entirely well-defined independent of the
    application.  Therefore, Subsection 2d requires that any
    application-supplied function or table used by this function must
    be optional: if the application does not supply it, the square
    root function must still compute square roots.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Library,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Library, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote
it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Library.

In addition, mere aggregation of another work not based on the Library
with the Library (or with a work based on the Library) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may opt to apply the terms of the ordinary GNU General Public
License instead of this License to a given copy of the Library.  To do
this, you must alter all the notices that refer to this License, so
that they refer to the ordinary GNU General Public License, version 2,
instead of to this License.  (If a newer version than version 2 of the
ordinary GNU General Public License has appeared, then you can specify
that version instead if you wish.)  Do not make any other change in
these notices.

  Once this change is made in a given copy, it is irreversible for
that copy, so the ordinary GNU General Public License applies to all
subsequent copies and derivative works made from that copy.

  This option is useful when you wish to copy part of the code of
the Library into a program that is not a library.

  4. You may copy and distribute the Library (or a portion or
derivative of it, under Section 2) in object code or executable form
under the terms of Sections 1 and 2 above provided that you accompany
it with the complete corresponding machine-readable source code, which
must be distributed under the terms of Sections 1 and 2 above on a
medium customarily used for software interchange.

  If distribution of object code is made by offering access to copy
from a designated place, then offering equivalent access to copy the
source code from the same place satisfies the requirement to
distribute the source code, even though third parties are not
compelled to copy the source along with the object code.

  5. A program that contains no derivative of any portion of the
Library, but is designed to work with the Library by being compiled or
linked with it, is called a "work that uses the Library".  Such a
work, in isolation, is not a derivative work of the Library, and
therefore falls outside the scope of this License.

  However, linking a "work that uses the Library" with the Library
creates an executable that is a derivative of the Library (because it
contains portions of the Library), rather than a "work that uses the
library".  The executable is therefore covered by this License.
Section 6 states terms for distribution of such executables.

  When a "work that uses the Library" uses material from a header file
that is part of the Library, the object code for the work may be a
derivative work of the Library even though the source code is not.
Whether this is true is especially significant if the work can be
linked without the Library, or if the work is itself a library.  The
threshold for this to be true is not precisely defined by law.

  If such an object file uses only numerical parameters, data
structure layouts and accessors, and small macros and small inline
functions (ten lines or less in length), then the use of the object
file is unrestricted, regardless of whether it is legally a derivative
work.  (Executables containing this object code plus portions of the
Library will still fall under Section 6.)

  Otherwise, if the work is a derivative of the Library, you may
distribute the object code for the work under the terms of Section 6.
Any executables containing that work also fall under Section 6,
whether or not they are linked directly with the Library itself.

  6. As an exception to the Sections above, you may also combine or
link a "work that uses the Library" with the Library to produce a
work containing portions of the Library, and distribute that work
under terms of your choice, provided that the terms permit
modification of the work for the customer's own use and reverse
engineering for debugging such modifications.

  You must give prominent notice with each copy of the work that the
Library is used in it and that the Library and its use are covered by
this License.  You must supply a copy of this License.  If the work
during execution displays copyright notices, you must include the
copyright notice for the Library among them, as well as a reference
directing the user to the copy of this License.  Also, you must do one
of these things:

    a) Accompany the work with the complete corresponding
    machine-readable source code for the Library including whatever
    changes were used in the work (which must be distributed under
    Sections 1 and 2 above); and, if the work is an executable linked
    with the Library, with the complete machine-readable "work that
    uses the Library", as object code and/or source code, so that the
    user can modify the Library and then relink to produce a modified
    executable containing the modified Library.  (It is understood
    that the user who changes the contents of definitions files in the
    Library will not necessarily be able to recompile the application
    to use the modified definitions.)

    b) Use a suitable shared library mechanism for linking with the
    Library.  A suitable mechanism is one that (1) uses at run time a
    copy of the library already present on the user's computer system,
    rather than copying library functions into the executable, and (2)
    will operate properly with a modified version of the library, if
    the user installs one, as long as the modified version is
    interface-compatible with the version that the work was made with.

    c) Accompany the work with a written offer, valid for at
    least three years, to give the same user the materials
    specified in Subsection 6a, above, for a charge no more
    than the cost of performing this distribution.

    d) If distribution of the work is made by offering access to copy
    from a designated place, offer equivalent access to copy the above
    specified materials from the same place.

    e) Verify that the user has already received a copy of these
    materials or that you have already sent this user a copy.

  For an executable, the required form of the "work that uses the
Library" must include any data and utility programs needed for
reproducing the executable from it.  However, as a special exception,
the materials to be distributed need not include anything that is
normally distributed (in either source or binary form) with the major
components (compiler, kernel, and so on) of the operating system on
which the executable runs, unless that component itself accompanies
the executable.

  It may happen that this requirement contradicts the license
restrictions of other proprietary libraries that do not normally
accompany the operating system.  Such a contradiction means you cannot
use both them and the Library together in an executable that you
distribute.

  7. You may place library facilities that are a work based on the
Library side-by-side in a single library together with other library
facilities not covered by this License, and distribute such a combined
library, provided that the separate distribution of the work based on
the Library and of the other library facilities is otherwise
permitted, and provided that you do these two things:

    a) Accompany the combined library with a copy of the same work
    based on the Library, uncombined with any other library
    facilities.  This must be distributed under the terms of the
    Sections above.

    b) Give prominent notice with the combined library of the fact
    that part of it is a work based on the Library, and explaining
    where to find the accompanying uncombined form of the same work.

  8. You may not copy, modify, sublicense, link with, or distribute
the Library except as expressly provided under this License.  Any
attempt otherwise to copy, modify, sublicense, link with, or
distribute the Library is void, and will automatically terminate your
rights under this License.  However, parties who have received copies,
or rights, from you under this License will not have their licenses
terminated so long as such parties remain in full compliance.

  9. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Library or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Library (or any work based on the
Library), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Library or works based on it.

  10. Each time you redistribute the Library (or any work based on the
Library), the recipient automatically receives a license from the
original licensor to copy, distribute, link with or modify the Library
subject to these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties with
this License.

  11. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Library at all.  For example, if a patent
license would not permit royalty-free redistribution of the Library by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Library.

If any portion of this section is held invalid or unenforceable under any
particular circumstance, the balance of the section is intended to apply,
and the section as a whole is intended to apply in other circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  12. If the distribution and/or use of the Library is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Library under this License may add
an explicit geographical distribution limitation excluding those countries,
so that distribution is permitted only in or among countries not thus
excluded.  In such case, this License incorporates the limitation as if
written in the body of this License.

  13. The Free Software Foundation may publish revised and/or new
versions of the Lesser General Public License from time to time.
Such new versions will be similar in spirit to the present version,
but may differ in detail to address new problems or concerns.

Each version is given a distinguishing version number.  If the Library
specifies a version number of this License which applies to it and
"any later version", you have the option of following the terms and
conditions either of that version or of any later version published by
the Free Software Foundation.  If the Library does not specify a
license version number, you may choose any version ever published by
the Free Software Foundation.

  14. If you wish to incorporate parts of the Library into other free
programs whose distribution conditions are incompatible with these,
write to the author to ask for permission.  For software which is
copyrighted by the Free Software Foundation, write to the Free
Software Foundation; we sometimes make exceptions for this.  Our
decision will be guided by the two goals of preserving the free status
of all derivatives of our free software and of promoting the sharing
and reuse of software generally.

                            NO WARRANTY

  15. BECAUSE THE LIBRARY IS LICENSED FREE OF CHARGE, THERE IS NO
WARRANTY FOR THE LIBRARY, TO THE EXTENT PERMITTED BY APPLICABLE LAW.
EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR
OTHER PARTIES PROVIDE THE LIBRARY "AS IS" WITHOUT WARRANTY OF ANY
KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE
LIBRARY IS WITH YOU.  SHOULD THE LIBRARY PROVE DEFECTIVE, YOU ASSUME
THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN
WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY
AND/OR REDISTRIBUTE THE LIBRARY AS PERMITTED ABOVE, BE LIABLE TO YOU
FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR
CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE
LIBRARY (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING
RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A
FAILURE OF THE LIBRARY TO OPERATE WITH ANY OTHER SOFTWARE), EVEN IF
SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH
DAMAGES.

                     END OF TERMS AND CONDITIONS

           How to Apply These Terms to Your New Libraries

  If you develop a new library, and you want it to be of the greatest
possible use to the public, we recommend making it free software that
everyone can redistribute and change.  You can do so by permitting
redistribution under these terms (or, alternatively, under the terms of the
ordinary General Public License).

  To apply these terms, attach the following notices to the library.  It is
safest to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least the
"copyright" line and a pointer to where the full notice is found.

    <one line to give the library's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
    USA

Also add information on how to contact you by electronic and paper mail.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the library, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the
  library `Frob' (a library for tweaking knobs) written by James Random
  Hacker.

  <signature of Ty Coon>, 1 April 1990
  Ty Coon, President of Vice

That's all there is to it!


File: /mikrotik.php
<?php
//=====================================================PLEASE NOT TO BE DELETED====================================================//

/*
 *  Base Code   : Banghasan
 *  moded    	  : BangAchil
 *  Email     	: kesumaerlangga@gmail.com
 *  Telegram  	: @bangachil
 *
 *  Name      	: Mikrotik bot telegram - php
 *  Fungsi    	: Monitoring mikortik api (Edit Rule Comingsoon )
 *  Pembuatan 	: November 2018
 *  version     : 3.1.0   last 1.0.0, 1.2.0, 1.3.0,  3.0.0
 *  Thnks to Banghasan
 *  ____________________________________________________________
*/

//=====================================================PLEASE NOT TO BE DELETED====================================================//

  //////// //////////PORT SERVICE API HARUS ENABLE DAN DEFAULT//////////////////////

 /*
 Command avalibe update time
 * /address
 * /pool
 * /ping
 * /Dhcp
 * /monitor
 * /traffic
 * /dns
 * /hotspot (aktif)(user)
 * /resource
 * /interface or (bride)
 *NEW
 * /neighbor
 * /ipbinding
 * +user
 * /remove user
 * other comingsoon
 */

 //Yang baru download silahkan ikuti langkah langkah berikut

 /************************************************************************************
 * ** methode long poolling** *
 * Perisapkan Sebuah PC atau sebuah vps
 * OS windows Linux other
 * Internet
 * InstalL Apliaksi WEBSERVER (OS WINSOWS XAMPP, APPSERV )
 * Copy file zip ini didalam sebuah folder root www/htdocs ()
 * extrack file
 * edit file data.json dengan notepad++ (recom) atau notepade
 * edit iprouter username dan pasword
 * Kemudian simpan
 * edit file mikrotik.php
 * edit token bot dan username bot
 * Kemudian simpan
 * Anda bisa langsung menjalankan bot
 * dengan cara menggunakan CMD bukan membukanya melalui webbrowser
 * Langkah - Langkah Running bot
 *   * Masuk ke tempat file mikbotam berada
 *   * tekan CTRL + klik kanan maouse
 *   * Kemudian sort cousor ke Open command window here
 *   * Muncul window CMD
 *   * Run bot dengan Mengetikan php mikrotik.php Kemudian Enter atau $ mikrotik.php
 *   * Jika anda melihat sebuah text
 *             FrameBot version 1.5
 *             Mode    : Long Polling
 *                 Debug   : ON
 *   * Selamat Bot anda berjalan
 * jika error pastikan komputer terhubung ke internet dan dapat melakukan ping ke mikrotik
 * Edit file mikrotik.php sesuai Kebutuhan anda happy coding
 *
 *****************************************************************************/

 /*
  * ** methode webhook hosting ** *
Persiapan Webhook

1.    Router wajib ip public /DNS cloud

2.    Hosting/Domain/ Cpanel / Web service

3.    Hosting dan domain WAJIB memiliki SSL

4.    Apa itu SSL https://telegra.ph/Pengertian-SSL-dan-Cara-Kerja-SSL-12-30

5.    Pastikan hosting Bisa terkoneksi dengan mirotik

6.    Baca Tutorial Buat Bot https://telegra.ph/MIKROTIK-Bot-Telegram-01-05

7.    Simpan Token Bot

8.   Extrack File yang di Download tadi

9.   Edit File Mikrotik.php Dan Data.json Mengunkan notepade ++ atau sejenisnya

10.  Jika sudah diedit
11.  Upload Seluruh Folder bot ke hosting

12.  Saatnya menjalankan Bot

13.  Menjalankannya Tidak seperti long polling

14.  Cukup dengan set webhook ke api.telegram.org

15.  Dengan cara. https://api.telegram.org/botTOKENBOTANDAINIWAJIBDIGANTI/setWebhook?url=URLDIMANA BOTMIKROTIK.PHPBERADA

Contoh :

https://api.telegram.org/botsHgGbgHhTRdCcDFfFDcFfdEwWsXcvVBhJujYt/setWebhook?url=https://mywebpagetorespondtobot/mikrotik.php .

16.  Jika muncul webhook was set

17.  Bot sudah memiliki engine
 */






require_once 'src/FrameBot.php';
$bot = new FrameBot('TOKEN_BOT', 'BOT_USERNAME');   //Ganti sesuai dengan token dan username bot

require_once ('formatbytesbites.php');
require_once ('routeros_api.class.php');




// /DHCP lease command
$bot->cmd('/dhcp|/Dhcp|!Dhcp', function ($dhcp){
               $json = file_get_contents("data.json");
    $json_a = json_decode($json, TRUE);
     //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!
    $API = new routeros_api();
    if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {

    if($dhcp=='lease'){
        $getlease = $API->comm("/ip/dhcp-server/lease/print");
        $TotalReg = count($getlease);
        $countlease = $API->comm("/ip/dhcp-server/lease/print", array(
            "count-only" => "",
        ));
        if ($countlease < 2) {
            echo "$countlease item";
        }
        else if ($countlease > 1) {
            $data1.= "$countlease items";
        };
        $data.= "<b> 🏷 Daftar DHCP Total : $TotalReg </b>\n\n";
        for ($i = 0; $i < $TotalReg; $i++) {
            $lease = $getlease[$i];
            $id = $lease['.id'];
            $addr = $lease['address'];
            $maca = $lease['mac-address'];
            $server = $lease['server'];
            $aaddr = $lease['active-address'];
            $amaca = $lease['active-mac-address'];
            $ahostname = $lease['host-name'];
            $host = str_replace("android", "AD", $ahostname);
            $status = $lease['status'];
            if ($lease['dynamic'] == "true") {
                $dy = "🎯Dynamic";
            }
            else {
                $dy = "📝Static";
            }
            $data.= "🔎 Dhcp to $addr \n  ";
            $data.= "┠  <code>$dy</code>  \n";
            $data.= "  ┠ <b>IP</b>       : <code>$addr</code>\n";
            $data.= "  ┠ <b>Mac</b>     :  <code>$maca</code>\n";
            $data.= "  ┠ <b>DHCP</b>   :  <code>$server</code>\n";
            $data.= "  ┗ <b>HOST</b>   :  <code>$host</code>\n";
            $data.= "\n ";
        }
         }else if($dhcp=='server'){
     $ARRAY = $API->comm("/ip/dhcp-server/print");
    $datatext.= "DHCP SERVER LIST\n\n";
    //kumpulkan data
    $num = count($ARRAY);
    for ($i = 0; $i < $num; $i++) {
        $name = $ARRAY[$i]['name'];
        $interface = $ARRAY[$i]['interface'];
        $lease = $ARRAY[$i]['lease-time'];
        $bootp = $ARRAY[$i]['bootp-support'];
        $authoritative = $ARRAY[$i]['authoritative'];
        $use_radius = $ARRAY[$i]['use-radius'];
        $dynamic = $ARRAY[$i]['dynamic'];
        $disable = $ARRAY[$i]['disabled'];


        $data.= "\n";
        $data.= "📋 Dhcp Server\n";
        $data.= "┠Nama :$name\n";
        $data.= "┠Interface :$interface \n";
        $data.= "┠lease-time :$lease \n";
        $data.= "┠bootp-support :$bootp \n";
        $data.= "┠authoritative :$authoritative \n";
        $data.= "┠use-radius :$use_radius \n";
        if ($dynamic == "true") {
            $data .= "┠Dynamic : Iya \n";
        } else {
            $data .= "┠Dynamic : Tidak \n";
        }
        if ($disable == "true") {
            $data .= "┗Status: ⚠ Disable\n";
        } else {
            $data .= "┗Status : ✔ Enable \n";
        }
      }

      } else {
                $texta = "Server or lease";
                $keyboard = [['!Dhcp server', '!Dhcp lease'], ['Help', 'Sembunyikan'], ];
                $replyMarkup = ['keyboard' => $keyboard, 'resize_keyboard' => true, 'setOneTimeKeyboard' => true, 'selective' => true];
                $anu['reply_markup'] = json_encode($replyMarkup);
                Bot::sendMessage($texta, $anu);
            }
        } else {
            $data = "Tidak dapat Terhubung dengan Mikrotik Coba Kembali";
        }
        $replyMarkup = ['keyboard' => [], 'remove_keyboard' => true, 'selective' => false, ];
        $anu['reply_markup'] = json_encode($replyMarkup);
        return Bot::sendMessage($data, $anu);

});
//dns command
$bot->cmd('/dns|/Dns', function () {


    $json = file_get_contents("data.json");
    $json_a = json_decode($json, TRUE);

    //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!

    $API = new routeros_api();
    if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
        $ARRAY = $API->comm("/ip/dns/print");
    $Ipserver = $ARRAY[0]['servers'];
    $dyserver = $ARRAY[0]['dynamic-servers'];
    $Allow = $ARRAY[0]['allow-remote-requests'];
    $cache = $ARRAY[0]['cache-used'];

    $text.= "🌏 DNS\n";
    $text.= "┠ Server :$Ipserver\n";
    $text.= "┠ Dynamic Server :$dyserver\n";
    if ($Allow == "true") {
        $text .= "┠ Allow Remote : Iya \n";
    } else {
        $text .= "┠ Allow Remote : Tidak \n";
    }
    $text.= "┗ Cache Used  :$cache \n";
}else{
    $text="Tidak Terkoneksi Dengan Mikrotik Coba Lagi";

}
    return Bot::sendMessage($text);
});
// /traffic command
$bot->cmd('/traffic|traffic|/Traffic', function () {

     $json = file_get_contents("data.json");
    $json_a = json_decode($json, TRUE);

    //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!

    $API = new routeros_api();

    //traffic ether1
    if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
        $getinterface = $API->comm("/interface/print");
    $interface = $getinterface[0]['name'];
    $getinterfacetraffic = $API->comm("/interface/monitor-traffic", array(
        "interface" => "ether1",  //traffic ether yang akan kita tampilkan
        "once" => "",

    ));;
    $tx = formatBites($getinterfacetraffic[0]['tx-bits-per-second'],1);
    $rx = formatBites($getinterfacetraffic[0]['rx-bits-per-second'],1);
    if ($maxtx == "" || $maxtx == "0") {
        $mxtx = formatBites(100000000,0);
        $maxtx = "100000000";
    } else {
        $mxtx = formatBites($maxtx,0);
        $maxtx = $maxtx;
    }
    if ($maxrx == "" || $maxrx == "0") {
        $mxrx = formatBites(100000000,0);
        $maxrx = "100000000";
    } else {
        $mxrx = formatBites($maxrx,0);
        $maxrx = $maxrx;
    }
    $Traffic .="Traffic\n";
    $Traffic .="====================\n\n";
    $Traffic .="Traffic ether1\n";
    $Traffic .="TX: <code>$tx / $mxtx </code>\n";
    $Traffic .="RX: <code>$rx / $mxrx </code>\n";
    $Traffic .="====================\n\n";
     //ulanggi lagi ether2
    if ($API->connect($mikrotik_ip, $mikrotik_username,$mikrotik_password))
        $getinterface = $API->comm("/interface/print");
    $interface = $getinterface[0]['name'];
    $getinterfacetraffic = $API->comm("/interface/monitor-traffic", array(
        "interface" => "ether2",  //traffic ether yang akan kita tampilkan
        "once" => "",

    ));;
    $tx = formatBites($getinterfacetraffic[0]['tx-bits-per-second'],1);
    $rx = formatBites($getinterfacetraffic[0]['rx-bits-per-second'],1);
    if ($maxtx == "" || $maxtx == "0") {
        $mxtx = formatBites(100000000,0);
        $maxtx = "100000000";
    } else {
        $mxtx = formatBites($maxtx,0);
        $maxtx = $maxtx;
    }
    if ($maxrx == "" || $maxrx == "0") {
        $mxrx = formatBites(100000000,0);
        $maxrx = "100000000";
    } else {
        $mxrx = formatBites($maxrx,0);
        $maxrx = $maxrx;
    }

    $Traffic .="Traffic ether2\n";
    $Traffic .="TX: <code>$tx / $mxtx </code>\n";
    $Traffic .="RX: <code>$rx / $mxrx </code>\n";
    $Traffic .="====================\n\n";

    //ulanggi lagi ether3
    if ($API->connect($mikrotik_ip, $mikrotik_username,$mikrotik_password))
        $getinterface = $API->comm("/interface/print");
    $interface = $getinterface[0]['name'];
    $getinterfacetraffic = $API->comm("/interface/monitor-traffic", array(
        "interface" => "ether3",   //traffic ether yang akan kita tampilkan
        "once" => "",

    ));;
    $tx = formatBites($getinterfacetraffic[0]['tx-bits-per-second'],1);
    $rx = formatBites($getinterfacetraffic[0]['rx-bits-per-second'],1);
    if ($maxtx == "" || $maxtx == "0") {
        $mxtx = formatBites(100000000,0);
        $maxtx = "100000000";
    } else {
        $mxtx = formatBites($maxtx,0);
        $maxtx = $maxtx;
    }
    if ($maxrx == "" || $maxrx == "0") {
        $mxrx = formatBites(100000000,0);
        $maxrx = "100000000";
    } else {
        $mxrx = formatBites($maxrx,0);
        $maxrx = $maxrx;
    }

    $Traffic .="Traffic ether3\n";
    $Traffic .="TX: <code>$tx / $mxtx </code>\n";
    $Traffic .="RX: <code>$rx / $mxrx </code>\n";
    $Traffic .="====================\n\n";

     //ulangi lagi ether 4
    if ($API->connect($mikrotik_ip, $mikrotik_username,$mikrotik_password))
        $getinterface = $API->comm("/interface/print");
    $interface = $getinterface[0]['name'];
    $getinterfacetraffic = $API->comm("/interface/monitor-traffic", array(
        "interface" => "ether4",   //traffic ether yang akan kita tampilkan
        "once" => "",

    ));;
    $tx = formatBites($getinterfacetraffic[0]['tx-bits-per-second'],1);
    $rx = formatBites($getinterfacetraffic[0]['rx-bits-per-second'],1);
    if ($maxtx == "" || $maxtx == "0") {
        $mxtx = formatBites(100000000,0);
        $maxtx = "100000000";
    } else {
        $mxtx = formatBites($maxtx,0);
        $maxtx = $maxtx;
    }
    if ($maxrx == "" || $maxrx == "0") {
        $mxrx = formatBites(100000000,0);
        $maxrx = "100000000";
    } else {
        $mxrx = formatBites($maxrx,0);
        $maxrx = $maxrx;
    }

    $Traffic .="Traffic ether4\n";
    $Traffic .="TX: <code>$tx / $mxtx </code>\n";
    $Traffic .="RX: <code>$rx / $mxrx </code>\n";
    $Traffic .="====================\n\n";

    //ulangi lagi ether5
    //ulangi lagi ether6 Dst.

}else{
    $Traffic="Tidak dapat terhubung ke mikrotik coba lagi";
}
        $options = [
                   'parse_mode' => 'html',
                   'reply' => true,
                   ];
    return Bot::sendMessage($Traffic, $options);
});
        //ping situs dari router test latency ke luar dan local
        //anda bisa gunakan multi command contoh /ping ping PING Ping
        //*Perbaikan Untuk bugs ping
$bot->cmd('/ping|ping|PING|Ping', function ($address){

        if ($address == NULL) {     ///Your Costum text
            $datas = "\nPing latency\n=======================\nContoh Penggunaan :\n=======================\nping google.com\nping detik.com\nping kompas.com\nping youtube.com\nMasukan Alamat Tidak Boleh pakai http://\n";

            Bot::sendMessage($datas);

        } else if (preg_match('/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\z/', $address)) {       //*detect ip address jalankan ini
            $texta = "Mohon Ditunggu Permintaan Sedang Diproses";
            Bot::sendMessage($texta);
            $json = file_get_contents("data.json");
            $json_a = json_decode($json, TRUE);

            //============ Tidak boleh diubah!!!
            $mikrotik_ip = $json_a['ipaddress'];
            $mikrotik_username = $json_a['user'];
            $mikrotik_password = $json_a['password'];
            //====================================!!!

            $API = new routeros_api();
            if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
               $PING = $API->comm("/ping", array(
                "address" => "$address",
                 "count" => "5",)); //*Jumlah ping bisa di tambah atau dikurangi
                $num = count($PING);
                $text = "<b>Ping  $address</b>\n\n";
                for ($i = 0;$i < $num;$i++) {
                    $hot = $PING[$i]['host'];
                    $status = $PING[$i]['status'];
                    $size = $PING[$i]['size'];
                    $ttl = $PING[$i]['ttl'];
                    $time = $PING[$i]['time'];
                    $packet_loss = $PING[$i]['packet-loss'];
                    $avg = $PING[$i]['avg-rtt'];
                    $packet_loss = $PING[$i]['packet-loss'];
                    if ($status == 'timeout') {
                        $text.= "<code>PING $hot \nStatus $status Loss $packet_loss% </code>\n\n";
                    } else {
                        $text.= "<code>PING $hot \nSize $size TTL $ttl \nTime $time AVG $avg</code>\n\n";
                    }
                }
            } else {
                $data = "Tidak Terkoneksi Dengan Mikrotik Coba Lagi";
            }

            return Bot::sendMessage($text);
        } elseif (preg_match('/^[-a-z0-9]+\.[a-z]{2,6}$/', strtolower($address))) {     //*detect domain jalankan ini
            $texta = "Mohon Ditunggu Permintaan Sedang Diproses";
            Bot::sendMessage($texta);
            $json = file_get_contents("data.json");
            $json_a = json_decode($json, TRUE);

            //============ Tidak boleh diubah!!!
            $mikrotik_ip = $json_a['ipaddress'];
            $mikrotik_username = $json_a['user'];
            $mikrotik_password = $json_a['password'];
            //====================================!!!

            $API = new routeros_api();
            if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
                $PING = $API->comm("/ping", array(
                "address" => "$address",
                 "count" => "5",));//*Jumlah ping bisa di tambah atau dikurangi
                $num = count($PING);
                $text = "<b>Ping  $address</b>\n\n";
                for ($i = 0;$i < $num;$i++) {
                    $hot = $PING[$i]['host'];
                    $status = $PING[$i]['status'];
                    $size = $PING[$i]['size'];
                    $ttl = $PING[$i]['ttl'];
                    $time = $PING[$i]['time'];
                    $packet_loss = $PING[$i]['packet-loss'];
                    $avg = $PING[$i]['avg-rtt'];
                    $packet_loss = $PING[$i]['packet-loss'];
                    if ($status == 'timeout') {
                        $text.= "<code>PING $hot \nStatus $status Loss $packet_loss% </code>\n\n";
                    } else {
                        $text.= "<code>PING $hot \nSize $size TTL $ttl \nTime $time AVG $avg</code>\n\n";
                    }
                }
            } else {
                $text = "Tidak Terkoneksi Dengan Mikrotik Coba Lagi";
            }
                $options = ['parse_mode' => 'html', ];
                return Bot::sendMessage($text, $options);
        }
});
//Paling sulit disini Perulangan from ping ke local untuk memonitoring Acesspoint
$bot->cmd('/Monitor|/monitor|monitor|Monitor', function (){

    $texta = "Mohon ditunggu Permintaan sedang diprosses";
    Bot::sendMessage($texta);

    $json = file_get_contents("data.json");
    $json_a = json_decode($json, TRUE);

    //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!

    $API = new routeros_api();
    if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
        $PING = $API->comm("/ping", array(
            "address" => "10.150.1.7",  //ip local target ping silahkan dirubah
            "count" => "1",
        ));
        $hot = $PING[0]['host'];
        $status = $PING[0]['status'];
        $size = $PING[0]['size'];
        $ttl = $PING[0]['ttl'];
        $time = $PING[0]['time'];
        $packet_loss = $PING[0]['packet-loss'];
        $avg = $PING[0]['avg-rtt'];
        if ($status == 'timeout') {
            $data = "PING WIFI 1 ⚠ Down \nHost :$hot Status : <b>$status</b> Loss :$packet_loss%";
        }
        else {
            $data = "PING WIFI 1 ✔ Reply  \nHost :$hot Time : <b>$time</b> Loss :$packet_loss%";
        }

        $options = ['parse_mode' => 'html', ];
        Bot::sendMessage($data, $options);   //hasil 1 akan dikirim


        $PING = $API->comm("/ping", array(
            "address" => "10.150.1.6",   //ip local target ping silahkan dirubah
            "count" => "1",
        ));
        $hot = $PING[0]['host'];
        $status = $PING[0]['status'];
        $size = $PING[0]['size'];
        $ttl = $PING[0]['ttl'];
        $time = $PING[0]['time'];
        $packet_loss = $PING[0]['packet-loss'];
        $avg = $PING[0]['avg-rtt'];
        if ($status == 'timeout') {
            $data = "PING WIFI 2 ⚠ Down \nHost :$hot Status : <b>$status</b> Loss :$packet_loss%";
        }
        else {
            $data = "PING WIFI 2  ✔ Reply \nHost :$hot Time : <b>$time</b> Loss :$packet_loss%";
        }

        $options = ['parse_mode' => 'html', ];
        Bot::sendMessage($data, $options);     //hasil 2 akan dikirim

        $PING = $API->comm("/ping", array(
            "address" => "10.150.1.1",   //ip local target ping silahkan dirubah
            "count" => "1",
        ));
        $hot = $PING[0]['host'];
        $status = $PING[0]['status'];
        $size = $PING[0]['size'];
        $ttl = $PING[0]['ttl'];
        $time = $PING[0]['time'];
        $packet_loss = $PING[0]['packet-loss'];
        $avg = $PING[0]['avg-rtt'];
        if ($status == 'timeout') {
            $data = "PING WIFI 3 ⚠ Down  \nHost :$hot Status : <b>$status</b> Loss :$packet_loss%";
        }
        else {
            $data = "PING WIFI 3  ✔ Reply  \nHost :$hot Time : <b>$time</b> Loss :$packet_loss%";
        }

        $options = ['parse_mode' => 'html', ];
        Bot::sendMessage($data, $options);    //hasil3 akan dikirim

        $PING = $API->comm("/ping", array(
            "address" => "10.150.1.2",     //ip local target ping silahkan dirubah
            "count" => "1",
        ));
        $hot = $PING[0]['host'];
        $status = $PING[0]['status'];
        $size = $PING[0]['size'];
        $ttl = $PING[0]['ttl'];
        $time = $PING[0]['time'];
        $packet_loss = $PING[0]['packet-loss'];
        $avg = $PING[0]['avg-rtt'];
        if ($status == 'timeout') {
            $data = "PING WIFI 4 ⚠ Down  \nHost :$hot Status : <b>$status</b> Loss :$packet_loss%";
        }
        else {
            $data = "PING WIFI 4 ✔ Reply  \nHost :$hot Time : <b>$time</b> Loss :$packet_loss%";
        }

        $options = ['parse_mode' => 'html', ];
        Bot::sendMessage($data, $options);      //hasil4 akan dikirim

        $PING = $API->comm("/ping", array(
            "address" => "10.150.1.3",   //ip local target ping silahkan dirubah
            "count" => "1",
        ));
        $hot = $PING[0]['host'];
        $status = $PING[0]['status'];
        $size = $PING[0]['size'];
        $ttl = $PING[0]['ttl'];
        $time = $PING[0]['time'];
        $packet_loss = $PING[0]['packet-loss'];
        $avg = $PING[0]['avg-rtt'];
        if ($status == 'timeout') {
            $data = "PING WIFI 5 ⚠ Down  \nHost :$hot Status : <b>$status</b> Loss :$packet_loss%";
        }
        else {
            $data = "PING WIFI 5 ✔ Reply  \nHost :$hot Time : <b>$time</b> Loss :$packet_loss%";
        }

        $options = ['parse_mode' => 'html', ];
        Bot::sendMessage($data, $options);      //hasil5 akan dikirim

        $PING = $API->comm("/ping", array(
            "address" => "10.150.1.9",      //ip local target ping silahkan dirubah
            "count" => "1",
        ));
        $hot = $PING[0]['host'];
        $status = $PING[0]['status'];
        $size = $PING[0]['size'];
        $ttl = $PING[0]['ttl'];
        $time = $PING[0]['time'];
        $packet_loss = $PING[0]['packet-loss'];
        $avg = $PING[0]['avg-rtt'];
        if ($status == 'timeout') {
            $data = "PING WIFI 6 ⚠ Down  \nHost :$hot Status : <b>$status</b> Loss :$packet_loss%";
        }
        else {
            $data = "PING WIFI 6 ✔ Reply   \nHost :$hot Time : <b>$time</b> Loss :$packet_loss%";
        }

        $options = ['parse_mode' => 'html', ];
        Bot::sendMessage($data, $options);      //hasil6 akan dikirim

        ///====================//*loopinglagi//====================///
        $PING = $API->comm("/ping", array(
            "address" => "10.150.1.8",     //ip local target ping silahkan dirubah
            "count" => "1",
        ));
        $hot = $PING[0]['host'];
        $status = $PING[0]['status'];
        $size = $PING[0]['size'];
        $ttl = $PING[0]['ttl'];
        $time = $PING[0]['time'];
        $packet_loss = $PING[0]['packet-loss'];
        $avg = $PING[0]['avg-rtt'];
        if ($status == 'timeout') {
            $data = "PING WIFI 7 ⚠ Down  \nHost :$hot Status : <b>$status</b> Loss :$packet_loss%";
        }
        else {
            $data = "PING WIFI 7 ✔ Reply  \nHost :$hot Time : <b>$time</b> Loss :$packet_loss%";
        }
        $options = ['parse_mode' => 'html', ];
        Bot::sendMessage($data, $options);  //hasil 7 akan dikirim
        ///====================//*SelesaIlooping//====================///


        //*Jika inggin menambahkan silahkan tambahkan sendiri
       //* Untuk menambahkan copy dari tulisan //*loopinlagi Sampai dengan //*Selesailooping dan pastekan dibawah ini (Sesuaikan kebutuhan )



    }

    else {
        $datas="Tidak dapat Terhubung dengan Mikrotik Coba Kembali";
    }
    $options = ['parse_mode' => 'html', ];
    return Bot::sendMessage($datas, $options);
});

// /interface command    pengunaan ada dua /interface dan /interface bridge
$bot->cmd('/interface|/Interface|!interface', function ($bridge) {
      $json = file_get_contents("data.json");
    $json_a = json_decode($json, TRUE);

    //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!

    $API = new routeros_api();
    if ($bridge == 'Bridge') {
        if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
            $ARRAY = $API->comm('/interface/bridge/print');
            // kumpulkan data
            $num = count($ARRAY);
            for ($i = 0;$i < $num;$i++) {
                $nama = $ARRAY[$i]['name'];
                $mtu = $ARRAY[$i]['mtu'];
                $Mac_status = $ARRAY[$i]['mac-address'];
                $pro = $ARRAY[$i]['protocol-mode'];
                $run = $ARRAY[$i]['running'];
                $Disable = $ARRAY[$i]['disabled'];
                $text.= "\n";
                $text.= "🚗 Bridge\n";
                $text.= "┠Nama : $nama\n";
                $text.= "┠Mtu : $mtu \n";
                $text.= "┠Mac : $Mac_status \n";
                $text.= "┠Protocol : $pro \n";
                if ($run == "true") {
                    $text.= "┠Active : Iya \n";
                } else {
                    $text.= "┠Active : Tidak \n";
                }
                if ($Disable == "false") {
                    $text.= "┠Disable : Tidak \n";
                } else {
                    $text.= "┠Disable : Iya \n";
                }
                $text.= "┠Disablenow  : hidden  \n";
            }
            $text.= "┗Enablenow : hidden \n";
        } else {
            $text = "Tidak dapat Terhubung dengan Mikrotik Coba Kembali ";
        }
    } else if ($bridge == 'List') {
        if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
            $ARRAY = $API->comm("/interface/print");
            $num = count($ARRAY);
            for ($i = 0;$i < $num;$i++) {
                $no = $i + 1;
                $ids = $ARRAY[$i]['.id'];
                $dataid = str_replace('*', 'id', $ids);
                $namaport = $ARRAY[$i]['name'];
                $comentport = $ARRAY[$i]['comment'];
                $typeport = $ARRAY[$i]['type'];
                $tx = formatBytes($ARRAY[$i]['rx-byte']);
                $rx = formatBytes($ARRAY[$i]['rx-byte']);
                $true = $ARRAY[$i]['running'];
                $text.= " \n ";
                $text.= "💻 Interface$no \n ";
                //Deteksi
                if ($true == "true") {
                    $text.= " ┠🆙 CONNECT \n";
                } else {
                    $text.= " ┠⚠ DISCONNECT\n";
                }
                $text.= "  ┠Nama : $namaport \n";
                $text.= "  ┠Comment : $comentport  \n";
                $text.= "  ┠Type : $typeport \n";
                $text.= "  ┠Download : $tx\n";
                $text.= "  ┠Upload : $rx\n";
                $text.= "  ┠Disablenow  : /Comingsoon  \n";
                $text.= "  ┗Enablenow : /omingsoon \n";
            }
        } else {
            $text = "Tidak dapat Terhubung dengan Mikrotik Coba Kembali";
        }
    } else {
        $texta = "Interface List or Bridge?";
        $keyboard = [['!interface List', '!interface Bridge'], ['Help', 'Sembunyikan'], ];
        $replyMarkup = ['keyboard' => $keyboard, 'resize_keyboard' => true, 'setOneTimeKeyboard' => true, 'selective' => true];
        $anu['reply_markup'] = json_encode($replyMarkup);
        Bot::sendMessage($texta, $anu);
    }
    $replyMarkup = ['keyboard' => [], 'remove_keyboard' => true, 'selective' => true, ];
    $anu['reply_markup'] = json_encode($replyMarkup);
    return Bot::sendMessage($text, $anu);
});
// /address command
$bot->cmd('/Address|/address', function () {


      $json = file_get_contents("data.json");
    $json_a = json_decode($json, TRUE);

    //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!

    $API = new routeros_api();
     if ($API->connect($mikrotik_ip, $mikrotik_username,$mikrotik_password)) {
        $ARRAY = $API->comm("/ip/address/print");
         $num = count($ARRAY);
         $text .= "Daftar IP Address $num\n";
    for ($i = 0; $i < $num; $i++) {
        $address = $ARRAY[$i]['address'];
        $network = $ARRAY[$i]['network'];
        $interface = $ARRAY[$i]['interface'];
        $dynamic = $ARRAY[$i]['dynamic'];
        $disabled = $ARRAY[$i]['disabled'];

        //ambil data
        $text .= "\n♨  $interface\n";
        $text .= "┠IP address :  $address\n";
        $text .= "┠Network    : $network \n";
        $text .= "┠interface  : $interface \n";
        //pecah kata true

        if ($dynamic == "true") {
            $text .= "┠Dynamic : Iya \n";
        } else {
            $text .= "┠Dynamic : Tidak \n";
        }

        //pecah kata false
        if ($disabled == "false") {
            $text .= "┗Disable : Tidak  \n";
        } else {
            $text .= "┗Disable : Yes  \n";
        }

    }
     }

    return Bot::sendMessage($text);
});

// /hotspot command ada dua command /hotspot aktif  dan/hotspot user
$bot->cmd('Hotspot|hotspot|/hotspot|/Hotspot|!Hotspot', function ($user) {


   $json = file_get_contents("data.json");
    $json_a = json_decode($json, TRUE);

    //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!

$API = new routeros_api();
        if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
            if ($user == 'aktif') {
                if ($serveractive != "") {
                    $gethotspotactive = $API->comm("/ip/hotspot/active/print", array("?server" => "" . $serveractive . ""));
                    $TotalReg = count($gethotspotactive);
                    $counthotspotactive = $API->comm("/ip/hotspot/active/print", array("count-only" => "", "?server" => "" . $serveractive . ""));
                } else {
                    $gethotspotactive = $API->comm("/ip/hotspot/active/print");
                    $TotalReg = count($gethotspotactive);
                    $counthotspotactive = $API->comm("/ip/hotspot/active/print", array("count-only" => "",));
                }
                $text.= "User Aktif $counthotspotactive item\n\n";
                for ($i = 0;$i < $TotalReg;$i++) {
                    $hotspotactive = $gethotspotactive[$i];
                    $id = $hotspotactive['.id'];
                    $server = $hotspotactive['server'];
                    $user = $hotspotactive['user'];
                    $address = $hotspotactive['address'];
                    $mac = $hotspotactive['mac-address'];
                    $uptime = $hotspotactive['uptime'];
                    $usesstime = $hotspotactive['session-time-left'];
                    $bytesi = formatBytes($hotspotactive['bytes-in'], 2);
                    $byteso = formatBytes($hotspotactive['bytes-out'], 2);
                    $loginby = $hotspotactive['login-by'];
                    $comment = $hotspotactive['comment'];
                    $text.= "👤 User aktif\n";
                    $text.= "┠ID :$id\n";
                    $text.= "┠SERVER :$server\n";
                    $text.= "┠USER :$user\n";
                    $text.= "┠IP :$address\n";
                    $text.= "┠UPTIME:$uptime\n";
                    $text.= "┠B IN :$bytesi\n";
                    $text.= "┠B OUT :$byteso\n";
                    $text.= "┠SESION :$usesstime\n";
                    $text.= "┗LOGIN :$loginby\n \n";
                }
            } elseif ($user == 'user') {
                $ARRAY = $API->comm("/ip/hotspot/user/print");
                $num = count($ARRAY);
                $text = "Total $num User\n\n";
                for ($i = 0;$i < $num;$i++) {
                    $no = $i;
                    $data = $ARRAY[$i]['.id'];
                    $dataid = str_replace('*', 'id', $data);
                    $data1 = $ARRAY[$i]['server'];
                    $data2 = $ARRAY[$i]['name'];
                    $data3 = $ARRAY[$i]['password'];
                    $data4 = $ARRAY[$i]['mac-address'];
                    $data5 = $ARRAY[$i]['profile'];
                    $data6 = $ARRAY[$i]['limit-uptime'];
                    $text.= "👥  ($dataid)\n";
                    $text.= "┣Server :$data1 \n";
                    $text.= "┣Nama : $data2\n";
                    $text.= "┣password : $data3 \n";
                    $text.= "┣mac : $data4\n";
                    $text.= "┣Profil : $data5\n";
                    $text.= "┣limit : $data6\n┗RemoveNow User /rEm0v$dataid\n\n";
                }
            } else {
                $texta = "User list Or aktif";
                $keyboard = [['!Hotspot user', '!Hotspot aktif'], ['Help', 'Sembunyikan'], ];

                $replyMarkup = [

                'keyboard' => $keyboard,
                'resize_keyboard' => true,
                'setOneTimeKeyboard' => true,
                'selective' => true,

                ];

                $anu['reply_markup'] = json_encode($replyMarkup);

                Bot::sendMessage($texta, $anu);
            }
        } else {
            $text = "Tidak dapat Terhubung dengan Mikrotik Coba Kembali";
        }
        $replyMarkup = [

         'keyboard' => [],
         'remove_keyboard' => true,
         'selective' => true,

         ];

        $anu['reply_markup'] = json_encode($replyMarkup);
        return Bot::sendMessage($text, $anu);
});
// /resoure command
$bot->cmd('/resource|/Resource', function () {


    $json = file_get_contents("data.json");
    $json_a = json_decode($json, TRUE);

    //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!

    $API = new routeros_api();
     if ($API->connect($mikrotik_ip, $mikrotik_username,$mikrotik_password)) {
         $health = $API->comm("/system/health/print");
         $dhealth = $health['0'];
         $ARRAY = $API->comm("/system/resource/print");
         $first = $ARRAY['0'];
         $memperc = ($first['free-memory']/$first['total-memory']);
         $hddperc = ($first['free-hdd-space']/$first['total-hdd-space']);
         $mem = ($memperc*100);
         $hdd = ($hddperc*100);

         $sehat=$dhealth['temperature'];
         $platform=$first['platform'];
         $board=$first['board-name'];
         $version=$first['version'];
         $architecture=$first['architecture-name'];
         $cpu=$first['cpu'];
         $cpuload=$first['cpu-load'];
         $uptime=$first['uptime'];
         $cpufreq=$first['cpu-frequency'];
         $cpucount=$first['cpu-count'];
         $memory=formatBytes($first['total-memory']);
         $fremem=formatBytes($first['free-memory']);
         $mempersen=number_format($mem,3);
         $hdd=formatBytes($first['total-hdd-space']);
         $frehdd=formatBytes($first['free-hdd-space']);
         $hddpersen=number_format($hdd,3);
         $sector=$first['write-sect-total'];
         $setelahreboot=$first['write-sect-since-reboot'];
         $kerusakan=$first['bad-blocks'];

        $text.="<b>📡 Resource</b>\n";
        $text.="<code>Boardname: $board</code>\n";
        $text.="<code>Platform : $platform</code>\n";
        $text.="<code>Uptime is: $uptime</code>\n";
        $text.="<code>Cpu Load : $cpuload%</code>\n";
        $text.="<code>Cpu type : $cpu</code>\n";
        $text.="<code>Cpu Hz   : $cpufreq Mhz/$cpucount core</code>\n==========================\n";
        $text.="<code>Free memory and memory \n$memory-$fremem/$mempersen %</code>\n==========================\n";
        $text.="<code>Free disk and disk      \n$hdd-$frehdd/$hddpersen %</code>\n==========================\n";
        $text.="<code>Since reboot, bad blocks \n$sector-$setelahreboot/$kerusakan%</code>\n==========================\n";
     }

    $options = ['parse_mode' => 'html', ];
    return Bot::sendMessage($text, $options);
});
 //*New Command /neighbor
$bot->cmd('/neighbor|/Neighbor', function () {
    $info = bot::message();
    $id = $info['chat']['id'];
    $iduser = $info['from']['id'];
    $msgid = $info['message_id'];

        $json = file_get_contents("data.json");
        $json_a = json_decode($json, TRUE);

    //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!
        $API = new routeros_api();
        if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
            $ARRAY3 = $API->comm("/ip/hotspot/user/print");
            $ARRAY2 = $API->comm("/system/scheduler/print");
            $ARRAY = $API->comm("/ip/neighbor/print");
            $num = count($ARRAY);
            $num2 = count($ARRAY2);
            $num3 = count($ARRAY3);
            for ($i = 0;$i < $num;$i++) {
                $no = $i + 1;
                $interfaces = "<code>" . $ARRAY[$i]['interface'] . "</code>";
                $identity = "<code>" . $ARRAY[$i]['identity'] . "</code>";
                $address = "<code>" . $ARRAY[$i]['address'] . "</code>";
                $mac = "<code>" . $ARRAY[$i]['mac-address'] . "</code>";
                $version = "<code>" . $ARRAY[$i]['version'] . "</code>";
                $uptime = "<code>" . $ARRAY[$i]['uptime'] . "</code>";
                $text.= "👥  $no\n";
                $text.= "┣Interface :  $interfaces \n";
                $text.= "┣Nama : $identity\n";
                $text.= "┣IP address : $address \n";
                $text.= "┣Mac : $mac\n";
                $text.= "┣version :    $version\n";
                $text.= "┗Uptime :     $uptime\n\n";
            }
        } else {
            $text = "Tidak dapat Terhubung dengan Mikrotik Coba Kembali";
        }
        $keyboard[] = [['text' => '💝 Mikrotik Diskusi', 'url' => 'https://t.me/mikrotikuser'], ['text' => '🌏 Tes Bot', 'url' => 'https://t.me/testingbotmikrotik'], ];
        $options = ['parse_mode' => 'html', 'reply_markup' => ['inline_keyboard' => $keyboard], ];
        Bot::sendMessage($text, $options);

});
$bot->cmd('/Pool|/pool', function () {
    $json = file_get_contents("data.json");
    $json_a = json_decode($json, TRUE);

   //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!

    $API = new routeros_api();
    if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
        $ARRAY = $API->comm("/ip/pool/print");
        // kumpulkan data
        $num = count($ARRAY);
        for ($i = 0;$i < $num;$i++) {
            $namapool = $ARRAY[$i]['name'];
            $rannge = $ARRAY[$i]['ranges'];
            $id = $ARRAY[$i]['.id'];
            $text.= "🎯 \n";
            $text.= "┠Nama :$namapool\n";
            $text.= "┠range:$rannge\n";
            $text.= "┗ID   :$id \n";
        }
    } else {
        $text = "Tidak dapat Terhubung dengan Mikrotik Coba Kembali";
    }
    $keyboard[] = [['text' => '💝 Mikrotik Diskusi', 'url' => 'https://t.me/mikrotikuser'], ['text' => '🌏 Tes Bot', 'url' => 'https://t.me/testingbotmikrotik'], ];
    $options = ['parse_mode' => 'html', 'reply_markup' => ['inline_keyboard' => $keyboard], ];
    return Bot::sendMessage($text, $options);
});

//*New Command ipbinding
$bot->cmd('/ipbinding||/Ipbinding', function () {
    $info = bot::message();
    $id = $info['chat']['id'];
    $iduser = $info['from']['id'];
    $msgid = $info['message_id'];

        $json = file_get_contents("data.json");
        $json_a = json_decode($json, TRUE);

      //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!

        $API = new routeros_api();
        if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
            $ARRAY = $API->comm('/ip/hotspot/ip-binding/getall');
            $num = count($ARRAY);
            $baris = $ARRAY;
            for ($i = 0;$i < $num;$i++) {
                $no = $i + 1;
                $id = "<code>" . $baris[$i]['.id'] . "</code>";
                $address = "<code>" . $baris[$i]['address'] . "</code>";
                $mac = "<code>" . $baris[$i]['mac-address'] . "</code>";
                $toaddress = "<code>" . $baris[$i]['to-address'] . "</code>";
                $server = "<code>" . $baris[$i]['server'] . "</code>";
                $type = "<code>" . $baris[$i]['type'] . "</code>";
                $comment = "<code>" . $baris[$i]['comment'] . "</code>";
                $disabled = "<code>" . $baris[$i]['disabled'] . "</code>";
                $text.= "👥  $no\n";
                $text.= "┣Address :  $address \n";
                $text.= "┣Mac address :  $mac \n";
                $text.= "┣To address  : $toaddress\n";
                $text.= "┣Server      : $server \n";
                $text.= "┣Type    : $type\n";
                $text.= "┗Disable : $disabled\n\n";
            }
        } else {
            $text = "Tidak dapat Terhubung dengan Mikrotik Coba Kembali";
        }
        $options = ['parse_mode' => 'html', ];
        return Bot::sendMessage($text, $options);

});
 //*Command Nambah user
 /*

  Cara Mengunakannya :

  usagenya
  Command spasi namaserver spasi userprofil spasi usernameuser spasi passworduser

  +user server profil username password

  contoh :

  +user all admin testing testing
  +user hotspot1 admin testing2 testing2

  */
$bot->cmd('+user', function ($server, $username, $password) {
    $info = bot::message();
    $id = $info['chat']['id'];
    $iduser = $info['from']['id'];
    $msgid = $info['message_id'];
    $json = file_get_contents("data.json");
    $json_a = json_decode($json, TRUE);

 //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!

    $API = new routeros_api();
    if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
        $add_user_api = $API->comm("/ip/hotspot/user/add", array(
        "server"    => $server,
        "name"     => $username,
        "password" => $password,

          ));
        $texta = json_encode($add_user_api);
        if (strpos(strtolower($texta), 'failure: already have user with this name for this server') !== false) {
            $gagal = $add_user_api['!trap'][0]['message'];
            $text.= "⛔ Gagal Menginput user baru pastikan mengisikannya dengan benar \n\n<b>KETERANGAN   :</b>\n$gagal";
        } elseif (strpos(strtolower($texta), 'ambiguous value of server, more than one possible value matches input') !== false) {
            $gagal = $add_user_api['!trap'][0]['message'];
            $text.= "⛔ Gagal Menginput user baru pastikan mengisikannya dengan benar \n\n<b>KETERANGAN   :</b>\n$gagal";
        } elseif (strpos(strtolower($texta), 'input does not match any value of server') !== false) {
            $gagal = $add_user_api['!trap'][0]['message'];
            $text.= "⛔ Gagal Menginput user baru pastikan mengisikannya dengan benar \n\n<b>KETERANGAN   :</b>\n$gagal";
        } else {
            $text.= "Berhasil Diinput\n\n";
            $text.= "<code>ID         : $add_user_api</code>\n";
            $text.= "<code>Server     : $server</code>\n";
            $text.= "<code>Name       : $username</code>\n";
            $text.= "<code>Password   : $password</code>\n";
            $dataid = str_replace('*', 'id', $add_user_api);
            $text.= "RemoveNow   : /rEm0v$dataid\n";
        }
    } else {
        $text = "Tidak dapat Terhubung dengan Mikrotik Coba Kembali";
    }
    $options = ['parse_mode' => 'html', ];
    return Bot::sendMessage($text, $options);
});

//$bot->cmd('!userbyprofil', function ($id) {
 //     //Comingsoon
//    return Bot::sendMessage($text, $options);
//});

//$bot->cmd('!Generate', function () {
    //  Comingsiin
    //   return Bot::sendMessage($text, $options);
    //   $API->disconnect();
//});

//Command Untuk Remove User
 $bot->regex('/^\/rEm0vid/', function ($matches) {
    $mess = Bot::Message();
    $id = $mess['chat']['id'];
    $isi = $mess['text'];
    if ($isi == '/rEm0vid') {
        $text.= "⛔ Gagal dihapus \n\n<b>KETERANGAN   :</b>\nTidak Ditemukan Id User";
    } else {
        $id = str_replace('/rEm0vid', '*', $isi);
        $ids = str_replace('@Mikrotikinbot', '', $id);/////////////////////////PERHATIKAN INI ISIKAN SESUAI DENGAN  USERNAMEBOT DIAWALI DENGAN @  (manualdulu sambil buat belajar dan kegiatan keik mengetik :-D )
        $json = file_get_contents("data.json");
        $json_a = json_decode($json, TRUE);

    //============ Tidak boleh diubah!!!
    $mikrotik_ip = $json_a['ipaddress'];
    $mikrotik_username = $json_a['user'];
    $mikrotik_password = $json_a['password'];
    //====================================!!!

        $API = new routeros_api();
        if ($API->connect($mikrotik_ip, $mikrotik_username, $mikrotik_password)) {
            $ARRAY = $API->comm("/ip/hotspot/user/print", array("?.id" => $ids,));
            $data1 = $ARRAY[0]['.id'];
            $data1 = $ARRAY[0]['profile'];
            $data2 = $ARRAY[0]['name'];
            $data3 = $ARRAY[0]['password'];
            $ARRAY2 = $API->comm("/ip/hotspot/user/remove", array("numbers" => $ids,));
            $texta = json_encode($ARRAY2);
            if (strpos(strtolower($texta), 'no such item') !== false) {
                $gagal = $ARRAY2['!trap'][0]['message'];
                $text.= "⛔ Gagal dihapus \n\n<b>KETERANGAN   :</b>\n$gagal";
            } elseif (strpos(strtolower($texta), 'invalid internal item number') !== false) {
                $gagal = $ARRAY2['!trap'][0]['message'];
                $text.= "⛔ Gagal dihapus \n\n<b>KETERANGAN   :</b>\n$gagal";
            } elseif (strpos(strtolower($texta), 'default trial user can not be removed') !== false) {
                $gagal = $ARRAY2['!trap'][0]['message'];
                $text.= "⛔ Gagal dihapus \n\n<b>KETERANGAN   :</b>\n$gagal";
            } else {
                $text.= "Berhasil Dihapus\n\n";
                $text.= "<code>ID         : $ids</code>\n";
                $text.= "<code>Server     : $data1</code>\n";
                $text.= "<code>Name       : $data2</code>\n";
                $text.= "<code>Password   : $data3</code>\n";
                sleep(2);
                $ARRAY3 = $API->comm("/ip/hotspot/user/print");
                $jumlah = count($ARRAY3);
                $text.= "Jumlah user saat ini : $jumlah user";
            }
        } else {
            $text = "Gagal Periksa sambungan Kerouter";
        }
    }
    $options = ['parse_mode' => 'html', ];
    $texta = json_encode($ARRAY2);
    return Bot::sendMessage($text, $options);
});
// Simple whoami command
//contoh command
$bot->cmd('/start', function () {

       $text="Mikrotik bot telegram see command in /help";
    return Bot::sendMessage($text);
});


 //TAMBAHAKAN DISINI UNTUK CASTOM PERINTAH///



// slice text by space
$bot->cmd('!help|/help|Help', function ()
{

    $text.= "Apa yang bisa saya bantu?\n";
    $text.= "Daftar Perintah\n";
    $text.= "/Monitor - Monitoring Wifi\n";
    $text.= "/ping - Ping local / Internet\n";
    $text.= "/Dhcp - Dhcp view (lease)\n";
    $text.= "/Address - Address list\n";
    $text.= "/Pool - Pool list view\n";
    $text.= "/Traffic - Traffic view\n";
    $text.= "/Interface - Interface view(bride)\n";
    $text.= "/Dns - Dns view\n";
    $text.= "/Hotspot - Hotspot view(aktif)(user)\n";
    $text.= "/Resource - Dns view\n";
    $text.= "/Neighbor\n";
    $text.= "/Ipbinding\n";
    $text.= "Other Comingsoon\n";

 $keyboard = [
        ['Monitor','Ping google.com'], ['Hotspot'],['Help','Sembunyikan'],
    ];

    $replyMarkup = [
        'keyboard'        => $keyboard,
        'resize_keyboard' => true,
        'setOneTimeKeyboard' => true,
        'selective' => true,
    ];
      $anu['reply_markup'] = json_encode($replyMarkup);
    return Bot::sendMessage($text, $anu);
});


$bot->cmd('Sembunyikan|!Sembunyikan', function ()
{
    $text="disembunyikan";

    $replyMarkup = [
            'keyboard' => [],
            'remove_keyboard' => true,
            'selective' => false,
          ];
    $anu['reply_markup'] = json_encode($replyMarkup);
    return Bot::sendMessage($text, $anu);
});


$bot->on('new_chat_member', function() {

    $info=bot::message();
    $nama=$info['new_chat_member']['first_name'];
    $grup=$info['chat']['title'];

    $text.="Selamat datang  💘 " . $nama."\n\nSaat ini Anda  Berada di Grup \n<b>$grup</b>";

   $options = ['parse_mode' => 'html', ];

    return Bot::sendMessage($text, $options);
});

$bot->run();


File: /README.md
# Mikrotikbottelegram
   bot yang dibuat dengan memanfaatkan API dari Mikrotik client telegram. Keuntungan Bot ini yaitu memiliki fitur semua yang ada pada mikrotik. Sedangkan kekurangannya adalah Tidak suport Untuk Multi user anda harus membuat bot sendiri sengan source code yang ada DAN demikian terkait privasi masing masing pengguna mikrotik .          


File: /routeros_api.class.php
<?php
/*****************************
 *
 * RouterOS PHP API class v1.5
 * Author: Denis Basta
 * Contributors:
 *    Nick Barnes
 *    Ben Menking (ben [at] infotechsc [dot] com)
 *    Jeremy Jefferson (http://jeremyj.com)
 *    Cristian Deluxe (djcristiandeluxe [at] gmail [dot] com)
 *
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 ******************************/

class routeros_api
{
    var $debug = false;      // Show debug information
    var $error_no;           // Variable for storing connection error number, if any
    var $error_str;          // Variable for storing connection error text, if any
    var $attempts = 1;       // Connection attempt count
    var $connected = false;  // Connection state
    var $delay = 1;          // Delay between connection attempts in seconds
    var $port = 8728;        // Port to connect to
    var $timeout = 1;        // Connection attempt timeout and data read timeout
    var $socket;             // Variable for storing socket resource
    
    /**
     * Print text for debug purposes
     *
     * @param string      $text       Text to print
     *
     * @return void
     */
    function debug($text)
    {
        if ($this->debug)
            echo $text . "\n";
    }
	
	
    /**
     * 
     *
     * @param string        $length
     *
     * @return void
     */
    function encode_length($length)
    {
        if ($length < 0x80) {
            $length = chr($length);
        } else if ($length < 0x4000) {
            $length |= 0x8000;
            $length = chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } else if ($length < 0x200000) {
            $length |= 0xC00000;
            $length = chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } else if ($length < 0x10000000) {
            $length |= 0xE0000000;
            $length = chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } else if ($length >= 0x10000000)
            $length = chr(0xF0) . chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        return $length;
    }
	
	
    /**
     * Login to RouterOS
     *
     * @param string      $ip         Hostname (IP or domain) of the RouterOS server
     * @param string      $login      The RouterOS username
     * @param string      $password   The RouterOS password
     *
     * @return boolean                If we are connected or not
     */
    function connect($ip, $login, $password)
    {
        for ($ATTEMPT = 1; $ATTEMPT <= $this->attempts; $ATTEMPT++) {
            $this->connected = false;
            $this->debug('Connection attempt #' . $ATTEMPT . ' to ' . $ip . ':' . $this->port . '...');
            $this->socket = @fsockopen($ip, $this->port, $this->error_no, $this->error_str, $this->timeout);
            if ($this->socket) {
                socket_set_timeout($this->socket, $this->timeout);
                $this->write('/login');
                $RESPONSE = $this->read(false);
                if ($RESPONSE[0] == '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $RESPONSE[1], $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret' && strlen($MATCHES[0][1]) == 32) {
                            $this->write('/login', false);
                            $this->write('=name=' . $login, false);
                            $this->write('=response=00' . md5(chr(0) . $password . pack('H*', $MATCHES[0][1])));
                            $RESPONSE = $this->read(false);
                            if ($RESPONSE[0] == '!done') {
                                $this->connected = true;
                                break;
                            }
                        }
                    }
                }
                fclose($this->socket);
            }
            sleep($this->delay);
        }
        if ($this->connected){
            $this->debug('Connected...');			
        }else{
            $this->debug('Error...');			
        }
        return $this->connected;
    }
	
	
    /**
     * Disconnect from RouterOS
     *
     * @return void
     */
    function disconnect()
    {
        fclose($this->socket);
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
    function parse_response($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array(
                    '!fatal',
                    '!re',
                    '!trap'
                ))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else
                        $CURRENT =& $PARSED[$x][];
                } else if ($x != '!done') {
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
        } else
            return array();
    }
	
	
    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    function parse_response4smarty($response)
    {
        if (is_array($response)) {
            $PARSED  = array();
            $CURRENT = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array(
                    '!fatal',
                    '!re',
                    '!trap'
                ))) {
                    if ($x == '!re')
                        $CURRENT =& $PARSED[];
                    else
                        $CURRENT =& $PARSED[$x][];
                } else if ($x != '!done') {
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
                $PARSED[$key] = $this->array_change_key_name($value);
            }
            return $PARSED;
            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }
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
    function array_change_key_name(&$array)
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
    function read($parse = true)
    {
        $RESPONSE = array();
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
            if ($_ == "!done")
                $receiveddone = true;
            $STATUS = socket_get_status($this->socket);
            if ($LENGTH > 0)
                $this->debug('>>> [' . $LENGTH . ', ' . $STATUS['unread_bytes'] . ']' . $_);
            if ((!$this->connected && !$STATUS['unread_bytes']) || ($this->connected && !$STATUS['unread_bytes'] && $receiveddone))
                break;
        }
        if ($parse)
            $RESPONSE = $this->parse_response($RESPONSE);
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
    function write($command, $param2 = true)
    {
        if ($command) {
            $data = explode("\n", $command);
            foreach ($data as $com) {
                $com = trim($com);
                fwrite($this->socket, $this->encode_length(strlen($com)) . $com);
                $this->debug('<<< [' . strlen($com) . '] ' . $com);
            }
            if (gettype($param2) == 'integer') {
                fwrite($this->socket, $this->encode_length(strlen('.tag=' . $param2)) . '.tag=' . $param2 . chr(0));
                $this->debug('<<< [' . strlen('.tag=' . $param2) . '] .tag=' . $param2);
            } else if (gettype($param2) == 'boolean')
                fwrite($this->socket, ($param2 ? chr(0) : ''));
            return true;
        } else
            return false;
    }
	
	
    /**
     * Write (send) data to Router OS
     *
     * @param string      $com        A string with the command to send
     * @param array       $arr        An array with arguments or queries
     *
     * @return array                  Array with parsed
     */
    function comm($com, $arr = array())
    {
        $count = count($arr);
        $this->write($com, !$arr);
        $i = 0;
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
        return $this->read();
    }
}
?>


File: /src\Bot.php
<?php
/**
 * Bot.php.
 *
 *
 * @author Radya <radya@gmx.com>
 *
 * @link https://github.com/radyakaze/FrameBot
 *
 * @license GPL-3.0
 */

/**
 * Class Bot.
 */
class Bot
{
    /**
     * Bot response debug.
     *
     * @var string
     */
    public static $debug = '';

    /**
     * Send request to telegram api server.
     *
     * @param string $action
     * @param array  $data   [optional]
     *
     * @return array|bool
     */
    public static function send($action = 'sendMessage', $data = [])
    {
        $upload = false;
        $actionUpload = ['sendPhoto', 'sendAudio', 'sendDocument', 'sendSticker', 'sendVideo', 'sendVoice'];

        if (in_array($action, $actionUpload)) {
            $field = str_replace('send', '', strtolower($action));

            if (is_file($data[$field])) {
                $upload = true;
                $data[$field] = self::curlFile($data[$field]);
            }
        }

        $needChatId = ['sendMessage', 'forwardMessage', 'sendPhoto', 'sendAudio', 'sendDocument', 'sendSticker', 'sendVideo', 'sendVoice', 'sendLocation', 'sendVenue', 'sendContact', 'sendChatAction', 'editMessageText', 'editMessageCaption', 'editMessageReplyMarkup', 'sendGame'];
        if (in_array($action, $needChatId) && !isset($data['chat_id'])) {
            $getUpdates = FrameBot::$getUpdates;
            if (isset($getUpdates['callback_query'])) {
                $getUpdates['callback_query'];
            }
            $data['chat_id'] = $getUpdates['message']['chat']['id'];
            // Reply message
            if (!isset($data['reply_to_message_id']) && isset($data['reply']) && $data['reply'] === true) {
                $data['reply_to_message_id'] = $getUpdates['message']['message_id'];
                unset($data['reply']);
            }
        }

        if (isset($data['reply_markup']) && is_array($data['reply_markup'])) {
            $data['reply_markup'] = json_encode($data['reply_markup']);
        }

        $ch = curl_init();
        $options = [
            CURLOPT_URL            => 'https://api.telegram.org/bot'.FrameBot::$token.'/'.$action,
            CURLOPT_POST           => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_SSL_VERIFYHOST => false,
            CURLOPT_SSL_VERIFYPEER => false,
        ];

        if (is_array($data)) {
            $options[CURLOPT_POSTFIELDS] = $data;
        }

        if ($upload !== false) {
            $options[CURLOPT_HTTPHEADER] = ['Content-Type: multipart/form-data'];
        }

        curl_setopt_array($ch, $options);

        $result = curl_exec($ch);

        if (curl_errno($ch)) {
            echo curl_error($ch)."\n";
        }
        $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);

        if (FrameBot::$debug && $action != 'getUpdates') {
            self::$debug .= 'Method: '.$action."\n";
            self::$debug .= 'Data: '.str_replace("Array\n", '', print_r($data, true))."\n";
            self::$debug .= 'Response: '.$result."\n";
        }

        if ($httpcode == 401) {
            throw new Exception('Incorect bot token');
            return false;
        } else {
            return $result;
        }
    }

    /**
     * Answer Inline.
     *
     * @param array $results
     * @param array $options
     *
     * @return string
     */
    public static function answerInlineQuery($results, $options = [])
    {
        if (!empty($options)) {
            $data = $options;
        }

        if (!isset($options['inline_query_id'])) {
            $get = FrameBot::$getUpdates;
            $data['inline_query_id'] = $get['inline_query']['id'];
        }

        $data['results'] = json_encode($results);

        return self::send('answerInlineQuery', $data);
    }

    /**
     * Answer Callback.
     *
     * @param string $text
     * @param array  $options [optional]
     *
     * @return string
     */
    public static function answerCallbackQuery($text, $options = [])
    {
        $options['text'] = $text;

        if (!isset($options['callback_query_id'])) {
            $get = FrameBot::$getUpdates;
            $options['callback_query_id'] = $get['callback_query']['id'];
        }

        return self::send('answerCallbackQuery', $options);
    }

    /**
     * Create curl file.
     *
     * @param string $path
     *
     * @return string
     */
    private static function curlFile($path)
    {
        // PHP 5.5 introduced a CurlFile object that deprecates the old @filename syntax
        // See: https://wiki.php.net/rfc/curl-file-upload
        if (function_exists('curl_file_create')) {
            return curl_file_create($path);
        } else {
            // Use the old style if using an older version of PHP
            return "@$path";
        }
    }

    /**
     * Get message properties.
     *
     * @return array
     */
    public static function message()
    {
        $get = FrameBot::$getUpdates;
        if (isset($get['message'])) {
            return $get['message'];
        } elseif (isset($get['callback_query'])) {
            return $get['callback_query'];
        } elseif (isset($get['inline_query'])) {
            return $get['inline_query'];
        } elseif (isset($get['edited_message'])) {
            return $get['edited_message'];
        } elseif (isset($get['channel_post'])) {
            return $get['channel_post'];
        } elseif (isset($get['edited_channel_post'])) {
            return $get['edited_channel_post'];
        } else {
            return [];
        }
    }

    /**
     * Mesage type.
     *
     * @return string
     */
    public static function type()
    {
        $getUpdates = FrameBot::$getUpdates;

        if (isset($getUpdates['message']['text'])) {
            return 'text';
        } elseif (isset($getUpdates['message']['photo'])) {
            return 'photo';
        } elseif (isset($getUpdates['message']['video'])) {
            return 'video';
        } elseif (isset($getUpdates['message']['audio'])) {
            return 'audio';
        } elseif (isset($getUpdates['message']['voice'])) {
            return 'voice';
        } elseif (isset($getUpdates['message']['document'])) {
            return 'document';
        } elseif (isset($getUpdates['message']['sticker'])) {
            return 'sticker';
        } elseif (isset($getUpdates['message']['venue'])) {
            return 'venue';
        } elseif (isset($getUpdates['message']['location'])) {
            return 'location';
        } elseif (isset($getUpdates['inline_query'])) {
            return 'inline';
        } elseif (isset($getUpdates['callback_query'])) {
            return 'callback';
        } elseif (isset($getUpdates['message']['new_chat_member'])) {
            return 'new_chat_member';
        } elseif (isset($getUpdates['message']['left_chat_member'])) {
            return 'left_chat_member';
        } elseif (isset($getUpdates['message']['new_chat_title'])) {
            return 'new_chat_title';
        } elseif (isset($getUpdates['message']['new_chat_photo'])) {
            return 'new_chat_photo';
        } elseif (isset($getUpdates['message']['delete_chat_photo'])) {
            return 'delete_chat_photo';
        } elseif (isset($getUpdates['message']['group_chat_created'])) {
            return 'group_chat_created';
        } elseif (isset($getUpdates['message']['channel_chat_created'])) {
            return 'channel_chat_created';
        } elseif (isset($getUpdates['message']['supergroup_chat_created'])) {
            return 'supergroup_chat_created';
        } elseif (isset($getUpdates['message']['migrate_to_chat_id'])) {
            return 'migrate_to_chat_id';
        } elseif (isset($getUpdates['message']['migrate_from_chat_id '])) {
            return 'migrate_from_chat_id ';
        } elseif (isset($getUpdates['edited_message'])) {
            return 'edited';
        } elseif (isset($getUpdates['message']['game'])) {
            return 'game';
        } elseif (isset($getUpdates['channel_post'])) {
            return 'channel';
        } elseif (isset($getUpdates['edited_channel_post'])) {
            return 'edited_channel';
        } else {
            return 'unknown';
        }
    }

    /**
     * Create an action.
     *
     * @param string $name
     * @param array  $args
     *
     * @return array
     */
    public static function __callStatic($action, $args)
    {
        $param = [];
        $firstParam = [
            'sendMessage'           => 'text',
            'sendPhoto'             => 'photo',
            'sendVideo'             => 'video',
            'sendAudio'             => 'audio',
            'sendVoice'             => 'voice',
            'sendDocument'          => 'document',
            'sendSticker'           => 'sticker',
            'sendVenue'             => 'venue',
            'sendChatAction'        => 'action',
            'setWebhook'            => 'url',
            'getUserProfilePhotos'  => 'user_id',
            'getFile'               => 'file_id',
            'getChat'               => 'chat_id',
            'leaveChat'             => 'chat_id',
            'getChatAdministrators' => 'chat_id',
            'getChatMembersCount'   => 'chat_id',
            'sendGame'              => 'game_short_name',
            'getGameHighScores'     => 'user_id',
        ];

        if (!isset($firstParam[$action])) {
            if (isset($args[0]) && is_array($args[0])) {
                $param = $args[0];
            }
        } else {
            $param[$firstParam[$action]] = $args[0];
            if (isset($args[1]) && is_array($args[1])) {
                $param = array_merge($param, $args[1]);
            }
        }

        return call_user_func_array('self::send', [$action, $param]);
    }
}


File: /src\FrameBot.php
<?php
/**
 * FrameBot.php.
 *
 * Hasanudin <banghasan@gmail.com>
 * Telegram @hasanuinhs
 *
 * Fork dari: radyakaze/phptelebot
 */

/**
 * Class FrameBot.
 */
class FrameBot
{
    public static $getUpdates = [];
    protected $_command = [];
    protected $_onMessage = [];
    public static $token = '';
    protected static $username = '';
    public static $debug = true;
    protected static $version = '1.5';

    private $callback_before;
    private $callback_after;

    /**
     * FrameBot Constructor.
     *
     * @param string $token
     * @param string $username
     * @param callback
     */
    public function __construct($token, $username = '')
    {
        // Check php version
        if (version_compare(phpversion(), '5.4', '<')) {
            die("FrameBot needs to use PHP 5.4 or higher.\n");
        }

        // Check curl
        if (!function_exists('curl_version')) {
            die("cURL is NOT installed on this server.\n");
        }

        // Check bot token
        if (empty($token)) {
            die("Bot token should not be empty!\n");
        }

        self::$token = $token;
        self::$username = $username;

        $this->callback_before = function () {
        };
        $this->callback_after = function () {
        };
    }

    /**
     * Command.
     *
     * @param string          $command
     * @param callable|string $answer
     */
    public function cmd($command, $answer)
    {
        if ($command != '*') {
            $this->_command[$command] = $answer;
        }

        if (strrpos($command, '*') !== false) {
            $this->_onMessage['text'] = $answer;
        }
    }

    /**
     * Events.
     *
     * @param string          $types
     * @param callable|string $answer
     */
    public function on($types, $answer)
    {
        $types = explode('|', $types);
        foreach ($types as $type) {
            $this->_onMessage[$type] = $answer;
        }
    }

    /**
     * Custom regex for command.
     *
     * @param string          $regex
     * @param callable|string $answer
     */
    public function regex($regex, $answer)
    {
        $this->_command['customRegex:'.$regex] = $answer;
    }

    /**
     * Run telebot.
     *
     * @return bool
     */
    public function run()
    {
        try {
            if (php_sapi_name() == 'cli') {
                echo 'FrameBot |mikbotam version '.self::$version;
                echo "\nMode\t: Long Polling\n";
                $options = getopt('q', ['quiet']);
                if (isset($options['q']) || isset($options['quiet'])) {
                    self::$debug = false;
                }
                echo "Debug\t: ".(self::$debug ? 'ON' : 'OFF')."\n";
                $this->longPoll();
            } else {
                $this->webhook();
            }

            return true;
        } catch (Exception $e) {
            echo $e->getMessage()."\n";

            return false;
        }
    }

    /**
     * Webhook Mode.
     */
    private function webhook()
    {
        if ($_SERVER['REQUEST_METHOD'] == 'POST' && $_SERVER['CONTENT_TYPE'] == 'application/json') {
            self::$getUpdates = json_decode(file_get_contents('php://input'), true);
            echo $this->process();

            //echo "\n ---------- callback_after ----------- \n";
            call_user_func($this->callback_after);
        } else {
            http_response_code(400);
            throw new Exception('Jalankan menggunakan CMD/webhook bukan membukanya melalui webbrowser');
        }
    }

    /**
     * Long Poll Mode.
     *
     * @throws Exception
     */
    private function longPoll()
    {
        $offset = 0;
        while (true) {
            $req = json_decode(Bot::send('getUpdates', ['offset' => $offset, 'timeout' => 30]), true);

            // Check error.
            if (isset($req['error_code'])) {
                if ($req['error_code'] == 404) {
                    $req['description'] = 'Incorrect bot token';
                }
                throw new Exception($req['description']);
            }

            if (!empty($req['result'])) {
                foreach ($req['result'] as $update) {
                    self::$getUpdates = $update;
                    $process = $this->process();

                    if (self::$debug) {
                        $line = "\n--------------------\n";
                        $outputFormat = "$line %s $update[update_id] $line%s";
                        echo sprintf($outputFormat, 'Query ID :', json_encode($update));
                        echo sprintf($outputFormat, 'Response for :', Bot::$debug ?: $process ?: '--NO RESPONSE--');
                        // reset debug
                        Bot::$debug = '';
                    }
                    $offset = $update['update_id'] + 1;

                    // echo "\n ---------- callback_after ----------- \n";
                    call_user_func($this->callback_after);
                }
            }

            // Delay 1 second
            sleep(1);
        }
    }

    /*
     * Fungsi Proses Global Before
     * Perubahan panggilan fungsi global sebelum menjalankan proses
     */

    public function before($callback)
    {
        // cek ricek
        if (is_callable($callback)) {
            // call_user_func($callback);
            $this->callback_before = $callback;
        }
    }

    /*
     * Fungsi Proses Global After
     * Perubahan panggilan fungsi global, sesudah menjalankan proses
     */

    public function after($callback)
    {
        // cek ricek
        if (is_callable($callback)) {
            $this->callback_after = $callback;
        }
    }

    /**
     * Process the message.
     *
     * @return string
     */
    private function process()
    {
        $get = self::$getUpdates;
        $run = false;

        call_user_func($this->callback_before);

        if (Bot::type() == 'text') {
            $customRegex = false;
            foreach ($this->_command as $cmd => $call) {
                if (substr($cmd, 0, 12) == 'customRegex:') {
                    $regex = substr($cmd, 12);
                    // Remove bot username from command
                     if (self::$username != '') {
                         $get['message']['text'] = preg_replace('/^\/(.*)@'.self::$username.'(.*)/', '/$1$2', $get['message']['text']);
                     }
                    $customRegex = true;
                } else {
                    $regex = '/^(?:'.addcslashes($cmd, '/\+*?[^]$(){}=!<>:-').')'.(self::$username ? '(?:@'.self::$username.')?' : '').'(?:\s(.*))?$/';
                }
                if ($get['message']['text'] != '*' && preg_match($regex, $get['message']['text'], $matches)) {
                    $run = true;
                    if ($customRegex) {
                        $param = [$matches];
                    } else {
                        $param = isset($matches[1]) ? $matches[1] : '';
                    }
                    break;
                }
            }
        }

        if (isset($this->_onMessage) && $run === false) {
            if (in_array(Bot::type(), array_keys($this->_onMessage))) {
                $run = true;
                $call = $this->_onMessage[Bot::type()];
            } elseif (isset($this->_onMessage['*'])) {
                $run = true;
                $call = $this->_onMessage['*'];
            }

            if ($run) {
                switch (Bot::type()) {
                    case 'callback':
                        $param = $get['callback_query']['data'];
                    break;
                    case 'inline':
                        $param = $get['inline_query']['query'];
                    break;
                    case 'location':
                        $param = [$get['message']['location']['longitude'], $get['message']['location']['latitude']];
                    break;
                    case 'text':
                        $param = $get['message']['text'];
                    break;
                    default:
                        $param = '';
                    break;
                }
            }
        }

        if ($run) {
            if (is_callable($call)) {
                if (!is_array($param)) {
                    $count = count((new ReflectionFunction($call))->getParameters());
                    if ($count > 1) {
                        $param = array_pad(explode(' ', $param, $count), $count, '');
                    } else {
                        $param = [$param];
                    }
                }

                return call_user_func_array($call, $param);
            } else {
                if (!isset($get['inline_query'])) {
                    return Bot::send('sendMessage', ['text' => $call]);
                }
            }
        }
    }
}

require_once __DIR__.'/Bot.php';


