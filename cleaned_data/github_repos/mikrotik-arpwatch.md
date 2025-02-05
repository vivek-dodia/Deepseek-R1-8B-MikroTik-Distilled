# Repository Information
Name: mikrotik-arpwatch

# Directory Structure
Directory structure:
└── github_repos/mikrotik-arpwatch/
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
    │   │       ├── pack-8d73d1d740c8ad3d32a3279cec735bb4cf72ede6.idx
    │   │       └── pack-8d73d1d740c8ad3d32a3279cec735bb4cf72ede6.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── ArpWatch/
    │   ├── ArpData.py
    │   ├── ArpWatchLogging.py
    │   ├── RosAPI.py
    │   └── __init__.py
    ├── LICENSE
    ├── mikrotik-arpwatch
    ├── mikrotik-arpwatch.cfg
    ├── mikrotik-arpwatch.py
    ├── README.md
    ├── rpm/
    │   └── mikrotik-arpwatch.spec
    ├── setup.py
    └── testdata/
        └── testdata.txt


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
	url = https://github.com/davidnutter/mikrotik-arpwatch.git
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
0000000000000000000000000000000000000000 48d9f9c67fa5eb34eb709ae8bf2b575cb72a4975 vivek-dodia <vivek.dodia@icloud.com> 1738606058 -0500	clone: from https://github.com/davidnutter/mikrotik-arpwatch.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 48d9f9c67fa5eb34eb709ae8bf2b575cb72a4975 vivek-dodia <vivek.dodia@icloud.com> 1738606058 -0500	clone: from https://github.com/davidnutter/mikrotik-arpwatch.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 48d9f9c67fa5eb34eb709ae8bf2b575cb72a4975 vivek-dodia <vivek.dodia@icloud.com> 1738606058 -0500	clone: from https://github.com/davidnutter/mikrotik-arpwatch.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
48d9f9c67fa5eb34eb709ae8bf2b575cb72a4975 refs/remotes/origin/master


File: /.git\refs\heads\master
48d9f9c67fa5eb34eb709ae8bf2b575cb72a4975


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /ArpWatch\ArpData.py
# Copyright (C) 2014  Biomathematics and Statistics Scotland
#               
# Author: David Nutter (david.nutter@bioss.ac.uk)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
#    Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
#    Neither the name of Biomathematics and Statistics Scotland nor the
#    names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import ArpWatchLogging
import math,os,re,shutil,socket,syslog,tempfile,time
        
class ArpEntry:
    "Represent ARP table entry"
    def __init__(self,ip,mac,epoch=int(time.time()),host=None):
        self.ip=ip
        self.mac=mac
        self.epoch=epoch
        
        if host is not None:
            self.host=host
        else:
            try:
                hostbits=socket.gethostbyaddr(ip) #TODO: this might be slow due to timeout issues; look at pydns if required
                self.host=hostbits[0].split(".")[0]
            except Exception,err:
                self.host=ip
                

    def equals(self,other_entry):
        "Return true if this entry is identical in all ways to the other entry"
        if isinstance(other_entry,ArpEntry):
            return (self.ip==other_entry.ip and
                    self.mac==other_entry.mac and
                    self.epoch==other_entry.epoch and
                    self.host==other_entry.host)
        return False

    def equivalent(self,other_entry):
        "Return true if IP/MAC pairing is the same as in other_entry"
        if isinstance(other_entry,ArpEntry):
            return (self.ip==other_entry.ip and
                    self.mac==other_entry.mac)
        return False

    def refresh(self):
        "Refresh the epoch time associated with this IP/MAC pairing to the current local time"
        self.epoch=int(time.time())

    def hash_key(self):
        return self.ip+"_"+self.mac
        

    #TODO: CIDR would be a better way than regex of doing ip include/exclude. 
class ArpData:
    
    def __init__(self,file_name):
        self.file_last_written=0
        self.file_name=file_name
        self.include_macaddr=None
        self.exclude_macaddr=None
        self.include_ipaddr=None
        self.exclude_ipaddr=None
        self.arp_table=dict()
        
    def read_file(self,clear_table=True):

        if clear_table:
            self.clear_table()

        ArpWatchLogging.log_message(syslog.LOG_INFO,"Reading ARP data file '%s'" % self.file_name)
        
        if not os.path.isfile(self.file_name):
            ArpWatchLogging.log_message(syslog.LOG_INFO,"ARP data file %s does not exist. It will be created when next written" % self.file_name)
            return True
        
        try:
            self.last_written=os.stat(self.file_name).st_mtime
            
            f = open(self.file_name)

            for line in f:
                try:
                    (mac,ip,epoch,host)=line.split("\t")
                    
                    entry=ArpEntry(ip,mac,int(epoch),host.rstrip())
                    self.arp_table[entry.hash_key()]=entry
                except Exception,err:
                    ArpWatchLogging.log_message(syslog.LOG_WARN,"Ignoring invalid ARP data line '%s'" % line)
                    continue
            f.close()
            return True
        
        except IOError,err:
            ArpWatchLogging.log_message(syslog.LOG_ERR,"Unable to read ARP data file '%s'.\nReason: '%s'" %(self.file_name,err))
            if clear_table:
                self.clear_table()
            return False

    def clear_table(self):
        "clear the arp table of data"

        ArpWatchLogging.log_message(syslog.LOG_INFO,"Clearing ARP data table")
        self.arp_table=dict()
        self.last_written=0
        
    def write_file(self):
        "write out the arp data in the arpwatch format"
        try:
            ArpWatchLogging.log_message(syslog.LOG_INFO,"Writing ARP data file '%s'" %(self.file_name))
            temp = tempfile.NamedTemporaryFile()
            for entry in self.arp_table.values():
                temp.write("%s\t%s\t%d\t%s\n" % ( entry.mac,entry.ip,entry.epoch,entry.host ))            
            temp.flush()
            shutil.copy(temp.name,self.file_name)
            temp.close()
            self.last_written=int(time.time())
        except IOError,err:
            ArpWatchLogging.log_message(syslog.LOG_ERR,"Unable to write to %s\n. Reason '%s'" % (self.file_name,err))

    def update_arp_entry(self,ip,mac):
        "update/create an entry for the specified ip/mac pair"

        if ip is None or mac is None:
            ArpWatchLogging.log_message(syslog.LOG_DEBUG,"Missing IP/Mac address when updating arp entries. Ignoring. ")
            return

        if not self.ip_address_included(ip):
            ArpWatchLogging.log_message(syslog.LOG_DEBUG,"IP address %s excluded by pattern rule. Ignoring. " % ip )
            return
        
        if not self.mac_address_included(mac):
            ArpWatchLogging.log_message(syslog.LOG_DEBUG,"MAC address %s excluded by pattern rule. Ignoring. " % mac )
            return
        
        ArpWatchLogging.log_message(syslog.LOG_INFO,"Updating ARP entry for %s %s" % (ip,mac))
        
        #TODO: better input validation
        key=ip+"_"+mac

        if self.arp_table.has_key(key):    
            entry = self.arp_table[ key ]
            entry.epoch=int(time.time())
        else:
            entry=ArpEntry(ip,mac)
            self.arp_table[ entry.hash_key() ]=entry;

    def entry(self,ip,mac):
        "Retrieve an entry, or None if entry does not exist"
        if ip is None or mac is None:
            return None
         
        key=ip+"_"+mac

        if self.arp_table.has_key(key):
            return self.arp_table[ key ]
        
        return None
        
    def clean_stale_arp(self,keep_days=180):
        "Clean up ARP entries older than keep_days. Also checks against include/exlude lists"


        # datetime could be used here for more accurate date
        # arithmetic but for these purposes it isn't necessary; just
        # simple epoch delta will do

        current_time=int(time.time())
        time_delta=keep_days*24*math.pow(60,2)
        oldest_allowed=current_time-time_delta

        ArpWatchLogging.log_message(syslog.LOG_NOTICE,
                                    "Cleaning up ARP entries older than %s" %
                                    (time.strftime("%F %X %Z",time.gmtime(oldest_allowed))))
        
        new_table=dict()
        remove_count=0
        
        for entry in self.arp_table.values():

            if ( self.ip_address_included(entry.ip) and
                 self.mac_address_included(entry.mac) and
                 entry.epoch > oldest_allowed):
                new_table[entry.hash_key()]=entry
            else:
                remove_count+=1

        ArpWatchLogging.log_message(syslog.LOG_NOTICE,"%d entries removed" % remove_count)
        
        self.arp_table=new_table

    def include_mac_address(self,pattern):
        if self.include_macaddr is None:
            self.include_macaddr=[]

        self.include_macaddr.append(re.compile(pattern))
    
    def exclude_mac_address(self,pattern):
        if self.exclude_macaddr is None:
            self.exclude_macaddr=[]

        self.exclude_macaddr.append(re.compile(pattern))
    
    def include_ip_address(self,pattern):
        if self.include_ipaddr is None:
            self.include_ipaddr=[]

        self.include_ipaddr.append(re.compile(pattern))
    
    def exclude_ip_address(self,pattern):
        if self.exclude_ipaddr is None:
            self.exclude_ipaddr=[]

        self.exclude_ipaddr.append(re.compile(pattern))
    
    def ip_address_included(self,address):
        if address is None:
            return False
        
        if self.include_ipaddr is not None:
            for pattern in self.include_ipaddr:
                if pattern.match(address):
                    return True
        
        if self.exclude_ipaddr is not None:
            for pattern in self.exclude_ipaddr:
                if pattern.match(address):
                    return False
        
        return True

    def mac_address_included(self,mac):

        if mac is None:
            return False
        
        if self.include_macaddr is not None:
            for pattern in self.include_macaddr:
                if pattern.match(mac):
                    return True
        
        if self.exclude_macaddr is not None:
            for pattern in self.exclude_macaddr:
                if pattern.match(mac):
                    return False
         
        return True
        
        
        


File: /ArpWatch\ArpWatchLogging.py
# Copyright (C) 2014  Biomathematics and Statistics Scotland
#               
# Author: David Nutter (david.nutter@bioss.ac.uk)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
#    Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
#    Neither the name of Biomathematics and Statistics Scotland nor the
#    names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys
import syslog

#Constants to set the default target
TARGET_CONSOLE=1
TARGET_SYSLOG=2

#Initialisation defaults. 
DEFAULT_LOG_LEVEL=syslog.LOG_NOTICE
LOG_FACILITY=syslog.LOG_USER

global_target=TARGET_CONSOLE
global_level=DEFAULT_LOG_LEVEL

#Symbol tables to convert numeric log levels into names. Only single
#levels supported.
SYMBOLIC_DISPATCH={
    "emergency": syslog.LOG_EMERG,
    "alert"    : syslog.LOG_ALERT,
    "critical" : syslog.LOG_CRIT,
    "error"    : syslog.LOG_ERR,
    "warning"  : syslog.LOG_WARNING,
    "notice"   : syslog.LOG_NOTICE,
    "info"     : syslog.LOG_INFO,
    "debug"    : syslog.LOG_DEBUG
    }

LEVEL_DISPATCH = dict((v,k) for k, v in SYMBOLIC_DISPATCH.iteritems())

SYMBOLIC_LEVEL_ORDER=['emergency', 'alert', 'critical', 'error', 'warning','notice', 'info', 'debug']

def init_logging(target=TARGET_CONSOLE,level=DEFAULT_LOG_LEVEL):
    global global_target
    global global_level

    if not type(level) is int:        
        raise RuntimeError("Unknown log level value %s" % level)
    
    global_target=target
    global_level=level
    
    if target==TARGET_CONSOLE:
        pass
    elif target==TARGET_SYSLOG:
        syslog.openlog("arpwatch",0,syslog.LOG_USER)
        syslog.setlogmask(syslog.LOG_UPTO(global_level))
    else:
        raise RuntimeError("Unknown target value")
                 
def log_message(priority,message):
    if global_target==TARGET_CONSOLE:
        sys.stderr.write(message.rstrip()+"\n")
    elif global_target==TARGET_SYSLOG:
        syslog.syslog(priority,message)

def symbolic_to_level(name):
    global SYMBOLIC_DISPATCH,DEFAULT_LOG_LEVEL
    
    if name is not None and SYMBOLIC_DISPATCH.has_key(name.lower()):
        return SYMBOLIC_DISPATCH[name.lower()]
    else:
        return DEFAULT_LOG_LEVEL

def level_to_symbolic(level):
    global LEVEL_DISPATCH,DEFAULT_LOG_LEVEL
    if level is not None and LEVEL_DISPATCH.has_key(int(level)):
        return LEVEL_DISPATCH[int(level)]
    else:
        return None

def is_symbolic_level(name):
    global SYMBOLIC_DISPATCH
    if name is not None:
        return SYMBOLIC_DISPATCH.has_key(name.lower())

    return False

def get_symbolic_levels():
    global SYMBOLIC_LEVEL_ORDER
    return SYMBOLIC_LEVEL_ORDER


File: /ArpWatch\RosAPI.py

# Original client source from Mikrotik themselves:
#
# http://wiki.mikrotik.com/index.php?title=Manual:API#Example_client
#
# Copyright (c) 2014, Mikrotik Inc.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
#    Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
#    Neither the name of Biomathematics and Statistics Scotland nor the
#    names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import posix, time, md5, binascii

DEBUG=False

class ApiRos:
    "Routeros api"
    def __init__(self, sk):
        self.sk = sk
        self.currenttag = 0
        
    def login(self, username, pwd):
        for repl, attrs in self.talk(["/login"]):
            chal = binascii.unhexlify(attrs['=ret'])
        md = md5.new()
        md.update('\x00')
        md.update(pwd)
        md.update(chal)
        replies = self.talk(["/login", "=name=" + username,
                             "=response=00" + binascii.hexlify(md.digest())])

        #Check for failed login
        for repl,attrs in replies:
            if repl=='!trap':
                return (False,attrs['=message'])
            
        return (True,'')

    #TODO: add logout method for clean(er) shutdown
    
    def talk(self, words):
        if self.writeSentence(words) == 0: return
        r = []
        while 1:
            i = self.readSentence();
            if len(i) == 0: continue
            reply = i[0]
            attrs = {}
            for w in i[1:]:
                j = w.find('=', 1)
                if (j == -1):
                    attrs[w] = ''
                else:
                    attrs[w[:j]] = w[j+1:]
            r.append((reply, attrs))
            if reply == '!done': return r

    def writeSentence(self, words):
        ret = 0
        for w in words:
            self.writeWord(w)
            ret += 1
        self.writeWord('')
        return ret

    def readSentence(self):
        r = []
        while 1:
            w = self.readWord()
            if w == '': return r
            r.append(w)
            
    def writeWord(self, w):
        if DEBUG:
            print "<<< " + w
        self.writeLen(len(w))
        self.writeStr(w)

    def readWord(self):
        ret = self.readStr(self.readLen())
        if DEBUG:
            print ">>> " + ret
        return ret

    def writeLen(self, l):
        if l < 0x80:
            self.writeStr(chr(l))
        elif l < 0x4000:
            l |= 0x8000
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        elif l < 0x200000:
            l |= 0xC00000
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        elif l < 0x10000000:        
            l |= 0xE0000000         
            self.writeStr(chr((l >> 24) & 0xFF))
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        else:                       
            self.writeStr(chr(0xF0))
            self.writeStr(chr((l >> 24) & 0xFF))
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))

    def readLen(self):              
        c = ord(self.readStr(1))    
        if (c & 0x80) == 0x00:      
            pass                    
        elif (c & 0xC0) == 0x80:    
            c &= ~0xC0              
            c <<= 8                 
            c += ord(self.readStr(1))    
        elif (c & 0xE0) == 0xC0:    
            c &= ~0xE0              
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
        elif (c & 0xF0) == 0xE0:    
            c &= ~0xF0              
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
        elif (c & 0xF8) == 0xF0:    
            c = ord(self.readStr(1))     
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
            c <<= 8                 
            c += ord(self.readStr(1))    
        return c                    

    def writeStr(self, str):        
        n = 0;                      
        while n < len(str):         
            r = self.sk.send(str[n:])
            if r == 0: raise ConnectionError, "connection closed by remote end"
            n += r                  

    def readStr(self, length):      
        ret = ''                    
        while len(ret) < length:    
            s = self.sk.recv(length - len(ret))
            if s == '': raise ConnectionError, "connection closed by remote end"
            ret += s
        return ret

class ConnectionError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


File: /ArpWatch\__init__.py
# Copyright (C) 2014  Biomathematics and Statistics Scotland
#               
# Author: David Nutter (david.nutter@bioss.ac.uk)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
#    Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
#    Neither the name of Biomathematics and Statistics Scotland nor the
#    names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

__all__ = ['ArpWatchLogging', 'ArpData','RosAPI']


File: /LICENSE
Copyright (c) 2015, davidnutter
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of mikrotik-arpwatch nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



File: /mikrotik-arpwatch
#!/bin/sh
#
# mikrotik-arpwatch     This shell script starts the mikrotik-arpwatch daemon
#
# chkconfig: - 86 04
# description: mikrotik-arpwatch connects to a routerboard
#
### BEGIN INIT INFO
# Provides: mikrotik-arpwatch
# Required-Start: $local_fs $network
# Required-Stop: $local_fs $network
# Default-Stop: 0 1 6
# Short-Description: This shell script starts the mikrotik-arpwatch daemon
# Description:       mikrotik-arpwatch collects arpwatch data from the Routerboard family of routers
### END INIT INFO

# Source function library.
. /etc/rc.d/init.d/functions

# Source networking configuration.
. /etc/sysconfig/network

# Source prog-specific configuration
if [ -f /etc/sysconfig/mikrotik-arpwatch ]; then
	. /etc/sysconfig/mikrotik-arpwatch
fi

# Check that networking is up.
[ ${NETWORKING} = "no" ] && exit 0

RETVAL=0
prog="mikrotik-arpwatch"
script="/usr/bin/mikrotik-arpwatch"

[ -f $script ] || exit 0

start() {
    # Start daemon
    echo -n "Starting $prog: "
    daemon $script --pid-file /var/run/$prog.pid
    RETVAL=$?
    if [ $RETVAL -eq 0 ]; then echo_success; else echo_failure; fi
    echo
    [ $RETVAL -eq 0 ] && touch /var/lock/subsys/$prog
    return $RETVAL
}


stop() {
    # Stop daemon
    echo -n "Shutting down $prog: "
    killproc $prog
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && rm -f /var/lock/subsys/$prog
    return $RETVAL
}

# See how we were called.
case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart|reload)
        stop
        start
        ;;
    status)
        status "$script"
        RETVAL=$?
        ;;
    condrestart)
        if status "$script" >/dev/null; then
            stop
            start
        fi
        ;;
    *)
        echo $"Usage: $0 {start|stop|restart|reload|status|condrestart}"
        exit 1
esac

exit $RETVAL



File: /mikrotik-arpwatch.cfg
#-*-shell-script-*-
[arpwatch]
#Where to write the ARP data we are using
datafile=/var/lib/mikrotik-arpwatch/arp.dat
#Keep records for this long (days)
keepdays=180

[daemon]
#Daemon's log level (one of 'emergency', 'alert', 'critical', 'error', 'warning','notice', 'info', 'debug')
#All messages up to this level will be logged
log_level=notice
#Username to run as
user=nobody
#Group to run as
group=nobody
#pid file to use
pid_file=/var/run/mikrotik-arpwatch.pid



[schedule]
#At least this many seconds between each write of the datafile to disk
writedelay=120
#Seconds between cleanup attempts
cleanupdelay=43200
#Seconds to wait for messages from routerboard before going and doing
#something else
select_timeout=5

[api]
user=apiuser
password=password
host=firewall.example.com:8728
#Use TCP keepalive to detect loss of connection to firewall
keepalive_enabled=True
#Override sysctl net.ipv4.tcp_keepalive_time (Default: 20 mins before sending a probe)
keepalive_time=1200
#Override sysctl net.ipv4.tcp_keepalive_probes (Default: send 9 probes before giving up) 
keepalive_probes=9
#Override sysctl net.ipv4.tcp_keepalive_intvl (Default: 30secs between probes)
keepalive_interval=30
#Number of seconds to wait before retrying a failed connection. A value of 0 will result in the daemon exiting immediately
#Otherwise the daemon will retry indefinitely at the specified intervals
retry_interval=60


#Use multiline items to set multiple patterns
#[patterns]
#include_mac=
#exclude_mac=
#include_ip=
#exclude_ip=


File: /mikrotik-arpwatch.py
#!/usr/bin/python

# Copyright (C) 2014  Biomathematics and Statistics Scotland
#               
# Author: David Nutter (david.nutter@bioss.ac.uk)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
#    Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
#    Neither the name of Biomathematics and Statistics Scotland nor the
#    names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from optparse import OptionParser

from ArpWatch import *
import ConfigParser
import errno
import grp
import os
import pwd
import re
import resource
import select
import signal
import socket
import sys
import syslog
import time
import traceback

#GLOBAL CONFIG OPTIONS

#Default API port on Routerboards. Can be specified in --host argument if change is needed
DEFAULT_PORT=8728

#Hardcode our config file path 
CONFIG_FILE=["/etc/mikrotik-arpwatch.cfg", "mikrotik-arpwatch.cfg"]

# File mode creation mask of the daemon.
UMASK = 0

# Default working directory for the daemon.
WORKDIR = "/"

# Default maximum for the number of available file descriptors.
MAXFD = 1024

# The standard I/O file descriptors are redirected to /dev/null by default.
if (hasattr(os, "devnull")):
   REDIRECT_TO = os.devnull
else:
   REDIRECT_TO = "/dev/null"

#GLOBAL VARIABLES (WRITABLE)
#---------------------------

#Allow access to the options set from config file/commandline
global_options=None

#Arp data object, accessible globally for convenience
global_arp_data=None


def set_default(section,element,cfg_parser,option_parser):
   if cfg_parser.has_option(section,element):
      option_parser.set_default( "%s_%s" % (section,element),cfg_parser.get(section,element))

def set_default_list(section,element,cfg_parser,option_parser):
   if cfg_parser.has_option(section,element):
      optionlist=cfg_parser.get(section,element).split("\n")
      option_parser.set_default( "%s_%s" % (section,element),optionlist)
   
def process_args(): 
    config = ConfigParser.SafeConfigParser()

    file_read_success=False
    
    for cfg_file in CONFIG_FILE:
       if not os.path.isfile(cfg_file):
          continue 
       
       try:       
          config.readfp(open(cfg_file))
          file_read_success=True
       except IOError,err:
          sys.stderr.write("Unable to read default config file %s.\nReason: %s\n" %(cfg_file,err))

    if not file_read_success:
       sys.stderr.write("No config files from the list %s could be read. Quitting\n" % ",".join(CONFIG_FILE))

    parser = OptionParser(usage="%prog [options]",version="%prog 0.2")

    #Config file options
    parser.add_option("","--datafile",type="string",dest="arpwatch_datafile",
                      help="Name of the datafile to save IP:MAC pairings")
    parser.add_option("","--keepdays",type="int",dest="arpwatch_keepdays",
                      help="Number of days to save IP:MAC pairings")

   
    parser.add_option("","--log-level",type="string",dest="daemon_log_level",
                      help="Log level to log upto. One of 'emergency', 'alert', 'critical', 'error', 'warning','notice', 'info', 'debug'") 
    parser.add_option("","--run-user",type="string",dest="daemon_user",
                      help="Username to run under when privileges are dropped")
    parser.add_option("","--run-group",type="string",dest="daemon_group",
                      help="Group to run under when privileges are dropped")
    parser.add_option("","--pid-file",type="string",dest="daemon_pid_file",
                      help="PID file to use (only relevant in Daemon mode)")
    
    parser.add_option("","--write-delay",type="int",dest="schedule_writedelay",
                      help="The minimum delay (in seconds) that will elapse between writes of the arp.dat file in normal usage")
    parser.add_option("","--cleanup-delay",type="int",dest="schedule_cleanupdelay",
                      help="The minimum delay (in seconds) that will elapse between cleanup of the arp data in normal usage")
    parser.add_option("","--select-timout",type="int",dest="schedule_select_timeout",
                      help="The maximum time to wait for messages from the routerboard before going and doing something else")

    parser.add_option("-u","--username",type="string",dest="api_user",
                      help="Username to connect to the routerboard with")
    parser.add_option("-p","--password",type="string",dest="api_password",
                      help="Password to connect to the routerboard with")
    parser.add_option("","--host",type="string",dest="api_host",                     
                      help="Hostname:port combo specifying the routerboard to connect to")

    parser.add_option("-k","--keepalive",action="store_true",dest="api_keepalive_enabled",                     
                      help="Enable TCP keepalive on connection to routerboard. Useful to detect loss of connection")
    parser.add_option("-K","--no-keepalive",action="store_false",dest="api_keepalive_enabled",                     
                      help="Disable TCP keepalive on connection to routerboard. Useful to detect loss of connection")        
    parser.add_option("","--keepalive-time",type="int",dest="api_keepalive_time",                     
                      help="Time in seconds before sending first keepalive probe")
    parser.add_option("","--keepalive-probes",type="int",dest="api_keepalive_probes",                     
                      help="Number of probe packets to send before assuming the connection is dead and raising a timeout error")
    parser.add_option("","--keepalive-interval",type="int",dest="api_keepalive_interval",                     
                      help="Time in seconds between probe packets")
    parser.add_option("","--retry-interval", type="int",dest="api_retry_interval",
                      help="""Time in seconds to wait before retrying a failed connection.
A value of 0 will result in immediate exit. Otherwise the daemon will retry
connections indefinitely at the specified interval""")
        
    parser.add_option("","--include-mac",action="append",dest="patterns_include_mac",
                      help="Supply a regex which matches MAC addresses to be explicitly included in the ARP data")
    parser.add_option("","--exclude-mac",action="append",dest="patterns_exclude_mac",
                      help="Supply a regex which matches MAC addresses to be explicitly excluded in the ARP data")
    parser.add_option("","--include-ip",action="append",dest="patterns_include_ip",
                      help="Supply a regex which matches IP addresses to be explicitly included in the ARP data")
    parser.add_option("","--exclude-ip",action="append",dest="patterns_exclude_ip",
                      help="Supply a regex which matches IP addresses to be explicitly excluded in the ARP data")
    
    #Set defaults from config file
    set_default("arpwatch","datafile",config,parser)
    set_default("arpwatch","keepdays",config,parser)

    set_default("daemon","log_level",config,parser)
    set_default("daemon","user",config,parser)
    set_default("daemon","group",config,parser)
    set_default("daemon","pid_file",config,parser)
    
    set_default("schedule","writedelay",config,parser)
    set_default("schedule","cleanupdelay",config,parser)
    set_default("schedule","select_timeout",config,parser)

    set_default("api","user",config,parser)
    set_default("api","password",config,parser)
    set_default("api","host",config,parser)
    set_default("api","keepalive_enabled",config,parser)
    set_default("api","keepalive_time",config,parser)
    set_default("api","keepalive_probes",config,parser)
    set_default("api","keepalive_interval",config,parser)
    set_default("api","retry_interval",config,parser)

    set_default_list("patterns","include_mac",config,parser)
    set_default_list("patterns","exclude_mac",config,parser)
    set_default_list("patterns","include_ip",config,parser)
    set_default_list("patterns","exclude_ip",config,parser)

    #Regular command line options
    parser.add_option("-t","--test",type="string",dest="test_data",
                      help="Do not connect to the routerboard. Instead process the input file and act accordingly. Will also print configuration information")

    parser.add_option("","--show-config",action="store_true",dest="print_config", default=False,
                      help="Do not connect to the the routerboard, just print configuration information")
    parser.add_option("-D","--no-detach",action="store_true",dest="nodetach", default=False,
                      help="Do not detach from console (daemonise). Instead, remain attached and print actions as they occur")

    
    (options,args) = parser.parse_args()
        
    return (options,args)

def establish_session():
    "Create a session with the routerboard API. Failures are logged. Socket is returned or Exceptions raised in the case of failure"
    hostbits = global_options.api_host.split(":")
    if len(hostbits) == 1:
        host = hostbits[0]
        port = int(DEFAULT_PORT)
    elif len(hostbits) ==2:
        host = hostbits[0]
        port = int(hostbits[1])
    else:
        ArpWatchLogging.log_message(syslog.LOG_ERR,"Host spec %s does not appear to be in host.name:port format. Aborting" % global_options.host)
        sys.exit(1)
    

    addr = socket.gethostbyname(host)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if global_options.api_keepalive_enabled:
       x = s.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE)
       if (x == 0):              
          x = s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
          s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, global_options.api_keepalive_time)
          s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, global_options.api_keepalive_probes)
          s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, global_options.api_keepalive_interval)
          
          ArpWatchLogging.log_message(syslog.LOG_NOTICE,"TCP Keepalive enabled: time=%d, probes=%d, probe_interval=%d" %
                                      (global_options.api_keepalive_time,
                                       global_options.api_keepalive_probes,
                                       global_options.api_keepalive_interval))
    else:
       ArpWatchLogging.log_message(syslog.LOG_WARNING,
                                   "TCP keepalive is disabled. Network disruption may cause this daemon to silently lose communication with the routerboard. Consider a periodic restart via cron to work around this potential issue")
                                       

    #TODO: Potentially set an explicit timeout here so we don't hang around for too long connecting to an unresponsive host
    ArpWatchLogging.log_message(syslog.LOG_NOTICE, "Attempting connection to routerboard %s" % global_options.api_host)
    s.connect((addr, port))  
    ArpWatchLogging.log_message(syslog.LOG_NOTICE, "Connected to routerboard %s" % global_options.api_host)
                                
    apiros = RosAPI.ApiRos(s)
    (login_ok,message)=apiros.login(global_options.api_user,global_options.api_password)

    if not login_ok:
       err_message="Login to routerboard failed. Potential Username/password issue.\nRouterboard responded: '%s' " % message
       ArpWatchLogging.log_message(syslog.LOG_ERR, err_message)
       s.close()
       raise LoginError(err_message)

    return apiros
       

def process_arp(response):

    if response is None:
        return

    ArpWatchLogging.log_message(syslog.LOG_DEBUG,"Processing API response\n"+'\n'.join(response))
    
    #We're only interested in actual ARP responses, not other things the API can send us.
    arp_response=dict()
    
    for resp_line in response:
        resp_line=resp_line.rstrip()

        match=re.match("=([^=]+)=(.*)$",resp_line)
        if match is not None:
            arp_response[match.group(1)]=match.group(2)

    if arp_response.has_key("address") and arp_response.has_key("mac-address"):
        global_arp_data.update_arp_entry(arp_response["address"],arp_response["mac-address"])                                

def test_mode():
    if not os.path.isfile(global_options.test_data):
        ArpWatchLogging.log_message(syslog.LOG_ERR,"Test data file '%s' is missing" % global_options.test_data)
        sys.exit(1)
        
    ArpWatchLogging.log_message(syslog.LOG_INFO,"Starting test mode using file '%s'" % global_options.test_data)
    
    try:
        input_data = open(global_options.test_data)
        
        rb_sentence=""
        
        for line in input_data:
            line=re.sub('\s*#.*$','',line)
            if len(line.rstrip())==0:
                if len(rb_sentence.rstrip()) > 0:
                    process_arp(rb_sentence.split("\n"))
                    rb_sentence=""
                    continue
                
            if len(line) > 0:
                rb_sentence=rb_sentence+line
                    
        input_data.close()

    except IOError,err:
        ArpWatchLogging.log_message(syslog.LOG_ERR,
                                    "Error reading testdata file '%s'\nReason: '%s'" %
                                    (global_options.test_data,err))
        sys.exit(1)
        
    for (key,arp_entry) in global_arp_data.arp_table.items():
        ArpWatchLogging.log_message(syslog.LOG_DEBUG,
                                    "Arp entry: %-20s %-20s %-20s %s"
                                    %(arp_entry.mac,arp_entry.ip,arp_entry.epoch,arp_entry.host))
                                        
    global_arp_data.write_file()

def data_mode():
   signal.signal(signal.SIGTERM,sigterm_handler)
   signal.signal(signal.SIGHUP,sighup_handler)
   signal.signal(signal.SIGUSR1,sigusr1_handler)
           
   ArpWatchState.next_write=global_arp_data.last_written+global_options.schedule_writedelay
   ArpWatchState.next_cleanup=global_arp_data.last_written+global_options.schedule_cleanupdelay
   
   ArpWatchLogging.log_message(syslog.LOG_NOTICE,"Starting Mikrotik Arpwatch. PID %d" % os.getpid())
   ArpWatchLogging.log_message(syslog.LOG_INFO,"Next data file write: %s" %
                               time.strftime("%F %X %Z",time.gmtime(ArpWatchState.next_write)))
   ArpWatchLogging.log_message(syslog.LOG_INFO,"Next data cleanup write: %s" %
                               time.strftime("%F %X %Z",time.gmtime(ArpWatchState.next_cleanup)))

   retry_count = 0 
   
   #Currently dead peer detection relies on TCP keepalive. Some other possible approaches:
   #1) PEEK a byte from each socket when it becomes available to read, if 0 bytes read then peer has gone away.
   #
   #2) Keep an activity timer within this daemon for each socket; when
   #   exceeded assume the connection is dead and restart
   #
   #3) Periodically send /cancel command and restart /ip/arp/listen;
   #   any attempt to write to a dead socket should cause an exception
   #   which we can catch
   #
   # Some discussion: http://blog.stephencleary.com/2009/05/detection-of-half-open-dropped.html
   #
   # Testing keepalive:
   #
   # 0) Configure reasonably short timeouts
   # 1) Create a connection as normal
   # 2) Insert a filewall rule like
   #       /sbin/iptables -I RH-Firewall-1-INPUT 7 -p tcp --sport 8728 -j DROP
   #    or similar (make sure you insert this above the related or established rule)
   # 3) Wait for the connection to die. Hopefully the daemon should then start retrying
   # 4) Finally, remove the firewall rule and hopefully the daemon should reconnect safely
   #
   while ArpWatchState.keep_running:
      try:

         #TODO: we could allow multiple routerboard sessions to be established
         #here; select will pick up the results for each 

         if retry_count > 0 and global_options.api_retry_interval <= 0:
            ArpWatchLogging.log_message(syslog.LOG_NOTICE, "Connection retry disabled (retry_interval=%d). Shutting down cleanly." %
                                        global_options.api_retry_interval)
            break
         elif retry_count > 0:
            ArpWatchLogging.log_message(syslog.LOG_NOTICE, "Waiting %d seconds before retrying connection" %
                                        global_options.api_retry_interval)
            time.sleep(global_options.api_retry_interval)
            
            
         rb_api=establish_session()
                 
         rb_api.writeSentence(["/ip/arp/listen"])

         while ArpWatchState.keep_running:
            r = select.select([rb_api.sk], [], [], global_options.schedule_select_timeout )
            if rb_api.sk in r[0]: 
               x = rb_api.readSentence() 
               process_arp(x)

            current_time=int(time.time())

            if current_time > ArpWatchState.next_cleanup:
               global_arp_data.clean_stale_arp(global_options.arpwatch_keepdays)
               ArpWatchState.next_cleanup=current_time+global_options.schedule_cleanupdelay
                        
            if current_time > ArpWatchState.next_write:
               global_arp_data.write_file()
               ArpWatchState.next_write=current_time+global_options.schedule_writedelay

      except socket.timeout, timeout_err:
         (errnum,message) = timeout_err

         ArpWatchLogging.log_message(syslog.LOG_ERR,"Lost connection to routerboard %s - timeout." % global_options.api_host)
         retry_count+=1
      except socket.error, socket_err:
         (errnum,message) = socket_err

         ArpWatchLogging.log_message(syslog.LOG_ERR,"Failed connection to routerboard %s - socket error: (%d) %s" %
                                     (global_options.api_host,errnum,message))
         retry_count+=1
         
      except select.error, select_err:
         (errnum,message) = select_err
         
         #Ignore EINTR so signal handlers can do their thing, otherwise treat as failed connection
         if errnum!=errno.EINTR:
            ArpWatchLogging.log_message(syslog.LOG_ERR,"select call aborted. Reason '%s'\n" % message)
            retry_count+=1
            
      except RosAPI.ConnectionError,conn_err: 
         ArpWatchLogging.log_message(syslog.LOG_ERR,"Lost connection to routerboard %s - %s " %
                                     (global_options.api_host,con_err))
         retry_count+=1
      except KeyboardInterrupt,int_err: 
         ArpWatchLogging.log_message(syslog.LOG_NOTICE,"Interrupt received, shutting down cleanly")                
         break         

   global_arp_data.write_file()
             
#SIGHUP in daemon mode will force data file write and cleanup to take place.
#In terminal mode, shutdown will occur
#
#TODO: could consider rereading the config file in daemon mode but a
#straight restart might be easier due to dropping privileges
def sighup_handler(signum,frame):
    if global_options.nodetach:
        ArpWatchLogging.log_message(syslog.LOG_NOTICE,"SIGHUP recieved, shutting down")
        ArpWatchState.keep_running=False
    else:
        ArpWatchLogging.log_message(syslog.LOG_NOTICE,"SIGHUP recieved, forcing cleanup and datafile write")
        current_time=int(time.time())
        ArpWatchState.next_write=current_time-5
        ArpWatchState.next_cleanup=current_time-5
     

#Shutdown process cleanly
def sigterm_handler(signum,frame):
    ArpWatchLogging.log_message(syslog.LOG_NOTICE,"SIGTERM recieved, shutting down")
    ArpWatchState.keep_running=False

#Force cleanup and datafile write
def sigusr1_handler(signum,frame):
    ArpWatchLogging.log_message(syslog.LOG_NOTICE,"SIGUSR1 recieved, forcing cleanup and datafile write")
    current_time=int(time.time())
    ArpWatchState.next_write=current_time-5
    ArpWatchState.next_cleanup=current_time-5

def create_daemon():
    #See here for inspiration: http://code.activestate.com/recipes/278731/
    try:
        pid = os.fork() #Fork a child
    except OSError, e:
        raise Exception, "%s [%d]" % (e.strerror, e.errno)

    if (pid == 0):	
        os.setsid()
      
        try:
            pid = os.fork()	# Fork a second child.
        except OSError, e:
            raise Exception, "%s [%d]" % (e.strerror, e.errno)

        if (pid == 0):	
            os.chdir(WORKDIR)

            os.umask(UMASK)
        else:
            os._exit(0)	# Exit parent (the first child) of the second child.
    else:
        os._exit(0)	# Exit parent of the first child.

    maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
    
    if (maxfd == resource.RLIM_INFINITY):
        maxfd = MAXFD
  
    # Iterate through and close all file descriptors.
    for fd in range(0, maxfd):
        try:
            os.close(fd)
        except OSError:	# ERROR, fd wasn't open to begin with (ignored)
            pass

    # Redirect standard file descriptors
    os.open(REDIRECT_TO, os.O_RDWR)	# standard input (0)
   
    # Duplicate standard input to standard output and standard error.
    os.dup2(0, 1)			# standard output (1)
    os.dup2(0, 2)			# standard error (2)

    # Create PID file before privilege drop
    try:
        pid_file=open(global_options.daemon_pid_file,'w')
        pid_file.write("%d\n" % os.getpid())
        pid_file.flush() 
        pid_file.close()
    except Exception,err:
        ArpWatchLogging.log_message(syslog.LOG_ERR,
                                    "Error creating PID file %s for daemon process. Aborting. Error was '%s'" %
                                    (global_options.daemon_pid_file,err))
        os._exit(1)
   
    return(0) 

def drop_privileges(uid_name='nobody', gid_name='nogroup'):
    if os.getuid() != 0:
        return

    die_horribly=False
    new_uid=None
    new_gid=None
    
    try:
        new_uid = pwd.getpwnam(uid_name).pw_uid
    except KeyError,err:
        ArpWatchLogging.log_err(syslog.LOG_ERR,"Drop privileges failed: User name '%s' does not exist" % uid_name)
        die_horribly=True
        
    try:
        new_gid = grp.getgrnam(gid_name).gr_gid
    except KeyError,err:
        ArpWatchLogging.log_err(syslog.LOG_ERR,"Drop privileges failed: Group name '%s' does not exist" % uid_name)
        die_horribly=True
        
    if die_horribly:
        sys.exit(1)
        
    ArpWatchLogging.log_message(syslog.LOG_INFO,"Dropping privileges to %s:%s" % (uid_name, gid_name))
    
    os.setgroups([])
    os.setgid(new_gid)
    os.setuid(new_uid)

    old_umask = os.umask(077)
    
def main():

    global global_arp_data,global_options
    
    (options,args) = process_args()

    global_options=options    

    if global_options.print_config or global_options.test_data:
       print "Current configuration:"
       for option,value in options.__dict__.items():
          print "%-20s = %s" % (option,value)
          
       if global_options.print_config:
          sys.exit(0)                  

    global_arp_data=ArpData.ArpData(global_options.arpwatch_datafile)

    #Validate options TODO: more to be done here...
    option_error=False
    if not ArpWatchLogging.is_symbolic_level(global_options.daemon_log_level):
       ArpWatchLogging.log_message(syslog.LOG_ERR,"Option daemon_log_level must have a value from the range %s " % ",".join(ArpWatchLogging.get_symbolic_levels()) )
       option_error=True

    #Get logging going ASAP
    if not (options.nodetach or options.test_data):
       numeric_log_level=ArpWatchLogging.symbolic_to_level(global_options.daemon_log_level)
       ArpWatchLogging.init_logging(target=ArpWatchLogging.TARGET_SYSLOG,level=numeric_log_level)

    if global_options.schedule_writedelay < 1:
       ArpWatchLogging.log_message(syslog.LOG_ERR,"Option schedule_writedelay must have positive integer value")
       option_error=True
       
    if global_options.patterns_include_mac is not None:
       for pattern in global_options.patterns_include_mac:
          global_arp_data.include_mac_address(pattern)

    if global_options.patterns_exclude_mac is not None:
       for pattern in global_options.patterns_exclude_mac:
          global_arp_data.exclude_mac_address(pattern)

    if global_options.patterns_include_ip is not None:
       for pattern in global_options.patterns_include_ip:
          global_arp_data.include_ip_address(pattern)

    if global_options.patterns_exclude_ip is not None:
       for pattern in global_options.patterns_exclude_ip:
          global_arp_data.exclude_ip_address(pattern)
          
    if option_error:
       sys.exit(1)

    try:
       #Options OK so daemonise unless we're in test mode or forced to foreground 
       if not (options.nodetach or options.test_data):
          create_daemon()
          drop_privileges(global_options.daemon_user,global_options.daemon_group)

       global_arp_data.read_file()
       global_arp_data.clean_stale_arp(global_options.arpwatch_keepdays)   

       if global_options.test_data:
          test_mode()
       else:       
          data_mode()
    except Exception,err:
       ArpWatchLogging.log_message(syslog.LOG_ERR,"Global exception handler triggered. Trace:\n%s" % traceback.format_exc())
       if global_options.nodetach or global_options.test_data:
          sys.exit(1) #Exit with cleanup in non-daemon mode
       else:
          os._exit(1) #Exit without cleanup in daemon mode
                
class ArpWatchState:
    keep_running=True
    next_cleanup=0
    next_write=0    

class LoginError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

    
if __name__ == '__main__':
    main()


File: /README.md
# mikrotik-arpwatch
Arpwatch-like daemon to monitor Mikrotik RouterOS devices.


File: /rpm\mikrotik-arpwatch.spec
#-*-shell-script-*-
%define debug_package %{nil}
Summary: Tool to read ARP data from Mikrotik router API 
Name: mikrotik-arpwatch
Version: 0.2
Release: 1%{?dist}
License: BSD
BuildArch: noarch
Group: Systems/Environment
URL: http://www.bioss.ac.uk/
Source0: %{name}-%{version}.tar.gz
BuildRequires: python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Tool to read ARP data from Mikrotik router API. Required for providing
network accounting information to service provider for billing
purposes.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

#Must list this explicity to allow us to set attrs
sed -i -e '/mikrotik-arpwatch.cfg/ d' -e 's/mikrotik-arpwatch.py/mikrotik-arpwatch/' INSTALLED_FILES
%{__install} -d -m 0755 %{buildroot}/var/lib/%{name}
%{__mv} %{buildroot}/%{_bindir}/mikrotik-arpwatch.py %{buildroot}/%{_bindir}/mikrotik-arpwatch

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name}

%preun
if [ $1 = 0 ]; then
 [ -f /var/run/%{name}.pid ] && /sbin/service %{name} stop > /dev/null 2>&1
 /sbin/chkconfig --del %{name}
fi


%files -f INSTALLED_FILES
%defattr(-,root,root,-)
%config(noreplace) %attr(0600,root,root) /etc/mikrotik-arpwatch.cfg
%dir %attr(-,nobody,nobody) /var/lib/mikrotik-arpwatch

%changelog
* Wed Jan 13 2016 David Nutter <david.nutter@bioss.ac.uk> - mikrotik-arpwatch-0.2.el5
- Added functioning keepalive support to detect network errors
* Thu Mar 6 2014 David Nutter <david.nutter@bioss.ac.uk> - mikrotik-arpwatch-0.1.el5
- Initial build


File: /setup.py
#!/usr/bin/python
# Build script for mikrotik-arpwatch package
# 
# Copyright (C) 2014  Biomathematics and Statistics Scotland
#               
# Author: David Nutter (david.nutter@bioss.ac.uk)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
#    Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
#    Neither the name of Biomathematics and Statistics Scotland nor the
#    names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from distutils.core import setup

setup(name='mikrotik-arpwatch',
      version='0.1',
      description='',
      author='David Nutter',
      author_email='david.nutter@bioss.ac.uk',
      packages=['ArpWatch'],
      scripts=['mikrotik-arpwatch.py'],
      data_files=[ ('/etc/',['mikrotik-arpwatch.cfg']),
                   ('/etc/init.d',['mikrotik-arpwatch']) ]
)


File: /testdata\testdata.txt
# TEST DATA FILE for testmode. Flesh out with responses other than arp
# responses for robustness
#
# Comments like this are ignored

=.id=*1
=address=212.219.57.129
=mac-address=00:23:AE:AD:D6:92
=interface=ether8
=invalid=false
=DHCP=false
=dynamic=true
=disabled=false

!re
=.id=*2
=address=212.219.57.235
=mac-address=00:14:4F:01:A8:20
=interface=ether8
=invalid=false
=DHCP=false
=dynamic=true
=disabled=false

!re
=.id=*3
=address=212.219.57.254
=mac-address=00:0C:42:C0:B5:5C
=interface=ether8
=invalid=false
=DHCP=false
=dynamic=true
=disabled=false

!re
=.id=*4
=address=212.219.57.230
=mac-address=00:14:4F:D2:60:FC
=interface=ether8
=invalid=false
=DHCP=false
=dynamic=true
=disabled=false

!re
=.id=*5
=address=212.219.57.233
=mac-address=00:14:4F:D2:60:C4
=interface=ether8
=invalid=false
=DHCP=false
=dynamic=true
=disabled=false


#Indicates when an arp entry is removed. We can ignore these.

!re
=.id=*5
=.dead=true
 


