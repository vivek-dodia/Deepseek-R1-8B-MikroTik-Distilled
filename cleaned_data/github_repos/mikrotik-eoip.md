# Repository Information
Name: mikrotik-eoip

# Directory Structure
Directory structure:
└── github_repos/mikrotik-eoip/
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
    │   │       ├── pack-1f8d822d3a3ae78f11f72d852543ea93444fd651.idx
    │   │       └── pack-1f8d822d3a3ae78f11f72d852543ea93444fd651.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── eoip.c
    ├── eoip.cfg
    ├── Makefile
    ├── minGlue.h
    ├── minIni.c
    ├── minIni.h
    ├── vip.c
    └── vip.cfg


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
	url = https://github.com/LynxChaus/mikrotik-eoip.git
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
0000000000000000000000000000000000000000 abafbc2c6a87bfe746dbbf1b45589a919bf04bfd vivek-dodia <vivek.dodia@icloud.com> 1738606378 -0500	clone: from https://github.com/LynxChaus/mikrotik-eoip.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 abafbc2c6a87bfe746dbbf1b45589a919bf04bfd vivek-dodia <vivek.dodia@icloud.com> 1738606378 -0500	clone: from https://github.com/LynxChaus/mikrotik-eoip.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 abafbc2c6a87bfe746dbbf1b45589a919bf04bfd vivek-dodia <vivek.dodia@icloud.com> 1738606378 -0500	clone: from https://github.com/LynxChaus/mikrotik-eoip.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
abafbc2c6a87bfe746dbbf1b45589a919bf04bfd refs/remotes/origin/master


File: /.git\refs\heads\master
abafbc2c6a87bfe746dbbf1b45589a919bf04bfd


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
*.[oa]
*~
eoip
vip


File: /eoip.c
/*
    file:   eoip.c
    Authors: Denys Fedoryshchenko aka NuclearCat <nuclearcat (at) nuclearcat.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.*
*/
#ifndef __UCLIBC__
#define _GNU_SOURCE
#endif
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netinet/if_ether.h>
#include <net/ethernet.h>
#include <netinet/ether.h>
#include <linux/if_tun.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <net/if.h>
#include <poll.h>
#include <unistd.h>
#include <err.h>
#include <signal.h>
#include <assert.h>
#include <pthread.h>
#include <limits.h>
#include <asm/byteorder.h>
#include "minIni.h"

/* In theory maximum payload that can be handled is 65536, but if we use vectorized
   code with preallocated buffers - it is waste of space, especially for embedded setup.
   So if you want oversized packets - increase MAXPAYLOAD up to 65536 (or a bit less)
   If your choice performance - more vectors, to avoid expensive context switches
   TODO: readv, writev
*/

#define LINUX_THREAD_STACK_SIZE (PTHREAD_STACK_MIN * 2)
#ifdef __UCLIBC__
#define MAXPAYLOAD (2048)
#define PREALLOCBUF 4
#define MAXRINGBUF  4
#else
#define MAXPAYLOAD (2048)
#define PREALLOCBUF 32
#define MAXRINGBUF  64
#endif

#define sizearray(a)  (sizeof(a) / sizeof((a)[0]))

typedef struct {
	struct sockaddr_in daddr;
	int id;
	int fd;
	struct ifreq ifr;
	char name[65];
	int dynamic;
#ifndef __UCLIBC__
	int cpu;
#endif
} Tunnel;

struct thr_rx {
	int raw_socket;
};

struct thr_tx {
	int raw_socket;
#ifndef __UCLIBC__
	int cpu;
#endif
	Tunnel *tunnel;
};

struct gre_hdr {
	uint32_t header;
	uint16_t payload_size;
	uint16_t tunnel_id;
} __attribute__ ((__packed__));

int numtunnels;
Tunnel *tunnels;
pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;

static void term_handler(int s)
{
	int fd, i;
	Tunnel *tunnel;

	if ((fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
		perror("socket() failed");
		exit(-1);
	}
	for (i = 0; i < numtunnels; i++) {
		tunnel = tunnels + i;
		close(tunnel->fd);
	}

	close(fd);
	exit(0);
}

static int open_tun(Tunnel * tunnel)
{
	int fd;

	if ((fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
		perror("socket() failed");
		return 1;
	}
	if ((tunnel->fd = open("/dev/net/tun", O_RDWR)) < 0) {
		perror("open_tun: /dev/net/tun error");
		return 1;
	}

	memset(&tunnel->ifr, 0x0, sizeof(tunnel->ifr));

	tunnel->ifr.ifr_flags = IFF_TAP | IFF_NO_PI;
	if (tunnel->name[0] != 0)
		strncpy(tunnel->ifr.ifr_name, tunnel->name, IFNAMSIZ);
	else
		strncpy(tunnel->ifr.ifr_name, "eoip%d", IFNAMSIZ);

	if (ioctl(tunnel->fd, TUNSETIFF, (void *)&tunnel->ifr) < 0) {
		perror("ioctl-1");
		close(fd);
		return 1;
	}

	tunnel->ifr.ifr_flags |= IFF_UP;
	tunnel->ifr.ifr_flags |= IFF_RUNNING;

	if (ioctl(fd, SIOCSIFFLAGS, (void *)&tunnel->ifr) < 0) {
		perror("ioctl-2");
		close(fd);
		return 1;
	}
	close(fd);
	return 0;
}

static void *thr_rx(void *threadid)
{
	struct sockaddr_in saddr[MAXRINGBUF];
	struct thr_rx *thr_rx_data = (struct thr_rx *)threadid;
	unsigned char *rxringbufptr[MAXRINGBUF];
	unsigned char *rxringbuffer;
	unsigned char *ptr;
	struct gre_hdr *ghdr;
	int i, ret, rxringbufused = 0, rxringbufconsumed, rxringpayload[MAXRINGBUF];
	int saddr_size = sizeof(saddr[0]);
	int raw_socket = thr_rx_data->raw_socket;
	uint16_t tnlid;
	Tunnel *tunnel;
	fd_set rfds;

#ifndef __UCLIBC__
	cpu_set_t cpuset;
	pthread_t thread = pthread_self();
	int cpu = 0;

	CPU_ZERO(&cpuset);
	CPU_SET(cpu, &cpuset);

	ret = pthread_setaffinity_np(thread, sizeof(cpu_set_t), &cpuset);
	if (ret)
		printf("Affinity error %d\n", ret);
	else
		printf("RX thread set to cpu %d\n", cpu);
#endif

	rxringbuffer = malloc(MAXPAYLOAD * MAXRINGBUF);
	if (!rxringbuffer) {
		perror("malloc()");
		exit(1);
	}
	/* Temporary code */
	for (i = 0; i < MAXRINGBUF; i++) {
		rxringbufptr[i] = rxringbuffer + (MAXPAYLOAD * i);
	}

	while (1) {
		FD_ZERO(&rfds);
		FD_SET(raw_socket, &rfds);
		ret = select(raw_socket + 1, &rfds, NULL, NULL, NULL);
		assert(rxringbufused == 0);
		while (rxringbufused < MAXRINGBUF) {
			rxringpayload[rxringbufused] =
			    recvfrom(raw_socket, rxringbufptr[rxringbufused],
				     MAXPAYLOAD, 0, &saddr[rxringbufused], &saddr_size);
			if (rxringpayload[rxringbufused] < 0)
				break;
			if (rxringpayload[rxringbufused] >= 28)
				rxringbufused++;
		}

		if (!rxringbufused)
			continue;

		rxringbufconsumed = 0;
		do {
			ptr = rxringbufptr[rxringbufconsumed];
			ghdr = (struct gre_hdr *)(ptr + 20);
			tnlid = __le16_to_cpu(ghdr->tunnel_id);
			ret = 0;
			/* TODO: Optimize search of tunnel id */
			for (i = 0; i < numtunnels; i++) {
				tunnel = tunnels + i;
				if (tnlid == tunnel->id) {
					/* This is a dynamic tunnel */
					if (tunnel->dynamic) {
						if (saddr[rxringbufconsumed].sin_addr.s_addr !=
						    tunnel->daddr.sin_addr.s_addr) {
							/* Updating tunnel */
							pthread_mutex_lock(&mutex1);
							tunnel->daddr.sin_addr.s_addr =
							    saddr[rxringbufconsumed].sin_addr.s_addr;
							pthread_mutex_unlock(&mutex1);
						}
					}
					/* skip keep-alive zero payload packets */
					if (__le16_to_cpu(ghdr->payload_size)) {
						ret =
						    write(tunnel->fd, ptr + 28, rxringpayload[rxringbufconsumed] - 28);
					} else {
						/* generate keepalive packet back */
						sendto(raw_socket, ghdr, 8, 0, (struct sockaddr *)&tunnel->daddr,
							(socklen_t) sizeof(tunnel->daddr));
					}
					break;
				}
			}
			rxringbufconsumed++;
		} while (rxringbufconsumed < rxringbufused);
		rxringbufused -= rxringbufconsumed;
		if (rxringbufused) {
			memmove(&rxringpayload[0], &rxringpayload[rxringbufconsumed], rxringbufused);
		}
	}
	return (NULL);
}

static void *thr_tx(void *threadid)
{
	struct thr_tx *thr_tx_data = (struct thr_tx *)threadid;
	struct sockaddr_in daddr;
	Tunnel *tunnel = thr_tx_data->tunnel;
	int fd = tunnel->fd;
	int raw_socket = thr_tx_data->raw_socket;
	int payloadsz, ret;
	unsigned char *ip = malloc(MAXPAYLOAD + 8);	/* 8-byte header of GRE, rest is payload */
	struct gre_hdr *ghdr = (struct gre_hdr *)ip;
	unsigned char *payloadptr = ip + 8;
	fd_set rfds;
#ifndef __UCLIBC__
	int cpu = thr_tx_data->cpu;
	cpu_set_t cpuset;
	pthread_t thread = pthread_self();

	CPU_ZERO(&cpuset);
	CPU_SET(cpu, &cpuset);

	ret = pthread_setaffinity_np(thread, sizeof(cpu_set_t), &cpuset);
	if (ret)
		printf("Affinity error %d\n", ret);
	else
		printf("TX thread(ID %d) set to cpu %d\n", tunnel->id, cpu);
#endif
	memset(ip, 0x0, 20);

	ghdr->header = __cpu_to_be32(0x20016400);
	while (1) {
		FD_ZERO(&rfds);
		FD_SET(fd, &rfds);
		ret = select(fd + 1, &rfds, NULL, NULL, NULL);

		payloadsz = read(fd, payloadptr, MAXPAYLOAD);
		if (payloadsz < 0)
			continue;
		ghdr->payload_size = __cpu_to_be16((uint16_t) payloadsz);
		ghdr->tunnel_id = __cpu_to_le16((uint16_t) tunnel->id);
		if (tunnel->dynamic)
			pthread_mutex_lock(&mutex1);
		if (sendto
		    (raw_socket, ip, payloadsz + 8, 0,
		     (struct sockaddr *)&tunnel->daddr, (socklen_t) sizeof(daddr)) < 0)
			perror("send() err");
		if (tunnel->dynamic)
			pthread_mutex_unlock(&mutex1);
	}
	return (NULL);
}

int main(int argc, char **argv)
{
	struct thr_rx thr_rx_data;
	struct thr_tx *thr_tx_data;
	int ret, i, sn, rc, optval = 262144;
	Tunnel *tunnel;
	struct sigaction sa;
	struct stat mystat;
	char section[IFNAMSIZ];
	char strbuf[256];
	char *configname;
	char defaultcfgname[] = "/etc/eoip.cfg";
	pthread_t *threads;
	pthread_attr_t attr;
	void *status;
	FILE *mfd;
	char *pidfile;

	thr_rx_data.raw_socket = socket(PF_INET, SOCK_RAW, 47);
	if (thr_rx_data.raw_socket == -1) {

		if (errno == EPERM) {
			printf("You need root privileges or CAP_NET_RAW capability to run this program\n");
		} else {
			perror("raw socket()");
		}
		return (1);
	}
	if (setsockopt(thr_rx_data.raw_socket, SOL_SOCKET, SO_RCVBUF, &optval, sizeof(optval)))
		perror("setsockopt(RCVBUF)");
	if (setsockopt(thr_rx_data.raw_socket, SOL_SOCKET, SO_SNDBUF, &optval, sizeof(optval)))
		perror("setsockopt(SNDBUF)");

	if (argc == 3) {
		struct sockaddr_in serv_addr;
		serv_addr.sin_family = AF_INET;
		if (!inet_pton(AF_INET, argv[2], (struct in_addr *)&serv_addr.sin_addr.s_addr)) {
			perror("bind address invalid");
			exit(-1);
		}
		serv_addr.sin_port = 0;
		if (bind(thr_rx_data.raw_socket, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
			perror("bind error");
			exit(-1);
		}
	}

	if (argc == 1)
		configname = defaultcfgname;
	else
		configname = argv[1];

	if (stat(configname, &mystat)) {
		printf("Mikrotik-compatible EoIP %s\n", PACKAGE_VERSION);
		printf("(c) Denys Fedoryshchenko <nuclearcat@nuclearcat.com>\n");
		printf("%s [configfile [bindip]]\n", argv[0]);
		exit(-1);
	}

	for (sn = 0; ini_getsection(sn, section, sizearray(section), configname) > 0; sn++) {
		numtunnels++;
	}

	tunnels = malloc(sizeof(Tunnel) * numtunnels);
	if (tunnels == NULL) {
		perror("malloc() failed");
		exit(-1);
	}
	memset(tunnels, 0x0, sizeof(Tunnel) * numtunnels);

	for (sn = 0; ini_getsection(sn, section, sizearray(section), configname) > 0; sn++) {
		tunnel = tunnels + sn;
		printf("Creating tunnel: %s num %d\n", section, sn);
		if (strlen(section) > 64) {
			printf("Name of tunnel need to be shorter than 64 symbols\n");
			exit(-1);
		}
		strncpy(tunnel->name, section, 64);
		tunnel->daddr.sin_family = AF_INET;
		tunnel->daddr.sin_port = 0;
		tunnel->dynamic = 0;
		if (ini_gets(section, "dst", "0.0.0.0", strbuf, sizeof(strbuf), configname) < 1) {
			printf("Destination for %s not correct\n", section);
		} else {
			printf("Destination for %s: %s\n", section, strbuf);
		}

		if (!inet_pton(AF_INET, strbuf, (struct in_addr *)&tunnel->daddr.sin_addr.s_addr)) {
			warn("Destination \"%s\" is not correct\n", strbuf);
			exit(-1);
		}
		memset(tunnel->daddr.sin_zero, 0x0, sizeof(tunnel->daddr.sin_zero));
		tunnel->id = (int)ini_getl(section, "id", 0, configname);
		/* TODO: What is max value of tunnel? */
		if (tunnel->id == 0 || tunnel->id > 65536) {
			warn("ID of \"%d\" is not correct\n", tunnel->id);
			exit(-1);
		}
		tunnel->dynamic = (int)ini_getl(section, "dynamic", 0, configname);
	}

	if (thr_rx_data.raw_socket == -1) {
		perror("raw socket error():");
		exit(-1);
	}
	fcntl(thr_rx_data.raw_socket, F_SETFL, O_NONBLOCK);

	for (i = 0; i < numtunnels; i++) {
		tunnel = tunnels + i;
		if (open_tun(tunnel)) {
			exit(-1);
		}
	}

	memset(&sa, 0x0, sizeof(sa));
	sa.sa_handler = term_handler;
	sigaction(SIGTERM, &sa, 0);
	sigaction(SIGINT, &sa, 0);
	threads = malloc(sizeof(pthread_t) * (numtunnels + 1));

	/* Fork after creating tunnels, useful for scripts */
	ret = daemon(1, 1);
	if (ret)
	    perror("daemon() fail:");

	if (asprintf(&pidfile, "/var/run/eoip-%s", basename(configname)) == -1)
		exit(1);

	mfd = fopen(pidfile, "w");
	fprintf(mfd, "%d", getpid());
	fclose(mfd);

	/* structure of Mikrotik EoIP:
	   ... IP header ...
	   4 byte - GRE info
	   2 byte - tunnel id
	 */

	pthread_attr_init(&attr);
	pthread_attr_setstacksize(&attr, LINUX_THREAD_STACK_SIZE);
	pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);
	rc = pthread_create(&threads[0], &attr, thr_rx, (void *)&thr_rx_data);
	if (rc)
	    perror("pthread_create");

	for (i = 0; i < numtunnels; i++) {
		tunnel = tunnels + i;
		fcntl(tunnel->fd, F_SETFL, O_NONBLOCK);
		/* Allocate for each thread */
		thr_tx_data = malloc(sizeof(struct thr_tx));
		thr_tx_data->tunnel = tunnel;
#ifndef __UCLIBC__
		thr_tx_data->cpu = i + 1;
#endif
		thr_tx_data->raw_socket = thr_rx_data.raw_socket;
		rc = pthread_create(&threads[0], &attr, thr_tx, (void *)thr_tx_data);
	}
	rc = pthread_join(threads[0], &status);
	return (0);
}


File: /eoip.cfg
[zeoip0]
id=123
dst=192.168.20.1
dynamic=1

[zeoip1]
id=124
dst=1.1.1.2

[zeoip2]
id=126
dst=1.1.1.8


File: /Makefile
CFLAGS	:=-O2 -Wall -DPACKAGE_VERSION=\"0.5-1\"
INISRC	:= minIni.c
LDFLAGS	:= -lpthread

all: eoip vip

eoip: eoip.c
	$(CC) $(CFLAGS) eoip.c $(INISRC) $(LDFLAGS) -o eoip

vip: vip.c
	$(CC) $(CFLAGS) vip.c $(INISRC) $(LDFLAGS) -o vip

clean:
	rm -f eoip vip


File: /minGlue.h
/*  Glue functions for the minIni library, based on the C/C++ stdio library
 *
 *  Or better said: this file contains macros that maps the function interface
 *  used by minIni to the standard C/C++ file I/O functions.
 *
 *  Copyright (c) ITB CompuPhase, 2008-2010
 *
 *  Licensed under the Apache License, Version 2.0 (the "License"); you may not
 *  use this file except in compliance with the License. You may obtain a copy
 *  of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 *  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 *  License for the specific language governing permissions and limitations
 *  under the License.
 *
 *  Version: $Id: minGlue.h 29 2010-07-06 13:38:05Z thiadmer.riemersma $
 */

/* map required file I/O to the standard C library */
#include <stdio.h>
#define ini_openread(filename,file)   ((*(file) = fopen((filename),"rt")) != NULL)
#define ini_openwrite(filename,file)  ((*(file) = fopen((filename),"wt")) != NULL)
#define ini_close(file)               fclose(*(file))
#define ini_read(buffer,size,file)    fgets((buffer),(size),*(file))
#define ini_write(buffer,file)        fputs((buffer),*(file))
#define ini_rename(source,dest)       rename((source),(dest))
#define ini_remove(filename)          remove(filename)
#define ini_rewind(file)              rewind(*(file))


File: /minIni.c
/*  minIni - Multi-Platform INI file parser, suitable for embedded systems
 *
 *  These routines are in part based on the article "Multiplatform .INI Files"
 *  by Joseph J. Graf in the March 1994 issue of Dr. Dobb's Journal.
 *
 *  Copyright (c) ITB CompuPhase, 2008-2010
 *
 *  Licensed under the Apache License, Version 2.0 (the "License"); you may not
 *  use this file except in compliance with the License. You may obtain a copy
 *  of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 *  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 *  License for the specific language governing permissions and limitations
 *  under the License.
 *
 *  Version: $Id: minIni.c 29 2010-07-06 13:38:05Z thiadmer.riemersma $
 */

#if (defined _UNICODE || defined __UNICODE__ || defined UNICODE) && !defined MININI_ANSI
#if !defined UNICODE		/* for Windows */
#define UNICODE
#endif
#if !defined _UNICODE		/* for C library */
#define _UNICODE
#endif
#endif

#define MININI_IMPLEMENTATION
#include "minIni.h"
#if defined NDEBUG
#define assert(e)
#else
#include <assert.h>
#endif

#if !defined __T
#include <string.h>
#include <stdlib.h>
  /* definition of TCHAR already in minIni.h */
#define __T(s)    s
#define _tcscat   strcat
#define _tcschr   strchr
#define _tcscmp   strcmp
#define _tcscpy   strcpy
#define _tcsicmp  stricmp
#define _tcslen   strlen
#define _tcsncpy  strncpy
#define _tcsnicmp strnicmp
#define _tcsrchr  strrchr
#define _tcstol   strtol
#define _tfgets   fgets
#define _tfputs   fputs
#define _tfopen   fopen
#define _tremove  remove
#define _trename  rename
#endif

#if defined __linux || defined __linux__
#define __LINUX__
#endif
#if defined FREEBSD && !defined __FreeBSD__
#define __FreeBSD__
#endif
#if !defined strnicmp
#if defined __LINUX__ || defined __FreeBSD__ || defined __OpenBSD__ || defined __APPLE__
#define strnicmp  strncasecmp
#endif
#endif

#if !defined INI_LINETERM
#define INI_LINETERM    __T("\n")
#endif
#if !defined INI_FILETYPE
#define INI_FILETYPE    FILE*
#endif

#if !defined sizearray
#define sizearray(a)    (sizeof(a) / sizeof((a)[0]))
#endif

enum quote_option {
	QUOTE_NONE,
	QUOTE_ENQUOTE,
	QUOTE_DEQUOTE,
};

static TCHAR *skipleading(const TCHAR * str)
{
	assert(str != NULL);
	while (*str != '\0' && *str <= ' ')
		str++;
	return (TCHAR *) str;
}

static TCHAR *skiptrailing(const TCHAR * str, const TCHAR * base)
{
	assert(str != NULL);
	assert(base != NULL);
	while (str > base && *(str - 1) <= ' ')
		str--;
	return (TCHAR *) str;
}

static TCHAR *striptrailing(TCHAR * str)
{
	TCHAR *ptr = skiptrailing(_tcschr(str, '\0'), str);
	assert(ptr != NULL);
	*ptr = '\0';
	return str;
}

static TCHAR *save_strncpy(TCHAR * dest, const TCHAR * source, size_t maxlen, enum quote_option option)
{
	size_t d, s;

	assert(maxlen > 0);
	if (option == QUOTE_ENQUOTE && maxlen < 3)
		option = QUOTE_NONE;	/* cannot store two quotes and a terminating zero in less than 3 characters */

	switch (option) {
	case QUOTE_NONE:
		_tcsncpy(dest, source, maxlen);
		dest[maxlen - 1] = '\0';
		break;
	case QUOTE_ENQUOTE:
		d = 0;
		dest[d++] = '"';
		for (s = 0; source[s] != '\0' && d < maxlen - 2; s++, d++) {
			if (source[s] == '"') {
				if (d >= maxlen - 3)
					break;	/* no space to store the escape character plus the one that follows it */
				dest[d++] = '\\';
			}	/* if */
			dest[d] = source[s];
		}		/* for */
		dest[d++] = '"';
		dest[d] = '\0';
		break;
	case QUOTE_DEQUOTE:
		for (d = s = 0; source[s] != '\0' && d < maxlen - 1; s++, d++) {
			if ((source[s] == '"' || source[s] == '\\')
			    && source[s + 1] == '"')
				s++;
			dest[d] = source[s];
		}		/* for */
		dest[d] = '\0';
		break;
	default:
		assert(0);
	}			/* switch */

	return dest;
}

static int getkeystring(INI_FILETYPE * fp, const TCHAR * Section,
			const TCHAR * Key, int idxSection, int idxKey, TCHAR * Buffer, int BufferSize)
{
	TCHAR *sp, *ep;
	int len, idx, isstring;
	TCHAR LocalBuffer[INI_BUFFERSIZE];

	assert(fp != NULL);
	/* Move through file 1 line at a time until a section is matched or EOF. If
	 * parameter Section is NULL, only look at keys above the first section. If
	 * idxSection is postive, copy the relevant section name.
	 */
	len = (Section != NULL) ? _tcslen(Section) : 0;
	if (len > 0 || idxSection >= 0) {
		idx = -1;
		do {
			if (!ini_read(LocalBuffer, INI_BUFFERSIZE, fp))
				return 0;
			sp = skipleading(LocalBuffer);
			ep = _tcschr(sp, ']');
		} while (*sp != '[' || ep == NULL
			 || (((int)(ep - sp - 1) != len || _tcsnicmp(sp + 1, Section, len) != 0)
			     && ++idx != idxSection));
		if (idxSection >= 0) {
			if (idx == idxSection) {
				assert(ep != NULL);
				assert(*ep == ']');
				*ep = '\0';
				save_strncpy(Buffer, sp + 1, BufferSize, QUOTE_NONE);
				return 1;
			}	/* if */
			return 0;	/* no more section found */
		}		/* if */
	}

	/* if */
	/* Now that the section has been found, find the entry.
	 * Stop searching upon leaving the section's area.
	 */
	assert(Key != NULL || idxKey >= 0);
	len = (Key != NULL) ? (int)_tcslen(Key) : 0;
	idx = -1;
	do {
		if (!ini_read(LocalBuffer, INI_BUFFERSIZE, fp)
		    || *(sp = skipleading(LocalBuffer)) == '[')
			return 0;
		sp = skipleading(LocalBuffer);
		ep = _tcschr(sp, '=');	/* Parse out the equal sign */
		if (ep == NULL)
			ep = _tcschr(sp, ':');
	} while (*sp == ';' || *sp == '#' || ep == NULL
		 || (((int)(skiptrailing(ep, sp) - sp) != len || _tcsnicmp(sp, Key, len) != 0) && ++idx != idxKey));
	if (idxKey >= 0) {
		if (idx == idxKey) {
			assert(ep != NULL);
			assert(*ep == '=' || *ep == ':');
			*ep = '\0';
			striptrailing(sp);
			save_strncpy(Buffer, sp, BufferSize, QUOTE_NONE);
			return 1;
		}		/* if */
		return 0;	/* no more key found (in this section) */
	}

	/* if */
	/* Copy up to BufferSize chars to buffer */
	assert(ep != NULL);
	assert(*ep == '=' || *ep == ':');
	sp = skipleading(ep + 1);
	/* Remove a trailing comment */
	isstring = 0;
	for (ep = sp; *ep != '\0' && ((*ep != ';' && *ep != '#') || isstring); ep++) {
		if (*ep == '"') {
			if (*(ep + 1) == '"')
				ep++;	/* skip "" (both quotes) */
			else
				isstring = !isstring;	/* single quote, toggle isstring */
		} else if (*ep == '\\' && *(ep + 1) == '"') {
			ep++;	/* skip \" (both quotes */
		}		/* if */
	}			/* for */
	assert(ep != NULL && (*ep == '\0' || *ep == ';' || *ep == '#'));
	*ep = '\0';		/* terminate at a comment */
	striptrailing(sp);
	/* Remove double quotes surrounding a value */
	isstring = QUOTE_NONE;
	if (*sp == '"' && (ep = _tcschr(sp, '\0')) != NULL && *(ep - 1) == '"') {
		sp++;
		*--ep = '\0';
		isstring = QUOTE_DEQUOTE;	/* this is a string, so remove escaped characters */
	}			/* if */
	save_strncpy(Buffer, sp, BufferSize, isstring);
	return 1;
}

/** ini_gets()
 * \param Section     the name of the section to search for
 * \param Key         the name of the entry to find the value of
 * \param DefValue    default string in the event of a failed read
 * \param Buffer      a pointer to the buffer to copy into
 * \param BufferSize  the maximum number of characters to copy
 * \param Filename    the name and full path of the .ini file to read from
 *
 * \return            the number of characters copied into the supplied buffer
 */
int ini_gets(const TCHAR * Section, const TCHAR * Key, const TCHAR * DefValue,
	     TCHAR * Buffer, int BufferSize, const TCHAR * Filename)
{
	INI_FILETYPE fp;
	int ok = 0;

	if (Buffer == NULL || BufferSize <= 0 || Key == NULL)
		return 0;
	if (ini_openread(Filename, &fp)) {
		ok = getkeystring(&fp, Section, Key, -1, -1, Buffer, BufferSize);
		ini_close(&fp);
	}			/* if */
	if (!ok)
		save_strncpy(Buffer, DefValue, BufferSize, QUOTE_NONE);
	return _tcslen(Buffer);
}

/** ini_getl()
 * \param Section     the name of the section to search for
 * \param Key         the name of the entry to find the value of
 * \param DefValue    the default value in the event of a failed read
 * \param Filename    the name of the .ini file to read from
 *
 * \return            the value located at Key
 */
long ini_getl(const TCHAR * Section, const TCHAR * Key, long DefValue, const TCHAR * Filename)
{
	TCHAR buff[64];
	int len = ini_gets(Section, Key, __T(""), buff, sizearray(buff), Filename);
	return (len == 0) ? DefValue : _tcstol(buff, NULL, 10);
}

/** ini_getsection()
 * \param idx         the zero-based sequence number of the section to return
 * \param Buffer      a pointer to the buffer to copy into
 * \param BufferSize  the maximum number of characters to copy
 * \param Filename    the name and full path of the .ini file to read from
 *
 * \return            the number of characters copied into the supplied buffer
 */
int ini_getsection(int idx, TCHAR * Buffer, int BufferSize, const TCHAR * Filename)
{
	INI_FILETYPE fp;
	int ok = 0;

	if (Buffer == NULL || BufferSize <= 0 || idx < 0)
		return 0;
	if (ini_openread(Filename, &fp)) {
		ok = getkeystring(&fp, NULL, NULL, idx, -1, Buffer, BufferSize);
		ini_close(&fp);
	}			/* if */
	if (!ok)
		*Buffer = '\0';
	return _tcslen(Buffer);
}

/** ini_getkey()
 * \param Section     the name of the section to browse through, or NULL to
 *                    browse through the keys outside any section
 * \param idx         the zero-based sequence number of the key to return
 * \param Buffer      a pointer to the buffer to copy into
 * \param BufferSize  the maximum number of characters to copy
 * \param Filename    the name and full path of the .ini file to read from
 *
 * \return            the number of characters copied into the supplied buffer
 */
int ini_getkey(const TCHAR * Section, int idx, TCHAR * Buffer, int BufferSize, const TCHAR * Filename)
{
	INI_FILETYPE fp;
	int ok = 0;

	if (Buffer == NULL || BufferSize <= 0 || idx < 0)
		return 0;
	if (ini_openread(Filename, &fp)) {
		ok = getkeystring(&fp, Section, NULL, -1, idx, Buffer, BufferSize);
		ini_close(&fp);
	}			/* if */
	if (!ok)
		*Buffer = '\0';
	return _tcslen(Buffer);
}

#if ! defined INI_READONLY
static void ini_tempname(TCHAR * dest, const TCHAR * source, int maxlength)
{
	TCHAR *p;

	save_strncpy(dest, source, maxlength, QUOTE_NONE);
	p = _tcsrchr(dest, '\0');
	assert(p != NULL);
	*(p - 1) = '~';
}

static enum quote_option check_enquote(const TCHAR * Value)
{
	const TCHAR *p;

	/* run through the value, if it has trailing spaces, or '"', ';' or '#'
	 * characters, enquote it
	 */
	assert(Value != NULL);
	for (p = Value; *p != '\0' && *p != '"' && *p != ';' && *p != '#'; p++)
		/* nothing */ ;
	return (*p != '\0' || (p > Value && *(p - 1) == ' ')) ? QUOTE_ENQUOTE : QUOTE_NONE;
}

static void writesection(TCHAR * LocalBuffer, const TCHAR * Section, INI_FILETYPE * fp)
{
	TCHAR *p;

	if (Section != NULL && _tcslen(Section) > 0) {
		LocalBuffer[0] = '[';
		save_strncpy(LocalBuffer + 1, Section, INI_BUFFERSIZE - 4, QUOTE_NONE);	/* -1 for '[', -1 for ']', -2 for '\r\n' */
		p = _tcsrchr(LocalBuffer, '\0');
		assert(p != NULL);
		*p++ = ']';
		_tcscpy(p, INI_LINETERM);	/* copy line terminator (typically "\n") */
		ini_write(LocalBuffer, fp);
	}			/* if */
}

static void writekey(TCHAR * LocalBuffer, const TCHAR * Key, const TCHAR * Value, INI_FILETYPE * fp)
{
	TCHAR *p;
	enum quote_option option = check_enquote(Value);
	save_strncpy(LocalBuffer, Key, INI_BUFFERSIZE - 3, QUOTE_NONE);	/* -1 for '=', -2 for '\r\n' */
	p = _tcsrchr(LocalBuffer, '\0');
	assert(p != NULL);
	*p++ = '=';
	save_strncpy(p, Value, INI_BUFFERSIZE - (p - LocalBuffer) - 2, option);	/* -2 for '\r\n' */
	p = _tcsrchr(LocalBuffer, '\0');
	assert(p != NULL);
	_tcscpy(p, INI_LINETERM);	/* copy line terminator (typically "\n") */
	ini_write(LocalBuffer, fp);
}

static void write_quoted(const TCHAR * Value, INI_FILETYPE * fp)
{
	TCHAR s[3];
	int idx;
	if (check_enquote(Value) == QUOTE_NONE) {
		ini_write(Value, fp);
	} else {
		ini_write("\"", fp);
		for (idx = 0; Value[idx] != '\0'; idx++) {
			if (Value[idx] == '"') {
				s[0] = '\\';
				s[1] = Value[idx];
				s[2] = '\0';
			} else {
				s[0] = Value[idx];
				s[1] = '\0';
			}	/* if */
			ini_write(s, fp);
		}		/* for */
		ini_write("\"", fp);
	}			/* if */
}

/** ini_puts()
 * \param Section     the name of the section to write the string in
 * \param Key         the name of the entry to write, or NULL to erase all keys in the section
 * \param Value       a pointer to the buffer the string, or NULL to erase the key
 * \param Filename    the name and full path of the .ini file to write to
 *
 * \return            1 if successful, otherwise 0
 */
int ini_puts(const TCHAR * Section, const TCHAR * Key, const TCHAR * Value, const TCHAR * Filename)
{
	INI_FILETYPE rfp;
	INI_FILETYPE wfp;
	TCHAR *sp, *ep;
	TCHAR LocalBuffer[INI_BUFFERSIZE];
	int len, match, count;

	assert(Filename != NULL);
	if (!ini_openread(Filename, &rfp)) {
		/* If the .ini file doesn't exist, make a new file */
		if (Key != NULL && Value != NULL) {
			if (!ini_openwrite(Filename, &wfp))
				return 0;
			writesection(LocalBuffer, Section, &wfp);
			writekey(LocalBuffer, Key, Value, &wfp);
			ini_close(&wfp);
		}		/* if */
		return 1;
	}

	/* if */
	/* If parameters Key and Value are valid (so this is not an "erase" request)
	 * and the setting already exists and it already has the correct value, do
	 * nothing. This early bail-out avoids rewriting the INI file for no reason.
	 */
	if (Key != NULL && Value != NULL) {
		match = getkeystring(&rfp, Section, Key, -1, -1, LocalBuffer, sizearray(LocalBuffer));
		if (match && _tcscmp(LocalBuffer, Value) == 0) {
			ini_close(&rfp);
			return 1;
		}
		/* if */
		/* key not found, or different value -> proceed (but rewind the input file first) */
		ini_rewind(&rfp);
	}

	/* if */
	/* Get a temporary file name to copy to. Use the existing name, but with
	 * the last character set to a '~'.
	 */
	ini_tempname(LocalBuffer, Filename, INI_BUFFERSIZE);
	if (!ini_openwrite(LocalBuffer, &wfp)) {
		ini_close(&rfp);
		return 0;
	}

	/* if */
	/* Move through the file one line at a time until a section is
	 * matched or until EOF. Copy to temp file as it is read.
	 */
	count = 0;
	len = (Section != NULL) ? _tcslen(Section) : 0;
	if (len > 0) {
		do {
			if (!ini_read(LocalBuffer, INI_BUFFERSIZE, &rfp)) {
				/* Failed to find section, so add one to the end */
				if (Key != NULL && Value != NULL) {
					ini_write(INI_LINETERM, &wfp);	/* force a new line (there may not have been one) behind the last line of the INI file */
					writesection(LocalBuffer, Section, &wfp);
					writekey(LocalBuffer, Key, Value, &wfp);
				}
				/* if */
				/* Clean up and rename */
				ini_close(&rfp);
				ini_close(&wfp);
				ini_remove(Filename);
				ini_tempname(LocalBuffer, Filename, INI_BUFFERSIZE);
				ini_rename(LocalBuffer, Filename);
				return 1;
			}
			/* if */
			/* Copy the line from source to dest, but not if this is the section that
			 * we are looking for and this section must be removed
			 */
			sp = skipleading(LocalBuffer);
			ep = _tcschr(sp, ']');
			match = (*sp == '[' && ep != NULL
				 && (int)(ep - sp - 1) == len && _tcsnicmp(sp + 1, Section, len) == 0);
			if (!match || Key != NULL) {
				/* Remove blank lines, but insert a blank line (possibly one that was
				 * removed on the previous iteration) before a new section. This creates
				 * "neat" INI files.
				 */
				if (_tcslen(sp) > 0) {
					if (*sp == '[' && count > 0)
						ini_write(INI_LINETERM, &wfp);
					ini_write(sp, &wfp);
					count++;
				}	/* if */
			}	/* if */
		} while (!match);
	}

	/* if */
	/* Now that the section has been found, find the entry. Stop searching
	 * upon leaving the section's area. Copy the file as it is read
	 * and create an entry if one is not found.
	 */
	len = (Key != NULL) ? _tcslen(Key) : 0;
	for (;;) {
		if (!ini_read(LocalBuffer, INI_BUFFERSIZE, &rfp)) {
			/* EOF without an entry so make one */
			if (Key != NULL && Value != NULL) {
				ini_write(INI_LINETERM, &wfp);	/* force a new line (there may not have been one) behind the last line of the INI file */
				writekey(LocalBuffer, Key, Value, &wfp);
			}
			/* if */
			/* Clean up and rename */
			ini_close(&rfp);
			ini_close(&wfp);
			ini_remove(Filename);
			ini_tempname(LocalBuffer, Filename, INI_BUFFERSIZE);
			ini_rename(LocalBuffer, Filename);
			return 1;
		}		/* if */
		sp = skipleading(LocalBuffer);
		ep = _tcschr(sp, '=');	/* Parse out the equal sign */
		if (ep == NULL)
			ep = _tcschr(sp, ':');
		match = (ep != NULL && (int)(skiptrailing(ep, sp) - sp) == len && _tcsnicmp(sp, Key, len) == 0);
		if ((Key != NULL && match) || *sp == '[')
			break;	/* found the key, or found a new section */
		/* in the section that we re-write, do not copy empty lines */
		if (Key != NULL && _tcslen(sp) > 0)
			ini_write(sp, &wfp);
	}			/* for */
	if (*sp == '[') {
		/* found start of new section, the key was not in the specified
		 * section, so we add it just before the new section
		 */
		if (Key != NULL && Value != NULL) {
			/* We cannot use "writekey()" here, because we need to preserve the
			 * contents of LocalBuffer.
			 */
			ini_write(Key, &wfp);
			ini_write("=", &wfp);
			write_quoted(Value, &wfp);
			ini_write(INI_LINETERM INI_LINETERM, &wfp);	/* put a blank line between the current and the next section */
		}
		/* if */
		/* write the new section header that we read previously */
		ini_write(sp, &wfp);
	} else {
		/* We found the key; ignore the line just read (with the key and
		 * the current value) and write the key with the new value.
		 */
		if (Key != NULL && Value != NULL)
			writekey(LocalBuffer, Key, Value, &wfp);
	}			/* if */
	/* Copy the rest of the INI file (removing empty lines, except before a section) */
	while (ini_read(LocalBuffer, INI_BUFFERSIZE, &rfp)) {
		sp = skipleading(LocalBuffer);
		if (_tcslen(sp) > 0) {
			if (*sp == '[')
				ini_write(INI_LINETERM, &wfp);
			ini_write(sp, &wfp);
		}		/* if */
	}			/* while */
	/* Clean up and rename */
	ini_close(&rfp);
	ini_close(&wfp);
	ini_remove(Filename);
	ini_tempname(LocalBuffer, Filename, INI_BUFFERSIZE);
	ini_rename(LocalBuffer, Filename);
	return 1;
}

/* Ansi C "itoa" based on Kernighan & Ritchie's "Ansi C" book. */
#define ABS(v)  ((v) < 0 ? -(v) : (v))

static void strreverse(TCHAR * str)
{
	TCHAR t;
	int i, j;

	for (i = 0, j = _tcslen(str) - 1; i < j; i++, j--) {
		t = str[i];
		str[i] = str[j];
		str[j] = t;
	}			/* for */
}

static void long2str(long value, TCHAR * str)
{
	int i = 0;
	long sign = value;
	int n;

	/* generate digits in reverse order */
	do {
		n = (int)(value % 10);	/* get next lowest digit */
		str[i++] = (TCHAR) (ABS(n) + '0');	/* handle case of negative digit */
	} while (value /= 10);	/* delete the lowest digit */
	if (sign < 0)
		str[i++] = '-';
	str[i] = '\0';

	strreverse(str);
}

/** ini_putl()
 * \param Section     the name of the section to write the value in
 * \param Key         the name of the entry to write, or NULL to erase all keys in the section
 * \param Value       the value to write
 * \param Filename    the name and full path of the .ini file to write to
 *
 * \return            1 if successful, otherwise 0
 */
int ini_putl(const TCHAR * Section, const TCHAR * Key, long Value, const TCHAR * Filename)
{
	TCHAR str[32];
	long2str(Value, str);
	return ini_puts(Section, Key, str, Filename);
}
#endif /* !INI_READONLY */

#if defined PORTABLE_STRNICMP
int strnicmp(const TCHAR * s1, const TCHAR * s2, size_t n)
{
	register unsigned TCHAR c1, c2;

	while (n-- != 0 && (*s1 || *s2)) {
		c1 = *(const unsigned TCHAR *)s1++;
		if ('a' <= c1 && c1 <= 'z')
			c1 += ('A' - 'a');
		c2 = *(const unsigned TCHAR *)s2++;
		if ('a' <= c2 && c2 <= 'z')
			c2 += ('A' - 'a');
		if (c1 != c2)
			return c1 - c2;
	}			/* while */
	return 0;
}
#endif /* PORTABLE_STRNICMP */


File: /minIni.h
/*  minIni - Multi-Platform INI file parser, suitable for embedded systems
 *
 *  Copyright (c) ITB CompuPhase, 2008-2010
 *
 *  Licensed under the Apache License, Version 2.0 (the "License"); you may not
 *  use this file except in compliance with the License. You may obtain a copy
 *  of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 *  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 *  License for the specific language governing permissions and limitations
 *  under the License.
 *
 *  Version: $Id: minIni.h 30 2010-07-06 15:49:17Z thiadmer.riemersma $
 */
#ifndef MININI_H
#define MININI_H

#include "minGlue.h"

#if (defined _UNICODE || defined __UNICODE__ || defined UNICODE) && !defined INI_ANSIONLY
#include <tchar.h>
#elif !defined __T
typedef char TCHAR;
#endif

#if !defined INI_BUFFERSIZE
#define INI_BUFFERSIZE  512
#endif

#if defined __cplusplus
extern "C" {
#endif

	long ini_getl(const TCHAR * Section, const TCHAR * Key, long DefValue, const TCHAR * Filename);
	int ini_gets(const TCHAR * Section, const TCHAR * Key, const TCHAR * DefValue, TCHAR * Buffer, int BufferSize,
		     const TCHAR * Filename);
	int ini_putl(const TCHAR * Section, const TCHAR * Key, long Value, const TCHAR * Filename);
	int ini_puts(const TCHAR * Section, const TCHAR * Key, const TCHAR * Value, const TCHAR * Filename);
	int ini_getsection(int idx, TCHAR * Buffer, int BufferSize, const TCHAR * Filename);
	int ini_getkey(const TCHAR * Section, int idx, TCHAR * Buffer, int BufferSize, const TCHAR * Filename);

#if defined __cplusplus
}
#endif
#if defined __cplusplus
#if defined __WXWINDOWS__
#include "wxMinIni.h"
#else
#include <string>
  /* The C++ class in minIni.h was contributed by Steven Van Ingelgem. */ class minIni
{
      public:
	minIni(const std::string & filename):iniFilename(filename) {
	} long getl(const std::string & Section, const std::string & Key, long DefValue = 0) const {
		return ini_getl(Section.c_str(), Key.c_str(), DefValue, iniFilename.c_str());
	} int geti(const std::string & Section, const std::string & Key, int DefValue = 0) const {
		return static_cast < int >(this->getl(Section, Key, long (DefValue)));
	} std::string gets(const std::string & Section, const std::string & Key, const std::string & DefValue = "") const {
		char buffer[INI_BUFFERSIZE];
		 ini_gets(Section.c_str(), Key.c_str(), DefValue.c_str(), buffer, INI_BUFFERSIZE, iniFilename.c_str());
		 return buffer;
	} std::string getsection(int idx)const {
		char buffer[INI_BUFFERSIZE];
		 ini_getsection(idx, buffer, INI_BUFFERSIZE, iniFilename.c_str());
		 return buffer;
	} std::string getkey(const std::string & Section, int idx)const {
		char buffer[INI_BUFFERSIZE];
		 ini_getkey(Section.c_str(), idx, buffer, INI_BUFFERSIZE, iniFilename.c_str());
		 return buffer;
	}
#if ! defined INI_READONLY
	bool put(const std::string & Section, const std::string & Key, long Value)const {
		return (bool) ini_putl(Section.c_str(), Key.c_str(), Value, iniFilename.c_str());
	} bool put(const std::string & Section, const std::string & Key, int Value)const {
		return (bool) ini_putl(Section.c_str(), Key.c_str(), (long)Value, iniFilename.c_str());
	} bool put(const std::string & Section, const std::string & Key, const std::string & Value) const {
		return (bool) ini_puts(Section.c_str(), Key.c_str(), Value.c_str(), iniFilename.c_str());
	} bool del(const std::string & Section, const std::string & Key)const {
		return (bool) ini_puts(Section.c_str(), Key.c_str(), 0, iniFilename.c_str());
	} bool del(const std::string & Section)const {
		return (bool) ini_puts(Section.c_str(), 0, 0, iniFilename.c_str());
	}
#endif
      private:
	 std::string iniFilename;
};

#endif /* __WXWINDOWS__ */
#endif /* __cplusplus */

#endif /* MININI_H */


File: /vip.c
/*
    file:   vip.c
    Authors:
    Linux initial code: Denys Fedoryshchenko aka NuclearCat <nuclearcat (at) nuclearcat.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.*
*/
#ifndef __UCLIBC__
#define _GNU_SOURCE
#endif
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netinet/if_ether.h>
#include <net/ethernet.h>
#include <netinet/ether.h>
#include <linux/if_tun.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <net/if.h>
#include <poll.h>
#include <unistd.h>
#include <err.h>
#include <signal.h>
#include <assert.h>
#include <pthread.h>
#include "minIni.h"
#include <getopt.h>

#ifdef HAVE_LIBLZO2
#include <lzo/lzo1x.h>
#endif

//#ifdef GCRYPT
//#include <gcrypt.h>
//#define  ADDON 2
//#else
#define  ADDON 0
//#endif

/* In theory maximum payload that can be handled is 65536, but if we use vectorized
   code with preallocated buffers - it is waste of space, especially for embedded setup.
   So if you want oversized packets - increase MAXPAYLOAD up to 65536 (or a bit less)
   If you choice performance - more vectors, to avoid expensive context switches
*/

#define MAXPAYLOAD (4096)
//#define MAXPACKED (1500-200)
//#define MAXPACKED (1700)
//#define PREALLOCBUF 32
#define MAXRINGBUF  64

#define BIT_COMPRESSED 		(1 << 0)
#define BIT_PACKED 		(1 << 1)
#define BIT_SERVICE 		(1 << 2)

#define sizearray(a)  (sizeof(a) / sizeof((a)[0]))

#ifndef __cacheline_aligned
#define __cacheline_aligned \
__attribute__((__aligned__(SMP_CACHE_BYTES), \
__section__(".data.cacheline_aligned")))
#endif /* __cacheline_aligned */
#define __read_mostly __attribute__((__section__(".data.read_mostly")))

pthread_mutex_t raw_mutex = PTHREAD_MUTEX_INITIALIZER;

typedef struct {
	struct sockaddr_in daddr;
	int id;
	int fd;
	struct ifreq ifr;
	char name[65];
	struct thr_tx *thr_tx_data;
} Tunnel;

struct thr_rx {
	int raw_socket;
};

struct thr_tx {
	int raw_socket;
	Tunnel *tunnel;
	int cpu;
	unsigned int packdelay;
	int maxpacked;
	int compression;
};

/*
struct snd_buf
{
    unsigned char		data[MAXPAYLOAD];
    unsigned int 		size;
    unsigned int		crc;
};
*/

static int numtunnels;
static Tunnel *tunnels;

/*
void error( const char* format, ...) {
    va_list args;
    va_start( args, format );
    vfprintf( stderr, format, args );
    va_end( args );
    fprintf( stderr, "\n" );
}
*/

static int open_tun(Tunnel * tunnel)
{
	int fd;

	if ((fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
		perror("socket() failed");
		return 1;
	}
	if ((tunnel->fd = open("/dev/net/tun", O_RDWR)) < 0) {
		perror("open_tun: /dev/net/tun error");
		return 1;
	}

	memset(&tunnel->ifr, 0x0, sizeof(tunnel->ifr));

	tunnel->ifr.ifr_flags = IFF_TUN | IFF_NO_PI;
	if (tunnel->name[0] != 0)
		strncpy(tunnel->ifr.ifr_name, tunnel->name, IFNAMSIZ);
	else
		strncpy(tunnel->ifr.ifr_name, "vip%d", IFNAMSIZ);

	if (ioctl(tunnel->fd, TUNSETIFF, (void *)&tunnel->ifr) < 0) {
		perror("ioctl-1");
		close(fd);
		return 1;
	}

	tunnel->ifr.ifr_flags |= IFF_UP;
	tunnel->ifr.ifr_flags |= IFF_RUNNING;

	if (ioctl(fd, SIOCSIFFLAGS, (void *)&tunnel->ifr) < 0) {
		perror("ioctl-2");
		close(fd);
		return 1;
	}
	close(fd);
	return 0;
}

static void *thr_rx(void *threadid)
{
	static unsigned char *rxringbufptr[MAXRINGBUF];
	static int rxringpayload[MAXRINGBUF];
	static unsigned char *rxringbuffer;
	static int rxringbufused = 0, rxringconsumed;
	static unsigned char *ptr;
	static int i, ret;
	struct thr_rx *thr_rx_data = (struct thr_rx *)threadid;
	static Tunnel *tunnel;
	int raw_socket = thr_rx_data->raw_socket;
	static unsigned char *decompressed = NULL;
	static unsigned int decompressedsz;
	static fd_set rfds;

	/* 2-byte header of VIP, rest is payload */
	if (posix_memalign((void *)&decompressed, 64, MAXPAYLOAD)) {
		printf("memalign failed\n");
		pthread_exit(0);
	}
#ifndef __UCLIBC__
	cpu_set_t cpuset;
	int cpu = 0;
	pthread_t thread = pthread_self();

	CPU_ZERO(&cpuset);
	CPU_SET(cpu, &cpuset);

	ret = pthread_setaffinity_np(thread, sizeof(cpu_set_t), &cpuset);
	if (ret)
		printf("Affinity error %d\n", ret);
	else
		printf("RX thread cpu %d\n", cpu);
#endif
#ifdef HAVE_LIBLZO2
	ret = lzo_init();
	if (ret != LZO_E_OK) {
		printf("LZO init failed\n");
		exit(1);
	}
//    if (posix_memalign((void **)&wrkmem, 64, LZO1X_1_MEM_COMPRESS))
//      exit(1);

#endif

	rxringbuffer = malloc(MAXPAYLOAD * MAXRINGBUF);

/*    if (posix_memalign((void **)&rxringbuffer, 64, MAXPAYLOAD*MAXRINGBUF))
	exit(1);
*/

	if (!rxringbuffer) {
		perror("malloc()");
		exit(1);
	}
	/* Temporary code */
	for (i = 0; i < MAXRINGBUF; i++) {
		rxringbufptr[i] = rxringbuffer + (MAXPAYLOAD * i);
	}

	while (1) {

		FD_ZERO(&rfds);
		FD_SET(raw_socket, &rfds);
		ret = select(raw_socket + 1, &rfds, NULL, NULL, NULL);

		while (rxringbufused < MAXRINGBUF) {
			pthread_mutex_lock(&raw_mutex);
			rxringpayload[rxringbufused] = read(raw_socket, rxringbufptr[rxringbufused], MAXPAYLOAD);
			pthread_mutex_unlock(&raw_mutex);

			if (rxringpayload[rxringbufused] < 0)
				break;

			if (rxringpayload[rxringbufused] >= 2)
				rxringbufused++;
		}

		if (!rxringbufused)
			continue;

		rxringconsumed = 0;
		do {
			ptr = rxringbufptr[rxringconsumed];
			ret = 0;
			/* TODO: Optimize search of tunnel id */
			for (i = 0; i < numtunnels; i++) {

				tunnel = tunnels + i;
				if (ptr[20] == (unsigned char)(tunnel->id)) {

#ifdef HAVE_LIBLZO2
					if (ptr[21] & BIT_COMPRESSED) {
//						decompressedsz = MAXPAYLOAD-22-3; /* Lzo note about 3 bytes in asm algos */
						decompressedsz = MAXPAYLOAD;
						if (lzo1x_decompress_safe
						    (ptr + 22,
						     rxringpayload
						     [rxringconsumed] - 22,
						     decompressed, (lzo_uintp) & decompressedsz, NULL) == LZO_E_OK) {
							if (decompressed == NULL) {
								printf("Please report to developer about this bug\n");
								//pthread_exit(1);
							}
							memcpy(ptr + 22, decompressed, decompressedsz);
							rxringpayload[rxringconsumed] = decompressedsz + 22;
						} else {
							perror("lzo feeling bad about your packet\n");
							break;
							//exit(1);
						}
					}
#else

					if (ptr[21] & BIT_COMPRESSED) {
						printf("Can't decompress. TODO\n");
						exit(0);
					}
#endif

					if ((ptr[21] & BIT_PACKED)) {
						unsigned int offset = 22;	/* 20 IP header + 2 byte of tunnel id and bitfield */
						unsigned short total;

//						ctr_packed++;
						while (1) {
							total = ntohs(*(uint16_t *) (ptr + offset + 2));	/* 2 byte - IP offset to total len */

							if ((int)
							    (offset + total) > rxringpayload[rxringconsumed]) {
								printf
								    ("invalid offset! %d > %d IP size %d\n",
								     (offset +
								      total), rxringpayload[rxringconsumed], total);
								break;
							}
							pthread_mutex_lock(&raw_mutex);
							ret = write(tunnel->fd, ptr + offset, total);
							pthread_mutex_unlock(&raw_mutex);
							if (ret < 0) {
								perror("tunnel write error #1\n");
								printf("error details: %d,%d\n", offset, total);
								break;
							}

							offset += total;

							/* This is correct, finished processing packed data */
							if ((int)offset == rxringpayload[rxringconsumed])
								break;
							if ((int)offset > rxringpayload[rxringconsumed]) {
								printf
								    ("invalid offset! %d+%d > %d\n",
								     offset, total, rxringpayload[rxringconsumed]);
								break;
							}

						}
					} else {
						pthread_mutex_lock(&raw_mutex);
						ret = write(tunnel->fd, ptr + 22, rxringpayload[rxringconsumed] - 22);
						pthread_mutex_unlock(&raw_mutex);

						if (ret < 0)
							printf("tunnel write error #2\n");
					}
					break;
				}
			}

			rxringconsumed++;
		} while (rxringconsumed < rxringbufused);
		rxringbufused -= rxringconsumed;
		if (rxringbufused) {
			memmove(&rxringpayload[0], &rxringpayload[rxringconsumed], rxringbufused);
		}

	}
	return (NULL);
}

static void preserve_data(unsigned char *data, int size)
{

}

/* Reading from tun interface, processing and pushing to raw socket */
static void *thr_tx(void *threadid)
{
	struct thr_tx *thr_tx_data = (struct thr_tx *)threadid;
	Tunnel *tunnel = thr_tx_data->tunnel;
	int fd = tunnel->fd;
	int raw_socket = thr_tx_data->raw_socket;
	unsigned char *ip = malloc(MAXPAYLOAD + 2);	/* 2-byte header of VIP, rest is payload */
	unsigned char *payloadptr = ip + 2;

	unsigned char *prevptr = malloc(MAXPAYLOAD);	/* 2-byte header of VIP, rest is payload */
	int prevavail = 0;

	unsigned char *compressed = malloc(MAXPAYLOAD * 2);	/* 2-byte header of VIP, rest is payload */
#ifdef HAVE_LIBLZO2
	lzo_voidp wrkmem;
#endif
	int payloadsz;
	int compressedsz;
	struct sockaddr_in daddr;
	int ret;

//    unsigned int ctr_uncompressed = 0, ctr_compressed = 0, ctr_packed = 0, ctr_normal = 0;
	fd_set rfds;
	struct timeval timeout;
	unsigned int packdelay = thr_tx_data->packdelay;
	int maxpacked = thr_tx_data->maxpacked;
	int compression = thr_tx_data->compression;
	int multiplier = 1;
#ifndef __UCLIBC__
	int cpu = thr_tx_data->cpu;
	cpu_set_t cpuset;
	pthread_t thread = pthread_self();
//#ifdef GCRYPT
//    /* CTRL_PKT, 2 byte VIP hdr, 2 byte extra, 1476 - 369 checksums */
//    uint32_t cksumbuf[369];
//#endif

	CPU_ZERO(&cpuset);
	CPU_SET(cpu, &cpuset);
	ret = pthread_setaffinity_np(thread, sizeof(cpu_set_t), &cpuset);
	if (ret)
		printf("Affinity error %d\n", ret);
	else
		printf("TX thread(ID %d) set to cpu %d packdelay %d\n", tunnel->id, cpu, packdelay);

#endif

#ifdef HAVE_LIBLZO2
	ret = lzo_init();
	if (ret != LZO_E_OK) {
		printf("LZO init failed\n");
		exit(1);
	}
	wrkmem = (lzo_voidp) malloc(LZO1X_1_MEM_COMPRESS);
#endif

	memset(ip, 0x0, 20);

	while (1) {
		FD_ZERO(&rfds);
		FD_SET(fd, &rfds);
		ret = select(fd + 1, &rfds, NULL, NULL, NULL);

		// tunnel id
		ip[0] = (unsigned char)(tunnel->id & 0xFF);
		ip[1] = 0;

		if (!prevavail) {
			pthread_mutex_lock(&raw_mutex);
			payloadsz = read(fd, payloadptr, MAXPAYLOAD);
			pthread_mutex_unlock(&raw_mutex);

			if (payloadsz < 0)
				continue;

			unsigned short total = ntohs(*(uint16_t *) (payloadptr + 2));
			if (total != payloadsz)
				printf("t %d p %d\n", total, payloadsz);

		} else {
			payloadsz = prevavail;
			memcpy(payloadptr, prevptr, prevavail);
			prevavail = 0;
		}

		/* If we are fragmented anyway, try to increase second packet size
		   so average packet size will be higher
		 */
		if (payloadsz > maxpacked)
			multiplier = 2;
		else
			multiplier = 1;

		timeout.tv_sec = 0;
		timeout.tv_usec = packdelay;	/* ms*1000, 0.05ms */

		while (payloadsz < (maxpacked * multiplier)) {
			/* try to get next packet */
			FD_ZERO(&rfds);
			FD_SET(fd, &rfds);
			ret = select(fd + 1, &rfds, NULL, NULL, &timeout);
			if (ret <= 0) {
				break;
			}

			prevavail = read(fd, prevptr, MAXPAYLOAD);
			/* TODO: unlikely */
			if (prevavail < 0) {
				perror("Invalid situation\n");
				prevavail = 0;
				continue;
				//break;
			}

			if (prevavail + payloadsz <= (maxpacked * multiplier)) {
				/* Still small, merge packets */
				ip[1] |= BIT_PACKED;
				memcpy(payloadptr + payloadsz, prevptr, prevavail);
				payloadsz += prevavail;
				prevavail = 0;
			} else {
				/* This packet too big, send it alone */
				break;
			}
		}

#ifdef HAVE_LIBLZO2
		if (compression) {
			compressedsz = MAXPAYLOAD * 2;
			ret = lzo1x_1_compress(payloadptr, payloadsz, compressed, (lzo_uintp) & compressedsz, wrkmem);

			/* Adaptive compression */
			if (compressedsz >= payloadsz || compressedsz > MAXPAYLOAD) {
				compressedsz = 0;
			} else {
				ip[1] |= BIT_COMPRESSED;
				memcpy(payloadptr, compressed, compressedsz);
				payloadsz = compressedsz;
			}
		}
#else
		compressedsz = 0;
#endif

//#ifdef GCRYPT
//		gcry_md_hash_buffer(GCRY_MD_CRC32,cksumbuf,ip,payloadsz+2);
//#endif

		pthread_mutex_lock(&raw_mutex);
		if (sendto
		    (raw_socket, ip, payloadsz + 2, 0,
		     (struct sockaddr *)&tunnel->daddr, (socklen_t) sizeof(daddr)) < 0)
			perror("send() err");
		pthread_mutex_unlock(&raw_mutex);

	}
	return (NULL);
}

int main(int argc, char **argv)
{
	struct thr_rx thr_rx_data;
	int ret, i, sn, rc, protocol = 50, c, len;
	Tunnel *tunnel;
	struct sigaction sa;
	struct stat mystat;
	char section[IFNAMSIZ];
	char strbuf[256];
	char *configname = NULL;
	char *bindaddr = NULL;
	char defaultcfgname[] = "/etc/vip.cfg";
	pthread_t *threads;
	pthread_attr_t attr;
	void *status;
	int optval = 262144;

	while (1) {

		static struct option long_options[] = {
			{"protocol", required_argument, 0, 'p'},
			{"config", required_argument, 0, 'c'},
			{"bind", required_argument, 0, 'b'},
			{"help", no_argument, 0, 'h'},
			{0, 0, 0, 0}
		};
		/* getopt_long stores the option index here. */
		int option_index = 0;

		c = getopt_long(argc, argv, "c:p:b:h", long_options, &option_index);
		/* Detect the end of the options. */
		if (c == -1)
			break;

		switch (c) {
		case 'p':
			protocol = atoi(optarg);
			break;

		case 'b':
			len = strlen(optarg) + 1;
			bindaddr = malloc(len);
			strncpy(bindaddr, optarg, len);
			break;

		case 'c':
			len = strlen(optarg) + 1;
			configname = malloc(len);
			strncpy(configname, optarg, len);
			break;

		case 'h':
			printf("Available options:\n");
			printf("--protocol 		- Protocol \n");
			printf("--config 		- Config path\n");
			printf("--bind 			- Bind address\n");
			printf("--help			- Help\n");
//			printf("--triggeroutage         - Detect outage, missed packets/packets ok (0/0)\n");
			/* getopt_long already printed an error message. */
			exit(1);
			break;

		default:
			abort();
		}
	}

//#ifdef HAVE_LIBLZO2
//    ret = lzo_init();
//#endif

	printf("Virtual IP %s\n", PACKAGE_VERSION);
	printf("(c) Denys Fedoryshchenko <nuclearcat@nuclearcat.com>\n");

	thr_rx_data.raw_socket = socket(PF_INET, SOCK_RAW, protocol);
	if (setsockopt(thr_rx_data.raw_socket, SOL_SOCKET, SO_RCVBUF, &optval, sizeof(optval)))
		perror("setsockopt(RCVBUF)");
	if (setsockopt(thr_rx_data.raw_socket, SOL_SOCKET, SO_SNDBUF, &optval, sizeof(optval)))
		perror("setsockopt(SNDBUF)");

	if (bindaddr != NULL) {
		struct sockaddr_in serv_addr;
		serv_addr.sin_family = AF_INET;
		if (!inet_pton(AF_INET, bindaddr, (struct in_addr *)&serv_addr.sin_addr.s_addr)) {
			perror("bind address invalid");
			exit(-1);
		}
		serv_addr.sin_port = 0;
		if (bind(thr_rx_data.raw_socket, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
			perror("bind error");
			exit(-1);
		}
	}

	if (configname == NULL)
		configname = defaultcfgname;

	if (stat(configname, &mystat)) {
		perror("config file error");
		printf("Filename: %s\n", configname);

		/* TODO: Check readability */
		exit(-1);
	}

	for (sn = 0; ini_getsection(sn, section, sizearray(section), configname) > 0; sn++) {
		numtunnels++;
	}

	tunnels = malloc(sizeof(Tunnel) * numtunnels);
	memset(tunnels, 0x0, sizeof(Tunnel) * numtunnels);

	for (sn = 0; ini_getsection(sn, section, sizearray(section), configname) > 0; sn++) {
		tunnel = tunnels + sn;
		printf("Creating tunnel: %s num %d\n", section, sn);

		if (strlen(section) > 64) {
			printf("Name of tunnel need to be shorter than 64 symbols\n");
			exit(-1);
		}
		strncpy(tunnel->name, section, 64);

		tunnel->daddr.sin_family = AF_INET;
		tunnel->daddr.sin_port = 0;
		if (ini_gets(section, "dst", "0.0.0.0", strbuf, sizeof(strbuf), configname) < 1) {
			printf("Destination for %s not correct\n", section);
		} else {
			printf("Destination for %s: %s\n", section, strbuf);
		}

		if (!inet_pton(AF_INET, strbuf, (struct in_addr *)&tunnel->daddr.sin_addr.s_addr)) {
			warn("Destination \"%s\" is not correct\n", strbuf);
			exit(-1);
		}
		memset(tunnel->daddr.sin_zero, 0x0, sizeof(tunnel->daddr.sin_zero));
		tunnel->id = (int)ini_getl(section, "id", 0, configname);
		/* TODO: What is max value of tunnel? */
		if (tunnel->id == 0 || tunnel->id > 255) {
			warn("ID of \"%d\" is not correct\n", tunnel->id);
			exit(-1);
		}
		/* Allocate for each thread */
		tunnel->thr_tx_data = malloc(sizeof(struct thr_tx));
		tunnel->thr_tx_data->tunnel = tunnel;
		tunnel->thr_tx_data->cpu = sn + 1;
		tunnel->thr_tx_data->packdelay = (int)ini_getl(section, "delay", 1000, configname);
		tunnel->thr_tx_data->maxpacked = (int)ini_getl(section, "maxpacked", 1500, configname);
		tunnel->thr_tx_data->compression = (int)ini_getl(section, "compression", 1, configname);
		tunnel->thr_tx_data->raw_socket = thr_rx_data.raw_socket;
		if (tunnel->thr_tx_data->maxpacked > 1500)
			tunnel->thr_tx_data->maxpacked = 1500;
		printf("Name %s ID %d Delay %d maxpacked %d compression %d\n",
		       tunnel->name, tunnel->id, tunnel->thr_tx_data->packdelay,
		       tunnel->thr_tx_data->maxpacked, tunnel->thr_tx_data->compression);
		//printf("Max packed %d\n",tunnel->thr_tx_data->maxpacked);
	}

	if (thr_rx_data.raw_socket == -1) {
		perror("raw socket error():");
		exit(-1);
	}
	fcntl(thr_rx_data.raw_socket, F_SETFL, O_NONBLOCK);

	for (i = 0; i < numtunnels; i++) {
		tunnel = tunnels + i;

		if (open_tun(tunnel)) {
			exit(-1);
		}
	}

//	memset(&sa, 0x0,sizeof(sa));
//	sa.sa_handler = term_handler;
//	sigaction( SIGTERM , &sa, 0);
//	sigaction( SIGINT , &sa, 0);

	threads = malloc(sizeof(pthread_t) * (numtunnels + 1));

	/* Fork after creating tunnels, useful for scripts */
	ret = daemon(1, 1);

	pthread_attr_init(&attr);
	pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);

	rc = pthread_create(&threads[0], &attr, thr_rx, (void *)&thr_rx_data);

	for (i = 0; i < numtunnels; i++) {
		tunnel = tunnels + i;
		fcntl(tunnel->fd, F_SETFL, O_NONBLOCK);
		rc = pthread_create(&threads[i + 1], &attr, thr_tx, (void *)tunnel->thr_tx_data);
	}

	rc = pthread_join(threads[0], &status);

	return (0);
}


File: /vip.cfg
[vip0]
id=1
dst=
delay=10000
maxpacked=1400



