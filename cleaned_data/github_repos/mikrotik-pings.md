# Repository Information
Name: mikrotik-pings

# Directory Structure
Directory structure:
└── github_repos/mikrotik-pings/
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
    │   │       ├── pack-b2244dd047d811ec0be6e1c89cc3cf96c45cf99f.idx
    │   │       └── pack-b2244dd047d811ec0be6e1c89cc3cf96c45cf99f.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── arping.c
    ├── clockdiff.c
    ├── colors.h
    ├── in6_flowlabel.h
    ├── INSTALL
    ├── ipg
    ├── iputils.spec
    ├── Makefile
    ├── ninfod/
    │   ├── config.h.in
    │   ├── configure
    │   ├── configure.in
    │   ├── COPYING
    │   ├── icmp6_nodeinfo.h
    │   ├── install-sh
    │   ├── Makefile.in
    │   ├── ninfod.c
    │   ├── ninfod.h
    │   ├── ninfod.sh.in
    │   ├── ninfod_addrs.c
    │   ├── ninfod_core.c
    │   ├── ninfod_name.c
    │   ├── ni_ifaddrs.c
    │   └── ni_ifaddrs.h
    ├── ping.c
    ├── ping6.c
    ├── ping6_niquery.h
    ├── ping_common.c
    ├── ping_common.h
    ├── rarpd.c
    ├── rdisc.c
    ├── README.md
    ├── RELNOTES
    ├── SNAPSHOT.h
    ├── tftp.h
    ├── tftpd.c
    ├── tftpsubs.c
    ├── tracepath.c
    ├── tracepath6.c
    └── traceroute6.c


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
	url = https://github.com/patrickbrandao/mikrotik-pings.git
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
0000000000000000000000000000000000000000 4cee50d9112836dca252d445a40fbc66cade13c2 vivek-dodia <vivek.dodia@icloud.com> 1738606338 -0500	clone: from https://github.com/patrickbrandao/mikrotik-pings.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 4cee50d9112836dca252d445a40fbc66cade13c2 vivek-dodia <vivek.dodia@icloud.com> 1738606338 -0500	clone: from https://github.com/patrickbrandao/mikrotik-pings.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 4cee50d9112836dca252d445a40fbc66cade13c2 vivek-dodia <vivek.dodia@icloud.com> 1738606338 -0500	clone: from https://github.com/patrickbrandao/mikrotik-pings.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
4cee50d9112836dca252d445a40fbc66cade13c2 refs/remotes/origin/master


File: /.git\refs\heads\master
4cee50d9112836dca252d445a40fbc66cade13c2


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /arping.c
/*
 * arping.c
 *
 *		This program is free software; you can redistribute it and/or
 *		modify it under the terms of the GNU General Public License
 *		as published by the Free Software Foundation; either version
 *		2 of the License, or (at your option) any later version.
 *
 * Authors:	Alexey Kuznetsov, <kuznet@ms2.inr.ac.ru>
 * 		YOSHIFUJI Hideaki <yoshfuji@linux-ipv6.org>
 */

#include <stdlib.h>
#include <sys/param.h>
#include <sys/socket.h>
#include <linux/sockios.h>
#include <sys/file.h>
#include <sys/time.h>
#include <sys/signal.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <linux/if_packet.h>
#include <linux/if_ether.h>
#include <net/if_arp.h>
#include <sys/uio.h>
#ifdef CAPABILITIES
#include <sys/prctl.h>
#include <sys/capability.h>
#endif

#include <termios.h>
#include <netdb.h>
#include <unistd.h>
#include <stdio.h>
#include <ctype.h>
#include <errno.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#ifdef USE_SYSFS
#include <sysfs/libsysfs.h>
struct sysfs_devattr_values;
#endif

#ifndef WITHOUT_IFADDRS
#include <ifaddrs.h>
#endif

#ifdef USE_IDN
#include <idna.h>
#include <locale.h>
#endif

#include "colors.h"
#include "SNAPSHOT.h"

static void usage(void) __attribute__((noreturn));

#ifdef DEFAULT_DEVICE
# define DEFAULT_DEVICE_STR	DEFAULT_DEVICE
#else
# define DEFAULT_DEVICE		NULL
#endif

struct device {
	char *name;
	int ifindex;
#ifndef WITHOUT_IFADDRS
	struct ifaddrs *ifa;
#endif
#ifdef USE_SYSFS
	struct sysfs_devattr_values *sysfs;
#endif
};

int quit_on_reply=0;
struct device device = {
	.name = DEFAULT_DEVICE,
};
char *source;
struct in_addr src, dst;
char *target;
int dad, unsolicited, advert;
int quiet;
int count=-1;
int timeout;
int unicasting;
int s;
int broadcast_only;

struct sockaddr_storage me;
struct sockaddr_storage he;

struct timeval start, last;

int sent, brd_sent;
int received, brd_recv, req_recv;

/* timing */
int timing;					/* flag to do timing */
long tmin = -1;				/* minimum round trip time */
long tmax = -1;				/* maximum round trip time */
long long tsum = 0;			/* sum of all times, for doing average */
long long tsum2 = 0;


#ifndef CAPABILITIES
static uid_t euid;
#endif

#define MS_TDIFF(tv1,tv2) ( ((tv1).tv_sec-(tv2).tv_sec)*1000 + \
			   ((tv1).tv_usec-(tv2).tv_usec)/1000 )

#define OFFSET_OF(name,ele)	((size_t)(((name *)0)->ele))

static inline socklen_t sll_len(size_t halen)
{
	socklen_t len = OFFSET_OF(struct sockaddr_ll, sll_addr) + halen;
	if (len < sizeof(struct sockaddr_ll))
		len = sizeof(struct sockaddr_ll);
	return len;
}

#define SLL_LEN(hln)		sll_len(hln)


// cabecalho
void print_header(void);

void usage(void)
{
	fprintf(stderr,
		"Usage: arping [-fqbDUAV] [-c count] [-w timeout] [-I device] [-s source] destination\n"
		"  -f : quit on first reply\n"
		"  -q : be quiet\n"
		"  -b : keep broadcasting, don't go unicast\n"
		"  -D : duplicate address detection mode\n"
		"  -U : Unsolicited ARP mode, update your neighbours\n"
		"  -A : ARP answer mode, update your neighbours\n"
		"  -V : print version and exit\n"
		"  -c count : how many packets to send\n"
		"  -w timeout : how long to wait for a reply\n"
		"  -I device : which ethernet device to use"
#ifdef DEFAULT_DEVICE_STR
			" (" DEFAULT_DEVICE_STR ")"
#endif
			"\n"
		"  -s source : source ip address\n"
		"  destination : ask for what ip address\n"
		);
	exit(2);
}

void set_signal(int signo, void (*handler)(void))
{
	struct sigaction sa;

	memset(&sa, 0, sizeof(sa));
	sa.sa_handler = (void (*)(int))handler;
	sa.sa_flags = SA_RESTART;
	sigaction(signo, &sa, NULL);
}

#ifdef CAPABILITIES
static const cap_value_t caps[] = { CAP_NET_RAW, };
static cap_flag_value_t cap_raw = CAP_CLEAR;
#endif

void limit_capabilities(void){

#ifdef CAPABILITIES
	cap_t cap_p;

	cap_p = cap_get_proc();
	if (!cap_p) {
		perror("arping: cap_get_proc");
		exit(-1);
	}

	cap_get_flag(cap_p, CAP_NET_RAW, CAP_PERMITTED, &cap_raw);

	if (cap_raw != CAP_CLEAR) {
		if (cap_clear(cap_p) < 0) {
			perror("arping: cap_clear");
			exit(-1);
		}

		cap_set_flag(cap_p, CAP_PERMITTED, 1, caps, CAP_SET);

		if (cap_set_proc(cap_p) < 0) {
			perror("arping: cap_set_proc");
			if (errno != EPERM)
				exit(-1);
		}
	}

	if (prctl(PR_SET_KEEPCAPS, 1) < 0) {
		perror("arping: prctl");
		exit(-1);
	}

	if (setuid(getuid()) < 0) {
		perror("arping: setuid");
		exit(-1);
	}

	if (prctl(PR_SET_KEEPCAPS, 0) < 0) {
		perror("arping: prctl");
		exit(-1);
	}

	cap_free(cap_p);
#else
	euid = geteuid();
#endif
}

int modify_capability_raw(int on){

#ifdef CAPABILITIES
	cap_t cap_p;

	if (cap_raw != CAP_SET)
		return on ? -1 : 0;

	cap_p = cap_get_proc();
	if (!cap_p) {
		perror("arping: cap_get_proc");
		return -1;
	}

	cap_set_flag(cap_p, CAP_EFFECTIVE, 1, caps, on ? CAP_SET : CAP_CLEAR);

	if (cap_set_proc(cap_p) < 0) {
		perror("arping: cap_set_proc");
		return -1;
	}

	cap_free(cap_p);
#else
	if (setuid(on ? euid : getuid())) {
		perror("arping: setuid");
		return -1;
	}
#endif
	return 0;
}

static inline int enable_capability_raw(void){
	return modify_capability_raw(1);
}

static inline int disable_capability_raw(void){
	return modify_capability_raw(0);
}

void drop_capabilities(void){

#ifdef CAPABILITIES
	cap_t cap_p = cap_init();

	if (!cap_p) {
		perror("arping: cap_init");
		exit(-1);
	}

	if (cap_set_proc(cap_p) < 0) {
		perror("arping: cap_set_proc");
		exit(-1);
	}

	cap_free(cap_p);
#else
	if (setuid(getuid()) < 0) {
		perror("arping: setuid");
		exit(-1);
	}
#endif
}

int send_pack(int s, struct in_addr src, struct in_addr dst,
	      struct sockaddr_ll *ME, struct sockaddr_ll *HE)
{
	int err;
	struct timeval now;
	unsigned char buf[256];
	struct arphdr *ah = (struct arphdr*)buf;
	unsigned char *p = (unsigned char *)(ah+1);

	ah->ar_hrd = htons(ME->sll_hatype);
	if (ah->ar_hrd == htons(ARPHRD_FDDI))
		ah->ar_hrd = htons(ARPHRD_ETHER);
	ah->ar_pro = htons(ETH_P_IP);
	ah->ar_hln = ME->sll_halen;
	ah->ar_pln = 4;
	ah->ar_op  = advert ? htons(ARPOP_REPLY) : htons(ARPOP_REQUEST);

	memcpy(p, &ME->sll_addr, ah->ar_hln);
	p+=ME->sll_halen;

	memcpy(p, &src, 4);
	p+=4;

	if (advert)
		memcpy(p, &ME->sll_addr, ah->ar_hln);
	else
		memcpy(p, &HE->sll_addr, ah->ar_hln);
	p+=ah->ar_hln;

	memcpy(p, &dst, 4);
	p+=4;

	gettimeofday(&now, NULL);
	err = sendto(s, buf, p-buf, 0, (struct sockaddr*)HE, SLL_LEN(ah->ar_hln));
	if (err == p-buf) {
		last = now;
		sent++;
		if (!unicasting)
			brd_sent++;
	}
	return err;
}


void finish(void)
{

	// imprimir estatisticas
	//printf("Fechando\n");
	print_stats(0);

	if (dad)
		exit(!!received);
	if (unsolicited)
		exit(0);

	exit(!received);
}

void catcher(void){
	struct timeval tv, tv_s, tv_o;

	gettimeofday(&tv, NULL);

	if (start.tv_sec==0)
		start = tv;

	timersub(&tv, &start, &tv_s);
	tv_o.tv_sec = timeout;
	tv_o.tv_usec = 500 * 1000;

	if (count-- == 0 || (timeout && timercmp(&tv_s, &tv_o, >)))
		finish();

	timersub(&tv, &last, &tv_s);
	tv_o.tv_sec = 0;

	if (last.tv_sec==0 || timercmp(&tv_s, &tv_o, >)) {
		send_pack(s, src, dst,
			  (struct sockaddr_ll *)&me, (struct sockaddr_ll *)&he);
		if (count == 0 && unsolicited)
			finish();
	}
	alarm(1);
}

void print_hex(unsigned char *p, int len)
{
	int i;
	for (i=0; i<len; i++) {
		printf("%02X", p[i]);
		if (i != len-1)
			printf(":");
	}
}

// Imprimir estatisticas
void print_stats(int reprint_header){
	int nreceived = 0;
	int lost=0;
	long temp_msecs = 0;
	static showcount = 0;
	int show_header = 0;

	showcount++;
	if(reprint_header){
		// mikrotik: 19 pings
		if(showcount == 19){
			show_header = 1;
			showcount=0;
			// printf("\n");

		}else{
			return;
		}
	}


	// string de tempo minimo
	char buf_minrtt[16]; bzero(buf_minrtt, 16);
	long _tmin_usecs = tmin;
	temp_msecs = (_tmin_usecs+500)/1000;
	_tmin_usecs -= temp_msecs*1000 - 500;
	sprintf(buf_minrtt, "%ld.%03ld", temp_msecs, _tmin_usecs);

	// string de tempo maximo
	char buf_maxrtt[16]; bzero(buf_maxrtt, 16);
	long _tmax_usecs = tmax;
	temp_msecs = (_tmax_usecs+500)/1000;
	_tmax_usecs -= temp_msecs*1000 - 500;
	sprintf(buf_maxrtt, "%ld.%03ld", temp_msecs, _tmax_usecs);

	// string de tempo medio
	char buf_avgrtt[16]; bzero(buf_avgrtt, 16);
	long _tavg_usecs = received ? (tsum / received) : 0;
	temp_msecs = (_tavg_usecs+500)/1000;
	_tavg_usecs -= temp_msecs*1000 - 500;
	sprintf(buf_avgrtt, "%ld.%03ld", temp_msecs, _tavg_usecs);

//		tsum /= nreceived + nrepeats;

	// calcular perdas
	if (sent) {
		// enviados....: sent
		// recebidos...: received
		long long sa, rb;
		sa = (long long)sent;
		rb = (long long)received;
		lost = 100;
		if(received){
			// 100 = send
			//  x  = received
			lost = (int) ((((sa - rb)) * 100) / sa);
		}
	}

	if (!quiet) { 
		printf("     ");
		printf("%ssent=%s%ld%s received=%s%d%s packet-loss=%s%d%%%s min-rtt=%s%s%s avg-rtt=%s%s%s max-rtt=%s%s%s",
				KGRN,
				LWHT, sent, KGRN,
				LWHT, received, KGRN, 
				LWHT, lost, KGRN,
					LWHT, buf_minrtt, KGRN, 
					LWHT, buf_avgrtt,KGRN,
					LWHT, buf_maxrtt, RESET
		);
		if(show_header){
			printf("\n");
			print_header();
		}else{
			printf("\n");
		}

		fflush(stdout);

	}

}

// cabecalho
void print_header(void){
	printf("%s%s SEQ TYPE    TARGET         MAC-ADDRESS          TIME      STATUS%s\n",  FONT_BOLD, LWHT, RESET);
//	printf("%s%s SEQ ARP-TYPE                MAC-ADDRESS           TIME    STATUS%s\n",  FONT_BOLD, LWHT, RESET);
  //printf("%s%s SEQ HOST                                      SIZE TTL TIME  STATUS%s\n",  FONT_BOLD, LWHT, RESET);
}


int recv_pack(unsigned char *buf, int len, struct sockaddr_ll *FROM){
	struct timeval tv;
	struct arphdr *ah = (struct arphdr*)buf;
	unsigned char *p = (unsigned char *)(ah+1);
	struct in_addr src_ip, dst_ip;

	gettimeofday(&tv, NULL);

	/* Filter out wild packets */
	if (FROM->sll_pkttype != PACKET_HOST &&
	    FROM->sll_pkttype != PACKET_BROADCAST &&
	    FROM->sll_pkttype != PACKET_MULTICAST)
		return 0;

	/* Only these types are recognised */
	if (ah->ar_op != htons(ARPOP_REQUEST) &&
	    ah->ar_op != htons(ARPOP_REPLY))
		return 0;

	/* ARPHRD check and this darned FDDI hack here :-( */
	if (ah->ar_hrd != htons(FROM->sll_hatype) &&
	    (FROM->sll_hatype != ARPHRD_FDDI || ah->ar_hrd != htons(ARPHRD_ETHER)))
		return 0;

	/* Protocol must be IP. */
	if (ah->ar_pro != htons(ETH_P_IP))
		return 0;
	if (ah->ar_pln != 4)
		return 0;
	if (ah->ar_hln != ((struct sockaddr_ll *)&me)->sll_halen)
		return 0;
	if (len < sizeof(*ah) + 2*(4 + ah->ar_hln))
		return 0;
	memcpy(&src_ip, p+ah->ar_hln, 4);
	memcpy(&dst_ip, p+ah->ar_hln+4+ah->ar_hln, 4);
	if (!dad) {
		if (src_ip.s_addr != dst.s_addr)
			return 0;
		if (src.s_addr != dst_ip.s_addr)
			return 0;
		if (memcmp(p+ah->ar_hln+4, ((struct sockaddr_ll *)&me)->sll_addr, ah->ar_hln))
			return 0;
	} else {
		/* DAD packet was:
		   src_ip = 0 (or some src)
		   src_hw = ME
		   dst_ip = tested address
		   dst_hw = <unspec>

		   We fail, if receive request/reply with:
		   src_ip = tested_address
		   src_hw != ME
		   if src_ip in request was not zero, check
		   also that it matches to dst_ip, otherwise
		   dst_ip/dst_hw do not matter.
		 */
		if (src_ip.s_addr != dst.s_addr)
			return 0;
		if (memcmp(p, ((struct sockaddr_ll *)&me)->sll_addr, ((struct sockaddr_ll *)&me)->sll_halen) == 0)
			return 0;
		if (src.s_addr && src.s_addr != dst_ip.s_addr)
			return 0;
	}

	// ATUALIZAR ESTATISTICAS

	received++;
	if (FROM->sll_pkttype != PACKET_HOST)
		brd_recv++;
	if (ah->ar_op == htons(ARPOP_REQUEST))
		req_recv++;
	if (quit_on_reply)
		finish();
	if(!broadcast_only) {
		memcpy(((struct sockaddr_ll *)&he)->sll_addr, p, ((struct sockaddr_ll *)&me)->sll_halen);
		unicasting=1;
	}

	// ATUALIZAR TEMPOS MINIMOS E MAXIMOS
	if (last.tv_sec) {
		long usecs = (tv.tv_sec-last.tv_sec) * 1000000 + tv.tv_usec-last.tv_usec;
		if(tmin < 0 || tmin > usecs) tmin = usecs;	// minimo
		if(tmax < 0 || tmax < usecs) tmax = usecs;	// maior
		tsum += usecs; // soma total do tempo das respostas
	}

	/*
	tsum += triptime;
	tsum2 += (long long)triptime * (long long)triptime;
	if (triptime < tmin)
		tmin = triptime;
	if (triptime > tmax)
		tmax = triptime;
	if (!rtt)
		rtt = triptime*8;
	else
		rtt += triptime-rtt/8;
	if (options&F_ADAPTIVE)
		update_interval();
	*/


	// IMPRIMIR RESPOSTA
	if (!quiet) {
		int s_printed = 0;
		int tmp = 0;

		// ENVIADOS
		printf("%4u ", sent);

		// Tipo ethernet
		if(ah->ar_op == htons(ARPOP_REPLY)){
			printf("Reply  ");
		}else{
			printf("Request");
		}

		// Tipo de resposta
		if(FROM->sll_pkttype==PACKET_HOST){
			printf(" ");
		}else{
			printf("*");
		}

		//printf("%s ", FROM->sll_pkttype==PACKET_HOST ? "Unicast" : "Broadcast");
		// printf("%s from ", ah->ar_op == htons(ARPOP_REPLY) ? "reply" : "request");
		printf("%-15s", inet_ntoa(src_ip));
		//printf("255.255.255.255 ");
		print_hex(p, ah->ar_hln);
		// printf("] ");

		// espaco entre MAC e time
		printf("    ");

		if (last.tv_sec) {
			char buf[16];
			bzero(buf, 16);

			long usecs = (tv.tv_sec-last.tv_sec) * 1000000 +
				tv.tv_usec-last.tv_usec;
			long msecs = (usecs+500)/1000;
			usecs -= msecs*1000 - 500;


			sprintf(buf, "%ld.%03ld", msecs, usecs);
			printf("%-9s", buf);

		} else {

			printf("%sUNSOLICIT%s", LYEL, RESET);
			tmp = 1;
		}

		// Status
		printf(" ");

		if (dst_ip.s_addr != src.s_addr) {
			printf("%sFor %s %s", LBLU, inet_ntoa(dst_ip), RESET);
			s_printed = 1;
			tmp = 1;
		}
		if (memcmp(p+ah->ar_hln+4, ((struct sockaddr_ll *)&me)->sll_addr, ah->ar_hln)) {
			if (!s_printed)
				printf("%sFor %s", KBLU, RESET);
			printf("%s", LBLU);
			print_hex(p+ah->ar_hln+4, ah->ar_hln);
			printf("%s", RESET);
			tmp = 1;
		}

		// status padrao
		if(!tmp){
			printf("%sOK%s", LGRN, RESET);
		}
		// fim
		printf("\n");

		print_stats(1);

		/*
		if (dst_ip.s_addr != src.s_addr) {
			printf("for %s ", inet_ntoa(dst_ip));
			s_printed = 1;
		}
		if (memcmp(p+ah->ar_hln+4, ((struct sockaddr_ll *)&me)->sll_addr, ah->ar_hln)) {
			if (!s_printed)
				printf("for ");
			printf("[");
			print_hex(p+ah->ar_hln+4, ah->ar_hln);
			printf("]");
		}
		*/



		fflush(stdout);

	}


	return 1;

}

#ifdef USE_SYSFS
union sysfs_devattr_value {
	unsigned long	ulong;
	void		*ptr;
};

enum {
	SYSFS_DEVATTR_IFINDEX,
	SYSFS_DEVATTR_FLAGS,
	SYSFS_DEVATTR_ADDR_LEN,
#if 0
	SYSFS_DEVATTR_TYPE,
	SYSFS_DEVATTR_ADDRESS,
#endif
	SYSFS_DEVATTR_BROADCAST,
	SYSFS_DEVATTR_NUM
};

struct sysfs_devattr_values
{
	char *ifname;
	union sysfs_devattr_value	value[SYSFS_DEVATTR_NUM];
};

static int sysfs_devattr_ulong_dec(char *ptr, struct sysfs_devattr_values *v, unsigned idx);
static int sysfs_devattr_ulong_hex(char *ptr, struct sysfs_devattr_values *v, unsigned idx);
static int sysfs_devattr_macaddr(char *ptr, struct sysfs_devattr_values *v, unsigned idx);

struct sysfs_devattrs {
	const char *name;
	int (*handler)(char *ptr, struct sysfs_devattr_values *v, unsigned int idx);
	int free;
} sysfs_devattrs[SYSFS_DEVATTR_NUM] = {
	[SYSFS_DEVATTR_IFINDEX] = {
		.name		= "ifindex",
		.handler	= sysfs_devattr_ulong_dec,
	},
	[SYSFS_DEVATTR_ADDR_LEN] = {
		.name		= "addr_len",
		.handler	= sysfs_devattr_ulong_dec,
	},
	[SYSFS_DEVATTR_FLAGS] = {
		.name		= "flags",
		.handler	= sysfs_devattr_ulong_hex,
	},
#if 0
	[SYSFS_DEVATTR_TYPE] = {
		.name		= "type",
		.handler	= sysfs_devattr_ulong_dec,
	},
	[SYSFS_DEVATTR_ADDRESS] = {
		.name		= "address",
		.handler	= sysfs_devattr_macaddr,
		.free		= 1,
	},
#endif
	[SYSFS_DEVATTR_BROADCAST] = {
		.name		= "broadcast",
		.handler	= sysfs_devattr_macaddr,
		.free		= 1,
	},
};
#endif

/*
 * find_device()
 *
 * This function checks 1) if the device (if given) is okay for ARP,
 * or 2) find fist appropriate device on the system.
 *
 * Return value:
 *	>0	: Succeeded, and appropriate device not found.
 *		  device.ifindex remains 0.
 *	0	: Succeeded, and approptiate device found.
 *		  device.ifindex is set.
 *	<0	: Failed.  Support not found, or other
 *		: system error.  Try other method.
 *
 * If an appropriate device found, it is recorded inside the
 * "device" variable for later reference.
 *
 * We have several implementations for this.
 *	by_ifaddrs():	requires getifaddr() in glibc, and rtnetlink in
 *			kernel. default and recommended for recent systems.
 *	by_sysfs():	requires libsysfs , and sysfs in kernel.
 *	by_ioctl():	unable to list devices without ipv4 address; this
 *			means, you need to supply the device name for
 *			DAD purpose.
 */
/* Common check for ifa->ifa_flags */
static int check_ifflags(unsigned int ifflags, int fatal)
{
	if (!(ifflags & IFF_UP)) {
		if (fatal) {
			if (!quiet)
				printf("Interface \"%s\" is down\n", device.name);
			exit(2);
		}
		return -1;
	}
	if (ifflags & (IFF_NOARP | IFF_LOOPBACK)) {
		if (fatal) {
			if (!quiet)
				printf("Interface \"%s\" is not ARPable\n", device.name);
			exit(dad ? 0 : 2);
		}
		return -1;
	}
	return 0;
}

static int find_device_by_ifaddrs(void)
{
#ifndef WITHOUT_IFADDRS
	int rc;
	struct ifaddrs *ifa0, *ifa;
	int count = 0;

	rc = getifaddrs(&ifa0);
	if (rc) {
		perror("getifaddrs");
		return -1;
	}

	for (ifa = ifa0; ifa; ifa = ifa->ifa_next) {
		if (!ifa->ifa_addr)
			continue;
		if (ifa->ifa_addr->sa_family != AF_PACKET)
			continue;
		if (device.name && ifa->ifa_name && strcmp(ifa->ifa_name, device.name))
			continue;

		if (check_ifflags(ifa->ifa_flags, device.name != NULL) < 0)
			continue;

		if (!((struct sockaddr_ll *)ifa->ifa_addr)->sll_halen)
			continue;
		if (!ifa->ifa_broadaddr)
			continue;

		device.ifa = ifa;

		if (count++)
			break;
	}

	if (count == 1 && device.ifa) {
		device.ifindex = if_nametoindex(device.ifa->ifa_name);
		if (!device.ifindex) {
			perror("arping: if_nametoindex");
			freeifaddrs(ifa0);
			return -1;
		}
		device.name  = device.ifa->ifa_name;
		return 0;
	}
	return 1;
#else
	return -1;
#endif
}

#ifdef USE_SYSFS
static void sysfs_devattr_values_init(struct sysfs_devattr_values *v, int do_free)
{
	int i;
	if (do_free) {
		free(v->ifname);
		for (i = 0; i < SYSFS_DEVATTR_NUM; i++) {
			if (sysfs_devattrs[i].free)
				free(v->value[i].ptr);
		}
	}
	memset(v, 0, sizeof(*v));
}

static int sysfs_devattr_ulong(char *ptr, struct sysfs_devattr_values *v, unsigned int idx,
				     unsigned int base)
{
	unsigned long *p;
	char *ep;

	if (!ptr || !v)
		return -1;

	p = &v->value[idx].ulong;
	errno = 0;
	*p = strtoul(ptr, &ep, base);
	if ((*ptr && isspace(*ptr & 0xff)) || errno || (*ep != '\0' && *ep != '\n'))
		goto out;

	return 0;
out:
	return -1;
}

static int sysfs_devattr_ulong_dec(char *ptr, struct sysfs_devattr_values *v, unsigned int idx)
{
	int rc = sysfs_devattr_ulong(ptr, v, idx, 10);
	return rc;
}

static int sysfs_devattr_ulong_hex(char *ptr, struct sysfs_devattr_values *v, unsigned int idx)
{
	int rc = sysfs_devattr_ulong(ptr, v, idx, 16);
	return rc;
}

static int sysfs_devattr_macaddr(char *ptr, struct sysfs_devattr_values *v, unsigned int idx)
{
	unsigned char *m;
	int i;
	unsigned int addrlen;

	if (!ptr || !v)
		return -1;

	addrlen = v->value[SYSFS_DEVATTR_ADDR_LEN].ulong;
	m = malloc(addrlen);

	for (i = 0; i < addrlen; i++) {
		if (i && *(ptr + i * 3 - 1) != ':')
			goto out;
		if (sscanf(ptr + i * 3, "%02hhx", &m[i]) != 1)
			goto out;
	}

	v->value[idx].ptr = m;
	return 0;
out:
	free(m);
	return -1;
}
#endif

int find_device_by_sysfs(void)
{
	int rc = -1;
#ifdef USE_SYSFS
	struct sysfs_class *cls_net;
	struct dlist *dev_list;
	struct sysfs_class_device *dev;
	struct sysfs_attribute *dev_attr;
	struct sysfs_devattr_values sysfs_devattr_values;
	int count = 0;

	if (!device.sysfs) {
		device.sysfs = malloc(sizeof(*device.sysfs));
		sysfs_devattr_values_init(device.sysfs, 0);
	}

	cls_net = sysfs_open_class("net");
	if (!cls_net) {
		perror("sysfs_open_class");
		return -1;
	}

	dev_list = sysfs_get_class_devices(cls_net);
	if (!dev_list) {
		perror("sysfs_get_class_devices");
		goto out;
	}

	sysfs_devattr_values_init(&sysfs_devattr_values, 0);

	dlist_for_each_data(dev_list, dev, struct sysfs_class_device) {
		int i;
		int rc = -1;

		if (device.name && strcmp(dev->name, device.name))
			goto do_next;

		sysfs_devattr_values_init(&sysfs_devattr_values, 1);

		for (i = 0; i < SYSFS_DEVATTR_NUM; i++) {

			dev_attr = sysfs_get_classdev_attr(dev, sysfs_devattrs[i].name);
			if (!dev_attr) {
				perror("sysfs_get_classdev_attr");
				rc = -1;
				break;
			}
			if (sysfs_read_attribute(dev_attr)) {
				perror("sysfs_read_attribute");
				rc = -1;
				break;
			}
			rc = sysfs_devattrs[i].handler(dev_attr->value, &sysfs_devattr_values, i);

			if (rc < 0)
				break;
		}

		if (rc < 0)
			goto do_next;

		if (check_ifflags(sysfs_devattr_values.value[SYSFS_DEVATTR_FLAGS].ulong,
				  device.name != NULL) < 0)
			goto do_next;

		if (!sysfs_devattr_values.value[SYSFS_DEVATTR_ADDR_LEN].ulong)
			goto do_next;

		if (device.sysfs->value[SYSFS_DEVATTR_IFINDEX].ulong) {
			if (device.sysfs->value[SYSFS_DEVATTR_FLAGS].ulong & IFF_RUNNING)
				goto do_next;
		}

		sysfs_devattr_values.ifname = strdup(dev->name);
		if (!sysfs_devattr_values.ifname) {
			perror("malloc");
			goto out;
		}

		sysfs_devattr_values_init(device.sysfs, 1);
		memcpy(device.sysfs, &sysfs_devattr_values, sizeof(*device.sysfs));
		sysfs_devattr_values_init(&sysfs_devattr_values, 0);

		if (count++)
			break;

		continue;
do_next:
		sysfs_devattr_values_init(&sysfs_devattr_values, 1);
	}

	if (count == 1) {
		device.ifindex = device.sysfs->value[SYSFS_DEVATTR_IFINDEX].ulong;
		device.name = device.sysfs->ifname;
	}
	rc = !device.ifindex;
out:
	sysfs_close_class(cls_net);
#endif
	return rc;
}

static int check_device_by_ioctl(int s, struct ifreq *ifr)
{
	if (ioctl(s, SIOCGIFFLAGS, ifr) < 0) {
		perror("ioctl(SIOCGIFINDEX");
		return -1;
	}

	if (check_ifflags(ifr->ifr_flags, device.name != NULL) < 0)
		return 1;

	if (ioctl(s, SIOCGIFINDEX, ifr) < 0) {
		perror("ioctl(SIOCGIFINDEX");
		return -1;
	}

	return 0;
}

static int find_device_by_ioctl(void)
{
	int s;
	struct ifreq *ifr0, *ifr, *ifr_end;
	size_t ifrsize = sizeof(*ifr);
	struct ifconf ifc;
	static struct ifreq ifrbuf;
	int count = 0;

	s = socket(AF_INET, SOCK_DGRAM, 0);
	if (s < 0) {
		perror("socket");
		return -1;
	}

	memset(&ifrbuf, 0, sizeof(ifrbuf));

	if (device.name) {
		strncpy(ifrbuf.ifr_name, device.name, sizeof(ifrbuf.ifr_name) - 1);
		if (check_device_by_ioctl(s, &ifrbuf))
			goto out;
		count++;
	} else {
		do {
			int rc;
			ifr0 = malloc(ifrsize);
			if (!ifr0) {
				perror("malloc");
				goto out;
			}

			ifc.ifc_buf = (char *)ifr0;
			ifc.ifc_len = ifrsize;

			rc = ioctl(s, SIOCGIFCONF, &ifc);
			if (rc < 0) {
				perror("ioctl(SIOCFIFCONF");
				goto out;
			}

			if (ifc.ifc_len + sizeof(*ifr0) + sizeof(struct sockaddr_storage) - sizeof(struct sockaddr) <= ifrsize)
				break;
			ifrsize *= 2;
			free(ifr0);
			ifr0 = NULL;
		} while(ifrsize < INT_MAX / 2);

		if (!ifr0) {
			fprintf(stderr, "arping: too many interfaces!?\n");
			goto out;
		}

		ifr_end = (struct ifreq *)(((char *)ifr0) + ifc.ifc_len - sizeof(*ifr0));
		for (ifr = ifr0; ifr <= ifr_end; ifr++) {
			if (check_device_by_ioctl(s, &ifrbuf))
				continue;
			memcpy(&ifrbuf.ifr_name, ifr->ifr_name, sizeof(ifrbuf.ifr_name));
			if (count++)
				break;
		}
	}

	close(s);

	if (count == 1) {
		device.ifindex = ifrbuf.ifr_ifindex;
		device.name = ifrbuf.ifr_name;
	}
	return !device.ifindex;
out:
	close(s);
	return -1;
}

static int find_device(void)
{
	int rc;
	rc = find_device_by_ifaddrs();
	if (rc >= 0)
		goto out;
	rc = find_device_by_sysfs();
	if (rc >= 0)
		goto out;
	rc = find_device_by_ioctl();
out:
	return rc;
}

/*
 * set_device_broadcast()
 *
 * This fills the device "broadcast address"
 * based on information found by find_device() funcion.
 */
static int set_device_broadcast_ifaddrs_one(struct device *device, unsigned char *ba, size_t balen, int fatal)
{
#ifndef WITHOUT_IFADDRS
	struct ifaddrs *ifa;
	struct sockaddr_ll *sll;

	if (!device)
		return -1;

	ifa = device->ifa;
	if (!ifa)
		return -1;

	sll = (struct sockaddr_ll *)ifa->ifa_broadaddr;

	if (sll->sll_halen != balen) {
		if (fatal) {
			if (!quiet)
				printf("Address length does not match...\n");
			exit(2);
		}
		return -1;
	}
	memcpy(ba, sll->sll_addr, sll->sll_halen);
	return 0;
#else
	return -1;
#endif
}
int set_device_broadcast_sysfs(struct device *device, unsigned char *ba, size_t balen)
{
#ifdef USE_SYSFS
	struct sysfs_devattr_values *v;
	if (!device)
		return -1;
	v = device->sysfs;
	if (!v)
		return -1;
	if (v->value[SYSFS_DEVATTR_ADDR_LEN].ulong != balen)
		return -1;
	memcpy(ba, v->value[SYSFS_DEVATTR_BROADCAST].ptr, balen);
	return 0;
#else
	return -1;
#endif
}

static int set_device_broadcast_fallback(struct device *device, unsigned char *ba, size_t balen)
{
	if (!quiet)
		fprintf(stderr, "WARNING: using default broadcast address.\n");
	memset(ba, -1, balen);
	return 0;
}

static void set_device_broadcast(struct device *dev, unsigned char *ba, size_t balen)
{
	if (!set_device_broadcast_ifaddrs_one(dev, ba, balen, 0))
		return;
	if (!set_device_broadcast_sysfs(dev, ba, balen))
		return;
	set_device_broadcast_fallback(dev, ba, balen);
}

int
main(int argc, char **argv)
{
	int socket_errno;
	int ch;

	limit_capabilities();

#ifdef USE_IDN
	setlocale(LC_ALL, "");
#endif

	enable_capability_raw();

	s = socket(PF_PACKET, SOCK_DGRAM, 0);
	socket_errno = errno;

	disable_capability_raw();

	while ((ch = getopt(argc, argv, "h?bfDUAqc:w:s:I:V")) != EOF) {
		switch(ch) {
		case 'b':
			broadcast_only=1;
			break;
		case 'D':
			dad++;
			quit_on_reply=1;
			break;
		case 'U':
			unsolicited++;
			break;
		case 'A':
			advert++;
			unsolicited++;
			break;
		case 'q':
			quiet++;
			break;
		case 'c':
			count = atoi(optarg);
			break;
		case 'w':
			timeout = atoi(optarg);
			break;
		case 'I':
			device.name = optarg;
			break;
		case 'f':
			quit_on_reply=1;
			break;
		case 's':
			source = optarg;
			break;
		case 'V':
			printf("arping utility, iputils-%s\n", SNAPSHOT);
			exit(0);
		case 'h':
		case '?':
		default:
			usage();
		}
	}
	argc -= optind;
	argv += optind;

	if (argc != 1)
		usage();

	target = *argv;

	if (device.name && !*device.name)
		device.name = NULL;

	if (s < 0) {
		errno = socket_errno;
		perror("arping: socket");
		exit(2);
	}

	if (find_device() < 0)
		exit(2);

	if (!device.ifindex) {
		if (device.name) {
			fprintf(stderr, "arping: Device %s not available.\n", device.name);
			exit(2);
		}
		fprintf(stderr, "arping: device (option -I) is required.\n");
		usage();
	}

	if (inet_aton(target, &dst) != 1) {
		struct hostent *hp;
		char *idn = target;
#ifdef USE_IDN
		int rc;

		rc = idna_to_ascii_lz(target, &idn, 0);

		if (rc != IDNA_SUCCESS) {
			fprintf(stderr, "arping: IDN encoding failed: %s\n", idna_strerror(rc));
			exit(2);
		}
#endif

		hp = gethostbyname2(idn, AF_INET);
		if (!hp) {
			fprintf(stderr, "arping: unknown host %s\n", target);
			exit(2);
		}

#ifdef USE_IDN
		free(idn);
#endif

		memcpy(&dst, hp->h_addr, 4);
	}

	if (source && inet_aton(source, &src) != 1) {
		fprintf(stderr, "arping: invalid source %s\n", source);
		exit(2);
	}

	if (!dad && unsolicited && src.s_addr == 0)
		src = dst;

	if (!dad || src.s_addr) {
		struct sockaddr_in saddr;
		int probe_fd = socket(AF_INET, SOCK_DGRAM, 0);

		if (probe_fd < 0) {
			perror("socket");
			exit(2);
		}
		if (device.name) {
			enable_capability_raw();

			if (setsockopt(probe_fd, SOL_SOCKET, SO_BINDTODEVICE, device.name, strlen(device.name)+1) == -1)
				perror("WARNING: interface is ignored");

			disable_capability_raw();
		}
		memset(&saddr, 0, sizeof(saddr));
		saddr.sin_family = AF_INET;
		if (src.s_addr) {
			saddr.sin_addr = src;
			if (bind(probe_fd, (struct sockaddr*)&saddr, sizeof(saddr)) == -1) {
				perror("bind");
				exit(2);
			}
		} else if (!dad) {
			int on = 1;
			socklen_t alen = sizeof(saddr);

			saddr.sin_port = htons(1025);
			saddr.sin_addr = dst;

			if (setsockopt(probe_fd, SOL_SOCKET, SO_DONTROUTE, (char*)&on, sizeof(on)) == -1)
				perror("WARNING: setsockopt(SO_DONTROUTE)");
			if (connect(probe_fd, (struct sockaddr*)&saddr, sizeof(saddr)) == -1) {
				perror("connect");
				exit(2);
			}
			if (getsockname(probe_fd, (struct sockaddr*)&saddr, &alen) == -1) {
				perror("getsockname");
				exit(2);
			}
			src = saddr.sin_addr;
		}
		close(probe_fd);
	};

	((struct sockaddr_ll *)&me)->sll_family = AF_PACKET;
	((struct sockaddr_ll *)&me)->sll_ifindex = device.ifindex;
	((struct sockaddr_ll *)&me)->sll_protocol = htons(ETH_P_ARP);
	if (bind(s, (struct sockaddr*)&me, sizeof(me)) == -1) {
		perror("bind");
		exit(2);
	}

	if (1) {
		socklen_t alen = sizeof(me);
		if (getsockname(s, (struct sockaddr*)&me, &alen) == -1) {
			perror("getsockname");
			exit(2);
		}
	}
	if (((struct sockaddr_ll *)&me)->sll_halen == 0) {
		if (!quiet)
			printf("Interface \"%s\" is not ARPable (no ll address)\n", device.name);
		exit(dad?0:2);
	}

	he = me;

	set_device_broadcast(&device, ((struct sockaddr_ll *)&he)->sll_addr,
			     ((struct sockaddr_ll *)&he)->sll_halen);

/*
	if (!quiet) {
		printf("ARPING %s ", inet_ntoa(dst));
		printf("from %s %s\n",  inet_ntoa(src), device.name ? : "");
	}
*/

	print_header();



	if (!src.s_addr && !dad) {
		fprintf(stderr, "arping: no source address in not-DAD mode\n");
		exit(2);
	}

	drop_capabilities();


	set_signal(SIGINT, finish);
	set_signal(SIGALRM, catcher);


	catcher();

	while(1) {
		sigset_t sset, osset;
		unsigned char packet[4096];
		struct sockaddr_storage from;
		socklen_t alen = sizeof(from);
		int cc;

		if ((cc = recvfrom(s, packet, sizeof(packet), 0,
				   (struct sockaddr *)&from, &alen)) < 0) {
			perror("arping: recvfrom");
			continue;
		}

		sigemptyset(&sset);
		sigaddset(&sset, SIGALRM);
		sigaddset(&sset, SIGINT);
		sigprocmask(SIG_BLOCK, &sset, &osset);
		recv_pack(packet, cc, (struct sockaddr_ll *)&from);
		sigprocmask(SIG_SETMASK, &osset, NULL);
	}
}




File: /clockdiff.c
#include <time.h>
#include <sys/types.h>
#include <sys/param.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <sys/time.h>
#include <sys/timex.h>
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#define TSPTYPES
#include <protocols/timed.h>
#include <fcntl.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <errno.h>
#include <linux/types.h>
#ifdef CAPABILITIES
#include <sys/capability.h>
#endif

void usage(void) __attribute__((noreturn));

#define MAX_HOSTNAMELEN	NI_MAXHOST

/*
 * Checksum routine for Internet Protocol family headers.
 *
 * This routine is very heavily used in the network
 * code and should be modified for each CPU to be as fast as possible.
 *
 * This implementation is TAHOE version.
 */

#undef	ADDCARRY
#define ADDCARRY(sum) { \
	if (sum & 0xffff0000) {	\
		sum &= 0xffff; \
		sum++; \
	} \
}

int in_cksum(u_short *addr, int len)
{
	union word {
		char	c[2];
		u_short	s;
	} u;
	int sum = 0;

	while (len > 0) {
		/*
		 * add by words.
		 */
		while ((len -= 2) >= 0) {
			if ((unsigned long)addr & 0x1) {
				/* word is not aligned */
				u.c[0] = *(char *)addr;
				u.c[1] = *((char *)addr+1);
				sum += u.s;
				addr++;
			} else
				sum += *addr++;
			ADDCARRY(sum);
		}
		if (len == -1)
			/*
			 * Odd number of bytes.
			 */
			u.c[0] = *(u_char *)addr;
	}
	if (len == -1) {
		/* The last mbuf has odd # of bytes. Follow the
		   standard (the odd byte is shifted left by 8 bits) */
		u.c[1] = 0;
		sum += u.s;
		ADDCARRY(sum);
	}
	return (~sum & 0xffff);
}

#define ON		1
#define OFF		0

#define RANGE		1		/* best expected round-trip time, ms */
#define MSGS 		50
#define TRIALS		10

#define GOOD		0
#define UNREACHABLE	2
#define NONSTDTIME	3
#define HOSTDOWN 	0x7fffffff


int interactive = 0;
uint16_t id;
int sock;
int sock_raw;
struct sockaddr_in server;
int ip_opt_len = 0;

#define BIASP	 	43199999
#define BIASN		-43200000
#define MODULO	 	86400000
#define PROCESSING_TIME	0 	/* ms. to reduce error in measurement */

#define PACKET_IN	1024

int measure_delta;
int measure_delta1;
static u_short seqno, seqno0, acked;
long rtt = 1000;
long min_rtt;
long rtt_sigma = 0;

/*
 * Measures the differences between machines' clocks using
 * ICMP timestamp messages.
 */
int
measure(struct sockaddr_in * addr)
{
	socklen_t length;
	int msgcount;
	int cc, count;
	fd_set ready;
	long sendtime, recvtime, histime;
	long min1, min2, diff;
	long delta1, delta2;
	struct timeval tv1, tout;
	u_char packet[PACKET_IN], opacket[64];
	struct icmphdr *icp = (struct icmphdr *) packet;
	struct icmphdr *oicp = (struct icmphdr *) opacket;
	struct iphdr *ip = (struct iphdr *) packet;

	min1 = min2 = 0x7fffffff;
	min_rtt = 0x7fffffff;
	measure_delta = HOSTDOWN;
	measure_delta1 = HOSTDOWN;

/* empties the icmp input queue */
	FD_ZERO(&ready);

empty:
	tout.tv_sec = tout.tv_usec = 0;
	FD_SET(sock_raw, &ready);
	if (select(FD_SETSIZE, &ready, (fd_set *)0, (fd_set *)0, &tout)) {
		length = sizeof(struct sockaddr_in);
		cc = recvfrom(sock_raw, (char *)packet, PACKET_IN, 0,
		    (struct sockaddr *)NULL, &length);
		if (cc < 0)
			return -1;
		goto empty;
	}

	/*
	 * To measure the difference, select MSGS messages whose round-trip
	 * time is smaller than RANGE if ckrange is 1, otherwise simply
	 * select MSGS messages regardless of round-trip transmission time.
	 * Choose the smallest transmission time in each of the two directions.
	 * Use these two latter quantities to compute the delta between
	 * the two clocks.
	 */

	length = sizeof(struct sockaddr_in);
	oicp->type = ICMP_TIMESTAMP;
	oicp->code = 0;
	oicp->checksum = 0;
	oicp->un.echo.id = id;
	((__u32*)(oicp+1))[0] = 0;
	((__u32*)(oicp+1))[1] = 0;
	((__u32*)(oicp+1))[2] = 0;
	FD_ZERO(&ready);
	msgcount = 0;

	acked = seqno = seqno0 = 0;

	for (msgcount = 0; msgcount < MSGS; ) {

	/*
	 * If no answer is received for TRIALS consecutive times,
	 * the machine is assumed to be down
	 */
		if (seqno - acked > TRIALS)
			return HOSTDOWN;

		oicp->un.echo.sequence = ++seqno;
		oicp->checksum = 0;

		(void)gettimeofday (&tv1, (struct timezone *)0);
		*(__u32*)(oicp+1) = htonl((tv1.tv_sec % (24*60*60)) * 1000
					  + tv1.tv_usec / 1000);
		oicp->checksum = in_cksum((u_short *)oicp, sizeof(*oicp) + 12);

		count = sendto(sock_raw, (char *)opacket, sizeof(*oicp)+12, 0,
			       (struct sockaddr *)addr, sizeof(struct sockaddr_in));

		if (count < 0)
			return UNREACHABLE;

		for (;;) {
			FD_ZERO(&ready);
			FD_SET(sock_raw, &ready);
			{
			  long tmo = rtt + rtt_sigma;
			  tout.tv_sec =  tmo/1000;
			  tout.tv_usec = (tmo - (tmo/1000)*1000)*1000;
			}

			if ((count = select(FD_SETSIZE, &ready, (fd_set *)0,
			    (fd_set *)0, &tout)) <= 0)
				break;

			(void)gettimeofday(&tv1, (struct timezone *)0);
			cc = recvfrom(sock_raw, (char *)packet, PACKET_IN, 0,
			    (struct sockaddr *)NULL, &length);

			if (cc < 0)
				return(-1);

			icp = (struct icmphdr *)(packet + (ip->ihl << 2));
			if( icp->type == ICMP_TIMESTAMPREPLY &&
			    icp->un.echo.id == id && icp->un.echo.sequence >= seqno0 &&
						  icp->un.echo.sequence <= seqno) {
			  if (acked < icp->un.echo.sequence)
			    acked = icp->un.echo.sequence;

			  recvtime = (tv1.tv_sec % (24*60*60)) * 1000 +
				     tv1.tv_usec / 1000;
			  sendtime = ntohl(*(__u32*)(icp+1));
			  diff = recvtime - sendtime;
		/*
		 * diff can be less than 0 aroud midnight
		 */
			  if (diff < 0)
			    continue;
			  rtt = (rtt * 3 + diff)/4;
			  rtt_sigma = (rtt_sigma *3 + abs(diff-rtt))/4;
			  msgcount++;
			  histime = ntohl(((__u32*)(icp+1))[1]);
		/*
		 * a hosts using a time format different from
		 * ms. since midnight UT (as per RFC792) should
		 * set the high order bit of the 32-bit time
		 * value it transmits.
		 */
			if ((histime & 0x80000000) != 0)
			  return NONSTDTIME;

			if (interactive) {
			  printf(".");
			  fflush(stdout);
			}

			delta1 = histime - sendtime;
		/*
		 * Handles wrap-around to avoid that around
		 * midnight small time differences appear
		 * enormous. However, the two machine's clocks
		 * must be within 12 hours from each other.
		 */
			if (delta1 < BIASN)
				delta1 += MODULO;
			else if (delta1 > BIASP)
				delta1 -= MODULO;

			delta2 = recvtime - histime;
			if (delta2 < BIASN)
				delta2 += MODULO;
			else if (delta2 > BIASP)
				delta2 -= MODULO;

			if (delta1 < min1)
				min1 = delta1;
			if (delta2 < min2)
				min2 = delta2;
			if (delta1 + delta2 < min_rtt) {
			  min_rtt  = delta1 + delta2;
			  measure_delta1 = (delta1 - delta2)/2 + PROCESSING_TIME;
			}
			if (diff < RANGE) {
				min1 = delta1;
				min2 = delta2;
				goto good_exit;
			}
		      }
		}
	}

good_exit:
	measure_delta = (min1 - min2)/2 + PROCESSING_TIME;
	return GOOD;
}

char *myname, *hisname;

int
measure_opt(struct sockaddr_in * addr)
{
	socklen_t length;
	int msgcount;
	int cc, count;
	fd_set ready;
	long sendtime, recvtime, histime, histime1;
	long min1, min2, diff;
	long delta1, delta2;
	struct timeval tv1, tout;
	u_char packet[PACKET_IN], opacket[64];
	struct icmphdr *icp = (struct icmphdr *) packet;
	struct icmphdr *oicp = (struct icmphdr *) opacket;
	struct iphdr *ip = (struct iphdr *) packet;

	min1 = min2 = 0x7fffffff;
	min_rtt = 0x7fffffff;
	measure_delta = HOSTDOWN;
	measure_delta1 = HOSTDOWN;

/* empties the icmp input queue */
	FD_ZERO(&ready);
empty:
	tout.tv_sec = tout.tv_usec = 0;
	FD_SET(sock_raw, &ready);
	if (select(FD_SETSIZE, &ready, (fd_set *)0, (fd_set *)0, &tout)) {
		length = sizeof(struct sockaddr_in);
		cc = recvfrom(sock_raw, (char *)packet, PACKET_IN, 0,
		    (struct sockaddr *)NULL, &length);
		if (cc < 0)
			return -1;
		goto empty;
	}

	/*
	 * To measure the difference, select MSGS messages whose round-trip
	 * time is smaller than RANGE if ckrange is 1, otherwise simply
	 * select MSGS messages regardless of round-trip transmission time.
	 * Choose the smallest transmission time in each of the two directions.
	 * Use these two latter quantities to compute the delta between
	 * the two clocks.
	 */

	length = sizeof(struct sockaddr_in);
	oicp->type = ICMP_ECHO;
	oicp->code = 0;
	oicp->checksum = 0;
	oicp->un.echo.id = id;
	((__u32*)(oicp+1))[0] = 0;
	((__u32*)(oicp+1))[1] = 0;
	((__u32*)(oicp+1))[2] = 0;

	FD_ZERO(&ready);
	msgcount = 0;

	acked = seqno = seqno0 = 0;

	for (msgcount = 0; msgcount < MSGS; ) {

	/*
	 * If no answer is received for TRIALS consecutive times,
	 * the machine is assumed to be down
	 */
		if ( seqno - acked > TRIALS) {
			errno = EHOSTDOWN;
			return HOSTDOWN;
		}
		oicp->un.echo.sequence = ++seqno;
		oicp->checksum = 0;

		gettimeofday (&tv1, NULL);
		((__u32*)(oicp+1))[0] = htonl((tv1.tv_sec % (24*60*60)) * 1000
					      + tv1.tv_usec / 1000);
		oicp->checksum = in_cksum((u_short *)oicp, sizeof(*oicp)+12);

		count = sendto(sock_raw, (char *)opacket, sizeof(*oicp)+12, 0,
			       (struct sockaddr *)addr, sizeof(struct sockaddr_in));

		if (count < 0) {
			errno = EHOSTUNREACH;
			return UNREACHABLE;
		}

		for (;;) {
			FD_ZERO(&ready);
			FD_SET(sock_raw, &ready);
			{
				long tmo = rtt + rtt_sigma;
				tout.tv_sec =  tmo/1000;
				tout.tv_usec = (tmo - (tmo/1000)*1000)*1000;
			}

			if ((count = select(FD_SETSIZE, &ready, (fd_set *)0,
			    (fd_set *)0, &tout)) <= 0)
				break;

			(void)gettimeofday(&tv1, (struct timezone *)0);
			cc = recvfrom(sock_raw, (char *)packet, PACKET_IN, 0,
				      (struct sockaddr *)NULL, &length);

			if (cc < 0)
				return(-1);

			icp = (struct icmphdr *)(packet + (ip->ihl << 2));
			if (icp->type == ICMP_ECHOREPLY &&
			    packet[20] == IPOPT_TIMESTAMP &&
			    icp->un.echo.id == id &&
			    icp->un.echo.sequence >= seqno0 &&
			    icp->un.echo.sequence <= seqno) {
				int i;
				__u8 *opt = packet+20;

				if (acked < icp->un.echo.sequence)
					acked = icp->un.echo.sequence;
				if ((opt[3]&0xF) != IPOPT_TS_PRESPEC) {
					fprintf(stderr, "Wrong timestamp %d\n", opt[3]&0xF);
					return NONSTDTIME;
				}
				if (opt[3]>>4) {
					if ((opt[3]>>4) != 1 || ip_opt_len != 4+3*8)
						fprintf(stderr, "Overflow %d hops\n", opt[3]>>4);
				}
				sendtime = recvtime = histime = histime1 = 0;
				for (i=0; i < (opt[2]-5)/8; i++) {
					__u32 *timep = (__u32*)(opt+4+i*8+4);
					__u32 t = ntohl(*timep);

					if (t & 0x80000000)
						return NONSTDTIME;

					if (i == 0)
						sendtime = t;
					if (i == 1)
						histime = histime1 = t;
					if (i == 2) {
						if (ip_opt_len == 4+4*8)
							histime1 = t;
						else
							recvtime = t;
					}
					if (i == 3)
						recvtime = t;
				}

				if (!(sendtime&histime&histime1&recvtime)) {
					fprintf(stderr, "wrong timestamps\n");
					return -1;
				}

				diff = recvtime - sendtime;
				/*
				 * diff can be less than 0 aroud midnight
				 */
				if (diff < 0)
					continue;
				rtt = (rtt * 3 + diff)/4;
				rtt_sigma = (rtt_sigma *3 + abs(diff-rtt))/4;
				msgcount++;

				if (interactive) {
					printf(".");
					fflush(stdout);
				}

				delta1 = histime - sendtime;
				/*
				 * Handles wrap-around to avoid that around
				 * midnight small time differences appear
				 * enormous. However, the two machine's clocks
				 * must be within 12 hours from each other.
				 */
				if (delta1 < BIASN)
					delta1 += MODULO;
				else if (delta1 > BIASP)
					delta1 -= MODULO;

				delta2 = recvtime - histime1;
				if (delta2 < BIASN)
					delta2 += MODULO;
				else if (delta2 > BIASP)
					delta2 -= MODULO;

				if (delta1 < min1)
					min1 = delta1;
				if (delta2 < min2)
					min2 = delta2;
				if (delta1 + delta2 < min_rtt) {
					min_rtt  = delta1 + delta2;
					measure_delta1 = (delta1 - delta2)/2 + PROCESSING_TIME;
				}
				if (diff < RANGE) {
					min1 = delta1;
					min2 = delta2;
					goto good_exit;
				}
			}
		}
	}

good_exit:
	measure_delta = (min1 - min2)/2 + PROCESSING_TIME;
	return GOOD;
}


/*
 * Clockdiff computes the difference between the time of the machine on
 * which it is called and the time of the machines given as argument.
 * The time differences measured by clockdiff are obtained using a sequence
 * of ICMP TSTAMP messages which are returned to the sender by the IP module
 * in the remote machine.
 * In order to compare clocks of machines in different time zones, the time
 * is transmitted (as a 32-bit value) in milliseconds since midnight UT.
 * If a hosts uses a different time format, it should set the high order
 * bit of the 32-bit quantity it transmits.
 * However, VMS apparently transmits the time in milliseconds since midnight
 * local time (rather than GMT) without setting the high order bit.
 * Furthermore, it does not understand daylight-saving time.  This makes
 * clockdiff behaving inconsistently with hosts running VMS.
 *
 * In order to reduce the sensitivity to the variance of message transmission
 * time, clockdiff sends a sequence of messages.  Yet, measures between
 * two `distant' hosts can be affected by a small error. The error can, however,
 * be reduced by increasing the number of messages sent in each measurement.
 */

void
usage() {
  fprintf(stderr, "Usage: clockdiff [-o] <host>\n");
  exit(1);
}

void drop_rights(void) {
#ifdef CAPABILITIES
	cap_t caps = cap_init();
	if (cap_set_proc(caps)) {
		perror("clockdiff: cap_set_proc");
		exit(-1);
	}
	cap_free(caps);
#endif
	if (setuid(getuid())) {
		perror("clockdiff: setuid");
		exit(-1);
	}
}

int
main(int argc, char *argv[])
{
	int measure_status;
	struct hostent * hp;
	char hostname[MAX_HOSTNAMELEN];
	int s_errno = 0;
	int n_errno = 0;

	if (argc < 2) {
		drop_rights();
		usage();
	}

	sock_raw = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
	s_errno = errno;

	errno = 0;
	if (nice(-16) == -1)
		n_errno = errno;
	drop_rights();

	if (argc == 3) {
		if (strcmp(argv[1], "-o") == 0) {
			ip_opt_len = 4 + 4*8;
			argv++;
		} else if (strcmp(argv[1], "-o1") == 0) {
			ip_opt_len = 4 + 3*8;
			argv++;
		} else
			usage();
	} else if (argc != 2)
		usage();

	if (sock_raw < 0)  {
		errno = s_errno;
		perror("clockdiff: socket");
		exit(1);
	}

	if (n_errno < 0) {
		errno = n_errno;
		perror("clockdiff: nice");
		exit(1);
	}

	if (isatty(fileno(stdin)) && isatty(fileno(stdout)))
		interactive = 1;

	id = getpid();

	(void)gethostname(hostname,sizeof(hostname));
	hp = gethostbyname(hostname);
	if (hp == NULL) {
		fprintf(stderr, "clockdiff: %s: my host not found\n", hostname);
		exit(1);
	}
	myname = strdup(hp->h_name);

	hp = gethostbyname(argv[1]);
	if (hp == NULL) {
		fprintf(stderr, "clockdiff: %s: host not found\n", argv[1]);
		exit(1);
	}
	hisname = strdup(hp->h_name);

	memset(&server, 0, sizeof(server));
	server.sin_family = hp->h_addrtype;
	memcpy(&(server.sin_addr.s_addr), hp->h_addr, 4);

	if (connect(sock_raw, (struct sockaddr*)&server, sizeof(server)) == -1) {
		perror("connect");
		exit(1);
	}
	if (ip_opt_len) {
		struct sockaddr_in myaddr;
		socklen_t addrlen = sizeof(myaddr);
		unsigned char rspace[ip_opt_len];

		memset(rspace, 0, sizeof(rspace));
		rspace[0] = IPOPT_TIMESTAMP;
		rspace[1] = ip_opt_len;
		rspace[2] = 5;
		rspace[3] = IPOPT_TS_PRESPEC;
		if (getsockname(sock_raw, (struct sockaddr*)&myaddr, &addrlen) == -1) {
			perror("getsockname");
			exit(1);
		}
		((__u32*)(rspace+4))[0*2] = myaddr.sin_addr.s_addr;
		((__u32*)(rspace+4))[1*2] = server.sin_addr.s_addr;
		((__u32*)(rspace+4))[2*2] = myaddr.sin_addr.s_addr;
		if (ip_opt_len == 4+4*8) {
			((__u32*)(rspace+4))[2*2] = server.sin_addr.s_addr;
			((__u32*)(rspace+4))[3*2] = myaddr.sin_addr.s_addr;
		}

		if (setsockopt(sock_raw, IPPROTO_IP, IP_OPTIONS, rspace, ip_opt_len) < 0) {
			perror("ping: IP_OPTIONS (fallback to icmp tstamps)");
			ip_opt_len = 0;
		}
	}

	if ((measure_status = (ip_opt_len ? measure_opt : measure)(&server)) < 0) {
		if (errno)
			perror("measure");
		else
			fprintf(stderr, "measure: unknown failure\n");
		exit(1);
	}

	switch (measure_status) {
	case HOSTDOWN:
		fprintf(stderr, "%s is down\n", hisname);
		exit(1);
	case NONSTDTIME:
		fprintf(stderr, "%s time transmitted in a non-standard format\n", hisname);
		exit(1);
	case UNREACHABLE:
		fprintf(stderr, "%s is unreachable\n", hisname);
		exit(1);
	default:
		break;
	}


	{
		time_t now = time(NULL);

		if (interactive)
			printf("\nhost=%s rtt=%ld(%ld)ms/%ldms delta=%dms/%dms %s", hisname,
			       rtt, rtt_sigma, min_rtt,
			       measure_delta, measure_delta1,
			       ctime(&now));
		else
			printf("%ld %d %d\n", now, measure_delta, measure_delta1);
	}
	exit(0);
}


File: /colors.h
#include <stdio.h>

#ifndef _COLORS_H
#define _COLORS_H

// ---------- Mapa de cores compativeis com readline

// --------------------------------------------- cores ANSI

// ANSI-Cores
#define		 SCREEN_RESET		"\033[00m"	//0
#define		 SCREEN_EMPTY		""			// NULL

#define		SCREEN_CLRSCR		"\033c"		// limpar a tela

// FORMATACAO
#define		 FONT_BOLD		"\033[1m" 		// negrito
#define		 FONT_SUBT		"\033[4m" 		// sublinhado
#define		 FONT_BLINK		"\033[5m" 		// piscando

#define KNRM  "\x1B[0m"
#define KRED  "\x1B[31m"		// vermelho
#define KGRN  "\x1B[32m"		// verde
#define KYEL  "\x1B[33m"		// amarelo
#define KBLU  "\x1B[34m"		// azul
#define KMAG  "\x1B[35m"		// magenta/pink
#define KCYN  "\x1B[36m"		// ciano/azul claro
#define KWHT  "\x1B[37m"		// branco
#define KLGT  "\x1B[38m"		// branco claro
#define RESET "\033[0m"			// restar cores

#define LGRE  "\x1B[90m"		// cinza
#define LRED  "\x1B[91m"		// laranja/vermelho
#define LGRN  "\x1B[92m"		// verde claro
#define LYEL  "\x1B[93m"		// amarelo claro
#define LBLU  "\x1B[94m"		// azul claro
#define LMAG  "\x1B[95m"		// magenta claro
#define LCYN  "\x1B[96m"		// ciano/azul claro
#define LWHT  "\x1B[97m"		// branco claro
#define LLGT  "\x1B[98m"		// branco claro
#define LLGA  "\x1B[99m"		// branco claro

#define L00A  "\x1B[100m"		// branco claro com fundo cinza
#define L00B  "\x1B[101m"		// branco claro com fundo vermelho
#define L00C  "\x1B[102m"		// branco claro com fundo verde
#define L00D  "\x1B[103m"		// branco claro com fundo amarelo
#define L00E  "\x1B[104m"		// branco claro com fundo azul
#define L00F  "\x1B[105m"		// branco claro com fundo magenta
#define L00G  "\x1B[106m"		// branco claro com fundo azul piscina
#define L00H  "\x1B[107m"		// branco claro com fundo azul piscina
#define L00I  "\x1B[108m"		// branco claro com fundo preto

// --------------------------------------------- cores ANSI com readline

#define RL_KNRM  "\001\x1B[0m\002"
#define RL_KRED  "\001\x1B[31m\002"			// vermelho
#define RL_KGRN  "\001\x1B[32m\002"			// verde
#define RL_KYEL  "\001\x1B[33m\002"			// amarelo
#define RL_KBLU  "\001\x1B[34m\002"			// azul
#define RL_KMAG  "\001\x1B[35m\002"			// magenta/pink
#define RL_KCYN  "\001\x1B[36m\002"			// ciano/azul claro
#define RL_KWHT  "\001\x1B[37m\002"			// branco
#define RL_KLGT  "\001\x1B[38m\002"			// branco claro
#define RL_RESET "\001\033[0m\002"			// restar cores

#define RL_LGRE  "\001\x1B[90m\002"			// cinza
#define RL_LRED  "\001\x1B[91m\002"			// laranja/vermelho
#define RL_LGRN  "\001\x1B[92m\002"			// verde claro
#define RL_LYEL  "\001\x1B[93m\002"			// amarelo claro
#define RL_LBLU  "\001\x1B[94m\002"			// azul claro
#define RL_LMAG  "\001\x1B[95m\002"			// magenta claro
#define RL_LCYN  "\001\x1B[96m\002"			// ciano/azul claro
#define RL_LWHT  "\001\x1B[97m\002"			// branco claro
#define RL_LLGT  "\001\x1B[98m\002"			// branco claro
#define RL_LLGA  "\001\x1B[99m\002"			// branco claro

#define RL_L00A  "\001\x1B[100m\002"		// branco claro com fundo cinza
#define RL_L00B  "\001\x1B[101m\002"		// branco claro com fundo vermelho
#define RL_L00C  "\001\x1B[102m\002"		// branco claro com fundo verde
#define RL_L00D  "\001\x1B[103m\002"		// branco claro com fundo amarelo
#define RL_L00E  "\001\x1B[104m\002"		// branco claro com fundo azul
#define RL_L00F  "\001\x1B[105m\002"		// branco claro com fundo magenta
#define RL_L00G  "\001\x1B[106m\002"		// branco claro com fundo azul piscina
#define RL_L00H  "\001\x1B[107m\002"		// branco claro com fundo azul piscina


#endif



















File: /in6_flowlabel.h
/*
   It is just a stripped copy of the kernel header "linux/in6.h"

   "Flow label" things are still not defined in "netinet/in*.h" headers,
   but we cannot use "linux/in6.h" immediately because it currently
   conflicts with "netinet/in.h" .
*/

struct in6_flowlabel_req
{
	struct in6_addr	flr_dst;
	__u32	flr_label;
	__u8	flr_action;
	__u8	flr_share;
	__u16	flr_flags;
	__u16 	flr_expires;
	__u16	flr_linger;
	__u32	__flr_pad;
	/* Options in format of IPV6_PKTOPTIONS */
};

#define IPV6_FL_A_GET	0
#define IPV6_FL_A_PUT	1
#define IPV6_FL_A_RENEW	2

#define IPV6_FL_F_CREATE	1
#define IPV6_FL_F_EXCL		2

#define IPV6_FL_S_NONE		0
#define IPV6_FL_S_EXCL		1
#define IPV6_FL_S_PROCESS	2
#define IPV6_FL_S_USER		3
#define IPV6_FL_S_ANY		255

#define IPV6_FLOWINFO_FLOWLABEL		0x000fffff
#define IPV6_FLOWINFO_PRIORITY		0x0ff00000

#define IPV6_FLOWLABEL_MGR	32
#define IPV6_FLOWINFO_SEND	33


File: /INSTALL

make
make html
make man
lynx doc/iputils.html
Read...



If the first "make" fails, no problems:

make html
lynx doc/iputils.html
Read section "Installation notes"...



But if "make html" fails too, check that DocBook package is installed
on your machine. If it is installed, and nevertheless "make" does not work,
delete iputils and go to sleep. The next day repeat. If even full reset
did not help, I bring apologies. :-)





File: /ipg
#! /bin/bash

if [ -e /proc/modules ] ; then
	modprobe pg3 >& /dev/null
	modprobe pktgen >& /dev/null
fi

for PGDEV in /proc/net/pg /proc/net/pktgen/pg0 / ; do
	[ -e ${PGDEV} ] && break
done
if [ "${PGDEV}" = "/" ] ; then
	echo "Could not locate pg in /proc/net" 1>&2
	exit 1
fi

function pgset() {
    local result

    echo $1 > ${PGDEV}

    result=`cat ${PGDEV} | fgrep "Result: OK:"`
    if [ "$result" = "" ]; then
         cat ${PGDEV} | fgrep Result:
    fi
}

function pg() {
    echo inject > ${PGDEV}
    cat ${PGDEV}
}

pgset "odev eth0"
pgset "dst 0.0.0.0"



File: /iputils.spec
#
# This spec file is for _testing_.
#

%define ssdate 20121221
Summary: The ping program for checking to see if network hosts are alive.
Name: iputils
Version: s%{ssdate}
Release: 1local
License: GPLv2+
Group: System Environment/Daemons
Source0: iputils-s%{ssdate}.tar.bz2
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-root
#BuildPrereq: docbook-dtd31-sgml, perl
Requires: kernel >= 2.4.7

%description
The iputils package contains ping, a basic networking tool.  The ping
command sends a series of ICMP protocol ECHO_REQUEST packets to a
specified network host and can tell you if that machine is alive and
receiving network traffic.

%prep
%setup -q %{name}

%build
make
make ninfod
make man
make html

%install
rm -fr ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}

install -c clockdiff            ${RPM_BUILD_ROOT}%{_sbindir}/
install -cp arping              ${RPM_BUILD_ROOT}%{_sbindir}/
install -cp ping                ${RPM_BUILD_ROOT}%{_bindir}/
install -cp rdisc               ${RPM_BUILD_ROOT}%{_sbindir}/
install -cp ping6               ${RPM_BUILD_ROOT}%{_bindir}/
install -cp tracepath           ${RPM_BUILD_ROOT}%{_bindir}/
install -cp tracepath6          ${RPM_BUILD_ROOT}%{_bindir}/
install -cp ninfod/ninfod       ${RPM_BUILD_ROOT}%{_sbindir}/

mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
ln -sf ../bin/ping6 ${RPM_BUILD_ROOT}%{_sbindir}
ln -sf ../bin/tracepath ${RPM_BUILD_ROOT}%{_sbindir}
ln -sf ../bin/tracepath6 ${RPM_BUILD_ROOT}%{_sbindir}

mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
install -cp doc/clockdiff.8     ${RPM_BUILD_ROOT}%{_mandir}/man8/
install -cp doc/arping.8        ${RPM_BUILD_ROOT}%{_mandir}/man8/
install -cp doc/ping.8          ${RPM_BUILD_ROOT}%{_mandir}/man8/
install -cp doc/rdisc.8         ${RPM_BUILD_ROOT}%{_mandir}/man8/
install -cp doc/tracepath.8     ${RPM_BUILD_ROOT}%{_mandir}/man8/
install -cp doc/ninfod.8        ${RPM_BUILD_ROOT}%{_mandir}/man8/
ln -s ping.8.gz ${RPM_BUILD_ROOT}%{_mandir}/man8/ping6.8.gz
ln -s tracepath.8.gz ${RPM_BUILD_ROOT}%{_mandir}/man8/tracepath6.8.gz

iconv -f ISO88591 -t UTF8 RELNOTES -o RELNOTES.tmp
touch -r RELNOTES RELNOTES.tmp
mv -f RELNOTES.tmp RELNOTES

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc RELNOTES
%attr(0755,root,root) %caps(cap_net_raw=ep) %{_sbindir}/clockdiff
#%attr(4755,root,root) %{_sbindir}/clockdiff
%attr(0755,root,root) %caps(cap_net_raw=ep) %{_sbindir}/arping
#%attr(4755,root,root) %{_sbindir}/arping
%attr(0755,root,root) %caps(cap_net_raw=ep cap_net_admin=ep) %{_bindir}/ping
#%attr(4755,root,root) %{_bindir}/ping
%attr(0755,root,root) %caps(cap_net_raw=ep cap_net_admin=ep) %{_bindir}/ping6
#%attr(4755,root,root) %{_bindir}/ping6
%{_sbindir}/rdisc
%{_bindir}/tracepath
%{_bindir}/tracepath6
%{_sbindir}/ping6
%{_sbindir}/tracepath
%{_sbindir}/tracepath6
%{_sbindir}/ninfod
%attr(644,root,root) %{_mandir}/man8/*

%changelog
* Fri Nov 30 2012 YOSHIFUJI Hideaki <yoshfuji@linux-ipv6.org>
  Partically sync with current Fedora's specfile.
* Sat Feb 23 2001 Alexey Kuznetsov <kuznet@ms2.inr.ac.ru>
  Taken iputils rpm from ASPLinux-7.2 as pattern.


File: /Makefile
#
# Configuration
#

# CC
CC=gcc
# Path to parent kernel include files directory
LIBC_INCLUDE=/usr/include
# Libraries
ADDLIB=
# Linker flags
LDFLAG_STATIC=-Wl,-Bstatic
LDFLAG_DYNAMIC=-Wl,-Bdynamic
LDFLAG_CAP=-lcap
LDFLAG_GNUTLS=-lgnutls-openssl
LDFLAG_CRYPTO=-lcrypto
LDFLAG_IDN=-lidn
LDFLAG_RESOLV=-lresolv
LDFLAG_SYSFS=-lsysfs

#
# Options
#

# Capability support (with libcap) [yes|static|no]
USE_CAP=yes
# sysfs support (with libsysfs - deprecated) [no|yes|static]
USE_SYSFS=no
# IDN support (experimental) [no|yes|static]
USE_IDN=no

# Do not use getifaddrs [no|yes|static]
WITHOUT_IFADDRS=no
# arping default device (e.g. eth0) []
ARPING_DEFAULT_DEVICE=

# GNU TLS library for ping6 [yes|no|static]
USE_GNUTLS=yes
# Crypto library for ping6 [shared|static]
USE_CRYPTO=shared
# Resolv library for ping6 [yes|static]
USE_RESOLV=yes
# ping6 source routing (deprecated by RFC5095) [no|yes|RFC3542]
ENABLE_PING6_RTHDR=no

# rdisc server (-r option) support [no|yes]
ENABLE_RDISC_SERVER=no

# -------------------------------------
# What a pity, all new gccs are buggy and -Werror does not work. Sigh.
# CCOPT=-fno-strict-aliasing -Wstrict-prototypes -Wall -Werror -g
CCOPT=-fno-strict-aliasing -Wstrict-prototypes -Wall -g
CCOPTOPT=-O3
GLIBCFIX=-D_GNU_SOURCE
DEFINES=
LDLIB=

FUNC_LIB = $(if $(filter static,$(1)),$(LDFLAG_STATIC) $(2) $(LDFLAG_DYNAMIC),$(2))

# USE_GNUTLS: DEF_GNUTLS, LIB_GNUTLS
# USE_CRYPTO: LIB_CRYPTO
ifneq ($(USE_GNUTLS),no)
	LIB_CRYPTO = $(call FUNC_LIB,$(USE_GNUTLS),$(LDFLAG_GNUTLS))
	DEF_CRYPTO = -DUSE_GNUTLS
else
	LIB_CRYPTO = $(call FUNC_LIB,$(USE_CRYPTO),$(LDFLAG_CRYPTO))
endif

# USE_RESOLV: LIB_RESOLV
LIB_RESOLV = $(call FUNC_LIB,$(USE_RESOLV),$(LDFLAG_RESOLV))

# USE_CAP:  DEF_CAP, LIB_CAP
ifneq ($(USE_CAP),no)
	DEF_CAP = -DCAPABILITIES
	LIB_CAP = $(call FUNC_LIB,$(USE_CAP),$(LDFLAG_CAP))
endif

# USE_SYSFS: DEF_SYSFS, LIB_SYSFS
ifneq ($(USE_SYSFS),no)
	DEF_SYSFS = -DUSE_SYSFS
	LIB_SYSFS = $(call FUNC_LIB,$(USE_SYSFS),$(LDFLAG_SYSFS))
endif

# USE_IDN: DEF_IDN, LIB_IDN
ifneq ($(USE_IDN),no)
	DEF_IDN = -DUSE_IDN
	LIB_IDN = $(call FUNC_LIB,$(USE_IDN),$(LDFLAG_IDN))
endif

# WITHOUT_IFADDRS: DEF_WITHOUT_IFADDRS
ifneq ($(WITHOUT_IFADDRS),no)
	DEF_WITHOUT_IFADDRS = -DWITHOUT_IFADDRS
endif

# ENABLE_RDISC_SERVER: DEF_ENABLE_RDISC_SERVER
ifneq ($(ENABLE_RDISC_SERVER),no)
	DEF_ENABLE_RDISC_SERVER = -DRDISC_SERVER
endif

# ENABLE_PING6_RTHDR: DEF_ENABLE_PING6_RTHDR
ifneq ($(ENABLE_PING6_RTHDR),no)
	DEF_ENABLE_PING6_RTHDR = -DPING6_ENABLE_RTHDR
ifeq ($(ENABLE_PING6_RTHDR),RFC3542)
	DEF_ENABLE_PING6_RTHDR += -DPINR6_ENABLE_RTHDR_RFC3542
endif
endif

# -------------------------------------
IPV4_TARGETS=tracepath ping clockdiff rdisc arping tftpd rarpd
IPV6_TARGETS=tracepath6 traceroute6 ping6
TARGETS=$(IPV4_TARGETS) $(IPV6_TARGETS)

CFLAGS=$(CCOPTOPT) $(CCOPT) $(GLIBCFIX) $(DEFINES)
LDLIBS=$(LDLIB) $(ADDLIB)

UNAME_N:=$(shell uname -n)
LASTTAG:=$(shell git describe HEAD | sed -e 's/-.*//')
TODAY=$(shell date +%Y/%m/%d)
DATE=$(shell date --date $(TODAY) +%Y%m%d)
TAG:=$(shell date --date=$(TODAY) +s%Y%m%d)


# -------------------------------------
.PHONY: all ninfod clean distclean man html check-kernel modules

all: $(TARGETS)

%.s: %.c
	$(COMPILE.c) $< $(DEF_$(patsubst %.o,%,$@)) -S -o $@
%.o: %.c
	$(COMPILE.c) $< $(DEF_$(patsubst %.o,%,$@)) -o $@
$(TARGETS): %: %.o
	$(LINK.o) $^ $(LIB_$@) $(LDLIBS) -o $@

# -------------------------------------
# arping
DEF_arping = $(DEF_SYSFS) $(DEF_CAP) $(DEF_IDN) $(DEF_WITHOUT_IFADDRS)
LIB_arping = $(LIB_SYSFS) $(LIB_CAP) $(LIB_IDN)

ifneq ($(ARPING_DEFAULT_DEVICE),)
DEF_arping += -DDEFAULT_DEVICE=\"$(ARPING_DEFAULT_DEVICE)\"
endif

# clockdiff
DEF_clockdiff = $(DEF_CAP)
LIB_clockdiff = $(LIB_CAP)

# ping / ping6
DEF_ping_common = $(DEF_CAP) $(DEF_IDN)
DEF_ping  = $(DEF_CAP) $(DEF_IDN) $(DEF_WITHOUT_IFADDRS)
LIB_ping  = $(LIB_CAP) $(LIB_IDN)
DEF_ping6 = $(DEF_CAP) $(DEF_IDN) $(DEF_WITHOUT_IFADDRS) $(DEF_ENABLE_PING6_RTHDR)
LIB_ping6 = $(LIB_CAP) $(LIB_IDN) $(LIB_RESOLV) $(LIB_CRYPTO)

ping: ping_common.o
ping6: ping_common.o
ping.o ping_common.o: ping_common.h
ping6.o: ping_common.h in6_flowlabel.h

# rarpd
DEF_rarpd =
LIB_rarpd =

# rdisc
DEF_rdisc = $(DEF_ENABLE_RDISC_SERVER)
LIB_rdisc =

# tracepath
DEF_tracepath = $(DEF_IDN)
LIB_tracepath = $(LIB_IDN)

# tracepath6
DEF_tracepath6 = $(DEF_IDN)
LIB_tracepath6 =

# traceroute6
DEF_traceroute6 = $(DEF_CAP) $(DEF_IDN)
LIB_traceroute6 = $(LIB_CAP) $(LIB_IDN)

# tftpd
DEF_tftpd =
DEF_tftpsubs =
LIB_tftpd =

tftpd: tftpsubs.o
tftpd.o tftpsubs.o: tftp.h

# -------------------------------------
# ninfod
ninfod:
	@set -e; \
		if [ ! -f ninfod/Makefile ]; then \
			cd ninfod; \
			./configure; \
			cd ..; \
		fi; \
		$(MAKE) -C ninfod

# -------------------------------------
# modules / check-kernel are only for ancient kernels; obsolete
check-kernel:
ifeq ($(KERNEL_INCLUDE),)
	@echo "Please, set correct KERNEL_INCLUDE"; false
else
	@set -e; \
	if [ ! -r $(KERNEL_INCLUDE)/linux/autoconf.h ]; then \
		echo "Please, set correct KERNEL_INCLUDE"; false; fi
endif

modules: check-kernel
	$(MAKE) KERNEL_INCLUDE=$(KERNEL_INCLUDE) -C Modules

# -------------------------------------

clean:
	@rm -f *.o $(TARGETS)
	@set -e; \
		if [ -f ninfod/Makefile ]; then \
			$(MAKE) -C ninfod clean; \
		fi

distclean: clean
	@set -e; \
		if [ -f ninfod/Makefile ]; then \
			$(MAKE) -C ninfod distclean; \
		fi



File: /ninfod\config.h.in
/* config.h.in.  Generated from configure.in by autoheader.  */

/* Define if building universal (internal helper macro) */
#undef AC_APPLE_UNIVERSAL_BUILD

/* Enable debugging */
#undef ENABLE_DEBUG

/* Enable ttl support for qtypes (deprecated) */
#undef ENABLE_SUPTYPES

/* Enable threads */
#undef ENABLE_THREADS

/* Define to 1 if you have the <arpa/inet.h> header file. */
#undef HAVE_ARPA_INET_H

/* Define to 1 if you have the <gnutls/openssl.h> header file. */
#undef HAVE_GNUTLS_OPENSSL_H

/* Define to 1 if you have the <inttypes.h> header file. */
#undef HAVE_INTTYPES_H

/* Define to 1 if you have the `cap' library (-lcap). */
#undef HAVE_LIBCAP

/* Define to 1 if you have the `pthread' library (-lpthread). */
#undef HAVE_LIBPTHREAD

/* Define to 1 if you have the <limits.h> header file. */
#undef HAVE_LIMITS_H

/* Define to 1 if you have the <linux/rtnetlink.h> header file. */
#undef HAVE_LINUX_RTNETLINK_H

/* Define to 1 if you have the <memory.h> header file. */
#undef HAVE_MEMORY_H

/* Define to 1 if you have the `nanosleep' function. */
#undef HAVE_NANOSLEEP

/* Define to 1 if you have the <netdb.h> header file. */
#undef HAVE_NETDB_H

/* Define to 1 if you have the <netinet/icmp6.h> header file. */
#undef HAVE_NETINET_ICMP6_H

/* Define to 1 if you have the <netinet/in.h> header file. */
#undef HAVE_NETINET_IN_H

/* Define to 1 if you have the <netinet/ip6.h> header file. */
#undef HAVE_NETINET_IP6_H

/* Define to 1 if you have the <openssl/md5.h> header file. */
#undef HAVE_OPENSSL_MD5_H

/* Define to 1 if you have the <pthread.h> header file. */
#undef HAVE_PTHREAD_H

/* Define to 1 if you have the <pwd.h> header file. */
#undef HAVE_PWD_H

/* Define to 1 if you have the <stdint.h> header file. */
#undef HAVE_STDINT_H

/* Define to 1 if you have the <stdlib.h> header file. */
#undef HAVE_STDLIB_H

/* Define to 1 if you have the <strings.h> header file. */
#undef HAVE_STRINGS_H

/* Define to 1 if you have the <string.h> header file. */
#undef HAVE_STRING_H

/* Define to 1 if you have struct icmp6_nodeinfo */
#undef HAVE_STRUCT_ICMP6_NODEINFO

/* Define to 1 if you have the <syslog.h> header file. */
#undef HAVE_SYSLOG_H

/* Define to 1 if you have the <sys/capability.h> header file. */
#undef HAVE_SYS_CAPABILITY_H

/* Define to 1 if you have the <sys/stat.h> header file. */
#undef HAVE_SYS_STAT_H

/* Define to 1 if you have the <sys/types.h> header file. */
#undef HAVE_SYS_TYPES_H

/* Define to 1 if you have the <sys/uio.h> header file. */
#undef HAVE_SYS_UIO_H

/* Define to 1 if you have the <sys/utsname.h> header file. */
#undef HAVE_SYS_UTSNAME_H

/* Define to 1 if you have the <unistd.h> header file. */
#undef HAVE_UNISTD_H

/* Define to the address where bug reports for this package should be sent. */
#undef PACKAGE_BUGREPORT

/* Define to the full name of this package. */
#undef PACKAGE_NAME

/* Define to the full name and version of this package. */
#undef PACKAGE_STRING

/* Define to the one symbol short name of this package. */
#undef PACKAGE_TARNAME

/* Define to the home page for this package. */
#undef PACKAGE_URL

/* Define to the version of this package. */
#undef PACKAGE_VERSION

/* Define to 1 if you have the ANSI C header files. */
#undef STDC_HEADERS

/* Define to 1 if you can safely include both <sys/time.h> and <time.h>. */
#undef TIME_WITH_SYS_TIME

/* Define WORDS_BIGENDIAN to 1 if your processor stores words with the most
   significant byte first (like Motorola and SPARC, unlike Intel). */
#if defined AC_APPLE_UNIVERSAL_BUILD
# if defined __BIG_ENDIAN__
#  define WORDS_BIGENDIAN 1
# endif
#else
# ifndef WORDS_BIGENDIAN
#  undef WORDS_BIGENDIAN
# endif
#endif

/* Define to empty if `const' does not conform to ANSI C. */
#undef const

/* Define to `unsigned int' if <sys/types.h> does not define. */
#undef size_t


File: /ninfod\configure
#! /bin/sh
# Guess values for system-dependent variables and create Makefiles.
# Generated by GNU Autoconf 2.68.
#
#
# Copyright (C) 1992, 1993, 1994, 1995, 1996, 1998, 1999, 2000, 2001,
# 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010 Free Software
# Foundation, Inc.
#
#
# This configure script is free software; the Free Software Foundation
# gives unlimited permission to copy, distribute and modify it.
#
# Copyright (C)2002 USAGI/WIDE Project.  All Rights Reserved.
## -------------------- ##
## M4sh Initialization. ##
## -------------------- ##

# Be more Bourne compatible
DUALCASE=1; export DUALCASE # for MKS sh
if test -n "${ZSH_VERSION+set}" && (emulate sh) >/dev/null 2>&1; then :
  emulate sh
  NULLCMD=:
  # Pre-4.2 versions of Zsh do word splitting on ${1+"$@"}, which
  # is contrary to our usage.  Disable this feature.
  alias -g '${1+"$@"}'='"$@"'
  setopt NO_GLOB_SUBST
else
  case `(set -o) 2>/dev/null` in #(
  *posix*) :
    set -o posix ;; #(
  *) :
     ;;
esac
fi


as_nl='
'
export as_nl
# Printing a long string crashes Solaris 7 /usr/bin/printf.
as_echo='\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\'
as_echo=$as_echo$as_echo$as_echo$as_echo$as_echo
as_echo=$as_echo$as_echo$as_echo$as_echo$as_echo$as_echo
# Prefer a ksh shell builtin over an external printf program on Solaris,
# but without wasting forks for bash or zsh.
if test -z "$BASH_VERSION$ZSH_VERSION" \
    && (test "X`print -r -- $as_echo`" = "X$as_echo") 2>/dev/null; then
  as_echo='print -r --'
  as_echo_n='print -rn --'
elif (test "X`printf %s $as_echo`" = "X$as_echo") 2>/dev/null; then
  as_echo='printf %s\n'
  as_echo_n='printf %s'
else
  if test "X`(/usr/ucb/echo -n -n $as_echo) 2>/dev/null`" = "X-n $as_echo"; then
    as_echo_body='eval /usr/ucb/echo -n "$1$as_nl"'
    as_echo_n='/usr/ucb/echo -n'
  else
    as_echo_body='eval expr "X$1" : "X\\(.*\\)"'
    as_echo_n_body='eval
      arg=$1;
      case $arg in #(
      *"$as_nl"*)
	expr "X$arg" : "X\\(.*\\)$as_nl";
	arg=`expr "X$arg" : ".*$as_nl\\(.*\\)"`;;
      esac;
      expr "X$arg" : "X\\(.*\\)" | tr -d "$as_nl"
    '
    export as_echo_n_body
    as_echo_n='sh -c $as_echo_n_body as_echo'
  fi
  export as_echo_body
  as_echo='sh -c $as_echo_body as_echo'
fi

# The user is always right.
if test "${PATH_SEPARATOR+set}" != set; then
  PATH_SEPARATOR=:
  (PATH='/bin;/bin'; FPATH=$PATH; sh -c :) >/dev/null 2>&1 && {
    (PATH='/bin:/bin'; FPATH=$PATH; sh -c :) >/dev/null 2>&1 ||
      PATH_SEPARATOR=';'
  }
fi


# IFS
# We need space, tab and new line, in precisely that order.  Quoting is
# there to prevent editors from complaining about space-tab.
# (If _AS_PATH_WALK were called with IFS unset, it would disable word
# splitting by setting IFS to empty value.)
IFS=" ""	$as_nl"

# Find who we are.  Look in the path if we contain no directory separator.
as_myself=
case $0 in #((
  *[\\/]* ) as_myself=$0 ;;
  *) as_save_IFS=$IFS; IFS=$PATH_SEPARATOR
for as_dir in $PATH
do
  IFS=$as_save_IFS
  test -z "$as_dir" && as_dir=.
    test -r "$as_dir/$0" && as_myself=$as_dir/$0 && break
  done
IFS=$as_save_IFS

     ;;
esac
# We did not find ourselves, most probably we were run as `sh COMMAND'
# in which case we are not to be found in the path.
if test "x$as_myself" = x; then
  as_myself=$0
fi
if test ! -f "$as_myself"; then
  $as_echo "$as_myself: error: cannot find myself; rerun with an absolute file name" >&2
  exit 1
fi

# Unset variables that we do not need and which cause bugs (e.g. in
# pre-3.0 UWIN ksh).  But do not cause bugs in bash 2.01; the "|| exit 1"
# suppresses any "Segmentation fault" message there.  '((' could
# trigger a bug in pdksh 5.2.14.
for as_var in BASH_ENV ENV MAIL MAILPATH
do eval test x\${$as_var+set} = xset \
  && ( (unset $as_var) || exit 1) >/dev/null 2>&1 && unset $as_var || :
done
PS1='$ '
PS2='> '
PS4='+ '

# NLS nuisances.
LC_ALL=C
export LC_ALL
LANGUAGE=C
export LANGUAGE

# CDPATH.
(unset CDPATH) >/dev/null 2>&1 && unset CDPATH

if test "x$CONFIG_SHELL" = x; then
  as_bourne_compatible="if test -n \"\${ZSH_VERSION+set}\" && (emulate sh) >/dev/null 2>&1; then :
  emulate sh
  NULLCMD=:
  # Pre-4.2 versions of Zsh do word splitting on \${1+\"\$@\"}, which
  # is contrary to our usage.  Disable this feature.
  alias -g '\${1+\"\$@\"}'='\"\$@\"'
  setopt NO_GLOB_SUBST
else
  case \`(set -o) 2>/dev/null\` in #(
  *posix*) :
    set -o posix ;; #(
  *) :
     ;;
esac
fi
"
  as_required="as_fn_return () { (exit \$1); }
as_fn_success () { as_fn_return 0; }
as_fn_failure () { as_fn_return 1; }
as_fn_ret_success () { return 0; }
as_fn_ret_failure () { return 1; }

exitcode=0
as_fn_success || { exitcode=1; echo as_fn_success failed.; }
as_fn_failure && { exitcode=1; echo as_fn_failure succeeded.; }
as_fn_ret_success || { exitcode=1; echo as_fn_ret_success failed.; }
as_fn_ret_failure && { exitcode=1; echo as_fn_ret_failure succeeded.; }
if ( set x; as_fn_ret_success y && test x = \"\$1\" ); then :

else
  exitcode=1; echo positional parameters were not saved.
fi
test x\$exitcode = x0 || exit 1"
  as_suggested="  as_lineno_1=";as_suggested=$as_suggested$LINENO;as_suggested=$as_suggested" as_lineno_1a=\$LINENO
  as_lineno_2=";as_suggested=$as_suggested$LINENO;as_suggested=$as_suggested" as_lineno_2a=\$LINENO
  eval 'test \"x\$as_lineno_1'\$as_run'\" != \"x\$as_lineno_2'\$as_run'\" &&
  test \"x\`expr \$as_lineno_1'\$as_run' + 1\`\" = \"x\$as_lineno_2'\$as_run'\"' || exit 1
test \$(( 1 + 1 )) = 2 || exit 1"
  if (eval "$as_required") 2>/dev/null; then :
  as_have_required=yes
else
  as_have_required=no
fi
  if test x$as_have_required = xyes && (eval "$as_suggested") 2>/dev/null; then :

else
  as_save_IFS=$IFS; IFS=$PATH_SEPARATOR
as_found=false
for as_dir in /bin$PATH_SEPARATOR/usr/bin$PATH_SEPARATOR$PATH
do
  IFS=$as_save_IFS
  test -z "$as_dir" && as_dir=.
  as_found=:
  case $as_dir in #(
	 /*)
	   for as_base in sh bash ksh sh5; do
	     # Try only shells that exist, to save several forks.
	     as_shell=$as_dir/$as_base
	     if { test -f "$as_shell" || test -f "$as_shell.exe"; } &&
		    { $as_echo "$as_bourne_compatible""$as_required" | as_run=a "$as_shell"; } 2>/dev/null; then :
  CONFIG_SHELL=$as_shell as_have_required=yes
		   if { $as_echo "$as_bourne_compatible""$as_suggested" | as_run=a "$as_shell"; } 2>/dev/null; then :
  break 2
fi
fi
	   done;;
       esac
  as_found=false
done
$as_found || { if { test -f "$SHELL" || test -f "$SHELL.exe"; } &&
	      { $as_echo "$as_bourne_compatible""$as_required" | as_run=a "$SHELL"; } 2>/dev/null; then :
  CONFIG_SHELL=$SHELL as_have_required=yes
fi; }
IFS=$as_save_IFS


      if test "x$CONFIG_SHELL" != x; then :
  # We cannot yet assume a decent shell, so we have to provide a
	# neutralization value for shells without unset; and this also
	# works around shells that cannot unset nonexistent variables.
	# Preserve -v and -x to the replacement shell.
	BASH_ENV=/dev/null
	ENV=/dev/null
	(unset BASH_ENV) >/dev/null 2>&1 && unset BASH_ENV ENV
	export CONFIG_SHELL
	case $- in # ((((
	  *v*x* | *x*v* ) as_opts=-vx ;;
	  *v* ) as_opts=-v ;;
	  *x* ) as_opts=-x ;;
	  * ) as_opts= ;;
	esac
	exec "$CONFIG_SHELL" $as_opts "$as_myself" ${1+"$@"}
fi

    if test x$as_have_required = xno; then :
  $as_echo "$0: This script requires a shell more modern than all"
  $as_echo "$0: the shells that I found on your system."
  if test x${ZSH_VERSION+set} = xset ; then
    $as_echo "$0: In particular, zsh $ZSH_VERSION has bugs and should"
    $as_echo "$0: be upgraded to zsh 4.3.4 or later."
  else
    $as_echo "$0: Please tell bug-autoconf@gnu.org about your system,
$0: including any error possibly output before this
$0: message. Then install a modern shell, or manually run
$0: the script under such a shell if you do have one."
  fi
  exit 1
fi
fi
fi
SHELL=${CONFIG_SHELL-/bin/sh}
export SHELL
# Unset more variables known to interfere with behavior of common tools.
CLICOLOR_FORCE= GREP_OPTIONS=
unset CLICOLOR_FORCE GREP_OPTIONS

## --------------------- ##
## M4sh Shell Functions. ##
## --------------------- ##
# as_fn_unset VAR
# ---------------
# Portably unset VAR.
as_fn_unset ()
{
  { eval $1=; unset $1;}
}
as_unset=as_fn_unset

# as_fn_set_status STATUS
# -----------------------
# Set $? to STATUS, without forking.
as_fn_set_status ()
{
  return $1
} # as_fn_set_status

# as_fn_exit STATUS
# -----------------
# Exit the shell with STATUS, even in a "trap 0" or "set -e" context.
as_fn_exit ()
{
  set +e
  as_fn_set_status $1
  exit $1
} # as_fn_exit

# as_fn_mkdir_p
# -------------
# Create "$as_dir" as a directory, including parents if necessary.
as_fn_mkdir_p ()
{

  case $as_dir in #(
  -*) as_dir=./$as_dir;;
  esac
  test -d "$as_dir" || eval $as_mkdir_p || {
    as_dirs=
    while :; do
      case $as_dir in #(
      *\'*) as_qdir=`$as_echo "$as_dir" | sed "s/'/'\\\\\\\\''/g"`;; #'(
      *) as_qdir=$as_dir;;
      esac
      as_dirs="'$as_qdir' $as_dirs"
      as_dir=`$as_dirname -- "$as_dir" ||
$as_expr X"$as_dir" : 'X\(.*[^/]\)//*[^/][^/]*/*$' \| \
	 X"$as_dir" : 'X\(//\)[^/]' \| \
	 X"$as_dir" : 'X\(//\)$' \| \
	 X"$as_dir" : 'X\(/\)' \| . 2>/dev/null ||
$as_echo X"$as_dir" |
    sed '/^X\(.*[^/]\)\/\/*[^/][^/]*\/*$/{
	    s//\1/
	    q
	  }
	  /^X\(\/\/\)[^/].*/{
	    s//\1/
	    q
	  }
	  /^X\(\/\/\)$/{
	    s//\1/
	    q
	  }
	  /^X\(\/\).*/{
	    s//\1/
	    q
	  }
	  s/.*/./; q'`
      test -d "$as_dir" && break
    done
    test -z "$as_dirs" || eval "mkdir $as_dirs"
  } || test -d "$as_dir" || as_fn_error $? "cannot create directory $as_dir"


} # as_fn_mkdir_p
# as_fn_append VAR VALUE
# ----------------------
# Append the text in VALUE to the end of the definition contained in VAR. Take
# advantage of any shell optimizations that allow amortized linear growth over
# repeated appends, instead of the typical quadratic growth present in naive
# implementations.
if (eval "as_var=1; as_var+=2; test x\$as_var = x12") 2>/dev/null; then :
  eval 'as_fn_append ()
  {
    eval $1+=\$2
  }'
else
  as_fn_append ()
  {
    eval $1=\$$1\$2
  }
fi # as_fn_append

# as_fn_arith ARG...
# ------------------
# Perform arithmetic evaluation on the ARGs, and store the result in the
# global $as_val. Take advantage of shells that can avoid forks. The arguments
# must be portable across $(()) and expr.
if (eval "test \$(( 1 + 1 )) = 2") 2>/dev/null; then :
  eval 'as_fn_arith ()
  {
    as_val=$(( $* ))
  }'
else
  as_fn_arith ()
  {
    as_val=`expr "$@" || test $? -eq 1`
  }
fi # as_fn_arith


# as_fn_error STATUS ERROR [LINENO LOG_FD]
# ----------------------------------------
# Output "`basename $0`: error: ERROR" to stderr. If LINENO and LOG_FD are
# provided, also output the error to LOG_FD, referencing LINENO. Then exit the
# script with STATUS, using 1 if that was 0.
as_fn_error ()
{
  as_status=$1; test $as_status -eq 0 && as_status=1
  if test "$4"; then
    as_lineno=${as_lineno-"$3"} as_lineno_stack=as_lineno_stack=$as_lineno_stack
    $as_echo "$as_me:${as_lineno-$LINENO}: error: $2" >&$4
  fi
  $as_echo "$as_me: error: $2" >&2
  as_fn_exit $as_status
} # as_fn_error

if expr a : '\(a\)' >/dev/null 2>&1 &&
   test "X`expr 00001 : '.*\(...\)'`" = X001; then
  as_expr=expr
else
  as_expr=false
fi

if (basename -- /) >/dev/null 2>&1 && test "X`basename -- / 2>&1`" = "X/"; then
  as_basename=basename
else
  as_basename=false
fi

if (as_dir=`dirname -- /` && test "X$as_dir" = X/) >/dev/null 2>&1; then
  as_dirname=dirname
else
  as_dirname=false
fi

as_me=`$as_basename -- "$0" ||
$as_expr X/"$0" : '.*/\([^/][^/]*\)/*$' \| \
	 X"$0" : 'X\(//\)$' \| \
	 X"$0" : 'X\(/\)' \| . 2>/dev/null ||
$as_echo X/"$0" |
    sed '/^.*\/\([^/][^/]*\)\/*$/{
	    s//\1/
	    q
	  }
	  /^X\/\(\/\/\)$/{
	    s//\1/
	    q
	  }
	  /^X\/\(\/\).*/{
	    s//\1/
	    q
	  }
	  s/.*/./; q'`

# Avoid depending upon Character Ranges.
as_cr_letters='abcdefghijklmnopqrstuvwxyz'
as_cr_LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
as_cr_Letters=$as_cr_letters$as_cr_LETTERS
as_cr_digits='0123456789'
as_cr_alnum=$as_cr_Letters$as_cr_digits


  as_lineno_1=$LINENO as_lineno_1a=$LINENO
  as_lineno_2=$LINENO as_lineno_2a=$LINENO
  eval 'test "x$as_lineno_1'$as_run'" != "x$as_lineno_2'$as_run'" &&
  test "x`expr $as_lineno_1'$as_run' + 1`" = "x$as_lineno_2'$as_run'"' || {
  # Blame Lee E. McMahon (1931-1989) for sed's syntax.  :-)
  sed -n '
    p
    /[$]LINENO/=
  ' <$as_myself |
    sed '
      s/[$]LINENO.*/&-/
      t lineno
      b
      :lineno
      N
      :loop
      s/[$]LINENO\([^'$as_cr_alnum'_].*\n\)\(.*\)/\2\1\2/
      t loop
      s/-\n.*//
    ' >$as_me.lineno &&
  chmod +x "$as_me.lineno" ||
    { $as_echo "$as_me: error: cannot create $as_me.lineno; rerun with a POSIX shell" >&2; as_fn_exit 1; }

  # Don't try to exec as it changes $[0], causing all sort of problems
  # (the dirname of $[0] is not the place where we might find the
  # original and so on.  Autoconf is especially sensitive to this).
  . "./$as_me.lineno"
  # Exit status is that of the last command.
  exit
}

ECHO_C= ECHO_N= ECHO_T=
case `echo -n x` in #(((((
-n*)
  case `echo 'xy\c'` in
  *c*) ECHO_T='	';;	# ECHO_T is single tab character.
  xy)  ECHO_C='\c';;
  *)   echo `echo ksh88 bug on AIX 6.1` > /dev/null
       ECHO_T='	';;
  esac;;
*)
  ECHO_N='-n';;
esac

rm -f conf$$ conf$$.exe conf$$.file
if test -d conf$$.dir; then
  rm -f conf$$.dir/conf$$.file
else
  rm -f conf$$.dir
  mkdir conf$$.dir 2>/dev/null
fi
if (echo >conf$$.file) 2>/dev/null; then
  if ln -s conf$$.file conf$$ 2>/dev/null; then
    as_ln_s='ln -s'
    # ... but there are two gotchas:
    # 1) On MSYS, both `ln -s file dir' and `ln file dir' fail.
    # 2) DJGPP < 2.04 has no symlinks; `ln -s' creates a wrapper executable.
    # In both cases, we have to default to `cp -p'.
    ln -s conf$$.file conf$$.dir 2>/dev/null && test ! -f conf$$.exe ||
      as_ln_s='cp -p'
  elif ln conf$$.file conf$$ 2>/dev/null; then
    as_ln_s=ln
  else
    as_ln_s='cp -p'
  fi
else
  as_ln_s='cp -p'
fi
rm -f conf$$ conf$$.exe conf$$.dir/conf$$.file conf$$.file
rmdir conf$$.dir 2>/dev/null

if mkdir -p . 2>/dev/null; then
  as_mkdir_p='mkdir -p "$as_dir"'
else
  test -d ./-p && rmdir ./-p
  as_mkdir_p=false
fi

if test -x / >/dev/null 2>&1; then
  as_test_x='test -x'
else
  if ls -dL / >/dev/null 2>&1; then
    as_ls_L_option=L
  else
    as_ls_L_option=
  fi
  as_test_x='
    eval sh -c '\''
      if test -d "$1"; then
	test -d "$1/.";
      else
	case $1 in #(
	-*)set "./$1";;
	esac;
	case `ls -ld'$as_ls_L_option' "$1" 2>/dev/null` in #((
	???[sx]*):;;*)false;;esac;fi
    '\'' sh
  '
fi
as_executable_p=$as_test_x

# Sed expression to map a string onto a valid CPP name.
as_tr_cpp="eval sed 'y%*$as_cr_letters%P$as_cr_LETTERS%;s%[^_$as_cr_alnum]%_%g'"

# Sed expression to map a string onto a valid variable name.
as_tr_sh="eval sed 'y%*+%pp%;s%[^_$as_cr_alnum]%_%g'"


test -n "$DJDIR" || exec 7<&0 </dev/null
exec 6>&1

# Name of the host.
# hostname on some systems (SVR3.2, old GNU/Linux) returns a bogus exit status,
# so uname gets run too.
ac_hostname=`(hostname || uname -n) 2>/dev/null | sed 1q`

#
# Initializations.
#
ac_default_prefix=/usr/local
ac_clean_files=
ac_config_libobj_dir=.
LIBOBJS=
cross_compiling=no
subdirs=
MFLAGS=
MAKEFLAGS=

# Identity of this package.
PACKAGE_NAME=
PACKAGE_TARNAME=
PACKAGE_VERSION=
PACKAGE_STRING=
PACKAGE_BUGREPORT=
PACKAGE_URL=

ac_unique_file="ninfod.c"
ac_default_prefix=/usr/local/v6
# Factoring default headers for most tests.
ac_includes_default="\
#include <stdio.h>
#ifdef HAVE_SYS_TYPES_H
# include <sys/types.h>
#endif
#ifdef HAVE_SYS_STAT_H
# include <sys/stat.h>
#endif
#ifdef STDC_HEADERS
# include <stdlib.h>
# include <stddef.h>
#else
# ifdef HAVE_STDLIB_H
#  include <stdlib.h>
# endif
#endif
#ifdef HAVE_STRING_H
# if !defined STDC_HEADERS && defined HAVE_MEMORY_H
#  include <memory.h>
# endif
# include <string.h>
#endif
#ifdef HAVE_STRINGS_H
# include <strings.h>
#endif
#ifdef HAVE_INTTYPES_H
# include <inttypes.h>
#endif
#ifdef HAVE_STDINT_H
# include <stdint.h>
#endif
#ifdef HAVE_UNISTD_H
# include <unistd.h>
#endif"

ac_subst_vars='LTLIBOBJS
LIBOBJS
EGREP
GREP
CPP
INSTALL_DIR
INSTALL_LIB
INSTALL_DATA
INSTALL_SCRIPT
INSTALL_PROGRAM
OBJEXT
EXEEXT
ac_ct_CC
CPPFLAGS
LDFLAGS
CFLAGS
CC
target_alias
host_alias
build_alias
LIBS
ECHO_T
ECHO_N
ECHO_C
DEFS
mandir
localedir
libdir
psdir
pdfdir
dvidir
htmldir
infodir
docdir
oldincludedir
includedir
localstatedir
sharedstatedir
sysconfdir
datadir
datarootdir
libexecdir
sbindir
bindir
program_transform_name
prefix
exec_prefix
PACKAGE_URL
PACKAGE_BUGREPORT
PACKAGE_STRING
PACKAGE_VERSION
PACKAGE_TARNAME
PACKAGE_NAME
PATH_SEPARATOR
SHELL'
ac_subst_files=''
ac_user_opts='
enable_option_checking
enable_debug
enable_threads
enable_suptypes
'
      ac_precious_vars='build_alias
host_alias
target_alias
CC
CFLAGS
LDFLAGS
LIBS
CPPFLAGS
CPP'


# Initialize some variables set by options.
ac_init_help=
ac_init_version=false
ac_unrecognized_opts=
ac_unrecognized_sep=
# The variables have the same names as the options, with
# dashes changed to underlines.
cache_file=/dev/null
exec_prefix=NONE
no_create=
no_recursion=
prefix=NONE
program_prefix=NONE
program_suffix=NONE
program_transform_name=s,x,x,
silent=
site=
srcdir=
verbose=
x_includes=NONE
x_libraries=NONE

# Installation directory options.
# These are left unexpanded so users can "make install exec_prefix=/foo"
# and all the variables that are supposed to be based on exec_prefix
# by default will actually change.
# Use braces instead of parens because sh, perl, etc. also accept them.
# (The list follows the same order as the GNU Coding Standards.)
bindir='${exec_prefix}/bin'
sbindir='${exec_prefix}/sbin'
libexecdir='${exec_prefix}/libexec'
datarootdir='${prefix}/share'
datadir='${datarootdir}'
sysconfdir='${prefix}/etc'
sharedstatedir='${prefix}/com'
localstatedir='${prefix}/var'
includedir='${prefix}/include'
oldincludedir='/usr/include'
docdir='${datarootdir}/doc/${PACKAGE}'
infodir='${datarootdir}/info'
htmldir='${docdir}'
dvidir='${docdir}'
pdfdir='${docdir}'
psdir='${docdir}'
libdir='${exec_prefix}/lib'
localedir='${datarootdir}/locale'
mandir='${datarootdir}/man'

ac_prev=
ac_dashdash=
for ac_option
do
  # If the previous option needs an argument, assign it.
  if test -n "$ac_prev"; then
    eval $ac_prev=\$ac_option
    ac_prev=
    continue
  fi

  case $ac_option in
  *=?*) ac_optarg=`expr "X$ac_option" : '[^=]*=\(.*\)'` ;;
  *=)   ac_optarg= ;;
  *)    ac_optarg=yes ;;
  esac

  # Accept the important Cygnus configure options, so we can diagnose typos.

  case $ac_dashdash$ac_option in
  --)
    ac_dashdash=yes ;;

  -bindir | --bindir | --bindi | --bind | --bin | --bi)
    ac_prev=bindir ;;
  -bindir=* | --bindir=* | --bindi=* | --bind=* | --bin=* | --bi=*)
    bindir=$ac_optarg ;;

  -build | --build | --buil | --bui | --bu)
    ac_prev=build_alias ;;
  -build=* | --build=* | --buil=* | --bui=* | --bu=*)
    build_alias=$ac_optarg ;;

  -cache-file | --cache-file | --cache-fil | --cache-fi \
  | --cache-f | --cache- | --cache | --cach | --cac | --ca | --c)
    ac_prev=cache_file ;;
  -cache-file=* | --cache-file=* | --cache-fil=* | --cache-fi=* \
  | --cache-f=* | --cache-=* | --cache=* | --cach=* | --cac=* | --ca=* | --c=*)
    cache_file=$ac_optarg ;;

  --config-cache | -C)
    cache_file=config.cache ;;

  -datadir | --datadir | --datadi | --datad)
    ac_prev=datadir ;;
  -datadir=* | --datadir=* | --datadi=* | --datad=*)
    datadir=$ac_optarg ;;

  -datarootdir | --datarootdir | --datarootdi | --datarootd | --dataroot \
  | --dataroo | --dataro | --datar)
    ac_prev=datarootdir ;;
  -datarootdir=* | --datarootdir=* | --datarootdi=* | --datarootd=* \
  | --dataroot=* | --dataroo=* | --dataro=* | --datar=*)
    datarootdir=$ac_optarg ;;

  -disable-* | --disable-*)
    ac_useropt=`expr "x$ac_option" : 'x-*disable-\(.*\)'`
    # Reject names that are not valid shell variable names.
    expr "x$ac_useropt" : ".*[^-+._$as_cr_alnum]" >/dev/null &&
      as_fn_error $? "invalid feature name: $ac_useropt"
    ac_useropt_orig=$ac_useropt
    ac_useropt=`$as_echo "$ac_useropt" | sed 's/[-+.]/_/g'`
    case $ac_user_opts in
      *"
"enable_$ac_useropt"
"*) ;;
      *) ac_unrecognized_opts="$ac_unrecognized_opts$ac_unrecognized_sep--disable-$ac_useropt_orig"
	 ac_unrecognized_sep=', ';;
    esac
    eval enable_$ac_useropt=no ;;

  -docdir | --docdir | --docdi | --doc | --do)
    ac_prev=docdir ;;
  -docdir=* | --docdir=* | --docdi=* | --doc=* | --do=*)
    docdir=$ac_optarg ;;

  -dvidir | --dvidir | --dvidi | --dvid | --dvi | --dv)
    ac_prev=dvidir ;;
  -dvidir=* | --dvidir=* | --dvidi=* | --dvid=* | --dvi=* | --dv=*)
    dvidir=$ac_optarg ;;

  -enable-* | --enable-*)
    ac_useropt=`expr "x$ac_option" : 'x-*enable-\([^=]*\)'`
    # Reject names that are not valid shell variable names.
    expr "x$ac_useropt" : ".*[^-+._$as_cr_alnum]" >/dev/null &&
      as_fn_error $? "invalid feature name: $ac_useropt"
    ac_useropt_orig=$ac_useropt
    ac_useropt=`$as_echo "$ac_useropt" | sed 's/[-+.]/_/g'`
    case $ac_user_opts in
      *"
"enable_$ac_useropt"
"*) ;;
      *) ac_unrecognized_opts="$ac_unrecognized_opts$ac_unrecognized_sep--enable-$ac_useropt_orig"
	 ac_unrecognized_sep=', ';;
    esac
    eval enable_$ac_useropt=\$ac_optarg ;;

  -exec-prefix | --exec_prefix | --exec-prefix | --exec-prefi \
  | --exec-pref | --exec-pre | --exec-pr | --exec-p | --exec- \
  | --exec | --exe | --ex)
    ac_prev=exec_prefix ;;
  -exec-prefix=* | --exec_prefix=* | --exec-prefix=* | --exec-prefi=* \
  | --exec-pref=* | --exec-pre=* | --exec-pr=* | --exec-p=* | --exec-=* \
  | --exec=* | --exe=* | --ex=*)
    exec_prefix=$ac_optarg ;;

  -gas | --gas | --ga | --g)
    # Obsolete; use --with-gas.
    with_gas=yes ;;

  -help | --help | --hel | --he | -h)
    ac_init_help=long ;;
  -help=r* | --help=r* | --hel=r* | --he=r* | -hr*)
    ac_init_help=recursive ;;
  -help=s* | --help=s* | --hel=s* | --he=s* | -hs*)
    ac_init_help=short ;;

  -host | --host | --hos | --ho)
    ac_prev=host_alias ;;
  -host=* | --host=* | --hos=* | --ho=*)
    host_alias=$ac_optarg ;;

  -htmldir | --htmldir | --htmldi | --htmld | --html | --htm | --ht)
    ac_prev=htmldir ;;
  -htmldir=* | --htmldir=* | --htmldi=* | --htmld=* | --html=* | --htm=* \
  | --ht=*)
    htmldir=$ac_optarg ;;

  -includedir | --includedir | --includedi | --included | --include \
  | --includ | --inclu | --incl | --inc)
    ac_prev=includedir ;;
  -includedir=* | --includedir=* | --includedi=* | --included=* | --include=* \
  | --includ=* | --inclu=* | --incl=* | --inc=*)
    includedir=$ac_optarg ;;

  -infodir | --infodir | --infodi | --infod | --info | --inf)
    ac_prev=infodir ;;
  -infodir=* | --infodir=* | --infodi=* | --infod=* | --info=* | --inf=*)
    infodir=$ac_optarg ;;

  -libdir | --libdir | --libdi | --libd)
    ac_prev=libdir ;;
  -libdir=* | --libdir=* | --libdi=* | --libd=*)
    libdir=$ac_optarg ;;

  -libexecdir | --libexecdir | --libexecdi | --libexecd | --libexec \
  | --libexe | --libex | --libe)
    ac_prev=libexecdir ;;
  -libexecdir=* | --libexecdir=* | --libexecdi=* | --libexecd=* | --libexec=* \
  | --libexe=* | --libex=* | --libe=*)
    libexecdir=$ac_optarg ;;

  -localedir | --localedir | --localedi | --localed | --locale)
    ac_prev=localedir ;;
  -localedir=* | --localedir=* | --localedi=* | --localed=* | --locale=*)
    localedir=$ac_optarg ;;

  -localstatedir | --localstatedir | --localstatedi | --localstated \
  | --localstate | --localstat | --localsta | --localst | --locals)
    ac_prev=localstatedir ;;
  -localstatedir=* | --localstatedir=* | --localstatedi=* | --localstated=* \
  | --localstate=* | --localstat=* | --localsta=* | --localst=* | --locals=*)
    localstatedir=$ac_optarg ;;

  -mandir | --mandir | --mandi | --mand | --man | --ma | --m)
    ac_prev=mandir ;;
  -mandir=* | --mandir=* | --mandi=* | --mand=* | --man=* | --ma=* | --m=*)
    mandir=$ac_optarg ;;

  -nfp | --nfp | --nf)
    # Obsolete; use --without-fp.
    with_fp=no ;;

  -no-create | --no-create | --no-creat | --no-crea | --no-cre \
  | --no-cr | --no-c | -n)
    no_create=yes ;;

  -no-recursion | --no-recursion | --no-recursio | --no-recursi \
  | --no-recurs | --no-recur | --no-recu | --no-rec | --no-re | --no-r)
    no_recursion=yes ;;

  -oldincludedir | --oldincludedir | --oldincludedi | --oldincluded \
  | --oldinclude | --oldinclud | --oldinclu | --oldincl | --oldinc \
  | --oldin | --oldi | --old | --ol | --o)
    ac_prev=oldincludedir ;;
  -oldincludedir=* | --oldincludedir=* | --oldincludedi=* | --oldincluded=* \
  | --oldinclude=* | --oldinclud=* | --oldinclu=* | --oldincl=* | --oldinc=* \
  | --oldin=* | --oldi=* | --old=* | --ol=* | --o=*)
    oldincludedir=$ac_optarg ;;

  -prefix | --prefix | --prefi | --pref | --pre | --pr | --p)
    ac_prev=prefix ;;
  -prefix=* | --prefix=* | --prefi=* | --pref=* | --pre=* | --pr=* | --p=*)
    prefix=$ac_optarg ;;

  -program-prefix | --program-prefix | --program-prefi | --program-pref \
  | --program-pre | --program-pr | --program-p)
    ac_prev=program_prefix ;;
  -program-prefix=* | --program-prefix=* | --program-prefi=* \
  | --program-pref=* | --program-pre=* | --program-pr=* | --program-p=*)
    program_prefix=$ac_optarg ;;

  -program-suffix | --program-suffix | --program-suffi | --program-suff \
  | --program-suf | --program-su | --program-s)
    ac_prev=program_suffix ;;
  -program-suffix=* | --program-suffix=* | --program-suffi=* \
  | --program-suff=* | --program-suf=* | --program-su=* | --program-s=*)
    program_suffix=$ac_optarg ;;

  -program-transform-name | --program-transform-name \
  | --program-transform-nam | --program-transform-na \
  | --program-transform-n | --program-transform- \
  | --program-transform | --program-transfor \
  | --program-transfo | --program-transf \
  | --program-trans | --program-tran \
  | --progr-tra | --program-tr | --program-t)
    ac_prev=program_transform_name ;;
  -program-transform-name=* | --program-transform-name=* \
  | --program-transform-nam=* | --program-transform-na=* \
  | --program-transform-n=* | --program-transform-=* \
  | --program-transform=* | --program-transfor=* \
  | --program-transfo=* | --program-transf=* \
  | --program-trans=* | --program-tran=* \
  | --progr-tra=* | --program-tr=* | --program-t=*)
    program_transform_name=$ac_optarg ;;

  -pdfdir | --pdfdir | --pdfdi | --pdfd | --pdf | --pd)
    ac_prev=pdfdir ;;
  -pdfdir=* | --pdfdir=* | --pdfdi=* | --pdfd=* | --pdf=* | --pd=*)
    pdfdir=$ac_optarg ;;

  -psdir | --psdir | --psdi | --psd | --ps)
    ac_prev=psdir ;;
  -psdir=* | --psdir=* | --psdi=* | --psd=* | --ps=*)
    psdir=$ac_optarg ;;

  -q | -quiet | --quiet | --quie | --qui | --qu | --q \
  | -silent | --silent | --silen | --sile | --sil)
    silent=yes ;;

  -sbindir | --sbindir | --sbindi | --sbind | --sbin | --sbi | --sb)
    ac_prev=sbindir ;;
  -sbindir=* | --sbindir=* | --sbindi=* | --sbind=* | --sbin=* \
  | --sbi=* | --sb=*)
    sbindir=$ac_optarg ;;

  -sharedstatedir | --sharedstatedir | --sharedstatedi \
  | --sharedstated | --sharedstate | --sharedstat | --sharedsta \
  | --sharedst | --shareds | --shared | --share | --shar \
  | --sha | --sh)
    ac_prev=sharedstatedir ;;
  -sharedstatedir=* | --sharedstatedir=* | --sharedstatedi=* \
  | --sharedstated=* | --sharedstate=* | --sharedstat=* | --sharedsta=* \
  | --sharedst=* | --shareds=* | --shared=* | --share=* | --shar=* \
  | --sha=* | --sh=*)
    sharedstatedir=$ac_optarg ;;

  -site | --site | --sit)
    ac_prev=site ;;
  -site=* | --site=* | --sit=*)
    site=$ac_optarg ;;

  -srcdir | --srcdir | --srcdi | --srcd | --src | --sr)
    ac_prev=srcdir ;;
  -srcdir=* | --srcdir=* | --srcdi=* | --srcd=* | --src=* | --sr=*)
    srcdir=$ac_optarg ;;

  -sysconfdir | --sysconfdir | --sysconfdi | --sysconfd | --sysconf \
  | --syscon | --sysco | --sysc | --sys | --sy)
    ac_prev=sysconfdir ;;
  -sysconfdir=* | --sysconfdir=* | --sysconfdi=* | --sysconfd=* | --sysconf=* \
  | --syscon=* | --sysco=* | --sysc=* | --sys=* | --sy=*)
    sysconfdir=$ac_optarg ;;

  -target | --target | --targe | --targ | --tar | --ta | --t)
    ac_prev=target_alias ;;
  -target=* | --target=* | --targe=* | --targ=* | --tar=* | --ta=* | --t=*)
    target_alias=$ac_optarg ;;

  -v | -verbose | --verbose | --verbos | --verbo | --verb)
    verbose=yes ;;

  -version | --version | --versio | --versi | --vers | -V)
    ac_init_version=: ;;

  -with-* | --with-*)
    ac_useropt=`expr "x$ac_option" : 'x-*with-\([^=]*\)'`
    # Reject names that are not valid shell variable names.
    expr "x$ac_useropt" : ".*[^-+._$as_cr_alnum]" >/dev/null &&
      as_fn_error $? "invalid package name: $ac_useropt"
    ac_useropt_orig=$ac_useropt
    ac_useropt=`$as_echo "$ac_useropt" | sed 's/[-+.]/_/g'`
    case $ac_user_opts in
      *"
"with_$ac_useropt"
"*) ;;
      *) ac_unrecognized_opts="$ac_unrecognized_opts$ac_unrecognized_sep--with-$ac_useropt_orig"
	 ac_unrecognized_sep=', ';;
    esac
    eval with_$ac_useropt=\$ac_optarg ;;

  -without-* | --without-*)
    ac_useropt=`expr "x$ac_option" : 'x-*without-\(.*\)'`
    # Reject names that are not valid shell variable names.
    expr "x$ac_useropt" : ".*[^-+._$as_cr_alnum]" >/dev/null &&
      as_fn_error $? "invalid package name: $ac_useropt"
    ac_useropt_orig=$ac_useropt
    ac_useropt=`$as_echo "$ac_useropt" | sed 's/[-+.]/_/g'`
    case $ac_user_opts in
      *"
"with_$ac_useropt"
"*) ;;
      *) ac_unrecognized_opts="$ac_unrecognized_opts$ac_unrecognized_sep--without-$ac_useropt_orig"
	 ac_unrecognized_sep=', ';;
    esac
    eval with_$ac_useropt=no ;;

  --x)
    # Obsolete; use --with-x.
    with_x=yes ;;

  -x-includes | --x-includes | --x-include | --x-includ | --x-inclu \
  | --x-incl | --x-inc | --x-in | --x-i)
    ac_prev=x_includes ;;
  -x-includes=* | --x-includes=* | --x-include=* | --x-includ=* | --x-inclu=* \
  | --x-incl=* | --x-inc=* | --x-in=* | --x-i=*)
    x_includes=$ac_optarg ;;

  -x-libraries | --x-libraries | --x-librarie | --x-librari \
  | --x-librar | --x-libra | --x-libr | --x-lib | --x-li | --x-l)
    ac_prev=x_libraries ;;
  -x-libraries=* | --x-libraries=* | --x-librarie=* | --x-librari=* \
  | --x-librar=* | --x-libra=* | --x-libr=* | --x-lib=* | --x-li=* | --x-l=*)
    x_libraries=$ac_optarg ;;

  -*) as_fn_error $? "unrecognized option: \`$ac_option'
Try \`$0 --help' for more information"
    ;;

  *=*)
    ac_envvar=`expr "x$ac_option" : 'x\([^=]*\)='`
    # Reject names that are not valid shell variable names.
    case $ac_envvar in #(
      '' | [0-9]* | *[!_$as_cr_alnum]* )
      as_fn_error $? "invalid variable name: \`$ac_envvar'" ;;
    esac
    eval $ac_envvar=\$ac_optarg
    export $ac_envvar ;;

  *)
    # FIXME: should be removed in autoconf 3.0.
    $as_echo "$as_me: WARNING: you should use --build, --host, --target" >&2
    expr "x$ac_option" : ".*[^-._$as_cr_alnum]" >/dev/null &&
      $as_echo "$as_me: WARNING: invalid host type: $ac_option" >&2
    : "${build_alias=$ac_option} ${host_alias=$ac_option} ${target_alias=$ac_option}"
    ;;

  esac
done

if test -n "$ac_prev"; then
  ac_option=--`echo $ac_prev | sed 's/_/-/g'`
  as_fn_error $? "missing argument to $ac_option"
fi

if test -n "$ac_unrecognized_opts"; then
  case $enable_option_checking in
    no) ;;
    fatal) as_fn_error $? "unrecognized options: $ac_unrecognized_opts" ;;
    *)     $as_echo "$as_me: WARNING: unrecognized options: $ac_unrecognized_opts" >&2 ;;
  esac
fi

# Check all directory arguments for consistency.
for ac_var in	exec_prefix prefix bindir sbindir libexecdir datarootdir \
		datadir sysconfdir sharedstatedir localstatedir includedir \
		oldincludedir docdir infodir htmldir dvidir pdfdir psdir \
		libdir localedir mandir
do
  eval ac_val=\$$ac_var
  # Remove trailing slashes.
  case $ac_val in
    */ )
      ac_val=`expr "X$ac_val" : 'X\(.*[^/]\)' \| "X$ac_val" : 'X\(.*\)'`
      eval $ac_var=\$ac_val;;
  esac
  # Be sure to have absolute directory names.
  case $ac_val in
    [\\/$]* | ?:[\\/]* )  continue;;
    NONE | '' ) case $ac_var in *prefix ) continue;; esac;;
  esac
  as_fn_error $? "expected an absolute directory name for --$ac_var: $ac_val"
done

# There might be people who depend on the old broken behavior: `$host'
# used to hold the argument of --host etc.
# FIXME: To remove some day.
build=$build_alias
host=$host_alias
target=$target_alias

# FIXME: To remove some day.
if test "x$host_alias" != x; then
  if test "x$build_alias" = x; then
    cross_compiling=maybe
    $as_echo "$as_me: WARNING: if you wanted to set the --build type, don't use --host.
    If a cross compiler is detected then cross compile mode will be used" >&2
  elif test "x$build_alias" != "x$host_alias"; then
    cross_compiling=yes
  fi
fi

ac_tool_prefix=
test -n "$host_alias" && ac_tool_prefix=$host_alias-

test "$silent" = yes && exec 6>/dev/null


ac_pwd=`pwd` && test -n "$ac_pwd" &&
ac_ls_di=`ls -di .` &&
ac_pwd_ls_di=`cd "$ac_pwd" && ls -di .` ||
  as_fn_error $? "working directory cannot be determined"
test "X$ac_ls_di" = "X$ac_pwd_ls_di" ||
  as_fn_error $? "pwd does not report name of working directory"


# Find the source files, if location was not specified.
if test -z "$srcdir"; then
  ac_srcdir_defaulted=yes
  # Try the directory containing this script, then the parent directory.
  ac_confdir=`$as_dirname -- "$as_myself" ||
$as_expr X"$as_myself" : 'X\(.*[^/]\)//*[^/][^/]*/*$' \| \
	 X"$as_myself" : 'X\(//\)[^/]' \| \
	 X"$as_myself" : 'X\(//\)$' \| \
	 X"$as_myself" : 'X\(/\)' \| . 2>/dev/null ||
$as_echo X"$as_myself" |
    sed '/^X\(.*[^/]\)\/\/*[^/][^/]*\/*$/{
	    s//\1/
	    q
	  }
	  /^X\(\/\/\)[^/].*/{
	    s//\1/
	    q
	  }
	  /^X\(\/\/\)$/{
	    s//\1/
	    q
	  }
	  /^X\(\/\).*/{
	    s//\1/
	    q
	  }
	  s/.*/./; q'`
  srcdir=$ac_confdir
  if test ! -r "$srcdir/$ac_unique_file"; then
    srcdir=..
  fi
else
  ac_srcdir_defaulted=no
fi
if test ! -r "$srcdir/$ac_unique_file"; then
  test "$ac_srcdir_defaulted" = yes && srcdir="$ac_confdir or .."
  as_fn_error $? "cannot find sources ($ac_unique_file) in $srcdir"
fi
ac_msg="sources are in $srcdir, but \`cd $srcdir' does not work"
ac_abs_confdir=`(
	cd "$srcdir" && test -r "./$ac_unique_file" || as_fn_error $? "$ac_msg"
	pwd)`
# When building in place, set srcdir=.
if test "$ac_abs_confdir" = "$ac_pwd"; then
  srcdir=.
fi
# Remove unnecessary trailing slashes from srcdir.
# Double slashes in file names in object file debugging info
# mess up M-x gdb in Emacs.
case $srcdir in
*/) srcdir=`expr "X$srcdir" : 'X\(.*[^/]\)' \| "X$srcdir" : 'X\(.*\)'`;;
esac
for ac_var in $ac_precious_vars; do
  eval ac_env_${ac_var}_set=\${${ac_var}+set}
  eval ac_env_${ac_var}_value=\$${ac_var}
  eval ac_cv_env_${ac_var}_set=\${${ac_var}+set}
  eval ac_cv_env_${ac_var}_value=\$${ac_var}
done

#
# Report the --help message.
#
if test "$ac_init_help" = "long"; then
  # Omit some internal or obsolete options to make the list less imposing.
  # This message is too long to be a string in the A/UX 3.1 sh.
  cat <<_ACEOF
\`configure' configures this package to adapt to many kinds of systems.

Usage: $0 [OPTION]... [VAR=VALUE]...

To assign environment variables (e.g., CC, CFLAGS...), specify them as
VAR=VALUE.  See below for descriptions of some of the useful variables.

Defaults for the options are specified in brackets.

Configuration:
  -h, --help              display this help and exit
      --help=short        display options specific to this package
      --help=recursive    display the short help of all the included packages
  -V, --version           display version information and exit
  -q, --quiet, --silent   do not print \`checking ...' messages
      --cache-file=FILE   cache test results in FILE [disabled]
  -C, --config-cache      alias for \`--cache-file=config.cache'
  -n, --no-create         do not create output files
      --srcdir=DIR        find the sources in DIR [configure dir or \`..']

Installation directories:
  --prefix=PREFIX         install architecture-independent files in PREFIX
                          [$ac_default_prefix]
  --exec-prefix=EPREFIX   install architecture-dependent files in EPREFIX
                          [PREFIX]

By default, \`make install' will install all the files in
\`$ac_default_prefix/bin', \`$ac_default_prefix/lib' etc.  You can specify
an installation prefix other than \`$ac_default_prefix' using \`--prefix',
for instance \`--prefix=\$HOME'.

For better control, use the options below.

Fine tuning of the installation directories:
  --bindir=DIR            user executables [EPREFIX/bin]
  --sbindir=DIR           system admin executables [EPREFIX/sbin]
  --libexecdir=DIR        program executables [EPREFIX/libexec]
  --sysconfdir=DIR        read-only single-machine data [PREFIX/etc]
  --sharedstatedir=DIR    modifiable architecture-independent data [PREFIX/com]
  --localstatedir=DIR     modifiable single-machine data [PREFIX/var]
  --libdir=DIR            object code libraries [EPREFIX/lib]
  --includedir=DIR        C header files [PREFIX/include]
  --oldincludedir=DIR     C header files for non-gcc [/usr/include]
  --datarootdir=DIR       read-only arch.-independent data root [PREFIX/share]
  --datadir=DIR           read-only architecture-independent data [DATAROOTDIR]
  --infodir=DIR           info documentation [DATAROOTDIR/info]
  --localedir=DIR         locale-dependent data [DATAROOTDIR/locale]
  --mandir=DIR            man documentation [DATAROOTDIR/man]
  --docdir=DIR            documentation root [DATAROOTDIR/doc/PACKAGE]
  --htmldir=DIR           html documentation [DOCDIR]
  --dvidir=DIR            dvi documentation [DOCDIR]
  --pdfdir=DIR            pdf documentation [DOCDIR]
  --psdir=DIR             ps documentation [DOCDIR]
_ACEOF

  cat <<\_ACEOF
_ACEOF
fi

if test -n "$ac_init_help"; then

  cat <<\_ACEOF

Optional Features:
  --disable-option-checking  ignore unrecognized --enable/--with options
  --disable-FEATURE       do not include FEATURE (same as --enable-FEATURE=no)
  --enable-FEATURE[=ARG]  include FEATURE [ARG=yes]
  --enable-debug          Enable debugging
  --disable-threads       Disable threads (and random delay)
  --enable-suptypes       Enable suptypes qtype (deprecated)
  --enable-ttl            Enable ttl support for qtypes (deprecated)

Some influential environment variables:
  CC          C compiler command
  CFLAGS      C compiler flags
  LDFLAGS     linker flags, e.g. -L<lib dir> if you have libraries in a
              nonstandard directory <lib dir>
  LIBS        libraries to pass to the linker, e.g. -l<library>
  CPPFLAGS    (Objective) C/C++ preprocessor flags, e.g. -I<include dir> if
              you have headers in a nonstandard directory <include dir>
  CPP         C preprocessor

Use these variables to override the choices made by `configure' or to help
it to find libraries and programs with nonstandard names/locations.

Report bugs to the package provider.
_ACEOF
ac_status=$?
fi

if test "$ac_init_help" = "recursive"; then
  # If there are subdirs, report their specific --help.
  for ac_dir in : $ac_subdirs_all; do test "x$ac_dir" = x: && continue
    test -d "$ac_dir" ||
      { cd "$srcdir" && ac_pwd=`pwd` && srcdir=. && test -d "$ac_dir"; } ||
      continue
    ac_builddir=.

case "$ac_dir" in
.) ac_dir_suffix= ac_top_builddir_sub=. ac_top_build_prefix= ;;
*)
  ac_dir_suffix=/`$as_echo "$ac_dir" | sed 's|^\.[\\/]||'`
  # A ".." for each directory in $ac_dir_suffix.
  ac_top_builddir_sub=`$as_echo "$ac_dir_suffix" | sed 's|/[^\\/]*|/..|g;s|/||'`
  case $ac_top_builddir_sub in
  "") ac_top_builddir_sub=. ac_top_build_prefix= ;;
  *)  ac_top_build_prefix=$ac_top_builddir_sub/ ;;
  esac ;;
esac
ac_abs_top_builddir=$ac_pwd
ac_abs_builddir=$ac_pwd$ac_dir_suffix
# for backward compatibility:
ac_top_builddir=$ac_top_build_prefix

case $srcdir in
  .)  # We are building in place.
    ac_srcdir=.
    ac_top_srcdir=$ac_top_builddir_sub
    ac_abs_top_srcdir=$ac_pwd ;;
  [\\/]* | ?:[\\/]* )  # Absolute name.
    ac_srcdir=$srcdir$ac_dir_suffix;
    ac_top_srcdir=$srcdir
    ac_abs_top_srcdir=$srcdir ;;
  *) # Relative name.
    ac_srcdir=$ac_top_build_prefix$srcdir$ac_dir_suffix
    ac_top_srcdir=$ac_top_build_prefix$srcdir
    ac_abs_top_srcdir=$ac_pwd/$srcdir ;;
esac
ac_abs_srcdir=$ac_abs_top_srcdir$ac_dir_suffix

    cd "$ac_dir" || { ac_status=$?; continue; }
    # Check for guested configure.
    if test -f "$ac_srcdir/configure.gnu"; then
      echo &&
      $SHELL "$ac_srcdir/configure.gnu" --help=recursive
    elif test -f "$ac_srcdir/configure"; then
      echo &&
      $SHELL "$ac_srcdir/configure" --help=recursive
    else
      $as_echo "$as_me: WARNING: no configuration information is in $ac_dir" >&2
    fi || ac_status=$?
    cd "$ac_pwd" || { ac_status=$?; break; }
  done
fi

test -n "$ac_init_help" && exit $ac_status
if $ac_init_version; then
  cat <<\_ACEOF
configure
generated by GNU Autoconf 2.68

Copyright (C) 2010 Free Software Foundation, Inc.
This configure script is free software; the Free Software Foundation
gives unlimited permission to copy, distribute and modify it.

Copyright (C)2002 USAGI/WIDE Project.  All Rights Reserved.
_ACEOF
  exit
fi

## ------------------------ ##
## Autoconf initialization. ##
## ------------------------ ##

# ac_fn_c_try_compile LINENO
# --------------------------
# Try to compile conftest.$ac_ext, and return whether this succeeded.
ac_fn_c_try_compile ()
{
  as_lineno=${as_lineno-"$1"} as_lineno_stack=as_lineno_stack=$as_lineno_stack
  rm -f conftest.$ac_objext
  if { { ac_try="$ac_compile"
case "(($ac_try" in
  *\"* | *\`* | *\\*) ac_try_echo=\$ac_try;;
  *) ac_try_echo=$ac_try;;
esac
eval ac_try_echo="\"\$as_me:${as_lineno-$LINENO}: $ac_try_echo\""
$as_echo "$ac_try_echo"; } >&5
  (eval "$ac_compile") 2>conftest.err
  ac_status=$?
  if test -s conftest.err; then
    grep -v '^ *+' conftest.err >conftest.er1
    cat conftest.er1 >&5
    mv -f conftest.er1 conftest.err
  fi
  $as_echo "$as_me:${as_lineno-$LINENO}: \$? = $ac_status" >&5
  test $ac_status = 0; } && {
	 test -z "$ac_c_werror_flag" ||
	 test ! -s conftest.err
       } && test -s conftest.$ac_objext; then :
  ac_retval=0
else
  $as_echo "$as_me: failed program was:" >&5
sed 's/^/| /' conftest.$ac_ext >&5

	ac_retval=1
fi
  eval $as_lineno_stack; ${as_lineno_stack:+:} unset as_lineno
  as_fn_set_status $ac_retval

} # ac_fn_c_try_compile

# ac_fn_c_try_cpp LINENO
# ----------------------
# Try to preprocess conftest.$ac_ext, and return whether this succeeded.
ac_fn_c_try_cpp ()
{
  as_lineno=${as_lineno-"$1"} as_lineno_stack=as_lineno_stack=$as_lineno_stack
  if { { ac_try="$ac_cpp conftest.$ac_ext"
case "(($ac_try" in
  *\"* | *\`* | *\\*) ac_try_echo=\$ac_try;;
  *) ac_try_echo=$ac_try;;
esac
eval ac_try_echo="\"\$as_me:${as_lineno-$LINENO}: $ac_try_echo\""
$as_echo "$ac_try_echo"; } >&5
  (eval "$ac_cpp conftest.$ac_ext") 2>conftest.err
  ac_status=$?
  if test -s conftest.err; then
    grep -v '^ *+' conftest.err >conftest.er1
    cat conftest.er1 >&5
    mv -f conftest.er1 conftest.err
  fi
  $as_echo "$as_me:${as_lineno-$LINENO}: \$? = $ac_status" >&5
  test $ac_status = 0; } > conftest.i && {
	 test -z "$ac_c_preproc_warn_flag$ac_c_werror_flag" ||
	 test ! -s conftest.err
       }; then :
  ac_retval=0
else
  $as_echo "$as_me: failed program was:" >&5
sed 's/^/| /' conftest.$ac_ext >&5

    ac_retval=1
fi
  eval $as_lineno_stack; ${as_lineno_stack:+:} unset as_lineno
  as_fn_set_status $ac_retval

} # ac_fn_c_try_cpp

# ac_fn_c_try_run LINENO
# ----------------------
# Try to link conftest.$ac_ext, and return whether this succeeded. Assumes
# that executables *can* be run.
ac_fn_c_try_run ()
{
  as_lineno=${as_lineno-"$1"} as_lineno_stack=as_lineno_stack=$as_lineno_stack
  if { { ac_try="$ac_link"
case "(($ac_try" in
  *\"* | *\`* | *\\*) ac_try_echo=\$ac_try;;
  *) ac_try_echo=$ac_try;;
esac
eval ac_try_echo="\"\$as_me:${as_lineno-$LINENO}: $ac_try_echo\""
$as_echo "$ac_try_echo"; } >&5
  (eval "$ac_link") 2>&5
  ac_status=$?
  $as_echo "$as_me:${as_lineno-$LINENO}: \$? = $ac_status" >&5
  test $ac_status = 0; } && { ac_try='./conftest$ac_exeext'
  { { case "(($ac_try" in
  *\"* | *\`* | *\\*) ac_try_echo=\$ac_try;;
  *) ac_try_echo=$ac_try;;
esac
eval ac_try_echo="\"\$as_me:${as_lineno-$LINENO}: $ac_try_echo\""
$as_echo "$ac_try_echo"; } >&5
  (eval "$ac_try") 2>&5
  ac_status=$?
  $as_echo "$as_me:${as_lineno-$LINENO}: \$? = $ac_status" >&5
  test $ac_status = 0; }; }; then :
  ac_retval=0
else
  $as_echo "$as_me: program exited with status $ac_status" >&5
       $as_echo "$as_me: failed program was:" >&5
sed 's/^/| /' conftest.$ac_ext >&5

       ac_retval=$ac_status
fi
  rm -rf conftest.dSYM conftest_ipa8_conftest.oo
  eval $as_lineno_stack; ${as_lineno_stack:+:} unset as_lineno
  as_fn_set_status $ac_retval

} # ac_fn_c_try_run

# ac_fn_c_check_header_mongrel LINENO HEADER VAR INCLUDES
# -------------------------------------------------------
# Tests whether HEADER exists, giving a warning if it cannot be compiled using
# the include files in INCLUDES and setting the cache variable VAR
# accordingly.
ac_fn_c_check_header_mongrel ()
{
  as_lineno=${as_lineno-"$1"} as_lineno_stack=as_lineno_stack=$as_lineno_stack
  if eval \${$3+:} false; then :
  { $as_echo "$as_me:${as_lineno-$LINENO}: checking for $2" >&5
$as_echo_n "checking for $2... " >&6; }
if eval \${$3+:} false; then :
  $as_echo_n "(cached) " >&6
fi
eval ac_res=\$$3
	       { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_res" >&5
$as_echo "$ac_res" >&6; }
else
  # Is the header compilable?
{ $as_echo "$as_me:${as_lineno-$LINENO}: checking $2 usability" >&5
$as_echo_n "checking $2 usability... " >&6; }
cat confdefs.h - <<_ACEOF >conftest.$ac_ext
/* end confdefs.h.  */
$4
#include <$2>
_ACEOF
if ac_fn_c_try_compile "$LINENO"; then :
  ac_header_compiler=yes
else
  ac_header_compiler=no
fi
rm -f core conftest.err conftest.$ac_objext conftest.$ac_ext
{ $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_header_compiler" >&5
$as_echo "$ac_header_compiler" >&6; }

# Is the header present?
{ $as_echo "$as_me:${as_lineno-$LINENO}: checking $2 presence" >&5
$as_echo_n "checking $2 presence... " >&6; }
cat confdefs.h - <<_ACEOF >conftest.$ac_ext
/* end confdefs.h.  */
#include <$2>
_ACEOF
if ac_fn_c_try_cpp "$LINENO"; then :
  ac_header_preproc=yes
else
  ac_header_preproc=no
fi
rm -f conftest.err conftest.i conftest.$ac_ext
{ $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_header_preproc" >&5
$as_echo "$ac_header_preproc" >&6; }

# So?  What about this header?
case $ac_header_compiler:$ac_header_preproc:$ac_c_preproc_warn_flag in #((
  yes:no: )
    { $as_echo "$as_me:${as_lineno-$LINENO}: WARNING: $2: accepted by the compiler, rejected by the preprocessor!" >&5
$as_echo "$as_me: WARNING: $2: accepted by the compiler, rejected by the preprocessor!" >&2;}
    { $as_echo "$as_me:${as_lineno-$LINENO}: WARNING: $2: proceeding with the compiler's result" >&5
$as_echo "$as_me: WARNING: $2: proceeding with the compiler's result" >&2;}
    ;;
  no:yes:* )
    { $as_echo "$as_me:${as_lineno-$LINENO}: WARNING: $2: present but cannot be compiled" >&5
$as_echo "$as_me: WARNING: $2: present but cannot be compiled" >&2;}
    { $as_echo "$as_me:${as_lineno-$LINENO}: WARNING: $2:     check for missing prerequisite headers?" >&5
$as_echo "$as_me: WARNING: $2:     check for missing prerequisite headers?" >&2;}
    { $as_echo "$as_me:${as_lineno-$LINENO}: WARNING: $2: see the Autoconf documentation" >&5
$as_echo "$as_me: WARNING: $2: see the Autoconf documentation" >&2;}
    { $as_echo "$as_me:${as_lineno-$LINENO}: WARNING: $2:     section \"Present But Cannot Be Compiled\"" >&5
$as_echo "$as_me: WARNING: $2:     section \"Present But Cannot Be Compiled\"" >&2;}
    { $as_echo "$as_me:${as_lineno-$LINENO}: WARNING: $2: proceeding with the compiler's result" >&5
$as_echo "$as_me: WARNING: $2: proceeding with the compiler's result" >&2;}
    ;;
esac
  { $as_echo "$as_me:${as_lineno-$LINENO}: checking for $2" >&5
$as_echo_n "checking for $2... " >&6; }
if eval \${$3+:} false; then :
  $as_echo_n "(cached) " >&6
else
  eval "$3=\$ac_header_compiler"
fi
eval ac_res=\$$3
	       { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_res" >&5
$as_echo "$ac_res" >&6; }
fi
  eval $as_lineno_stack; ${as_lineno_stack:+:} unset as_lineno

} # ac_fn_c_check_header_mongrel

# ac_fn_c_check_header_compile LINENO HEADER VAR INCLUDES
# -------------------------------------------------------
# Tests whether HEADER exists and can be compiled using the include files in
# INCLUDES, setting the cache variable VAR accordingly.
ac_fn_c_check_header_compile ()
{
  as_lineno=${as_lineno-"$1"} as_lineno_stack=as_lineno_stack=$as_lineno_stack
  { $as_echo "$as_me:${as_lineno-$LINENO}: checking for $2" >&5
$as_echo_n "checking for $2... " >&6; }
if eval \${$3+:} false; then :
  $as_echo_n "(cached) " >&6
else
  cat confdefs.h - <<_ACEOF >conftest.$ac_ext
/* end confdefs.h.  */
$4
#include <$2>
_ACEOF
if ac_fn_c_try_compile "$LINENO"; then :
  eval "$3=yes"
else
  eval "$3=no"
fi
rm -f core conftest.err conftest.$ac_objext conftest.$ac_ext
fi
eval ac_res=\$$3
	       { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_res" >&5
$as_echo "$ac_res" >&6; }
  eval $as_lineno_stack; ${as_lineno_stack:+:} unset as_lineno

} # ac_fn_c_check_header_compile

# ac_fn_c_check_type LINENO TYPE VAR INCLUDES
# -------------------------------------------
# Tests whether TYPE exists after having included INCLUDES, setting cache
# variable VAR accordingly.
ac_fn_c_check_type ()
{
  as_lineno=${as_lineno-"$1"} as_lineno_stack=as_lineno_stack=$as_lineno_stack
  { $as_echo "$as_me:${as_lineno-$LINENO}: checking for $2" >&5
$as_echo_n "checking for $2... " >&6; }
if eval \${$3+:} false; then :
  $as_echo_n "(cached) " >&6
else
  eval "$3=no"
  cat confdefs.h - <<_ACEOF >conftest.$ac_ext
/* end confdefs.h.  */
$4
int
main ()
{
if (sizeof ($2))
	 return 0;
  ;
  return 0;
}
_ACEOF
if ac_fn_c_try_compile "$LINENO"; then :
  cat confdefs.h - <<_ACEOF >conftest.$ac_ext
/* end confdefs.h.  */
$4
int
main ()
{
if (sizeof (($2)))
	    return 0;
  ;
  return 0;
}
_ACEOF
if ac_fn_c_try_compile "$LINENO"; then :

else
  eval "$3=yes"
fi
rm -f core conftest.err conftest.$ac_objext conftest.$ac_ext
fi
rm -f core conftest.err conftest.$ac_objext conftest.$ac_ext
fi
eval ac_res=\$$3
	       { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_res" >&5
$as_echo "$ac_res" >&6; }
  eval $as_lineno_stack; ${as_lineno_stack:+:} unset as_lineno

} # ac_fn_c_check_type

# ac_fn_c_try_link LINENO
# -----------------------
# Try to link conftest.$ac_ext, and return whether this succeeded.
ac_fn_c_try_link ()
{
  as_lineno=${as_lineno-"$1"} as_lineno_stack=as_lineno_stack=$as_lineno_stack
  rm -f conftest.$ac_objext conftest$ac_exeext
  if { { ac_try="$ac_link"
case "(($ac_try" in
  *\"* | *\`* | *\\*) ac_try_echo=\$ac_try;;
  *) ac_try_echo=$ac_try;;
esac
eval ac_try_echo="\"\$as_me:${as_lineno-$LINENO}: $ac_try_echo\""
$as_echo "$ac_try_echo"; } >&5
  (eval "$ac_link") 2>conftest.err
  ac_status=$?
  if test -s conftest.err; then
    grep -v '^ *+' conftest.err >conftest.er1
    cat conftest.er1 >&5
    mv -f conftest.er1 conftest.err
  fi
  $as_echo "$as_me:${as_lineno-$LINENO}: \$? = $ac_status" >&5
  test $ac_status = 0; } && {
	 test -z "$ac_c_werror_flag" ||
	 test ! -s conftest.err
       } && test -s conftest$ac_exeext && {
	 test "$cross_compiling" = yes ||
	 $as_test_x conftest$ac_exeext
       }; then :
  ac_retval=0
else
  $as_echo "$as_me: failed program was:" >&5
sed 's/^/| /' conftest.$ac_ext >&5

	ac_retval=1
fi
  # Delete the IPA/IPO (Inter Procedural Analysis/Optimization) information
  # created by the PGI compiler (conftest_ipa8_conftest.oo), as it would
  # interfere with the next link command; also delete a directory that is
  # left behind by Apple's compiler.  We do this before executing the actions.
  rm -rf conftest.dSYM conftest_ipa8_conftest.oo
  eval $as_lineno_stack; ${as_lineno_stack:+:} unset as_lineno
  as_fn_set_status $ac_retval

} # ac_fn_c_try_link

# ac_fn_c_check_func LINENO FUNC VAR
# ----------------------------------
# Tests whether FUNC exists, setting the cache variable VAR accordingly
ac_fn_c_check_func ()
{
  as_lineno=${as_lineno-"$1"} as_lineno_stack=as_lineno_stack=$as_lineno_stack
  { $as_echo "$as_me:${as_lineno-$LINENO}: checking for $2" >&5
$as_echo_n "checking for $2... " >&6; }
if eval \${$3+:} false; then :
  $as_echo_n "(cached) " >&6
else
  cat confdefs.h - <<_ACEOF >conftest.$ac_ext
/* end confdefs.h.  */
/* Define $2 to an innocuous variant, in case <limits.h> declares $2.
   For example, HP-UX 11i <limits.h> declares gettimeofday.  */
#define $2 innocuous_$2

/* System header to define __stub macros and hopefully few prototypes,
    which can conflict with char $2 (); below.
    Prefer <limits.h> to <assert.h> if __STDC__ is defined, since
    <limits.h> exists even on freestanding compilers.  */

#ifdef __STDC__
# include <limits.h>
#else
# include <assert.h>
#endif

#undef $2

/* Override any GCC internal prototype to avoid an error.
   Use char because int might match the return type of a GCC
   builtin and then its argument prototype would still apply.  */
#ifdef __cplusplus
extern "C"
#endif
char $2 ();
/* The GNU C library defines this for functions which it implements
    to always fail with ENOSYS.  Some functions are actually named
    something starting with __ and the normal name is an alias.  */
#if defined __stub_$2 || defined __stub___$2
choke me
#endif

int
main ()
{
return $2 ();
  ;
  return 0;
}
_ACEOF
if ac_fn_c_try_link "$LINENO"; then :
  eval "$3=yes"
else
  eval "$3=no"
fi
rm -f core conftest.err conftest.$ac_objext \
    conftest$ac_exeext conftest.$ac_ext
fi
eval ac_res=\$$3
	       { $as_echo "$as_me:${as_lineno-$LINENO}: result: $ac_res" >&5
$as_echo "$ac_res" >&6; }
  eval $as_lineno_stack; ${as_lineno_stack:+:} unset as_lineno

} # ac_fn_c_check_func
cat >config.log <<_ACEOF
This file contains any messages produced by compilers while
running configure, to aid debugging if configure makes a mistake.

It was created by $as_me, which was
generated by GNU Autoconf 2.68.  Invocation command line was

  $ $0 $@

_ACEOF
File: /ninfod\configure.in
dnl $USAGI: configure.in,v 1.12 2003-07-16 09:49:01 yoshfuji Exp $

dnl Copyright (C) 2002 USAGI/WIDE Project.
dnl All rights reserved.
dnl 
dnl Redistribution and use in source and binary forms, with or without
dnl modification, are permitted provided that the following conditions
dnl are met:
dnl 1. Redistributions of source code must retain the above copyright
dnl    notice, this list of conditions and the following disclaimer.
dnl 2. Redistributions in binary form must reproduce the above copyright
dnl    notice, this list of conditions and the following disclaimer in the
dnl    documentation and/or other materials provided with the distribution.
dnl 3. Neither the name of the project nor the names of its contributors
dnl    may be used to endorse or promote products derived from this software
dnl    without specific prior written permission.
dnl 
dnl THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
dnl ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
dnl IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
dnl ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
dnl FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
dnl DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
dnl OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
dnl HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
dnl LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
dnl OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
dnl SUCH DAMAGE.

AC_PREREQ(2.53)
AC_INIT(ninfod.c)
AC_CONFIG_HEADER(config.h)
AC_PREFIX_DEFAULT(/usr/local/v6)

AC_COPYRIGHT([Copyright (C)2002 USAGI/WIDE Project.  All Rights Reserved.])

dnl Checks for programs.
AC_PROG_CC
AC_PROG_INSTALL
INSTALL_LIB="\${INSTALL_DATA}"
AC_SUBST(INSTALL_LIB)
INSTALL_DIR="\${INSTALL} -d"
AC_SUBST(INSTALL_DIR)

dnl Checks for Enable/With
AC_ARG_ENABLE(debug,
[  --enable-debug          Enable debugging])
if test x"$enableval" != x"no"; then
  AC_DEFINE(ENABLE_DEBUG, 1, 
	    [Enable debugging])
fi

AC_ARG_ENABLE(threads,
[  --disable-threads       Disable threads (and random delay)],,enable_threads=no)
if test x"$enableval" != x"no"; then
  AC_DEFINE(ENABLE_THREADS, 1,
            [Enable threads])
fi

AC_ARG_ENABLE(suptypes,
[  --enable-suptypes       Enable suptypes qtype (deprecated)])
if test x"$enableval" != x"no"; then
  AC_DEFINE(ENABLE_SUPTYPES, 1,
	    [Enable suptypes (deprecated)])
fi

AC_ARG_ENABLE(suptypes,
[  --enable-ttl            Enable ttl support for qtypes (deprecated)])
if test x"$enableval" != x"no"; then
  AC_DEFINE(ENABLE_SUPTYPES, 1,
	    [Enable ttl support for qtypes (deprecated)])
fi

dnl Checks for libraries.

dnl Checks for header files.
AC_HEADER_STDC
AC_HEADER_TIME
AC_CHECK_HEADERS(limits.h)
AC_CHECK_HEADERS(gnutls/openssl.h)
AC_CHECK_HEADERS(openssl/md5.h)
AC_CHECK_HEADERS(sys/uio.h)
AC_CHECK_HEADERS(sys/utsname.h arpa/inet.h netdb.h syslog.h)
AC_CHECK_HEADERS(sys/capability.h)
AC_CHECK_HEADERS(pwd.h)
AC_CHECK_HEADERS(netinet/in.h)
AC_CHECK_HEADERS(netinet/ip6.h netinet/icmp6.h,,,[
#if HAVE_SYS_TYPES_H
# include <sys/types.h>
#endif
#if HAVE_NETINET_IN_H
# include <netinet/in.h>
#endif
])
AC_CHECK_HEADERS(linux/rtnetlink.h,,,[
#include <asm/types.h>
#include <sys/socket.h>
])
AC_CHECK_HEADERS(pthread.h)

dnl Checks for typedefs, structures, and compiler characteristics.
AC_C_BIGENDIAN
AC_C_CONST
AC_TYPE_SIZE_T

AC_MSG_CHECKING([for struct icmp6_nodeinfo])
AC_TRY_COMPILE([
#include <sys/types.h>
#include <netinet/in.h>
#include <netinet/icmp6.h>
],[
struct icmp6_nodeinfo nodeinfo;
],[
	AC_MSG_RESULT([yes])
	AC_DEFINE([HAVE_STRUCT_ICMP6_NODEINFO], 1,
		  [Define to 1 if you have struct icmp6_nodeinfo])
],[
	AC_MSG_RESULT([no])
])

dnl Checks for library functions.
AC_CHECK_FUNCS(nanosleep)
AC_CHECK_LIB(pthread, pthread_create)
AC_CHECK_LIB(cap, cap_init)

AC_CHECK_LIB(gnutls-openssl, MD5_Init,
	AC_DEFINE(HAVE_MD5_INIT)
	LIBS="-lgnutls-openssl $LIBS",
	AC_CHECK_LIB(crypto, MD5_Init,
		AC_DEFINE(HAVE_MD5_INIT)
		LIBS="-lcrypto $LIBS",
	)
)
dnl AC_CHECK_LIB(crypto, MD5Init,
dnl	AC_DEFINE(HAVE_MD5INIT)
dnl	LIBS="-lcrypto $LIBS",
dnl)

dnl AC_SUBST(DEFS)

AC_OUTPUT(Makefile ninfod.sh)


File: /ninfod\COPYING
Copyright (C) 2002 USAGI/WIDE Project.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of the project nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.


File: /ninfod\icmp6_nodeinfo.h
/*
 * Copyright (C) 2002 USAGI/WIDE Project.
 * Copyright (C) 1995, 1996, 1997, and 1998 WIDE Project.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the project nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#ifndef ICMP6_NODEINFO_H
#define ICMP6_NODEINFO_H

struct icmp6_nodeinfo {
	struct icmp6_hdr	icmp6_ni_hdr;
	uint8_t			icmp6_ni_nonce[8];
	/* could be followed by reply data */
};

#define ni_type		icmp6_ni_hdr.icmp6_type
#define ni_code		icmp6_ni_hdr.icmp6_code
#define ni_cksum	icmp6_ni_hdr.icmp6_cksum
#define ni_qtype	icmp6_ni_hdr.icmp6_data16[0]
#define ni_flags	icmp6_ni_hdr.icmp6_data16[1]
#define ni_nonce	icmp6_ni_nonce

/* ICMP6 types */
#define ICMP6_NI_QUERY			139
#define ICMP6_NI_REPLY			140

/* ICMP6 codes for NI Query */
#define ICMP6_NI_SUBJ_IPV6		0	/* Query Subject is an ipv6 address */
#define ICMP6_NI_SUBJ_FQDN		1	/* Query Subject is a Domain name */
#define ICMP6_NI_SUBJ_IPV4		2	/* Query Subject is an ipv4 address */

/* ICMP6 codes for NI Reply */
#define ICMP6_NI_SUCCESS		0	/* NI successful reply */
#define ICMP6_NI_REFUSED		1	/* NI request is refused */
#define ICMP6_NI_UNKNOWN		2	/* unknown Qtype */

/* NI Codes */
#define NI_QTYPE_NOOP			0	/* NOOP  */
#define NI_QTYPE_SUPTYPES		1	/* Supported Qtypes */
#define NI_QTYPE_DNSNAME		2	/* DNS Name */
#define NI_QTYPE_NODEADDR		3	/* Node Addresses */
#define NI_QTYPE_IPV4ADDR		4	/* IPv4 Addresses */

/* NI Flags */
#if WORDS_BIGENDIAN
#define NI_SUPTYPE_FLAG_COMPRESS	0x1
#define NI_FQDN_FLAG_VALIDTTL		0x1
#else
#define NI_SUPTYPE_FLAG_COMPRESS	0x0100
#define NI_FQDN_FLAG_VALIDTTL		0x0100
#endif

#if WORDS_BIGENDIAN
#define NI_NODEADDR_FLAG_TRUNCATE	0x1
#define NI_NODEADDR_FLAG_ALL		0x2
#define NI_NODEADDR_FLAG_COMPAT		0x4
#define NI_NODEADDR_FLAG_LINKLOCAL	0x8
#define NI_NODEADDR_FLAG_SITELOCAL	0x10
#define NI_NODEADDR_FLAG_GLOBAL		0x20
#else
#define NI_NODEADDR_FLAG_TRUNCATE	0x0100
#define NI_NODEADDR_FLAG_ALL		0x0200
#define NI_NODEADDR_FLAG_COMPAT		0x0400
#define NI_NODEADDR_FLAG_LINKLOCAL	0x0800
#define NI_NODEADDR_FLAG_SITELOCAL	0x1000
#define NI_NODEADDR_FLAG_GLOBAL		0x2000
#endif

#define NI_IPV4ADDR_FLAG_TRUNCATE	NI_NODEADDR_FLAG_TRUNCATE
#define NI_IPV4ADDR_FLAG_ALL		NI_NODEADDR_FLAG_ALL

#endif



File: /ninfod\install-sh
#!/bin/sh
#
# install - install a program, script, or datafile
# This comes from X11R5 (mit/util/scripts/install.sh).
#
# Copyright 1991 by the Massachusetts Institute of Technology
#
# Permission to use, copy, modify, distribute, and sell this software and its
# documentation for any purpose is hereby granted without fee, provided that
# the above copyright notice appear in all copies and that both that
# copyright notice and this permission notice appear in supporting
# documentation, and that the name of M.I.T. not be used in advertising or
# publicity pertaining to distribution of the software without specific,
# written prior permission.  M.I.T. makes no representations about the
# suitability of this software for any purpose.  It is provided "as is"
# without express or implied warranty.
#
# Calling this script install-sh is preferred over install.sh, to prevent
# `make' implicit rules from creating a file called install from it
# when there is no Makefile.
#
# This script is compatible with the BSD install script, but was written
# from scratch.  It can only install one file at a time, a restriction
# shared with many OS's install programs.


# set DOITPROG to echo to test this script

# Don't use :- since 4.3BSD and earlier shells don't like it.
doit="${DOITPROG-}"


# put in absolute paths if you don't have them in your path; or use env. vars.

mvprog="${MVPROG-mv}"
cpprog="${CPPROG-cp}"
chmodprog="${CHMODPROG-chmod}"
chownprog="${CHOWNPROG-chown}"
chgrpprog="${CHGRPPROG-chgrp}"
stripprog="${STRIPPROG-strip}"
rmprog="${RMPROG-rm}"
mkdirprog="${MKDIRPROG-mkdir}"

transformbasename=""
transform_arg=""
instcmd="$mvprog"
chmodcmd="$chmodprog 0755"
chowncmd=""
chgrpcmd=""
stripcmd=""
rmcmd="$rmprog -f"
mvcmd="$mvprog"
src=""
dst=""
dir_arg=""

while [ x"$1" != x ]; do
    case $1 in
	-c) instcmd="$cpprog"
	    shift
	    continue;;

	-d) dir_arg=true
	    shift
	    continue;;

	-m) chmodcmd="$chmodprog $2"
	    shift
	    shift
	    continue;;

	-o) chowncmd="$chownprog $2"
	    shift
	    shift
	    continue;;

	-g) chgrpcmd="$chgrpprog $2"
	    shift
	    shift
	    continue;;

	-s) stripcmd="$stripprog"
	    shift
	    continue;;

	-t=*) transformarg=`echo $1 | sed 's/-t=//'`
	    shift
	    continue;;

	-b=*) transformbasename=`echo $1 | sed 's/-b=//'`
	    shift
	    continue;;

	*)  if [ x"$src" = x ]
	    then
		src=$1
	    else
		# this colon is to work around a 386BSD /bin/sh bug
		:
		dst=$1
	    fi
	    shift
	    continue;;
    esac
done

if [ x"$src" = x ]
then
	echo "install:	no input file specified"
	exit 1
else
	true
fi

if [ x"$dir_arg" != x ]; then
	dst=$src
	src=""
	
	if [ -d $dst ]; then
		instcmd=:
		chmodcmd=""
	else
		instcmd=mkdir
	fi
else

# Waiting for this to be detected by the "$instcmd $src $dsttmp" command
# might cause directories to be created, which would be especially bad 
# if $src (and thus $dsttmp) contains '*'.

	if [ -f $src -o -d $src ]
	then
		true
	else
		echo "install:  $src does not exist"
		exit 1
	fi
	
	if [ x"$dst" = x ]
	then
		echo "install:	no destination specified"
		exit 1
	else
		true
	fi

# If destination is a directory, append the input filename; if your system
# does not like double slashes in filenames, you may need to add some logic

	if [ -d $dst ]
	then
		dst="$dst"/`basename $src`
	else
		true
	fi
fi

## this sed command emulates the dirname command
dstdir=`echo $dst | sed -e 's,[^/]*$,,;s,/$,,;s,^$,.,'`

# Make sure that the destination directory exists.
#  this part is taken from Noah Friedman's mkinstalldirs script

# Skip lots of stat calls in the usual case.
if [ ! -d "$dstdir" ]; then
defaultIFS='	
'
IFS="${IFS-${defaultIFS}}"

oIFS="${IFS}"
# Some sh's can't handle IFS=/ for some reason.
IFS='%'
set - `echo ${dstdir} | sed -e 's@/@%@g' -e 's@^%@/@'`
IFS="${oIFS}"

pathcomp=''

while [ $# -ne 0 ] ; do
	pathcomp="${pathcomp}${1}"
	shift

	if [ ! -d "${pathcomp}" ] ;
        then
		$mkdirprog "${pathcomp}"
	else
		true
	fi

	pathcomp="${pathcomp}/"
done
fi

if [ x"$dir_arg" != x ]
then
	$doit $instcmd $dst &&

	if [ x"$chowncmd" != x ]; then $doit $chowncmd $dst; else true ; fi &&
	if [ x"$chgrpcmd" != x ]; then $doit $chgrpcmd $dst; else true ; fi &&
	if [ x"$stripcmd" != x ]; then $doit $stripcmd $dst; else true ; fi &&
	if [ x"$chmodcmd" != x ]; then $doit $chmodcmd $dst; else true ; fi
else

# If we're going to rename the final executable, determine the name now.

	if [ x"$transformarg" = x ] 
	then
		dstfile=`basename $dst`
	else
		dstfile=`basename $dst $transformbasename | 
			sed $transformarg`$transformbasename
	fi

# don't allow the sed command to completely eliminate the filename

	if [ x"$dstfile" = x ] 
	then
		dstfile=`basename $dst`
	else
		true
	fi

# Make a temp file name in the proper directory.

	dsttmp=$dstdir/#inst.$$#

# Move or copy the file name to the temp name

	$doit $instcmd $src $dsttmp &&

	trap "rm -f ${dsttmp}" 0 &&

# and set any options; do chmod last to preserve setuid bits

# If any of these fail, we abort the whole thing.  If we want to
# ignore errors from any of these, just make sure not to ignore
# errors from the above "$doit $instcmd $src $dsttmp" command.

	if [ x"$chowncmd" != x ]; then $doit $chowncmd $dsttmp; else true;fi &&
	if [ x"$chgrpcmd" != x ]; then $doit $chgrpcmd $dsttmp; else true;fi &&
	if [ x"$stripcmd" != x ]; then $doit $stripcmd $dsttmp; else true;fi &&
	if [ x"$chmodcmd" != x ]; then $doit $chmodcmd $dsttmp; else true;fi &&

# Now rename the file to the real destination.

	$doit $rmcmd -f $dstdir/$dstfile &&
	$doit $mvcmd $dsttmp $dstdir/$dstfile 

fi &&


exit 0


File: /ninfod\Makefile.in
# $USAGI: Makefile.in,v 1.6 2003-01-15 06:41:23 mk Exp $
#
# Copyright (C)2002 USAGI/WIDE Project.
# Copyright (C)2000-2001 Hideaki YOSHIFUJI and USAGI Project.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the project nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#

# $Id: Makefile.in,v 1.2 2000/06/10 05:45:14 yoshfuji Exp yoshfuji $

SHELL = @SHELL@

srcdir = @srcdir@
prefix = @prefix@
exec_prefix = @exec_prefix@

bindir = @bindir@
sbindir = @sbindir@
libexecdir = @libexecdir@
datarootdir = @datarootdir@
datadir = @datadir@
sysconfdir = @sysconfdir@
sharedstatedir = @sharedstatedir@
localstatedir = @localstatedir@
libdir = @libdir@
infodir = @infodir@
mandir = @mandir@
includedir = @includedir@

INSTALL = @INSTALL@

CC = @CC@
CFLAGS=@CFLAGS@ -D_GNU_SOURCE
DEFS=@DEFS@
LIBS=@LIBS@
LDFLAGS=@LDFLAGS@
INSTALL = @INSTALL@

# ----------------
all: ninfod
clean:
	-rm -f *.o ninfod
distclean: clean
	-rm -f *~ *.bak #*
	-rm -fr autom4te.cache
File: /ninfod\ninfod.c
/* $USAGI: ninfod.c,v 1.34 2003-01-15 06:41:23 mk Exp $ */
/*
 * Copyright (C) 2002 USAGI/WIDE Project.
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the project nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */
/*
 * Author:
 * 	YOSHIFUJI Hideaki <yoshfuji@linux-ipv6.org>
 */

#if HAVE_CONFIG_H
#include "config.h"
#endif

#if HAVE_SYS_TYPES_H
# include <sys/types.h>
#endif
#if STDC_HEADERS
# include <stdio.h>
# include <stdlib.h>
# include <stddef.h>
# include <stdarg.h>
#else
# if HAVE_STDLIB_H
#  include <stdlib.h>
# endif
#endif

#if HAVE_STRING_H
# if !STDC_HEADERS && HAVE_MEMORY_H
#  include <memory.h>
# endif
# include <string.h>
#endif
#if HAVE_STRINGS_H
# include <strings.h>
#endif
#if HAVE_INTTYPES_H
# include <inttypes.h>
#else
# if HAVE_STDINT_H
#  include <stdint.h>
# endif
#endif
#if HAVE_LIMITS_H
# include <limits.h>
#endif
#if HAVE_UNISTD_H
# include <unistd.h>
#endif

#ifdef TIME_WITH_SYS_TIME
# include <sys/time.h>
# include <time.h>
#else
# ifdef HAVE_SYS_TIME_H
#  include <sys/time.h>
# else
#  include <time.h>
# endif
#endif

#if HAVE_SYS_UIO_H
#include <sys/uio.h>
#endif

#include <sys/socket.h>

#if HAVE_NETINET_IN_H
# include <netinet/in.h>
#endif

#if HAVE_NETINET_ICMP6_H
# include <netinet/icmp6.h>
#endif
#ifndef HAVE_STRUCT_ICMP6_NODEINFO
# include "icmp6_nodeinfo.h"
#endif

#if HAVE_NETDB_H
# include <netdb.h>
#endif
#include <errno.h>

#include <signal.h>

#if HAVE_SYSLOG_H
# include <syslog.h>
#endif

#if HAVE_PWD_H
# include <pwd.h>
#endif

#if HAVE_SYS_CAPABILITY_H
# include <sys/prctl.h>
# include <sys/capability.h>
#endif

#include "ninfod.h"

#ifndef offsetof
# define offsetof(aggregate,member)	((size_t)&((aggregate *)0)->member)
#endif

/* --------- */
/* ID */
static char *RCSID __attribute__ ((unused)) = "$USAGI: ninfod.c,v 1.34 2003-01-15 06:41:23 mk Exp $";

/* Variables */
int sock;
int daemonized;

char *appname;
static int opt_d = 0;	/* debug */
static int opt_h = 0;	/* help */
static char *opt_p = NINFOD_PIDFILE;	/* pidfile */
int opt_v = 0;		/* verbose */
static uid_t opt_u;

static int ipv6_pktinfo = IPV6_PKTINFO;

/* --------- */
#if ENABLE_DEBUG
static const __inline__ char * log_level(int priority) {
	switch(priority) {
	case LOG_EMERG:		return "EMERG";
	case LOG_ALERT:		return "ALERT";
	case LOG_CRIT:		return "CRIT";
	case LOG_ERR:		return "ERR";
	case LOG_WARNING:	return "WARNING";
	case LOG_NOTICE:	return "NOTICE";
	case LOG_INFO:		return "INFO";
	case LOG_DEBUG:		return "DEBUG";
	default:		return "???";
	}
}

void stderrlog(int pri, char *fmt, ...)
{
	va_list ap;
	char ebuf[512];
	char *buf;
	size_t buflen;

	va_start(ap, fmt);

	for (buf = ebuf, buflen = sizeof(ebuf);
	     buflen < SIZE_MAX / 2;
	     free(buf != ebuf ? buf : NULL), buf = NULL, buflen *= 2) {
		size_t rem;
		size_t res;

		buf = malloc(buflen);
		if (!buf)
			break;	/*XXX*/

		rem = buflen;

		res = snprintf(buf, rem, "[%s] ", log_level(pri));
		if (res >= rem)
			continue;
		rem -= res;

		res = vsnprintf(buf + res, rem, fmt, ap);

		if (res >= rem)
			continue;
		break;
	}

	if (buf) {
		fputs(buf, stderr);
		free(buf != ebuf ? buf : NULL);
	}

	va_end(ap);
}
#endif

/* --------- */
static int __inline__ open_sock(void)
{
	return socket(PF_INET6, SOCK_RAW, IPPROTO_ICMPV6);
}

static int set_recvpktinfo(int sock)
{
	int on, ret;

	on = 1;

#if defined(IPV6_RECVPKTINFO)
	ret = setsockopt(sock,
			 IPPROTO_IPV6, IPV6_RECVPKTINFO,
			 &on, sizeof(on));
	if (!ret)
		return 0;
# if defined(IPV6_2292PKTINFO)
	ret = setsockopt(sock,
			 IPPROTO_IPV6, IPV6_2292PKTINFO,
			 &on, sizeof(on));
	if (!ret) {
		ipv6_pktinfo = IPV6_2292PKTINFO;
		return 0;
	}

	DEBUG(LOG_ERR, "setsockopt(IPV6_RECVPKTINFO/IPV6_2292PKTINFO): %s\n",
	      strerror(errno));
# else
	DEBUG(LOG_ERR, "setsockopt(IPV6_RECVPKTINFO): %s\n",
	      strerror(errno));
# endif
#else
	ret = setsockopt(sock,
			 IPPROTO_IPV6, IPV6_PKTINFO,
			 &on, sizeof(on));
	if (!ret)
		return 0;

	DEBUG(LOG_ERR, "setsockopt(IPV6_PKTINFO): %s\n",
	      strerror(errno));
#endif

	return -1;
}

static int __inline__ init_sock(int sock)
{
	struct icmp6_filter filter;
#if NEED_IPV6CHECKSUM
	int i;

	i = offsetof(struct icmp6_nodeinfo, ni_cksum);
	if (setsockopt(sock,
		       IPPROTO_IPV6, IPV6_CHECKSUM,
		       &i, sizeof(i)) < 0) {
		DEBUG(LOG_ERR, "setsockopt(IPV6_CHECKSUM): %s\n",
		      strerror(errno));
		return -1;
	}
#endif

	ICMP6_FILTER_SETBLOCKALL(&filter);
	ICMP6_FILTER_SETPASS(ICMP6_NI_QUERY, &filter);
	if (setsockopt(sock,
		       IPPROTO_ICMPV6, ICMP6_FILTER,
		       &filter, sizeof(filter)) < 0) {
		DEBUG(LOG_ERR, "setsockopt(ICMP6_FILTER): %s\n",
		      strerror(errno));
		return -1;
	}

	if (set_recvpktinfo(sock) < 0)
		return -1;

	return 0;
}

/* --------- */
int ni_recv(struct packetcontext *p)
{
	int sock = p->sock;
	struct iovec iov[1];
	struct msghdr msgh;
	char recvcbuf[CMSG_SPACE(sizeof(p->pktinfo))];
	struct cmsghdr *cmsg;
	int cc;

	DEBUG(LOG_DEBUG, "%s()\n", __func__);

	memset(&iov, 0, sizeof(iov));
	iov[0].iov_base = p->query;
	iov[0].iov_len = sizeof(p->query);

	memset(&msgh, 0, sizeof(msgh));
	msgh.msg_name = (struct sockaddr *)&p->addr;
	msgh.msg_namelen = sizeof(p->addr);
	msgh.msg_iov = iov;
	msgh.msg_iovlen = 1;
	msgh.msg_control = recvcbuf;
	msgh.msg_controllen = sizeof(recvcbuf);

	if ((cc = recvmsg(sock, &msgh, 0)) < 0)
		return -1;

	p->querylen = cc;
	p->addrlen = msgh.msg_namelen;

	for (cmsg = CMSG_FIRSTHDR(&msgh); cmsg;
	     cmsg = CMSG_NXTHDR(&msgh, cmsg)) {
		if (cmsg->cmsg_level == IPPROTO_IPV6 &&
		    (cmsg->cmsg_type == IPV6_PKTINFO
#if defined(IPV6_2292PKTINFO)
		     || cmsg->cmsg_type == IPV6_2292PKTINFO
#endif
		    )) {
			memcpy(&p->pktinfo, CMSG_DATA(cmsg), sizeof(p->pktinfo));
			break;
		}
	}

	return 0;
}

int ni_send(struct packetcontext *p)
{
	int sock = p->sock;
	struct iovec iov[2];
	char cbuf[CMSG_SPACE(sizeof(p->pktinfo))];
	struct msghdr msgh;
	struct cmsghdr *cmsg;
	int cc;

	DEBUG(LOG_DEBUG, "%s()\n", __func__);

	memset(&iov, 0, sizeof(iov));
	iov[0].iov_base = &p->reply;
	iov[0].iov_len = sizeof(p->reply);
	iov[1].iov_base = p->replydata;
	iov[1].iov_len = p->replydatalen;

	memset(&msgh, 0, sizeof(msgh));
	msgh.msg_name = (struct sockaddr *)&p->addr;
	msgh.msg_namelen = p->addrlen;
	msgh.msg_iov = iov;
	msgh.msg_iovlen = p->replydata ? 2 : 1;

	msgh.msg_control = cbuf;
	msgh.msg_controllen = sizeof(cbuf);

	cmsg = CMSG_FIRSTHDR(&msgh);
	cmsg->cmsg_level = IPPROTO_IPV6;
	cmsg->cmsg_type = ipv6_pktinfo;
	cmsg->cmsg_len = CMSG_LEN(sizeof(p->pktinfo));
	memcpy(CMSG_DATA(cmsg), &p->pktinfo, sizeof(p->pktinfo));

	msgh.msg_controllen = cmsg->cmsg_len;

	if (p->delay) {
#if HAVE_NANOSLEEP
		struct timespec ts, rts;
		int err = 0;

		rts.tv_sec  = p->delay / 1000000;
		rts.tv_nsec = (long)(p->delay % 1000000) * 1000;

		do {
			ts = rts;
			err = nanosleep(&ts, &rts);
		} while(err < 0);
#else
		usleep(p->delay);	/*XXX: signal*/
#endif
	}

	cc = sendmsg(sock, &msgh, 0);
	if (cc < 0)
		DEBUG(LOG_DEBUG, "sendmsg(): %s\n", strerror(errno));

	ni_free(p->replydata);
	ni_free(p);

	return cc;
}

/* --------- */
static void sig_handler(int sig)
{
	int err;

	DEBUG(LOG_INFO, "singnal(%d) received, quit.\n", sig);
	err = unlink(opt_p);
	if (err < 0) {
		DEBUG(LOG_ERR, "failed to unlink file '%s' : %s\n",
				opt_p, strerror(errno));
		exit(1);
	}
	/* closelog() */

	exit(0);
}

static void do_daemonize(void)
{
	FILE *fp = NULL;
	struct sigaction act;
	sigset_t smask;
	pid_t pid;

	if (opt_p) {
		if (!access(opt_p, R_OK)) {
			if ((fp = fopen(opt_p, "r"))) {
				if (fscanf(fp, "%d", &pid) != 1) {
					DEBUG(LOG_ERR, "pid file '%s' exists, but read failed.\n",
					      opt_p);
				} else {
					DEBUG(LOG_ERR, "pid file '%s' exists : %d\n",
					      opt_p, pid);
				}
				fclose(fp);
				exit(1);
			}
		}

		sigemptyset(&smask);
		sigaddset(&smask, SIGHUP);
		sigaddset(&smask, SIGINT);
		sigaddset(&smask, SIGQUIT);
		sigaddset(&smask, SIGTERM);

		memset(&act, 0, sizeof(act));
		act.sa_handler = sig_handler;
		act.sa_mask = smask;

		sigaction(SIGHUP, &act, NULL);
		sigaction(SIGINT, &act, NULL);
		sigaction(SIGQUIT, &act, NULL);
		sigaction(SIGTERM, &act, NULL);

		fp = fopen(opt_p, "w+");
		if (!fp) {
			DEBUG(LOG_ERR, "failed to open file '%s': %s\n",
			      opt_p, strerror(errno));
			exit(1);
		}
	}

	if (daemon(0, 0) < 0) {
		DEBUG(LOG_ERR, "failed to daemon(): %s\n", strerror(errno));
		unlink(opt_p);
		exit(1);
	}
#if ENABLE_DEBUG
	openlog(NINFOD, 0, LOG_USER);
#endif
	daemonized = 1;

	if (fp) {
		fprintf(fp, "%d\n", getpid());
		fclose(fp);
	}
}

/* --------- */
#ifdef HAVE_LIBCAP
static const cap_value_t cap_net_raw = CAP_NET_RAW;
static const cap_value_t cap_setuid =  CAP_SETUID; 
static cap_flag_value_t cap_ok;
#else
static uid_t euid;
#endif

static void limit_capabilities(void)
{
#ifdef HAVE_LIBCAP
	cap_t cap_p, cap_cur_p;

	cap_p = cap_init();
	if (!cap_p) {
		DEBUG(LOG_ERR, "cap_init: %s\n", strerror(errno));
		exit(-1);
	}

	cap_cur_p = cap_get_proc();
	if (!cap_cur_p) {
		DEBUG(LOG_ERR, "cap_get_proc: %s\n", strerror(errno));
		exit(-1);
        }

	/* net_raw + setuid / net_raw */
	cap_get_flag(cap_cur_p, CAP_NET_RAW, CAP_PERMITTED, &cap_ok);
	if (cap_ok != CAP_CLEAR) {
		cap_set_flag(cap_p, CAP_PERMITTED, 1, &cap_net_raw, CAP_SET);
		cap_set_flag(cap_p, CAP_EFFECTIVE, 1, &cap_net_raw, CAP_SET);
	}

	cap_get_flag(cap_cur_p, CAP_SETUID, CAP_PERMITTED, &cap_ok);
	if (cap_ok != CAP_CLEAR)
		cap_set_flag(cap_p, CAP_PERMITTED, 1, &cap_setuid, CAP_SET);

	if (cap_set_proc(cap_p) < 0) {
		DEBUG(LOG_ERR, "cap_set_proc: %s\n", strerror(errno));
		if (errno != EPERM)
			exit(-1);
	}

	if (prctl(PR_SET_KEEPCAPS, 1) < 0) {
		DEBUG(LOG_ERR, "prctl: %s\n", strerror(errno));
		exit(-1);
	}

	cap_free(cap_cur_p);
	cap_free(cap_p);
#else
	euid = geteuid();
#endif
}

static void drop_capabilities(void)
{
#ifdef HAVE_LIBCAP
	cap_t cap_p;

	cap_p = cap_init();
	if (!cap_p) {
		DEBUG(LOG_ERR, "cap_init: %s\n", strerror(errno));
		exit(-1);
	}

	/* setuid / setuid */
	if (cap_ok != CAP_CLEAR) {
		cap_set_flag(cap_p, CAP_PERMITTED, 1, &cap_setuid, CAP_SET);
		cap_set_flag(cap_p, CAP_EFFECTIVE, 1, &cap_setuid, CAP_SET);

		if (cap_set_proc(cap_p) < 0) {
			DEBUG(LOG_ERR, "cap_set_proc: %s\n", strerror(errno));
			exit(-1);
		}
	}

	if (seteuid(opt_u ? opt_u : getuid()) < 0) {
		DEBUG(LOG_ERR, "setuid: %s\n", strerror(errno));
		exit(-1);
	}

	if (prctl(PR_SET_KEEPCAPS, 0) < 0) {
		DEBUG(LOG_ERR, "prctl: %s\n", strerror(errno));
		exit(-1);
	}

	cap_clear(cap_p);
	if (cap_set_proc(cap_p) < 0) {
		DEBUG(LOG_ERR, "cap_set_proc: %s\n", strerror(errno));
		exit(-1);
	}

	cap_free(cap_p);
#else
	if (setuid(getuid()) < 0) {
		DEBUG(LOG_ERR, "setuid: %s\n", strerror(errno));
		exit(-1);
	}
#endif
}

/* --------- */
static void parse_args(int argc, char **argv)
{
	int c;
	unsigned long val;
	char *ep;

	/* parse options */
	while ((c = getopt(argc, argv, "dhvp:u:")) != -1) {
		switch(c) {
		case 'd':	/* debug */
			opt_d = 1;
			break;
		case 'v':	/* verbose */
			opt_v = 1;
			break;
		case 'p':
			opt_p = optarg;
			break;
		case 'u':
			val = strtoul(optarg, &ep, 10);
			if (!optarg || *ep) {
				struct passwd *pw = getpwnam(optarg);
				if (!pw) {
					DEBUG(LOG_ERR, "No such user: %s", optarg);
					exit(1);
				}
				opt_u = pw->pw_uid;
			} else
				opt_u = val;
			break;
		case 'h':	/* help */
		default:
			opt_h = 1;
			break;
		}
	}

	argc -= optind;
#if 0
	argv += optind;
#endif

	if (argc)
		opt_h = 1;
}

static void print_copying(void) {
	fprintf(stderr,
		"Node Information Daemon\n"
		"Copyright (C)2002 USAGI/WIDE Project.  All Rights Reserved.\n"
		"\n"
	);
}

static void print_usage(void) {
	fprintf(stderr, 
		"Usage: %s [-d] [-p pidfile] [-u user] [-h] [-v]\n\n",
		appname
	);
}

/* --------- */
int main (int argc, char **argv)
{
	int sock_errno = 0;

	appname = argv[0];

	limit_capabilities();

	sock = open_sock();
	if (sock < 0)
		sock_errno = errno;

	parse_args(argc, argv);

	drop_capabilities();

	if (opt_h || opt_v)
		print_copying();
	if (opt_h) {
		print_usage();
		exit(1);
	}

	if (sock_errno) {
		DEBUG(LOG_ERR, "socket: %s\n", strerror(sock_errno));
		exit(1);
	}

	setbuf(stderr, NULL);

	if (!opt_d)
		do_daemonize();

	/* initialize */
	if (init_sock(sock) < 0)
		exit(1);

	init_core(1);

	/* main loop */
	while(1) {
		struct packetcontext *p;
		struct icmp6_hdr *icmph;
#if ENABLE_DEBUG
		char saddrbuf[NI_MAXHOST];
		int gni;
#endif 

		init_core(0);

		p = ni_malloc(sizeof(*p));
		if (!p) {
			DEBUG(LOG_WARNING, "%s(): failed to allocate packet context; sleep 1 sec.\n",
			      __func__);
			sleep(1);
			continue;
		}

		while (1) {
			memset(p, 0, sizeof(*p));
			p->sock = sock;

			if (ni_recv(p) < 0) {
				if (errno == EAGAIN || errno == EINTR)
					continue;
				/* XXX: syslog */
				continue;
			}
			break;
		}

#if ENABLE_DEBUG
		gni = getnameinfo((struct sockaddr *)&p->addr,
				  p->addrlen,
				  saddrbuf, sizeof(saddrbuf),
				  NULL, 0,
				  NI_NUMERICHOST);
		if (gni)
			sprintf(saddrbuf, "???");
#endif
		init_core(0);

		if (p->querylen < sizeof(struct icmp6_hdr)) {
			ni_free(p);
			DEBUG(LOG_WARNING, "Too short icmp message from %s\n", saddrbuf);
			continue;
		}

		icmph = (struct icmp6_hdr *)p->query;

		DEBUG(LOG_DEBUG,
		      "type=%d, code=%d, cksum=0x%04x\n",
		      icmph->icmp6_type, icmph->icmp6_code,
		      ntohs(icmph->icmp6_cksum));

		if (icmph->icmp6_type != ICMP6_NI_QUERY) {
			DEBUG(LOG_WARNING,
			      "Strange icmp type %d from %s\n", 
			      icmph->icmp6_type, saddrbuf);
			ni_free(p);
			continue;
		}

		pr_nodeinfo(p);	/* this frees p */
	}
}



File: /ninfod\ninfod.h
/* $USAGI: ninfod.h,v 1.20 2002-12-19 15:51:16 yoshfuji Exp $ */
/*
 * Copyright (C) 2002 USAGI/WIDE Project.
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the project nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */
/*
 * Author:
 * 	YOSHIFUJI Hideaki <yoshfuji@linux-ipv6.org>
 */

/* definitions */
#define NINFOD			"ninfod"
#define NINFOD_PIDFILE		"/var/run/ninfod.pid"

#define	MAX_ANYCAST_DELAY_TIME	1000000.0	/* 1 sec */

#define MAX_DNSLABEL_SIZE	63
#define MAX_DNSNAME_SIZE	255
#define MAX_QUERY_SIZE		(sizeof(struct icmp6_nodeinfo)+MAX_DNSNAME_SIZE+2)
#define MAX_REPLY_SIZE		1280-sizeof(struct ip6_hdr)

#define MAX_SUPTYPES		32

#define CHECKANDFILL_ARGS	struct packetcontext *p,\
				char *subject, size_t subjlen,	\
				unsigned int flags,		\
				unsigned int *subj_if,		\
				int reply
#define INIT_ARGS		\
				int forced

struct packetcontext {
	/* socket */
	int sock;

	/* query info */
	struct sockaddr_storage addr;
	socklen_t addrlen;
	struct in6_pktinfo pktinfo;
	char query[MAX_QUERY_SIZE];
	int querylen;

	/* reply info */
	struct icmp6_nodeinfo reply;	/* common */
	char *replydata;		/* data */
	int replydatalen;

	unsigned int delay;		/* (random) delay */
};

/* variables */
extern int opt_v;		/* ninfod.c */
extern int daemonized;		/* ninfod.c */
extern int sock;		/* ninfod.c */
extern int initialized;		/* ninfod_core.c */

/* ninfod.c* */
int ni_recv(struct packetcontext *p);
int ni_send(struct packetcontext *p);

/* ninfod_core.c */
#if ENABLE_DEBUG
void stderrlog(int priority, char *format, ...);
# define DEBUG(pri, fmt, args...)	do {									\
						int saved_errno = errno;					\
						if (opt_v || pri != LOG_DEBUG) {				\
							if (daemonized) {					\
								syslog(pri, fmt, ## args);			\
							} else {						\
								stderrlog(pri, fmt, ## args);			\
							}							\
						}								\
						errno = saved_errno;						\
					} while(0)
#else
# define DEBUG(pri, fmt, args...)	do { ; } while(0)
#endif

#define ni_malloc(size)	({										\
				size_t _size = (size);							\
				void *p = malloc(_size);						\
				DEBUG(LOG_DEBUG, "%s(): malloc(%zu) = %p\n", __func__, _size, p);	\
				p;									\
			})
#define ni_free(p)	({										\
				void *_p = (p);								\
				int saved_errno = errno;						\
				DEBUG(LOG_DEBUG, "%s(): free(%p)\n", __func__, _p);			\
				free(_p);								\
				errno = saved_errno;							\
			})

void init_core(int forced);
int pr_nodeinfo(struct packetcontext *p);

int pr_nodeinfo_unknown(CHECKANDFILL_ARGS);
int pr_nodeinfo_refused(CHECKANDFILL_ARGS);
int pr_nodeinfo_noop(CHECKANDFILL_ARGS);
void init_nodeinfo_suptypes(INIT_ARGS);
int pr_nodeinfo_suptypes(CHECKANDFILL_ARGS);

/* ninfod_addrs.c */
void init_nodeinfo_ipv6addr(INIT_ARGS);
int pr_nodeinfo_ipv6addr(CHECKANDFILL_ARGS);
void init_nodeinfo_ipv4addr(INIT_ARGS);
int pr_nodeinfo_ipv4addr(CHECKANDFILL_ARGS);

/* ninfod_name.c */
int check_nigroup(const struct in6_addr *addr);
void init_nodeinfo_nodename(INIT_ARGS);
int pr_nodeinfo_nodename(CHECKANDFILL_ARGS);



File: /ninfod\ninfod.sh.in
#!/bin/sh

NINFOD=@prefix@/sbin/ninfod
PID=/var/run/ninfod.pid

if ! [ -x $NINFOD ]; then
	exit 0
fi

case "$1" in
    start)
	echo -n "Starting node infomation daemon:"
	echo -n " ninfod" ; 
	$NINFOD 
	echo "."
	;;
    stop)
	echo -n "Stopping node infomation daemon:"
	echo -n " ninfod" ; 
	kill `cat $PID`
	echo "."
	;;
    restart)
	echo -n "Restarting node information daemon:"
	echo -n " ninfod"
	kill `cat $PID`
	$NINFOD
	echo "."
	;;
    *)
	echo "Usage: /etc/init.d/ninfod {start|stop|restart}"
	exit 1
	;;
esac

exit 0



File: /ninfod\ninfod_addrs.c
/* $USAGI: ninfod_addrs.c,v 1.18 2003-07-16 09:49:01 yoshfuji Exp $ */
/*
 * Copyright (C) 2002 USAGI/WIDE Project.
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the project nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */
/*
 * Author:
 * 	YOSHIFUJI Hideaki <yoshfuji@linux-ipv6.org>
 */

#if HAVE_CONFIG_H
#include "config.h"
#endif

#if HAVE_SYS_TYPES_H
# include <sys/types.h>
#endif

#if STDC_HEADERS
# include <stdio.h>
# include <stdlib.h>
# include <stddef.h>
#else
# if HAVE_STDLIB_H
#  include <stdlib.h>
# endif
#endif
#if HAVE_STRING_H
# if !STDC_HEADERS && HAVE_MEMORY_H
#  include <memory.h>
# endif
# include <string.h>
#endif
#if HAVE_STRINGS_H
# include <strings.h>
#endif
#if HAVE_INTTYPES_H
# include <inttypes.h>
#else
# if HAVE_STDINT_H
#  include <stdint.h>
# endif
#endif
#if HAVE_UNISTD_H
# include <unistd.h>
#endif

#if TIME_WITH_SYS_TIME   
# include <sys/time.h>  
# include <time.h>
#else
# if HAVE_SYS_TIME_H     
#  include <sys/time.h>
# else                
#  include <time.h>
# endif                  
#endif                   

#if HAVE_SYS_UIO_H
#include <sys/uio.h>
#endif

#include <sys/socket.h>
#if HAVE_LINUX_RTNETLINK_H
#include <asm/types.h>
#include <linux/rtnetlink.h>
#endif

#if HAVE_NETINET_IN_H
# include <netinet/in.h>
#endif

#if HAVE_NETINET_IP6_H
# include <netinet/ip6.h>
#endif

#if HAVE_NETINET_ICMP6_H
# include <netinet/icmp6.h>
#endif
#ifndef HAVE_STRUCT_ICMP6_NODEINFO
# include "icmp6_nodeinfo.h"
#endif

#if HAVE_NETDB_H
# include <netdb.h>
#endif
#include <errno.h>

#if HAVE_SYSLOG_H
# include <syslog.h>
#endif

#include "ninfod.h"
#include "ni_ifaddrs.h"

#ifndef offsetof
# define offsetof(aggregate,member)	((size_t)&((aggregate *)0)->member)
#endif

/* ---------- */
/* ID */
static char *RCSID __attribute__ ((unused)) = "$USAGI: ninfod_addrs.c,v 1.18 2003-07-16 09:49:01 yoshfuji Exp $";

/* ---------- */
/* ipv6 address */
void init_nodeinfo_ipv6addr(INIT_ARGS)
{
	DEBUG(LOG_DEBUG, "%s()\n", __func__);
	return;
}

int filter_ipv6addr(const struct in6_addr *ifaddr, unsigned int flags)
{
	if (IN6_IS_ADDR_UNSPECIFIED(ifaddr) ||
	    IN6_IS_ADDR_LOOPBACK(ifaddr)) {
		return 1;
	} else if (IN6_IS_ADDR_V4COMPAT(ifaddr) ||
		   IN6_IS_ADDR_V4MAPPED(ifaddr)) {
		return !(flags & NI_NODEADDR_FLAG_COMPAT);
	} else if (IN6_IS_ADDR_LINKLOCAL(ifaddr)) {
		return !(flags & NI_NODEADDR_FLAG_LINKLOCAL);
	} else if (IN6_IS_ADDR_SITELOCAL(ifaddr)) {
		return !(flags & NI_NODEADDR_FLAG_SITELOCAL);
	}
	return !(flags & NI_NODEADDR_FLAG_GLOBAL);
}

int pr_nodeinfo_ipv6addr(CHECKANDFILL_ARGS)
{
	struct ni_ifaddrs *ifa0;
	unsigned int ifindex = 0;

	DEBUG(LOG_DEBUG, "%s()\n", __func__);

	if (subject && subjlen != sizeof(struct in6_addr)) {
		DEBUG(LOG_INFO,
		      "%s(): invalid subject length %zu for IPv6 Address Subject\n",
		      __func__, subjlen);
		return 1;
	}
	if (ni_ifaddrs(&ifa0, AF_INET6))
		return -1;	/* failed to get addresses */

	/* pass 0: consider subject and determine subjected interface */
	if (subject) {
		struct ni_ifaddrs *ifa;

		for (ifa = ifa0; ifa; ifa = ifa->ifa_next) {
			if (!ifa->ifa_addr)
				continue;
			if (ifa->ifa_flags & (IFA_F_TENTATIVE|IFA_F_SECONDARY))
				continue;
			if (!ifindex && 
			    IN6_ARE_ADDR_EQUAL(&p->pktinfo.ipi6_addr,
					       (struct in6_addr *)subject)) {
				/*
				 * if subject is equal to destination
				 * address, receiving interface is
				 * the candidate subject interface.
				 */
				ifindex = p->pktinfo.ipi6_ifindex;
			}
			if (!IN6_IS_ADDR_LOOPBACK((struct in6_addr *)subject) &&
			    IN6_ARE_ADDR_EQUAL((struct in6_addr *)ifa->ifa_addr,
					       (struct in6_addr *)subject)) {
				/*
				 * address is assigned on some interface.
				 * if multiple interfaces have the same interface,
				 *  1) prefer receiving interface
				 *  2) use first found one
				 */
				if (!ifindex ||
				    (p->pktinfo.ipi6_ifindex == ifindex))
					ifindex = ifa->ifa_ifindex;
			}
		}
		if (!ifindex) {
			ni_freeifaddrs(ifa0);
			return 1;	/* subject not found */
		}
		if (subj_if)
			*subj_if = ifindex;
	} else {
		ifindex = subj_if ? *subj_if : 0;
		if (ifindex == 0)
			ifindex = p->pktinfo.ipi6_ifindex;
		if (ifindex == 0) {
			ni_freeifaddrs(ifa0);
			return 1;	/* XXX */
		}
	}

	if (reply) {
		struct ni_ifaddrs *ifa;
		unsigned int addrs0 = 0, paddrs0 = 0;
		unsigned int addrs, paddrs = 0, daddrs = 0;

		flags &= ~NI_NODEADDR_FLAG_TRUNCATE;	
	
		/* pass 1: count addresses and preferred addresses to be returned */
		for (ifa = ifa0; ifa; ifa = ifa->ifa_next) {
			if (!ifa->ifa_addr)
				continue;
			if (ifa->ifa_flags & (IFA_F_TENTATIVE|IFA_F_SECONDARY))
				continue;
			if (!(flags & NI_NODEADDR_FLAG_ALL) &&
			    ifa->ifa_ifindex != ifindex)
				continue;
			if (filter_ipv6addr((struct in6_addr *)ifa->ifa_addr, flags))
				continue;

			if (addrs0 + 1 >= ((MAX_REPLY_SIZE - sizeof(struct icmp6_nodeinfo)) / (sizeof(uint32_t) + sizeof(struct in6_addr)))) {
				flags |= ~NI_NODEADDR_FLAG_TRUNCATE;
				break;
			}

			addrs0++;
			if (!(ifa->ifa_flags & IFA_F_DEPRECATED))
				paddrs0++;
		}
		
		p->reply.ni_type = ICMP6_NI_REPLY;
		p->reply.ni_code = ICMP6_NI_SUCCESS;
		p->reply.ni_cksum = 0;
		p->reply.ni_qtype = htons(NI_QTYPE_NODEADDR);
		p->reply.ni_flags = flags&(NI_NODEADDR_FLAG_COMPAT|
					   NI_NODEADDR_FLAG_LINKLOCAL|
					   NI_NODEADDR_FLAG_SITELOCAL|
					   NI_NODEADDR_FLAG_GLOBAL);

		/* pass 2: store addresses */
		p->replydatalen = (sizeof(uint32_t)+sizeof(struct in6_addr)) * addrs0;
		p->replydata = p->replydatalen ? ni_malloc(p->replydatalen) : NULL;

		if (p->replydatalen && !p->replydata) {
			p->reply.ni_flags |= NI_NODEADDR_FLAG_TRUNCATE;
			addrs0 = paddrs0 = 0;
		}

		for (ifa = ifa0, addrs = 0; 
		     ifa && addrs < addrs0; 
		     ifa = ifa->ifa_next) {
			char *cp;
			uint32_t ttl;

			if (!ifa->ifa_addr)
				continue;
			if (ifa->ifa_flags & (IFA_F_TENTATIVE|IFA_F_SECONDARY))
				continue;
			if (!(flags & NI_NODEADDR_FLAG_ALL) &&
			    ((subj_if && *subj_if) ? (ifa->ifa_ifindex != *subj_if) :
						     (ifa->ifa_ifindex != p->pktinfo.ipi6_ifindex)))
				continue;
			if (filter_ipv6addr((struct in6_addr *)ifa->ifa_addr, flags))
				continue;

#if ENABLE_TTL
			if (ifa->ifa_cacheinfo) {
				ttl = ifa->ifa_cacheinfo->ifa_valid > 0x7fffffff ? 
				      htonl(0x7fffffff) : htonl(ifa->ifa_cacheinfo->ifa_valid);
			} else {
				ttl = (ifa->ifa_flags & IFA_F_PERMANENT) ? htonl(0x7fffffff) : 0;
			}
#else
			ttl = 0;
#endif

			cp = p->replydata +
			     (sizeof(uint32_t)+sizeof(struct in6_addr)) * (ifa->ifa_flags & IFA_F_DEPRECATED ? paddrs0+daddrs : paddrs);
			memcpy(cp, &ttl, sizeof(ttl));
			memcpy(cp + sizeof(ttl), ifa->ifa_addr, sizeof(struct in6_addr));

			addrs++;
			if (ifa->ifa_flags & IFA_F_DEPRECATED)
				daddrs++;
			else
				paddrs++;
		}
	}

	ni_freeifaddrs(ifa0);
	return 0;
}

/* ipv4 address */
void init_nodeinfo_ipv4addr(INIT_ARGS)
{
	DEBUG(LOG_DEBUG, "%s()\n", __func__);
	return;
}

int filter_ipv4addr(const struct in_addr *ifaddr, unsigned int flags)
{
	return 0;
}

int pr_nodeinfo_ipv4addr(CHECKANDFILL_ARGS)
{
	struct ni_ifaddrs *ifa0;
	unsigned int ifindex = 0;

	DEBUG(LOG_DEBUG, "%s()\n", __func__);

	if (subject && subjlen != sizeof(struct in_addr)) {
		DEBUG(LOG_INFO,
		      "%s(): invalid subject length %zu for IPv4 Address Subject\n",
		      __func__, subjlen);
		return 1;
	}
	if (ni_ifaddrs(&ifa0, AF_INET))
		return -1;	/* failed to get addresses */

	/* pass 0: consider subject and determine subjected interface */
	if (subject) {
		struct ni_ifaddrs *ifa;

		for (ifa = ifa0; ifa; ifa = ifa->ifa_next) {
			if (!ifa->ifa_addr)
				continue;
			if (ifa->ifa_flags & (IFA_F_TENTATIVE|IFA_F_SECONDARY))
				continue;
			if ((((struct in_addr *)subject)->s_addr != htonl(INADDR_LOOPBACK)) &&
			    memcmp((struct in_addr *)ifa->ifa_addr,
				   (struct in_addr *)subject,
				   sizeof(struct in_addr)) == 0) {
				/*
				 * address is assigned on some interface.
				 * if multiple interfaces have the same interface,
				 *  1) prefer receiving interface
				 *  2) use first found one
				 */
				if (!ifindex ||
				    (p->pktinfo.ipi6_ifindex == ifindex))
					ifindex = ifa->ifa_ifindex;
			}
		}
		if (!ifindex) {
			ni_freeifaddrs(ifa0);
			return 1;	/* subject not found */
		}
		if (subj_if)
			*subj_if = ifindex;
	} else {
		ifindex = subj_if ? *subj_if : 0;
		if (ifindex == 0)
			ifindex = p->pktinfo.ipi6_ifindex;
		if (ifindex == 0) {
			ni_freeifaddrs(ifa0);
			return 1;	/* XXX */
		}
	}

	if (reply) {
		struct ni_ifaddrs *ifa;
		unsigned int addrs0 = 0, paddrs0 = 0;
		unsigned int addrs, paddrs = 0, daddrs = 0;

		flags &= ~NI_IPV4ADDR_FLAG_TRUNCATE;

		/* pass 1: count addresses and preferred addresses to be returned */
		for (ifa = ifa0; ifa; ifa = ifa->ifa_next) {
			if (!ifa->ifa_addr)
				continue;
#if 1	/* not used in kernel */
			if (ifa->ifa_flags & (IFA_F_TENTATIVE))
				continue;
#endif
			if (!(flags & NI_NODEADDR_FLAG_ALL) &&
			    ((subj_if && *subj_if) ? (ifa->ifa_ifindex != *subj_if) :
						     (ifa->ifa_ifindex != p->pktinfo.ipi6_ifindex)))
				continue;
			if (filter_ipv4addr((struct in_addr *)ifa->ifa_addr, flags))
				continue;

			if (addrs0 + 1 >= ((MAX_REPLY_SIZE - sizeof(struct icmp6_nodeinfo)) / (sizeof(uint32_t) + sizeof(struct in_addr)))) {
				flags |= NI_IPV4ADDR_FLAG_TRUNCATE;
				break;
			}

			addrs0++;
			if (!(ifa->ifa_flags & IFA_F_DEPRECATED))
				paddrs0++;
		}

		p->reply.ni_type = ICMP6_NI_REPLY;
		p->reply.ni_code = ICMP6_NI_SUCCESS;
		p->reply.ni_cksum = 0;
		p->reply.ni_qtype = htons(NI_QTYPE_IPV4ADDR);
		p->reply.ni_flags = flags & NI_IPV4ADDR_FLAG_ALL;

		/* pass 2: store addresses */
		p->replydatalen = (sizeof(uint32_t)+sizeof(struct in_addr)) * addrs0;
		p->replydata = addrs0 ? ni_malloc(p->replydatalen) : NULL;

		if (p->replydatalen && !p->replydata) {
			p->reply.ni_flags |= NI_NODEADDR_FLAG_TRUNCATE;
			addrs0 = paddrs0 = 0;
		}

		for (ifa = ifa0, addrs = 0; 
		     ifa && addrs < addrs0; 
		     ifa = ifa->ifa_next) {
			char *cp;
			uint32_t ttl;

			if (!ifa->ifa_addr)
				continue;
#if 1	/* not used in kernel */
			if (ifa->ifa_flags & (IFA_F_TENTATIVE))
				continue;
#endif
			if (!(flags & NI_NODEADDR_FLAG_ALL) &&
			    (ifa->ifa_ifindex != ifindex))
				continue;
			if (filter_ipv4addr((struct in_addr *)ifa->ifa_addr, flags))
				continue;	

#if ENABLE_TTL
			if (ifa->ifa_cacheinfo) {
				ttl = ifa->ifa_cacheinfo->ifa_valid > 0x7fffffff ? 
				      htonl(0x7fffffff) : htonl(ifa->ifa_cacheinfo->ifa_valid);
			} else {
				ttl = 0;	/*XXX*/
			}
#else
			ttl = 0;
#endif

			cp = (p->replydata +
			      (sizeof(uint32_t)+sizeof(struct in_addr)) * (ifa->ifa_flags & IFA_F_DEPRECATED ? paddrs0+daddrs : paddrs));
			memcpy(cp, &ttl, sizeof(ttl));
			memcpy(cp + sizeof(ttl), ifa->ifa_addr, sizeof(struct in_addr));

			addrs++;
			if (ifa->ifa_flags & IFA_F_DEPRECATED)
				daddrs++;
			else
				paddrs++;
		}
	}

	ni_freeifaddrs(ifa0);
	return 0;
}



File: /ninfod\ninfod_core.c
/* $USAGI: ninfod_core.c,v 1.29 2003-07-16 09:49:01 yoshfuji Exp $ */
/*
 * Copyright (C) 2002 USAGI/WIDE Project.
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the project nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */
/*
 * Author:
 * 	YOSHIFUJI Hideaki <yoshfuji@linux-ipv6.org>
 */

#if HAVE_CONFIG_H
#include "config.h"
#endif

#if HAVE_SYS_TYPES_H
# include <sys/types.h>
#endif
#if STDC_HEADERS
# include <stdio.h>
# include <stdlib.h>
# include <stddef.h>
#else
# if HAVE_STDLIB_H
#  include <stdlib.h>
# endif
#endif
#if ENABLE_THREADS && HAVE_PTHREAD_H
# include <pthread.h>
#endif
#if HAVE_STRING_H
# if !STDC_HEADERS && HAVE_MEMORY_H
#  include <memory.h>
# endif
# include <string.h>
#endif
#if HAVE_STRINGS_H
# include <strings.h>
#endif
#if HAVE_INTTYPES_H
# include <inttypes.h>
#else
# if HAVE_STDINT_H
#  include <stdint.h>
# endif
#endif
#if HAVE_UNISTD_H
# include <unistd.h>
#endif

#if TIME_WITH_SYS_TIME   
# include <sys/time.h>  
# include <time.h>
#else
# if HAVE_SYS_TIME_H     
#  include <sys/time.h>
# else                
#  include <time.h>
# endif                  
#endif                   

#if HAVE_SYS_UIO_H
#include <sys/uio.h>
#endif

#if HAVE_NETINET_IN_H
# include <netinet/in.h>
#endif

#if HAVE_NETINET_ICMP6_H
# include <netinet/icmp6.h>
#endif
#ifndef HAVE_STRUCT_ICMP6_NODEINFO
# include "icmp6_nodeinfo.h"
#endif

#if HAVE_NETDB_H
# include <netdb.h>
#endif
#include <errno.h>

#if HAVE_SYSLOG_H
# include <syslog.h>
#endif

#include "ninfod.h"

#ifndef offsetof
# define offsetof(aggregate,member)	((size_t)&((aggregate *)0)->member)
#endif

#define ARRAY_SIZE(a)		(sizeof(a) / sizeof(a[0]))

/* ---------- */
/* ID */
static char *RCSID __attribute__ ((unused)) = "$USAGI: ninfod_core.c,v 1.29 2003-07-16 09:49:01 yoshfuji Exp $";

/* Variables */
int initialized = 0;

#if ENABLE_THREADS && HAVE_LIBPTHREAD
pthread_attr_t pattr;
#endif

static uint32_t suptypes[(MAX_SUPTYPES+31)>>5];
static size_t suptypes_len;

/* ---------- */
struct subjinfo {
	uint8_t	code;
	char	*name;
	int	(*checksubj)(CHECKANDFILL_ARGS);
	int	(*init)(INIT_ARGS);
};

static struct subjinfo subjinfo_table [] = {
	[ICMP6_NI_SUBJ_IPV6] = {
		.code = ICMP6_NI_SUBJ_IPV6,
		.name = "IPv6",
		//.init = init_nodeinfo_ipv6addr,
		.checksubj = pr_nodeinfo_ipv6addr,
	},
	[ICMP6_NI_SUBJ_FQDN] = {
		.code = ICMP6_NI_SUBJ_FQDN,
		.name = "FQDN",
		//.init = init_nodeinfo_nodename,
		.checksubj = pr_nodeinfo_nodename,
	},
	[ICMP6_NI_SUBJ_IPV4] = {
		.code = ICMP6_NI_SUBJ_IPV4,
		.name = "IPv4",
		//.init = init_nodeinfo_ipv4addr,
		.checksubj = pr_nodeinfo_ipv4addr,
	},
};

static struct subjinfo subjinfo_null = {
	.name = "null",
	.checksubj = pr_nodeinfo_noop,
};

static __inline__ struct subjinfo *subjinfo_lookup(int code)
{
	if (code >= ARRAY_SIZE(subjinfo_table))
		return NULL;
	if (subjinfo_table[code].name == NULL)
		return NULL;
	return &subjinfo_table[code];
}

/* ---------- */
#define QTYPEINFO_F_RATELIMIT	0x1

struct qtypeinfo {
	uint16_t qtype;
	char	*name;
	int	(*getreply)(CHECKANDFILL_ARGS);
	void	(*init)(INIT_ARGS);
	int	flags;
};

static struct qtypeinfo qtypeinfo_table[] = {
	[NI_QTYPE_NOOP]		= {
		.qtype = NI_QTYPE_NOOP,
		.name = "NOOP",
		.getreply = pr_nodeinfo_noop,
	},
#if ENABLE_SUPTYPES
	[NI_QTYPE_SUPTYPES]	= {
		.qtype = NI_QTYPE_SUPTYPES,
		.name = "SupTypes",
		.getreply = pr_nodeinfo_suptypes,
		.init = init_nodeinfo_suptypes,
	},
#endif
	[NI_QTYPE_DNSNAME]	= {
		.qtype = NI_QTYPE_DNSNAME,
		.name = "DnsName",
		.getreply = pr_nodeinfo_nodename,
		.init = init_nodeinfo_nodename,
	},
	[NI_QTYPE_NODEADDR]	= {
		.qtype = NI_QTYPE_NODEADDR,
		.name = "NodeAddr",
		.getreply = pr_nodeinfo_ipv6addr,
		.init = init_nodeinfo_ipv6addr,
	},
	[NI_QTYPE_IPV4ADDR]	= {
		.qtype = NI_QTYPE_IPV4ADDR,
		.name = "IPv4Addr",
		.getreply = pr_nodeinfo_ipv4addr,
		.init = init_nodeinfo_ipv4addr,
	},
};

static struct qtypeinfo qtypeinfo_unknown = {
	.name = "unknown",
	.getreply = pr_nodeinfo_unknown,
	.flags = QTYPEINFO_F_RATELIMIT,
};

static struct qtypeinfo qtypeinfo_refused = {
	.name = "refused",
	.getreply = pr_nodeinfo_refused,
	.flags = QTYPEINFO_F_RATELIMIT,
};

static __inline__ struct qtypeinfo *qtypeinfo_lookup(int qtype)
{
	if (qtype >= ARRAY_SIZE(qtypeinfo_table))
		return &qtypeinfo_unknown;
	if (qtypeinfo_table[qtype].name == NULL)
		return &qtypeinfo_unknown;
	return &qtypeinfo_table[qtype];
}

/* ---------- */
/* noop */
int pr_nodeinfo_noop(CHECKANDFILL_ARGS)
{
	DEBUG(LOG_DEBUG, "%s()\n", __func__);

	if (subjlen) {
		DEBUG(LOG_WARNING,
		      "%s(): invalid subject length(%zu)\n",
		      __func__, subjlen);
		return 1;
	}

	if (reply) {
		p->reply.ni_type = ICMP6_NI_REPLY;
		p->reply.ni_code = ICMP6_NI_SUCCESS;
		p->reply.ni_cksum = 0;
		p->reply.ni_qtype = htons(NI_QTYPE_NOOP);
		p->reply.ni_flags = flags;
	}

	if (subj_if)
		*subj_if = 0;

	return 0;
}

#if ENABLE_SUPTYPES
/* suptypes */
int pr_nodeinfo_suptypes(CHECKANDFILL_ARGS)
{
	DEBUG(LOG_DEBUG, "%s()\n", __func__);

	if (subjlen) {
		DEBUG(LOG_WARNING, "%s(): invalid subject length(%zu)\n",
		      __func__, subjlen);
		return 1;
	}

	if (reply) {
		p->reply.ni_type = ICMP6_NI_REPLY;
		p->reply.ni_code = ICMP6_NI_SUCCESS;
		p->reply.ni_cksum = 0;
		p->reply.ni_qtype = htons(NI_QTYPE_SUPTYPES);
		p->reply.ni_flags = flags&~NI_SUPTYPE_FLAG_COMPRESS;
		
		p->replydatalen = suptypes_len<<2;
		p->replydata = ni_malloc(p->replydatalen);
		if (p->replydata == NULL) {
			p->replydatalen = -1;
			return -1;	/*XXX*/
		}

		memcpy(p->replydata, suptypes, p->replydatalen);
	}
	return 0;
}

void init_nodeinfo_suptypes(INIT_ARGS)
{
	size_t w, b;
	int i;

	if (!forced && initialized)
		return;

	memset(suptypes, 0, sizeof(suptypes));
	suptypes_len = 0;

	for (i=0; i < ARRAY_SIZE(qtypeinfo_table); i++) {
		unsigned short qtype;

		if (qtypeinfo_table[i].name == NULL)
			continue;
		qtype = qtypeinfo_table[i].qtype;
		w = qtype>>5;
		b = qtype&0x1f;
		if (w >= ARRAY_SIZE(suptypes)) {
			/* This is programming error. */
			DEBUG(LOG_ERR, "Warning: Too Large Supported Types\n");
			exit(1);
		}
		suptypes[w] |= htonl(1<<b);

		if (suptypes_len < w)
			suptypes_len = w;
	}
	suptypes_len++;
}
#endif

/* ---------- */
/* unknown qtype response */
int pr_nodeinfo_unknown(CHECKANDFILL_ARGS)
{
	if (!reply)
		return -1;	/*???*/

	p->reply.ni_type = ICMP6_NI_REPLY;
	p->reply.ni_code = ICMP6_NI_UNKNOWN;
	p->reply.ni_cksum = 0;
	//p->reply.ni_qtype = 0;
	p->reply.ni_flags = flags;

	p->replydata = NULL;
	p->replydatalen = 0;

	return 0;
}

/* refused response */
int pr_nodeinfo_refused(CHECKANDFILL_ARGS)
{
	if (!reply)
		return -1;	/*???*/

	p->reply.ni_type = ICMP6_NI_REPLY;
	p->reply.ni_code = ICMP6_NI_REFUSED;
	p->reply.ni_cksum = 0;
	//p->reply.ni_qtype = 0;
	p->reply.ni_flags = flags;

	p->replydata = NULL;
	p->replydatalen = 0;

	return 0;
}

/* ---------- */
/* Policy */
static int ni_policy(struct packetcontext *p)
{
	const struct in6_addr *saddr = &((const struct sockaddr_in6 *)&p->addr)->sin6_addr;

	/*
	 * >0: reply
	 *  0: refused
	 * <0: discard
	 */

	/* Default policy is to refuse queries from
	 * non-local addresses; loopback, link-local or
	 * site-local are okay
	 */
	if (!(IN6_IS_ADDR_LINKLOCAL(saddr) ||
	      IN6_IS_ADDR_SITELOCAL(saddr) ||
	      IN6_IS_ADDR_LOOPBACK(saddr)))
		return 0;
	return 1;
}

/* ---------- */
void init_core(int forced)
{
	int i;

	DEBUG(LOG_DEBUG, "%s()\n", __func__);

	if (!initialized || forced) {
		struct timeval tv;
		unsigned int seed = 0;
		pid_t pid;

		if (gettimeofday(&tv, NULL) < 0) {
			DEBUG(LOG_WARNING, "%s(): failed to gettimeofday()\n", __func__);
		} else {
			seed = (tv.tv_usec & 0xffffffff);
		}

		pid = getpid();
		seed ^= (((unsigned long)pid) & 0xffffffff);

		srand(seed);

#if ENABLE_THREADS && HAVE_LIBPTHREAD
		if (initialized)
			pthread_attr_destroy(&pattr);

		pthread_attr_init(&pattr);
		pthread_attr_setdetachstate(&pattr, PTHREAD_CREATE_DETACHED);
#endif
	}

	for (i=0; i < ARRAY_SIZE(subjinfo_table); i++) {
		if (subjinfo_table[i].name == NULL)
			continue;
		if (subjinfo_table[i].init)
			subjinfo_table[i].init(forced);
	}

	for (i=0; i < ARRAY_SIZE(qtypeinfo_table); i++) {
		if (qtypeinfo_table[i].name == NULL)
			continue;
		if (qtypeinfo_table[i].init)
			qtypeinfo_table[i].init(forced);
	}

	initialized = 1;

	return;
}

#if ENABLE_THREADS && HAVE_LIBPTHREAD
static void *ni_send_thread(void *data)
{
	int ret;
	DEBUG(LOG_DEBUG, "%s(): thread=%ld\n", __func__, pthread_self());
	ret = ni_send(data);
	DEBUG(LOG_DEBUG, "%s(): thread=%ld => %d\n", __func__, pthread_self(), ret);
	return NULL;
}
#else
static int ni_send_fork(struct packetcontext *p)
{
	pid_t child = fork();
	if (child < 0)
		return -1;
	if (child == 0) {
		pid_t grandchild = fork();
		if (grandchild < 0)
			exit(1);
		if (grandchild == 0) {
			int ret;
			DEBUG(LOG_DEBUG, "%s(): worker=%d\n",
			      __func__, getpid());
			ret = ni_send(p);
			DEBUG(LOG_DEBUG, "%s(): worker=%d => %d\n",
			      __func__, getpid(), ret);
			exit(ret > 0 ? 1 : 0);
		}
		ni_free(p->replydata);
		ni_free(p);
		exit(0);
	} else {
		waitpid(child, NULL, 0);
		ni_free(p->replydata);
		ni_free(p);
	}
	return 0;
}
#endif

static int ni_ratelimit(void)
{
	static struct timeval last;
	struct timeval tv, sub;

	if (gettimeofday(&tv, NULL) < 0) {
		DEBUG(LOG_WARNING, "%s(): gettimeofday(): %s\n",
		      __func__, strerror(errno));
		return -1;
	}

	if (!timerisset(&last)) {
		last = tv;
		return 0;
	}

	timersub(&tv, &last, &sub);

	if (sub.tv_sec < 1)
		return 1;

	last = tv;
	return 0;
}

int pr_nodeinfo(struct packetcontext *p)
{
	struct icmp6_nodeinfo *query = (struct icmp6_nodeinfo *)p->query;

	char *subject = (char *)(query + 1);
	size_t subjlen;
	struct subjinfo *subjinfo;
	struct qtypeinfo *qtypeinfo;
	int replyonsubjcheck = 0;
	unsigned int subj_if;
#if ENABLE_DEBUG
	char printbuf[128];
	int i;
	char *cp;
#endif
#if ENABLE_THREADS && HAVE_PTHREAD_H
	pthread_t thread;
#endif
	int rc;

	/* Step 0: Check destination address
	 *		discard non-linklocal multicast
	 *		discard non-nigroup multicast address(?)
	 */
	if (IN6_IS_ADDR_MULTICAST(&p->pktinfo.ipi6_addr)) {
		if (!IN6_IS_ADDR_MC_LINKLOCAL(&p->pktinfo.ipi6_addr)) {
			DEBUG(LOG_WARNING,
			      "Destination is non-link-local multicast address.\n");
			ni_free(p);
			return -1;
		}
#if 0
		/* Do not discard NI Queries to multicast address
		 * other than its own NI Group Address(es) by default.
		 */
		if (!check_nigroup(&p->pktinfo.ipi6_addr)) {
			DEBUG(LOG_WARNING,
			      "Destination is link-local multicast address other than "
			      "NI Group address.\n");
			ni_free(p);
			return -1;
		}
#endif
	}

	/* Step 1: Check length */
	if (p->querylen < sizeof(struct icmp6_nodeinfo)) {
		DEBUG(LOG_WARNING, "Query too short\n");
		ni_free(p);
		return -1;
	}

#if ENABLE_DEBUG
	cp = printbuf;
	for (i = 0; i < sizeof(query->icmp6_ni_nonce); i++) {
		cp += sprintf(cp, " %02x", query->icmp6_ni_nonce[i]);
	}
	DEBUG(LOG_DEBUG, "%s(): qtype=%d, flags=0x%04x, nonce[] = {%s }\n",
	      __func__,
	      ntohs(query->ni_qtype), ntohs(query->ni_flags), printbuf);
#endif

	subjlen = p->querylen - sizeof(struct icmp6_nodeinfo);

	/* Step 2: Check Subject Code */
	switch(htons(query->ni_qtype)) {
	case NI_QTYPE_NOOP:
	case NI_QTYPE_SUPTYPES:
		if (query->ni_code != ICMP6_NI_SUBJ_FQDN) {
			DEBUG(LOG_WARNING,
			      "%s(): invalid/unknown code %u\n",
			      __func__, query->ni_code);
			subjlen = 0;
		}
		subjinfo = &subjinfo_null;
		break;
	default:
		subjinfo = subjinfo_lookup(query->ni_code);
		if (!subjinfo) {
			DEBUG(LOG_WARNING,
			      "%s(): unknown code %u\n",
			      __func__, query->ni_code);
			ni_free(p);
			return -1;
		}
	}

	/* Step 3: Lookup Qtype */
	qtypeinfo = qtypeinfo_lookup(ntohs(query->ni_qtype));

	/* Step 4: Check Subject
	 *         (And fill reply if it is available now)
	 */
	if (qtypeinfo->getreply == subjinfo->checksubj)
		replyonsubjcheck = 1;

	if (subjinfo->checksubj(p,
				subject, subjlen,
				query->ni_flags,
				replyonsubjcheck ? NULL : &subj_if,
				replyonsubjcheck)) {
		if (p->replydatalen < 0) {
			DEBUG(LOG_WARNING,
			      "failed to make reply: %s\n",
			      strerror(errno));
		}
		ni_free(p);
		return -1;
	}

	/* XXX: Step 5: Check the policy */
	rc = ni_policy(p);
	if (rc <= 0) {
		ni_free(p->replydata);
		p->replydata = NULL;
		p->replydatalen = 0;
		if (rc < 0) {
			DEBUG(LOG_WARNING, "Ignored by policy.\n");
			ni_free(p);
			return -1;
		}
		DEBUG(LOG_WARNING, "Refused by policy.\n");
		replyonsubjcheck = 0;
		qtypeinfo = &qtypeinfo_refused;
	}

	/* Step 6: Fill the reply if not yet done */
	if (!replyonsubjcheck) {
		if (qtypeinfo->getreply(p,
					NULL, 0,
					query->ni_flags,
					&subj_if,
					1)) {
			if (p->replydatalen) {
				DEBUG(LOG_WARNING,
				      "failed to make reply: %s\n",
				      strerror(errno));
			}
			ni_free(p);
			return -1;
		}
	}

	/* Step 7: Rate Limit */
	if (qtypeinfo->flags&QTYPEINFO_F_RATELIMIT &&
	    ni_ratelimit()) {
		ni_free(p->replydata);
		ni_free(p);
		return -1;
	}

	/* Step 8: Fill Qtype / Nonce */
	p->reply.ni_qtype = query->ni_qtype;
	memcpy(p->reply.icmp6_ni_nonce, query->icmp6_ni_nonce, sizeof(p->reply.icmp6_ni_nonce));

	/* Step 9: Source address selection */
	if (IN6_IS_ADDR_MULTICAST(&p->pktinfo.ipi6_addr)) {
		/* if query was sent to multicast address,
		 * use source address selection in kernel.
		 * XXX: anycast?
		 */
		memset(&p->pktinfo.ipi6_addr, 0, sizeof(p->pktinfo.ipi6_addr));

	 	/* Random Delay between zero and MAX_ANYCAST_DELAY_TIME is
		 * required if query was sent to anycast or multicast address.
		 */
		p->delay = (int) (MAX_ANYCAST_DELAY_TIME*rand()/(RAND_MAX+1.0));
	} else {
		p->delay = 0;
	}

	/* Step 10: Send the reply
	 * XXX: with possible random delay */
#if ENABLE_THREADS && HAVE_LIBPTHREAD
	/* ni_send_thread() frees p */
	if (pthread_create(&thread, &pattr, ni_send_thread, p)) {
		ni_free(p->replydata);
		ni_free(p);
		return -1;
	}
#else
	/* ni_send_fork() frees p */
	if (ni_send_fork(p)) {
		ni_free(p->replydata);
		ni_free(p);
		return -1;
	}
#endif

	return 0;
}



File: /ninfod\ninfod_name.c
/* $USAGI: ninfod_name.c,v 1.15 2003-01-11 14:33:28 yoshfuji Exp $ */
/*
 * Copyright (C) 2002 USAGI/WIDE Project.
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the project nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */
/*
 * Author:
 * 	YOSHIFUJI Hideaki <yoshfuji@linux-ipv6.org>
 */

#if HAVE_CONFIG_H
#include "config.h"
#endif

#if HAVE_SYS_TYPES_H
# include <sys/types.h>
#endif
#if STDC_HEADERS
# include <stdio.h>
# include <stdlib.h>
# include <stddef.h>
# include <ctype.h>
#else
# if HAVE_STDLIB_H
#  include <stdlib.h>
# endif
#endif
#if HAVE_STRING_H
# if !STDC_HEADERS && HAVE_MEMORY_H
#  include <memory.h>
# endif
# include <string.h>
#endif
#if HAVE_STRINGS_H
# include <strings.h>
#endif
#if HAVE_INTTYPES_H
# include <inttypes.h>
#else
# if HAVE_STDINT_H
#  include <stdint.h>
# endif
#endif
#if HAVE_UNISTD_H
# include <unistd.h>
#endif

#if TIME_WITH_SYS_TIME   
# include <sys/time.h>  
# include <time.h>
#else
# if HAVE_SYS_TIME_H     
#  include <sys/time.h>
# else                
#  include <time.h>
# endif                  
#endif                   

#if HAVE_SYS_UIO_H
#include <sys/uio.h>
#endif

#include <sys/socket.h>

#if HAVE_NETINET_IN_H
# include <netinet/in.h>
#endif

#if HAVE_NETINET_ICMP6_H
# include <netinet/icmp6.h>
#endif
#ifndef HAVE_STRUCT_ICMP6_NODEINFO
# include "icmp6_nodeinfo.h"
#endif

#include <arpa/inet.h>

#if defined(HAVE_GNUTLS_OPENSSL_H)
# include <gnutls/openssl.h>
#elif defined(HAVE_OPENSSL_MD5_H)
# include <openssl/md5.h>
#endif

#if HAVE_SYS_UTSNAME_H
# include <sys/utsname.h>
#endif
#if HAVE_NETDB_H
# include <netdb.h>
#endif
#include <errno.h>

#if HAVE_SYSLOG_H
# include <syslog.h>
#endif

#include "ninfod.h"

#ifndef offsetof
# define offsetof(aggregate,member)	((size_t)&((aggregate *)0)->member)
#endif

/* Hmm,,, */
#ifndef IPV6_JOIN_GROUP
# define IPV6_JOIN_GROUP	IPV6_ADD_MEMBERSHIP
# define IPV6_LEAVE_GROUP	IPV6_DROP_MEMBERSHIP
#endif

/* ---------- */
/* ID */
static char *RCSID __attribute__ ((unused)) = "$USAGI: ninfod_name.c,v 1.15 2003-01-11 14:33:28 yoshfuji Exp $";

/* Variables */
static struct utsname utsname;
static char *uts_nodename = utsname.nodename;

char nodename[MAX_DNSNAME_SIZE];
static size_t nodenamelen;

static struct ipv6_mreq nigroup;

/* ---------- */
/* Functions */
int check_nigroup(const struct in6_addr *addr)
{
	return IN6_IS_ADDR_MULTICAST(&nigroup.ipv6mr_multiaddr) &&
	       IN6_ARE_ADDR_EQUAL(&nigroup.ipv6mr_multiaddr, addr);
}

static int encode_dnsname(const char *name, 
			  char *buf, size_t buflen, 
			  int fqdn)
{
	size_t namelen;
	int i;

	if (buflen < 0)
		return -1;

	namelen = strlen(name);
	if (namelen == 0)
		return 0;
	if (namelen > 255 || buflen < namelen+1)
		return -1;

	i = 0;
	while(i <= namelen) {
		const char *e;
		int llen, ii;

		e = strchr(&name[i], '.');
		if (e == NULL)
			e = name + namelen;
		llen = e - &name[i];
		if (llen == 0) {
			if (*e)
				return -1;
			if (fqdn < 0)
				return -1;
			fqdn = 1;
			break;
		}
		if (llen >= 0x40)
			return -1;
		buf[i] = llen;
		for (ii = 0; ii < llen; ii++) {
			if (!isascii(name[i+ii]))
				return -1;
			if (ii == 0 || ii == llen-1) {
				if (!isalpha(name[i+ii]) && !isdigit(name[i+ii]))
					return -1;
			} else if (!isalnum(name[i+ii]) && name[i+ii] != '-')
				return -1;
			buf[i+ii+1] = isupper(name[i+ii]) ? tolower(name[i+ii]) : name[i+ii];
		}
		i += llen + 1;
	}
	if (buflen < i + 1 + !(fqdn > 0))
		return -1;
	buf[i++] = 0;
	if (!(fqdn > 0))
		buf[i++] = 0;
	return i;
}

static int compare_dnsname(const char *s, size_t slen,
			   const char *n, size_t nlen)
{
	const char *s0 = s, *n0 = n;
	int done = 0, retcode = 0;
	if (slen < 1 || nlen < 1)
		return -1;	/* invalid length */
	/* simple case */
	if (slen == nlen && memcmp(s, n, slen) == 0)
		return 0;
	if (*(s0 + slen - 1) || *(n0 + nlen - 1))
		return -1;	/* invalid termination */
	while (s < s0 + slen && n < n0 + nlen) {
		if (*s >= 0x40 || *n >= 0x40)
			return -1;	/* DNS compression is not allowed here */
		if (s + *s + 1 > s0 + slen || n + *n + 1 > n0 + nlen)
			return -1;	/* overrun */
		if (*s == '\0') {
			if (s == s0 + slen - 1)
				break;	/* FQDN */
			else if (s + 1 == s0 + slen - 1)
				return retcode;	/* truncated */
			else
				return -1;	/* more than one subject */
		}
		if (!done) {
			if (*n == '\0') {
				if (n == n0 + nlen - 1) {
					done = 1;	/* FQDN */
				} else if (n + 1 == n0 + nlen - 1) {
					retcode = 1;	// trunc
					done = 1;
				} else
					return -1;
			} else {
				if (*s != *n) {
					done = 1;
					retcode = 1;
				} else {
					if (memcmp(s+1, n+1, *s)) {
						done = 1;
						retcode = 1;
					}
				}
			}
		}
		s += *s + 1;
		n += done ? 0 : (*n + 1);
	}
	return retcode;
}

static int nodeinfo_group(const char *dnsname, int namelen, 
			  struct in6_addr *nigroup)
{
	MD5_CTX ctxt;
	unsigned char digest[16];

	if (!dnsname || !nigroup)
		return -1;

	MD5_Init(&ctxt);
	MD5_Update(&ctxt, dnsname, *dnsname);
	MD5_Final(digest, &ctxt);

#ifdef s6_addr32
	nigroup->s6_addr32[0] = htonl(0xff020000);
	nigroup->s6_addr32[1] = 0;
	nigroup->s6_addr32[2] = htonl(0x00000002);
#else
	memset(nigroup, 0, sizeof(*nigroup));
	nigroup->s6_addr[ 0] = 0xff;
	nigroup->s6_addr[ 1] = 0x02;
	nigroup->s6_addr[11] = 0x02;
#endif
	memcpy(&nigroup->s6_addr[12], digest, 4);

	return 0;
}

/* ---------- */
void init_nodeinfo_nodename(int forced)
{
	struct utsname newname;
	int len;
	int changed = 0;

	DEBUG(LOG_DEBUG, "%s()\n", __func__);

	uname(&newname);
	changed = strcmp(newname.nodename, utsname.nodename);

	if (!changed && !forced)
		return;

	memcpy(&utsname, &newname, sizeof(newname));

	/* leave old group */
	if ((changed || forced) && !IN6_IS_ADDR_UNSPECIFIED(&nigroup.ipv6mr_multiaddr)) {
		if (setsockopt(sock, IPPROTO_IPV6, IPV6_LEAVE_GROUP, &nigroup, sizeof(nigroup)) < 0) {
#if ENABLE_DEBUG
			char niaddrbuf[INET6_ADDRSTRLEN];
			if (inet_ntop(AF_INET6, &nigroup, niaddrbuf, sizeof(niaddrbuf)) == NULL)
				strcpy(niaddrbuf, "???");
#endif
			DEBUG(LOG_WARNING,
			      "%s(): failed to leave group %s.\n",
			      __func__, niaddrbuf);
			memset(&nigroup, 0, sizeof(nigroup));
		}
	}

	len = encode_dnsname(uts_nodename,
			     nodename, 
			     sizeof(nodename),
			     0);

	/* setup ni reply */
	nodenamelen = len > 0 ? len : 0;

	/* setup ni group */
	if (changed || forced) {
		if (nodenamelen) {
			memset(&nigroup, 0, sizeof(nigroup));
			nodeinfo_group(nodename, len, &nigroup.ipv6mr_multiaddr);
			nigroup.ipv6mr_interface = 0;
			if (setsockopt(sock, IPPROTO_IPV6, IPV6_JOIN_GROUP, &nigroup, sizeof(nigroup)) < 0) {
#if ENABLE_DEBUG
				char niaddrbuf[INET6_ADDRSTRLEN];
				if (inet_ntop(AF_INET6, &nigroup, niaddrbuf, sizeof(niaddrbuf)) == NULL)
					strcpy(niaddrbuf, "???");
#endif
				DEBUG(LOG_WARNING,
				      "%s(): failed to join group %s.\n",
				      __func__, niaddrbuf);
				memset(&nigroup, 0, sizeof(nigroup));
			}
		} else {
			memset(&nigroup, 0, sizeof(nigroup));
		}
	}

	return;
}

/* ---------- */
/* nodename */
int pr_nodeinfo_nodename(CHECKANDFILL_ARGS)
{
	DEBUG(LOG_DEBUG, "%s()\n", __func__);

	if (subject) {
		if (!nodenamelen ||
		    compare_dnsname(subject, subjlen, 
				    nodename, 
				    nodenamelen))
			return 1;
		if (subj_if)
			*subj_if = p->pktinfo.ipi6_ifindex;
	}

	if (reply) {
		uint32_t ttl = 0;

		p->reply.ni_type = ICMP6_NI_REPLY;
		p->reply.ni_code = ICMP6_NI_SUCCESS;
		p->reply.ni_cksum = 0;
		p->reply.ni_qtype = htons(NI_QTYPE_DNSNAME);
		p->reply.ni_flags = 0;

		p->replydatalen = nodenamelen ? sizeof(ttl)+nodenamelen : 0;
		p->replydata = nodenamelen ? ni_malloc(p->replydatalen) : NULL;
		if (p->replydata) {
			memcpy(p->replydata, &ttl, sizeof(ttl));
			memcpy(p->replydata + sizeof(ttl), &nodename, nodenamelen);
		}
	}

	return 0;
}



File: /ninfod\ni_ifaddrs.c
/* $USAGI: ni_ifaddrs.c,v 1.8 2007-10-11 06:25:21 yoshfuji Exp $ */
/*
 * Copyright (C) 2002 USAGI/WIDE Project.
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the project nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

/* reformatted by indent -kr -i8 -l 1000 */
/* USAGI: ifaddrs.c,v 1.18 2002/03/06 01:50:46 yoshfuji Exp */

/**************************************************************************
 * ifaddrs.c
 * Copyright (C)2000 Hideaki YOSHIFUJI, All Rights Reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the author nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#include "config.h"

#include <string.h>
#include <time.h>
#include <malloc.h>
#include <errno.h>
#include <unistd.h>

#include <sys/socket.h>
#include <asm/types.h>
#include <linux/netlink.h>
#include <linux/rtnetlink.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netpacket/packet.h>
#include <net/ethernet.h>	/* the L2 protocols */
#include <sys/uio.h>
#include <net/if.h>
#include <net/if_arp.h>
#include "ni_ifaddrs.h"
#include <netinet/in.h>

#ifdef _USAGI_LIBINET6
#include "libc-compat.h"
#endif

//#define IFA_LOCAL	IFA_LOCAL

static const char *RCSID __attribute__ ((unused)) = "$USAGI: ni_ifaddrs.c,v 1.8 2007-10-11 06:25:21 yoshfuji Exp $ based on USAGI: ifaddrs.c,v 1.18 2002/03/06 01:50:46 yoshfuji Exp";

/* ====================================================================== */
struct nlmsg_list {
	struct nlmsg_list *nlm_next;
	struct nlmsghdr *nlh;
	int size;
	time_t seq;
};

#ifndef IFA_LOCAL
struct rtmaddr_ifamap {
	void *address;
	void *local;
	void *broadcast;
	int address_len;
	int local_len;
	int broadcast_len;
};
#endif

/* ====================================================================== */
static int nl_sendreq(int sd, int request, int flags, int *seq)
{
	char reqbuf[NLMSG_ALIGN(sizeof(struct nlmsghdr)) + NLMSG_ALIGN(sizeof(struct rtgenmsg))];
	struct sockaddr_nl nladdr;
	struct nlmsghdr *req_hdr;
	struct rtgenmsg *req_msg;
	time_t t = time(NULL);

	if (seq)
		*seq = t;
	memset(&reqbuf, 0, sizeof(reqbuf));
	req_hdr = (struct nlmsghdr *) reqbuf;
	req_msg = (struct rtgenmsg *) NLMSG_DATA(req_hdr);
	req_hdr->nlmsg_len = NLMSG_LENGTH(sizeof(*req_msg));
	req_hdr->nlmsg_type = request;
	req_hdr->nlmsg_flags = flags | NLM_F_REQUEST;
	req_hdr->nlmsg_pid = 0;
	req_hdr->nlmsg_seq = t;
	req_msg->rtgen_family = AF_UNSPEC;
	memset(&nladdr, 0, sizeof(nladdr));
	nladdr.nl_family = AF_NETLINK;
	return (sendto(sd, (void *) req_hdr, req_hdr->nlmsg_len, 0, (struct sockaddr *) &nladdr, sizeof(nladdr)));
}

static int nl_recvmsg(int sd, int request, int seq, void *buf, size_t buflen, int *flags)
{
	struct msghdr msg;
	struct iovec iov = { buf, buflen };
	struct sockaddr_nl nladdr;
	int read_len;

	for (;;) {
		msg.msg_name = (void *) &nladdr;
		msg.msg_namelen = sizeof(nladdr);
		msg.msg_iov = &iov;
		msg.msg_iovlen = 1;
		msg.msg_control = NULL;
		msg.msg_controllen = 0;
		msg.msg_flags = 0;
		read_len = recvmsg(sd, &msg, 0);
		if ((read_len < 0 && errno == EINTR)
		    || (msg.msg_flags & MSG_TRUNC))
			continue;
		if (flags)
			*flags = msg.msg_flags;
		break;
	}
	return read_len;
}

static int nl_getmsg(int sd, int request, int seq, struct nlmsghdr **nlhp, int *done)
{
	struct nlmsghdr *nh;
	size_t bufsize = 65536, lastbufsize = 0;
	void *buff = NULL;
	int result = 0, read_size;
	int msg_flags;
	pid_t pid = getpid();
	for (;;) {
		void *newbuff = realloc(buff, bufsize);
		if (newbuff == NULL || bufsize < lastbufsize) {
			free(newbuff);
			result = -1;
			break;
		}
		buff = newbuff;
		result = read_size = nl_recvmsg(sd, request, seq, buff, bufsize, &msg_flags);
		if (read_size < 0 || (msg_flags & MSG_TRUNC)) {
			lastbufsize = bufsize;
			bufsize *= 2;
			continue;
		}
		if (read_size == 0)
			break;
		nh = (struct nlmsghdr *) buff;
		for (nh = (struct nlmsghdr *) buff; NLMSG_OK(nh, read_size); nh = (struct nlmsghdr *) NLMSG_NEXT(nh, read_size)) {
			if (nh->nlmsg_pid != pid || nh->nlmsg_seq != seq)
				continue;
			if (nh->nlmsg_type == NLMSG_DONE) {
				(*done)++;
				break;	/* ok */
			}
			if (nh->nlmsg_type == NLMSG_ERROR) {
				struct nlmsgerr *nlerr = (struct nlmsgerr *) NLMSG_DATA(nh);
				result = -1;
				if (nh->nlmsg_len < NLMSG_LENGTH(sizeof(struct nlmsgerr)))
					errno = EIO;
				else
					errno = -nlerr->error;
				break;
			}
		}
		break;
	}
	if (result < 0)
		if (buff) {
			int saved_errno = errno;
			free(buff);
			buff = NULL;
			errno = saved_errno;
		}
	*nlhp = (struct nlmsghdr *) buff;
	return result;
}

static int nl_getlist(int sd, int seq, int request, struct nlmsg_list **nlm_list, struct nlmsg_list **nlm_end)
{
	struct nlmsghdr *nlh = NULL;
	int status;
	int done = 0;

	status = nl_sendreq(sd, request, NLM_F_ROOT | NLM_F_MATCH, &seq);
	if (status < 0)
		return status;
	if (seq == 0)
		seq = (int) time(NULL);
	while (!done) {
		status = nl_getmsg(sd, request, seq, &nlh, &done);
		if (status < 0)
			return status;
		if (nlh) {
			struct nlmsg_list *nlm_next = (struct nlmsg_list *) malloc(sizeof(struct nlmsg_list));
			if (nlm_next == NULL) {
				int saved_errno = errno;
				free(nlh);
				errno = saved_errno;
				status = -1;
			} else {
				nlm_next->nlm_next = NULL;
				nlm_next->nlh = (struct nlmsghdr *) nlh;
				nlm_next->size = status;
				nlm_next->seq = seq;
				if (*nlm_list == NULL) {
					*nlm_list = nlm_next;
					*nlm_end = nlm_next;
				} else {
					(*nlm_end)->nlm_next = nlm_next;
					*nlm_end = nlm_next;
				}
			}
		}
	}
	return status >= 0 ? seq : status;
}

/* ---------------------------------------------------------------------- */
static void free_nlmsglist(struct nlmsg_list *nlm0)
{
	struct nlmsg_list *nlm, *nlm_next;
	int saved_errno;
	if (!nlm0)
		return;
	saved_errno = errno;
	nlm = nlm0;
	while(nlm) {
		if(nlm->nlh)
			free(nlm->nlh);
		nlm_next = nlm->nlm_next;
		free(nlm);
		nlm = nlm_next;
	}
	errno = saved_errno;
}

static void free_data(void *data)
{
	int saved_errno = errno;
	if (data != NULL)
		free(data);
	errno = saved_errno;
}

/* ---------------------------------------------------------------------- */
static void nl_close(int sd)
{
	int saved_errno = errno;
	if (sd >= 0)
		close(sd);
	errno = saved_errno;
}

/* ---------------------------------------------------------------------- */
static int nl_open(void)
{
	struct sockaddr_nl nladdr;
	int sd;

	sd = socket(PF_NETLINK, SOCK_RAW, NETLINK_ROUTE);
	if (sd < 0)
		return -1;
	memset(&nladdr, 0, sizeof(nladdr));
	nladdr.nl_family = AF_NETLINK;
	if (bind(sd, (struct sockaddr *) &nladdr, sizeof(nladdr)) < 0) {
		nl_close(sd);
		return -1;
	}
	return sd;
}

/* ====================================================================== */
int ni_ifaddrs(struct ni_ifaddrs **ifap, sa_family_t family)
{
	int sd;
	struct nlmsg_list *nlmsg_list, *nlmsg_end, *nlm;
	/* - - - - - - - - - - - - - - - */
	int icnt;
	size_t dlen, xlen;
	uint32_t max_ifindex = 0;

	pid_t pid = getpid();
	int seq = 0;
	int result;
	int build;		/* 0 or 1 */

/* ---------------------------------- */
	/* initialize */
	icnt = dlen = xlen = 0;
	nlmsg_list = nlmsg_end = NULL;

	if (ifap)
		*ifap = NULL;

/* ---------------------------------- */
	/* open socket and bind */
	sd = nl_open();
	if (sd < 0)
		return -1;

/* ---------------------------------- */
	/* gather info */
	if ((seq = nl_getlist(sd, seq + 1, RTM_GETADDR, &nlmsg_list, &nlmsg_end)) < 0) {
		free_nlmsglist(nlmsg_list);
		nl_close(sd);
		return -1;
	}

/* ---------------------------------- */
	/* Estimate size of result buffer and fill it */
	for (build = 0; build <= 1; build++) {
		struct ni_ifaddrs *ifl = NULL, *ifa = NULL;
		struct nlmsghdr *nlh, *nlh0;
		void *data = NULL, *xdata = NULL;
		uint16_t *ifflist = NULL;
#ifndef IFA_LOCAL
		struct rtmaddr_ifamap ifamap;
#endif

		if (build) {
			ifa = data = calloc(1, NLMSG_ALIGN(sizeof(struct ni_ifaddrs[icnt]))
					    + dlen + xlen);
			if (ifap != NULL)
				*ifap = ifa;
			else {
				free_data(data);
				result = 0;
				break;
			}
			if (data == NULL) {
				free_data(data);
				result = -1;
				break;
			}
			ifl = NULL;
			data += NLMSG_ALIGN(sizeof(struct ni_ifaddrs)) * icnt;
			xdata = data + dlen;
			ifflist = xdata + xlen;
		}

		for (nlm = nlmsg_list; nlm; nlm = nlm->nlm_next) {
			int nlmlen = nlm->size;
			if (!(nlh0 = nlm->nlh))
				continue;
			for (nlh = nlh0; NLMSG_OK(nlh, nlmlen); nlh = NLMSG_NEXT(nlh, nlmlen)) {
				struct ifaddrmsg *ifam = NULL;
				struct rtattr *rta;

				size_t nlm_struct_size = 0;
				sa_family_t nlm_family = 0;
				uint32_t nlm_scope = 0, nlm_index = 0;
				unsigned int nlm_flags;
				size_t rtasize;

#ifndef IFA_LOCAL
				memset(&ifamap, 0, sizeof(ifamap));
#endif

				/* check if the message is what we want */
				if (nlh->nlmsg_pid != pid || nlh->nlmsg_seq != nlm->seq)
					continue;
				if (nlh->nlmsg_type == NLMSG_DONE) {
					break;	/* ok */
				}
				switch (nlh->nlmsg_type) {
				case RTM_NEWADDR:
					ifam = (struct ifaddrmsg *) NLMSG_DATA(nlh);
					nlm_struct_size = sizeof(*ifam);
					nlm_family = ifam->ifa_family;
					nlm_scope = ifam->ifa_scope;
					nlm_index = ifam->ifa_index;
					nlm_flags = ifam->ifa_flags;
					if (family && nlm_family != family)
						continue;
					if (build) {
						ifa->ifa_ifindex = nlm_index;
						ifa->ifa_flags = nlm_flags;
					}
					break;
				default:
					continue;
				}

				if (!build) {
					if (max_ifindex < nlm_index)
						max_ifindex = nlm_index;
				} else {
					if (ifl != NULL)
						ifl->ifa_next = ifa;
				}

				rtasize = NLMSG_PAYLOAD(nlh, nlmlen) - NLMSG_ALIGN(nlm_struct_size);
				for (rta = (struct rtattr *) (((char *) NLMSG_DATA(nlh)) + 
									NLMSG_ALIGN(nlm_struct_size)); 
				     RTA_OK(rta, rtasize); 
				     rta = RTA_NEXT(rta, rtasize)) {
					void *rtadata = RTA_DATA(rta);
					size_t rtapayload = RTA_PAYLOAD(rta);

					switch (nlh->nlmsg_type) {
					case RTM_NEWADDR:
						if (nlm_family == AF_PACKET)
							break;
						switch (rta->rta_type) {
#ifndef IFA_LOCAL
						case IFA_ADDRESS:
							ifamap.address = rtadata;
							ifamap.address_len = rtapayload;
							break;
						case IFA_LOCAL:
							ifamap.local = rtadata;
							ifamap.local_len = rtapayload;
							break;
						case IFA_BROADCAST:
							ifamap.broadcast = rtadata;
							ifamap.broadcast_len = rtapayload;
							break;
						case IFA_LABEL:
							break;
						case IFA_UNSPEC:
							break;
#else
						case IFA_LOCAL:
							if (!build)
								dlen += NLMSG_ALIGN(rtapayload);
							else {
								memcpy(data, rtadata, rtapayload);
								ifa->ifa_addr = data;
								data += NLMSG_ALIGN(rtapayload);
							}
							break;
#endif
						case IFA_CACHEINFO:
							if (!build)
								xlen += NLMSG_ALIGN(rtapayload);
							else {
								memcpy(xdata, rtadata, rtapayload);
								ifa->ifa_cacheinfo = xdata;
								xdata += NLMSG_ALIGN(rtapayload);
							}
							break;
						}
					}
				}
#ifndef IFA_LOCAL
				if (nlh->nlmsg_type == RTM_NEWADDR && nlm_family != AF_PACKET) {
					if (!ifamap.local) {
						ifamap.local = ifamap.address;
						ifamap.local_len = ifamap.address_len;
					}
					if (!ifamap.address) {
						ifamap.address = ifamap.local;
						ifamap.address_len = ifamap.local_len;
					}
					if (ifamap.address_len != ifamap.local_len || 
					    (ifamap.address != NULL && 
					     memcmp(ifamap.address, ifamap.local, ifamap.address_len))) {
						/* p2p; address is peer and local is ours */
						ifamap.broadcast = ifamap.address;
						ifamap.broadcast_len = ifamap.address_len;
						ifamap.address = ifamap.local;
						ifamap.address_len = ifamap.local_len;
					}
					if (ifamap.address) {
						if (!build)
							dlen += NLMSG_ALIGN(ifamap.address_len);
						else {
							ifa->ifa_addr = (struct sockaddr *) data;
							memcpy(ifa->ifa_addr, ifamap.address, ifamap.address_len);
							data += NLMSG_ALIGN(ifamap.address_len);
						}
					}
				}
#endif
				if (!build) {
					icnt++;
				} else {
					ifl = ifa++;
				}
			}
		}
		if (!build) {
			if (icnt == 0 && (dlen + xlen == 0)) {
				if (ifap != NULL)
					*ifap = NULL;
				break;	/* cannot found any addresses */
			}
		}
	}

/* ---------------------------------- */
	/* Finalize */
	free_nlmsglist(nlmsg_list);
	nl_close(sd);
	return 0;
}

/* ---------------------------------------------------------------------- */
void ni_freeifaddrs(struct ni_ifaddrs *ifa)
{
	free(ifa);
}



File: /ninfod\ni_ifaddrs.h
/* $USAGI: ni_ifaddrs.h,v 1.1 2002-12-03 17:48:53 yoshfuji Exp $ */
/*
 * Copyright (C) 2002 USAGI/WIDE Project.
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the project nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */
#ifndef NODEINFO_IFADDRS_H
#define NODEINFO_IFADDRS_H

struct ni_ifaddrs {
	struct ni_ifaddrs  	*ifa_next;
	unsigned int		ifa_ifindex;
	unsigned short		ifa_flags;
	void			*ifa_addr;
	struct ifa_cacheinfo	*ifa_cacheinfo;
};

int ni_ifaddrs(struct ni_ifaddrs **ifap, sa_family_t family);
void ni_freeifaddrs(struct ni_ifaddrs *ifa);

#endif



File: /ping.c
/*
 * Copyright (c) 1989 The Regents of the University of California.
 * All rights reserved.
 *
 * This code is derived from software contributed to Berkeley by
 * Mike Muuss.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 *	This product includes software developed by the University of
 *	California, Berkeley and its contributors.
 * 4. Neither the name of the University nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#ifndef lint
char copyright[] =
"@(#) Copyright (c) 1989 The Regents of the University of California.\n\
 All rights reserved.\n";
#endif /* not lint */

/*
 *			P I N G . C
 *
 * Using the InterNet Control Message Protocol (ICMP) "ECHO" facility,
 * measure round-trip-delays and packet loss across network paths.
 *
 * Author -
 *	Mike Muuss
 *	U. S. Army Ballistic Research Laboratory
 *	December, 1983
 *
 * Status -
 *	Public Domain.  Distribution Unlimited.
 * Bugs -
 *	More statistics could always be gathered.
 *	This program has to run SUID to ROOT to access the ICMP socket.
 */

#include "ping_common.h"

#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#ifndef WITHOUT_IFADDRS
#include <ifaddrs.h>
#endif

#ifndef ICMP_FILTER
#define ICMP_FILTER	1
struct icmp_filter {
	__u32	data;
};
#endif


#define	MAXIPLEN	60
#define	MAXICMPLEN	76
#define	NROUTES		9		/* number of record route slots */
#define TOS_MAX		255		/* 8-bit TOS field */
#define MAX_HOSTNAMELEN	NI_MAXHOST


static int ts_type;
static int nroute = 0;
static __u32 route[10];



struct sockaddr_in whereto;	/* who to ping */
int optlen = 0;
int settos = 0;			/* Set TOS, Precendence or other QOS options */
int icmp_sock;			/* socket file descriptor */
u_char outpack[0x10000];
int maxpacket = sizeof(outpack);

static int broadcast_pings = 0;

static char *pr_addr(__u32);
static void pr_options(unsigned char * cp, int hlen);
static void pr_iph(struct iphdr *ip);
static void usage(void) __attribute__((noreturn));
static u_short in_cksum(const u_short *addr, int len, u_short salt);
static void pr_icmph(__u8 type, __u8 code, __u32 info, struct icmphdr *icp);
static int parsetos(char *str);

static struct {
	struct cmsghdr cm;
	struct in_pktinfo ipi;
} cmsg = { {sizeof(struct cmsghdr) + sizeof(struct in_pktinfo), SOL_IP, IP_PKTINFO},
	   {0, }};
int cmsg_len;

struct sockaddr_in source;
char *device;
int pmtudisc = -1;


int main(int argc, char **argv){
	struct hostent *hp;
	int ch, hold, packlen;
	int socket_errno;
	u_char *packet;
	char *target;
#ifdef USE_IDN
	char *hnamebuf = NULL;
#else
	char hnamebuf[MAX_HOSTNAMELEN];
#endif
	char rspace[3 + 4 * NROUTES + 1];	/* record route space */

	limit_capabilities();

#ifdef USE_IDN
	setlocale(LC_ALL, "");
#endif

	enable_capability_raw();

	icmp_sock = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
	socket_errno = errno;

	disable_capability_raw();

	source.sin_family = AF_INET;

	preload = 1;
	while ((ch = getopt(argc, argv, COMMON_OPTSTR "bRT:")) != EOF) {
		switch(ch) {
		case 'b':
			broadcast_pings = 1;
			break;
		case 'Q':
			settos = parsetos(optarg);
			if (settos &&
			    (setsockopt(icmp_sock, IPPROTO_IP, IP_TOS,
					(char *)&settos, sizeof(int)) < 0)) {
				perror("ping: error setting QOS sockopts");
				exit(2);
			}
			break;
		case 'R':
			if (options & F_TIMESTAMP) {
				fprintf(stderr, "Only one of -T or -R may be used\n");
				exit(2);
			}
			options |= F_RROUTE;
			break;
		case 'T':
			if (options & F_RROUTE) {
				fprintf(stderr, "Only one of -T or -R may be used\n");
				exit(2);
			}
			options |= F_TIMESTAMP;
			if (strcmp(optarg, "tsonly") == 0)
				ts_type = IPOPT_TS_TSONLY;
			else if (strcmp(optarg, "tsandaddr") == 0)
				ts_type = IPOPT_TS_TSANDADDR;
			else if (strcmp(optarg, "tsprespec") == 0)
				ts_type = IPOPT_TS_PRESPEC;
			else {
				fprintf(stderr, "Invalid timestamp type\n");
				exit(2);
			}
			break;
		case 'I':
		{
#if 0
			char dummy;
			int i1, i2, i3, i4;

			if (sscanf(optarg, "%u.%u.%u.%u%c",
				   &i1, &i2, &i3, &i4, &dummy) == 4) {
				__u8 *ptr;
				ptr = (__u8*)&source.sin_addr;
				ptr[0] = i1;
				ptr[1] = i2;
				ptr[2] = i3;
				ptr[3] = i4;
				options |= F_STRICTSOURCE;
			} else {
				device = optarg;
			}
#else
			if (inet_pton(AF_INET, optarg, &source.sin_addr) > 0)
				options |= F_STRICTSOURCE;
			else
				device = optarg;
#endif
			break;
		}
		case 'M':
			if (strcmp(optarg, "do") == 0)
				pmtudisc = IP_PMTUDISC_DO;
			else if (strcmp(optarg, "dont") == 0)
				pmtudisc = IP_PMTUDISC_DONT;
			else if (strcmp(optarg, "want") == 0)
				pmtudisc = IP_PMTUDISC_WANT;
			else {
				fprintf(stderr, "ping: wrong value for -M: do, dont, want are valid ones.\n");
				exit(2);
			}
			break;
		case 'V':
			printf("ping utility, iputils-%s\n", SNAPSHOT);
			exit(0);
		COMMON_OPTIONS
			common_options(ch);
			break;
		default:
			usage();
		}
	}
	argc -= optind;
	argv += optind;

	if (argc == 0)
		usage();
	if (argc > 1) {
		if (options & F_RROUTE)
			usage();
		else if (options & F_TIMESTAMP) {
			if (ts_type != IPOPT_TS_PRESPEC)
				usage();
			if (argc > 5)
				usage();
		} else {
			if (argc > 10)
				usage();
			options |= F_SOURCEROUTE;
		}
	}
	while (argc > 0) {
		target = *argv;

		memset((char *)&whereto, 0, sizeof(whereto));
		whereto.sin_family = AF_INET;
		if (inet_aton(target, &whereto.sin_addr) == 1) {
			hostname = target;
			if (argc == 1)
				options |= F_NUMERIC;
		} else {
			char *idn;
#ifdef USE_IDN
			int rc;

			if (hnamebuf) {
				free(hnamebuf);
				hnamebuf = NULL;
			}

			rc = idna_to_ascii_lz(target, &idn, 0);
			if (rc != IDNA_SUCCESS) {
				fprintf(stderr, "ping: IDN encoding failed: %s\n", idna_strerror(rc));
				exit(2);
			}
#else
			idn = target;
#endif
			hp = gethostbyname(idn);
			if (!hp) {
				fprintf(stderr, "ping: unknown host %s\n", target);
				exit(2);
			}
#ifdef USE_IDN
			free(idn);
#endif
			memcpy(&whereto.sin_addr, hp->h_addr, 4);
#ifdef USE_IDN
			if (idna_to_unicode_lzlz(hp->h_name, &hnamebuf, 0) != IDNA_SUCCESS) {
				hnamebuf = strdup(hp->h_name);
				if (!hnamebuf) {
					perror("ping: strdup");
					exit(-1);
				}
			}
#else
			strncpy(hnamebuf, hp->h_name, sizeof(hnamebuf) - 1);
			hnamebuf[sizeof(hnamebuf) - 1] = 0;
#endif
			hostname = hnamebuf;
		}
		if (argc > 1)
			route[nroute++] = whereto.sin_addr.s_addr;
		argc--;
		argv++;
	}

	if (source.sin_addr.s_addr == 0) {
		socklen_t alen;
		struct sockaddr_in dst = whereto;
		int probe_fd = socket(AF_INET, SOCK_DGRAM, 0);

		if (probe_fd < 0) {
			perror("socket");
			exit(2);
		}
		if (device) {
			struct ifreq ifr;
			int rc;

			memset(&ifr, 0, sizeof(ifr));
			strncpy(ifr.ifr_name, device, IFNAMSIZ-1);

			enable_capability_raw();
			rc = setsockopt(probe_fd, SOL_SOCKET, SO_BINDTODEVICE, device, strlen(device)+1);
			disable_capability_raw();

			if (rc == -1) {
				if (IN_MULTICAST(ntohl(dst.sin_addr.s_addr))) {
					struct ip_mreqn imr;
					if (ioctl(probe_fd, SIOCGIFINDEX, &ifr) < 0) {
						fprintf(stderr, "ping: unknown iface %s\n", device);
						exit(2);
					}
					memset(&imr, 0, sizeof(imr));
					imr.imr_ifindex = ifr.ifr_ifindex;
					if (setsockopt(probe_fd, SOL_IP, IP_MULTICAST_IF, &imr, sizeof(imr)) == -1) {
						perror("ping: IP_MULTICAST_IF");
						exit(2);
					}
				} else {
					perror("ping: SO_BINDTODEVICE");
					exit(2);
				}
			}
		}

		if (settos &&
		    setsockopt(probe_fd, IPPROTO_IP, IP_TOS, (char *)&settos, sizeof(int)) < 0)
			perror("Warning: error setting QOS sockopts");

		dst.sin_port = htons(1025);
		if (nroute)
			dst.sin_addr.s_addr = route[0];
		if (connect(probe_fd, (struct sockaddr*)&dst, sizeof(dst)) == -1) {
			if (errno == EACCES) {
				if (broadcast_pings == 0) {
					fprintf(stderr, "Do you want to ping broadcast? Then -b\n");
					exit(2);
				}
				fprintf(stderr, "WARNING: pinging broadcast address\n");
				if (setsockopt(probe_fd, SOL_SOCKET, SO_BROADCAST,
					       &broadcast_pings, sizeof(broadcast_pings)) < 0) {
					perror ("can't set broadcasting");
					exit(2);
				}
				if (connect(probe_fd, (struct sockaddr*)&dst, sizeof(dst)) == -1) {
					perror("connect");
					exit(2);
				}
			} else {
				perror("connect");
				exit(2);
			}
		}
		alen = sizeof(source);
		if (getsockname(probe_fd, (struct sockaddr*)&source, &alen) == -1) {
			perror("getsockname");
			exit(2);
		}
		source.sin_port = 0;

#ifndef WITHOUT_IFADDRS
		if (device) {
			struct ifaddrs *ifa0, *ifa;
			int ret;

			ret = getifaddrs(&ifa0);
			if (ret) {
				fprintf(stderr, "gatifaddrs() failed.\n");
				exit(2);
			}
			for (ifa = ifa0; ifa; ifa = ifa->ifa_next) {
				if (!ifa->ifa_addr || ifa->ifa_addr->sa_family != AF_INET)
					continue;
				if (!strncmp(ifa->ifa_name, device, sizeof(device) - 1) &&
				    !memcmp(&((struct sockaddr_in *)ifa->ifa_addr)->sin_addr,
					    &source.sin_addr, sizeof(source.sin_addr)))
					break;
			}
			freeifaddrs(ifa0);
			if (!ifa)
				fprintf(stderr, "ping: Warning: source address might be selected on device other than %s.\n", device);
		}
#endif
		close(probe_fd);
	} while (0);

	if (whereto.sin_addr.s_addr == 0)
		whereto.sin_addr.s_addr = source.sin_addr.s_addr;

	if (icmp_sock < 0) {
		errno = socket_errno;
		perror("ping: icmp open socket");
		exit(2);
	}

	if (device) {
		struct ifreq ifr;

		memset(&ifr, 0, sizeof(ifr));
		strncpy(ifr.ifr_name, device, IFNAMSIZ-1);
		if (ioctl(icmp_sock, SIOCGIFINDEX, &ifr) < 0) {
			fprintf(stderr, "ping: unknown iface %s\n", device);
			exit(2);
		}
		cmsg.ipi.ipi_ifindex = ifr.ifr_ifindex;
		cmsg_len = sizeof(cmsg);
	}

	if (broadcast_pings || IN_MULTICAST(ntohl(whereto.sin_addr.s_addr))) {
		if (uid) {
			if (interval < 1000) {
				fprintf(stderr, "ping: broadcast ping with too short interval.\n");
				exit(2);
			}
			if (pmtudisc >= 0 && pmtudisc != IP_PMTUDISC_DO) {
				fprintf(stderr, "ping: broadcast ping does not fragment.\n");
				exit(2);
			}
		}
		if (pmtudisc < 0)
			pmtudisc = IP_PMTUDISC_DO;
	}

	if (pmtudisc >= 0) {
		if (setsockopt(icmp_sock, SOL_IP, IP_MTU_DISCOVER, &pmtudisc, sizeof(pmtudisc)) == -1) {
			perror("ping: IP_MTU_DISCOVER");
			exit(2);
		}
	}

	if ((options&F_STRICTSOURCE) &&
	    bind(icmp_sock, (struct sockaddr*)&source, sizeof(source)) == -1) {
		perror("bind");
		exit(2);
	}

	if (1) {
		struct icmp_filter filt;
		filt.data = ~((1<<ICMP_SOURCE_QUENCH)|
			      (1<<ICMP_DEST_UNREACH)|
			      (1<<ICMP_TIME_EXCEEDED)|
			      (1<<ICMP_PARAMETERPROB)|
			      (1<<ICMP_REDIRECT)|
			      (1<<ICMP_ECHOREPLY));
		if (setsockopt(icmp_sock, SOL_RAW, ICMP_FILTER, (char*)&filt, sizeof(filt)) == -1)
			perror("WARNING: setsockopt(ICMP_FILTER)");
	}

	hold = 1;
	if (setsockopt(icmp_sock, SOL_IP, IP_RECVERR, (char *)&hold, sizeof(hold)))
		fprintf(stderr, "WARNING: your kernel is veeery old. No problems.\n");

	/* record route option */
	if (options & F_RROUTE) {
		memset(rspace, 0, sizeof(rspace));
		rspace[0] = IPOPT_NOP;
		rspace[1+IPOPT_OPTVAL] = IPOPT_RR;
		rspace[1+IPOPT_OLEN] = sizeof(rspace)-1;
		rspace[1+IPOPT_OFFSET] = IPOPT_MINOFF;
		optlen = 40;
		if (setsockopt(icmp_sock, IPPROTO_IP, IP_OPTIONS, rspace, sizeof(rspace)) < 0) {
			perror("ping: record route");
			exit(2);
		}
	}
	if (options & F_TIMESTAMP) {
		memset(rspace, 0, sizeof(rspace));
		rspace[0] = IPOPT_TIMESTAMP;
		rspace[1] = (ts_type==IPOPT_TS_TSONLY ? 40 : 36);
		rspace[2] = 5;
		rspace[3] = ts_type;
		if (ts_type == IPOPT_TS_PRESPEC) {
			int i;
			rspace[1] = 4+nroute*8;
			for (i=0; i<nroute; i++)
				*(__u32*)&rspace[4+i*8] = route[i];
		}
		if (setsockopt(icmp_sock, IPPROTO_IP, IP_OPTIONS, rspace, rspace[1]) < 0) {
			rspace[3] = 2;
			if (setsockopt(icmp_sock, IPPROTO_IP, IP_OPTIONS, rspace, rspace[1]) < 0) {
				perror("ping: ts option");
				exit(2);
			}
		}
		optlen = 40;
	}
	if (options & F_SOURCEROUTE) {
		int i;
		memset(rspace, 0, sizeof(rspace));
		rspace[0] = IPOPT_NOOP;
		rspace[1+IPOPT_OPTVAL] = (options & F_SO_DONTROUTE) ? IPOPT_SSRR
			: IPOPT_LSRR;
		rspace[1+IPOPT_OLEN] = 3 + nroute*4;
		rspace[1+IPOPT_OFFSET] = IPOPT_MINOFF;
		for (i=0; i<nroute; i++)
			*(__u32*)&rspace[4+i*4] = route[i];

		if (setsockopt(icmp_sock, IPPROTO_IP, IP_OPTIONS, rspace, 4 + nroute*4) < 0) {
			perror("ping: record route");
			exit(2);
		}
		optlen = 40;
	}

	/* Estimate memory eaten by single packet. It is rough estimate.
	 * Actually, for small datalen's it depends on kernel side a lot. */
	hold = datalen + 8;
	hold += ((hold+511)/512)*(optlen + 20 + 16 + 64 + 160);
	sock_setbufs(icmp_sock, hold);

	if (broadcast_pings) {
		if (setsockopt(icmp_sock, SOL_SOCKET, SO_BROADCAST,
			       &broadcast_pings, sizeof(broadcast_pings)) < 0) {
			perror ("ping: can't set broadcasting");
			exit(2);
		}
	}

	if (options & F_NOLOOP) {
		int loop = 0;
		if (setsockopt(icmp_sock, IPPROTO_IP, IP_MULTICAST_LOOP,
							&loop, 1) == -1) {
			perror ("ping: can't disable multicast loopback");
			exit(2);
		}
	}
	if (options & F_TTL) {
		int ittl = ttl;
		if (setsockopt(icmp_sock, IPPROTO_IP, IP_MULTICAST_TTL,
							&ttl, 1) == -1) {
			perror ("ping: can't set multicast time-to-live");
			exit(2);
		}
		if (setsockopt(icmp_sock, IPPROTO_IP, IP_TTL,
							&ittl, sizeof(ittl)) == -1) {
			perror ("ping: can't set unicast time-to-live");
			exit(2);
		}
	}

	if (datalen > 0xFFFF - 8 - optlen - 20) {
		if (uid || datalen > sizeof(outpack)-8) {
			fprintf(stderr, "Error: packet size %d is too large. Maximum is %d\n", datalen, 0xFFFF-8-20-optlen);
			exit(2);
		}
		/* Allow small oversize to root yet. It will cause EMSGSIZE. */
		fprintf(stderr, "WARNING: packet size %d is too large. Maximum is %d\n", datalen, 0xFFFF-8-20-optlen);
	}

	if (datalen >= sizeof(struct timeval))	/* can we time transfer */
		timing = 1;
	packlen = datalen + MAXIPLEN + MAXICMPLEN;
	if (!(packet = (u_char *)malloc((u_int)packlen))) {
		fprintf(stderr, "ping: out of memory.\n");
		exit(2);
	}

	// Cabecalho inicial
	print_header();
/*
	printf("PING %s (%s) ", hostname, inet_ntoa(whereto.sin_addr));
	if (device || (options&F_STRICTSOURCE))
		printf("from %s %s: ", inet_ntoa(source.sin_addr), device ?: "");
	printf("%d(%d) bytes of data.\n", datalen, datalen+8+optlen+20);
*/
//	printf("  SEQ HOST                                     SIZE TTL TIME  STATUS\n");


	setup(icmp_sock);

	main_loop(icmp_sock, packet, packlen);
}

int receive_error_msg(){

	int res;
	char cbuf[512];
	struct iovec  iov;
	struct msghdr msg;
	struct cmsghdr *cmsg;
	struct sock_extended_err *e;
	struct icmphdr icmph;
	struct sockaddr_in target;
	int net_errors = 0;
	int local_errors = 0;
	int saved_errno = errno;

	iov.iov_base = &icmph;
	iov.iov_len = sizeof(icmph);
	msg.msg_name = (void*)&target;
	msg.msg_namelen = sizeof(target);
	msg.msg_iov = &iov;
	msg.msg_iovlen = 1;
	msg.msg_flags = 0;
	msg.msg_control = cbuf;
	msg.msg_controllen = sizeof(cbuf);

	res = recvmsg(icmp_sock, &msg, MSG_ERRQUEUE|MSG_DONTWAIT);
	if (res < 0)
		goto out;

	e = NULL;
	for (cmsg = CMSG_FIRSTHDR(&msg); cmsg; cmsg = CMSG_NXTHDR(&msg, cmsg)) {
		if (cmsg->cmsg_level == SOL_IP) {
			if (cmsg->cmsg_type == IP_RECVERR)
				e = (struct sock_extended_err *)CMSG_DATA(cmsg);
		}
	}
	if (e == NULL)
		abort();

	if (e->ee_origin == SO_EE_ORIGIN_LOCAL) {
		local_errors++;
		if (options & F_QUIET)
			goto out;
		if (options & F_FLOOD)
			write_stdout("E", 1);
		else if (e->ee_errno != EMSGSIZE)
			fprintf(stderr, "ping: local error: %s\n", strerror(e->ee_errno));
		else
			fprintf(stderr, "ping: local error: Message too long, mtu=%u\n", e->ee_info);
		nerrors++;
	} else if (e->ee_origin == SO_EE_ORIGIN_ICMP) {
		struct sockaddr_in *sin = (struct sockaddr_in*)(e+1);

		if (res < sizeof(icmph) ||
		    target.sin_addr.s_addr != whereto.sin_addr.s_addr ||
		    icmph.type != ICMP_ECHO ||
		    icmph.un.echo.id != ident) {
			/* Not our error, not an error at all. Clear. */
			saved_errno = 0;
			goto out;
		}

		acknowledge(ntohs(icmph.un.echo.sequence));

		if (!working_recverr) {
			struct icmp_filter filt;
			working_recverr = 1;
			/* OK, it works. Add stronger filter. */
			filt.data = ~((1<<ICMP_SOURCE_QUENCH)|
				      (1<<ICMP_REDIRECT)|
				      (1<<ICMP_ECHOREPLY));
			if (setsockopt(icmp_sock, SOL_RAW, ICMP_FILTER, (char*)&filt, sizeof(filt)) == -1)
				perror("\rWARNING: setsockopt(ICMP_FILTER)");
		}

		net_errors++;
		nerrors++;
		if (options & F_QUIET)
			goto out;
		if (options & F_FLOOD) {
			write_stdout("\bE", 2);
		} else {
			print_timestamp();
			printf("From %s icmp_seq=%u ", pr_addr(sin->sin_addr.s_addr), ntohs(icmph.un.echo.sequence));
			pr_icmph(e->ee_type, e->ee_code, e->ee_info, NULL);
			fflush(stdout);
		}
	}

out:
	errno = saved_errno;
	return net_errors ? : -local_errors;
}

// imprimir cabecalho
void print_header(){

	printf("%s%s SEQ HOST                                      SIZE TTL TIME  STATUS%s\n",  FONT_BOLD, LWHT, RESET);

// 65535 
}

/*
 * pinger --
 * 	Compose and transmit an ICMP ECHO REQUEST packet.  The IP packet
 * will be added on by the kernel.  The ID field is our UNIX process ID,
 * and the sequence number is an ascending integer.  The first 8 bytes
 * of the data portion are used to hold a UNIX "timeval" struct in VAX
 * byte-order, to compute the round-trip time.
 */
int send_probe(){
	struct icmphdr *icp;
	int cc;
	int i;

	icp = (struct icmphdr *)outpack;
	icp->type = ICMP_ECHO;
	icp->code = 0;
	icp->checksum = 0;
	icp->un.echo.sequence = htons(ntransmitted+1);
	icp->un.echo.id = ident;			/* ID */

	rcvd_clear(ntransmitted+1);

	if (timing) {
		if (options&F_LATENCY) {
			struct timeval tmp_tv;
			gettimeofday(&tmp_tv, NULL);
			memcpy(icp+1, &tmp_tv, sizeof(tmp_tv));
		} else {
			memset(icp+1, 0, sizeof(struct timeval));
		}
	}

	cc = datalen + 8;			/* skips ICMP portion */

	/* compute ICMP checksum here */
	icp->checksum = in_cksum((u_short *)icp, cc, 0);

	if (timing && !(options&F_LATENCY)) {
		struct timeval tmp_tv;
		gettimeofday(&tmp_tv, NULL);
		memcpy(icp+1, &tmp_tv, sizeof(tmp_tv));
		icp->checksum = in_cksum((u_short *)&tmp_tv, sizeof(tmp_tv), ~icp->checksum);
	}

	do {
		static struct iovec iov = {outpack, 0};
		static struct msghdr m = { &whereto, sizeof(whereto),
						   &iov, 1, &cmsg, 0, 0 };
		m.msg_controllen = cmsg_len;
		iov.iov_len = cc;

		i = sendmsg(icmp_sock, &m, confirm);
		confirm = 0;
	} while (0);

	return (cc == i ? 0 : i);
}

/*
 * parse_reply --
 *	Print out the packet, if it came from us.  This logic is necessary
 * because ALL readers of the ICMP socket get a copy of ALL ICMP packets
 * which arrive ('tis only fair).  This permits multiple copies of this
 * program to be run without having intermingled output (or statistics!).
 */
void pr_echo_reply(__u8 *_icp, int len){
	struct icmphdr *icp = (struct icmphdr *)_icp;
	printf("%4u ", ntohs(icp->un.echo.sequence));
}

int parse_reply(struct msghdr *msg, int cc, void *addr, struct timeval *tv){
	struct sockaddr_in *from = addr;
	__u8 *buf = msg->msg_iov->iov_base;
	struct icmphdr *icp;
	struct iphdr *ip;
	int hlen;
	int csfailed;

	/* Check the IP header */
	ip = (struct iphdr *)buf;
	hlen = ip->ihl*4;
	if (cc < hlen + 8 || ip->ihl < 5) {
		if (options & F_VERBOSE)
			fprintf(stderr, "ping: packet too short (%d bytes) from %s\n", cc,
				pr_addr(from->sin_addr.s_addr));
		return 1;
	}

	/* Now the ICMP part */
	cc -= hlen;
	icp = (struct icmphdr *)(buf + hlen);
	csfailed = in_cksum((u_short *)icp, cc, 0);

	if (icp->type == ICMP_ECHOREPLY) {
		if (icp->un.echo.id != ident)
			return 1;			/* 'Twas not our ECHO */
		if (gather_statistics((__u8*)icp, sizeof(*icp), cc,
				      ntohs(icp->un.echo.sequence),
				      ip->ttl, 0, tv, pr_addr(from->sin_addr.s_addr), pr_echo_reply))
			return 0;
	} else {
		/* We fall here when a redirect or source quench arrived.
		 * Also this branch processes icmp errors, when IP_RECVERR
		 * is broken. */

		switch (icp->type) {
		case ICMP_ECHO:
			/* MUST NOT */
			return 1;
		case ICMP_SOURCE_QUENCH:
		case ICMP_REDIRECT:
		case ICMP_DEST_UNREACH:
		case ICMP_TIME_EXCEEDED:
		case ICMP_PARAMETERPROB:
			{
				struct iphdr * iph = (struct  iphdr *)(&icp[1]);
				struct icmphdr *icp1 = (struct icmphdr*)((unsigned char *)iph + iph->ihl*4);
				int error_pkt;
				if (cc < 8+sizeof(struct iphdr)+8 ||
				    cc < 8+iph->ihl*4+8)
					return 1;
				if (icp1->type != ICMP_ECHO ||
				    iph->daddr != whereto.sin_addr.s_addr ||
				    icp1->un.echo.id != ident)
					return 1;
				error_pkt = (icp->type != ICMP_REDIRECT &&
					     icp->type != ICMP_SOURCE_QUENCH);
				if (error_pkt) {
					acknowledge(ntohs(icp1->un.echo.sequence));
					if (working_recverr) {
						return 0;
					} else {
						static int once;
						/* Sigh, IP_RECVERR for raw socket
						 * was broken until 2.4.9. So, we ignore
						 * the first error and warn on the second.
						 */
						if (once++ == 1)
							fprintf(stderr, "\rWARNING: kernel is not very fresh, upgrade is recommended.\n");
						if (once == 1)
							return 0;
					}
				}
				nerrors+=error_pkt;
				if (options&F_QUIET)
					return !error_pkt;
				if (options & F_FLOOD) {
					if (error_pkt)
						write_stdout("\bE", 2);
					return !error_pkt;
				}
				print_timestamp();
				printf("From %s: icmp_seq=%u ",
				       pr_addr(from->sin_addr.s_addr),
				       ntohs(icp1->un.echo.sequence));
				if (csfailed)
					printf("(BAD CHECKSUM)");
				pr_icmph(icp->type, icp->code, ntohl(icp->un.gateway), icp);
				return !error_pkt;
			}
		default:
			/* MUST NOT */
			break;
		}
		if ((options & F_FLOOD) && !(options & (F_VERBOSE|F_QUIET))) {
			if (!csfailed)
				write_stdout("!E", 2);
			else
				write_stdout("!EC", 3);
			return 0;
		}
		if (!(options & F_VERBOSE) || uid)
			return 0;
		if (options & F_PTIMEOFDAY) {
			struct timeval recv_time;
			gettimeofday(&recv_time, NULL);
			printf("%lu.%06lu ", (unsigned long)recv_time.tv_sec, (unsigned long)recv_time.tv_usec);
		}
		printf("From %s: ", pr_addr(from->sin_addr.s_addr));
		if (csfailed) {
			printf("(BAD CHECKSUM)\n");
			return 0;
		}
		pr_icmph(icp->type, icp->code, ntohl(icp->un.gateway), icp);
		return 0;
	}

	if (!(options & F_FLOOD)) {
		pr_options(buf + sizeof(struct iphdr), hlen);

		if (options & F_AUDIBLE)
			putchar('\a');
		putchar('\n');
		fflush(stdout);
	} else {
		putchar('\a');
		fflush(stdout);
	}
	return 0;
}


#if BYTE_ORDER == LITTLE_ENDIAN
# define ODDBYTE(v)	(v)
#elif BYTE_ORDER == BIG_ENDIAN
# define ODDBYTE(v)	((u_short)(v) << 8)
#else
# define ODDBYTE(v)	htons((u_short)(v) << 8)
#endif

u_short
in_cksum(const u_short *addr, register int len, u_short csum)
{
	register int nleft = len;
	const u_short *w = addr;
	register u_short answer;
	register int sum = csum;

	/*
	 *  Our algorithm is simple, using a 32 bit accumulator (sum),
	 *  we add sequential 16 bit words to it, and at the end, fold
	 *  back all the carry bits from the top 16 bits into the lower
	 *  16 bits.
	 */
	while (nleft > 1)  {
		sum += *w++;
		nleft -= 2;
	}

	/* mop up an odd byte, if necessary */
	if (nleft == 1)
		sum += ODDBYTE(*(u_char *)w); /* le16toh() may be unavailable on old systems */

	/*
	 * add back carry outs from top 16 bits to low 16 bits
	 */
	sum = (sum >> 16) + (sum & 0xffff);	/* add hi 16 to low 16 */
	sum += (sum >> 16);			/* add carry */
	answer = ~sum;				/* truncate to 16 bits */
	return (answer);
}

/*
 * pr_icmph --
 *	Print a descriptive string about an ICMP header.
 */
void pr_icmph(__u8 type, __u8 code, __u32 info, struct icmphdr *icp)
{
	switch(type) {
	case ICMP_ECHOREPLY:
		printf("Echo Reply\n");
		/* XXX ID + Seq + Data */
		break;
	case ICMP_DEST_UNREACH:
		switch(code) {
		case ICMP_NET_UNREACH:
			printf("Destination Net Unreachable\n");
			break;
		case ICMP_HOST_UNREACH:
			printf("Destination Host Unreachable\n");
			break;
		case ICMP_PROT_UNREACH:
			printf("Destination Protocol Unreachable\n");
			break;
		case ICMP_PORT_UNREACH:
			printf("Destination Port Unreachable\n");
			break;
		case ICMP_FRAG_NEEDED:
			printf("Frag needed and DF set (mtu = %u)\n", info);
			break;
		case ICMP_SR_FAILED:
			printf("Source Route Failed\n");
			break;
		case ICMP_NET_UNKNOWN:
			printf("Destination Net Unknown\n");
			break;
		case ICMP_HOST_UNKNOWN:
			printf("Destination Host Unknown\n");
			break;
		case ICMP_HOST_ISOLATED:
			printf("Source Host Isolated\n");
			break;
		case ICMP_NET_ANO:
			printf("Destination Net Prohibited\n");
			break;
		case ICMP_HOST_ANO:
			printf("Destination Host Prohibited\n");
			break;
		case ICMP_NET_UNR_TOS:
			printf("Destination Net Unreachable for Type of Service\n");
			break;
		case ICMP_HOST_UNR_TOS:
			printf("Destination Host Unreachable for Type of Service\n");
			break;
		case ICMP_PKT_FILTERED:
			printf("Packet filtered\n");
			break;
		case ICMP_PREC_VIOLATION:
			printf("Precedence Violation\n");
			break;
		case ICMP_PREC_CUTOFF:
			printf("Precedence Cutoff\n");
			break;
		default:
			printf("Dest Unreachable, Bad Code: %d\n", code);
			break;
		}
		if (icp && (options & F_VERBOSE))
			pr_iph((struct iphdr*)(icp + 1));
		break;
	case ICMP_SOURCE_QUENCH:
		printf("Source Quench\n");
		if (icp && (options & F_VERBOSE))
			pr_iph((struct iphdr*)(icp + 1));
		break;
	case ICMP_REDIRECT:
		switch(code) {
		case ICMP_REDIR_NET:
			printf("Redirect Network");
			break;
		case ICMP_REDIR_HOST:
			printf("Redirect Host");
			break;
		case ICMP_REDIR_NETTOS:
			printf("Redirect Type of Service and Network");
			break;
		case ICMP_REDIR_HOSTTOS:
			printf("Redirect Type of Service and Host");
			break;
		default:
			printf("Redirect, Bad Code: %d", code);
			break;
		}
		if (icp)
			printf("(New nexthop: %s)\n", pr_addr(icp->un.gateway));
		if (icp && (options & F_VERBOSE))
			pr_iph((struct iphdr*)(icp + 1));
		break;
	case ICMP_ECHO:
		printf("Echo Request\n");
		/* XXX ID + Seq + Data */
		break;
	case ICMP_TIME_EXCEEDED:
		switch(code) {
		case ICMP_EXC_TTL:
			printf("Time to live exceeded\n");
			break;
		case ICMP_EXC_FRAGTIME:
			printf("Frag reassembly time exceeded\n");
			break;
		default:
			printf("Time exceeded, Bad Code: %d\n", code);
			break;
		}
		if (icp && (options & F_VERBOSE))
			pr_iph((struct iphdr*)(icp + 1));
		break;
	case ICMP_PARAMETERPROB:
		printf("Parameter problem: pointer = %u\n", icp ? (ntohl(icp->un.gateway)>>24) : info);
		if (icp && (options & F_VERBOSE))
			pr_iph((struct iphdr*)(icp + 1));
		break;
	case ICMP_TIMESTAMP:
		printf("Timestamp\n");
		/* XXX ID + Seq + 3 timestamps */
		break;
	case ICMP_TIMESTAMPREPLY:
		printf("Timestamp Reply\n");
		/* XXX ID + Seq + 3 timestamps */
		break;
	case ICMP_INFO_REQUEST:
		printf("Information Request\n");
		/* XXX ID + Seq */
		break;
	case ICMP_INFO_REPLY:
		printf("Information Reply\n");
		/* XXX ID + Seq */
		break;
#ifdef ICMP_MASKREQ
	case ICMP_MASKREQ:
		printf("Address Mask Request\n");
		break;
#endif
#ifdef ICMP_MASKREPLY
	case ICMP_MASKREPLY:
		printf("Address Mask Reply\n");
		break;
#endif
	default:
		printf("Bad ICMP type: %d\n", type);
	}
}

void pr_options(unsigned char * cp, int hlen)
{
	int i, j;
	int optlen, totlen;
	unsigned char * optptr;
	static int old_rrlen;
	static char old_rr[MAX_IPOPTLEN];

	totlen = hlen-sizeof(struct iphdr);
	optptr = cp;

	while (totlen > 0) {
		if (*optptr == IPOPT_EOL)
			break;
		if (*optptr == IPOPT_NOP) {
			totlen--;
			optptr++;
			printf("\nNOP");
			continue;
		}
		cp = optptr;
		optlen = optptr[1];
		if (optlen < 2 || optlen > totlen)
			break;

		switch (*cp) {
		case IPOPT_SSRR:
		case IPOPT_LSRR:
			printf("\n%cSRR: ", *cp==IPOPT_SSRR ? 'S' : 'L');
			j = *++cp;
			i = *++cp;
			i -= 4;
			cp++;
			if (j > IPOPT_MINOFF) {
				for (;;) {
					__u32 address;
					memcpy(&address, cp, 4);
					cp += 4;
					if (address == 0)
						printf("\t0.0.0.0");
					else
						printf("\t%s", pr_addr(address));
					j -= 4;
					putchar('\n');
					if (j <= IPOPT_MINOFF)
						break;
				}
			}
			break;
		case IPOPT_RR:
			j = *++cp;		/* get length */
			i = *++cp;		/* and pointer */
			if (i > j)
				i = j;
			i -= IPOPT_MINOFF;
			if (i <= 0)
				break;
			if (i == old_rrlen
			    && !memcmp(cp, old_rr, i)
			    && !(options & F_FLOOD)) {
				printf("\t(same route)");
				i = ((i + 3) / 4) * 4;
				cp += i;
				break;
			}
			old_rrlen = i;
			memcpy(old_rr, (char *)cp, i);
			printf("\nRR: ");
			cp++;
			for (;;) {
				__u32 address;
				memcpy(&address, cp, 4);
				cp += 4;
				if (address == 0)
					printf("\t0.0.0.0");
				else
					printf("\t%s", pr_addr(address));
				i -= 4;
				putchar('\n');
				if (i <= 0)
					break;
			}
			break;
		case IPOPT_TS:
		{
			int stdtime = 0, nonstdtime = 0;
			__u8 flags;
			j = *++cp;		/* get length */
			i = *++cp;		/* and pointer */
			if (i > j)
				i = j;
			i -= 5;
			if (i <= 0)
				break;
			flags = *++cp;
			printf("\nTS: ");
			cp++;
			for (;;) {
				long l;

				if ((flags&0xF) != IPOPT_TS_TSONLY) {
					__u32 address;
					memcpy(&address, cp, 4);
					cp += 4;
					if (address == 0)
						printf("\t0.0.0.0");
					else
						printf("\t%s", pr_addr(address));
					i -= 4;
					if (i <= 0)
						break;
				}
				l = *cp++;
				l = (l<<8) + *cp++;
				l = (l<<8) + *cp++;
				l = (l<<8) + *cp++;

				if  (l & 0x80000000) {
					if (nonstdtime==0)
						printf("\t%ld absolute not-standard", l&0x7fffffff);
					else
						printf("\t%ld not-standard", (l&0x7fffffff) - nonstdtime);
					nonstdtime = l&0x7fffffff;
				} else {
					if (stdtime==0)
						printf("\t%ld absolute", l);
					else
						printf("\t%ld", l - stdtime);
					stdtime = l;
				}
				i -= 4;
				putchar('\n');
				if (i <= 0)
					break;
			}
			if (flags>>4)
				printf("Unrecorded hops: %d\n", flags>>4);
			break;
		}
		default:
			printf("\nunknown option %x", *cp);
			break;
		}
		totlen -= optlen;
		optptr += optlen;
	}
}


/*
 * pr_iph --
 *	Print an IP header with options.
 */
void pr_iph(struct iphdr *ip)
{
	int hlen;
	u_char *cp;

	hlen = ip->ihl << 2;
	cp = (u_char *)ip + 20;		/* point to options */

	printf("Vr HL TOS  Len   ID Flg  off TTL Pro  cks      Src      Dst Data\n");
	printf(" %1x  %1x  %02x %04x %04x",
	       ip->version, ip->ihl, ip->tos, ip->tot_len, ip->id);
	printf("   %1x %04x", ((ip->frag_off) & 0xe000) >> 13,
	       (ip->frag_off) & 0x1fff);
	printf("  %02x  %02x %04x", ip->ttl, ip->protocol, ip->check);
	printf(" %s ", inet_ntoa(*(struct in_addr *)&ip->saddr));
	printf(" %s ", inet_ntoa(*(struct in_addr *)&ip->daddr));
	printf("\n");
	pr_options(cp, hlen);
}

/*
 * pr_addr --
 *	Return an ascii host address as a dotted quad and optionally with
 * a hostname.
 */
char *
pr_addr(__u32 addr)
{
	struct hostent *hp;
	static char buf[4096];

	in_pr_addr = !setjmp(pr_addr_jmp);

	if (exiting || (options & F_NUMERIC) ||
	    !(hp = gethostbyaddr((char *)&addr, 4, AF_INET)))
		sprintf(buf, "%s", inet_ntoa(*(struct in_addr *)&addr));
	else {
		char *s;
#if USE_IDN
		if (idna_to_unicode_lzlz(hp->h_name, &s, 0) != IDNA_SUCCESS)
			s = NULL;
#else
		s = NULL;
#endif
		snprintf(buf, sizeof(buf), "%s (%s)", s ? s : hp->h_name,
			 inet_ntoa(*(struct in_addr *)&addr));
#if USE_IDN
		free(s);
#endif
	}

	in_pr_addr = 0;

	return(buf);
}


/* Set Type of Service (TOS) and other Quality of Service relating bits */
int parsetos(char *str)
{
	const char *cp;
	int tos;
	char *ep;

	/* handle both hex and decimal values */
	if (str[0] == '0' && (str[1] == 'x' || str[1] == 'X')) {
		cp = str + 2;
		tos = (int)strtol(cp, &ep, 16);
	} else
		tos = (int)strtol(str, &ep, 10);

	/* doesn't look like decimal or hex, eh? */
	if (*ep != '\0') {
		fprintf(stderr, "ping: \"%s\" bad value for TOS\n", str);
		exit(2);
	}

	if (tos > TOS_MAX) {
		fprintf(stderr, "ping: the decimal value of TOS bits must be 0-254 (or zero)\n");
		exit(2);
	}
	return(tos);
}

#include <linux/filter.h>

void install_filter(void)
{
	static int once;
	static struct sock_filter insns[] = {
		BPF_STMT(BPF_LDX|BPF_B|BPF_MSH, 0), /* Skip IP header. F..g BSD... Look into ping6. */
		BPF_STMT(BPF_LD|BPF_H|BPF_IND, 4), /* Load icmp echo ident */
		BPF_JUMP(BPF_JMP|BPF_JEQ|BPF_K, 0xAAAA, 0, 1), /* Ours? */
		BPF_STMT(BPF_RET|BPF_K, ~0U), /* Yes, it passes. */
		BPF_STMT(BPF_LD|BPF_B|BPF_IND, 0), /* Load icmp type */
		BPF_JUMP(BPF_JMP|BPF_JEQ|BPF_K, ICMP_ECHOREPLY, 1, 0), /* Echo? */
		BPF_STMT(BPF_RET|BPF_K, 0xFFFFFFF), /* No. It passes. */
		BPF_STMT(BPF_RET|BPF_K, 0) /* Echo with wrong ident. Reject. */
	};
	static struct sock_fprog filter = {
		sizeof insns / sizeof(insns[0]),
		insns
	};

	if (once)
		return;
	once = 1;

	/* Patch bpflet for current identifier. */
	insns[2] = (struct sock_filter)BPF_JUMP(BPF_JMP|BPF_JEQ|BPF_K, htons(ident), 0, 1);

	if (setsockopt(icmp_sock, SOL_SOCKET, SO_ATTACH_FILTER, &filter, sizeof(filter)))
		perror("WARNING: failed to install socket filter\n");
}

#define USAGE_NEWLINE	"\n           "

void usage(void){

	fprintf(stderr,
		"Usage: ping"
		" [-"
			"aAbBdDfhLnOqrRUvV"
		"]"
		" [-c count]"
		" [-i interval]"
		" [-I interface]"
		USAGE_NEWLINE
		" [-m mark]"
		" [-M pmtudisc_option]"
		" [-l preload]"
		" [-p pattern]"
		" [-Q tos]"
		USAGE_NEWLINE
		" [-s packetsize]"
		" [-S sndbuf]"
		" [-t ttl]"
		" [-T timestamp_option]"
		USAGE_NEWLINE
		" [-w deadline]"
		" [-W timeout]"
		" [hop1 ...] destination"
		"\n"
	);
	exit(2);
}


File: /ping6.c
/*
 *
 *	Modified for AF_INET6 by Pedro Roque
 *
 *	<roque@di.fc.ul.pt>
 *
 *	Original copyright notice included bellow
 */

/*
 * Copyright (c) 1989 The Regents of the University of California.
 * All rights reserved.
 *
 * This code is derived from software contributed to Berkeley by
 * Mike Muuss.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 *	This product includes software developed by the University of
 *	California, Berkeley and its contributors.
 * 4. Neither the name of the University nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#ifndef lint
char copyright[] =
"@(#) Copyright (c) 1989 The Regents of the University of California.\n\
 All rights reserved.\n";
#endif /* not lint */

/*
 *			P I N G . C
 *
 * Using the InterNet Control Message Protocol (ICMP) "ECHO" facility,
 * measure round-trip-delays and packet loss across network paths.
 *
 * Author -
 *	Mike Muuss
 *	U. S. Army Ballistic Research Laboratory
 *	December, 1983
 *
 * Status -
 *	Public Domain.  Distribution Unlimited.
 * Bugs -
 *	More statistics could always be gathered.
 *	This program has to run SUID to ROOT to access the ICMP socket.
 */
#include "ping_common.h"

#include <linux/filter.h>
#include <netinet/ip6.h>
#include <netinet/icmp6.h>
#include <resolv.h>
#ifndef WITHOUT_IFADDRS
#include <ifaddrs.h>
#endif

#ifdef USE_IDN
#include <stringprep.h>
#endif

#include "ping6_niquery.h"
#include "in6_flowlabel.h"

#ifndef SOL_IPV6
#define SOL_IPV6 IPPROTO_IPV6
#endif

#ifndef SOL_ICMPV6
#define SOL_ICMPV6 IPPROTO_ICMPV6
#endif

/* RFC3542 */
#ifndef ICMP6_DST_UNREACH_BEYONDSCOPE
#define ICMP6_DST_UNREACH_BEYONDSCOPE ICMP6_DST_UNREACH_NOTNEIGHBOR
#endif

#if defined(ENABLE_PING6_RTHDR) && !defined(ENABLE_PING6_RTHDR_RFC3542)
#ifndef IPV6_SRCRT_TYPE_0
#define IPV6_SRCRT_TYPE_0	0
#endif
#endif

#ifndef MLD_LISTENER_QUERY
#define MLD_LISTENER_QUERY	130
#define MLD_LISTENER_REPORT	131
#define MLD_LISTENER_REDUCTION	132
#endif

#define BIT_CLEAR(nr, addr) do { ((__u32 *)(addr))[(nr) >> 5] &= ~(1U << ((nr) & 31)); } while(0)
#define BIT_SET(nr, addr) do { ((__u32 *)(addr))[(nr) >> 5] |= (1U << ((nr) & 31)); } while(0)
#define BIT_TEST(nr, addr) do { (__u32 *)(addr))[(nr) >> 5] & (1U << ((nr) & 31)); } while(0)

#ifndef ICMP6_FILTER_WILLPASS
#define ICMP6_FILTER_WILLPASS(type, filterp) \
	(BIT_TEST((type), filterp) == 0)

#define ICMP6_FILTER_WILLBLOCK(type, filterp) \
	BIT_TEST((type), filterp)

#define ICMP6_FILTER_SETPASS(type, filterp) \
	BIT_CLEAR((type), filterp)

#define ICMP6_FILTER_SETBLOCK(type, filterp) \
	BIT_SET((type), filterp)

#define ICMP6_FILTER_SETPASSALL(filterp) \
	memset(filterp, 0, sizeof(struct icmp6_filter));

#define ICMP6_FILTER_SETBLOCKALL(filterp) \
	memset(filterp, 0xFF, sizeof(struct icmp6_filter));
#endif

#define	MAXPACKET	128000		/* max packet size */

#ifdef SO_TIMESTAMP
#define HAVE_SIN6_SCOPEID 1
#endif

#ifndef SCOPE_DELIMITER
# define SCOPE_DELIMITER '%'
#endif

__u32 flowlabel;
__u32 tclass;
#ifdef ENABLE_PING6_RTHDR
struct cmsghdr *srcrt;
#endif

struct sockaddr_in6 whereto;	/* who to ping */
u_char outpack[MAXPACKET];
int maxpacket = sizeof(outpack);

static unsigned char cmsgbuf[4096];
static int cmsglen = 0;

static char * pr_addr(struct in6_addr *addr);
static char * pr_addr_n(struct in6_addr *addr);
static int pr_icmph(__u8 type, __u8 code, __u32 info);
static void usage(void) __attribute((noreturn));

struct sockaddr_in6 source;
char *device;
int pmtudisc=-1;

static int icmp_sock;

#ifdef USE_GNUTLS
# include <gnutls/openssl.h>
#else
# include <openssl/md5.h>
#endif

/* Node Information query */
int ni_query = -1;
int ni_flag = 0;
void *ni_subject = NULL;
int ni_subject_len = 0;
int ni_subject_type = -1;
char *ni_group;

static inline int ntohsp(__u16 *p)
{
	__u16 v;
	memcpy(&v, p, sizeof(v));
	return ntohs(v);
}

#if defined(ENABLE_PING6_RTHDR) && !defined(ENABLE_PING6_RTHDR_RFC3542)
size_t inet6_srcrt_space(int type, int segments)
{
	if (type != 0 || segments > 24)
		return 0;

	return (sizeof(struct cmsghdr) + sizeof(struct ip6_rthdr0) +
		segments * sizeof(struct in6_addr));
}

extern struct cmsghdr *	inet6_srcrt_init(void *bp, int type)
{
	struct cmsghdr *cmsg;

	if (type)
		return NULL;

	memset(bp, 0, sizeof(struct cmsghdr) + sizeof(struct ip6_rthdr0));
	cmsg = (struct cmsghdr *) bp;

	cmsg->cmsg_len = sizeof(struct cmsghdr) + sizeof(struct ip6_rthdr0);
	cmsg->cmsg_level = SOL_IPV6;
	cmsg->cmsg_type = IPV6_RTHDR;

	return cmsg;
}

int inet6_srcrt_add(struct cmsghdr *cmsg, const struct in6_addr *addr)
{
	struct ip6_rthdr0 *hdr;

	hdr = (struct ip6_rthdr0 *) CMSG_DATA(cmsg);

	cmsg->cmsg_len += sizeof(struct in6_addr);
	hdr->ip6r0_len += sizeof(struct in6_addr) / 8;

	memcpy(&hdr->ip6r0_addr[hdr->ip6r0_segleft++], addr,
	       sizeof(struct in6_addr));

	return 0;
}
#endif

unsigned int if_name2index(const char *ifname)
{
	unsigned int i = if_nametoindex(ifname);
	if (!i) {
		fprintf(stderr, "ping: unknown iface %s\n", ifname);
		exit(2);
	}
	return i;
}

struct niquery_option {
	char *name;
	int namelen;
	int has_arg;
	int data;
	int (*handler)(int index, const char *arg);
};

#define NIQUERY_OPTION(_name, _has_arg, _data, _handler)	\
	{							\
		.name = _name,					\
		.namelen = sizeof(_name) - 1,			\
		.has_arg = _has_arg,				\
		.data = _data,					\
		.handler = _handler				\
	}

static int niquery_option_name_handler(int index, const char *arg);
static int niquery_option_ipv6_handler(int index, const char *arg);
static int niquery_option_ipv6_flag_handler(int index, const char *arg);
static int niquery_option_ipv4_handler(int index, const char *arg);
static int niquery_option_ipv4_flag_handler(int index, const char *arg);
static int niquery_option_subject_addr_handler(int index, const char *arg);
static int niquery_option_subject_name_handler(int index, const char *arg);
static int niquery_option_help_handler(int index, const char *arg);

struct niquery_option niquery_options[] = {
	NIQUERY_OPTION("name",			0,	0,				niquery_option_name_handler),
	NIQUERY_OPTION("fqdn",			0,	0,				niquery_option_name_handler),
	NIQUERY_OPTION("ipv6",			0,	0,				niquery_option_ipv6_handler),
	NIQUERY_OPTION("ipv6-all",		0,	NI_IPV6ADDR_F_ALL,		niquery_option_ipv6_flag_handler),
	NIQUERY_OPTION("ipv6-compatible",	0,	NI_IPV6ADDR_F_COMPAT,		niquery_option_ipv6_flag_handler),
	NIQUERY_OPTION("ipv6-linklocal",	0,	NI_IPV6ADDR_F_LINKLOCAL,	niquery_option_ipv6_flag_handler),
	NIQUERY_OPTION("ipv6-sitelocal",	0,	NI_IPV6ADDR_F_SITELOCAL,	niquery_option_ipv6_flag_handler),
	NIQUERY_OPTION("ipv6-global",		0,	NI_IPV6ADDR_F_GLOBAL,		niquery_option_ipv6_flag_handler),
	NIQUERY_OPTION("ipv4",			0,	0,				niquery_option_ipv4_handler),
	NIQUERY_OPTION("ipv4-all",		0,	NI_IPV4ADDR_F_ALL,		niquery_option_ipv4_flag_handler),
	NIQUERY_OPTION("subject-ipv6",		1,	NI_SUBJ_IPV6,			niquery_option_subject_addr_handler),
	NIQUERY_OPTION("subject-ipv4",		1,	NI_SUBJ_IPV4,			niquery_option_subject_addr_handler),
	NIQUERY_OPTION("subject-name",		1,	0,				niquery_option_subject_name_handler),
	NIQUERY_OPTION("subject-fqdn",		1,	-1,				niquery_option_subject_name_handler),
	NIQUERY_OPTION("help",			0,	0,				niquery_option_help_handler),
	{},
};

static inline int niquery_is_enabled(void)
{
	return ni_query >= 0;
}

#if PING6_NONCE_MEMORY
__u8 *ni_nonce_ptr;
#else
struct {
	struct timeval tv;
	pid_t pid;
} ni_nonce_secret;
#endif

static void niquery_init_nonce(void)
{
#if PING6_NONCE_MEMORY
	struct timeval tv;
	unsigned long seed;

	seed = (unsigned long)getpid();
	if (!gettimeofday(&tv, NULL))
		seed ^= tv.tv_usec;
	srand(seed);

	ni_nonce_ptr = calloc(NI_NONCE_SIZE, MAX_DUP_CHK);
	if (!ni_nonce_ptr) {
		perror("ping6: calloc");
		exit(2);
	}

	ni_nonce_ptr[0] = ~0;
#else
	gettimeofday(&ni_nonce_secret.tv, NULL);
	ni_nonce_secret.pid = getpid();
#endif
}

#if !PING6_NONCE_MEMORY
static int niquery_nonce(__u8 *nonce, int fill)
{
	static __u8 digest[MD5_DIGEST_LENGTH];
	static int seq = -1;

	if (fill || seq != *(__u16 *)nonce || seq < 0) {
		MD5_CTX ctxt;

		MD5_Init(&ctxt);
		MD5_Update(&ctxt, &ni_nonce_secret, sizeof(ni_nonce_secret));
		MD5_Update(&ctxt, nonce, sizeof(__u16));
		MD5_Final(digest, &ctxt);

		seq = *(__u16 *)nonce;
	}

	if (fill) {
		memcpy(nonce + sizeof(__u16), digest, NI_NONCE_SIZE - sizeof(__u16));
		return 0;
	} else {
		if (memcmp(nonce + sizeof(__u16), digest, NI_NONCE_SIZE - sizeof(__u16)))
			return -1;
		return ntohsp((__u16 *)nonce);
	}
}
#endif

static inline void niquery_fill_nonce(__u16 seq, __u8 *nonce)
{
	__u16 v = htons(seq);
#if PING6_NONCE_MEMORY
	int i;

	memcpy(&ni_nonce_ptr[NI_NONCE_SIZE * (seq % MAX_DUP_CHK)], &v, sizeof(v));

	for (i = sizeof(v); i < NI_NONCE_SIZE; i++)
		ni_nonce_ptr[NI_NONCE_SIZE * (seq % MAX_DUP_CHK) + i] = 0x100 * (rand() / (RAND_MAX + 1.0));

	memcpy(nonce, &ni_nonce_ptr[NI_NONCE_SIZE * (seq % MAX_DUP_CHK)], NI_NONCE_SIZE);
#else
	memcpy(nonce, &v, sizeof(v));
	niquery_nonce(nonce, 1);
#endif
}

static inline int niquery_check_nonce(__u8 *nonce)
{
#if PING6_NONCE_MEMORY
	__u16 seq = ntohsp((__u16 *)nonce);
	if (memcmp(nonce, &ni_nonce_ptr[NI_NONCE_SIZE * (seq % MAX_DUP_CHK)], NI_NONCE_SIZE))
		return -1;
	return seq;
#else
	return niquery_nonce(nonce, 0);
#endif
}

static int niquery_set_qtype(int type)
{
	if (niquery_is_enabled() && ni_query != type) {
		printf("Qtype conflict\n");
		return -1;
	}
	ni_query = type;
	return 0;
}

static int niquery_option_name_handler(int index, const char *arg)
{
	if (niquery_set_qtype(NI_QTYPE_NAME) < 0)
		return -1;
	return 0;
}

static int niquery_option_ipv6_handler(int index, const char *arg)
{
	if (niquery_set_qtype(NI_QTYPE_IPV6ADDR) < 0)
		return -1;
	return 0;
}

static int niquery_option_ipv6_flag_handler(int index, const char *arg)
{
	if (niquery_set_qtype(NI_QTYPE_IPV6ADDR) < 0)
		return -1;
	ni_flag |= niquery_options[index].data;
	return 0;
}

static int niquery_option_ipv4_handler(int index, const char *arg)
{
	if (niquery_set_qtype(NI_QTYPE_IPV4ADDR) < 0)
		return -1;
	return 0;
}

static int niquery_option_ipv4_flag_handler(int index, const char *arg)
{
	if (niquery_set_qtype(NI_QTYPE_IPV4ADDR) < 0)
		return -1;
	ni_flag |= niquery_options[index].data;
	return 0;
}

static inline int niquery_is_subject_valid(void)
{
	return ni_subject_type >= 0 && ni_subject;
}

static int niquery_set_subject_type(int type)
{
	if (niquery_is_subject_valid() && ni_subject_type != type) {
		printf("Subject type conflict\n");
		return -1;
	}
	ni_subject_type = type;
	return 0;
}

#define ARRAY_SIZE(array)	(sizeof(array) / sizeof(array[0]))
#define OFFSET_OF(type,elem)	((size_t)&((type *)0)->elem)

static int niquery_option_subject_addr_handler(int index, const char *arg)
{
	struct addrinfo hints, *ai0, *ai;
	int offset;
	int gai;

	if (niquery_set_subject_type(niquery_options[index].data) < 0)
		return -1;

	ni_subject_type = niquery_options[index].data;

	memset(&hints, 0, sizeof(hints));

	switch (niquery_options[index].data) {
	case NI_SUBJ_IPV6:
		ni_subject_len = sizeof(struct in6_addr);
		offset = OFFSET_OF(struct sockaddr_in6, sin6_addr);
		hints.ai_family = AF_INET6;
		break;
	case NI_SUBJ_IPV4:
		ni_subject_len = sizeof(struct in_addr);
		offset = OFFSET_OF(struct sockaddr_in, sin_addr);
		hints.ai_family = AF_INET;
		break;
	default:
		/* should not happen. */
		offset = -1;
	}

	hints.ai_socktype = SOCK_DGRAM;
#ifdef USE_IDN
	hints.ai_flags = AI_IDN;
#endif

	gai = getaddrinfo(arg, 0, &hints, &ai0);
	if (gai) {
		fprintf(stderr, "Unknown host: %s\n", arg);
		return -1;
	}

	for (ai = ai0; ai; ai = ai->ai_next) {
		void *p = malloc(ni_subject_len);
		if (!p)
			continue;
		memcpy(p, (__u8 *)ai->ai_addr + offset, ni_subject_len);
		free(ni_subject);
		ni_subject = p;
		break;
	}
	freeaddrinfo(ai0);

	return 0;
}

static int niquery_option_subject_name_handler(int index, const char *arg)
{
	static char nigroup_buf[INET6_ADDRSTRLEN + 1 + IFNAMSIZ];
	unsigned char *dnptrs[2], **dpp, **lastdnptr;
	int n;
	int i;
	char *name, *p;
	char *canonname = NULL, *idn = NULL;
	unsigned char *buf = NULL;
	size_t namelen;
	size_t buflen;
	int dots, fqdn = niquery_options[index].data;
	MD5_CTX ctxt;
	__u8 digest[MD5_DIGEST_LENGTH];
#ifdef USE_IDN
	int rc;
#endif

	if (niquery_set_subject_type(NI_SUBJ_NAME) < 0)
		return -1;

#ifdef USE_IDN
	name = stringprep_locale_to_utf8(arg);
	if (!name) {
		fprintf(stderr, "ping6: IDN support failed.\n");
		exit(2);
	}
#else
	name = strdup(arg);
	if (!name)
		goto oomexit;
#endif

	p = strchr(name, SCOPE_DELIMITER);
	if (p) {
		*p = '\0';
		if (strlen(p + 1) >= IFNAMSIZ) {
			fprintf(stderr, "ping6: too long scope name.\n");
			exit(1);
		}
	}

#ifdef USE_IDN
	rc = idna_to_ascii_8z(name, &idn, 0);
	if (rc) {
		fprintf(stderr, "ping6: IDN encoding error: %s\n",
			idna_strerror(rc));
		exit(2);
	}
#else
	idn = strdup(name);
	if (!idn)
		goto oomexit;
#endif

	namelen = strlen(idn);
	canonname = malloc(namelen + 1);
	if (!canonname)
		goto oomexit;

	dots = 0;
	for (i = 0; i < namelen + 1; i++) {
		canonname[i] = isupper(idn[i]) ? tolower(idn[i]) : idn[i];
		if (idn[i] == '.')
			dots++;
	}

	if (fqdn == 0) {
		/* guess if hostname is FQDN */
		fqdn = dots ? 1 : -1;
	}

	buflen = namelen + 3 + 1;	/* dn_comp() requrires strlen() + 3,
					   plus non-fqdn indicator. */
	buf = malloc(buflen);
	if (!buf) {
		fprintf(stderr, "ping6: out of memory.\n");
		goto errexit;
	}

	dpp = dnptrs;
	lastdnptr = &dnptrs[ARRAY_SIZE(dnptrs)];

	*dpp++ = (unsigned char *)buf;
	*dpp++ = NULL;

	n = dn_comp(canonname, (unsigned char *)buf, buflen, dnptrs, lastdnptr);
	if (n < 0) {
		fprintf(stderr, "ping6: Inappropriate subject name: %s\n", canonname);
		goto errexit;
	} else if (n >= buflen) {
		fprintf(stderr, "ping6: dn_comp() returned too long result.\n");
		goto errexit;
	}

	MD5_Init(&ctxt);
	MD5_Update(&ctxt, buf, buf[0]);
	MD5_Final(digest, &ctxt);

	sprintf(nigroup_buf, "ff02::2:%02x%02x:%02x%02x%s%s",
		digest[0], digest[1], digest[2], digest[3],
		p ? "%" : "",
		p ? p + 1 : "");

	if (fqdn < 0)
		buf[n] = 0;

	free(ni_subject);

	ni_group = nigroup_buf;
	ni_subject = buf;
	ni_subject_len = n + (fqdn < 0);
	ni_group = nigroup_buf;

	free(canonname);
	free(idn);
	free(name);

	return 0;
oomexit:
	fprintf(stderr, "ping6: out of memory.\n");
errexit:
	free(buf);
	free(canonname);
	free(idn);
	free(name);
	exit(1);
}

int niquery_option_help_handler(int index, const char *arg)
{
	fprintf(stderr, "ping6 -N suboptions\n"
			"\tHelp:\n"
			"\t\thelp\n"
			"\tQuery:\n"
			"\t\tname,\n"
			"\t\tipv6,ipv6-all,ipv6-compatible,ipv6-linklocal,ipv6-sitelocal,ipv6-global,\n"
			"\t\tipv4,ipv4-all,\n"
			"\tSubject:\n"
			"\t\tsubject-ipv6=addr,subject-ipv4=addr,subject-name=name,subject-fqdn=name,\n"
		);
	exit(2);
}

int niquery_option_handler(const char *opt_arg)
{
	struct niquery_option *p;
	int i;
	int ret = -1;
	for (i = 0, p = niquery_options; p->name; i++, p++) {
		if (strncmp(p->name, opt_arg, p->namelen))
			continue;
		if (!p->has_arg) {
			if (opt_arg[p->namelen] == '\0') {
				ret = p->handler(i, NULL);
				if (ret >= 0)
					break;
			}
		} else {
			if (opt_arg[p->namelen] == '=') {
				ret = p->handler(i, &opt_arg[p->namelen] + 1);
				if (ret >= 0)
					break;
			}
		}
	}
	if (!p->name)
		ret = niquery_option_help_handler(0, NULL);
	return ret;
}

static int hextoui(const char *str)
{
	unsigned long val;
	char *ep;

	errno = 0;
	val = strtoul(str, &ep, 16);
	if (*ep) {
		if (!errno)
			errno = EINVAL;
		return -1;
	}

	if (val > UINT_MAX) {
		errno = ERANGE;
		return UINT_MAX;
	}

	return val;
}

int main(int argc, char *argv[])
{
	int ch, hold, packlen;
	u_char *packet;
	char *target;
	struct addrinfo hints, *ai;
	int gai;
	struct sockaddr_in6 firsthop;
	int socket_errno;
	struct icmp6_filter filter;
	int err;
#ifdef __linux__
	int csum_offset, sz_opt;
#endif
	static uint32_t scope_id = 0;

	limit_capabilities();

#ifdef USE_IDN
	setlocale(LC_ALL, "");
#endif

	enable_capability_raw();

	icmp_sock = socket(AF_INET6, SOCK_RAW, IPPROTO_ICMPV6);
	socket_errno = errno;

	disable_capability_raw();

	source.sin6_family = AF_INET6;
	memset(&firsthop, 0, sizeof(firsthop));
	firsthop.sin6_family = AF_INET6;

	preload = 1;
	while ((ch = getopt(argc, argv, COMMON_OPTSTR "F:N:")) != EOF) {
		switch(ch) {
		case 'F':
			flowlabel = hextoui(optarg);
			if (errno || (flowlabel & ~IPV6_FLOWINFO_FLOWLABEL)) {
				fprintf(stderr, "ping: Invalid flowinfo %s\n", optarg);
				exit(2);
			}
			options |= F_FLOWINFO;
			break;
		case 'Q':
			tclass = hextoui(optarg);
			if (errno || (tclass & ~0xff)) {
				fprintf(stderr, "ping: Invalid tclass %s\n", optarg);
				exit(2);
			}
			options |= F_TCLASS;
			break;
		case 'I':
			if (strchr(optarg, ':')) {
				char *p, *addr = strdup(optarg);

				if (!addr) {
					fprintf(stderr, "ping: out of memory\n");
					exit(2);
				}

				p = strchr(addr, SCOPE_DELIMITER);
				if (p) {
					*p = '\0';
					device = optarg + (p - addr) + 1;
				}

				if (inet_pton(AF_INET6, addr, (char*)&source.sin6_addr) <= 0) {
					fprintf(stderr, "ping: invalid source address %s\n", optarg);
					exit(2);
				}

				options |= F_STRICTSOURCE;

				free(addr);
			} else {
				device = optarg;
			}
			break;
		case 'M':
			if (strcmp(optarg, "do") == 0)
				pmtudisc = IPV6_PMTUDISC_DO;
			else if (strcmp(optarg, "dont") == 0)
				pmtudisc = IPV6_PMTUDISC_DONT;
			else if (strcmp(optarg, "want") == 0)
				pmtudisc = IPV6_PMTUDISC_WANT;
			else {
				fprintf(stderr, "ping: wrong value for -M: do, dont, want are valid ones.\n");
				exit(2);
			}
			break;
		case 'V':
			printf("ping6 utility, iputils-%s\n", SNAPSHOT);
			exit(0);
		case 'N':
			if (niquery_option_handler(optarg) < 0) {
				usage();
				break;
			}
			break;
		COMMON_OPTIONS
			common_options(ch);
			break;
		default:
			usage();
		}
	}
	argc -= optind;
	argv += optind;

#ifdef ENABLE_PING6_RTHDR
	while (argc > 1) {
		struct in6_addr *addr;

		if (srcrt == NULL) {
			int space;

			fprintf(stderr, "ping6: Warning: "
					"Source routing is deprecated by RFC5095.\n");

#ifdef ENABLE_PING6_RTHDR_RFC3542
			space = inet6_rth_space(IPV6_RTHDR_TYPE_0, argc - 1);
#else
			space = inet6_srcrt_space(IPV6_SRCRT_TYPE_0, argc - 1);
#endif
			if (space == 0)	{
				fprintf(stderr, "srcrt_space failed\n");
				exit(2);
			}
#ifdef ENABLE_PING6_RTHDR_RFC3542
			if (cmsglen + CMSG_SPACE(space) > sizeof(cmsgbuf)) {
				fprintf(stderr, "no room for options\n");
				exit(2);
			}
#else
			if (space + cmsglen > sizeof(cmsgbuf)) {
				fprintf(stderr, "no room for options\n");
				exit(2);
			}
#endif
			srcrt = (struct cmsghdr*)(cmsgbuf+cmsglen);
#ifdef ENABLE_PING6_RTHDR_RFC3542
			memset(srcrt, 0, CMSG_SPACE(0));
			srcrt->cmsg_len = CMSG_LEN(space);
			srcrt->cmsg_level = IPPROTO_IPV6;
			srcrt->cmsg_type = IPV6_RTHDR;
			inet6_rth_init(CMSG_DATA(srcrt), space, IPV6_RTHDR_TYPE_0, argc - 1);
			cmsglen += CMSG_SPACE(space);
#else
			cmsglen += CMSG_ALIGN(space);
			inet6_srcrt_init(srcrt, IPV6_SRCRT_TYPE_0);
#endif
		}

		target = *argv;

		memset(&hints, 0, sizeof(hints));
		hints.ai_family = AF_INET6;
#ifdef USE_IDN
		hints.ai_flags = AI_IDN;
#endif
		gai = getaddrinfo(target, NULL, &hints, &ai);
		if (gai) {
			fprintf(stderr, "unknown host\n");
			exit(2);
		}
		addr = &((struct sockaddr_in6 *)(ai->ai_addr))->sin6_addr;
#ifdef ENABLE_PING6_RTHDR_RFC3542
		inet6_rth_add(CMSG_DATA(srcrt), addr);
#else
		inet6_srcrt_add(srcrt, addr);
#endif
		if (IN6_IS_ADDR_UNSPECIFIED(&firsthop.sin6_addr)) {
			memcpy(&firsthop.sin6_addr, addr, 16);
#ifdef HAVE_SIN6_SCOPEID
			firsthop.sin6_scope_id = ((struct sockaddr_in6 *)(ai->ai_addr))->sin6_scope_id;
			/* Verify scope_id is the same as previous nodes */
			if (firsthop.sin6_scope_id && scope_id && firsthop.sin6_scope_id != scope_id) {
				fprintf(stderr, "scope discrepancy among the nodes\n");
				exit(2);
			} else if (!scope_id) {
				scope_id = firsthop.sin6_scope_id;
			}
#endif
		}
		freeaddrinfo(ai);

		argv++;
		argc--;
	}
#endif

	if (niquery_is_enabled()) {
		niquery_init_nonce();

		if (!niquery_is_subject_valid()) {
			ni_subject = &whereto.sin6_addr;
			ni_subject_len = sizeof(whereto.sin6_addr);
			ni_subject_type = NI_SUBJ_IPV6;
		}
	}

	if (argc > 1) {
#ifndef ENABLE_PING6_RTHDR
		fprintf(stderr, "ping6: Source routing is deprecated by RFC5095.\n");
#endif
		usage();
	} else if (argc == 1) {
		target = *argv;
	} else {
		if (ni_query < 0 && ni_subject_type != NI_SUBJ_NAME)
			usage();
		target = ni_group;
	}

	memset(&hints, 0, sizeof(hints));
	hints.ai_family = AF_INET6;
#ifdef USE_IDN
	hints.ai_flags = AI_IDN;
#endif
	gai = getaddrinfo(target, NULL, &hints, &ai);
	if (gai) {
		fprintf(stderr, "unknown host\n");
		exit(2);
	}

	memcpy(&whereto, ai->ai_addr, sizeof(whereto));
	whereto.sin6_port = htons(IPPROTO_ICMPV6);

	if (memchr(target, ':', strlen(target)))
		options |= F_NUMERIC;

	freeaddrinfo(ai);

	if (IN6_IS_ADDR_UNSPECIFIED(&firsthop.sin6_addr)) {
		memcpy(&firsthop.sin6_addr, &whereto.sin6_addr, 16);
#ifdef HAVE_SIN6_SCOPEID
		firsthop.sin6_scope_id = whereto.sin6_scope_id;
		/* Verify scope_id is the same as intermediate nodes */
		if (firsthop.sin6_scope_id && scope_id && firsthop.sin6_scope_id != scope_id) {
			fprintf(stderr, "scope discrepancy among the nodes\n");
			exit(2);
		} else if (!scope_id) {
			scope_id = firsthop.sin6_scope_id;
		}
#endif
	}

	hostname = target;

	if (IN6_IS_ADDR_UNSPECIFIED(&source.sin6_addr)) {
		socklen_t alen;
		int probe_fd = socket(AF_INET6, SOCK_DGRAM, 0);

		if (probe_fd < 0) {
			perror("socket");
			exit(2);
		}
		if (device) {
#if defined(IPV6_RECVPKTINFO) || defined(HAVE_SIN6_SCOPEID)
			unsigned int iface = if_name2index(device);
#endif
#ifdef IPV6_RECVPKTINFO
			struct in6_pktinfo ipi;

			memset(&ipi, 0, sizeof(ipi));
			ipi.ipi6_ifindex = iface;
#endif

#ifdef HAVE_SIN6_SCOPEID
			if (IN6_IS_ADDR_LINKLOCAL(&firsthop.sin6_addr) ||
			    IN6_IS_ADDR_MC_LINKLOCAL(&firsthop.sin6_addr))
				firsthop.sin6_scope_id = iface;
#endif
			enable_capability_raw();
			if (
#ifdef IPV6_RECVPKTINFO
			    setsockopt(probe_fd, IPPROTO_IPV6, IPV6_PKTINFO, &ipi, sizeof(ipi)) == -1 &&
#endif
			    setsockopt(probe_fd, SOL_SOCKET, SO_BINDTODEVICE, device, strlen(device)+1) == -1) {
				perror("setsockopt(SO_BINDTODEVICE)");
				exit(2);
			}
			disable_capability_raw();
		}
		firsthop.sin6_port = htons(1025);
		if (connect(probe_fd, (struct sockaddr*)&firsthop, sizeof(firsthop)) == -1) {
			perror("connect");
			exit(2);
		}
		alen = sizeof(source);
		if (getsockname(probe_fd, (struct sockaddr*)&source, &alen) == -1) {
			perror("getsockname");
			exit(2);
		}
		source.sin6_port = 0;
		close(probe_fd);

#ifndef WITHOUT_IFADDRS
		if (device) {
			struct ifaddrs *ifa0, *ifa;

			if (getifaddrs(&ifa0)) {
				perror("getifaddrs");
				exit(2);
			}

			for (ifa = ifa0; ifa; ifa = ifa->ifa_next) {
				if (!ifa->ifa_addr || ifa->ifa_addr->sa_family != AF_INET6)
					continue;
				if (!strncmp(ifa->ifa_name, device, sizeof(device) - 1) &&
				    IN6_ARE_ADDR_EQUAL(&((struct sockaddr_in6 *)ifa->ifa_addr)->sin6_addr,
						       &source.sin6_addr))
					break;
			}
			if (!ifa)
				fprintf(stderr, "ping6: Warning: source address might be selected on device other than %s.\n", device);

			freeifaddrs(ifa0);
		}
#endif
	}
#ifdef HAVE_SIN6_SCOPEID
	else if (device && (IN6_IS_ADDR_LINKLOCAL(&source.sin6_addr) ||
			    IN6_IS_ADDR_MC_LINKLOCAL(&source.sin6_addr)))
		source.sin6_scope_id = if_name2index(device);
#endif

	if (icmp_sock < 0) {
		errno = socket_errno;
		perror("ping: icmp open socket");
		exit(2);
	}

	if (device) {
		struct cmsghdr *cmsg;
		struct in6_pktinfo *ipi;

		cmsg = (struct cmsghdr*)(cmsgbuf+cmsglen);
		cmsglen += CMSG_SPACE(sizeof(*ipi));
		cmsg->cmsg_len = CMSG_LEN(sizeof(*ipi));
		cmsg->cmsg_level = SOL_IPV6;
		cmsg->cmsg_type = IPV6_PKTINFO;

		ipi = (struct in6_pktinfo*)CMSG_DATA(cmsg);
		memset(ipi, 0, sizeof(*ipi));
		ipi->ipi6_ifindex = if_name2index(device);
	}

	if ((whereto.sin6_addr.s6_addr16[0]&htons(0xff00)) == htons (0xff00)) {
		if (uid) {
			if (interval < 1000) {
				fprintf(stderr, "ping: multicast ping with too short interval.\n");
				exit(2);
			}
			if (pmtudisc >= 0 && pmtudisc != IPV6_PMTUDISC_DO) {
				fprintf(stderr, "ping: multicast ping does not fragment.\n");
				exit(2);
			}
		}
		if (pmtudisc < 0)
			pmtudisc = IPV6_PMTUDISC_DO;
	}

	if (pmtudisc >= 0) {
		if (setsockopt(icmp_sock, SOL_IPV6, IPV6_MTU_DISCOVER, &pmtudisc, sizeof(pmtudisc)) == -1) {
			perror("ping: IPV6_MTU_DISCOVER");
			exit(2);
		}
	}

	if ((options&F_STRICTSOURCE) &&
	    bind(icmp_sock, (struct sockaddr*)&source, sizeof(source)) == -1) {
		perror("ping: bind icmp socket");
		exit(2);
	}

	if (datalen >= sizeof(struct timeval) && (ni_query < 0)) {
		/* can we time transfer */
		timing = 1;
	}
	packlen = datalen + 8 + 4096 + 40 + 8; /* 4096 for rthdr */
	if (!(packet = (u_char *)malloc((u_int)packlen))) {
		fprintf(stderr, "ping: out of memory.\n");
		exit(2);
	}

	working_recverr = 1;
	hold = 1;
	if (setsockopt(icmp_sock, SOL_IPV6, IPV6_RECVERR, (char *)&hold, sizeof(hold))) {
		fprintf(stderr, "WARNING: your kernel is veeery old. No problems.\n");
		working_recverr = 0;
	}

	/* Estimate memory eaten by single packet. It is rough estimate.
	 * Actually, for small datalen's it depends on kernel side a lot. */
	hold = datalen+8;
	hold += ((hold+511)/512)*(40+16+64+160);
	sock_setbufs(icmp_sock, hold);

#ifdef __linux__
	csum_offset = 2;
	sz_opt = sizeof(int);

	err = setsockopt(icmp_sock, SOL_RAW, IPV6_CHECKSUM, &csum_offset, sz_opt);
	if (err < 0) {
		/* checksum should be enabled by default and setting this
		 * option might fail anyway.
		 */
		fprintf(stderr, "setsockopt(RAW_CHECKSUM) failed - try to continue.");
	}
#endif

	/*
	 *	select icmp echo reply as icmp type to receive
	 */

	ICMP6_FILTER_SETBLOCKALL(&filter);

	if (!working_recverr) {
		ICMP6_FILTER_SETPASS(ICMP6_DST_UNREACH, &filter);
		ICMP6_FILTER_SETPASS(ICMP6_PACKET_TOO_BIG, &filter);
		ICMP6_FILTER_SETPASS(ICMP6_TIME_EXCEEDED, &filter);
		ICMP6_FILTER_SETPASS(ICMP6_PARAM_PROB, &filter);
	}

	if (niquery_is_enabled())
		ICMP6_FILTER_SETPASS(ICMPV6_NI_REPLY, &filter);
	else
		ICMP6_FILTER_SETPASS(ICMP6_ECHO_REPLY, &filter);

	err = setsockopt(icmp_sock, IPPROTO_ICMPV6, ICMP6_FILTER, &filter,
			 sizeof(struct icmp6_filter));

	if (err < 0) {
		perror("setsockopt(ICMP6_FILTER)");
		exit(2);
	}

	if (options & F_NOLOOP) {
		int loop = 0;
		if (setsockopt(icmp_sock, IPPROTO_IPV6, IPV6_MULTICAST_LOOP,
							&loop, sizeof(loop)) == -1) {
			perror ("can't disable multicast loopback");
			exit(2);
		}
	}
	if (options & F_TTL) {
		if (setsockopt(icmp_sock, IPPROTO_IPV6, IPV6_MULTICAST_HOPS,
			       &ttl, sizeof(ttl)) == -1) {
			perror ("can't set multicast hop limit");
			exit(2);
		}
		if (setsockopt(icmp_sock, IPPROTO_IPV6, IPV6_UNICAST_HOPS,
			       &ttl, sizeof(ttl)) == -1) {
			perror ("can't set unicast hop limit");
			exit(2);
		}
	}

	if (1) {
		int on = 1;
		if (
#ifdef IPV6_RECVHOPLIMIT
		    setsockopt(icmp_sock, IPPROTO_IPV6, IPV6_RECVHOPLIMIT,
			       &on, sizeof(on)) == -1 &&
		    setsockopt(icmp_sock, IPPROTO_IPV6, IPV6_2292HOPLIMIT,
			       &on, sizeof(on)) == -1
#else
		    setsockopt(icmp_sock, IPPROTO_IPV6, IPV6_HOPLIMIT,
			       &on, sizeof(on)) == -1
#endif
		   ){
			perror ("can't receive hop limit");
			exit(2);
		}
	}

	if (options & F_TCLASS) {
#ifdef IPV6_TCLASS
		if (setsockopt(icmp_sock, IPPROTO_IPV6, IPV6_TCLASS,
			       &tclass, sizeof(tclass)) == -1) {
			perror ("setsockopt(IPV6_TCLASS)");
			exit(2);
		}
#else
		fprintf(stderr, "Traffic class is not supported.\n");
#endif
	}

	if (options&F_FLOWINFO) {
#ifdef IPV6_FLOWINFO_SEND
		int on = 1;
#endif
#ifdef IPV6_FLOWLABEL_MGR
		char freq_buf[CMSG_ALIGN(sizeof(struct in6_flowlabel_req)) + cmsglen];
		struct in6_flowlabel_req *freq = (struct in6_flowlabel_req *)freq_buf;
		int freq_len = sizeof(*freq);
#ifdef ENABLE_PING6_RTHDR
		if (srcrt)
			freq_len = CMSG_ALIGN(sizeof(*freq)) + srcrt->cmsg_len;
#endif
		memset(freq, 0, sizeof(*freq));
		freq->flr_label = htonl(flowlabel & IPV6_FLOWINFO_FLOWLABEL);
		freq->flr_action = IPV6_FL_A_GET;
		freq->flr_flags = IPV6_FL_F_CREATE;
		freq->flr_share = IPV6_FL_S_EXCL;
		memcpy(&freq->flr_dst, &whereto.sin6_addr, 16);
#ifdef ENABLE_PING6_RTHDR
		if (srcrt)
			memcpy(freq_buf + CMSG_ALIGN(sizeof(*freq)), srcrt, srcrt->cmsg_len);
#endif
		if (setsockopt(icmp_sock, IPPROTO_IPV6, IPV6_FLOWLABEL_MGR,
			       freq, freq_len) == -1) {
			perror ("can't set flowlabel");
			exit(2);
		}
		flowlabel = freq->flr_label;
#ifdef ENABLE_PING6_RTHDR
		if (srcrt) {
			cmsglen = (char*)srcrt - (char*)cmsgbuf;
			srcrt = NULL;
		}
#endif
#else
		fprintf(stderr, "Flow labels are not supported.\n");
		exit(2);
#endif

#ifdef IPV6_FLOWINFO_SEND
		whereto.sin6_flowinfo = flowlabel;
		if (setsockopt(icmp_sock, IPPROTO_IPV6, IPV6_FLOWINFO_SEND,
			       &on, sizeof(on)) == -1) {
			perror ("can't send flowinfo");
			exit(2);
		}
#else
		fprintf(stderr, "Flowinfo is not supported.\n");
		exit(2);
#endif
	}

	// Cabecalho inicial
	print_header();

	/*
	printf("PING %s(%s) ", hostname, pr_addr(&whereto.sin6_addr));
	if (flowlabel)
		printf(", flow 0x%05x, ", (unsigned)ntohl(flowlabel));
	if (device || (options&F_STRICTSOURCE)) {
		printf("from %s %s: ",
		       pr_addr_n(&source.sin6_addr), device ? : "");
	}
	printf("%d data bytes\n", datalen);
	*/

	setup(icmp_sock);

	drop_capabilities();

	main_loop(icmp_sock, packet, packlen);
}

int receive_error_msg()
{
	int res;
	char cbuf[512];
	struct iovec  iov;
	struct msghdr msg;
	struct cmsghdr *cmsg;
	struct sock_extended_err *e;
	struct icmp6_hdr icmph;
	struct sockaddr_in6 target;
	int net_errors = 0;
	int local_errors = 0;
	int saved_errno = errno;

	iov.iov_base = &icmph;
	iov.iov_len = sizeof(icmph);
	msg.msg_name = (void*)&target;
	msg.msg_namelen = sizeof(target);
	msg.msg_iov = &iov;
	msg.msg_iovlen = 1;
	msg.msg_flags = 0;
	msg.msg_control = cbuf;
	msg.msg_controllen = sizeof(cbuf);

	res = recvmsg(icmp_sock, &msg, MSG_ERRQUEUE|MSG_DONTWAIT);
	if (res < 0)
		goto out;

	e = NULL;
	for (cmsg = CMSG_FIRSTHDR(&msg); cmsg; cmsg = CMSG_NXTHDR(&msg, cmsg)) {
		if (cmsg->cmsg_level == SOL_IPV6) {
			if (cmsg->cmsg_type == IPV6_RECVERR)
				e = (struct sock_extended_err *)CMSG_DATA(cmsg);
		}
	}
	if (e == NULL)
		abort();

	if (e->ee_origin == SO_EE_ORIGIN_LOCAL) {
		local_errors++;
		if (options & F_QUIET)
			goto out;
		if (options & F_FLOOD)
			write_stdout("E", 1);
		else if (e->ee_errno != EMSGSIZE)
			fprintf(stderr, "ping: local error: %s\n", strerror(e->ee_errno));
		else
			fprintf(stderr, "ping: local error: Message too long, mtu=%u\n", e->ee_info);
		nerrors++;
	} else if (e->ee_origin == SO_EE_ORIGIN_ICMP6) {
		struct sockaddr_in6 *sin6 = (struct sockaddr_in6*)(e+1);

		if (res < sizeof(icmph) ||
		    memcmp(&target.sin6_addr, &whereto.sin6_addr, 16) ||
		    icmph.icmp6_type != ICMP6_ECHO_REQUEST ||
		    icmph.icmp6_id != ident) {
			/* Not our error, not an error at all. Clear. */
			saved_errno = 0;
			goto out;
		}

		net_errors++;
		nerrors++;
		if (options & F_QUIET)
			goto out;
		if (options & F_FLOOD) {
			write_stdout("\bE", 2);
		} else {
			print_timestamp();
			printf("From %s icmp_seq=%u ", pr_addr(&sin6->sin6_addr), ntohs(icmph.icmp6_seq));
			pr_icmph(e->ee_type, e->ee_code, e->ee_info);
			putchar('\n');
			fflush(stdout);
		}
	}

out:
	errno = saved_errno;
	return net_errors ? : -local_errors;
}

// imprimir cabecalho
void print_header(){

	printf("%s%s SEQ HOST                                      SIZE TTL TIME  STATUS%s\n",  FONT_BOLD, LWHT, RESET);

// 65535 
}


/*
 * pinger --
 * 	Compose and transmit an ICMP ECHO REQUEST packet.  The IP packet
 * will be added on by the kernel.  The ID field is our UNIX process ID,
 * and the sequence number is an ascending integer.  The first 8 bytes
 * of the data portion are used to hold a UNIX "timeval" struct in VAX
 * byte-order, to compute the round-trip time.
 */
int build_echo(__u8 *_icmph)
{
	struct icmp6_hdr *icmph;
	int cc;

	icmph = (struct icmp6_hdr *)_icmph;
	icmph->icmp6_type = ICMP6_ECHO_REQUEST;
	icmph->icmp6_code = 0;
	icmph->icmp6_cksum = 0;
	icmph->icmp6_seq = htons(ntransmitted+1);
	icmph->icmp6_id = ident;

	if (timing)
		gettimeofday((struct timeval *)&outpack[8],
		    (struct timezone *)NULL);

	cc = datalen + 8;			/* skips ICMP portion */

	return cc;
}


int build_niquery(__u8 *_nih)
{
	struct ni_hdr *nih;
	int cc;

	nih = (struct ni_hdr *)_nih;
	nih->ni_cksum = 0;

	nih->ni_type = ICMPV6_NI_QUERY;
	cc = sizeof(*nih);
	datalen = 0;

	niquery_fill_nonce(ntransmitted + 1, nih->ni_nonce);
	nih->ni_code = ni_subject_type;
	nih->ni_qtype = htons(ni_query);
	nih->ni_flags = ni_flag;
	memcpy(nih + 1, ni_subject, ni_subject_len);
	cc += ni_subject_len;

	return cc;
}

int send_probe(void)
{
	int len, cc;

	rcvd_clear(ntransmitted + 1);

	if (niquery_is_enabled())
		len = build_niquery(outpack);
	else
		len = build_echo(outpack);

	if (cmsglen == 0) {
		cc = sendto(icmp_sock, (char *)outpack, len, confirm,
			    (struct sockaddr *) &whereto,
			    sizeof(struct sockaddr_in6));
	} else {
		struct msghdr mhdr;
		struct iovec iov;

		iov.iov_len  = len;
		iov.iov_base = outpack;

		memset(&mhdr, 0, sizeof(mhdr));
		mhdr.msg_name = &whereto;
		mhdr.msg_namelen = sizeof(struct sockaddr_in6);
		mhdr.msg_iov = &iov;
		mhdr.msg_iovlen = 1;
		mhdr.msg_control = cmsgbuf;
		mhdr.msg_controllen = cmsglen;

		cc = sendmsg(icmp_sock, &mhdr, confirm);
	}
	confirm = 0;

	return (cc == len ? 0 : cc);
}

void pr_echo_reply(__u8 *_icmph, int cc)
{
	struct icmp6_hdr *icmph = (struct icmp6_hdr *) _icmph;
	printf("%4u ", ntohs(icmph->icmp6_seq));
};


static void putchar_safe(char c)
{
	if (isprint(c))
		putchar(c);
	else
		printf("\\%03o", c);
}

void pr_niquery_reply_name(struct ni_hdr *nih, int len)
{
	__u8 *h = (__u8 *)(nih + 1);
	__u8 *p = h + 4;
	__u8 *end = (__u8 *)nih + len;
	int continued = 0;
	char buf[1024];
	int ret;

	len -= sizeof(struct ni_hdr) + 4;

	if (len < 0) {
		printf(" parse error (too short)");
		return;
	}
	while (p < end) {
		int fqdn = 1;
		int i;

		memset(buf, 0xff, sizeof(buf));

		if (continued)
			putchar(',');

		ret = dn_expand(h, end, p, buf, sizeof(buf));
		if (ret < 0) {
			printf(" parse error (truncated)");
			break;
		}
		if (p + ret < end && *(p + ret) == '\0')
			fqdn = 0;

		putchar(' ');
		for (i = 0; i < strlen(buf); i++)
			putchar_safe(buf[i]);
		if (fqdn)
			putchar('.');

		p += ret + !fqdn;

		continued = 1;
	}
}

void pr_niquery_reply_addr(struct ni_hdr *nih, int len)
{
	__u8 *h = (__u8 *)(nih + 1);
	__u8 *p = h + 4;
	__u8 *end = (__u8 *)nih + len;
	int af;
	int aflen;
	int continued = 0;
	int truncated;
	char buf[1024];

	switch (ntohs(nih->ni_qtype)) {
	case NI_QTYPE_IPV4ADDR:
		af = AF_INET;
		aflen = sizeof(struct in_addr);
		truncated = nih->ni_flags & NI_IPV6ADDR_F_TRUNCATE;
		break;
	case NI_QTYPE_IPV6ADDR:
		af = AF_INET6;
		aflen = sizeof(struct in6_addr);
		truncated = nih->ni_flags & NI_IPV4ADDR_F_TRUNCATE;
		break;
	default:
		/* should not happen */
		af = aflen = truncated = 0;
	}
	p = h;
	if (len < 0) {
		printf(" parse error (too short)");
		return;
	}

	while (p < end) {
		if (continued)
			putchar(',');

		if (p + sizeof(__u32) + aflen > end) {
			printf(" parse error (truncated)");
			break;
		}
		if (!inet_ntop(af, p + sizeof(__u32), buf, sizeof(buf)))
			printf(" unexpeced error in inet_ntop(%s)",
			       strerror(errno));
		else
			printf(" %s", buf);
		p += sizeof(__u32) + aflen;

		continued = 1;
	}
	if (truncated)
		printf(" (truncated)");
}

void pr_niquery_reply(__u8 *_nih, int len)
{
	struct ni_hdr *nih = (struct ni_hdr *)_nih;

	switch (nih->ni_code) {
	case NI_SUCCESS:
		switch (ntohs(nih->ni_qtype)) {
		case NI_QTYPE_NAME:
			pr_niquery_reply_name(nih, len);
			break;
		case NI_QTYPE_IPV4ADDR:
		case NI_QTYPE_IPV6ADDR:
			pr_niquery_reply_addr(nih, len);
			break;
		default:
			printf(" unknown qtype(0x%02x)", ntohs(nih->ni_qtype));
		}
		break;
	case NI_REFUSED:
		printf(" refused");
		break;
	case NI_UNKNOWN:
		printf(" unknown");
		break;
	default:
		printf(" unknown code(%02x)", ntohs(nih->ni_code));
	}
	printf("; seq=%u;", ntohsp((__u16*)nih->ni_nonce));
}

/*
 * parse_reply --
 *	Print out the packet, if it came from us.  This logic is necessary
 * because ALL readers of the ICMP socket get a copy of ALL ICMP packets
 * which arrive ('tis only fair).  This permits multiple copies of this
 * program to be run without having intermingled output (or statistics!).
 */
int
parse_reply(struct msghdr *msg, int cc, void *addr, struct timeval *tv)
{
	struct sockaddr_in6 *from = addr;
	__u8 *buf = msg->msg_iov->iov_base;
	struct cmsghdr *c;
	struct icmp6_hdr *icmph;
	int hops = -1;

	for (c = CMSG_FIRSTHDR(msg); c; c = CMSG_NXTHDR(msg, c)) {
		if (c->cmsg_level != SOL_IPV6)
			continue;
		switch(c->cmsg_type) {
		case IPV6_HOPLIMIT:
#ifdef IPV6_2292HOPLIMIT
		case IPV6_2292HOPLIMIT:
#endif
			if (c->cmsg_len < CMSG_LEN(sizeof(int)))
				continue;
			memcpy(&hops, CMSG_DATA(c), sizeof(hops));
		}
	}


	/* Now the ICMP part */

	icmph = (struct icmp6_hdr *) buf;
	if (cc < 8) {
		if (options & F_VERBOSE)
			fprintf(stderr, "ping: packet too short (%d bytes)\n", cc);
		return 1;
	}

	if (icmph->icmp6_type == ICMP6_ECHO_REPLY) {
		if (icmph->icmp6_id != ident)
			return 1;
		if (gather_statistics((__u8*)icmph, sizeof(*icmph), cc,
				      ntohs(icmph->icmp6_seq),
				      hops, 0, tv, pr_addr(&from->sin6_addr),
				      pr_echo_reply))
			return 0;
	} else if (icmph->icmp6_type == ICMPV6_NI_REPLY) {
		struct ni_hdr *nih = (struct ni_hdr *)icmph;
		int seq = niquery_check_nonce(nih->ni_nonce);
		if (seq < 0)
			return 1;
		if (gather_statistics((__u8*)icmph, sizeof(*icmph), cc,
				      seq,
				      hops, 0, tv, pr_addr(&from->sin6_addr),
				      pr_niquery_reply))
			return 0;
	} else {
		int nexthdr;
		struct ip6_hdr *iph1 = (struct ip6_hdr*)(icmph+1);
		struct icmp6_hdr *icmph1 = (struct icmp6_hdr *)(iph1+1);

		/* We must not ever fall here. All the messages but
		 * echo reply are blocked by filter and error are
		 * received with IPV6_RECVERR. Ugly code is preserved
		 * however, just to remember what crap we avoided
		 * using RECVRERR. :-)
		 */

		if (cc < 8+sizeof(struct ip6_hdr)+8)
			return 1;

		if (memcmp(&iph1->ip6_dst, &whereto.sin6_addr, 16))
			return 1;

		nexthdr = iph1->ip6_nxt;

		if (nexthdr == 44) {
			nexthdr = *(__u8*)icmph1;
			icmph1++;
		}
		if (nexthdr == IPPROTO_ICMPV6) {
			if (icmph1->icmp6_type != ICMP6_ECHO_REQUEST ||
			    icmph1->icmp6_id != ident)
				return 1;
			acknowledge(ntohs(icmph1->icmp6_seq));
			if (working_recverr)
				return 0;
			nerrors++;
			if (options & F_FLOOD) {
				write_stdout("\bE", 2);
				return 0;
			}
			print_timestamp();
			printf("From %s: icmp_seq=%u ", pr_addr(&from->sin6_addr), ntohs(icmph1->icmp6_seq));
		} else {
			/* We've got something other than an ECHOREPLY */
			if (!(options & F_VERBOSE) || uid)
				return 1;
			print_timestamp();
			printf("From %s: ", pr_addr(&from->sin6_addr));
		}
		pr_icmph(icmph->icmp6_type, icmph->icmp6_code, ntohl(icmph->icmp6_mtu));
	}

	if (!(options & F_FLOOD)) {
		if (options & F_AUDIBLE)
			putchar('\a');
		putchar('\n');
		fflush(stdout);
	} else {
		putchar('\a');
		fflush(stdout);
	}
	return 0;
}


int pr_icmph(__u8 type, __u8 code, __u32 info)
{
	switch(type) {
	case ICMP6_DST_UNREACH:
		printf("Destination unreachable: ");
		switch (code) {
		case ICMP6_DST_UNREACH_NOROUTE:
			printf("No route");
			break;
		case ICMP6_DST_UNREACH_ADMIN:
			printf("Administratively prohibited");
			break;
		case ICMP6_DST_UNREACH_BEYONDSCOPE:
			printf("Beyond scope of source address");
			break;
		case ICMP6_DST_UNREACH_ADDR:
			printf("Address unreachable");
			break;
		case ICMP6_DST_UNREACH_NOPORT:
			printf("Port unreachable");
			break;
		default:
			printf("Unknown code %d", code);
			break;
		}
		break;
	case ICMP6_PACKET_TOO_BIG:
		printf("Packet too big: mtu=%u", info);
		if (code)
			printf(", code=%d", code);
		break;
	case ICMP6_TIME_EXCEEDED:
		printf("Time exceeded: ");
		if (code == ICMP6_TIME_EXCEED_TRANSIT)
			printf("Hop limit");
		else if (code == ICMP6_TIME_EXCEED_REASSEMBLY)
			printf("Defragmentation failure");
		else
			printf("code %d", code);
		break;
	case ICMP6_PARAM_PROB:
		printf("Parameter problem: ");
		if (code == ICMP6_PARAMPROB_HEADER)
			printf("Wrong header field ");
		else if (code == ICMP6_PARAMPROB_NEXTHEADER)
			printf("Unknown header ");
		else if (code == ICMP6_PARAMPROB_OPTION)
			printf("Unknown option ");
		else
			printf("code %d ", code);
		printf ("at %u", info);
		break;
	case ICMP6_ECHO_REQUEST:
		printf("Echo request");
		break;
	case ICMP6_ECHO_REPLY:
		printf("Echo reply");
		break;
	case MLD_LISTENER_QUERY:
		printf("MLD Query");
		break;
	case MLD_LISTENER_REPORT:
		printf("MLD Report");
		break;
	case MLD_LISTENER_REDUCTION:
		printf("MLD Reduction");
		break;
	default:
		printf("unknown icmp type: %u", type);

	}
	return 0;
}

#include <linux/filter.h>

void install_filter(void)
{
	static int once;
	static struct sock_filter insns[] = {
		BPF_STMT(BPF_LD|BPF_H|BPF_ABS, 4),  /* Load icmp echo ident */
		BPF_JUMP(BPF_JMP|BPF_JEQ|BPF_K, 0xAAAA, 0, 1),  /* Ours? */
		BPF_STMT(BPF_RET|BPF_K, ~0U),  /* Yes, it passes. */
		BPF_STMT(BPF_LD|BPF_B|BPF_ABS, 0),  /* Load icmp type */
		BPF_JUMP(BPF_JMP|BPF_JEQ|BPF_K, ICMP6_ECHO_REPLY, 1, 0), /* Echo? */
		BPF_STMT(BPF_RET|BPF_K, ~0U), /* No. It passes. This must not happen. */
		BPF_STMT(BPF_RET|BPF_K, 0), /* Echo with wrong ident. Reject. */
	};
	static struct sock_fprog filter = {
		sizeof insns / sizeof(insns[0]),
		insns
	};

	if (once)
		return;
	once = 1;

	/* Patch bpflet for current identifier. */
	insns[1] = (struct sock_filter)BPF_JUMP(BPF_JMP|BPF_JEQ|BPF_K, htons(ident), 0, 1);

	if (setsockopt(icmp_sock, SOL_SOCKET, SO_ATTACH_FILTER, &filter, sizeof(filter)))
		perror("WARNING: failed to install socket filter\n");
}


/*
 * pr_addr --
 *	Return an ascii host address as a dotted quad and optionally with
 * a hostname.
 */
char * pr_addr(struct in6_addr *addr)
{
	struct hostent *hp = NULL;
	static char *s;

#ifdef USE_IDN
	free(s);
#endif

	in_pr_addr = !setjmp(pr_addr_jmp);

	if (!(exiting || options&F_NUMERIC))
		hp = gethostbyaddr((__u8*)addr, sizeof(struct in6_addr), AF_INET6);

	in_pr_addr = 0;

	if (!hp
#ifdef USE_IDN
	    || idna_to_unicode_lzlz(hp->h_name, &s, 0) != IDNA_SUCCESS
#endif
	    )
		s = NULL;

	return hp ? (s ? s : hp->h_name) : pr_addr_n(addr);
}

char * pr_addr_n(struct in6_addr *addr)
{
	static char str[64];
	inet_ntop(AF_INET6, addr, str, sizeof(str));
	return str;
}

#define USAGE_NEWLINE	"\n            "

void usage(void)
{
	fprintf(stderr,
		"Usage: ping6"
		" [-"
			"aAbBdDfhLnOqrRUvV"
		"]"
		" [-c count]"
		" [-i interval]"
		" [-I interface]"
		USAGE_NEWLINE
		" [-l preload]"
		" [-m mark]"
		" [-M pmtudisc_option]"
		USAGE_NEWLINE
		" [-N nodeinfo_option]"
		" [-p pattern]"
		" [-Q tclass]"
		" [-s packetsize]"
		USAGE_NEWLINE
		" [-S sndbuf]"
		" [-t ttl]"
		" [-T timestamp_option]"
		" [-w deadline]"
		USAGE_NEWLINE
		" [-W timeout]"
#ifdef ENABLE_PING6_RTHDR
		" [hop1 ...]"
#endif
		" destination"
		"\n"
	);
	exit(2);
}


File: /ping6_niquery.h
#include <asm/byteorder.h>

#define NI_NONCE_SIZE			8

/* Node Information Query */
struct ni_hdr {
	struct icmp6_hdr		ni_u;
	__u8				ni_nonce[NI_NONCE_SIZE];
};

#define ni_type		ni_u.icmp6_type
#define ni_code		ni_u.icmp6_code
#define ni_cksum	ni_u.icmp6_cksum
#define ni_qtype	ni_u.icmp6_data16[0]
#define ni_flags	ni_u.icmp6_data16[1]

/* Types */
#ifndef ICMPV6_NI_QUERY
# define ICMPV6_NI_QUERY		139
# define ICMPV6_NI_REPLY		140
#endif

/* Query Codes */
#define NI_SUBJ_IPV6			0
#define NI_SUBJ_NAME			1
#define NI_SUBJ_IPV4			2

/* Reply Codes */
#define NI_SUCCESS			0
#define NI_REFUSED			1
#define NI_UNKNOWN			2

/* Qtypes */
#define NI_QTYPE_NOOP			0
#define NI_QTYPE_NAME			2
#define NI_QTYPE_IPV6ADDR		3
#define NI_QTYPE_IPV4ADDR		4

/* Flags */
#define NI_IPV6ADDR_F_TRUNCATE		__constant_cpu_to_be16(0x0001)
#define NI_IPV6ADDR_F_ALL		__constant_cpu_to_be16(0x0002)
#define NI_IPV6ADDR_F_COMPAT		__constant_cpu_to_be16(0x0004)
#define NI_IPV6ADDR_F_LINKLOCAL		__constant_cpu_to_be16(0x0008)
#define NI_IPV6ADDR_F_SITELOCAL		__constant_cpu_to_be16(0x0010)
#define NI_IPV6ADDR_F_GLOBAL		__constant_cpu_to_be16(0x0020)

#define NI_IPV4ADDR_F_TRUNCATE		NI_IPV6ADDR_F_TRUNCATE
#define NI_IPV4ADDR_F_ALL		NI_IPV6ADDR_F_ALL



File: /ping_common.c
#include "ping_common.h"
#include <ctype.h>
#include <sched.h>
#include <math.h>

int options;

int mark;
int sndbuf;
int ttl;
int rtt;
int rtt_addend;
__u16 acked;

struct rcvd_table rcvd_tbl;


/* counters */
long npackets;			/* max packets to transmit */
long nreceived;			/* # of packets we got back */
long nrepeats;			/* number of duplicates */
long ntransmitted;		/* sequence # for outbound packets = #sent */
long nchecksum;			/* replies with bad checksum */
long nerrors;			/* icmp errors */
int interval = 1000;		/* interval between packets (msec) */
int preload;
int deadline = 0;		/* time to die */
int lingertime = MAXWAIT*1000;
struct timeval start_time, cur_time;
volatile int exiting;
volatile int status_snapshot;
int confirm = 0;
volatile int in_pr_addr = 0;	/* pr_addr() is executing */
jmp_buf pr_addr_jmp;

/* Stupid workarounds for bugs/missing functionality in older linuces.
 * confirm_flag fixes refusing service of kernels without MSG_CONFIRM.
 * i.e. for linux-2.2 */
int confirm_flag = MSG_CONFIRM;
/* And this is workaround for bug in IP_RECVERR on raw sockets which is present
 * in linux-2.2.[0-19], linux-2.4.[0-7] */
int working_recverr;

/* timing */
int timing;			/* flag to do timing */
long tmin = LONG_MAX;		/* minimum round trip time */
long tmax;			/* maximum round trip time */
/* Message for rpm maintainers: have _shame_. If you want
 * to fix something send the patch to me for sanity checking.
 * "sparcfix" patch is a complete non-sense, apparenly the person
 * prepared it was stoned.
 */
long long tsum;			/* sum of all times, for doing average */
long long tsum2;
int  pipesize = -1;

int datalen = DEFDATALEN;

char *hostname;
int uid;
uid_t euid;
int ident;			/* process id to identify our packets */

static int screen_width = INT_MAX;

#define ARRAY_SIZE(a)	(sizeof(a) / sizeof(a[0]))

#ifdef CAPABILITIES
static cap_value_t cap_raw = CAP_NET_RAW;
static cap_value_t cap_admin = CAP_NET_ADMIN;
#endif

void limit_capabilities(void)
{
#ifdef CAPABILITIES
	cap_t cap_cur_p;
	cap_t cap_p;
	cap_flag_value_t cap_ok;

	cap_cur_p = cap_get_proc();
	if (!cap_cur_p) {
		perror("ping: cap_get_proc");
		exit(-1);
	}

	cap_p = cap_init();
	if (!cap_p) {
		perror("ping: cap_init");
		exit(-1);
	}

	cap_ok = CAP_CLEAR;
	cap_get_flag(cap_cur_p, CAP_NET_ADMIN, CAP_PERMITTED, &cap_ok);

	if (cap_ok != CAP_CLEAR)
		cap_set_flag(cap_p, CAP_PERMITTED, 1, &cap_admin, CAP_SET);

	cap_ok = CAP_CLEAR;
	cap_get_flag(cap_cur_p, CAP_NET_RAW, CAP_PERMITTED, &cap_ok);

	if (cap_ok != CAP_CLEAR)
		cap_set_flag(cap_p, CAP_PERMITTED, 1, &cap_raw, CAP_SET);

	if (cap_set_proc(cap_p) < 0) {
		perror("ping: cap_set_proc");
		exit(-1);
	}

	if (prctl(PR_SET_KEEPCAPS, 1) < 0) {
		perror("ping: prctl");
		exit(-1);
	}

	if (setuid(getuid()) < 0) {
		perror("setuid");
		exit(-1);
	}

	if (prctl(PR_SET_KEEPCAPS, 0) < 0) {
		perror("ping: prctl");
		exit(-1);
	}

	cap_free(cap_p);
	cap_free(cap_cur_p);
#endif
	uid = getuid();
	euid = geteuid();
#ifndef CAPABILITIES
	if (seteuid(uid)) {
		perror("ping: setuid");
		exit(-1);
	}
#endif
}

#ifdef CAPABILITIES
int modify_capability(cap_value_t cap, cap_flag_value_t on)
{
	cap_t cap_p = cap_get_proc();
	cap_flag_value_t cap_ok;
	int rc = -1;

	if (!cap_p) {
		perror("ping: cap_get_proc");
		goto out;
	}

	cap_ok = CAP_CLEAR;
	cap_get_flag(cap_p, cap, CAP_PERMITTED, &cap_ok);
	if (cap_ok == CAP_CLEAR) {
		rc = on ? -1 : 0;
		goto out;
	}

	cap_set_flag(cap_p, CAP_EFFECTIVE, 1, &cap, on);

	if (cap_set_proc(cap_p) < 0) {
		perror("ping: cap_set_proc");
		goto out;
	}

	cap_free(cap_p);

	rc = 0;
out:
	if (cap_p)
		cap_free(cap_p);
	return rc;
}
#else
int modify_capability(int on)
{
	if (seteuid(on ? euid : getuid())) {
		perror("seteuid");
		return -1;
	}

	return 0;
}
#endif

void drop_capabilities(void)
{
#ifdef CAPABILITIES
	cap_t cap = cap_init();
	if (cap_set_proc(cap) < 0) {
		perror("ping: cap_set_proc");
		exit(-1);
	}
	cap_free(cap);
#else
	if (setuid(getuid())) {
		perror("ping: setuid");
		exit(-1);
	}
#endif
}

/* Fills all the outpack, excluding ICMP header, but _including_
 * timestamp area with supplied pattern.
 */
static void fill(char *patp)
{
	int ii, jj, kk;
	int pat[16];
	char *cp;
	u_char *bp = outpack+8;

#ifdef USE_IDN
	setlocale(LC_ALL, "C");
#endif

	for (cp = patp; *cp; cp++) {
		if (!isxdigit(*cp)) {
			fprintf(stderr,
				"ping: patterns must be specified as hex digits.\n");
			exit(2);
		}
	}
	ii = sscanf(patp,
	    "%2x%2x%2x%2x%2x%2x%2x%2x%2x%2x%2x%2x%2x%2x%2x%2x",
	    &pat[0], &pat[1], &pat[2], &pat[3], &pat[4], &pat[5], &pat[6],
	    &pat[7], &pat[8], &pat[9], &pat[10], &pat[11], &pat[12],
	    &pat[13], &pat[14], &pat[15]);

	if (ii > 0) {
		for (kk = 0; kk <= maxpacket - (8 + ii); kk += ii)
			for (jj = 0; jj < ii; ++jj)
				bp[jj + kk] = pat[jj];
	}
	if (!(options & F_QUIET)) {
		printf("PATTERN: 0x");
		for (jj = 0; jj < ii; ++jj)
			printf("%02x", bp[jj] & 0xFF);
		printf("\n");
	}

#ifdef USE_IDN
	setlocale(LC_ALL, "");
#endif
}

void common_options(int ch)
{
	switch(ch) {
	case 'a':
		options |= F_AUDIBLE;
		break;
	case 'A':
		options |= F_ADAPTIVE;
		break;
	case 'c':
		npackets = atoi(optarg);
		if (npackets <= 0) {
			fprintf(stderr, "ping: bad number of packets to transmit.\n");
			exit(2);
		}
		break;
	case 'd':
		options |= F_SO_DEBUG;
		break;
	case 'D':
		options |= F_PTIMEOFDAY;
		break;
	case 'i':		/* wait between sending packets */
	{
		double dbl;
		char *ep;

		errno = 0;
		dbl = strtod(optarg, &ep);

		if (errno || *ep != '\0' ||
		    !finite(dbl) || dbl < 0.0 || dbl >= (double)INT_MAX / 1000 - 1.0) {
			fprintf(stderr, "ping: bad timing interval\n");
			exit(2);
		}

		interval = (int)(dbl * 1000);

		options |= F_INTERVAL;
		break;
	}
	case 'm':
	{
		char *endp;
		mark = (int)strtoul(optarg, &endp, 10);
		if (mark < 0 || *endp != '\0') {
			fprintf(stderr, "mark cannot be negative\n");
			exit(2);
		}
		options |= F_MARK;
		break;
	}
	case 'w':
		deadline = atoi(optarg);
		if (deadline < 0) {
			fprintf(stderr, "ping: bad wait time.\n");
			exit(2);
		}
		break;
	case 'l':
		preload = atoi(optarg);
		if (preload <= 0) {
			fprintf(stderr, "ping: bad preload value, should be 1..%d\n", MAX_DUP_CHK);
			exit(2);
		}
		if (preload > MAX_DUP_CHK)
			preload = MAX_DUP_CHK;
		if (uid && preload > 3) {
			fprintf(stderr, "ping: cannot set preload to value > 3\n");
			exit(2);
		}
		break;
	case 'O':
		options |= F_OUTSTANDING;
		break;
	case 'S':
		sndbuf = atoi(optarg);
		if (sndbuf <= 0) {
			fprintf(stderr, "ping: bad sndbuf value.\n");
			exit(2);
		}
		break;
	case 'f':
		options |= F_FLOOD;
		setbuf(stdout, (char *)NULL);
		/* fallthrough to numeric - avoid gethostbyaddr during flood */
	case 'n':
		options |= F_NUMERIC;
		break;
	case 'p':		/* fill buffer with user pattern */
		options |= F_PINGFILLED;
		fill(optarg);
		break;
	case 'q':
		options |= F_QUIET;
		break;
	case 'r':
		options |= F_SO_DONTROUTE;
		break;
	case 's':		/* size of packet to send */
		datalen = atoi(optarg);
		if (datalen < 0) {
			fprintf(stderr, "ping: illegal negative packet size %d.\n", datalen);
			exit(2);
		}
		if (datalen > maxpacket - 8) {
			fprintf(stderr, "ping: packet size too large: %d\n",
				datalen);
			exit(2);
		}
		break;
	case 'v':
		options |= F_VERBOSE;
		break;
	case 'L':
		options |= F_NOLOOP;
		break;
	case 't':
		options |= F_TTL;
		ttl = atoi(optarg);
		if (ttl < 0 || ttl > 255) {
			fprintf(stderr, "ping: ttl %u out of range\n", ttl);
			exit(2);
		}
		break;
	case 'U':
		options |= F_LATENCY;
		break;
	case 'B':
		options |= F_STRICTSOURCE;
		break;
	case 'W':
		lingertime = atoi(optarg);
		if (lingertime < 0 || lingertime > INT_MAX/1000000) {
			fprintf(stderr, "ping: bad linger time.\n");
			exit(2);
		}
		lingertime *= 1000;
		break;
	case 'V':
		printf("ping utility, iputils-%s\n", SNAPSHOT);
		exit(0);
	default:
		abort();
	}
}


static void sigexit(int signo)
{
	exiting = 1;
	if (in_pr_addr)
		longjmp(pr_addr_jmp, 0);
}

static void sigstatus(int signo)
{
	status_snapshot = 1;
}


int __schedule_exit(int next)
{
	static unsigned long waittime;
	struct itimerval it;

	if (waittime)
		return next;

	if (nreceived) {
		waittime = 2 * tmax;
		if (waittime < 1000*interval)
			waittime = 1000*interval;
	} else
		waittime = lingertime*1000;

	if (next < 0 || next < waittime/1000)
		next = waittime/1000;

	it.it_interval.tv_sec = 0;
	it.it_interval.tv_usec = 0;
	it.it_value.tv_sec = waittime/1000000;
	it.it_value.tv_usec = waittime%1000000;
	setitimer(ITIMER_REAL, &it, NULL);
	return next;
}

static inline void update_interval(void)
{
	int est = rtt ? rtt/8 : interval*1000;

	interval = (est+rtt_addend+500)/1000;
	if (uid && interval < MINUSERINTERVAL)
		interval = MINUSERINTERVAL;
}

/*
 * Print timestamp
 */
void print_timestamp(void)
{
	if (options & F_PTIMEOFDAY) {
		struct timeval tv;
		gettimeofday(&tv, NULL);
		printf("[%lu.%06lu] ",
		       (unsigned long)tv.tv_sec, (unsigned long)tv.tv_usec);
	}
}

/*
 * pinger --
 * 	Compose and transmit an ICMP ECHO REQUEST packet.  The IP packet
 * will be added on by the kernel.  The ID field is our UNIX process ID,
 * and the sequence number is an ascending integer.  The first 8 bytes
 * of the data portion are used to hold a UNIX "timeval" struct in VAX
 * byte-order, to compute the round-trip time.
 */
int pinger(void)
{
	static int oom_count;
	static int tokens;
	int i;

	/* Have we already sent enough? If we have, return an arbitrary positive value. */
	if (exiting || (npackets && ntransmitted >= npackets && !deadline))
		return 1000;

	/* Check that packets < rate*time + preload */
	if (cur_time.tv_sec == 0) {
		gettimeofday(&cur_time, NULL);
		tokens = interval*(preload-1);
	} else {
		long ntokens;
		struct timeval tv;

		gettimeofday(&tv, NULL);
		ntokens = (tv.tv_sec - cur_time.tv_sec)*1000 +
			(tv.tv_usec-cur_time.tv_usec)/1000;
		if (!interval) {
			/* Case of unlimited flood is special;
			 * if we see no reply, they are limited to 100pps */
			if (ntokens < MININTERVAL && in_flight() >= preload)
				return MININTERVAL-ntokens;
		}
		ntokens += tokens;
		if (ntokens > interval*preload)
			ntokens = interval*preload;
		if (ntokens < interval)
			return interval - ntokens;

		cur_time = tv;
		tokens = ntokens - interval;
	}

	if (options & F_OUTSTANDING) {
		if (ntransmitted > 0 && !rcvd_test(ntransmitted)) {
			print_timestamp();
			printf("no answer yet for icmp_seq=%lu\n", (ntransmitted % MAX_DUP_CHK));
			fflush(stdout);
		}
	}

resend:
	i = send_probe();

	if (i == 0) {
		oom_count = 0;
		advance_ntransmitted();
		if (!(options & F_QUIET) && (options & F_FLOOD)) {
			/* Very silly, but without this output with
			 * high preload or pipe size is very confusing. */
			if ((preload < screen_width && pipesize < screen_width) ||
			    in_flight() < screen_width)
				write_stdout(".", 1);
		}
		return interval - tokens;
	}

	/* And handle various errors... */
	if (i > 0) {
		/* Apparently, it is some fatal bug. */
		abort();
	} else if (errno == ENOBUFS || errno == ENOMEM) {
		int nores_interval;

		/* Device queue overflow or OOM. Packet is not sent. */
		tokens = 0;
		/* Slowdown. This works only in adaptive mode (option -A) */
		rtt_addend += (rtt < 8*50000 ? rtt/8 : 50000);
		if (options&F_ADAPTIVE)
			update_interval();
		nores_interval = SCHINT(interval/2);
		if (nores_interval > 500)
			nores_interval = 500;
		oom_count++;
		if (oom_count*nores_interval < lingertime)
			return nores_interval;
		i = 0;
		/* Fall to hard error. It is to avoid complete deadlock
		 * on stuck output device even when dealine was not requested.
		 * Expected timings are screwed up in any case, but we will
		 * exit some day. :-) */
	} else if (errno == EAGAIN) {
		/* Socket buffer is full. */
		tokens += interval;
		return MININTERVAL;
	} else {
		if ((i=receive_error_msg()) > 0) {
			/* An ICMP error arrived. */
			tokens += interval;
			return MININTERVAL;
		}
		/* Compatibility with old linuces. */
		if (i == 0 && confirm_flag && errno == EINVAL) {
			confirm_flag = 0;
			errno = 0;
		}
		if (!errno)
			goto resend;
	}

	/* Hard local error. Pretend we sent packet. */
	advance_ntransmitted();

	if (i == 0 && !(options & F_QUIET)) {
		if (options & F_FLOOD)
			write_stdout("E", 1);
		else
			perror("ping: sendmsg");
	}
	tokens = 0;
	return SCHINT(interval);
}

/* Set socket buffers, "alloc" is an estimate of memory taken by single packet. */

void sock_setbufs(int icmp_sock, int alloc)
{
	int rcvbuf, hold;
	socklen_t tmplen = sizeof(hold);

	if (!sndbuf)
		sndbuf = alloc;
	setsockopt(icmp_sock, SOL_SOCKET, SO_SNDBUF, (char *)&sndbuf, sizeof(sndbuf));

	rcvbuf = hold = alloc * preload;
	if (hold < 65536)
		hold = 65536;
	setsockopt(icmp_sock, SOL_SOCKET, SO_RCVBUF, (char *)&hold, sizeof(hold));
	if (getsockopt(icmp_sock, SOL_SOCKET, SO_RCVBUF, (char *)&hold, &tmplen) == 0) {
		if (hold < rcvbuf)
			fprintf(stderr, "WARNING: probably, rcvbuf is not enough to hold preload.\n");
	}
}

/* Protocol independent setup and parameter checks. */

void setup(int icmp_sock)
{
	int hold;
	struct timeval tv;
	sigset_t sset;

	if ((options & F_FLOOD) && !(options & F_INTERVAL))
		interval = 0;

	if (uid && interval < MINUSERINTERVAL) {
		fprintf(stderr, "ping: cannot flood; minimal interval, allowed for user, is %dms\n", MINUSERINTERVAL);
		exit(2);
	}

	if (interval >= INT_MAX/preload) {
		fprintf(stderr, "ping: illegal preload and/or interval\n");
		exit(2);
	}

	hold = 1;
	if (options & F_SO_DEBUG)
		setsockopt(icmp_sock, SOL_SOCKET, SO_DEBUG, (char *)&hold, sizeof(hold));
	if (options & F_SO_DONTROUTE)
		setsockopt(icmp_sock, SOL_SOCKET, SO_DONTROUTE, (char *)&hold, sizeof(hold));

#ifdef SO_TIMESTAMP
	if (!(options&F_LATENCY)) {
		int on = 1;
		if (setsockopt(icmp_sock, SOL_SOCKET, SO_TIMESTAMP, &on, sizeof(on)))
			fprintf(stderr, "Warning: no SO_TIMESTAMP support, falling back to SIOCGSTAMP\n");
	}
#endif
	if (options & F_MARK) {
		int ret;

		enable_capability_admin();
		ret = setsockopt(icmp_sock, SOL_SOCKET, SO_MARK, &mark, sizeof(mark));
		disable_capability_admin();

		if (ret == -1) {
			/* we probably dont wanna exit since old kernels
			 * dont support mark ..
			*/
			fprintf(stderr, "Warning: Failed to set mark %d\n", mark);
		}
	}

	/* Set some SNDTIMEO to prevent blocking forever
	 * on sends, when device is too slow or stalls. Just put limit
	 * of one second, or "interval", if it is less.
	 */
	tv.tv_sec = 1;
	tv.tv_usec = 0;
	if (interval < 1000) {
		tv.tv_sec = 0;
		tv.tv_usec = 1000 * SCHINT(interval);
	}
	setsockopt(icmp_sock, SOL_SOCKET, SO_SNDTIMEO, (char*)&tv, sizeof(tv));

	/* Set RCVTIMEO to "interval". Note, it is just an optimization
	 * allowing to avoid redundant poll(). */
	tv.tv_sec = SCHINT(interval)/1000;
	tv.tv_usec = 1000*(SCHINT(interval)%1000);
	if (setsockopt(icmp_sock, SOL_SOCKET, SO_RCVTIMEO, (char*)&tv, sizeof(tv)))
		options |= F_FLOOD_POLL;

	if (!(options & F_PINGFILLED)) {
		int i;
		u_char *p = outpack+8;

		/* Do not forget about case of small datalen,
		 * fill timestamp area too!
		 */
		for (i = 0; i < datalen; ++i)
			*p++ = i;
	}

	ident = htons(getpid() & 0xFFFF);

	set_signal(SIGINT, sigexit);
	set_signal(SIGALRM, sigexit);
	set_signal(SIGQUIT, sigstatus);

	sigemptyset(&sset);
	sigprocmask(SIG_SETMASK, &sset, NULL);

	gettimeofday(&start_time, NULL);

	if (deadline) {
		struct itimerval it;

		it.it_interval.tv_sec = 0;
		it.it_interval.tv_usec = 0;
		it.it_value.tv_sec = deadline;
		it.it_value.tv_usec = 0;
		setitimer(ITIMER_REAL, &it, NULL);
	}

	if (isatty(STDOUT_FILENO)) {
		struct winsize w;

		if (ioctl(STDOUT_FILENO, TIOCGWINSZ, &w) != -1) {
			if (w.ws_col > 0)
				screen_width = w.ws_col;
		}
	}
}

void main_loop(int icmp_sock, __u8 *packet, int packlen)
{
	char addrbuf[128];
	char ans_data[4096];
	struct iovec iov;
	struct msghdr msg;
	struct cmsghdr *c;
	int cc;
	int next;
	int polling;

	iov.iov_base = (char *)packet;

	for (;;) {
		/* Check exit conditions. */
		if (exiting)
			break;
		if (npackets && nreceived + nerrors >= npackets)
			break;
		if (deadline && nerrors)
			break;
		/* Check for and do special actions. */
		if (status_snapshot)
			status();

		/* Send probes scheduled to this time. */
		do {
			next = pinger();
			next = schedule_exit(next);
		} while (next <= 0);

		/* "next" is time to send next probe, if positive.
		 * If next<=0 send now or as soon as possible. */

		/* Technical part. Looks wicked. Could be dropped,
		 * if everyone used the newest kernel. :-)
		 * Its purpose is:
		 * 1. Provide intervals less than resolution of scheduler.
		 *    Solution: spinning.
		 * 2. Avoid use of poll(), when recvmsg() can provide
		 *    timed waiting (SO_RCVTIMEO). */
		polling = 0;
		if ((options & (F_ADAPTIVE|F_FLOOD_POLL)) || next<SCHINT(interval)) {
			int recv_expected = in_flight();

			/* If we are here, recvmsg() is unable to wait for
			 * required timeout. */
			if (1000 % HZ == 0 ? next <= 1000 / HZ : (next < INT_MAX / HZ && next * HZ <= 1000)) {
				/* Very short timeout... So, if we wait for
				 * something, we sleep for MININTERVAL.
				 * Otherwise, spin! */
				if (recv_expected) {
					next = MININTERVAL;
				} else {
					next = 0;
					/* When spinning, no reasons to poll.
					 * Use nonblocking recvmsg() instead. */
					polling = MSG_DONTWAIT;
					/* But yield yet. */
					sched_yield();
				}
			}

			if (!polling &&
			    ((options & (F_ADAPTIVE|F_FLOOD_POLL)) || interval)) {
				struct pollfd pset;
				pset.fd = icmp_sock;
				pset.events = POLLIN|POLLERR;
				pset.revents = 0;
				if (poll(&pset, 1, next) < 1 ||
				    !(pset.revents&(POLLIN|POLLERR)))
					continue;
				polling = MSG_DONTWAIT;
			}
		}

		for (;;) {
			struct timeval *recv_timep = NULL;
			struct timeval recv_time;
			int not_ours = 0; /* Raw socket can receive messages
					   * destined to other running pings. */

			iov.iov_len = packlen;
			memset(&msg, 0, sizeof(msg));
			msg.msg_name = addrbuf;
			msg.msg_namelen = sizeof(addrbuf);
			msg.msg_iov = &iov;
			msg.msg_iovlen = 1;
			msg.msg_control = ans_data;
			msg.msg_controllen = sizeof(ans_data);

			cc = recvmsg(icmp_sock, &msg, polling);
			polling = MSG_DONTWAIT;

			if (cc < 0) {
				if (errno == EAGAIN || errno == EINTR)
					break;
				if (!receive_error_msg()) {
					if (errno) {
						perror("ping: recvmsg");
						break;
					}
					not_ours = 1;
				}
			} else {

#ifdef SO_TIMESTAMP
				for (c = CMSG_FIRSTHDR(&msg); c; c = CMSG_NXTHDR(&msg, c)) {
					if (c->cmsg_level != SOL_SOCKET ||
					    c->cmsg_type != SO_TIMESTAMP)
						continue;
					if (c->cmsg_len < CMSG_LEN(sizeof(struct timeval)))
						continue;
					recv_timep = (struct timeval*)CMSG_DATA(c);
				}
#endif

				if ((options&F_LATENCY) || recv_timep == NULL) {
					if ((options&F_LATENCY) ||
					    ioctl(icmp_sock, SIOCGSTAMP, &recv_time))
						gettimeofday(&recv_time, NULL);
					recv_timep = &recv_time;
				}

				not_ours = parse_reply(&msg, cc, addrbuf, recv_timep);
			}

			/* See? ... someone runs another ping on this host. */
			if (not_ours)
				install_filter();

			/* If nothing is in flight, "break" returns us to pinger. */
			if (in_flight() == 0)
				break;

			/* Otherwise, try to recvmsg() again. recvmsg()
			 * is nonblocking after the first iteration, so that
			 * if nothing is queued, it will receive EAGAIN
			 * and return to pinger. */
		}
	}
	finish();
}

int gather_statistics(__u8 *icmph, int icmplen,
		      int cc, __u16 seq, int hops,
		      int csfailed, struct timeval *tv, char *from,
		      void (*pr_reply)(__u8 *icmph, int cc))
{
	int dupflag = 0;
	long triptime = 0;
	__u8 *ptr = icmph + icmplen;

	++nreceived;
	if (!csfailed)
		acknowledge(seq);

	if (timing && cc >= 8+sizeof(struct timeval)) {
		struct timeval tmp_tv;
		memcpy(&tmp_tv, ptr, sizeof(tmp_tv));

restamp:
		tvsub(tv, &tmp_tv);
		triptime = tv->tv_sec * 1000000 + tv->tv_usec;
		if (triptime < 0) {
			fprintf(stderr, "Warning: time of day goes back (%ldus), taking countermeasures.\n", triptime);
			triptime = 0;
			if (!(options & F_LATENCY)) {
				gettimeofday(tv, NULL);
				options |= F_LATENCY;
				goto restamp;
			}
		}
		if (!csfailed) {
			tsum += triptime;
			tsum2 += (long long)triptime * (long long)triptime;
			if (triptime < tmin)
				tmin = triptime;
			if (triptime > tmax)
				tmax = triptime;
			if (!rtt)
				rtt = triptime*8;
			else
				rtt += triptime-rtt/8;
			if (options&F_ADAPTIVE)
				update_interval();
		}
	}

	if (csfailed) {
		++nchecksum;
		--nreceived;
	} else if (rcvd_test(seq)) {
		++nrepeats;
		--nreceived;
		dupflag = 1;
	} else {
		rcvd_set(seq);
		dupflag = 0;
	}
	confirm = confirm_flag;

	if (options & F_QUIET)
		return 1;

	if (options & F_FLOOD) {
		if (!csfailed)
			write_stdout("\b \b", 3);
		else
			write_stdout("\bC", 2);
	} else {
		int i;
		int space=0;
		char tbuf[16];
		
		__u8 *cp, *dp;

		//print_timestamp();

		if (pr_reply)
			pr_reply(icmph, cc);

		// HOST

		// 255.255.255.255 = 15
		// 2804:1b40:1234:1234:cafe:cafe:cafe:cafe = 39
		// TOTAL: 40
		//	printf("%d bytes from %s:", cc, from);
		printf("%s%-40s%s", LWHT, from, RESET);

		// FLAGs (12 bytes)
		if (dupflag){
			printf("%sD%s", LYEL, RESET);
			space++;
		}

		if (csfailed){
			printf("%sX%s", LRED, RESET);
			space++;
		}
		while(++space <= 2) printf(" ");

		// STATUS SEM FLAG
		if (cc < datalen+8) {
			// status: trunk

			// Espacos das flags ate o status: 
			printf("%15s", " ");

			// Status
			printf("%sTruncated%s\n", LRED, RESET);
			return 1;
		}

		// SIZE
		printf("%4d ", cc);

		// TTL
		if (hops >= 0){
			printf("%3d", hops);
		}else{
			printf("   ");
		}

		// TEMPO
		//printf(" %ld.%03ld ms", triptime/1000,  triptime%1000);
		space = 0;
		bzero(tbuf, 16);

		// espaco antes do tempo
		printf(" ");

		if (timing) {

			// 100 mil
			if (triptime >= 100000)
				sprintf(tbuf, "%ld", triptime/1000);

			// 10 mil
			else if (triptime >= 10000)

				sprintf(tbuf, "%ld.%01ld", triptime/1000,  (triptime%1000)/100);

			// 1 mil
			else if (triptime >= 1000)

				sprintf(tbuf, "%ld.%03ld", triptime/1000,  (triptime%1000)/1);

			// microsegundos
			else

				sprintf(tbuf, "%ld.%03ld", triptime/1000,  triptime%1000);

			// imprimir
			space = strlen(tbuf);
			printf("%-6s", tbuf);

			// for(i=space;i<=8;i++)printf(" ");
		}else{
			// time em branco
			printf("        ");
		}

		printf(" ");

		/* check the data */
		space = 0;
		cp = ((u_char*)ptr) + sizeof(struct timeval);
		dp = &outpack[8 + sizeof(struct timeval)];
		for (i = sizeof(struct timeval); i < datalen; ++i, ++cp, ++dp) {

			if (*cp != *dp) {
				printf("%sB-%d 0x%x!=0x%x%s", LRED, i, *dp, *cp, RESET);
				space++;

				/*
				cp = (u_char*)ptr + sizeof(struct timeval);

				for (i = sizeof(struct timeval); i < datalen; ++i, ++cp) {
					if ((i % 32) == sizeof(struct timeval))
						printf("\n#%d\t", i);
					printf("%x ", *cp);
				}
				break;
				*/
			}
		}
		if(!space){
			printf("%secho reply%s", LGRN, RESET);
		}

		// atualizar informacao de estatisticas e cabecalhos
		print_stats(1);

	}
	return 0;
}

static long llsqrt(long long a)
{
	long long prev = ~((long long)1 << 63);
	long long x = a;

	if (x > 0) {
		while (x < prev) {
			prev = x;
			x = (x+(a/x))/2;
		}
	}

	return (long)x;
}

// imprimir cabecalho
static void print_header(){
	printf("%s%s SEQ HOST                                      SIZE TTL TIME  STATUS%s\n",  FONT_BOLD, LWHT, RESET);
}

// Imprimir estatisticas
void print_stats(int reprint_header){
	struct timeval tv = cur_time;
	char *comma = "";
	int lost=0;
	static showcount = 0;
	int show_header = 0;

	showcount++;
	if(reprint_header){
		// mikrotik: 19 pings
		if(showcount == 19){
			show_header = 1;
			showcount=0;
			printf("\n");

		}else{
			return;
		}
	}


	//long double minrtt = 0;
	//long double avgrtt = 0;
	//long double maxrtt = 0;

	char buf_minrtt[16]; bzero(buf_minrtt, 16);
	char buf_avgrtt[16]; bzero(buf_avgrtt, 16);
	char buf_maxrtt[16]; bzero(buf_maxrtt, 16);

	tvsub(&tv, &start_time);

	// calcular perdas
	if (ntransmitted) {
		lost = (int) ((((long long)(ntransmitted - nreceived)) * 100) / ntransmitted);
	}

	// calcular minimo, maximo, media
	if (nreceived && timing) {
		long tmdev;

		tsum /= nreceived + nrepeats;
		tsum2 /= nreceived + nrepeats;
		tmdev = llsqrt(tsum2 - tsum * tsum);

		sprintf(buf_minrtt, "%ld.%03ld",  (long)tmin/1000, (long)tmin%1000 );
		sprintf(buf_avgrtt, "%ld.%03ld",  (unsigned long)(tsum/1000), (long)(tsum%1000) );
		sprintf(buf_maxrtt, "%ld.%03ld",  (long)tmax/1000, (long)tmax%1000 );

	}
	if(!buf_minrtt[0]) buf_minrtt[0]='0';
	if(!buf_avgrtt[0]) buf_avgrtt[0]='0';
	if(!buf_maxrtt[0]) buf_maxrtt[0]='0';

	// estatisticas
	printf("     ");
	printf("%ssent=%s%ld%s received=%s%ld%s packet-loss=%s%d%s min-rtt=%s%s%s avg-rtt=%s%s%s max-rtt=%s%s%s",
			KGRN,
			LWHT, ntransmitted, KGRN,
			LWHT, nreceived, KGRN, 
			LWHT, lost, KGRN,
				LWHT, buf_minrtt, KGRN, 
				LWHT, buf_avgrtt,KGRN,
				LWHT, buf_maxrtt, RESET
	);
	if(show_header){
		printf("\n");
		printf("%s%s   SEQ  HOST                                   SIZE TTL TIME  STATUS%s",  FONT_BOLD, LWHT, RESET);
	}else{
		printf("\n");
	}
}


// LGRN
// LWHT
/*
	putchar('\n');
	fflush(stdout);
	printf("--- %s ping statistics ---\n", hostname);
	printf("%ld packets transmitted, ", ntransmitted);
	printf("%ld received", nreceived);
	if (nrepeats)
		printf(", +%ld duplicates", nrepeats);
	if (nchecksum)
		printf(", +%ld corrupted", nchecksum);
	if (nerrors)
		printf(", +%ld errors", nerrors);
	if (ntransmitted) {
		printf(", %d%% packet loss",
		       (int) ((((long long)(ntransmitted - nreceived)) * 100) /
			      ntransmitted));
		printf(", time %ldms", 1000*tv.tv_sec+tv.tv_usec/1000);
	}
	putchar('\n');


	if (nreceived && timing) {
		long tmdev;

		tsum /= nreceived + nrepeats;
		tsum2 /= nreceived + nrepeats;
		tmdev = llsqrt(tsum2 - tsum * tsum);

		printf("rtt min/avg/max/mdev = %ld.%03ld/%lu.%03ld/%ld.%03ld/%ld.%03ld ms",
		       (long)tmin/1000, (long)tmin%1000,
		       (unsigned long)(tsum/1000), (long)(tsum%1000),
		       (long)tmax/1000, (long)tmax%1000,
		       (long)tmdev/1000, (long)tmdev%1000
		       );
		comma = ", ";
	}
	if (pipesize > 1) {
		printf("%spipe %d", comma, pipesize);
		comma = ", ";
	}
	if (nreceived && (!interval || (options&(F_FLOOD|F_ADAPTIVE))) && ntransmitted > 1) {
		int ipg = (1000000*(long long)tv.tv_sec+tv.tv_usec)/(ntransmitted-1);
		printf("%sipg/ewma %d.%03d/%d.%03d ms",
		       comma, ipg/1000, ipg%1000, rtt/8000, (rtt/8)%1000);
	}
	*/
/*
 * finish --
 *	Print out statistics, and give up.
 */
void finish(void){
	print_stats(0);
	printf("\n");
	exit(!nreceived || (deadline && nreceived < npackets));
}


void status(void){
	int loss = 0;
	long tavg = 0;

	status_snapshot = 0;

	if (ntransmitted)
		loss = (((long long)(ntransmitted - nreceived)) * 100) / ntransmitted;

	fprintf(stderr, "\r%ld/%ld packets, %d%% loss", ntransmitted, nreceived, loss);

	if (nreceived && timing) {
		tavg = tsum / (nreceived + nrepeats);

		fprintf(stderr, ", min/avg/ewma/max = %ld.%03ld/%lu.%03ld/%d.%03d/%ld.%03ld ms",
		       (long)tmin/1000, (long)tmin%1000,
		       tavg/1000, tavg%1000,
		       rtt/8000, (rtt/8)%1000,
		       (long)tmax/1000, (long)tmax%1000
		       );
	}
	fprintf(stderr, "\n");
}



File: /ping_common.h
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <sys/param.h>
#include <sys/socket.h>
#include <linux/sockios.h>
#include <sys/file.h>
#include <sys/time.h>
#include <sys/signal.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <sys/uio.h>
#include <sys/poll.h>
#include <ctype.h>
#include <errno.h>
#include <string.h>
#include <netdb.h>
#include <setjmp.h>

#ifdef CAPABILITIES
#include <sys/prctl.h>
#include <sys/capability.h>
#endif

#ifdef USE_IDN
#include <locale.h>
#include <idna.h>
#endif

#include <netinet/in.h>
#include <arpa/inet.h>
#include <linux/types.h>
#include <linux/errqueue.h>

#include "colors.h"

#include "SNAPSHOT.h"

#define	DEFDATALEN	(64 - 8)	/* default data length */

#define	MAXWAIT		10		/* max seconds to wait for response */
#define MININTERVAL	10		/* Minimal interpacket gap */
#define MINUSERINTERVAL	200		/* Minimal allowed interval for non-root */

#define SCHINT(a)	(((a) <= MININTERVAL) ? MININTERVAL : (a))

/* various options */
extern int options;
#define	F_FLOOD		0x001
#define	F_INTERVAL	0x002
#define	F_NUMERIC	0x004
#define	F_PINGFILLED	0x008
#define	F_QUIET		0x010
#define	F_RROUTE	0x020
#define	F_SO_DEBUG	0x040
#define	F_SO_DONTROUTE	0x080
#define	F_VERBOSE	0x100
#define	F_TIMESTAMP	0x200
#define	F_FLOWINFO	0x200
#define	F_SOURCEROUTE	0x400
#define	F_TCLASS	0x400
#define	F_FLOOD_POLL	0x800
#define	F_LATENCY	0x1000
#define	F_AUDIBLE	0x2000
#define	F_ADAPTIVE	0x4000
#define	F_STRICTSOURCE	0x8000
#define F_NOLOOP	0x10000
#define F_TTL		0x20000
#define F_MARK		0x40000
#define F_PTIMEOFDAY	0x80000
#define F_OUTSTANDING	0x100000

/*
 * MAX_DUP_CHK is the number of bits in received table, i.e. the maximum
 * number of received sequence numbers we can keep track of.
 */
#define	MAX_DUP_CHK	0x10000

#if defined(__WORDSIZE) && __WORDSIZE == 64
# define USE_BITMAP64
#endif

#ifdef USE_BITMAP64
typedef __u64	bitmap_t;
# define BITMAP_SHIFT	6
#else
typedef __u32	bitmap_t;
# define BITMAP_SHIFT	5
#endif

#if ((MAX_DUP_CHK >> (BITMAP_SHIFT + 3)) << (BITMAP_SHIFT + 3)) != MAX_DUP_CHK
# error Please MAX_DUP_CHK and/or BITMAP_SHIFT
#endif

struct rcvd_table {
	bitmap_t bitmap[MAX_DUP_CHK / (sizeof(bitmap_t) * 8)];
};

extern struct rcvd_table rcvd_tbl;

#define	A(bit)	(rcvd_tbl.bitmap[(bit) >> BITMAP_SHIFT])	/* identify word in array */
#define	B(bit)	(((bitmap_t)1) << ((bit) & ((1 << BITMAP_SHIFT) - 1)))	/* identify bit in word */

static inline void rcvd_set(__u16 seq)
{
	unsigned bit = seq % MAX_DUP_CHK;
	A(bit) |= B(bit);
}

static inline void rcvd_clear(__u16 seq)
{
	unsigned bit = seq % MAX_DUP_CHK;
	A(bit) &= ~B(bit);
}

static inline bitmap_t rcvd_test(__u16 seq)
{
	unsigned bit = seq % MAX_DUP_CHK;
	return A(bit) & B(bit);
}

extern u_char outpack[];
extern int maxpacket;

extern int datalen;
extern char *hostname;
extern int uid;
extern int ident;			/* process id to identify our packets */

extern int sndbuf;
extern int ttl;

extern long npackets;			/* max packets to transmit */
extern long nreceived;			/* # of packets we got back */
extern long nrepeats;			/* number of duplicates */
extern long ntransmitted;		/* sequence # for outbound packets = #sent */
extern long nchecksum;			/* replies with bad checksum */
extern long nerrors;			/* icmp errors */
extern int interval;			/* interval between packets (msec) */
extern int preload;
extern int deadline;			/* time to die */
extern int lingertime;
extern struct timeval start_time, cur_time;
extern volatile int exiting;
extern volatile int status_snapshot;
extern int confirm;
extern int confirm_flag;
extern int working_recverr;

extern volatile int in_pr_addr;		/* pr_addr() is executing */
extern jmp_buf pr_addr_jmp;

#ifndef MSG_CONFIRM
#define MSG_CONFIRM 0
#endif


/* timing */
extern int timing;			/* flag to do timing */
extern long tmin;			/* minimum round trip time */
extern long tmax;			/* maximum round trip time */
extern long long tsum;			/* sum of all times, for doing average */
extern long long tsum2;
extern int rtt;
extern __u16 acked;
extern int pipesize;

#define COMMON_OPTIONS \
case 'a': case 'U': case 'c': case 'd': \
case 'f': case 'i': case 'w': case 'l': \
case 'S': case 'n': case 'p': case 'q': \
case 'r': case 's': case 'v': case 'L': \
case 't': case 'A': case 'W': case 'B': case 'm': \
case 'D': case 'O':

#define COMMON_OPTSTR "h?VQ:I:M:aUc:dfi:w:l:S:np:qrs:vLt:AW:Bm:DO"

/*
 * Write to stdout
 */
static inline void write_stdout(const char *str, size_t len)
{
	size_t o = 0;
	ssize_t cc;
	do {
		cc = write(STDOUT_FILENO, str + o, len - o);
		o += cc;
	} while (len > o || cc < 0);
}

/*
 * tvsub --
 *	Subtract 2 timeval structs:  out = out - in.  Out is assumed to
 * be >= in.
 */
static inline void tvsub(struct timeval *out, struct timeval *in)
{
	if ((out->tv_usec -= in->tv_usec) < 0) {
		--out->tv_sec;
		out->tv_usec += 1000000;
	}
	out->tv_sec -= in->tv_sec;
}

static inline void set_signal(int signo, void (*handler)(int))
{
	struct sigaction sa;

	memset(&sa, 0, sizeof(sa));

	sa.sa_handler = (void (*)(int))handler;
#ifdef SA_INTERRUPT
	sa.sa_flags = SA_INTERRUPT;
#endif
	sigaction(signo, &sa, NULL);
}

extern int __schedule_exit(int next);

static inline int schedule_exit(int next)
{
	if (npackets && ntransmitted >= npackets && !deadline)
		next = __schedule_exit(next);
	return next;
}

static inline int in_flight(void)
{
	__u16 diff = (__u16)ntransmitted - acked;
	return (diff<=0x7FFF) ? diff : ntransmitted-nreceived-nerrors;
}

static inline void acknowledge(__u16 seq)
{
	__u16 diff = (__u16)ntransmitted - seq;
	if (diff <= 0x7FFF) {
		if ((int)diff+1 > pipesize)
			pipesize = (int)diff+1;
		if ((__s16)(seq - acked) > 0 ||
		    (__u16)ntransmitted - acked > 0x7FFF)
			acked = seq;
	}
}

static inline void advance_ntransmitted(void)
{
	ntransmitted++;
	/* Invalidate acked, if 16 bit seq overflows. */
	if ((__u16)ntransmitted - acked > 0x7FFF)
		acked = (__u16)ntransmitted + 1;
}

extern void limit_capabilities(void);
static int enable_capability_raw(void);
static int disable_capability_raw(void);
static int enable_capability_admin(void);
static int disable_capability_admin(void);
#ifdef CAPABILITIES
extern int modify_capability(cap_value_t, cap_flag_value_t);
static inline int enable_capability_raw(void)		{ return modify_capability(CAP_NET_RAW,   CAP_SET);   };
static inline int disable_capability_raw(void)		{ return modify_capability(CAP_NET_RAW,   CAP_CLEAR); };
static inline int enable_capability_admin(void)		{ return modify_capability(CAP_NET_ADMIN, CAP_SET);   };
static inline int disable_capability_admin(void)	{ return modify_capability(CAP_NET_ADMIN, CAP_CLEAR); };
#else
extern int modify_capability(int);
static inline int enable_capability_raw(void)		{ return modify_capability(1); };
static inline int disable_capability_raw(void)		{ return modify_capability(0); };
static inline int enable_capability_admin(void)		{ return modify_capability(1); };
static inline int disable_capability_admin(void)	{ return modify_capability(0); };
#endif
extern void drop_capabilities(void);

extern int send_probe(void);
extern int receive_error_msg(void);
extern int parse_reply(struct msghdr *msg, int len, void *addr, struct timeval *);
extern void install_filter(void);

extern int pinger(void);
extern void sock_setbufs(int icmp_sock, int alloc);
extern void setup(int icmp_sock);
extern void main_loop(int icmp_sock, __u8 *buf, int buflen) __attribute__((noreturn));
extern void finish(void) __attribute__((noreturn));
extern void status(void);
extern void common_options(int ch);
extern int gather_statistics(__u8 *ptr, int icmplen,
			     int cc, __u16 seq, int hops,
			     int csfailed, struct timeval *tv, char *from,
			     void (*pr_reply)(__u8 *ptr, int cc));
extern void print_timestamp(void);


File: /rarpd.c
/*
 * rarpd.c	RARP daemon.
 *
 *		This program is free software; you can redistribute it and/or
 *		modify it under the terms of the GNU General Public License
 *		as published by the Free Software Foundation; either version
 *		2 of the License, or (at your option) any later version.
 *
 * Authors:	Alexey Kuznetsov, <kuznet@ms2.inr.ac.ru>
 */

#include <stdio.h>
#include <syslog.h>
#include <dirent.h>
#include <malloc.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/ioctl.h>
#include <sys/poll.h>
#include <sys/errno.h>
#include <sys/fcntl.h>
#include <sys/socket.h>
#include <sys/signal.h>
#include <linux/if.h>
#include <linux/if_arp.h>
#include <netinet/in.h>
#include <linux/if_packet.h>
#include <linux/filter.h>

int do_reload = 1;

int debug;
int verbose;
int ifidx;
int allow_offlink;
int only_ethers;
int all_ifaces;
int listen_arp;
char *ifname;
char *tftp_dir = "/etc/tftpboot";

extern int ether_ntohost(char *name, unsigned char *ea);
void usage(void) __attribute__((noreturn));

struct iflink
{
	struct iflink	*next;
	int	       	index;
	int		hatype;
	unsigned char	lladdr[16];
	char		name[IFNAMSIZ];
	struct ifaddr 	*ifa_list;
} *ifl_list;

struct ifaddr
{
	struct ifaddr 	*next;
	__u32		prefix;
	__u32		mask;
	__u32		local;
};

struct rarp_map
{
	struct rarp_map *next;

	int		ifindex;
	int		arp_type;
	int		lladdr_len;
	unsigned char	lladdr[16];
	__u32		ipaddr;
} *rarp_db;

void usage()
{
	fprintf(stderr, "Usage: rarpd [ -dveaA ] [ -b tftpdir ] [ interface]\n");
	exit(1);
}

void load_db(void)
{
}

void load_if(void)
{
	int fd;
	struct ifreq *ifrp, *ifend;
	struct iflink *ifl;
	struct ifaddr *ifa;
	struct ifconf ifc;
	struct ifreq ibuf[256];

	if ((fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
		syslog(LOG_ERR, "socket: %m");
		return;
	}

	ifc.ifc_len = sizeof ibuf;
	ifc.ifc_buf = (caddr_t)ibuf;
	if (ioctl(fd, SIOCGIFCONF, (char *)&ifc) < 0 ||
	    ifc.ifc_len < (int)sizeof(struct ifreq)) {
		syslog(LOG_ERR, "SIOCGIFCONF: %m");
		close(fd);
		return;
	}

	while ((ifl = ifl_list) != NULL) {
		while ((ifa = ifl->ifa_list) != NULL) {
			ifl->ifa_list = ifa->next;
			free(ifa);
		}
		ifl_list = ifl->next;
		free(ifl);
	}

	ifend = (struct ifreq *)((char *)ibuf + ifc.ifc_len);
	for (ifrp = ibuf; ifrp < ifend; ifrp++) {
		__u32 addr;
		__u32 mask;
		__u32 prefix;

		if (ifrp->ifr_addr.sa_family != AF_INET)
			continue;
		addr = ((struct sockaddr_in*)&ifrp->ifr_addr)->sin_addr.s_addr;
		if (addr == 0)
			continue;
		if (ioctl(fd, SIOCGIFINDEX, ifrp)) {
			syslog(LOG_ERR, "ioctl(SIOCGIFNAME): %m");
			continue;
		}
		if (ifidx && ifrp->ifr_ifindex != ifidx)
			continue;
		for (ifl = ifl_list; ifl; ifl = ifl->next)
			if (ifl->index == ifrp->ifr_ifindex)
				break;
		if (ifl == NULL) {
			char *p;
			int index = ifrp->ifr_ifindex;

			if (ioctl(fd, SIOCGIFHWADDR, ifrp)) {
				syslog(LOG_ERR, "ioctl(SIOCGIFHWADDR): %m");
				continue;
			}

			ifl = (struct iflink*)malloc(sizeof(*ifl));
			if (ifl == NULL)
				continue;
			memset(ifl, 0, sizeof(*ifl));
			ifl->next = ifl_list;
			ifl_list = ifl;
			ifl->index = index;
			ifl->hatype = ifrp->ifr_hwaddr.sa_family;
			memcpy(ifl->lladdr, ifrp->ifr_hwaddr.sa_data, 14);
			strncpy(ifl->name, ifrp->ifr_name, IFNAMSIZ);
			p = strchr(ifl->name, ':');
			if (p)
				*p = 0;
			if (verbose)
				syslog(LOG_INFO, "link %s", ifl->name);
		}
		if (ioctl(fd, SIOCGIFNETMASK, ifrp)) {
			syslog(LOG_ERR, "ioctl(SIOCGIFMASK): %m");
			continue;
		}
		mask = ((struct sockaddr_in*)&ifrp->ifr_netmask)->sin_addr.s_addr;
		if (ioctl(fd, SIOCGIFDSTADDR, ifrp)) {
			syslog(LOG_ERR, "ioctl(SIOCGIFDSTADDR): %m");
			continue;
		}
		prefix = ((struct sockaddr_in*)&ifrp->ifr_dstaddr)->sin_addr.s_addr;
		for (ifa = ifl->ifa_list; ifa; ifa = ifa->next) {
			if (ifa->local == addr &&
			    ifa->prefix == prefix &&
			    ifa->mask == mask)
				break;
		}
		if (ifa == NULL) {
			if (mask == 0 || prefix == 0)
				continue;
			ifa = (struct ifaddr*)malloc(sizeof(*ifa));
			memset(ifa, 0, sizeof(*ifa));
			ifa->local = addr;
			ifa->prefix = prefix;
			ifa->mask = mask;
			ifa->next = ifl->ifa_list;
			ifl->ifa_list = ifa;

			if (verbose) {
				int i;
				__u32 m = ~0U;
				for (i=32; i>=0; i--) {
					if (htonl(m) == mask)
						break;
					m <<= 1;
				}
				if (addr == prefix) {
					syslog(LOG_INFO, "  addr %s/%d on %s\n",
					       inet_ntoa(*(struct in_addr*)&addr), i, ifl->name);
				} else {
					char tmpa[64];
					sprintf(tmpa, "%s", inet_ntoa(*(struct in_addr*)&addr));
					syslog(LOG_INFO, "  addr %s %s/%d on %s\n", tmpa,
					       inet_ntoa(*(struct in_addr*)&prefix), i, ifl->name);
				}
			}
		}
	}
}

void configure(void)
{
	load_if();
	load_db();
}

int bootable(__u32 addr)
{
	struct dirent *dent;
	DIR *d;
	char name[9];

	sprintf(name, "%08X", (__u32)ntohl(addr));
	d = opendir(tftp_dir);
	if (d == NULL) {
		syslog(LOG_ERR, "opendir: %m");
		return 0;
	}
	while ((dent = readdir(d)) != NULL) {
		if (strncmp(dent->d_name, name, 8) == 0)
			break;
	}
	closedir(d);
	return dent != NULL;
}

struct ifaddr *select_ipaddr(int ifindex, __u32 *sel_addr, __u32 **alist)
{
	struct iflink *ifl;
	struct ifaddr *ifa;
	int retry = 0;
	int i;

retry:
	for (ifl=ifl_list; ifl; ifl=ifl->next)
		if (ifl->index == ifindex)
			break;
	if (ifl == NULL && !retry) {
		retry++;
		load_if();
		goto retry;
	}
	if (ifl == NULL)
		return NULL;

	for (i=0; alist[i]; i++) {
		__u32 addr = *(alist[i]);
		for (ifa=ifl->ifa_list; ifa; ifa=ifa->next) {
			if (!((ifa->prefix^addr)&ifa->mask)) {
				*sel_addr = addr;
				return ifa;
			}
		}
		if (ifa == NULL && retry==0) {
			retry++;
			load_if();
			goto retry;
		}
	}
	if (i==1 && allow_offlink) {
		*sel_addr = *(alist[0]);
		return ifl->ifa_list;
	}
	syslog(LOG_ERR, "Off-link request on %s", ifl->name);
	return NULL;
}

struct rarp_map *rarp_lookup(int ifindex, int hatype,
			     int halen, unsigned char *lladdr)
{
	struct rarp_map *r;

	for (r=rarp_db; r; r=r->next) {
		if (r->arp_type != hatype && r->arp_type != -1)
			continue;
		if (r->lladdr_len != halen)
			continue;
		if (r->ifindex != ifindex && r->ifindex != 0)
			continue;
		if (memcmp(r->lladdr, lladdr, halen) == 0)
			break;
	}

	if (r == NULL) {
		if (hatype == ARPHRD_ETHER && halen == 6) {
			struct ifaddr *ifa;
			struct hostent *hp;
			char ename[256];
			static struct rarp_map emap = {
				NULL,
				0,
				ARPHRD_ETHER,
				6,
			};

			if (ether_ntohost(ename, lladdr) != 0 ||
			    (hp = gethostbyname(ename)) == NULL) {
				if (verbose)
					syslog(LOG_INFO, "not found in /etc/ethers");
				return NULL;
			}
			if (hp->h_addrtype != AF_INET) {
				syslog(LOG_ERR, "no IP address");
				return NULL;
			}
			ifa = select_ipaddr(ifindex, &emap.ipaddr, (__u32 **)hp->h_addr_list);
			if (ifa) {
				memcpy(emap.lladdr, lladdr, 6);
				if (only_ethers || bootable(emap.ipaddr))
					return &emap;
				if (verbose)
					syslog(LOG_INFO, "not bootable");
			}
		}
	}
	return r;
}

static int load_arp_bpflet(int fd)
{
	static struct sock_filter insns[] = {
		BPF_STMT(BPF_LD|BPF_H|BPF_ABS, 6),
		BPF_JUMP(BPF_JMP|BPF_JEQ|BPF_K, ARPOP_RREQUEST, 0, 1),
		BPF_STMT(BPF_RET|BPF_K, 1024),
		BPF_STMT(BPF_RET|BPF_K, 0),
	};
	static struct sock_fprog filter = {
		sizeof insns / sizeof(insns[0]),
		insns
	};

	return setsockopt(fd, SOL_SOCKET, SO_ATTACH_FILTER, &filter, sizeof(filter));
}

int put_mylladdr(unsigned char **ptr_p, int ifindex, int alen)
{
	struct iflink *ifl;

	for (ifl=ifl_list; ifl; ifl = ifl->next)
		if (ifl->index == ifindex)
			break;

	if (ifl==NULL)
		return -1;

	memcpy(*ptr_p, ifl->lladdr, alen);
	*ptr_p += alen;
	return 0;
}

int put_myipaddr(unsigned char **ptr_p, int ifindex, __u32 hisipaddr)
{
	__u32 laddr = 0;
	struct iflink *ifl;
	struct ifaddr *ifa;

	for (ifl=ifl_list; ifl; ifl = ifl->next)
		if (ifl->index == ifindex)
			break;

	if (ifl==NULL)
		return -1;

	for (ifa=ifl->ifa_list; ifa; ifa=ifa->next) {
		if (!((ifa->prefix^hisipaddr)&ifa->mask)) {
			laddr = ifa->local;
			break;
		}
	}
	memcpy(*ptr_p, &laddr, 4);
	*ptr_p += 4;
	return 0;
}

void arp_advise(int ifindex, unsigned char *lladdr, int lllen, __u32 ipaddr)
{
	int fd;
	struct arpreq req;
	struct sockaddr_in *sin;
	struct iflink *ifl;

	for (ifl=ifl_list; ifl; ifl = ifl->next)
		if (ifl->index == ifindex)
			break;

	if (ifl == NULL)
		return;

	fd = socket(AF_INET, SOCK_DGRAM, 0);
	memset(&req, 0, sizeof(req));
	req.arp_flags = ATF_COM;
	sin = (struct sockaddr_in *)&req.arp_pa;
	sin->sin_family = AF_INET;
	sin->sin_addr.s_addr = ipaddr;
	req.arp_ha.sa_family = ifl->hatype;
	memcpy(req.arp_ha.sa_data, lladdr, lllen);
	memcpy(req.arp_dev, ifl->name, IFNAMSIZ);

	if (ioctl(fd, SIOCSARP, &req))
		syslog(LOG_ERR, "SIOCSARP: %m");
	close(fd);
}

void serve_it(int fd)
{
	unsigned char buf[1024];
	struct sockaddr_ll sll;
	socklen_t sll_len = sizeof(sll);
	struct arphdr *a = (struct arphdr*)buf;
	struct rarp_map *rmap;
	unsigned char *ptr;
	int n;

	n = recvfrom(fd, buf, sizeof(buf), MSG_DONTWAIT, (struct sockaddr*)&sll, &sll_len);
	if (n<0) {
		if (errno != EINTR && errno != EAGAIN)
			syslog(LOG_ERR, "recvfrom: %m");
		return;
	}

	/* Do not accept packets for other hosts and our own ones */
	if (sll.sll_pkttype != PACKET_BROADCAST &&
	    sll.sll_pkttype != PACKET_MULTICAST &&
	    sll.sll_pkttype != PACKET_HOST)
		return;

	if (ifidx && sll.sll_ifindex != ifidx)
		return;

	if (n<sizeof(*a)) {
		syslog(LOG_ERR, "truncated arp packet; len=%d", n);
		return;
	}

	/* Accept only RARP requests */
	if (a->ar_op != htons(ARPOP_RREQUEST))
		return;

	if (verbose) {
		int i;
		char tmpbuf[16*3];
		char *ptr = tmpbuf;
		for (i=0; i<sll.sll_halen; i++) {
			if (i) {
				sprintf(ptr, ":%02x", sll.sll_addr[i]);
				ptr++;
			} else
				sprintf(ptr, "%02x", sll.sll_addr[i]);
			ptr += 2;
		}
		syslog(LOG_INFO, "RARP request from %s on if%d", tmpbuf, sll.sll_ifindex);
	}

	/* Sanity checks */

	/* 1. IP only -> pln==4 */
	if (a->ar_pln != 4) {
		syslog(LOG_ERR, "interesting rarp_req plen=%d", a->ar_pln);
		return;
	}
	/* 2. ARP protocol must be IP */
	if (a->ar_pro != htons(ETH_P_IP)) {
		syslog(LOG_ERR, "rarp protocol is not IP %04x", ntohs(a->ar_pro));
		return;
	}
	/* 3. ARP types must match */
	if (htons(sll.sll_hatype) != a->ar_hrd) {
		switch (sll.sll_hatype) {
		case ARPHRD_FDDI:
			if (a->ar_hrd == htons(ARPHRD_ETHER) ||
			    a->ar_hrd == htons(ARPHRD_IEEE802))
				break;
		default:
			syslog(LOG_ERR, "rarp htype mismatch");
			return;
		}
	}
	/* 3. LL address lengths must be equal */
	if (a->ar_hln != sll.sll_halen) {
		syslog(LOG_ERR, "rarp hlen mismatch");
		return;
	}
	/* 4. Check packet length */
	if (sizeof(*a) + 2*4 + 2*a->ar_hln > n) {
		syslog(LOG_ERR, "truncated rarp request; len=%d", n);
		return;
	}
	/* 5. Silly check: if this guy set different source
	      addresses in MAC header and in ARP, he is insane
	 */
	if (memcmp(sll.sll_addr, a+1, sll.sll_halen)) {
		syslog(LOG_ERR, "this guy set different his lladdrs in arp and header");
		return;
	}
	/* End of sanity checks */

	/* Lookup requested target in our database */
	rmap = rarp_lookup(sll.sll_ifindex, sll.sll_hatype,
			   sll.sll_halen, (unsigned char*)(a+1) + sll.sll_halen + 4);
	if (rmap == NULL)
		return;

	/* Prepare reply. It is almost ready, we only
	   replace ARP packet type, put our lladdr and
	   IP address to source fileds,
	   and fill target IP address.
	 */
	a->ar_op = htons(ARPOP_RREPLY);
	ptr = (unsigned char*)(a+1);
	if (put_mylladdr(&ptr, sll.sll_ifindex, rmap->lladdr_len))
		return;
	if (put_myipaddr(&ptr, sll.sll_ifindex, rmap->ipaddr))
		return;
	/* It is already filled */
	ptr += rmap->lladdr_len;
	memcpy(ptr, &rmap->ipaddr, 4);
	ptr += 4;

	/* Update our ARP cache. Probably, this guy
	   will not able to make ARP (if it is broken)
	 */
	arp_advise(sll.sll_ifindex, rmap->lladdr, rmap->lladdr_len, rmap->ipaddr);

	/* Sendto is blocking, but with 5sec timeout */
	alarm(5);
	sendto(fd, buf, ptr - buf, 0, (struct sockaddr*)&sll, sizeof(sll));
	alarm(0);
}

void catch_signal(int sig, void (*handler)(int))
{
	struct sigaction sa;

	memset(&sa, 0, sizeof(sa));
	sa.sa_handler = handler;
#ifdef SA_INTERRUPT
	sa.sa_flags = SA_INTERRUPT;
#endif
	sigaction(sig, &sa, NULL);
}

void sig_alarm(int signo)
{
}

void sig_hup(int signo)
{
	do_reload = 1;
}

int main(int argc, char **argv)
{
	struct pollfd pset[2];
	int psize;
	int opt;


	opterr = 0;
	while ((opt = getopt(argc, argv, "aAb:dvoe")) != EOF) {
		switch (opt) {
		case 'a':
			++all_ifaces;
			break;

		case 'A':
			++listen_arp;
			break;

		case 'd':
			++debug;
			break;

		case 'v':
			++verbose;
			break;

		case 'o':
			++allow_offlink;
			break;

		case 'e':
			++only_ethers;
			break;

		case 'b':
			tftp_dir = optarg;
			break;

		default:
			usage();
		}
	}
	if (argc > optind) {
		if (argc > optind+1)
			usage();
		ifname = argv[optind];
	}

	psize = 1;
	pset[0].fd = socket(PF_PACKET, SOCK_DGRAM, 0);

	if (ifname) {
		struct ifreq ifr;
		memset(&ifr, 0, sizeof(ifr));
		strncpy(ifr.ifr_name, ifname, IFNAMSIZ);
		if (ioctl(pset[0].fd, SIOCGIFINDEX, &ifr)) {
			perror("ioctl(SIOCGIFINDEX)");
			usage();
		}
		ifidx = ifr.ifr_ifindex;
	}

	pset[1].fd = -1;
	if (listen_arp) {
		pset[1].fd = socket(PF_PACKET, SOCK_DGRAM, 0);
		if (pset[1].fd >= 0) {
			load_arp_bpflet(pset[1].fd);
			psize = 1;
		}
	}

	if (pset[1].fd >= 0) {
		struct sockaddr_ll sll;
		memset(&sll, 0, sizeof(sll));
		sll.sll_family = AF_PACKET;
		sll.sll_protocol = htons(ETH_P_ARP);
		sll.sll_ifindex = all_ifaces ? 0 : ifidx;
		if (bind(pset[1].fd, (struct sockaddr*)&sll, sizeof(sll)) < 0) {
			close(pset[1].fd);
			pset[1].fd = -1;
			psize = 1;
		}
	}
	if (pset[0].fd >= 0) {
		struct sockaddr_ll sll;
		memset(&sll, 0, sizeof(sll));
		sll.sll_family = AF_PACKET;
		sll.sll_protocol = htons(ETH_P_RARP);
		sll.sll_ifindex = all_ifaces ? 0 : ifidx;
		if (bind(pset[0].fd, (struct sockaddr*)&sll, sizeof(sll)) < 0) {
			close(pset[0].fd);
			pset[0].fd = -1;
		}
	}
	if (pset[0].fd < 0) {
		pset[0] = pset[1];
		psize--;
	}
	if (psize == 0) {
		fprintf(stderr, "failed to bind any socket. Aborting.\n");
		exit(1);
	}

	if (!debug) {
		int fd;
		pid_t pid = fork();

		if (pid > 0)
			exit(0);
		else if (pid == -1) {
			perror("rarpd: fork");
			exit(1);
		}

		if (chdir("/") < 0) {
			perror("rarpd: chdir");
			exit(1);
		}

		fd = open("/dev/null", O_RDWR);
		if (fd >= 0) {
			dup2(fd, 0);
			dup2(fd, 1);
			dup2(fd, 2);
			if (fd > 2)
				close(fd);
		}
		setsid();
	}

	openlog("rarpd", LOG_PID | LOG_CONS, LOG_DAEMON);
	catch_signal(SIGALRM, sig_alarm);
	catch_signal(SIGHUP, sig_hup);

	for (;;) {
		int i;

		if (do_reload) {
			configure();
			do_reload = 0;
		}

#define EVENTS (POLLIN|POLLPRI|POLLERR|POLLHUP)
		pset[0].events = EVENTS;
		pset[0].revents = 0;
		pset[1].events = EVENTS;
		pset[1].revents = 0;

		i = poll(pset, psize, -1);
		if (i <= 0) {
			if (errno != EINTR && i<0) {
				syslog(LOG_ERR, "poll returned some crap: %m\n");
				sleep(10);
			}
			continue;
		}
		for (i=0; i<psize; i++) {
			if (pset[i].revents&EVENTS)
				serve_it(pset[i].fd);
		}
	}
}


File: /rdisc.c
/*
 * Rdisc (this program) was developed by Sun Microsystems, Inc. and is
 * provided for unrestricted use provided that this legend is included on
 * all tape media and as a part of the software program in whole or part.
 * Users may copy or modify Rdisc without charge, and they may freely
 * distribute it.
 *
 * RDISC IS PROVIDED AS IS WITH NO WARRANTIES OF ANY KIND INCLUDING THE
 * WARRANTIES OF DESIGN, MERCHANTIBILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE, OR ARISING FROM A COURSE OF DEALING, USAGE OR TRADE PRACTICE.
 *
 * Rdisc is provided with no support and without any obligation on the
 * part of Sun Microsystems, Inc. to assist in its use, correction,
 * modification or enhancement.
 *
 * SUN MICROSYSTEMS, INC. SHALL HAVE NO LIABILITY WITH RESPECT TO THE
 * INFRINGEMENT OF COPYRIGHTS, TRADE SECRETS OR ANY PATENTS BY RDISC
 * OR ANY PART THEREOF.
 *
 * In no event will Sun Microsystems, Inc. be liable for any lost revenue
 * or profits or other special, indirect and consequential damages, even if
 * Sun has been advised of the possibility of such damages.
 *
 * Sun Microsystems, Inc.
 * 2550 Garcia Avenue
 * Mountain View, California  94043
 */
#include <stdio.h>
#include <errno.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/time.h>
/* Do not use "improved" glibc version! */
#include <linux/limits.h>

#include <sys/param.h>
#include <sys/socket.h>
#include <sys/file.h>
#include <malloc.h>

#include <sys/ioctl.h>
#include <linux/if.h>
#include <linux/route.h>

#include <netinet/in.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>

/*
 * The next include contains all defs and structures for multicast
 * that are not in SunOS 4.1.x. On a SunOS 4.1.x system none of this code
 * is ever used because it does not support multicast
 * Fraser Gardiner - Sun Microsystems Australia
 */

#include <netdb.h>
#include <arpa/inet.h>

#include <string.h>
#include <syslog.h>

#include "SNAPSHOT.h"

struct interface
{
	struct in_addr 	address;	/* Used to identify the interface */
	struct in_addr	localaddr;	/* Actual address if the interface */
	int 		preference;
	int		flags;
	struct in_addr	bcastaddr;
	struct in_addr	remoteaddr;
	struct in_addr	netmask;
	int		ifindex;
	char		name[IFNAMSIZ];
};

/*
 * TBD
 *	Use 255.255.255.255 for broadcasts - not the interface broadcast
 *	address.
 */

#define ALLIGN(ptr)	(ptr)

static int join(int sock, struct sockaddr_in *sin);
static void solicitor(struct sockaddr_in *);
#ifdef RDISC_SERVER
static void advertise(struct sockaddr_in *, int lft);
#endif
static char *pr_name(struct in_addr addr);
static void pr_pack(char *buf, int cc, struct sockaddr_in *from);
static void age_table(int time);
static void record_router(struct in_addr router, int preference, int ttl);
static void add_route(struct in_addr addr);
static void del_route(struct in_addr addr);
static void rtioctl(struct in_addr addr, int op);
static int support_multicast(void);
static int sendbcast(int s, char *packet, int packetlen);
static int sendmcast(int s, char *packet, int packetlen, struct sockaddr_in *);
static int sendbcastif(int s, char *packet, int packetlen, struct interface *ifp);
static int sendmcastif(int s, char *packet, int packetlen, struct sockaddr_in *sin, struct interface *ifp);
static int is_directly_connected(struct in_addr in);
static void initlog(void);
static void discard_table(void);
static void init(void);

#define ICMP_ROUTER_ADVERTISEMENT	9
#define ICMP_ROUTER_SOLICITATION	10

#define ALL_HOSTS_ADDRESS		"224.0.0.1"
#define ALL_ROUTERS_ADDRESS		"224.0.0.2"

#define MAXIFS 32

#if !defined(__GLIBC__) || __GLIBC__ < 2
/* For router advertisement */
struct icmp_ra
{
	u_char	icmp_type;		/* type of message, see below */
	u_char	icmp_code;		/* type sub code */
	u_short	icmp_cksum;		/* ones complement cksum of struct */
	u_char	icmp_num_addrs;
	u_char	icmp_wpa;		/* Words per address */
	short 	icmp_lifetime;
};

struct icmp_ra_addr
{
	__u32	ira_addr;
	__u32	ira_preference;
};
#else
#define icmp_ra icmp
#endif

/* Router constants */
#define	MAX_INITIAL_ADVERT_INTERVAL	16
#define	MAX_INITIAL_ADVERTISEMENTS  	3
#define	MAX_RESPONSE_DELAY		2	/* Not used */

/* Host constants */
#define MAX_SOLICITATIONS 		3
#define SOLICITATION_INTERVAL 		3
#define MAX_SOLICITATION_DELAY		1	/* Not used */

#define INELIGIBLE_PREF			0x80000000	/* Maximum negative */

#define MAX_ADV_INT 600

/* Statics */
static int num_interfaces;

static struct interface *interfaces;
static int interfaces_size;			/* Number of elements in interfaces */


#define	MAXPACKET	4096	/* max packet size */

/* fraser */
int debugfile;

const char usage[] =
"Usage:	rdisc [-b] [-d] [-s] [-v] [-f] [-a] [-V] [send_address] [receive_address]\n"
#ifdef RDISC_SERVER
"       rdisc -r [-b] [-d] [-s] [-v] [-f] [-a] [-V] [-p <preference>] [-T <secs>]\n"
"		 [send_address] [receive_address]\n"
#endif
;


int s;			/* Socket file descriptor */
struct sockaddr_in whereto;/* Address to send to */

/* Common variables */
int verbose = 0;
int debug = 0;
int trace = 0;
int solicit = 0;
int ntransmitted = 0;
int nreceived = 0;
int forever = 0;	/* Never give up on host. If 0 defer fork until
			 * first response.
			 */

#ifdef RDISC_SERVER
/* Router variables */
int responder;
int max_adv_int = MAX_ADV_INT;
int min_adv_int;
int lifetime;
int initial_advert_interval = MAX_INITIAL_ADVERT_INTERVAL;
int initial_advertisements = MAX_INITIAL_ADVERTISEMENTS;
int preference = 0;		/* Setable with -p option */
#endif

/* Host variables */
int max_solicitations = MAX_SOLICITATIONS;
unsigned int solicitation_interval = SOLICITATION_INTERVAL;
int best_preference = 1;  	/* Set to record only the router(s) with the
				   best preference in the kernel. Not set
				   puts all routes in the kernel. */


static void graceful_finish(void);
static void finish(void);
static void timer(void);
static void initifs(void);
static u_short in_cksum(u_short *addr, int len);

static int logging = 0;

#define logerr(fmt...) ({ if (logging) syslog(LOG_ERR, fmt); \
			  else fprintf(stderr, fmt); })
#define logtrace(fmt...) ({ if (logging) syslog(LOG_INFO, fmt); \
			  else fprintf(stderr, fmt); })
#define logdebug(fmt...) ({ if (logging) syslog(LOG_DEBUG, fmt); \
			  else fprintf(stderr, fmt); })
static void logperror(char *str);

static __inline__ int isbroadcast(struct sockaddr_in *sin)
{
	return (sin->sin_addr.s_addr == INADDR_BROADCAST);
}

static __inline__ int ismulticast(struct sockaddr_in *sin)
{
	return IN_CLASSD(ntohl(sin->sin_addr.s_addr));
}

static void prusage(void)
{
	fputs(usage, stderr);
	exit(1);
}

void do_fork(void)
{
	int t;
	pid_t pid;
	long open_max;

	if (trace)
		return;
	if ((open_max = sysconf(_SC_OPEN_MAX)) == -1) {
		if (errno == 0) {
			(void) fprintf(stderr, "OPEN_MAX is not supported\n");
		} 
		else {
			(void) fprintf(stderr, "sysconf() error\n");
		}
		exit(1);
	}


	if ((pid=fork()) != 0)
		exit(0);

	for (t = 0; t < open_max; t++)
		if (t != s)
			close(t);

	setsid();
	initlog();
}

void signal_setup(int signo, void (*handler)(void))
{
	struct sigaction sa;

	memset(&sa, 0, sizeof(sa));

	sa.sa_handler = (void (*)(int))handler;
#ifdef SA_INTERRUPT
	sa.sa_flags = SA_INTERRUPT;
#endif
	sigaction(signo, &sa, NULL);
}

/*
 * 			M A I N
 */
char    *sendaddress, *recvaddress;

int main(int argc, char **argv)
{
	struct sockaddr_in from;
	char **av = argv;
	struct sockaddr_in *to = &whereto;
	struct sockaddr_in joinaddr;
	sigset_t sset, sset_empty;
#ifdef RDISC_SERVER
	int val;

	min_adv_int =( max_adv_int * 3 / 4);
	lifetime = (3*max_adv_int);
#endif

	argc--, av++;
	while (argc > 0 && *av[0] == '-') {
		while (*++av[0]) {
			switch (*av[0]) {
			case 'd':
				debug = 1;
				break;
			case 't':
				trace = 1;
				break;
			case 'v':
				verbose++;
				break;
			case 's':
				solicit = 1;
				break;
#ifdef RDISC_SERVER
			case 'r':
				responder = 1;
				break;
#endif
			case 'a':
				best_preference = 0;
				break;
			case 'b':
				best_preference = 1;
				break;
			case 'f':
				forever = 1;
				break;
			case 'V':
				printf("rdisc utility, iputils-%s\n", SNAPSHOT);
				exit(0);
#ifdef RDISC_SERVER
			case 'T':
				argc--, av++;
				if (argc != 0) {
					val = strtol(av[0], (char **)NULL, 0);
					if (val < 4 || val > 1800) {
						(void) fprintf(stderr,
							       "Bad Max Advertizement Interval\n");
						exit(1);
					}
					max_adv_int = val;
					min_adv_int =( max_adv_int * 3 / 4);
					lifetime = (3*max_adv_int);
				} else {
					prusage();
					/* NOTREACHED*/
				}
				goto next;
			case 'p':
				argc--, av++;
				if (argc != 0) {
					val = strtol(av[0], (char **)NULL, 0);
					preference = val;
				} else {
					prusage();
					/* NOTREACHED*/
				}
				goto next;
#endif
			default:
				prusage();
				/* NOTREACHED*/
			}
		}
#ifdef RDISC_SERVER
next:
#endif
		argc--, av++;
	}
	if( argc < 1)  {
		if (support_multicast()) {
			sendaddress = ALL_ROUTERS_ADDRESS;
#ifdef RDISC_SERVER
			if (responder)
				sendaddress = ALL_HOSTS_ADDRESS;
#endif
		} else
			sendaddress = "255.255.255.255";
	} else {
		sendaddress = av[0];
		argc--;
	}

	if (argc < 1) {
		if (support_multicast()) {
			recvaddress = ALL_HOSTS_ADDRESS;
#ifdef RDISC_SERVER
			if (responder)
				recvaddress = ALL_ROUTERS_ADDRESS;
#endif
		} else
			recvaddress = "255.255.255.255";
	} else {
		recvaddress = av[0];
		argc--;
	}
	if (argc != 0) {
		(void) fprintf(stderr, "Extra parameters\n");
		prusage();
		/* NOTREACHED */
	}

#ifdef RDISC_SERVER
	if (solicit && responder) {
		prusage();
		/* NOTREACHED */
	}
#endif

	if (!(solicit && !forever)) {
		do_fork();
/*
 * Added the next line to stop forking a second time
 * Fraser Gardiner - Sun Microsystems Australia
 */
		forever = 1;
	}

	memset( (char *)&whereto, 0, sizeof(struct sockaddr_in) );
	to->sin_family = AF_INET;
	to->sin_addr.s_addr = inet_addr(sendaddress);

	memset( (char *)&joinaddr, 0, sizeof(struct sockaddr_in) );
	joinaddr.sin_family = AF_INET;
	joinaddr.sin_addr.s_addr = inet_addr(recvaddress);

#ifdef RDISC_SERVER
	if (responder)
		srandom((int)gethostid());
#endif

	if ((s = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)) < 0) {
		logperror("socket");
		exit(5);
	}

	setlinebuf( stdout );

	signal_setup(SIGINT, finish );
	signal_setup(SIGTERM, graceful_finish );
	signal_setup(SIGHUP, initifs );
	signal_setup(SIGALRM, timer );

	sigemptyset(&sset);
	sigemptyset(&sset_empty);
	sigaddset(&sset, SIGALRM);
	sigaddset(&sset, SIGHUP);
	sigaddset(&sset, SIGTERM);
	sigaddset(&sset, SIGINT);

	init();
	if (join(s, &joinaddr) < 0) {
		logerr("Failed joining addresses\n");
		exit (2);
	}

	timer();	/* start things going */

	for (;;) {
		u_char	packet[MAXPACKET];
		int len = sizeof (packet);
		socklen_t fromlen = sizeof (from);
		int cc;

		cc=recvfrom(s, (char *)packet, len, 0,
			    (struct sockaddr *)&from, &fromlen);
		if (cc<0) {
			if (errno == EINTR)
				continue;
			logperror("recvfrom");
			continue;
		}

		sigprocmask(SIG_SETMASK, &sset, NULL);
		pr_pack( (char *)packet, cc, &from );
		sigprocmask(SIG_SETMASK, &sset_empty, NULL);
	}
	/*NOTREACHED*/
}

#define TIMER_INTERVAL 	3
#define GETIFCONF_TIMER	30

static int left_until_advertise;

/* Called every TIMER_INTERVAL */
void timer()
{
	static int time;
	static int left_until_getifconf;
	static int left_until_solicit;


	time += TIMER_INTERVAL;

	left_until_getifconf -= TIMER_INTERVAL;
	left_until_advertise -= TIMER_INTERVAL;
	left_until_solicit -= TIMER_INTERVAL;

	if (left_until_getifconf < 0) {
		initifs();
		left_until_getifconf = GETIFCONF_TIMER;
	}
#ifdef RDISC_SERVER
	if (responder && left_until_advertise <= 0) {
		ntransmitted++;
		advertise(&whereto, lifetime);
		if (ntransmitted < initial_advertisements)
			left_until_advertise = initial_advert_interval;
		else
			left_until_advertise = min_adv_int +
				((max_adv_int - min_adv_int) *
				 (random() % 1000)/1000);
	} else
#endif
	if (solicit && left_until_solicit <= 0) {
		ntransmitted++;
		solicitor(&whereto);
		if (ntransmitted < max_solicitations)
			left_until_solicit = solicitation_interval;
		else {
			solicit = 0;
			if (!forever && nreceived == 0)
				exit(5);
		}
	}
	age_table(TIMER_INTERVAL);
	alarm(TIMER_INTERVAL);
}

/*
 * 			S O L I C I T O R
 *
 * Compose and transmit an ICMP ROUTER SOLICITATION REQUEST packet.
 * The IP packet will be added on by the kernel.
 */
void
solicitor(struct sockaddr_in *sin)
{
	static u_char outpack[MAXPACKET];
	struct icmphdr *icp = (struct icmphdr *) ALLIGN(outpack);
	int packetlen, i;

	if (verbose) {
		logtrace("Sending solicitation to %s\n",
			 pr_name(sin->sin_addr));
	}
	icp->type = ICMP_ROUTER_SOLICITATION;
	icp->code = 0;
	icp->checksum = 0;
	icp->un.gateway = 0; /* Reserved */
	packetlen = 8;

	/* Compute ICMP checksum here */
	icp->checksum = in_cksum( (u_short *)icp, packetlen );

	if (isbroadcast(sin))
		i = sendbcast(s, (char *)outpack, packetlen);
	else if (ismulticast(sin))
		i = sendmcast(s, (char *)outpack, packetlen, sin);
	else
		i = sendto( s, (char *)outpack, packetlen, 0,
			   (struct sockaddr *)sin, sizeof(struct sockaddr));

	if( i < 0 || i != packetlen )  {
		if( i<0 ) {
		    logperror("solicitor:sendto");
		}
		logerr("wrote %s %d chars, ret=%d\n",
			sendaddress, packetlen, i );
	}
}

#ifdef RDISC_SERVER
/*
 * 			A V E R T I S E
 *
 * Compose and transmit an ICMP ROUTER ADVERTISEMENT packet.
 * The IP packet will be added on by the kernel.
 */
void
advertise(struct sockaddr_in *sin, int lft)
{
	static u_char outpack[MAXPACKET];
	struct icmp_ra *rap = (struct icmp_ra *) ALLIGN(outpack);
	struct icmp_ra_addr *ap;
	int packetlen, i, cc;

	if (verbose) {
		logtrace("Sending advertisement to %s\n",
			 pr_name(sin->sin_addr));
	}

	for (i = 0; i < num_interfaces; i++) {
		rap->icmp_type = ICMP_ROUTER_ADVERTISEMENT;
		rap->icmp_code = 0;
		rap->icmp_cksum = 0;
		rap->icmp_num_addrs = 0;
		rap->icmp_wpa = 2;
		rap->icmp_lifetime = htons(lft);
		packetlen = 8;

		/*
		 * TODO handle multiple logical interfaces per
		 * physical interface. (increment with rap->icmp_wpa * 4 for
		 * each address.)
		 */
		ap = (struct icmp_ra_addr *)ALLIGN(outpack + ICMP_MINLEN);
		ap->ira_addr = interfaces[i].localaddr.s_addr;
		ap->ira_preference = htonl(interfaces[i].preference);
		packetlen += rap->icmp_wpa * 4;
		rap->icmp_num_addrs++;

		/* Compute ICMP checksum here */
		rap->icmp_cksum = in_cksum( (u_short *)rap, packetlen );

		if (isbroadcast(sin))
			cc = sendbcastif(s, (char *)outpack, packetlen,
					&interfaces[i]);
		else if (ismulticast(sin))
			cc = sendmcastif( s, (char *)outpack, packetlen, sin,
					&interfaces[i]);
		else {
			struct interface *ifp = &interfaces[i];
			/*
			 * Verify that the interface matches the destination
			 * address.
			 */
			if ((sin->sin_addr.s_addr & ifp->netmask.s_addr) ==
			    (ifp->address.s_addr & ifp->netmask.s_addr)) {
				if (debug) {
					logdebug("Unicast to %s ",
						 pr_name(sin->sin_addr));
					logdebug("on interface %s, %s\n",
						 ifp->name,
						 pr_name(ifp->address));
				}
				cc = sendto( s, (char *)outpack, packetlen, 0,
					    (struct sockaddr *)sin,
					    sizeof(struct sockaddr));
			} else
				cc = packetlen;
		}
		if( cc < 0 || cc != packetlen )  {
			if (cc < 0) {
				logperror("sendto");
			} else {
				logerr("wrote %s %d chars, ret=%d\n",
				       sendaddress, packetlen, cc );
			}
		}
	}
}
#endif

/*
 * 			P R _ T Y P E
 *
 * Convert an ICMP "type" field to a printable string.
 */
char *
pr_type(int t)
{
	static char *ttab[] = {
		"Echo Reply",
		"ICMP 1",
		"ICMP 2",
		"Dest Unreachable",
		"Source Quench",
		"Redirect",
		"ICMP 6",
		"ICMP 7",
		"Echo",
		"Router Advertise",
		"Router Solicitation",
		"Time Exceeded",
		"Parameter Problem",
		"Timestamp",
		"Timestamp Reply",
		"Info Request",
		"Info Reply",
		"Netmask Request",
		"Netmask Reply"
	};

	if ( t < 0 || t > 16 )
		return("OUT-OF-RANGE");

	return(ttab[t]);
}

/*
 *			P R _ N A M E
 *
 * Return a string name for the given IP address.
 */
char *pr_name(struct in_addr addr)
{
	struct hostent *phe;
	static char buf[80];

	phe = gethostbyaddr((char *)&addr.s_addr, 4, AF_INET);
	if (phe == NULL)
		return( inet_ntoa(addr));
	snprintf(buf, sizeof(buf), "%s (%s)", phe->h_name, inet_ntoa(addr));
	return(buf);
}

/*
 *			P R _ P A C K
 *
 * Print out the packet, if it came from us.  This logic is necessary
 * because ALL readers of the ICMP socket get a copy of ALL ICMP packets
 * which arrive ('tis only fair).  This permits multiple copies of this
 * program to be run without having intermingled output (or statistics!).
 */
void
pr_pack(char *buf, int cc, struct sockaddr_in *from)
{
	struct iphdr *ip;
	struct icmphdr *icp;
	int i;
	int hlen;

	ip = (struct iphdr *) ALLIGN(buf);
	hlen = ip->ihl << 2;
	if (cc < hlen + 8) {
		if (verbose)
			logtrace("packet too short (%d bytes) from %s\n", cc,
				 pr_name(from->sin_addr));
		return;
	}
	cc -= hlen;
	icp = (struct icmphdr *)ALLIGN(buf + hlen);

	switch (icp->type) {
	case ICMP_ROUTER_ADVERTISEMENT:
	{
		struct icmp_ra *rap = (struct icmp_ra *)ALLIGN(icp);
		struct icmp_ra_addr *ap;

#ifdef RDISC_SERVER
		if (responder)
			break;
#endif

		/* TBD verify that the link is multicast or broadcast */
		/* XXX Find out the link it came in over? */
		if (in_cksum((u_short *)ALLIGN(buf+hlen), cc)) {
			if (verbose)
				logtrace("ICMP %s from %s: Bad checksum\n",
					 pr_type((int)rap->icmp_type),
					 pr_name(from->sin_addr));
			return;
		}
		if (rap->icmp_code != 0) {
			if (verbose)
				logtrace("ICMP %s from %s: Code = %d\n",
					 pr_type((int)rap->icmp_type),
					 pr_name(from->sin_addr),
					 rap->icmp_code);
			return;
		}
		if (rap->icmp_num_addrs < 1) {
			if (verbose)
				logtrace("ICMP %s from %s: No addresses\n",
					 pr_type((int)rap->icmp_type),
					 pr_name(from->sin_addr));
			return;
		}
		if (rap->icmp_wpa < 2) {
			if (verbose)
				logtrace("ICMP %s from %s: Words/addr = %d\n",
					 pr_type((int)rap->icmp_type),
					 pr_name(from->sin_addr),
					 rap->icmp_wpa);
			return;
		}
		if ((unsigned)cc <
		    8 + rap->icmp_num_addrs * rap->icmp_wpa * 4) {
			if (verbose)
				logtrace("ICMP %s from %s: Too short %d, %d\n",
					      pr_type((int)rap->icmp_type),
					      pr_name(from->sin_addr),
					      cc,
					      8 + rap->icmp_num_addrs * rap->icmp_wpa * 4);
			return;
		}

		if (verbose)
			logtrace("ICMP %s from %s, lifetime %d\n",
				      pr_type((int)rap->icmp_type),
				      pr_name(from->sin_addr),
				      ntohs(rap->icmp_lifetime));

		/* Check that at least one router address is a neighboor
		 * on the arriving link.
		 */
		for (i = 0; (unsigned)i < rap->icmp_num_addrs; i++) {
			struct in_addr ina;
			ap = (struct icmp_ra_addr *)
				ALLIGN(buf + hlen + 8 +
				       i * rap->icmp_wpa * 4);
			ina.s_addr = ap->ira_addr;
			if (verbose)
				logtrace("\taddress %s, preference 0x%x\n",
					      pr_name(ina),
					      (unsigned int)ntohl(ap->ira_preference));
			if (is_directly_connected(ina))
				record_router(ina,
					      ntohl(ap->ira_preference),
					      ntohs(rap->icmp_lifetime));
		}
		nreceived++;
		if (!forever) {
			do_fork();
			forever = 1;
/*
 * The next line was added so that the alarm is set for the new procces
 * Fraser Gardiner Sun Microsystems Australia
 */
			(void) alarm(TIMER_INTERVAL);
		}
		break;
	}

#ifdef RDISC_SERVER
	case ICMP_ROUTER_SOLICITATION:
	{
		struct sockaddr_in sin;

		if (!responder)
			break;

		/* TBD verify that the link is multicast or broadcast */
		/* XXX Find out the link it came in over? */

		if (in_cksum((u_short *)ALLIGN(buf+hlen), cc)) {
			if (verbose)
				logtrace("ICMP %s from %s: Bad checksum\n",
					      pr_type((int)icp->type),
					      pr_name(from->sin_addr));
			return;
		}
		if (icp->code != 0) {
			if (verbose)
				logtrace("ICMP %s from %s: Code = %d\n",
					      pr_type((int)icp->type),
					      pr_name(from->sin_addr),
					      icp->code);
			return;
		}

		if (cc < ICMP_MINLEN) {
			if (verbose)
				logtrace("ICMP %s from %s: Too short %d, %d\n",
					      pr_type((int)icp->type),
					      pr_name(from->sin_addr),
					      cc,
					      ICMP_MINLEN);
			return;
		}

		if (verbose)
			logtrace("ICMP %s from %s\n",
				      pr_type((int)icp->type),
				      pr_name(from->sin_addr));

		/* Check that ip_src is either a neighboor
		 * on the arriving link or 0.
		 */
		sin.sin_family = AF_INET;
		if (ip->saddr == 0) {
			/* If it was sent to the broadcast address we respond
			 * to the broadcast address.
			 */
			if (IN_CLASSD(ntohl(ip->daddr)))
				sin.sin_addr.s_addr = htonl(0xe0000001);
			else
				sin.sin_addr.s_addr = INADDR_BROADCAST;
			/* Restart the timer when we broadcast */
			left_until_advertise = min_adv_int +
				((max_adv_int - min_adv_int)
				 * (random() % 1000)/1000);
		} else {
			sin.sin_addr.s_addr = ip->saddr;
			if (!is_directly_connected(sin.sin_addr)) {
				if (verbose)
					logtrace("ICMP %s from %s: source not directly connected\n",
						      pr_type((int)icp->type),
						      pr_name(from->sin_addr));
				break;
			}
		}
		nreceived++;
		ntransmitted++;
		advertise(&sin, lifetime);
		break;
	}
#endif
	}
}


/*
 *			I N _ C K S U M
 *
 * Checksum routine for Internet Protocol family headers (C Version)
 *
 */
#if BYTE_ORDER == LITTLE_ENDIAN
# define ODDBYTE(v)	(v)
#elif BYTE_ORDER == BIG_ENDIAN
# define ODDBYTE(v)	((u_short)(v) << 8)
#else
# define ODDBYTE(v)	htons((u_short)(v) << 8)
#endif

u_short in_cksum(u_short *addr, int len)
{
	register int nleft = len;
	register u_short *w = addr;
	register u_short answer;
	register int sum = 0;

	/*
	 *  Our algorithm is simple, using a 32 bit accumulator (sum),
	 *  we add sequential 16 bit words to it, and at the end, fold
	 *  back all the carry bits from the top 16 bits into the lower
	 *  16 bits.
	 */
	while( nleft > 1 )  {
		sum += *w++;
		nleft -= 2;
	}

	/* mop up an odd byte, if necessary */
	if( nleft == 1 )
		sum += ODDBYTE(*(u_char *)w);	/* le16toh() may be unavailable on old systems */

	/*
	 * add back carry outs from top 16 bits to low 16 bits
	 */
	sum = (sum >> 16) + (sum & 0xffff);	/* add hi 16 to low 16 */
	sum += (sum >> 16);			/* add carry */
	answer = ~sum;				/* truncate to 16 bits */
	return (answer);
}

/*
 *			F I N I S H
 *
 * Print out statistics, and give up.
 * Heavily buffered STDIO is used here, so that all the statistics
 * will be written with 1 sys-write call.  This is nice when more
 * than one copy of the program is running on a terminal;  it prevents
 * the statistics output from becomming intermingled.
 */
void
finish()
{
#ifdef RDISC_SERVER
	if (responder) {
		/* Send out a packet with a preference so that all
		 * hosts will know that we are dead.
		 *
		 * Wrong comment, wrong code.
		 *	ttl must be set to 0 instead. --ANK
		 */
		logerr("terminated\n");
		ntransmitted++;
		advertise(&whereto, 0);
	}
#endif
	logtrace("\n----%s rdisc Statistics----\n", sendaddress );
	logtrace("%d packets transmitted, ", ntransmitted );
	logtrace("%d packets received, ", nreceived );
	logtrace("\n");
	(void) fflush(stdout);
	exit(0);
}

void
graceful_finish()
{
	discard_table();
	finish();
	exit(0);
}


/* From libc/rpc/pmap_rmt.c */

int
sendbcast(int s, char *packet, int packetlen)
{
	int i, cc;

	for (i = 0; i < num_interfaces; i++) {
		if ((interfaces[i].flags & (IFF_BROADCAST|IFF_POINTOPOINT)) == 0)
			continue;
		cc = sendbcastif(s, packet, packetlen, &interfaces[i]);
		if (cc!= packetlen) {
			return (cc);
		}
	}
	return (packetlen);
}

int
sendbcastif(int s, char *packet, int packetlen, struct interface *ifp)
{
	int on;
	int cc;
	struct sockaddr_in baddr;

	baddr.sin_family = AF_INET;
	baddr.sin_addr = ifp->bcastaddr;
	if (debug)
		logdebug("Broadcast to %s\n",
			 pr_name(baddr.sin_addr));
	on = 1;
	setsockopt(s, SOL_SOCKET, SO_BROADCAST, (char*)&on, sizeof(on));
	cc = sendto(s, packet, packetlen, 0,
		    (struct sockaddr *)&baddr, sizeof (struct sockaddr));
	if (cc!= packetlen) {
		logperror("sendbcast: sendto");
		logerr("Cannot send broadcast packet to %s\n",
		       pr_name(baddr.sin_addr));
	}
	on = 0;
	setsockopt(s, SOL_SOCKET, SO_BROADCAST, (char*)&on, sizeof(on));
	return (cc);
}

int
sendmcast(int s, char *packet, int packetlen, struct sockaddr_in *sin)
{
	int i, cc;

	for (i = 0; i < num_interfaces; i++) {
		if ((interfaces[i].flags & (IFF_BROADCAST|IFF_POINTOPOINT|IFF_MULTICAST)) == 0)
			continue;
		cc = sendmcastif(s, packet, packetlen, sin, &interfaces[i]);
		if (cc!= packetlen) {
			return (cc);
		}
	}
	return (packetlen);
}

int
sendmcastif(int s, char *packet, int packetlen,	struct sockaddr_in *sin,
	    struct interface *ifp)
{
	int cc;
	struct ip_mreqn mreq;

	memset(&mreq, 0, sizeof(mreq));
	mreq.imr_ifindex = ifp->ifindex;
	mreq.imr_address = ifp->localaddr;
	if (debug)
		logdebug("Multicast to interface %s, %s\n",
			 ifp->name,
			 pr_name(mreq.imr_address));
	if (setsockopt(s, IPPROTO_IP, IP_MULTICAST_IF,
		       (char *)&mreq,
		       sizeof(mreq)) < 0) {
		logperror("setsockopt (IP_MULTICAST_IF)");
		logerr("Cannot send multicast packet over interface %s, %s\n",
		       ifp->name,
		       pr_name(mreq.imr_address));
		return (-1);
	}
	cc = sendto(s, packet, packetlen, 0,
		    (struct sockaddr *)sin, sizeof (struct sockaddr));
	if (cc!= packetlen) {
		logperror("sendmcast: sendto");
		logerr("Cannot send multicast packet over interface %s, %s\n",
		       ifp->name, pr_name(mreq.imr_address));
	}
	return (cc);
}

void
init()
{
	initifs();
#ifdef RDISC_SERVER
	{
		int i;
		for (i = 0; i < interfaces_size; i++)
			interfaces[i].preference = preference;
	}
#endif
}

void
initifs()
{
	int	sock;
	struct ifconf ifc;
	struct ifreq ifreq, *ifr;
	struct sockaddr_in *sin;
	int n, i;
	char *buf;
	int numifs;
	unsigned bufsize;

	sock = socket(AF_INET, SOCK_DGRAM, 0);
	if (sock < 0) {
		logperror("initifs: socket");
		return;
	}
#ifdef SIOCGIFNUM
	if (ioctl(sock, SIOCGIFNUM, (char *)&numifs) < 0) {
		numifs = MAXIFS;
	}
#else
	numifs = MAXIFS;
#endif
	bufsize = numifs * sizeof(struct ifreq);
	buf = (char *)malloc(bufsize);
	if (buf == NULL) {
		logerr("out of memory\n");
		(void) close(sock);
		return;
	}
	if (interfaces)
		interfaces = (struct interface *)ALLIGN(realloc((char *)interfaces,
					 numifs * sizeof(struct interface)));
	else
		interfaces = (struct interface *)ALLIGN(malloc(numifs *
						sizeof(struct interface)));
	if (interfaces == NULL) {
		logerr("out of memory\n");
		(void) close(sock);
		(void) free(buf);
		return;
	}
	interfaces_size = numifs;

	ifc.ifc_len = bufsize;
	ifc.ifc_buf = buf;
	if (ioctl(sock, SIOCGIFCONF, (char *)&ifc) < 0) {
		logperror("initifs: ioctl (get interface configuration)");
		(void) close(sock);
		(void) free(buf);
		return;
	}
	ifr = ifc.ifc_req;
	for (i = 0, n = ifc.ifc_len/sizeof (struct ifreq); n > 0; n--, ifr++) {
		ifreq = *ifr;
		if (strlen(ifreq.ifr_name) >= IFNAMSIZ)
			continue;
		if (ioctl(sock, SIOCGIFFLAGS, (char *)&ifreq) < 0) {
			logperror("initifs: ioctl (get interface flags)");
			continue;
		}
		if (ifr->ifr_addr.sa_family != AF_INET)
			continue;
		if ((ifreq.ifr_flags & IFF_UP) == 0)
			continue;
		if (ifreq.ifr_flags & IFF_LOOPBACK)
			continue;
		if ((ifreq.ifr_flags & (IFF_MULTICAST|IFF_BROADCAST|IFF_POINTOPOINT)) == 0)
			continue;
		strncpy(interfaces[i].name, ifr->ifr_name, IFNAMSIZ-1);

		sin = (struct sockaddr_in *)ALLIGN(&ifr->ifr_addr);
		interfaces[i].localaddr = sin->sin_addr;
		interfaces[i].flags = ifreq.ifr_flags;
		interfaces[i].netmask.s_addr = (__u32)0xffffffff;
		if (ioctl(sock, SIOCGIFINDEX, (char *)&ifreq) < 0) {
			logperror("initifs: ioctl (get ifindex)");
			continue;
		}
		interfaces[i].ifindex = ifreq.ifr_ifindex;
		if (ifreq.ifr_flags & IFF_POINTOPOINT) {
			if (ioctl(sock, SIOCGIFDSTADDR, (char *)&ifreq) < 0) {
				logperror("initifs: ioctl (get destination addr)");
				continue;
			}
			sin = (struct sockaddr_in *)ALLIGN(&ifreq.ifr_addr);
			/* A pt-pt link is identified by the remote address */
			interfaces[i].address = sin->sin_addr;
			interfaces[i].remoteaddr = sin->sin_addr;
			/* Simulate broadcast for pt-pt */
			interfaces[i].bcastaddr = sin->sin_addr;
			interfaces[i].flags |= IFF_BROADCAST;
		} else {
			/* Non pt-pt links are identified by the local address */
			interfaces[i].address = interfaces[i].localaddr;
			interfaces[i].remoteaddr = interfaces[i].address;
			if (ioctl(sock, SIOCGIFNETMASK, (char *)&ifreq) < 0) {
				logperror("initifs: ioctl (get netmask)");
				continue;
			}
			sin = (struct sockaddr_in *)ALLIGN(&ifreq.ifr_addr);
			interfaces[i].netmask = sin->sin_addr;
			if (ifreq.ifr_flags & IFF_BROADCAST) {
				if (ioctl(sock, SIOCGIFBRDADDR, (char *)&ifreq) < 0) {
					logperror("initifs: ioctl (get broadcast address)");
					continue;
				}
				sin = (struct sockaddr_in *)ALLIGN(&ifreq.ifr_addr);
				interfaces[i].bcastaddr = sin->sin_addr;
			}
		}
#ifdef notdef
		if (debug)
			logdebug("Found interface %s, flags 0x%x\n",
				 pr_name(interfaces[i].localaddr),
				 interfaces[i].flags);
#endif
		i++;
	}
	num_interfaces = i;
#ifdef notdef
	if (debug)
		logdebug("Found %d interfaces\n", num_interfaces);
#endif
	(void) close(sock);
	(void) free(buf);
}

int
join(int sock, struct sockaddr_in *sin)
{
	int i, j;
	struct ip_mreqn mreq;
	int joined[num_interfaces];

	memset(joined, 0, sizeof(joined));

	if (isbroadcast(sin))
		return (0);

	mreq.imr_multiaddr = sin->sin_addr;
	for (i = 0; i < num_interfaces; i++) {
		for (j = 0; j < i; j++) {
			if (joined[j] == interfaces[i].ifindex)
				break;
		}
		if (j != i)
			continue;

		mreq.imr_ifindex = interfaces[i].ifindex;
		mreq.imr_address.s_addr = 0;

		if (setsockopt(sock, IPPROTO_IP, IP_ADD_MEMBERSHIP,
			       (char *)&mreq, sizeof(mreq)) < 0) {
			logperror("setsockopt (IP_ADD_MEMBERSHIP)");
			return (-1);
		}

		joined[i] = interfaces[i].ifindex;
	}
	return (0);
}

int support_multicast()
{
	int sock;
	u_char ttl = 1;

	sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
	if (sock < 0) {
		logperror("support_multicast: socket");
		return (0);
	}

	if (setsockopt(sock, IPPROTO_IP, IP_MULTICAST_TTL,
		       (char *)&ttl, sizeof(ttl)) < 0) {
		(void) close(sock);
		return (0);
	}
	(void) close(sock);
	return (1);
}

int
is_directly_connected(struct in_addr in)
{
	int i;

	for (i = 0; i < num_interfaces; i++) {
		/* Check that the subnetwork numbers match */

		if ((in.s_addr & interfaces[i].netmask.s_addr ) ==
		    (interfaces[i].remoteaddr.s_addr & interfaces[i].netmask.s_addr))
			return (1);
	}
	return (0);
}

/*
 * TABLES
 */
struct table {
	struct in_addr	router;
	int		preference;
	int		remaining_time;
	int		in_kernel;
	struct table	*next;
};

struct table *table;

struct table *
find_router(struct in_addr addr)
{
	struct table *tp;

	tp = table;
	while (tp) {
		if (tp->router.s_addr == addr.s_addr)
			return (tp);
		tp = tp->next;
	}
	return (NULL);
}

int max_preference(void)
{
	struct table *tp;
	int max = (int)INELIGIBLE_PREF;

	tp = table;
	while (tp) {
		if (tp->preference > max)
			max = tp->preference;
		tp = tp->next;
	}
	return (max);
}


/* Note: this might leave the kernel with no default route for a short time. */
void
age_table(int time)
{
	struct table **tpp, *tp;
	int recalculate_max = 0;
	int max = max_preference();

	tpp = &table;
	while (*tpp != NULL) {
		tp = *tpp;
		tp->remaining_time -= time;
		if (tp->remaining_time <= 0) {
			*tpp = tp->next;
			if (tp->in_kernel)
				del_route(tp->router);
			if (best_preference &&
			    tp->preference == max)
				recalculate_max++;
			free((char *)tp);
		} else {
			tpp = &tp->next;
		}
	}
	if (recalculate_max) {
		int max = max_preference();

		if (max != INELIGIBLE_PREF) {
			tp = table;
			while (tp) {
				if (tp->preference == max && !tp->in_kernel) {
					add_route(tp->router);
					tp->in_kernel++;
				}
				tp = tp->next;
			}
		}
	}
}

void discard_table(void)
{
	struct table **tpp, *tp;

	tpp = &table;
	while (*tpp != NULL) {
		tp = *tpp;
		*tpp = tp->next;
		if (tp->in_kernel)
			del_route(tp->router);
		free((char *)tp);
	}
}


void
record_router(struct in_addr router, int preference, int ttl)
{
	struct table *tp;
	int old_max = max_preference();
	int changed_up = 0;	/* max preference could have increased */
	int changed_down = 0;	/* max preference could have decreased */

	if (ttl < 4)
		preference = INELIGIBLE_PREF;

	if (debug)
		logdebug("Recording %s, ttl %d, preference 0x%x\n",
			 pr_name(router),
			 ttl,
			 preference);
	tp = find_router(router);
	if (tp) {
		if (tp->preference > preference &&
		    tp->preference == old_max)
			changed_down++;
		else if (preference > tp->preference)
			changed_up++;
		tp->preference = preference;
		tp->remaining_time = ttl;
	} else {
		if (preference > old_max)
			changed_up++;
		tp = (struct table *)ALLIGN(malloc(sizeof(struct table)));
		if (tp == NULL) {
			logerr("Out of memory\n");
			return;
		}
		tp->router = router;
		tp->preference = preference;
		tp->remaining_time = ttl;
		tp->in_kernel = 0;
		tp->next = table;
		table = tp;
	}
	if (!tp->in_kernel &&
	    (!best_preference || tp->preference == max_preference()) &&
	    tp->preference != INELIGIBLE_PREF) {
		add_route(tp->router);
		tp->in_kernel++;
	}
	if (tp->preference == INELIGIBLE_PREF && tp->in_kernel) {
		del_route(tp->router);
		tp->in_kernel = 0;
	}
	if (best_preference && changed_down) {
		/* Check if we should add routes */
		int new_max = max_preference();
		if (new_max != INELIGIBLE_PREF) {
			tp = table;
			while (tp) {
				if (tp->preference == new_max &&
				    !tp->in_kernel) {
					add_route(tp->router);
					tp->in_kernel++;
				}
				tp = tp->next;
			}
		}
	}
	if (best_preference && (changed_up || changed_down)) {
		/* Check if we should remove routes already in the kernel */
		int new_max = max_preference();
		tp = table;
		while (tp) {
			if (tp->preference < new_max && tp->in_kernel) {
				del_route(tp->router);
				tp->in_kernel = 0;
			}
			tp = tp->next;
		}
	}
}

void
add_route(struct in_addr addr)
{
	if (debug)
		logdebug("Add default route to %s\n", pr_name(addr));
	rtioctl(addr, SIOCADDRT);
}

void
del_route(struct in_addr addr)
{
	if (debug)
		logdebug("Delete default route to %s\n", pr_name(addr));
	rtioctl(addr, SIOCDELRT);
}

void
rtioctl(struct in_addr addr, int op)
{
	int sock;
	struct rtentry rt;
	struct sockaddr_in *sin;

	memset((char *)&rt, 0, sizeof(struct rtentry));
	rt.rt_dst.sa_family = AF_INET;
	rt.rt_gateway.sa_family = AF_INET;
	rt.rt_genmask.sa_family = AF_INET;
	sin = (struct sockaddr_in *)ALLIGN(&rt.rt_gateway);
	sin->sin_addr = addr;
	rt.rt_flags = RTF_UP | RTF_GATEWAY;

	sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
	if (sock < 0) {
		logperror("rtioctl: socket");
		return;
	}
	if (ioctl(sock, op, (char *)&rt) < 0) {
		if (!(op == SIOCADDRT && errno == EEXIST))
			logperror("ioctl (add/delete route)");
	}
	(void) close(sock);
}

/*
 * LOGGER
 */

void initlog(void)
{
	logging++;
	openlog("in.rdiscd", LOG_PID | LOG_CONS, LOG_DAEMON);
}


void
logperror(char *str)
{
	if (logging)
		syslog(LOG_ERR, "%s: %m", str);
	else
		(void) fprintf(stderr, "%s: %s\n", str, strerror(errno));
}


File: /README.md

# mikrotik-pings

Mikrotik RouterOS ping like commands

Baseado no pacote iputils-s20121221.
Adicionado arquivo: colors.h
Editado: ping_commons.h e ping_commons.c

<pre>

make ping
make ping6

./ping 200.160.2.3 -c 6

 SEQ HOST                                      SIZE TTL TIME  STATUS
   1 200.160.2.3                                 64  53 23.2   echo reply
   2 200.160.2.3                                 64  53 24.0   echo reply
   3 200.160.2.3                                 64  53 23.3   echo reply
   4 200.160.2.3                                 64  53 23.6   echo reply
   5 200.160.2.3                                 64  53 23.1   echo reply
   6 200.160.2.3                                 64  53 23.1   echo reply
     sent=6 received=6 packet-loss=0 min-rtt=23.159 avg-rtt=23.433 max-rtt=24.037


./ping6 2804:49c:3103:401:ffff:ffff:ffff:1 -c 6

 SEQ HOST                                      SIZE TTL TIME  STATUS
   1 2804:49c:3103:401:ffff:ffff:ffff:1        1408  54 61.5   echo reply
   2 2804:49c:3103:401:ffff:ffff:ffff:1        1408  54 53.2   echo reply
   3 2804:49c:3103:401:ffff:ffff:ffff:1        1408  54 54.2   echo reply
   4 2804:49c:3103:401:ffff:ffff:ffff:1        1408  54 60.6   echo reply
   5 2804:49c:3103:401:ffff:ffff:ffff:1        1408  54 53.8   echo reply
   6 2804:49c:3103:401:ffff:ffff:ffff:1        1408  54 52.6   echo reply
     sent=6 received=6 packet-loss=0 min-rtt=52.617 avg-rtt=56.023 max-rtt=61.531

</pre>


File: /RELNOTES
[s20121221]

YOSHIFUJI Hideaki (14):
      ninfod: Use unsigned int for digest.
      ninfod: nanosleep(3) needs <time.h>.
      ninfod: Too many arguments for syslog(3)/fprintf(3) via DEBUG().
      ninfod: Fix several warnings on ununsed variables.
      ping6: Print unknown ICMP type.
      ping6: Fix flowlabel switch (-F option).
      arping: Fix sysfs decimal/hexadecimal parser for libsysfs support.
      ping6: Use GNU TLS by default.
      ninfod: Fix memory leakage in error path.
      ninfod: Fix off-by-one error to check possible programming error (again).
      ninfod: Do not expose freed buffer to caller.
      ping6: Ensure to initialize msghdr.
      ninfod: Support GNU TLS.
      ninfod: Allow printing usage without permission errors.


[s20121207]

YOSHIFUJI Hideaki (2):
      RELNOTES: Typos.
      ping,ping6: Check outgoing device only if specified.


[s20121205]

Jan Synacek (1):
      ping,tracepath doc: Fix missing end tags.

YOSHIFUJI Hideaki (35):
      tracepath6: packet length option (-l) did not have any effect.
      tracepath,tracepath6: Fix pktlen message.
      tracepath,tracepath6: Use calloc(3) instead of using stack.
      tracepath6: Ignore families other than IPv4 and IPv6.
      ping6: Improve randomness of NI Nonce.
      tracepath,tracepath6 doc: Fix default pktlen.
      ping,rdisc: Optimize checksumming.
      makefile: Static link support for crypto, resolv, cap and sysfs.
      doc: Ajdust spaces around sqare brackets.
      ping,rdisc: Use macro to get odd byte when checksumming.
      ping6: Do not try to free memory pointed by uninitialized variable on error path.
      arping: Allow building without default interface.
      arping: No default interface by default.
      arping: Allow printing usage without permission errors.
      ping,ping6: Allow printing usage without permission errors.
      ping,ping6: Fix cap_t leakage.
      arping,ping,ping6: Do not ideologically check return value from cap_free,cap_{set,get}_flag().
      arping: Fix sysfs_class leakage on error path.
      arping: Some comments for new functions for finding devices support.
      arping: Typo in type declaration.
      makefile: Use call function for external libraries.
      makefile: Add more comments.
      arping: Ensure to fail if no appropriate device found with sysfs.
      arping: Enforce user to specify device (-I) if multiple devices found.
      Makefile: parameterize options for linking libraries.
      Makefile: Use shell function instead if backquotes.
      Makefile: Ensure to have same date when making snapshot.
      spec: Maintainer does not use ipsec.spec.
      spec: partially sync with fedora.
      Makefile: Bump date in iputils.spec as well.
      spec: Add exmple lines for suid-root installation
      spec: Sort changelog.
      ping: Exit on SO_BINDTODEVICE failure.
      ping: Warn if kernel has selected source address from other interface.
      ping: Clarify difference between -I device and -I addr.


[s20121126]

YOSHIFUJI Hideaki (5):
      tracepath: Repair tracepath without -p option.
      tracepath,tracepath6: -p option in usage.
      ping,ping6: Use MAX_DUP_CHK directly, not using mx_dup_chk variable.
      ping,ping6: Abstract received bitmap macros/definitions.
      ping,ping6: Use __u64 or __u32 for bitmap.


[s20121125]

YOSHIFUJI Hideaki (30):
      ping6: Use IN6_IS_ADDR_UNSPECIFIED() instead of our own helper function.
      ping6 doc: Explicitly describe ping6 is IPv6 version if ping.
      ping6: Deprecate source routing by default (RFC5095).
      ping6: Use RFC3542 functions and definition for source routing.
      ping6: Introduce niquery_is_enabled() for readability.
      arping doc: interface is optional (-I option).
      ping: Eliminate dirty hack to cope with ancient egcs bug.
      Makefile: Fix missing right parenthes in comment.
      arping: Fix build failure with USE_SYSFS=yes and/or WITHOUT_IFADDRS=yes
      arping: Unify source files.
      arping: Reorder functions and comment out unsued code.
      arping,ping,ping6,tracepath,traceroute6 Makefile: Support static link of libidn by USE_IDN=static.
      Makefile: Minimize statically linked libraries.
      ping6: Do not clear seq check array twice for NI.
      ping6: Use MD5_DIGEST_LENGTH instead of magic value 16.
      ping6: Introduce helper functions for nonce in NI.
      ping6: Introduce NI_NONCE_SIZE macro instead of magic value 8.
      ping6: Ensure to call srand() to get some randomness in NI Nonce.
      ping6: Generate different NI Nonce in each NI Query (Memory version).
      ping6: Generate different NI Nonce in each NI Query (MD5 version).
      ping6: Cache NI Nonce.
      ping6: Print 'sequence number' embedded in NI Nonce.
      ninfod: Do noy try to memcpy to self.
      ninfod Makefile: More precise dependencies.
      ninfod: Discard multicat packet outside linklocal scope.
      ninfod: Apply default policy to refuse queries from global addresses.
      ninfod: Normalize timespec for delay.
      ninfod: Fix double-free without pthreads.
      ninfod: Do not mix output from multiple threads.
      ninfod: Employ internal buffer in stderrlog() for common case.


[s20121121]

Jan Synacek (2):
      ping,ping6: Add newline to error message.
      ping: Don't free an unintialized value.

YOSHIFUJI Hideaki (31):
      arping,clockdiff,ping,rarpd,rdisc,traceroute6 doc: s/CAP_NET_RAWIO/CAP_NET_RAW/.
      ping,ping6: Do not assume radix point is denoted by '.' (-i option).
      arping,ping,ping6,rdisc,traceroute6: Fix version string.
      makefile: Give -fno-strict-aliasing to compiler by default.
      ping6: Use SCOPE_DELIMITER.
      Makefile: Remove -lm from ADDLIB.
      rdisc_srv,Makefile: Fix build.
      rdisc_srv,Makefile: Build rdisc_srv with make all.
      arping: set_device_broadcast() does not need to store return value of sub-functions.
      arping,Makefile: Make default interface configurable.
      arping: Do not allow empty device name (-I option).
      arping: Introduce check_ifflags() helper function.
      arping: Introduce device structure to hold output device information.
      arping: ALlow no default interface and select one by getifaddrs().
      arping: Introduce 2nd (legacy) method to select interface by ioctls.
      arping,Makefile: Allow build without getifaddrs() with WITHOUT_IFADDRS=yes.
      Makefile: Use $< instead of $^ to complile C source code.
      ping,ping6: Reorder command-line options in alphabetical order.
      ping6: Show suboptions for Node Information Queries if -N suboption is invalid.
      ping,ping6 doc: Readability for TOS (-Q) option.
      rdisc: Missing new line after usage.
      rdisc: Make rdisc with responder support if configured.
      Makefile: distclean depends on clean.
      Makefile: Default to -O3.
      Makefile: Minimize options to gcc.
      Makefile: Add rule to build assembly files.
      arping,Makefile: 3rd legacy implementation to check network devices.
      arping: Less ifdefs.
      rdisc doc: Document -r, -p and -T options.
      ping6: NI Subjecet address did not work (-N subject-{ipv6,ipv4] suboptions).
      ping6: Ensure to detect subject type conflicts.


[s20121114]

Jan Synacek (2):
      clockdiff: remove unused variable
      ping: Wrap SO_BINDTODEVICE with the correct capability.

YOSHIFUJI Hideaki (13):
      ping: IP_MULTICAST_IF does not need CAP_NET_RAW.
      ping6: Check ranges of flowlabel (-F option) and tclass (-Q option) arguments.
      ping6: Accept 0x-notation for flowlabel (-F option) and tclass (-Q option) arguments.
      ping,ping6: Manual update regarding -F, -Q and -N option.
      arping,ping,ping6: Defer exitting to allow users to see usage.
      arping,ping,ping6,ninfod: Change euid to uid (non-root) even if capabiliy is enabled.
      ninfod: Add configure.
      ninfod: libcap support to drop capabilities.
      ninfod: Add run as user (-u user) option.
      ninfod: Fix usage message.
      arping,clockdiff,rarpd,rdisc,tftpd: Change RFC source to tools.ietf.org.
      ninfod: Add ninfod(8) manpage.
      makefile: Add ninfod, distclean targets.


[s20121112]

Sergey Fionov (1):
      ping,ping6: Fallback to numeric addresses while exiting

YOSHIFUJI Hideaki (18):
      ping,ping6: Rework capability support and Make sure -m and -I options work.
      ping,tracepath: Spelling fixes in manpages.
      ping,ping6: Fix integer overflow with large interval value (-i option).
      clockdiff: Make it work with large pid.
      ping,ping6: Make in_pr_addr volatile.
      arping: Do not quit too early with large deadline value (-w option).
      arping: Maintain minimum capabilities for SO_BINDTODEVICE(-I option).
      ping: Fix recorded route comparison.
      arping: Use getifaddrs() to get broadcast address.
      ping6: Fix typo in error message.
      ping6: Generate NI Group Address and Subject Name at once.
      ping,ping6: Unmask signals on start-up.
      arping: Build with USE_CAP=no.
      arping,ping,ping6,tracepath,tracepath6,traceroute6: Experimental IDN support.
      ping6: IDN support for the Subject Name in NI Query.
      tracepath,tracepath6: Introduce -p option for port.
      ping6: Add missing definitions/declarations for flowlabel management (-F option).
      makefile: Do not include merge commits in RELNOTES.


[s20121106]

YOSHIFUJI Hideaki (5):
      ninfod: Attatch configure and renew config.h.in.
      makefile: clean-up
      tracepath6: Print reason on getadrinfo() failure.
      ping,ping6: Fix hang with -f option.
      ping: Make sure to print C if checksum failed with -f option.


[s20121011]

Jan Synacek (2):
      ping,ping6: Defer the dropping if the "-m" is specified and correct capability is set.
      ping: Fix typo in echo reply

Ole Bjorn Hessen (1):
      ping: report outstanding packets before sending next packet

YOSHIFUJI Hideaki (32):
      ping,ping6: Add -D to synopsis.
      ping: More icmp code descriptions.
      ping,ping6: Hide ipg/ewma info without packets received.
      ping6: Remove unused variable.
      ping6: Help for -N suboptions.
      tracepath,tracepath6: Use argument type of int for field width specifier.
      clockdiff: Call nice() before changing effective uid.
      rdisc: Use fputs() instead of fprintf() to shut up gcc warning.
      rarpd: Check return value of chdir().
      makefile: Introduce new variable for capability support.
      ping,ping6: Check return value of write(2) for stdout.
      ping6,tracepath,tracepath6: Do not dereference type-punned pointer directly.
      Makefile: host changed from takos to pleiades.
      ping6: Provide enough buffer for dn_comp() and make NI Query with Name subject work.
      ping6: Consolidate error path of niquery_option_subject_name_handler().
      ninfod: Node Information Query (RFC4620) daemon from USAGI Project.
      ninfod: struct in6_pktinfo requires -D_GNU_SOURCE.
      ninfod: Use %zu format string for size_t variable.
      ninfod: Add missing entry for ENABLE_SUPTYPES in config.h.in.
      ninfod: Support newer environment supporting RFC3542.
      ninfod: Fix format string for string returned from strerror(3).
      ninfod: Check return value of fscanf(3).
      ninfod: Fix off-by-one error to check possible programming error.
      ninfod: Add datarootdir.
      ninfod: Use __func__ instead of __FUNCTION__.
      ninfod: Introduce ARRAY_SIZE macro for counting number of elements in an array.
      ninfod: Delete ninfod.sh by make distclean, not by make clean.
      ping6: Do not try to use result buffer when dn_comp(3) failed.
      ping,ping6: ifdef guard for inline function for capability support and fix build with USE_CAP=no.
      makefile: Do not use "-llib" dependency.
      arping: build without sysfs support (USE_SYSFS=no).

Ángel González (1):
      iputils: Add capability dropping


[s20101006]

Chris Caputo (1):
      ping,ping6: avoid gethostbyaddr during ping flood.

Paul Martin (1):
      arping: Set correct broadcast address.

YOSHIFUJI Hideaki (4):
      tracepath: Fix some small typos in tracepath.sgml.
      ping: Fix resource consumption triggered by specially crafted ICMP Echo Reply (CVE-2010-2529)
      Makefile: migrate main machine from beatrice to takos.
      Makefile: Use newer git subcommand style instead of git-subcommand.


[s20100418]

YOSHIFUJI Hideaki (28):
      ping6: Use IPV6_TCLASS to set outgoing traffic class if available.
      ping: Make build_echo(), gather_statistics() more generic.
      ping6: Experimental support for Node Information Queries (RFC4620).
      ping: simplify usage hint.
      ping: Rename constant names
      Extend -N option for NI Query options.
      ping6: Make length-check qtype-specific.
      ping6: Remove too many spaces between names.
      ping6: ping6_niquery.h needs asm/byteorder.h.
      ping6: Support Qtypes for IPv6/IPv4 Addresses.
      ping6: Split pr_niquery_reply().
      ping6: Handle ICMPv6 code in NI Reply.
      ping6: Add subject-ipv6 and subject-ipv4 NI sub-option for subject address.
      ping6: Support subject name.
      ping6: Free old memory when reassign pointers.
      ping6: Always enable IPv6 Node Information Queries.
      makefile: Do not always link libresolv and libcrypto.
      ping,traceroute6,clockdiff: Enlarge hostname buffer.
      ping6: do not allow too large packet size by -s option.
      ping: needless space when printing usage.
      rdisc: Fix typo in error message.
      rdisc: Allow multiple addresses on one interface.
      arping: Support link-layer type with larger link-layer address.
      tracepath6: resolve target even if -n option is supplied.
      tracepath,tracepath6: sync tracepath and tracepath6.
      tracepath6: Make it more protocol independent.


[s20100214]

Jamal Hadi Salim (2):
      ping: ping by mark
      ping: ping by mark doc update

Jamie Le Tual (1):
      ping: set un.echo.id to network byte order

YOSHIFUJI Hideaki (11):
      [PING6,TRACEROUTE6]: Ignore error in setting IPV6_CHECKSUM socket option for ICMPv6 socket.
      [PING6]: Use if_nametoindex() to convert ifname to ifindex.
      [PING6]: Allow to specify source address with interface in a single -I option.
      ping6: Try using IPV6_PKTINFO sticky option to specify outgoing interface.
      rdisc: Use FOPEN_MAX if OPEN_MAX is undefined.
      ping6: Fix source routing with source interface set.
      ping,ping6: Don't print extra ', ' in finish().
      tracepath: Fix documentation typo.
      Use sysconf(_SC_OPEN_MAX) instead of OPEN_MAX.
      ping,ping6: Add -D option to print timestamp.


[s20071127]

John Heffner (6):
      [iputils] tracepath: Add length flag to set initial MTU.
      [iputils] tracepath: Add documentation for the -l flag.
      [iputils] tracepath: Use PMTUDISC_PROBE mode if it exists.
      [iputils] tracepath: Document -n flag.
      [iputils] tracepath: Fix asymm messages.
      [iputils] tracepath: Re-probe at same TTL after MTU reduction.

YOSHIFUJI Hideaki (8):
      [DOC]: Delete duplicated lines in RELNOTES.
      Fix white space errors.
      [CLOCKDIFF,PING,RDISC,TRACEROUTE6]: Support uClibc.
      [RARPD]: Fixed several signedness issues for char strings.
      [PING]: Use inet_pton() instead of sscan().
      [PING6]: Use IN6_IS_ADDR_xxx() macro.
      [MAKEFILE]: Change authorized host to push snapshots.
      [MAKEFILE]: Use git-archive instead of git-tar-tree.


[s20070202]

Mike Frysinger (2):
      Use socklen_t in all the right places.
      [IPG]: handle pktgen setup in newer kernels.

Mitsuru Chinen (2):
      [CLOCKDIFF]: Fix compilation errors about labels at end of compound statements.
      [PING6]: Use getaddrinfo() for the name resolution of intermediate nodes.

YOSHIFUJI Hideaki (9):
      [MAKEFILE] Remove unused -I../include
      [TRACEPATH] Print usage if we met incorrect option.
      [PING6]: Fix compilation error with glibc-2.4 and later.
      [PING6]: Use getaddrinfo() to allow scoped addresses
      [PING6]: Ensure not to reverse-lookup if target is numeric address.


[s20060512]

YOSHIFUJI Hideaki:
      [BUILD] Build with standard headers.
      [ARPING,PING6] Build fix for some old systems.


[s20060425]

YOSHIFUJI Hideaki:
      [TRACEROUTE6] Fix ICMPv6 type printing with -v option
      [TRACEROUTE6] Mark ICMPv6 messages as known
      [DOC] Maintainer / Contact change
      [PING6,TRACEPATH6,TRACEROUTE6] Define SOL_IPV6,SOL_ICMPV6 where needed
      [TRACEROUTE6] Fix source/destination address with -v option
      [PING6,TRACEPATH6,TRACEROUTE6] Use new RFC3542 advanced API if available
      [RDISC] Use proper type for is_directly_connected()
      [PING,PING6] Use proper type for printf()
      [TRACEROUTE6] Fix inet_pton() error handling
      [TRACEROUTE6] Use minimum format if 0 is specified for datalen
      [TRACEROUTE6] Optimize datalen sanity checking code
      [TRACEPATH6] Use getaddrinfo() to allow scoped addresses
      [RDISC] Use strerror(errno) instead of sys_errlist[errno]
      [PING,PING6] Avoid using __constant_htons() if it is really needed
      [TRACEPATH6] Fix format for subseconds
      [ARPING,CLOCKDIFF,PING,PING6,TRACEROUTE6] Check return value from setuid().
      [PING,PING6] ensure to initialize msg.
      [MAKEFILE] Make snapshot using git


[020927]
* arping.sgml, some options were forgotten.
* send seqno in network byte order. Me.
* Mads Martin Jrgensen <mmj@suse.de> Recursive citation:
"On request of Mads Martin Jrgensen <mmj@suse.de> I've added manpages
pregenerated from the Docbook sources. One could argue it is redundant
when the Docbook sources are also there, but the argument of not having
to install Docbook on a very small system to get the man pages was
convinving enough to me. To quote Mads Martin: "How would a system
be without a man page for ping?" 
  As a chilidish revenge from my side enjoy with cyrillic date in these
  man pages. :-)
* Ken Cox <jkc@redhat.com>. Bogus definition of SOCK_DRGAM&SOCK_STREAM on mips.
* Error returned from recvmsg() resulted in a bogus printout in traceroute6. Me.
* Use IPV6_CHECKSUM on icmp socket in traceroute6. Me.
* Noah L. Meyerhans <frodo@morgul.net> Fix to doc.
!* Noah L. Meyerhans <frodo@morgul.net> What is the problem with "long" triptime?
!  Reporter does not respond. _Malignantly_.
* Thomas 'Dent' Mirlacher <dent@cosy.sbg.ac.at> Ping did not exit sometimes!
* Add option -W to override default 10 second linger timeout. Me.
* Mads Martin Jrgensen <mmj@suse.de>: ping should not bind to autoselected
  source address, it used to work when routing changes. Return classic
  behaviour, option -B is added to enforce binding.
* Pekka Savola <pekkas@netcore.fi> Forgotten \n messing output of ping6.
* Noah L. Meyerhans <frodo@morgul.net> traceroute6 -q 1 did not work.
* Pekka Savola <pekkas@netcore.fi> various sizeof() cleanups in traceroute6.c
* "Dmitry V. Levin" <ldv@alt-linux.org> wrote:
  > ping (as well as other utilities) may open raw socket with descriptor <=2;
  > In case of suid-root, it can be used by malicious user to send data to
  > this raw socket.
  > 
  > Yes, modern glibc and some kernels have workaround for it, but
  > IMHO iputils shouldn't rely on this feature.
  Taken into account, but no changes made.
* "Tilman Heinrich" <tilHeinrich@web.de> said some scripts are broken
  when word "packet" disappeared from "100% packet loss". Despite of
  the inarguable fact that such scripts are truly mad and deserve breaking
  (sigh... exit codes are too smart concept for script writers, I guess),
  I have to recognize removing this word carrying zero information
  was not enough motivated. Returned.
* ping used to retry forever when seeing ENOBUFS/ENOMEM without explicitly
  given deadline. Being logically correct it is bad in practice f.e. when
  pinging buggy device which locked up with some packets in queue.
  So, retry for a finite time... let is be lingertime. Fair? Me.
* Two "messages" are sent to rpm maintainers to make their wrong patches
  failed.
* Fix from RH iputils-20001007-deadline.patch. It was lost in the latest
  rpms btw.
* Dax Kelson <dax@gurulabs.com>: added _unsupported_ option to comppile
  rdisc_srv.

[020124]
* Michal Kochanowicz <michal@michal.waw.pl> typos in tracepath.8
* Michael Wardle <michael.wardle@adacel.com>: undo silly change of ss000305
  (printing rtt in some funny units). Michael noticed that "sec" is not
  standard abbreviation for time units (bullshit, of course), but real concern
  is that it is more difficult to interpret with a neglibible improvement
  to appearance. So, do this as expected: in "ms".
* Documentation. Wow! I did it. man pages are disassembled to docbook,
  audited wrt real state, edited... and promised to be maintained
  in sync with the state of utilities.

[011202]
* Utz Bacher <utz.bacher@de.ibm.com> Bitops in ping6 were wrong
  on bigendian machines. Wow, luckily I forgot to acknowledge that patch
  of 010805 which has gotten rid of kernel bitops and did this so wrongly.
* Michael Bakunin <bakunin@maphiasoft.org> (:-))
  found mud in tftpd.c, it will crash when directory supplied in argument
  is longer ~512 symbols.
* Alexandr D. Kanevskiy <kad@blackcatlinux.com>: buffer overflow
  in clockdiff. Very stupid one, the overflowed buffer even was not used. :-)
* Alexandr D. Kanevskiy <kad@blackcatlinux.com>: shit! Code recognizing
  kernels with broken IP_RECVERR for raw sockets depended on race
  and accused even good kernel of being buggy. :-)

[011002]
* Stepan Koltsov <yozh@mx1.ru>, tracepath/tracepth6 segfaulted when
  used without address.
* Alexandr D. Kanevskiy <kad@blackcatlinux.com>: arping printed
  "permission denied" instead of showing help page to non-superuser.

[010824]
* Alexandr D. Kanevskiy <kad@blackcatlinux.com>: ping compiled
  for linux-2.4 forgot to send the second packet, when used with linux-2.2
* Chris Evans <chris@scary.beasts.org>: buffer overflow in traceroute6.
  datalen was messed: counting header in half of places.
  Funny, looking into LBL traceroute, it is even worse :-)
* Alexandr D. Kanevskiy <kad@blackcatlinux.com>: relayed patches
  by Solar_Diz. Only missing description of option -q is accepted.
* <ipatel@wilnetonline.net> ping6 printed wrong mtu.
* Alexandr D. Kanevskiy <kad@blackcatlinux.com>: -Werror is removed.
  Newer gcc are buggy and generates some wrong warnings about
  uninitalized variables, which are evidently initialized.

[010805]
* Some news from Pekka Savola <pekkas@netcore.fi> around setting tos bits.
* arping: broadcast-only mode by Ard van Breemen <ard@telegraafnet.nl>
* ping6/traceroute6: parse ICMP errors with extension headers (me)
  traceroute6 works with size > mtu now. Nice.
* ping: Erik Quanstrom <quanstro@clark.net>. Serious patch.
  ping interval timer was not very broken, but very unintelligible.
  Though I remade the code to use leaky bucket logic, which
  is the most transparent one. Anyway, contribution by Eric is
  the most important one since the previous release.
  Short theory of operation: option -i (interval) sets rate r=1/interval pps,
  option -l (preload) sets burst size of l packets. So, ping sends
  at most r*t+l packets for an arbitrary interval t.
  Default values: l=1 and for non-flood case: r=1pps, for flood r=infinity.
  Nice? Exact algorithm is:

  Let N(t) be l/r=l*i initially and N(t) grow continuously with time as:

	N(t+delta) = min{l*i, N(t) + delta}

  Packet can be transmitted only at the time t_* when 1/r=i <= N(t_*)
  and in this case N(t) jumps:

	N(t_* + 0) = N(t_* - 0) - i.

  When interval is zero, algo degenerates allowing to send any amount
  of messages. In this case we modify it using l as limit on amount
  of unanswered requests and waiting for 10msec, when something is not
  answered. Note that the last thing (10msec) is just to be compatible with
  BSD manual pages. BSD ping is simply not able to avoid delay technically,
  we are able now.

  In result we got some new facilities:
  * "-f -l 100" becomes very aggressive, in fact on good link
    it holds permanently 100 packets in flight, which is very different
    of earlier bevaviour (one packet in flight).
  * -f and -i are not incompatible more. In fact, "-f -i 1" is equivalent
    to plain ping, only output is different (dotted). Essentially,
    change of output format is the only effect. "ping -i 0" is flood
    printing output in normal format.

  Moved some parts of code to ping_common.c. Common part is not fully
  trivial now. :-)

* ping: Ian Lynagh <igloo@earth.li>, larger and dynamic dup detector.
  Also, Ian submitted two large patches, one fixing formatting, another
  doing something with signedness/longness. Not now...
  Later note: found not working. x + 7 / 8 :-). Sorry... dubious, withdrawn.
  size of table increased to maximal value instead (8K of memory,
  not a big deal).
* tftpd: an old misprint. left@sbor.spb.su (Igor A. Lefterov)
* clockdiff: do not fail, if reversed resolution failed.
  Tommy Lacroix <tommyl@zeroknowledge.com>
* ping: audible ping by Patrik Schilt <patrik@bnc.ch>
  Patrick's option renamed to -a to align to freebsd.
* ping: react to device queue overflows using IP_RECVERR. me.
* ping: option -S allows to change sndbuf 
* rarpd is moved from separate package here (people asked)
* ping6: kernel style bitops are not used more.
* Option -A to adapt to network rtt.
* Use BPF, when multiple pings are detected.

[001110]
* ping is able to select TOS. By Pekka Savola <pekkas@netcore.fi>
* tracepath* DNS names. By Pawel Krawczyk <kravietz@ceti.com.pl> and
  Arkadiusz Miskiewicz <misiek@pld.org.pl>
* ping6 is expected to be compiled with linux-2.2.

[001011]
* RH bugid#16677: segfault, when ping is used by root and size
  is large enough. Fix is to allow oversize by root (it is necessary
  to check kernel side), but clamp it at some safe value.

[001010]
* More bug fixes from Chris Evans <chris@ferret.lmh.ox.ac.uk>
  - do not trust h_length returned by system resolver.
    This value is meaningless in any case.
  - ping: buffer overflow in fill()!!! Disgraceful bug.

* ping: allow not-priviledged users to use broadcasts. It was paranoia.
  Multicasts were allowed. 8)
* ping: but force broadcasts&multicasts not to fragment. BSD does
  not allow to do this to anyone, we still allow this for superuser.
* Option -M to control path mtu discovery.

[001007]
* By Pekka Savola <pekkas@netcore.fi>
  - SIOCGSTAMP/SO_TIMESTAMP are sensitive to bug in kernel.
    When get_fast_time != gettimeofday (f.e. timestampless x86),
    returned stamp can be out of sync with gettimeofday.
    Workaround is not to use SIOCGSTAMP/SO_TIMESTAMP on such systems.
  - fixes in man pages
  - compiles under rh-7.0
* Chris Evans <chris@ferret.lmh.ox.ac.uk>
  - ping: possible buffer overflow in pr_addr().

[000928]
* Sorry. I have lost all the CVS with changes made since 000418.
  If someone sent me a patch after this date, please, resubmit.
  Restored from the last backup and mailboxes:

* ping*, SO_TIMESTAMP support.
* ping*, allow zero data length (reported by Damjan Lango <damjan.lango@hermes.si>)
* iputils man and help updates. Pekka Savola <Pekka.Savola@netcore.fi>
* ping.8, fix to ping man page. By Dadid Eisner <cradle@glue.umd.edu>
* ping prints addresses in numeric, if destination is numeric.
  Proposed by Tim Waugh <twaugh@meme.surrey.redhat.com>

New:
* ping: strncpy bug <typo@inferno.tusculum.edu>
* arping: improvements by Charles Howes <croot@micro-logistics.com>
	- a feature to arping: quit as soon as a reply is received.
	- default to eth0.
	- spelling

[000418]
* llsqrt() was buggy again!
       (noticed by Sam Farin <sfarin@ratol.fi>)

[000404]
* tracepath*, "NURDUnet-gw" bug workaround.
	(noticed by Vitaly E.Lavrov <lve@aanet.ru>)
* tracepath*, handle case of routers initializing rtt to 128.
	Vitaly E.Lavrov <lve@aanet.ru>
* shadowed icmp_sock in ping6. James Morris <jmorris@@intercode.com.au>
* Bug in ping -f, introduced with SO_RCVTIMEO. me.
* llsqrt() (ping, ping6) was wrong yet. me.

[000310]
* Print mean deviation of RTT in ping/ping6.
* Use SIOCGSTAMP in ping/ping6. Old behaviour calculating
  true user-to-user latency is restored with option -U.
  Reason for this stupid change is mainly political; people
  wonder why freebsd has twice less latency on loopback.
  If to follow along this line, we have to print rtt equal to 0. 8)
  [ LATER NOTE: actually, the change is _right_ without any doubts.
    Ping has another bug: nameresolver is blocking, so that
    when it dies not respond, ping shows evenly increasing by 1 sec
    RTT. It is very confusing (look through linux-kernel maillists
    to count number of people, who were cheated by misconfigured dns). ]
* Use SO_RCVTIMEO instead of poll() with ping/ping6 -f.
* Added -V option to arping/ping/ping6/traceroute6/rdisc
  to print snapshot number.

[000305]
* rdisc: ugly bug in getting interface list. me.
* ping/ping6: ping -i N, N>=3 did not work. Jeff Jonson <jbj@redhat.com>
* ping/ping6: microsecond rtt measurements. me.

[000120]
* ping/ping6: non-zero exit code even without -w.

[991024]
* Option "-i" to ping/ping6 takes fractional time now, so that
  "ping -i 0.3 xxx" pings each 300 msec. The idea is by
  Marc Boucher <marc@mbsi.ca>
* alpha/glibc-2.1 alignment problems in ping are fixed (struct timeval
  was wrongly aligned).

[990915]
* ping/ping6 worked only with kernels 2.3.15+ in 990824.

[990824]
* tftpd is added. It uses MSG_CONFIRM to confirm arp entries.
* ping6: workaround for bug in some egcs versions.

[990610]
* ping: output buffer was too small for full sized ping.
* ping: silly restriction on ping size is removed.

[990530]
* short man pages (Oleg M. Shumsky <oms@cp.tomsk.su>)
* ping6: get and print hop limit of reply packets (ME)
* rdisc deletes routes before exit with -TERM
* ping/ping6: option -w TIMEOUT 
* arping: exit with error, if received no replies in normal
  (not DAD and not unsilicited ARP) mode.



File: /SNAPSHOT.h
static char SNAPSHOT[] = "s20121221";


File: /tftp.h
/*
 * Copyright (c) 1983, 1993
 *	The Regents of the University of California.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 *	This product includes software developed by the University of
 *	California, Berkeley and its contributors.
 * 4. Neither the name of the University nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 *
 *	@(#)tftp.h	8.1 (Berkeley) 6/2/93
 */

#ifndef _ARPA_TFTP_H
#define _ARPA_TFTP_H
/*
 * Trivial File Transfer Protocol (IEN-133)
 */
#define	SEGSIZE		512		/* data segment size */

/*
 * Packet types.
 */
#define	RRQ	01			/* read request */
#define	WRQ	02			/* write request */
#define	DATA	03			/* data packet */
#define	ACK	04			/* acknowledgement */
#define	ERROR	05			/* error code */

struct	tftphdr {
	short	th_opcode;		/* packet type */
	union {
		short	tu_block;	/* block # */
		short	tu_code;	/* error code */
		char	tu_stuff[1];	/* request packet stuff */
	} th_u;
	char	th_data[1];		/* data or error string */
};

#define	th_block	th_u.tu_block
#define	th_code		th_u.tu_code
#define	th_stuff	th_u.tu_stuff
#define	th_msg		th_data

/*
 * Error codes.
 */
#define	EUNDEF		0		/* not defined */
#define	ENOTFOUND	1		/* file not found */
#define	EACCESS		2		/* access violation */
#define	ENOSPACE	3		/* disk full or allocation exceeded */
#define	EBADOP		4		/* illegal TFTP operation */
#define	EBADID		5		/* unknown transfer ID */
#define	EEXISTS		6		/* file already exists */
#define	ENOUSER		7		/* no such user */


extern int readit(FILE * file, struct tftphdr **dpp, int convert);
extern void read_ahead(FILE *file, int convert);
extern int writeit(FILE *file, struct tftphdr **dpp, int ct, int convert);
extern int write_behind(FILE *file, int convert);
extern int synchnet(int f);
extern struct tftphdr *w_init(void);
extern struct tftphdr *r_init(void);


#endif /* _ARPA_TFTP_H */


File: /tftpd.c
/*
 * Copyright (c) 1983 Regents of the University of California.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 *	This product includes software developed by the University of
 *	California, Berkeley and its contributors.
 * 4. Neither the name of the University nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#ifndef lint
char copyright[] =
"@(#) Copyright (c) 1983 Regents of the University of California.\n\
 All rights reserved.\n";
#endif /* not lint */

#ifndef lint
/*static char sccsid[] = "from: @(#)tftpd.c	5.13 (Berkeley) 2/26/91";*/
/*static char rcsid[] = "$Id: tftpd.c,v 1.3 1993/08/01 18:28:53 mycroft Exp $";*/
#endif /* not lint */

/*
 * Trivial file transfer protocol server.
 *
 * This version includes many modifications by Jim Guyton <guyton@rand-unix>
 */

#include <sys/types.h>
#include <sys/ioctl.h>
#include <sys/stat.h>
#include <unistd.h>
#include <signal.h>
#include <fcntl.h>

#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

#include <setjmp.h>
#include <syslog.h>
#include <stdio.h>
#include <errno.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

#include "tftp.h"

#ifndef MSG_CONFIRM
#define MSG_CONFIRM 0
#warning Please, upgrade kernel, otherwise this tftpd has no advantages.
#endif

#define	TIMEOUT		5

int	peer;
int	rexmtval = TIMEOUT;
int	maxtimeout = 5*TIMEOUT;

#define	PKTSIZE	SEGSIZE+4
char	buf[PKTSIZE];
char	ackbuf[PKTSIZE];
union {
	struct	sockaddr     sa;
	struct	sockaddr_in  sin;
	struct	sockaddr_in6 sin6;
} from;
socklen_t	fromlen;

#define MAXARG	1
char	*dirs[MAXARG+1];

void tftp(struct tftphdr *tp, int size) __attribute__((noreturn));
void nak(int error);
int validate_access(char *filename, int mode);

struct formats;

void sendfile(struct formats *pf);
void recvfile(struct formats *pf);


int main(int ac, char **av)
{
	register struct tftphdr *tp;
	register int n = 0;
	int on = 1;

	/* Sanity. If parent forgot to setuid() on us. */
	if (geteuid() == 0) {
		setgid(65534);
		setuid(65534);
	}

	ac--; av++;
	while (ac-- > 0 && n < MAXARG)
		dirs[n++] = *av++;

	openlog("tftpd", LOG_PID, LOG_DAEMON);
	if (ioctl(0, FIONBIO, &on) < 0) {
		syslog(LOG_ERR, "ioctl(FIONBIO): %m\n");
		exit(1);
	}
	fromlen = sizeof (from);
	n = recvfrom(0, buf, sizeof (buf), 0,
	    (struct sockaddr *)&from, &fromlen);
	if (n < 0) {
		if (errno != EAGAIN)
			syslog(LOG_ERR, "recvfrom: %m\n");
		exit(1);
	}
	/*
	 * Now that we have read the message out of the UDP
	 * socket, we fork and exit.  Thus, inetd will go back
	 * to listening to the tftp port, and the next request
	 * to come in will start up a new instance of tftpd.
	 *
	 * We do this so that inetd can run tftpd in "wait" mode.
	 * The problem with tftpd running in "nowait" mode is that
	 * inetd may get one or more successful "selects" on the
	 * tftp port before we do our receive, so more than one
	 * instance of tftpd may be started up.  Worse, if tftpd
	 * break before doing the above "recvfrom", inetd would
	 * spawn endless instances, clogging the system.
	 */
	{
		int pid;
		int i;
		socklen_t j;

		for (i = 1; i < 20; i++) {
		    pid = fork();
		    if (pid < 0) {
				sleep(i);
				/*
				 * flush out to most recently sent request.
				 *
				 * This may drop some request, but those
				 * will be resent by the clients when
				 * they timeout.  The positive effect of
				 * this flush is to (try to) prevent more
				 * than one tftpd being started up to service
				 * a single request from a single client.
				 */
				j = sizeof from;
				i = recvfrom(0, buf, sizeof (buf), 0,
				    (struct sockaddr *)&from, &j);
				if (i > 0) {
					n = i;
					fromlen = j;
				}
		    } else {
				break;
		    }
		}
		if (pid < 0) {
			syslog(LOG_ERR, "fork: %m\n");
			exit(1);
		} else if (pid != 0) {
			exit(0);
		}
	}
	alarm(0);
	close(0);
	close(1);
	peer = socket(from.sa.sa_family, SOCK_DGRAM, 0);
	if (peer < 0) {
		syslog(LOG_ERR, "socket: %m\n");
		exit(1);
	}
	if (connect(peer, (struct sockaddr *)&from, sizeof(from)) < 0) {
		syslog(LOG_ERR, "connect: %m\n");
		exit(1);
	}
	tp = (struct tftphdr *)buf;
	tp->th_opcode = ntohs(tp->th_opcode);
	if (tp->th_opcode == RRQ || tp->th_opcode == WRQ)
		tftp(tp, n);
	exit(1);
}

struct formats {
	char	*f_mode;
	int	(*f_validate)(char *filename, int mode);
	void	(*f_send)(struct formats*);
	void	(*f_recv)(struct formats*);
	int	f_convert;
} formats[] = {
	{ "netascii",	validate_access,	sendfile,	recvfile, 1 },
	{ "octet",	validate_access,	sendfile,	recvfile, 0 },
#ifdef notdef
	{ "mail",	validate_user,		sendmail,	recvmail, 1 },
#endif
	{ 0 }
};

/*
 * Handle initial connection protocol.
 */
void tftp(struct tftphdr *tp, int size)
{
	register char *cp;
	int first = 1, ecode;
	register struct formats *pf;
	char *filename, *mode = NULL;

	filename = cp = tp->th_stuff;
again:
	while (cp < buf + size) {
		if (*cp == '\0')
			break;
		cp++;
	}
	if (*cp != '\0') {
		nak(EBADOP);
		exit(1);
	}
	if (first) {
		mode = ++cp;
		first = 0;
		goto again;
	}
	for (cp = mode; *cp; cp++)
		if (isupper(*cp))
			*cp = tolower(*cp);
	for (pf = formats; pf->f_mode; pf++)
		if (strcmp(pf->f_mode, mode) == 0)
			break;
	if (pf->f_mode == 0) {
		nak(EBADOP);
		exit(1);
	}
	ecode = (*pf->f_validate)(filename, tp->th_opcode);
	if (ecode) {
		nak(ecode);
		exit(1);
	}
	if (tp->th_opcode == WRQ)
		(*pf->f_recv)(pf);
	else
		(*pf->f_send)(pf);
	exit(0);
}


FILE *file;

/*
 * Validate file access.  Since we
 * have no uid or gid, for now require
 * file to exist and be publicly
 * readable/writable.
 * If we were invoked with arguments
 * from inetd then the file must also be
 * in one of the given directory prefixes.
 * Note also, full path name must be
 * given as we have no login directory.
 */
int validate_access(char *filename, int mode)
{
	struct stat stbuf;
	int    fd;
	char  *cp;
	char   fnamebuf[1024+512];

	for (cp = filename; *cp; cp++) {
		if(*cp == '.' && (cp == filename || strncmp(cp-1, "/../", 4) == 0)) {
			syslog(LOG_ERR, "bad path %s", filename);
			return(EACCESS);
		}
	}

	if (*filename == '/')
		filename++;

	if (!*dirs) {
		syslog(LOG_ERR, "no dirs");
		return EACCESS;
	}
	snprintf(fnamebuf, sizeof(fnamebuf)-1, "%s/%s", *dirs, filename);
	filename = fnamebuf;

	if (stat(filename, &stbuf) < 0) {
		syslog(LOG_ERR, "stat %s : %m", filename);
		return (errno == ENOENT ? ENOTFOUND : EACCESS);
	}
	if (mode == RRQ) {
		if ((stbuf.st_mode&(S_IREAD >> 6)) == 0) {
			syslog(LOG_ERR, "not readable %s", filename);
			return (EACCESS);
		}
	} else {
		if ((stbuf.st_mode&(S_IWRITE >> 6)) == 0) {
			syslog(LOG_ERR, "not writable %s", filename);
			return (EACCESS);
		}
	}
	fd = open(filename, mode == RRQ ? 0 : 1);
	if (fd < 0) {
		syslog(LOG_ERR, "cannot open %s: %m", filename);
		return (errno + 100);
	}
	file = fdopen(fd, (mode == RRQ)? "r":"w");
	if (file == NULL) {
		return errno+100;
	}
	return (0);
}

int	confirmed;
int	timeout;
jmp_buf	timeoutbuf;

void timer(int signo)
{
	confirmed = 0;
	timeout += rexmtval;
	if (timeout >= maxtimeout)
		exit(1);
	longjmp(timeoutbuf, 1);
}

/*
 * Send the requested file.
 */
void sendfile(struct formats *pf)
{
	struct tftphdr *dp;
	register struct tftphdr *ap;    /* ack packet */
	volatile int block = 1;
	int size, n;

	confirmed = 0;
	signal(SIGALRM, timer);
	dp = r_init();
	ap = (struct tftphdr *)ackbuf;
	do {
		size = readit(file, &dp, pf->f_convert);
		if (size < 0) {
			nak(errno + 100);
			goto abort;
		}
		dp->th_opcode = htons((u_short)DATA);
		dp->th_block = htons((u_short)block);
		timeout = 0;
		(void) setjmp(timeoutbuf);

send_data:
		if (send(peer, dp, size + 4, confirmed) != size + 4) {
			syslog(LOG_ERR, "tftpd: write: %m\n");
			goto abort;
		}
		confirmed = 0;
		read_ahead(file, pf->f_convert);
		for ( ; ; ) {
			alarm(rexmtval);        /* read the ack */
			n = recv(peer, ackbuf, sizeof (ackbuf), 0);
			alarm(0);
			if (n < 0) {
				syslog(LOG_ERR, "tftpd: read: %m\n");
				goto abort;
			}
			ap->th_opcode = ntohs((u_short)ap->th_opcode);
			ap->th_block = ntohs((u_short)ap->th_block);

			if (ap->th_opcode == ERROR)
				goto abort;

			if (ap->th_opcode == ACK) {
				if (ap->th_block == block) {
					confirmed = MSG_CONFIRM;
					break;
				}
				/* Re-synchronize with the other side */
				synchnet(peer);
				if (ap->th_block == (block -1)) {
					goto send_data;
				}
			}

		}
		block++;
	} while (size == SEGSIZE);
abort:
	(void) fclose(file);
}

void justquit(int signo)
{
	exit(0);
}


/*
 * Receive a file.
 */
void recvfile(struct formats *pf)
{
	struct tftphdr *dp;
	register struct tftphdr *ap;    /* ack buffer */
	volatile int block = 0, n, size;

	confirmed = 0;
	signal(SIGALRM, timer);
	dp = w_init();
	ap = (struct tftphdr *)ackbuf;
	do {
		timeout = 0;
		ap->th_opcode = htons((u_short)ACK);
		ap->th_block = htons((u_short)block);
		block++;
		(void) setjmp(timeoutbuf);
send_ack:
		if (send(peer, ackbuf, 4, confirmed) != 4) {
			syslog(LOG_ERR, "tftpd: write: %m\n");
			goto abort;
		}
		confirmed = 0;
		write_behind(file, pf->f_convert);
		for ( ; ; ) {
			alarm(rexmtval);
			n = recv(peer, dp, PKTSIZE, 0);
			alarm(0);
			if (n < 0) {            /* really? */
				syslog(LOG_ERR, "tftpd: read: %m\n");
				goto abort;
			}
			dp->th_opcode = ntohs((u_short)dp->th_opcode);
			dp->th_block = ntohs((u_short)dp->th_block);
			if (dp->th_opcode == ERROR)
				goto abort;
			if (dp->th_opcode == DATA) {
				if (dp->th_block == block) {
					confirmed = MSG_CONFIRM;
					break;   /* normal */
				}
				/* Re-synchronize with the other side */
				(void) synchnet(peer);
				if (dp->th_block == (block-1))
					goto send_ack;          /* rexmit */
			}
		}
		/*  size = write(file, dp->th_data, n - 4); */
		size = writeit(file, &dp, n - 4, pf->f_convert);
		if (size != (n-4)) {                    /* ahem */
			if (size < 0) nak(errno + 100);
			else nak(ENOSPACE);
			goto abort;
		}
	} while (size == SEGSIZE);
	write_behind(file, pf->f_convert);
	(void) fclose(file);            /* close data file */

	ap->th_opcode = htons((u_short)ACK);    /* send the "final" ack */
	ap->th_block = htons((u_short)(block));
	(void) send(peer, ackbuf, 4, confirmed);

	signal(SIGALRM, justquit);      /* just quit on timeout */
	alarm(rexmtval);
	n = recv(peer, buf, sizeof (buf), 0); /* normally times out and quits */
	alarm(0);
	if (n >= 4 &&                   /* if read some data */
	    dp->th_opcode == DATA &&    /* and got a data block */
	    block == dp->th_block) {	/* then my last ack was lost */
		(void) send(peer, ackbuf, 4, 0);     /* resend final ack */
	}
abort:
	return;
}

struct errmsg {
	int	e_code;
	char	*e_msg;
} errmsgs[] = {
	{ EUNDEF,	"Undefined error code" },
	{ ENOTFOUND,	"File not found" },
	{ EACCESS,	"Access violation" },
	{ ENOSPACE,	"Disk full or allocation exceeded" },
	{ EBADOP,	"Illegal TFTP operation" },
	{ EBADID,	"Unknown transfer ID" },
	{ EEXISTS,	"File already exists" },
	{ ENOUSER,	"No such user" },
	{ -1,		0 }
};

/*
 * Send a nak packet (error message).
 * Error code passed in is one of the
 * standard TFTP codes, or a UNIX errno
 * offset by 100.
 */
void nak(int error)
{
	register struct tftphdr *tp;
	int length;
	register struct errmsg *pe;

	tp = (struct tftphdr *)buf;
	tp->th_opcode = htons((u_short)ERROR);
	tp->th_code = htons((u_short)error);
	for (pe = errmsgs; pe->e_code >= 0; pe++)
		if (pe->e_code == error)
			break;
	if (pe->e_code < 0) {
		pe->e_msg = strerror(error - 100);
		tp->th_code = EUNDEF;   /* set 'undef' errorcode */
	}
	strcpy(tp->th_msg, pe->e_msg);
	length = strlen(pe->e_msg);
	tp->th_msg[length] = '\0';
	length += 5;
	if (send(peer, buf, length, 0) != length)
		syslog(LOG_ERR, "nak: %m\n");
}


File: /tftpsubs.c
/*
 * Copyright (c) 1983 Regents of the University of California.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 *	This product includes software developed by the University of
 *	California, Berkeley and its contributors.
 * 4. Neither the name of the University nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#ifndef lint
/*static char sccsid[] = "from: @(#)tftpsubs.c	5.6 (Berkeley) 2/28/91";*/
/* static char rcsid[] = "$Id: tftpsubs.c,v 1.2 1993/08/01 18:07:04 mycroft Exp $"; */
#endif /* not lint */

/* Simple minded read-ahead/write-behind subroutines for tftp user and
   server.  Written originally with multiple buffers in mind, but current
   implementation has two buffer logic wired in.

   Todo:  add some sort of final error check so when the write-buffer
   is finally flushed, the caller can detect if the disk filled up
   (or had an i/o error) and return a nak to the other side.

			Jim Guyton 10/85
 */

#include <sys/types.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <netinet/in.h>
#include <unistd.h>
#include <stdio.h>

#include "tftp.h"

#define PKTSIZE SEGSIZE+4       /* should be moved to tftp.h */

struct bf {
	int counter;            /* size of data in buffer, or flag */
	char buf[PKTSIZE];      /* room for data packet */
} bfs[2];

				/* Values for bf.counter  */
#define BF_ALLOC -3             /* alloc'd but not yet filled */
#define BF_FREE  -2             /* free */
/* [-1 .. SEGSIZE] = size of data in the data buffer */

static int nextone;     /* index of next buffer to use */
static int current;     /* index of buffer in use */

			/* control flags for crlf conversions */
int newline = 0;        /* fillbuf: in middle of newline expansion */
int prevchar = -1;      /* putbuf: previous char (cr check) */

struct tftphdr *rw_init(int);

struct tftphdr *w_init() { return rw_init(0); }         /* write-behind */
struct tftphdr *r_init() { return rw_init(1); }         /* read-ahead */

/* init for either read-ahead or write-behind */
/* x is zero for write-behind, one for read-head */
struct tftphdr *rw_init(int x)
{
	newline = 0;            /* init crlf flag */
	prevchar = -1;
	bfs[0].counter =  BF_ALLOC;     /* pass out the first buffer */
	current = 0;
	bfs[1].counter = BF_FREE;
	nextone = x;                    /* ahead or behind? */
	return (struct tftphdr *)bfs[0].buf;
}


/* Have emptied current buffer by sending to net and getting ack.
   Free it and return next buffer filled with data.
 */
int readit(FILE * file, struct tftphdr **dpp, int convert)
{
	struct bf *b;

	bfs[current].counter = BF_FREE; /* free old one */
	current = !current;             /* "incr" current */

	b = &bfs[current];              /* look at new buffer */
	if (b->counter == BF_FREE)      /* if it's empty */
		read_ahead(file, convert);      /* fill it */
#if 0
	assert(b->counter != BF_FREE);  /* check */
#endif
	*dpp = (struct tftphdr *)b->buf;        /* set caller's ptr */
	return b->counter;
}

/*
 * fill the input buffer, doing ascii conversions if requested
 * conversions are  lf -> cr,lf  and cr -> cr, nul
 */
void read_ahead(FILE *file, int convert)
{
	register int i;
	register char *p;
	register int c;
	struct bf *b;
	struct tftphdr *dp;

	b = &bfs[nextone];              /* look at "next" buffer */
	if (b->counter != BF_FREE)      /* nop if not free */
		return;
	nextone = !nextone;             /* "incr" next buffer ptr */

	dp = (struct tftphdr *)b->buf;

	if (convert == 0) {
		b->counter = read(fileno(file), dp->th_data, SEGSIZE);
		return;
	}

	p = dp->th_data;
	for (i = 0 ; i < SEGSIZE; i++) {
		if (newline) {
			if (prevchar == '\n')
				c = '\n';       /* lf to cr,lf */
			else    c = '\0';       /* cr to cr,nul */
			newline = 0;
		}
		else {
			c = getc(file);
			if (c == EOF) break;
			if (c == '\n' || c == '\r') {
				prevchar = c;
				c = '\r';
				newline = 1;
			}
		}
	       *p++ = c;
	}
	b->counter = (int)(p - dp->th_data);
}

/* Update count associated with the buffer, get new buffer
   from the queue.  Calls write_behind only if next buffer not
   available.
 */
int writeit(FILE *file, struct tftphdr **dpp, int ct, int convert)
{
	bfs[current].counter = ct;      /* set size of data to write */
	current = !current;             /* switch to other buffer */
	if (bfs[current].counter != BF_FREE)     /* if not free */
		write_behind(file, convert);     /* flush it */
	bfs[current].counter = BF_ALLOC;        /* mark as alloc'd */
	*dpp =  (struct tftphdr *)bfs[current].buf;
	return ct;                      /* this is a lie of course */
}

/*
 * Output a buffer to a file, converting from netascii if requested.
 * CR,NUL -> CR  and CR,LF => LF.
 * Note spec is undefined if we get CR as last byte of file or a
 * CR followed by anything else.  In this case we leave it alone.
 */
int write_behind(FILE *file, int convert)
{
	char *buf;
	int count;
	register int ct;
	register char *p;
	register int c;                 /* current character */
	struct bf *b;
	struct tftphdr *dp;

	b = &bfs[nextone];
	if (b->counter < -1)            /* anything to flush? */
		return 0;               /* just nop if nothing to do */

	count = b->counter;             /* remember byte count */
	b->counter = BF_FREE;           /* reset flag */
	dp = (struct tftphdr *)b->buf;
	nextone = !nextone;             /* incr for next time */
	buf = dp->th_data;

	if (count <= 0) return -1;      /* nak logic? */

	if (convert == 0)
		return write(fileno(file), buf, count);

	p = buf;
	ct = count;
	while (ct--) {                  /* loop over the buffer */
	    c = *p++;                   /* pick up a character */
	    if (prevchar == '\r') {     /* if prev char was cr */
		if (c == '\n')          /* if have cr,lf then just */
		   fseek(file, -1, 1);  /* smash lf on top of the cr */
		else
		   if (c == '\0')       /* if have cr,nul then */
			goto skipit;    /* just skip over the putc */
		/* else just fall through and allow it */
	    }
	    putc(c, file);
skipit:
	    prevchar = c;
	}
	return count;
}


/* When an error has occurred, it is possible that the two sides
 * are out of synch.  Ie: that what I think is the other side's
 * response to packet N is really their response to packet N-1.
 *
 * So, to try to prevent that, we flush all the input queued up
 * for us on the network connection on our host.
 *
 * We return the number of packets we flushed (mostly for reporting
 * when trace is active).
 */

int synchnet(int f)
{
	int j = 0;
	char dummy;

	while (1) {
		if (recv(f, &dummy, 1, MSG_DONTWAIT) < 0)
			break;
		j++;
	}
	return j;
}


File: /tracepath.c
/*
 * tracepath.c
 *
 *		This program is free software; you can redistribute it and/or
 *		modify it under the terms of the GNU General Public License
 *		as published by the Free Software Foundation; either version
 *		2 of the License, or (at your option) any later version.
 *
 * Authors:	Alexey Kuznetsov, <kuznet@ms2.inr.ac.ru>
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <linux/types.h>
#include <linux/errqueue.h>
#include <errno.h>
#include <string.h>
#include <netdb.h>
#include <netinet/in.h>
#include <resolv.h>
#include <sys/time.h>
#include <sys/uio.h>
#include <arpa/inet.h>
#ifdef USE_IDN
#include <idna.h>
#include <locale.h>
#endif

#ifndef IP_PMTUDISC_PROBE
#define IP_PMTUDISC_PROBE	3
#endif

struct hhistory
{
	int	hops;
	struct timeval sendtime;
};

struct hhistory his[64];
int hisptr;

struct sockaddr_in target;
__u16 base_port;

const int overhead = 28;
int mtu = 65535;
void *pktbuf;
int hops_to = -1;
int hops_from = -1;
int no_resolve = 0;
int show_both = 0;

#define HOST_COLUMN_SIZE	52

struct probehdr
{
	__u32 ttl;
	struct timeval tv;
};

void data_wait(int fd)
{
	fd_set fds;
	struct timeval tv;
	FD_ZERO(&fds);
	FD_SET(fd, &fds);
	tv.tv_sec = 1;
	tv.tv_usec = 0;
	select(fd+1, &fds, NULL, NULL, &tv);
}

void print_host(const char *a, const char *b, int both)
{
	int plen = 0;
	printf("%s", a);
	plen = strlen(a);
	if (both) {
		printf(" (%s)", b);
		plen += strlen(b) + 3;
	}
	if (plen >= HOST_COLUMN_SIZE)
		plen = HOST_COLUMN_SIZE - 1;
	printf("%*s", HOST_COLUMN_SIZE - plen, "");
}

int recverr(int fd, int ttl)
{
	int res;
	struct probehdr rcvbuf;
	char cbuf[512];
	struct iovec  iov;
	struct msghdr msg;
	struct cmsghdr *cmsg;
	struct sock_extended_err *e;
	struct sockaddr_in addr;
	struct timeval tv;
	struct timeval *rettv;
	int slot;
	int rethops;
	int sndhops;
	int progress = -1;
	int broken_router;

restart:
	memset(&rcvbuf, -1, sizeof(rcvbuf));
	iov.iov_base = &rcvbuf;
	iov.iov_len = sizeof(rcvbuf);
	msg.msg_name = (__u8*)&addr;
	msg.msg_namelen = sizeof(addr);
	msg.msg_iov = &iov;
	msg.msg_iovlen = 1;
	msg.msg_flags = 0;
	msg.msg_control = cbuf;
	msg.msg_controllen = sizeof(cbuf);

	gettimeofday(&tv, NULL);
	res = recvmsg(fd, &msg, MSG_ERRQUEUE);
	if (res < 0) {
		if (errno == EAGAIN)
			return progress;
		goto restart;
	}

	progress = mtu;

	rethops = -1;
	sndhops = -1;
	e = NULL;
	rettv = NULL;
	slot = ntohs(addr.sin_port) - base_port;
	if (slot>=0 && slot < 63 && his[slot].hops) {
		sndhops = his[slot].hops;
		rettv = &his[slot].sendtime;
		his[slot].hops = 0;
	}
	broken_router = 0;
	if (res == sizeof(rcvbuf)) {
		if (rcvbuf.ttl == 0 || rcvbuf.tv.tv_sec == 0) {
			broken_router = 1;
		} else {
			sndhops = rcvbuf.ttl;
			rettv = &rcvbuf.tv;
		}
	}

	for (cmsg = CMSG_FIRSTHDR(&msg); cmsg; cmsg = CMSG_NXTHDR(&msg, cmsg)) {
		if (cmsg->cmsg_level == SOL_IP) {
			if (cmsg->cmsg_type == IP_RECVERR) {
				e = (struct sock_extended_err *) CMSG_DATA(cmsg);
			} else if (cmsg->cmsg_type == IP_TTL) {
				memcpy(&rethops, CMSG_DATA(cmsg), sizeof(rethops));
			} else {
				printf("cmsg:%d\n ", cmsg->cmsg_type);
			}
		}
	}
	if (e == NULL) {
		printf("no info\n");
		return 0;
	}
	if (e->ee_origin == SO_EE_ORIGIN_LOCAL) {
		printf("%2d?: %*s ", ttl, -(HOST_COLUMN_SIZE - 1), "[LOCALHOST]");
	} else if (e->ee_origin == SO_EE_ORIGIN_ICMP) {
		char abuf[128];
		struct sockaddr_in *sin = (struct sockaddr_in*)(e+1);
		struct hostent *h = NULL;
		char *idn = NULL;

		inet_ntop(AF_INET, &sin->sin_addr, abuf, sizeof(abuf));

		if (sndhops>0)
			printf("%2d:  ", sndhops);
		else
			printf("%2d?: ", ttl);

		if (!no_resolve || show_both) {
			fflush(stdout);
			h = gethostbyaddr((char *) &sin->sin_addr, sizeof(sin->sin_addr), AF_INET);
		}

#ifdef USE_IDN
		if (h && idna_to_unicode_lzlz(h->h_name, &idn, 0) != IDNA_SUCCESS)
			idn = NULL;
#endif
		if (no_resolve)
			print_host(abuf, h ? (idn ? idn : h->h_name) : abuf, show_both);
		else
			print_host(h ? (idn ? idn : h->h_name) : abuf, abuf, show_both);

#ifdef USE_IDN
		free(idn);
#endif
	}

	if (rettv) {
		int diff = (tv.tv_sec-rettv->tv_sec)*1000000+(tv.tv_usec-rettv->tv_usec);
		printf("%3d.%03dms ", diff/1000, diff%1000);
		if (broken_router)
			printf("(This broken router returned corrupted payload) ");
	}

	switch (e->ee_errno) {
	case ETIMEDOUT:
		printf("\n");
		break;
	case EMSGSIZE:
		printf("pmtu %d\n", e->ee_info);
		mtu = e->ee_info;
		progress = mtu;
		break;
	case ECONNREFUSED:
		printf("reached\n");
		hops_to = sndhops<0 ? ttl : sndhops;
		hops_from = rethops;
		return 0;
	case EPROTO:
		printf("!P\n");
		return 0;
	case EHOSTUNREACH:
		if (e->ee_origin == SO_EE_ORIGIN_ICMP &&
		    e->ee_type == 11 &&
		    e->ee_code == 0) {
			if (rethops>=0) {
				if (rethops<=64)
					rethops = 65-rethops;
				else if (rethops<=128)
					rethops = 129-rethops;
				else
					rethops = 256-rethops;
				if (sndhops>=0 && rethops != sndhops)
					printf("asymm %2d ", rethops);
				else if (sndhops<0 && rethops != ttl)
					printf("asymm %2d ", rethops);
			}
			printf("\n");
			break;
		}
		printf("!H\n");
		return 0;
	case ENETUNREACH:
		printf("!N\n");
		return 0;
	case EACCES:
		printf("!A\n");
		return 0;
	default:
		printf("\n");
		errno = e->ee_errno;
		perror("NET ERROR");
		return 0;
	}
	goto restart;
}

int probe_ttl(int fd, int ttl)
{
	int i;
	struct probehdr *hdr = pktbuf;

	memset(pktbuf, 0, mtu);
restart:
	for (i=0; i<10; i++) {
		int res;

		hdr->ttl = ttl;
		target.sin_port = htons(base_port + hisptr);
		gettimeofday(&hdr->tv, NULL);
		his[hisptr].hops = ttl;
		his[hisptr].sendtime = hdr->tv;
		if (sendto(fd, pktbuf, mtu-overhead, 0, (struct sockaddr*)&target, sizeof(target)) > 0)
			break;
		res = recverr(fd, ttl);
		his[hisptr].hops = 0;
		if (res==0)
			return 0;
		if (res > 0)
			goto restart;
	}
	hisptr = (hisptr + 1)&63;

	if (i<10) {
		data_wait(fd);
		if (recv(fd, pktbuf, mtu, MSG_DONTWAIT) > 0) {
			printf("%2d?: reply received 8)\n", ttl);
			return 0;
		}
		return recverr(fd, ttl);
	}

	printf("%2d:  send failed\n", ttl);
	return 0;
}

static void usage(void) __attribute((noreturn));

static void usage(void)
{
	fprintf(stderr, "Usage: tracepath [-n] [-b] [-l <len>] [-p port] <destination>\n");
	exit(-1);
}

int
main(int argc, char **argv)
{
	struct hostent *he;
	int fd;
	int on;
	int ttl;
	char *p;
	int ch;
#ifdef USE_IDN
	int rc;
	setlocale(LC_ALL, "");
#endif

	while ((ch = getopt(argc, argv, "nbh?l:p:")) != EOF) {
		switch(ch) {
		case 'n':
			no_resolve = 1;
			break;
		case 'b':
			show_both = 1;
			break;
		case 'l':
			if ((mtu = atoi(optarg)) <= overhead) {
				fprintf(stderr, "Error: pktlen must be > %d and <= %d.\n",
					overhead, INT_MAX);
				exit(1);
			}
			break;
		case 'p':
			base_port = atoi(optarg);
			break;
		default:
			usage();
		}
	}

	argc -= optind;
	argv += optind;

	if (argc != 1)
		usage();

	fd = socket(AF_INET, SOCK_DGRAM, 0);
	if (fd < 0) {
		perror("socket");
		exit(1);
	}
	target.sin_family = AF_INET;

	/* Backward compatiblity */
	if (!base_port) {
		p = strchr(argv[0], '/');
		if (p) {
			*p = 0;
			base_port = atoi(p+1);
		} else
			base_port = 44444;
	}

	p = argv[0];
#ifdef USE_IDN
	rc = idna_to_ascii_lz(argv[0], &p, 0);
	if (rc != IDNA_SUCCESS) {
		fprintf(stderr, "IDNA encoding failed: %s\n", idna_strerror(rc));
		exit(2);
	}
#endif

	he = gethostbyname(p);
	if (he == NULL) {
		herror("gethostbyname");
		exit(1);
	}

#ifdef USE_IDN
	free(p);
#endif

	memcpy(&target.sin_addr, he->h_addr, 4);

	on = IP_PMTUDISC_PROBE;
	if (setsockopt(fd, SOL_IP, IP_MTU_DISCOVER, &on, sizeof(on)) &&
	    (on = IP_PMTUDISC_DO,
	     setsockopt(fd, SOL_IP, IP_MTU_DISCOVER, &on, sizeof(on)))) {
		perror("IP_MTU_DISCOVER");
		exit(1);
	}
	on = 1;
	if (setsockopt(fd, SOL_IP, IP_RECVERR, &on, sizeof(on))) {
		perror("IP_RECVERR");
		exit(1);
	}
	if (setsockopt(fd, SOL_IP, IP_RECVTTL, &on, sizeof(on))) {
		perror("IP_RECVTTL");
		exit(1);
	}

	pktbuf = malloc(mtu);
	if (!pktbuf) {
		perror("malloc");
		exit(1);
	}

	for (ttl=1; ttl<32; ttl++) {
		int res;
		int i;

		on = ttl;
		if (setsockopt(fd, SOL_IP, IP_TTL, &on, sizeof(on))) {
			perror("IP_TTL");
			exit(1);
		}

restart:
		for (i=0; i<3; i++) {
			int old_mtu;

			old_mtu = mtu;
			res = probe_ttl(fd, ttl);
			if (mtu != old_mtu)
				goto restart;
			if (res == 0)
				goto done;
			if (res > 0)
				break;
		}

		if (res < 0)
			printf("%2d:  no reply\n", ttl);
	}
	printf("     Too many hops: pmtu %d\n", mtu);
done:
	printf("     Resume: pmtu %d ", mtu);
	if (hops_to>=0)
		printf("hops %d ", hops_to);
	if (hops_from>=0)
		printf("back %d ", hops_from);
	printf("\n");
	exit(0);
}


File: /tracepath6.c
/*
 * tracepath6.c
 *
 *		This program is free software; you can redistribute it and/or
 *		modify it under the terms of the GNU General Public License
 *		as published by the Free Software Foundation; either version
 *		2 of the License, or (at your option) any later version.
 *
 * Authors:	Alexey Kuznetsov, <kuznet@ms2.inr.ac.ru>
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/icmp6.h>

#include <linux/types.h>
#include <linux/errqueue.h>
#include <errno.h>
#include <string.h>
#include <netdb.h>
#include <resolv.h>
#include <sys/time.h>
#include <sys/uio.h>
#include <arpa/inet.h>

#ifdef USE_IDN
#include <idna.h>
#include <locale.h>
#endif

#ifndef SOL_IPV6
#define SOL_IPV6 IPPROTO_IPV6
#endif

#ifndef IP_PMTUDISC_DO
#define IP_PMTUDISC_DO		3
#endif
#ifndef IPV6_PMTUDISC_DO
#define IPV6_PMTUDISC_DO	3
#endif

struct hhistory
{
	int	hops;
	struct timeval sendtime;
};

struct hhistory his[64];
int hisptr;

sa_family_t family = AF_INET6;
struct sockaddr_storage target;
socklen_t targetlen;
__u16 base_port;

int overhead;
int mtu;
void *pktbuf;
int hops_to = -1;
int hops_from = -1;
int no_resolve = 0;
int show_both = 0;
int mapped;

#define HOST_COLUMN_SIZE	52

struct probehdr
{
	__u32 ttl;
	struct timeval tv;
};

void data_wait(int fd)
{
	fd_set fds;
	struct timeval tv;
	FD_ZERO(&fds);
	FD_SET(fd, &fds);
	tv.tv_sec = 1;
	tv.tv_usec = 0;
	select(fd+1, &fds, NULL, NULL, &tv);
}

void print_host(const char *a, const char *b, int both)
{
	int plen = 0;
	printf("%s", a);
	plen = strlen(a);
	if (both) {
		printf(" (%s)", b);
		plen += strlen(b) + 3;
	}
	if (plen >= HOST_COLUMN_SIZE)
		plen = HOST_COLUMN_SIZE - 1;
	printf("%*s", HOST_COLUMN_SIZE - plen, "");
}

int recverr(int fd, int ttl)
{
	int res;
	struct probehdr rcvbuf;
	char cbuf[512];
	struct iovec  iov;
	struct msghdr msg;
	struct cmsghdr *cmsg;
	struct sock_extended_err *e;
	struct sockaddr_storage addr;
	struct timeval tv;
	struct timeval *rettv;
	int slot = 0;
	int rethops;
	int sndhops;
	int progress = -1;
	int broken_router;

restart:
	memset(&rcvbuf, -1, sizeof(rcvbuf));
	iov.iov_base = &rcvbuf;
	iov.iov_len = sizeof(rcvbuf);
	msg.msg_name = (caddr_t)&addr;
	msg.msg_namelen = sizeof(addr);
	msg.msg_iov = &iov;
	msg.msg_iovlen = 1;
	msg.msg_flags = 0;
	msg.msg_control = cbuf;
	msg.msg_controllen = sizeof(cbuf);

	gettimeofday(&tv, NULL);
	res = recvmsg(fd, &msg, MSG_ERRQUEUE);
	if (res < 0) {
		if (errno == EAGAIN)
			return progress;
		goto restart;
	}

	progress = mtu;

	rethops = -1;
	sndhops = -1;
	e = NULL;
	rettv = NULL;

	slot = -base_port;
	switch (family) {
	case AF_INET6:
		slot += ntohs(((struct sockaddr_in6 *)&addr)->sin6_port);
		break;
	case AF_INET:
		slot += ntohs(((struct sockaddr_in *)&addr)->sin_port);
		break;
	}

	if (slot >= 0 && slot < 63 && his[slot].hops) {
		sndhops = his[slot].hops;
		rettv = &his[slot].sendtime;
		his[slot].hops = 0;
	}
	broken_router = 0;
	if (res == sizeof(rcvbuf)) {
		if (rcvbuf.ttl == 0 || rcvbuf.tv.tv_sec == 0)
			broken_router = 1;
		else {
			sndhops = rcvbuf.ttl;
			rettv = &rcvbuf.tv;
		}
	}

	for (cmsg = CMSG_FIRSTHDR(&msg); cmsg; cmsg = CMSG_NXTHDR(&msg, cmsg)) {
		switch (cmsg->cmsg_level) {
		case SOL_IPV6:
			switch(cmsg->cmsg_type) {
			case IPV6_RECVERR:
				e = (struct sock_extended_err *)CMSG_DATA(cmsg);
				break;
			case IPV6_HOPLIMIT:
#ifdef IPV6_2292HOPLIMIT
			case IPV6_2292HOPLIMIT:
#endif
				memcpy(&rethops, CMSG_DATA(cmsg), sizeof(rethops));
				break;
			default:
				printf("cmsg6:%d\n ", cmsg->cmsg_type);
			}
			break;
		case SOL_IP:
			switch(cmsg->cmsg_type) {
			case IP_RECVERR:
				e = (struct sock_extended_err *)CMSG_DATA(cmsg);
				break;
			case IP_TTL:
				rethops = *(__u8*)CMSG_DATA(cmsg);
				break;
			default:
				printf("cmsg4:%d\n ", cmsg->cmsg_type);
			}
		}
	}
	if (e == NULL) {
		printf("no info\n");
		return 0;
	}
	if (e->ee_origin == SO_EE_ORIGIN_LOCAL)
		printf("%2d?: %-32s ", ttl, "[LOCALHOST]");
	else if (e->ee_origin == SO_EE_ORIGIN_ICMP6 ||
		 e->ee_origin == SO_EE_ORIGIN_ICMP) {
		char abuf[NI_MAXHOST], hbuf[NI_MAXHOST];
		struct sockaddr *sa = (struct sockaddr *)(e + 1);
		socklen_t salen;

		if (sndhops>0)
			printf("%2d:  ", sndhops);
		else
			printf("%2d?: ", ttl);

		switch (sa->sa_family) {
		case AF_INET6:
			salen = sizeof(struct sockaddr_in6);
			break;
		case AF_INET:
			salen = sizeof(struct sockaddr_in);
			break;
		default:
			salen = 0;
		}

		if (no_resolve || show_both) {
			if (getnameinfo(sa, salen,
					abuf, sizeof(abuf), NULL, 0,
					NI_NUMERICHOST))
				strcpy(abuf, "???");
		} else
			abuf[0] = 0;

		if (!no_resolve || show_both) {
			fflush(stdout);
			if (getnameinfo(sa, salen,
					hbuf, sizeof(hbuf), NULL, 0,
					0
#ifdef USE_IDN
					| NI_IDN
#endif
				        ))
				strcpy(hbuf, "???");
		} else
			hbuf[0] = 0;

		if (no_resolve)
			print_host(abuf, hbuf, show_both);
		else
			print_host(hbuf, abuf, show_both);
	}

	if (rettv) {
		int diff = (tv.tv_sec-rettv->tv_sec)*1000000+(tv.tv_usec-rettv->tv_usec);
		printf("%3d.%03dms ", diff/1000, diff%1000);
		if (broken_router)
			printf("(This broken router returned corrupted payload) ");
	}

	switch (e->ee_errno) {
	case ETIMEDOUT:
		printf("\n");
		break;
	case EMSGSIZE:
		printf("pmtu %d\n", e->ee_info);
		mtu = e->ee_info;
		progress = mtu;
		break;
	case ECONNREFUSED:
		printf("reached\n");
		hops_to = sndhops<0 ? ttl : sndhops;
		hops_from = rethops;
		return 0;
	case EPROTO:
		printf("!P\n");
		return 0;
	case EHOSTUNREACH:
		if ((e->ee_origin == SO_EE_ORIGIN_ICMP &&
		     e->ee_type == 11 &&
		     e->ee_code == 0) ||
		    (e->ee_origin == SO_EE_ORIGIN_ICMP6 &&
		     e->ee_type == 3 &&
		     e->ee_code == 0)) {
			if (rethops>=0) {
				if (rethops<=64)
					rethops = 65-rethops;
				else if (rethops<=128)
					rethops = 129-rethops;
				else
					rethops = 256-rethops;
				if (sndhops>=0 && rethops != sndhops)
					printf("asymm %2d ", rethops);
				else if (sndhops<0 && rethops != ttl)
					printf("asymm %2d ", rethops);
			}
			printf("\n");
			break;
		}
		printf("!H\n");
		return 0;
	case ENETUNREACH:
		printf("!N\n");
		return 0;
	case EACCES:
		printf("!A\n");
		return 0;
	default:
		printf("\n");
		errno = e->ee_errno;
		perror("NET ERROR");
		return 0;
	}
	goto restart;
}

int probe_ttl(int fd, int ttl)
{
	int i;
	struct probehdr *hdr = pktbuf;

	memset(pktbuf, 0, mtu);
restart:

	for (i=0; i<10; i++) {
		int res;

		hdr->ttl = ttl;
		switch (family) {
		case AF_INET6:
			((struct sockaddr_in6 *)&target)->sin6_port = htons(base_port + hisptr);
			break;
		case AF_INET:
			((struct sockaddr_in *)&target)->sin_port = htons(base_port + hisptr);
			break;
		}
		gettimeofday(&hdr->tv, NULL);
		his[hisptr].hops = ttl;
		his[hisptr].sendtime = hdr->tv;
		if (sendto(fd, pktbuf, mtu-overhead, 0, (struct sockaddr *)&target, targetlen) > 0)
			break;
		res = recverr(fd, ttl);
		his[hisptr].hops = 0;
		if (res==0)
			return 0;
		if (res > 0)
			goto restart;
	}
	hisptr = (hisptr + 1) & 63;

	if (i<10) {
		data_wait(fd);
		if (recv(fd, pktbuf, mtu, MSG_DONTWAIT) > 0) {
			printf("%2d?: reply received 8)\n", ttl);
			return 0;
		}
		return recverr(fd, ttl);
	}

	printf("%2d:  send failed\n", ttl);
	return 0;
}

static void usage(void) __attribute((noreturn));

static void usage(void)
{
	fprintf(stderr, "Usage: tracepath6 [-n] [-b] [-l <len>] [-p port] <destination>\n");
	exit(-1);
}


int main(int argc, char **argv)
{
	int fd;
	int on;
	int ttl;
	char *p;
	struct addrinfo hints, *ai, *ai0;
	int ch;
	int gai;
	char pbuf[NI_MAXSERV];

#ifdef USE_IDN
	setlocale(LC_ALL, "");
#endif

	while ((ch = getopt(argc, argv, "nbh?l:p:")) != EOF) {
		switch(ch) {
		case 'n':
			no_resolve = 1;
			break;
		case 'b':
			show_both = 1;
			break;
		case 'l':
			mtu = atoi(optarg);
			break;
		case 'p':
			base_port = atoi(optarg);
			break;
		default:
			usage();
		}
	}

	argc -= optind;
	argv += optind;

	if (argc != 1)
		usage();

	/* Backward compatiblity */
	if (!base_port) {
		p = strchr(argv[0], '/');
		if (p) {
			*p = 0;
			base_port = (unsigned)atoi(p+1);
		} else {
			base_port = 44444;
		}
	}
	sprintf(pbuf, "%u", base_port);

	memset(&hints, 0, sizeof(hints));
	hints.ai_family = family;
	hints.ai_socktype = SOCK_DGRAM;
	hints.ai_protocol = IPPROTO_UDP;
#ifdef USE_IDN
	hints.ai_flags = AI_IDN;
#endif
	gai = getaddrinfo(argv[0], pbuf, &hints, &ai0);
	if (gai) {
		fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(gai));
		exit(1);
	}

	fd = -1;
	for (ai = ai0; ai; ai = ai->ai_next) {
		/* sanity check */
		if (family && ai->ai_family != family)
			continue;
		if (ai->ai_family != AF_INET6 &&
		    ai->ai_family != AF_INET)
			continue;
		family = ai->ai_family;
		fd = socket(ai->ai_family, ai->ai_socktype, ai->ai_protocol);
		if (fd < 0)
			continue;
		memcpy(&target, ai->ai_addr, sizeof(target));
		targetlen = ai->ai_addrlen;
		break;
	}
	if (fd < 0) {
		perror("socket/connect");
		exit(1);
	}
	freeaddrinfo(ai0);

	switch (family) {
	case AF_INET6:
		overhead = 48;
		if (!mtu)
			mtu = 128000;
		if (mtu <= overhead)
			goto pktlen_error;

		on = IPV6_PMTUDISC_DO;
		if (setsockopt(fd, SOL_IPV6, IPV6_MTU_DISCOVER, &on, sizeof(on)) &&
		    (on = IPV6_PMTUDISC_DO,
		     setsockopt(fd, SOL_IPV6, IPV6_MTU_DISCOVER, &on, sizeof(on)))) {
			perror("IPV6_MTU_DISCOVER");
			exit(1);
		}
		on = 1;
		if (setsockopt(fd, SOL_IPV6, IPV6_RECVERR, &on, sizeof(on))) {
			perror("IPV6_RECVERR");
			exit(1);
		}
		if (
#ifdef IPV6_RECVHOPLIMIT
		    setsockopt(fd, SOL_IPV6, IPV6_HOPLIMIT, &on, sizeof(on)) &&
		    setsockopt(fd, SOL_IPV6, IPV6_2292HOPLIMIT, &on, sizeof(on))
#else
		    setsockopt(fd, SOL_IPV6, IPV6_HOPLIMIT, &on, sizeof(on))
#endif
		    ) {
			perror("IPV6_HOPLIMIT");
			exit(1);
		}
		if (!IN6_IS_ADDR_V4MAPPED(&(((struct sockaddr_in6 *)&target)->sin6_addr)))
			break;
		mapped = 1;
		/*FALLTHROUGH*/
	case AF_INET:
		overhead = 28;
		if (!mtu)
			mtu = 65535;
		if (mtu <= overhead)
			goto pktlen_error;

		on = IP_PMTUDISC_DO;
		if (setsockopt(fd, SOL_IP, IP_MTU_DISCOVER, &on, sizeof(on))) {
			perror("IP_MTU_DISCOVER");
			exit(1);
		}
		on = 1;
		if (setsockopt(fd, SOL_IP, IP_RECVERR, &on, sizeof(on))) {
			perror("IP_RECVERR");
			exit(1);
		}
		if (setsockopt(fd, SOL_IP, IP_RECVTTL, &on, sizeof(on))) {
			perror("IP_RECVTTL");
			exit(1);
		}
	}

	pktbuf = malloc(mtu);
	if (!pktbuf) {
		perror("malloc");
		exit(1);
	}

	for (ttl=1; ttl<32; ttl++) {
		int res;
		int i;

		on = ttl;
		switch (family) {
		case AF_INET6:
			if (setsockopt(fd, SOL_IPV6, IPV6_UNICAST_HOPS, &on, sizeof(on))) {
				perror("IPV6_UNICAST_HOPS");
				exit(1);
			}
			if (!mapped)
				break;
			/*FALLTHROUGH*/
		case AF_INET:
			if (setsockopt(fd, SOL_IP, IP_TTL, &on, sizeof(on))) {
				perror("IP_TTL");
				exit(1);
			}
		}

restart:
		for (i=0; i<3; i++) {
			int old_mtu;

			old_mtu = mtu;
			res = probe_ttl(fd, ttl);
			if (mtu != old_mtu)
				goto restart;
			if (res == 0)
				goto done;
			if (res > 0)
				break;
		}

		if (res < 0)
			printf("%2d:  no reply\n", ttl);
	}
	printf("     Too many hops: pmtu %d\n", mtu);

done:
	printf("     Resume: pmtu %d ", mtu);
	if (hops_to>=0)
		printf("hops %d ", hops_to);
	if (hops_from>=0)
		printf("back %d ", hops_from);
	printf("\n");
	exit(0);

pktlen_error:
	fprintf(stderr, "Error: pktlen must be > %d and <= %d\n",
		overhead, INT_MAX);
	exit(1);
}


File: /traceroute6.c
/*
 *      Modified for NRL 4.4BSD IPv6 release.
 *      07/31/96 bgp
 *
 *      Search for "#ifdef NRL" to find the changes.
 */

/*
 *	Modified for Linux IPv6 by Pedro Roque <roque@di.fc.ul.pt>
 *	31/07/1996
 *
 *	As ICMP error messages for IPv6 now include more than 8 bytes
 *	UDP datagrams are now sent via an UDP socket instead of magic
 *	RAW socket tricks.
 *
 *	Original copyright and comments left intact. They might not
 *	match the code anymore.
 */

/*-
 * Copyright (c) 1990, 1993
 *	The Regents of the University of California.  All rights reserved.
 *
 * This code is derived from software contributed to Berkeley by
 * Van Jacobson.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 *	This product includes software developed by the University of
 *	California, Berkeley and its contributors.
 * 4. Neither the name of the University nor the names of its contributors
 *    may be used to endorse or promote products derived from this software
 *    without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#ifndef lint
char copyright[] =
"@(#) Copyright (c) 1990, 1993\n\
	The Regents of the University of California.  All rights reserved.\n";
#endif /* not lint */

/*
 * traceroute host  - trace the route ip packets follow going to "host".
 *
 * Attempt to trace the route an ip packet would follow to some
 * internet host.  We find out intermediate hops by launching probe
 * packets with a small ttl (time to live) then listening for an
 * icmp "time exceeded" reply from a gateway.  We start our probes
 * with a ttl of one and increase by one until we get an icmp "port
 * unreachable" (which means we got to "host") or hit a max (which
 * defaults to 30 hops & can be changed with the -m flag).  Three
 * probes (change with -q flag) are sent at each ttl setting and a
 * line is printed showing the ttl, address of the gateway and
 * round trip time of each probe.  If the probe answers come from
 * different gateways, the address of each responding system will
 * be printed.  If there is no response within a 5 sec. timeout
 * interval (changed with the -w flag), a "*" is printed for that
 * probe.
 *
 * Probe packets are UDP format.  We don't want the destination
 * host to process them so the destination port is set to an
 * unlikely value (if some clod on the destination is using that
 * value, it can be changed with the -p flag).
 *
 * A sample use might be:
 *
 *     [yak 71]% traceroute nis.nsf.net.
 *     traceroute to nis.nsf.net (35.1.1.48), 30 hops max, 56 byte packet
 *      1  helios.ee.lbl.gov (128.3.112.1)  19 ms  19 ms  0 ms
 *      2  lilac-dmc.Berkeley.EDU (128.32.216.1)  39 ms  39 ms  19 ms
 *      3  lilac-dmc.Berkeley.EDU (128.32.216.1)  39 ms  39 ms  19 ms
 *      4  ccngw-ner-cc.Berkeley.EDU (128.32.136.23)  39 ms  40 ms  39 ms
 *      5  ccn-nerif22.Berkeley.EDU (128.32.168.22)  39 ms  39 ms  39 ms
 *      6  128.32.197.4 (128.32.197.4)  40 ms  59 ms  59 ms
 *      7  131.119.2.5 (131.119.2.5)  59 ms  59 ms  59 ms
 *      8  129.140.70.13 (129.140.70.13)  99 ms  99 ms  80 ms
 *      9  129.140.71.6 (129.140.71.6)  139 ms  239 ms  319 ms
 *     10  129.140.81.7 (129.140.81.7)  220 ms  199 ms  199 ms
 *     11  nic.merit.edu (35.1.1.48)  239 ms  239 ms  239 ms
 *
 * Note that lines 2 & 3 are the same.  This is due to a buggy
 * kernel on the 2nd hop system -- lbl-csam.arpa -- that forwards
 * packets with a zero ttl.
 *
 * A more interesting example is:
 *
 *     [yak 72]% traceroute allspice.lcs.mit.edu.
 *     traceroute to allspice.lcs.mit.edu (18.26.0.115), 30 hops max
 *      1  helios.ee.lbl.gov (128.3.112.1)  0 ms  0 ms  0 ms
 *      2  lilac-dmc.Berkeley.EDU (128.32.216.1)  19 ms  19 ms  19 ms
 *      3  lilac-dmc.Berkeley.EDU (128.32.216.1)  39 ms  19 ms  19 ms
 *      4  ccngw-ner-cc.Berkeley.EDU (128.32.136.23)  19 ms  39 ms  39 ms
 *      5  ccn-nerif22.Berkeley.EDU (128.32.168.22)  20 ms  39 ms  39 ms
 *      6  128.32.197.4 (128.32.197.4)  59 ms  119 ms  39 ms
 *      7  131.119.2.5 (131.119.2.5)  59 ms  59 ms  39 ms
 *      8  129.140.70.13 (129.140.70.13)  80 ms  79 ms  99 ms
 *      9  129.140.71.6 (129.140.71.6)  139 ms  139 ms  159 ms
 *     10  129.140.81.7 (129.140.81.7)  199 ms  180 ms  300 ms
 *     11  129.140.72.17 (129.140.72.17)  300 ms  239 ms  239 ms
 *     12  * * *
 *     13  128.121.54.72 (128.121.54.72)  259 ms  499 ms  279 ms
 *     14  * * *
 *     15  * * *
 *     16  * * *
 *     17  * * *
 *     18  ALLSPICE.LCS.MIT.EDU (18.26.0.115)  339 ms  279 ms  279 ms
 *
 * (I start to see why I'm having so much trouble with mail to
 * MIT.)  Note that the gateways 12, 14, 15, 16 & 17 hops away
 * either don't send ICMP "time exceeded" messages or send them
 * with a ttl too small to reach us.  14 - 17 are running the
 * MIT C Gateway code that doesn't send "time exceeded"s.  God
 * only knows what's going on with 12.
 *
 * The silent gateway 12 in the above may be the result of a bug in
 * the 4.[23]BSD network code (and its derivatives):  4.x (x <= 3)
 * sends an unreachable message using whatever ttl remains in the
 * original datagram.  Since, for gateways, the remaining ttl is
 * zero, the icmp "time exceeded" is guaranteed to not make it back
 * to us.  The behavior of this bug is slightly more interesting
 * when it appears on the destination system:
 *
 *      1  helios.ee.lbl.gov (128.3.112.1)  0 ms  0 ms  0 ms
 *      2  lilac-dmc.Berkeley.EDU (128.32.216.1)  39 ms  19 ms  39 ms
 *      3  lilac-dmc.Berkeley.EDU (128.32.216.1)  19 ms  39 ms  19 ms
 *      4  ccngw-ner-cc.Berkeley.EDU (128.32.136.23)  39 ms  40 ms  19 ms
 *      5  ccn-nerif35.Berkeley.EDU (128.32.168.35)  39 ms  39 ms  39 ms
 *      6  csgw.Berkeley.EDU (128.32.133.254)  39 ms  59 ms  39 ms
 *      7  * * *
 *      8  * * *
 *      9  * * *
 *     10  * * *
 *     11  * * *
 *     12  * * *
 *     13  rip.Berkeley.EDU (128.32.131.22)  59 ms !  39 ms !  39 ms !
 *
 * Notice that there are 12 "gateways" (13 is the final
 * destination) and exactly the last half of them are "missing".
 * What's really happening is that rip (a Sun-3 running Sun OS3.5)
 * is using the ttl from our arriving datagram as the ttl in its
 * icmp reply.  So, the reply will time out on the return path
 * (with no notice sent to anyone since icmp's aren't sent for
 * icmp's) until we probe with a ttl that's at least twice the path
 * length.  I.e., rip is really only 7 hops away.  A reply that
 * returns with a ttl of 1 is a clue this problem exists.
 * Traceroute prints a "!" after the time if the ttl is <= 1.
 * Since vendors ship a lot of obsolete (DEC's Ultrix, Sun 3.x) or
 * non-standard (HPUX) software, expect to see this problem
 * frequently and/or take care picking the target host of your
 * probes.
 *
 * Other possible annotations after the time are !H, !N, !P (got a host,
 * network or protocol unreachable, respectively), !S or !F (source
 * route failed or fragmentation needed -- neither of these should
 * ever occur and the associated gateway is busted if you see one).  If
 * almost all the probes result in some kind of unreachable, traceroute
 * will give up and exit.
 *
 * Notes
 * -----
 * This program must be run by root or be setuid.  (I suggest that
 * you *don't* make it setuid -- casual use could result in a lot
 * of unnecessary traffic on our poor, congested nets.)
 *
 * This program requires a kernel mod that does not appear in any
 * system available from Berkeley:  A raw ip socket using proto
 * IPPROTO_RAW must interpret the data sent as an ip datagram (as
 * opposed to data to be wrapped in a ip datagram).  See the README
 * file that came with the source to this program for a description
 * of the mods I made to /sys/netinet/raw_ip.c.  Your mileage may
 * vary.  But, again, ANY 4.x (x < 4) BSD KERNEL WILL HAVE TO BE
 * MODIFIED TO RUN THIS PROGRAM.
 *
 * The udp port usage may appear bizarre (well, ok, it is bizarre).
 * The problem is that an icmp message only contains 8 bytes of
 * data from the original datagram.  8 bytes is the size of a udp
 * header so, if we want to associate replies with the original
 * datagram, the necessary information must be encoded into the
 * udp header (the ip id could be used but there's no way to
 * interlock with the kernel's assignment of ip id's and, anyway,
 * it would have taken a lot more kernel hacking to allow this
 * code to set the ip id).  So, to allow two or more users to
 * use traceroute simultaneously, we use this task's pid as the
 * source port (the high bit is set to move the port number out
 * of the "likely" range).  To keep track of which probe is being
 * replied to (so times and/or hop counts don't get confused by a
 * reply that was delayed in transit), we increment the destination
 * port number before each probe.
 *
 * Don't use this as a coding example.  I was trying to find a
 * routing problem and this code sort-of popped out after 48 hours
 * without sleep.  I was amazed it ever compiled, much less ran.
 *
 * I stole the idea for this program from Steve Deering.  Since
 * the first release, I've learned that had I attended the right
 * IETF working group meetings, I also could have stolen it from Guy
 * Almes or Matt Mathis.  I don't know (or care) who came up with
 * the idea first.  I envy the originators' perspicacity and I'm
 * glad they didn't keep the idea a secret.
 *
 * Tim Seaver, Ken Adelman and C. Philip Wood provided bug fixes and/or
 * enhancements to the original distribution.
 *
 * I've hacked up a round-trip-route version of this that works by
 * sending a loose-source-routed udp datagram through the destination
 * back to yourself.  Unfortunately, SO many gateways botch source
 * routing, the thing is almost worthless.  Maybe one day...
 *
 *  -- Van Jacobson (van@helios.ee.lbl.gov)
 *     Tue Dec 20 03:50:13 PST 1988
 */

#include <sys/param.h>
#include <sys/time.h>
#include <sys/socket.h>
#include <sys/file.h>
#include <sys/ioctl.h>
#include <net/if.h>

#if __linux__
#include <endian.h>
#endif
#include <netinet/in_systm.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>
#include <netinet/udp.h>

#include <netinet/ip6.h>
#include <netinet/icmp6.h>
#include <linux/types.h>
#ifdef CAPABILITIES
#include <sys/capability.h>
#endif

#ifdef USE_IDN
#include <idna.h>
#include <locale.h>
#endif

#include <arpa/inet.h>

#include <netdb.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "SNAPSHOT.h"

#ifndef SOL_IPV6
#define SOL_IPV6 IPPROTO_IPV6
#endif

#define	MAXPACKET	65535
#define MAX_HOSTNAMELEN	NI_MAXHOST

#ifndef FD_SET
#define NFDBITS         (8*sizeof(fd_set))
#define FD_SETSIZE      NFDBITS
#define FD_SET(n, p)    ((p)->fds_bits[(n)/NFDBITS] |= (1 << ((n) % NFDBITS)))
#define FD_CLR(n, p)    ((p)->fds_bits[(n)/NFDBITS] &= ~(1 << ((n) % NFDBITS)))
#define FD_ISSET(n, p)  ((p)->fds_bits[(n)/NFDBITS] & (1 << ((n) % NFDBITS)))
#define FD_ZERO(p)      memset((char *)(p), 0, sizeof(*(p)))
#endif

#define Fprintf (void)fprintf
#define Printf (void)printf

u_char	packet[512];		/* last inbound (icmp) packet */

int	wait_for_reply(int, struct sockaddr_in6 *, struct in6_addr *, int);
int	packet_ok(u_char *buf, int cc, struct sockaddr_in6 *from,
		  struct in6_addr *to, int seq, struct timeval *);
void	send_probe(int seq, int ttl);
double	deltaT (struct timeval *, struct timeval *);
void	print(unsigned char *buf, int cc, struct sockaddr_in6 *from);
void	tvsub (struct timeval *, struct timeval *);
void	usage(void);

int icmp_sock;			/* receive (icmp) socket file descriptor */
int sndsock;			/* send (udp) socket file descriptor */
struct timezone tz;		/* leftover */

struct sockaddr_in6 whereto;	/* Who to try to reach */

struct sockaddr_in6 saddr;
struct sockaddr_in6 firsthop;
char *source = NULL;
char *device = NULL;
char *hostname;

int nprobes = 3;
int max_ttl = 30;
pid_t ident;
u_short port = 32768+666;	/* start udp dest port # for probe packets */
int options;			/* socket options */
int verbose;
int waittime = 5;		/* time to wait for response (in seconds) */
int nflag;			/* print addresses numerically */


struct pkt_format
{
	__u32 ident;
	__u32 seq;
	struct timeval tv;
};

char *sendbuff;
int datalen = sizeof(struct pkt_format);



int main(int argc, char *argv[])
{
	char pa[MAX_HOSTNAMELEN];
	extern char *optarg;
	extern int optind;
	struct hostent *hp;
	struct sockaddr_in6 from, *to;
	int ch, i, on, probe, seq, tos, ttl;
	int socket_errno;

	icmp_sock = socket(AF_INET6, SOCK_RAW, IPPROTO_ICMPV6);
	socket_errno = errno;

	if (setuid(getuid())) {
		perror("traceroute6: setuid");
		exit(-1);
	}
#ifdef CAPABILITIES
	{
		cap_t caps = cap_init();
		if (cap_set_proc(caps)) {
			perror("traceroute6: cap_set_proc");
			exit(-1);
		}
		cap_free(caps);
	}
#endif

#ifdef USE_IDN
	setlocale(LC_ALL, "");
#endif

	on = 1;
	seq = tos = 0;
	to = (struct sockaddr_in6 *)&whereto;
	while ((ch = getopt(argc, argv, "dm:np:q:rs:t:w:vi:g:V")) != EOF) {
		switch(ch) {
		case 'd':
			options |= SO_DEBUG;
			break;
		case 'm':
			max_ttl = atoi(optarg);
			if (max_ttl <= 1) {
				Fprintf(stderr,
				    "traceroute: max ttl must be >1.\n");
				exit(1);
			}
			break;
		case 'n':
			nflag++;
			break;
		case 'p':
			port = atoi(optarg);
			if (port < 1) {
				Fprintf(stderr,
				    "traceroute: port must be >0.\n");
				exit(1);
			}
			break;
		case 'q':
			nprobes = atoi(optarg);
			if (nprobes < 1) {
				Fprintf(stderr,
				    "traceroute: nprobes must be >0.\n");
				exit(1);
			}
			break;
		case 'r':
			options |= SO_DONTROUTE;
			break;
		case 's':
			/*
			 * set the ip source address of the outbound
			 * probe (e.g., on a multi-homed host).
			 */
			source = optarg;
			break;
		case 'i':
			device = optarg;
			break;
		case 'g':
			Fprintf(stderr, "Sorry, rthdr is not yet supported\n");
			break;
		case 'v':
			verbose++;
			break;
		case 'w':
			waittime = atoi(optarg);
			if (waittime <= 1) {
				Fprintf(stderr,
				    "traceroute: wait must be >1 sec.\n");
				exit(1);
			}
			break;
		case 'V':
			printf("traceroute6 utility, iputils-%s\n", SNAPSHOT);
			exit(0);
		default:
			usage();
		}
	}
	argc -= optind;
	argv += optind;

	if (argc < 1)
		usage();

	setlinebuf (stdout);

	(void) memset((char *)&whereto, 0, sizeof(whereto));

	to->sin6_family = AF_INET6;
	to->sin6_port = htons(port);

	if (inet_pton(AF_INET6, *argv, &to->sin6_addr) > 0) {
		hostname = *argv;
	} else {
		char *idn = NULL;
#ifdef USE_IDN
		if (idna_to_ascii_lz(*argv, &idn, 0) != IDNA_SUCCESS)
			idn = NULL;
#endif
		hp = gethostbyname2(idn ? idn : *argv, AF_INET6);
		if (hp) {
			memmove((caddr_t)&to->sin6_addr, hp->h_addr, sizeof(to->sin6_addr));
			hostname = (char *)hp->h_name;
		} else {
			(void)fprintf(stderr,
			    "traceroute: unknown host %s\n", *argv);
			exit(1);
		}
	}
	firsthop = *to;
	if (*++argv) {
		datalen = atoi(*argv);
		/* Message for rpm maintainers: have _shame_. If you want
		 * to fix something send the patch to me for sanity checking.
		 * "datalen" patch is a shit. */
		if (datalen == 0)
			datalen = sizeof(struct pkt_format);
		else if (datalen < (int)sizeof(struct pkt_format) ||
			 datalen >= MAXPACKET) {
			Fprintf(stderr,
			    "traceroute: packet size must be %d <= s < %d.\n",
				(int)sizeof(struct pkt_format), MAXPACKET);
			exit(1);
		}
	}

	ident = getpid();

	sendbuff = malloc(datalen);
	if (sendbuff == NULL) {
		fprintf(stderr, "malloc failed\n");
		exit(1);
	}

	if (icmp_sock < 0) {
		errno = socket_errno;
		perror("traceroute6: icmp socket");
		exit(1);
	}

#ifdef IPV6_RECVPKTINFO
	setsockopt(icmp_sock, SOL_IPV6, IPV6_RECVPKTINFO, &on, sizeof(on));
	setsockopt(icmp_sock, SOL_IPV6, IPV6_2292PKTINFO, &on, sizeof(on));
#else
	setsockopt(icmp_sock, SOL_IPV6, IPV6_PKTINFO, &on, sizeof(on));
#endif

	if (options & SO_DEBUG)
		setsockopt(icmp_sock, SOL_SOCKET, SO_DEBUG,
			   (char *)&on, sizeof(on));
	if (options & SO_DONTROUTE)
		setsockopt(icmp_sock, SOL_SOCKET, SO_DONTROUTE,
			   (char *)&on, sizeof(on));

#ifdef __linux__
	on = 2;
	if (setsockopt(icmp_sock, SOL_RAW, IPV6_CHECKSUM, &on, sizeof(on)) < 0) {
		/* checksum should be enabled by default and setting this
		 * option might fail anyway.
		 */
		fprintf(stderr, "setsockopt(RAW_CHECKSUM) failed - try to continue.");
	}
#endif

	if ((sndsock = socket(AF_INET6, SOCK_DGRAM, 0)) < 0) {
		perror("traceroute: UDP socket");
		exit(5);
	}
#ifdef SO_SNDBUF
	if (setsockopt(sndsock, SOL_SOCKET, SO_SNDBUF, (char *)&datalen,
		       sizeof(datalen)) < 0) {
		perror("traceroute: SO_SNDBUF");
		exit(6);
	}
#endif /* SO_SNDBUF */

	if (options & SO_DEBUG)
		(void) setsockopt(sndsock, SOL_SOCKET, SO_DEBUG,
				  (char *)&on, sizeof(on));
	if (options & SO_DONTROUTE)
		(void) setsockopt(sndsock, SOL_SOCKET, SO_DONTROUTE,
				  (char *)&on, sizeof(on));

	if (source == NULL) {
		socklen_t alen;
		int probe_fd = socket(AF_INET6, SOCK_DGRAM, 0);

		if (probe_fd < 0) {
			perror("socket");
			exit(1);
		}
		if (device) {
			if (setsockopt(probe_fd, SOL_SOCKET, SO_BINDTODEVICE, device, strlen(device)+1) == -1)
				perror("WARNING: interface is ignored");
		}
		firsthop.sin6_port = htons(1025);
		if (connect(probe_fd, (struct sockaddr*)&firsthop, sizeof(firsthop)) == -1) {
			perror("connect");
			exit(1);
		}
		alen = sizeof(saddr);
		if (getsockname(probe_fd, (struct sockaddr*)&saddr, &alen) == -1) {
			perror("getsockname");
			exit(1);
		}
		saddr.sin6_port = 0;
		close(probe_fd);
	} else {
		(void) memset((char *)&saddr, 0, sizeof(saddr));
		saddr.sin6_family = AF_INET6;
		if (inet_pton(AF_INET6, source, &saddr.sin6_addr) <= 0)
		{
			Printf("traceroute: unknown addr %s\n", source);
			exit(1);
		}
	}

	if (bind(sndsock, (struct sockaddr *)&saddr, sizeof(saddr)) < 0) {
		perror ("traceroute: bind sending socket");
		exit (1);
	}
	if (bind(icmp_sock, (struct sockaddr *)&saddr, sizeof(saddr)) < 0) {
		perror ("traceroute: bind icmp6 socket");
		exit (1);
	}

	Fprintf(stderr, "traceroute to %s (%s)", hostname,
		inet_ntop(AF_INET6, &to->sin6_addr, pa, sizeof(pa)));

	Fprintf(stderr, " from %s",
		inet_ntop(AF_INET6, &saddr.sin6_addr, pa, sizeof(pa)));
	Fprintf(stderr, ", %d hops max, %d byte packets\n", max_ttl, datalen);
	(void) fflush(stderr);

	for (ttl = 1; ttl <= max_ttl; ++ttl) {
		struct in6_addr lastaddr = {{{0,}}};
		int got_there = 0;
		int unreachable = 0;

		Printf("%2d ", ttl);
		for (probe = 0; probe < nprobes; ++probe) {
			int cc, reset_timer;
			struct timeval t1, t2;
			struct timezone tz;
			struct in6_addr to;

			gettimeofday(&t1, &tz);
			send_probe(++seq, ttl);
			reset_timer = 1;

			while ((cc = wait_for_reply(icmp_sock, &from, &to, reset_timer)) != 0) {
				gettimeofday(&t2, &tz);
				if ((i = packet_ok(packet, cc, &from, &to, seq, &t1))) {
					reset_timer = 1;
					if (memcmp(&from.sin6_addr, &lastaddr, sizeof(from.sin6_addr))) {
						print(packet, cc, &from);
						memcpy(&lastaddr,
						       &from.sin6_addr,
						       sizeof(lastaddr));
					}
					Printf("  %g ms", deltaT(&t1, &t2));
					switch(i - 1) {
					case ICMP6_DST_UNREACH_NOPORT:
						++got_there;
						break;

					case ICMP6_DST_UNREACH_NOROUTE:
						++unreachable;
						Printf(" !N");
						break;
					case ICMP6_DST_UNREACH_ADDR:
						++unreachable;
						Printf(" !H");
						break;

					case ICMP6_DST_UNREACH_ADMIN:
						++unreachable;
						Printf(" !S");
						break;
					}
					break;
				} else
					reset_timer = 0;
			}
			if (cc <= 0)
				Printf(" *");
			(void) fflush(stdout);
		}
		putchar('\n');
		if (got_there ||
		    (unreachable > 0 && unreachable >= nprobes-1))
			exit(0);
	}

	return 0;
}

int
wait_for_reply(sock, from, to, reset_timer)
	int sock;
	struct sockaddr_in6 *from;
	struct in6_addr *to;
	int reset_timer;
{
	fd_set fds;
	static struct timeval wait;
	int cc = 0;
	char cbuf[512];

	FD_ZERO(&fds);
	FD_SET(sock, &fds);
	if (reset_timer) {
		/*
		 * traceroute could hang if someone else has a ping
		 * running and our ICMP reply gets dropped but we don't
		 * realize it because we keep waking up to handle those
		 * other ICMP packets that keep coming in.  To fix this,
		 * "reset_timer" will only be true if the last packet that
		 * came in was for us or if this is the first time we're
		 * waiting for a reply since sending out a probe.  Note
		 * that this takes advantage of the select() feature on
		 * Linux where the remaining timeout is written to the
		 * struct timeval area.
		 */
		wait.tv_sec = waittime;
		wait.tv_usec = 0;
	}

	if (select(sock+1, &fds, (fd_set *)0, (fd_set *)0, &wait) > 0) {
		struct iovec iov;
		struct msghdr msg;
		iov.iov_base = packet;
		iov.iov_len = sizeof(packet);
		msg.msg_name = (void *)from;
		msg.msg_namelen = sizeof(*from);
		msg.msg_iov = &iov;
		msg.msg_iovlen = 1;
		msg.msg_flags = 0;
		msg.msg_control = cbuf;
		msg.msg_controllen = sizeof(cbuf);

		cc = recvmsg(icmp_sock, &msg, 0);
		if (cc >= 0) {
			struct cmsghdr *cmsg;
			struct in6_pktinfo *ipi;

			for (cmsg = CMSG_FIRSTHDR(&msg);
			     cmsg;
			     cmsg = CMSG_NXTHDR(&msg, cmsg)) {
				if (cmsg->cmsg_level != SOL_IPV6)
					continue;
				switch (cmsg->cmsg_type) {
				case IPV6_PKTINFO:
#ifdef IPV6_2292PKTINFO
				case IPV6_2292PKTINFO:
#endif
					ipi = (struct in6_pktinfo *)CMSG_DATA(cmsg);
					memcpy(to, ipi, sizeof(*to));
				}
			}
		}
	}

	return(cc);
}


void send_probe(int seq, int ttl)
{
	struct pkt_format *pkt = (struct pkt_format *) sendbuff;
	int i;

	pkt->ident = htonl(ident);
	pkt->seq = htonl(seq);
	gettimeofday(&pkt->tv, &tz);

	i = setsockopt(sndsock, SOL_IPV6, IPV6_UNICAST_HOPS, &ttl, sizeof(ttl));
	if (i < 0)
	{
		perror("setsockopt");
		exit(1);
	}

	do {
		i = sendto(sndsock, sendbuff, datalen, 0,
			   (struct sockaddr *)&whereto, sizeof(whereto));
	} while (i<0 && errno == ECONNREFUSED);

	if (i < 0 || i != datalen)  {
		if (i<0)
			perror("sendto");
		Printf("traceroute: wrote %s %d chars, ret=%d\n", hostname,
			datalen, i);
		(void) fflush(stdout);
	}
}


double deltaT(struct timeval *t1p, struct timeval *t2p)
{
	register double dt;

	dt = (double)(t2p->tv_sec - t1p->tv_sec) * 1000.0 +
	     (double)(t2p->tv_usec - t1p->tv_usec) / 1000.0;
	return (dt);
}


/*
 * Convert an ICMP "type" field to a printable string.
 */
char * pr_type(unsigned char t)
{
	switch(t) {
	/* Unknown */
	case 0:
		return "Error";
	case 1:
		/* ICMP6_DST_UNREACH: */
		return "Destination Unreachable";
	case 2:
		/* ICMP6_PACKET_TOO_BIG: */
		return "Packet Too Big";
	case 3:
		/* ICMP6_TIME_EXCEEDED */
		return "Time Exceeded in Transit";
	case 4:
		/* ICMP6_PARAM_PROB */
		return "Parameter Problem";
	case 128:
		/* ICMP6_ECHO_REQUEST */
		return "Echo Request";
	case 129:
		/* ICMP6_ECHO_REPLY */
		return "Echo Reply";
	case 130:
		/* ICMP6_MEMBERSHIP_QUERY */
		return "Membership Query";
	case 131:
		/* ICMP6_MEMBERSHIP_REPORT */
		return "Membership Report";
	case 132:
		/* ICMP6_MEMBERSHIP_REDUCTION */
		return "Membership Reduction";
	case 133:
		/* ND_ROUTER_SOLICIT */
		return "Router Solicitation";
	case 134:
		/* ND_ROUTER_ADVERT */
		return "Router Advertisement";
	case 135:
		/* ND_NEIGHBOR_SOLICIT */
		return "Neighbor Solicitation";
	case 136:
		/* ND_NEIGHBOR_ADVERT */
		return "Neighbor Advertisement";
	case 137:
		/* ND_REDIRECT */
		return "Redirect";
	}

	return("OUT-OF-RANGE");
}


int packet_ok(u_char *buf, int cc, struct sockaddr_in6 *from,
	      struct in6_addr *to, int seq,
	      struct timeval *tv)
{
	struct icmp6_hdr *icp;
	u_char type, code;

	icp = (struct icmp6_hdr *) buf;

	type = icp->icmp6_type;
	code = icp->icmp6_code;

	if ((type == ICMP6_TIME_EXCEEDED && code == ICMP6_TIME_EXCEED_TRANSIT) ||
	    type == ICMP6_DST_UNREACH)
	{
		struct ip6_hdr *hip;
		struct udphdr *up;
		int nexthdr;

		hip = (struct ip6_hdr *) (icp + 1);
		up = (struct udphdr *)(hip+1);
		nexthdr = hip->ip6_nxt;

		if (nexthdr == 44) {
			nexthdr = *(unsigned char*)up;
			up++;
		}
		if (nexthdr == IPPROTO_UDP)
		{
			struct pkt_format *pkt;

			pkt = (struct pkt_format *) (up + 1);

			if (ntohl(pkt->ident) == ident &&
			    ntohl(pkt->seq) == seq)
			{
				*tv = pkt->tv;
				return (type == ICMP6_TIME_EXCEEDED ? -1 : code+1);
			}
		}

	}

	if (verbose) {
		unsigned char *p;
		char pa1[MAX_HOSTNAMELEN];
		char pa2[MAX_HOSTNAMELEN];
		int i;

		p = (unsigned char *) (icp + 1);

		Printf("\n%d bytes from %s to %s", cc,
		       inet_ntop(AF_INET6, &from->sin6_addr, pa1, sizeof(pa1)),
		       inet_ntop(AF_INET6, to, pa2, sizeof(pa2)));

		Printf(": icmp type %d (%s) code %d\n", type, pr_type(type),
		       icp->icmp6_code);

		cc -= sizeof(struct icmp6_hdr);
		for (i = 0; i < cc ; i++) {
			if (i % 16 == 0)
				Printf("%04x:", i);
			if (i % 4 == 0)
				Printf(" ");
			Printf("%02x", 0xff & (unsigned)p[i]);
			if (i % 16 == 15 && i + 1 < cc)
				Printf("\n");
		}
		Printf("\n");
	}

	return(0);
}


void print(unsigned char *buf, int cc, struct sockaddr_in6 *from)
{
	char pa[MAX_HOSTNAMELEN];

	if (nflag)
		Printf(" %s", inet_ntop(AF_INET6, &from->sin6_addr,
					pa, sizeof(pa)));
	else
	{
		const char *hostname;
		struct hostent *hp;
		char *s = NULL;

		hostname = inet_ntop(AF_INET6, &from->sin6_addr, pa, sizeof(pa));

		if ((hp = gethostbyaddr((char *)&from->sin6_addr,
					sizeof(from->sin6_addr), AF_INET6))) {
#ifdef USE_IDN
			if (idna_to_unicode_lzlz(hp->h_name, &s, 0) != IDNA_SUCCESS)
				s = NULL;
#endif
		}

		Printf(" %s (%s)", hp ? (s ? s : hp->h_name) : hostname, pa);

		free(s);
	}
}


/*
 * Subtract 2 timeval structs:  out = out - in.
 * Out is assumed to be >= in.
 */
void
tvsub(out, in)
	register struct timeval *out, *in;
{
	if ((out->tv_usec -= in->tv_usec) < 0)   {
		out->tv_sec--;
		out->tv_usec += 1000000;
	}
	out->tv_sec -= in->tv_sec;
}

void usage(void)
{
	fprintf(stderr,
"Usage: traceroute6 [-dnrvV] [-m max_ttl] [-p port#] [-q nqueries]\n\t\
[-s src_addr] [-t tos] [-w wait] host [data size]\n");
	exit(1);
}


