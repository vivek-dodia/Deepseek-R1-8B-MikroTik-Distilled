# Repository Information
Name: mikrotik-routeros

# Directory Structure
Directory structure:
└── github_repos/mikrotik-routeros/
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
    │   │       ├── pack-374fdd95102b015d5cee304702df9156f8b97a51.idx
    │   │       └── pack-374fdd95102b015d5cee304702df9156f8b97a51.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── LICENSE
    ├── README.rst
    └── scripts/
        ├── Function.civilDateTimeToSecondsSince19700101.rsc
        ├── Function.civilDateToDaysSince19700101.rsc
        ├── Function.dateTimeToYYYYMMDDhhmmssNumber.rsc
        ├── Function.dateTimeToYYYYMMDDhhmmssString.rsc
        ├── Function.dateToYYYYMMDDString.rsc
        ├── Function.endsWithString.rsc
        ├── Function.escapeString.rsc
        ├── Function.isValidIPv4.rsc
        ├── Function.padLeftString.rsc
        ├── Function.padRightString.rsc
        ├── Function.startsWithString.rsc
        ├── Function.stripInvalidHostNameCharactersFromString.rsc
        ├── Function.systemScriptJobCountTypeIsCommand.rsc
        ├── Function.timeToHHMMSSString.rsc
        ├── Function.timeToSecondsSinceMidnight.rsc
        ├── Function.toString.rsc
        ├── Generate-convert-set-statements-for.Function.escapeString.rsc
        ├── import.file-scripts-functions-procedures.rsc
        ├── list.systemScript.file-subdirectory-scripts.rsc
        ├── list.systemScript.lengthName.rsc
        ├── Procedure.outputError.rsc
        ├── Procedure.outputInfo.rsc
        ├── Procedure.varDump.rsc
        └── README.rst


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
	url = https://github.com/jpluimers/mikrotik-routeros.git
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
0000000000000000000000000000000000000000 76808c53273dd2b6bd7a3f658103a7248ef4cd58 vivek-dodia <vivek.dodia@icloud.com> 1738605959 -0500	clone: from https://github.com/jpluimers/mikrotik-routeros.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 76808c53273dd2b6bd7a3f658103a7248ef4cd58 vivek-dodia <vivek.dodia@icloud.com> 1738605959 -0500	clone: from https://github.com/jpluimers/mikrotik-routeros.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 76808c53273dd2b6bd7a3f658103a7248ef4cd58 vivek-dodia <vivek.dodia@icloud.com> 1738605959 -0500	clone: from https://github.com/jpluimers/mikrotik-routeros.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
76808c53273dd2b6bd7a3f658103a7248ef4cd58 refs/remotes/origin/master


File: /.git\refs\heads\master
76808c53273dd2b6bd7a3f658103a7248ef4cd58


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /LICENSE
The MIT License (MIT)

Copyright (c) 2016 Jeroen Wiert Pluimers

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


File: /README.rst
Some usful MikroTik RouterOS things
===================================

This repository contains stuff I collected over time to help me administer MikroTik RouterOS based devices.

There is a README.rst per folder:

`scripts <scripts/README.rst>`_
-------------------------------

Scripting Examples


File: /scripts\Function.civilDateTimeToSecondsSince19700101.rsc
/system script environment remove [find where name="civilDateTimeToSecondsSince19700101"];
:global civilDateTimeToSecondsSince19700101 do={

  /system script environment get dateTimeToYYYYMMDDhhmmssString
  :global dateTimeToYYYYMMDDhhmmssString

  /system script environment get civilDateToDaysSince19700101
  :global civilDateToDaysSince19700101

  /system script environment get timeToSecondsSinceMidnight
  :global timeToSecondsSinceMidnight

#  /system script environment get varDump
#  :global varDump;

#:put "value=";
#$varDump value=$value;

  :local dateTimeString [$dateTimeToYYYYMMDDhhmmssString value=$value];
## now we have a valid date formatted like this:
##   20161023010203
##   012345678901234 index mod 10 for data
##   01234           YYYY
##       456             MM
##         678             DD
##           890            hh
##             012            mm
##               234            ss
  :local dateString [:pick $dateTimeString 0 8];
  :local timeString [:pick $dateTimeString 8 14];
#:put "dateTimeString=";
#$varDump value=$dateTimeString;
#:put "dateString=";
#$varDump value=$dateString;
#:put "dateString=";
#$varDump value=$dateString;

  :local daysSince19700101 [$civilDateToDaysSince19700101 value=$dateString];
  :local secondsSinceMidnight [$timeToSecondsSinceMidnight value=$timeString];

  :local result ($secondsSinceMidnight + 86400 * $daysSince19700101);

#:put "result=";
#$varDump value=$result;
  :return $result;
};

## Examples:
## /import scripts/Function.civilDateTimeToSecondsSince19700101.rsc
## :put [$civilDateTimeToSecondsSince19700101 value=([/system clock get date])]
## :put [$civilDateTimeToSecondsSince19700101 value="foo"]
## :put [$civilDateTimeToSecondsSince19700101 value="20161013"]
## 17087
## :put [$civilDateTimeToSecondsSince19700101 value="oct/13/2016"]
## 17087
## :put [$civilDateTimeToSecondsSince19700101 value="oct/13"]
## 17087
## :put [$civilDateTimeToSecondsSince19700101 value="20160103"]
## 16803
## :put [$civilDateTimeToSecondsSince19700101 value="jan/03/2016"]
## 16803
## :put [$civilDateTimeToSecondsSince19700101 value="jan/03"]
## 16803
## :put [$civilDateTimeToSecondsSince19700101 value="20161014"]
## 17088
## :put [$civilDateTimeToSecondsSince19700101 value="oct/14/2016"]
## 17088
## :put [$civilDateTimeToSecondsSince19700101 value="oct/14"]
## 17088


File: /scripts\Function.civilDateToDaysSince19700101.rsc
/system script environment remove [find where name="civilDateToDaysSince19700101"];
:global civilDateToDaysSince19700101 do={
## based on
## - http://stackoverflow.com/questions/7960318/math-to-convert-seconds-since-1970-into-date-and-vice-versa
## - http://howardhinnant.github.io/date_algorithms.html#days_from_civil

## $value can either be either in ISO-8601 (yyyymmdd) long (mmm/dd/yyyy) or short (mmm/dd) Mikrotik format. If short, then the current year is used in yyyy.
## if $value has an invalid date, then [/system clock get date] is used

## Does not take into account leap seconds: only leap days

## Returns number of days since civil 1970-01-01.  Negative values indicate
##    days prior to 1970-01-01.
## Preconditions:  y-m-d represents a date in the civil (Gregorian) calendar
##                 m is in [1, 12]
##                 d is in [1, last_day_of_month(y, m)]
##                 y is "approximately" in
##                   [numeric_limits<Int>::min()/366, numeric_limits<Int>::max()/366]
##                 Exact range of validity is:
##                 [civil_from_days(numeric_limits<Int>::min()),
##                  civil_from_days(numeric_limits<Int>::max()-719468)]

## template <class Int>
## constexpr
## Int
## days_from_civil(Int y, unsigned m, unsigned d) noexcept
## {
##     static_assert(std::numeric_limits<unsigned>::digits >= 18,
##              "This algorithm has not been ported to a 16 bit unsigned integer");
##     static_assert(std::numeric_limits<Int>::digits >= 20,
##              "This algorithm has not been ported to a 16 bit signed integer");
##     y -= m <= 2;
##     const Int era = (y >= 0 ? y : y-399) / 400;
##     const unsigned yoe = static_cast<unsigned>(y - era * 400);      // [0, 399]
##     const unsigned doy = (153*(m + (m > 2 ? -3 : 9)) + 2)/5 + d-1;  // [0, 365]
##     const unsigned doe = yoe * 365 + yoe/4 - yoe/100 + doy;         // [0, 146096]
##     return era * 146097 + static_cast<Int>(doe) - 719468;
## }

## split it into the various numeric parts, based on:
## - http://wiki.mikrotik.com/wiki/Script_to_find_the_day_of_the_week
## - http://forum.mikrotik.com/viewtopic.php?t=110778#p550429

#  /system script environment get varDump
#  :global varDump;

#:put "value=";
#$varDump value=$value;

## unlike POSIX, character classes like [:digit:] are not supported in regular expressions http://forum.mikrotik.com/viewtopic.php?f=9&t=113422
## unlike POSIX regex, you have to escape the $ here "because Mikrotik scripting language"
#  :local dateOnlyMask "^[a-zA-Z]{3}/[:digit:]{2}/[0-9]{4}\$";
  :local iso8601DateOnlyMask "^[0-9]{4}[0-9]{2}[0-9]{2}\$";
  :local dateOnlyMask "^[a-zA-Z]{3}/[0-9]{2}/[0-9]{4}\$";
  :local shortDateOnlyMask "^[a-zA-Z]{3}/[0-9]{2}\$";

  :local varDay;
  :local varMonth;
  :local varYear;

  :if ($value~$iso8601DateOnlyMask) do={
#    :put "iso8601DateOnly";
## now we have a valid date formatted like this:
##   20161013
##   012345678 index mod 10 for data
    :set $varYear [:pick $value 0 4];
    :set $varMonth [:pick $value 4 6];
    :set $varDay [:pick $value 6 8];
#:put "varYear=";
#$varDump value=$varYear;
#:put "varMonth=";
#$varDump value=$varMonth;
#:put "varDay=";
#$varDump value=$varDay;
  } else={
    :local date
    :if ($value~$dateOnlyMask) do={
#      :put "dateOnly";
      :set $date ($value);
    } else={
      :if ($value~$shortDateOnlyMask) do={
#          :put "shortDateOnly";
##       /log print where buffer=failedauth
##       oct/14 00:19:51 system,error,critical login failure for user root from 201.217.248.217 via telnet
##       012 45 78 01 34   index mod 10 for data
##          3  6  9  2  5  index mod 10 for separators
        :local currentDate [/system clock get date]
        :local currentYear [:pick $currentDate 7 11]
        :local shortDatePart [:pick $value 0 6]
        :set $date ($shortDatePart."/$currentYear");
      } else={
#        :put "not any of iso8601DateOnly, dateOnly, shortDateOnly"
        :set $date ([/system clock get date]);
      };
    };
#:put "date=";
#$varDump value=$date;
##   now we have a valid date formatted like this:
##   oct/13/2016
##   012 45 78901 index mod 10 for data
##      3  6      index mod 10 for separators
    :local months [:toarray "jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec"]
    :local varMonthString [:pick $date 0 3];
    :local varMonthPosition [:find $months $varMonthString -1];
    :set $varMonth ($varMonthPosition + 1);
#:put "months=";
#$varDump value=$months;
#:put "varMonthString=";
#$varDump value=$varMonthString;
#:put "varMonthPosition=";
#$varDump value=$varMonthPosition;
#:put "varMonth=";
#$varDump value=$varMonth;
    :if ($varMonth < 10) do={
      :set varMonth ("0" . $varMonth);
#:put "varMonth=";
#$varDump value=$varMonth;
    }
    :set $varDay [:pick $date 4 6];
    :set $varYear [:pick $date 7 11];
#:put "varDay=";
#$varDump value=$varDay;
#:put "varYear=";
#$varDump value=$varYear;
  };

  :local d [:tonum $varDay];
  :local m [:tonum $varMonth];
  :local y [:tonum $varYear];
#:put "d=";
#$varDump value=$d;
#:put "m=";
#$varDump value=$m;
#:put "y=";
#$varDump value=$y;

  :if ($m <= 2) do={
    :set y ($y -1);
  }
#:put "y=";
#$varDump value=$y;

  :local era $y;
  if (y < 0) do={
    :set era ($y-399);
  }
#:put "era=";
#$varDump value=$era;
  :set era ($era / 400);
#:put "era=";
#$varDump value=$era;

  :local yoe ($y - $era * 400);
  ## [0, 399]
#:put "y=";
#$varDump value=$y;

  :local moy $m;
  :if ($m > 2) do={
    :set moy ($moy-3);
  } else={
    :set moy ($moy+9);
  }
#:put "moy=";
#$varDump value=$moy;

  :local doy ((153*$moy + 2)/5 + $d-1);
  ## [0, 365]
#:put "doy=";
#$varDump value=$doy;

  :local doe ($yoe * 365 + $yoe/4 - $yoe/100 + $doy);
  ## [0, 146096]
#:put "doe=";
#$varDump value=$doe;

  :local result ($era * 146097 + $doe - 719468);

#:put "result=";
#$varDump value=$result;
  :return $result;
};

## Examples:
## /import scripts/Function.civilDateToDaysSince19700101.rsc
## :put [$civilDateToDaysSince19700101 value=([/system clock get date])]
## :put [$civilDateToDaysSince19700101 value="foo"]
## :put [$civilDateToDaysSince19700101 value="20161013"]
## 17087
## :put [$civilDateToDaysSince19700101 value="oct/13/2016"]
## 17087
## :put [$civilDateToDaysSince19700101 value="oct/13"]
## 17087
## :put [$civilDateToDaysSince19700101 value="20160103"]
## 16803
## :put [$civilDateToDaysSince19700101 value="jan/03/2016"]
## 16803
## :put [$civilDateToDaysSince19700101 value="jan/03"]
## 16803
## :put [$civilDateToDaysSince19700101 value="20161014"]
## 17088
## :put [$civilDateToDaysSince19700101 value="oct/14/2016"]
## 17088
## :put [$civilDateToDaysSince19700101 value="oct/14"]
## 17088


File: /scripts\Function.dateTimeToYYYYMMDDhhmmssNumber.rsc
/system script environment remove [find where name="dateTimeToYYYYMMDDhhmmssNumber"];
:global dateTimeToYYYYMMDDhhmmssNumber do={
## returns a numeric YYYYMMDDhhmmss representation of the DateTime string in $value
## if $value only contains a time portion, then [/system clock get date] is used as date portion
## if $value only contains a date portion, then [/system clock get time] is used as time portion
## if $value has an invalid date or time portion, then [/system clock get date].[/system clock get time] is used
## the date portion can be either in long (mmm/dd/yyyy) or short (mmm/dd) Mikrotik format. If short, then the current year is used in yyyy.

  /system script environment get dateTimeToYYYYMMDDhhmmssString
  :global dateTimeToYYYYMMDDhhmmssString;
#  /system script environment get varDump
#  :global varDump;

#:put "value=";
#$varDump value=$value;

  :local dateTimeString [$dateTimeToYYYYMMDDhhmmssString value=$value];

  :local result [:tonum $dateTimeString];

#:put "result=";
#$varDump value=$result;
  :return $result;
};

## Examples:
## /import scripts/Function.dateTimeToYYYYMMDDhhmmssNumber.rsc
## :put [$dateTimeToYYYYMMDDhhmmssNumber value=([/system clock get date] . [/system clock get time])]
## :put [$dateTimeToYYYYMMDDhhmmssNumber value=([/system clock get time])]
## :put [$dateTimeToYYYYMMDDhhmmssNumber value=([/system clock get date])]
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="oct/13/201617:37:09"]
## 20161013173709
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="17:37:09"]
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="oct/13/2016"]
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="oct/13"]
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="foo"]
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="jan/03"]
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="jan/03/2016"]
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="jan/03/201607:06:09"]
## 20160103070609
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="07:06:09"]
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="jan/03/2016"]
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="oct/14 00:19:51"]
## 20161014001951
## :put [$dateTimeToYYYYMMDDhhmmssNumber value="oct/14/2016 09:48:25"]
## 20161014094825


File: /scripts\Function.dateTimeToYYYYMMDDhhmmssString.rsc
/system script environment remove [find where name="dateTimeToYYYYMMDDhhmmssString"];
:global dateTimeToYYYYMMDDhhmmssString do={
## returns a string YYYYMMDDhhmmss representation of the DateTime string in $value
## if $value only contains a time portion, then [/system clock get date] is used as date portion
## if $value only contains a date portion, then [/system clock get time] is used as time portion
## the date portion of $value can be either in long (mmm/dd/yyyy) or short (mmm/dd) Mikrotik format. If short, then the current year is used in yyyy.
## the time portion of $value can either be either in ISO-8601 (hhmmss) Mikrotik (hh:mm:ss) format.
## if $value has an invalid date or time portion, then [/system clock get date].[/system clock get time] is used

## maybe TODO: ensure the various parts are valid:
## - month is valid
## - day of the month is valid (0..27 extended by max days in month)
## - hour in range 0..23
## - minute in range 0..59
## - second in range 0..59

  /system script environment get dateToYYYYMMDDString
  :global dateToYYYYMMDDString;

  /system script environment get timeToHHMMSSString
  :global timeToHHMMSSString;

#  /system script environment get varDump
#  :global varDump;

#:put "value=";
#$varDump value=$value;

  :local dateString "";
  :local timeString "";
## unlike POSIX, character classes like [:digit:] are not supported in regular expressions http://forum.mikrotik.com/viewtopic.php?f=9&t=113422
## unlike POSIX regex, you have to escape the $ here "because Mikrotik scripting language"
#  :local dateOnlyMask "^[a-zA-Z]{3}/[:digit:]{2}/[0-9]{4}\$";
  :local iso8601DateOnlyMask "^[0-9]{4}[0-9]{2}[0-9]{2}\$";
  :local dateOnlyMask "^[a-zA-Z]{3}/[0-9]{2}/[0-9]{4}\$";
  :local shortDateOnlyMask "^[a-zA-Z]{3}/[0-9]{2}\$";

  :local iso8601TimeOnlyMask "^[0-9]{2}[0-9]{2}[0-9]{2}\$";
  :local timeOnlyMask "^[0-9]{2}:[0-9]{2}:[0-9]{2}\$";

  :local iso8601DateTimeMask "^[0-9]{4}[0-9]{2}[0-9]{2}[0-9]{2}[0-9]{2}[0-9]{2}\$";
  :local iso8601DateSpaceTimeMask "^[0-9]{4}[0-9]{2}[0-9]{2} [0-9]{2}[0-9]{2}[0-9]{2}\$";

  :local dateTimeMask "^[a-zA-Z]{3}/[0-9]{2}/[0-9]{4}[0-9]{2}:[0-9]{2}:[0-9]{2}\$";
  :local dateSpaceTimeMask "^[a-zA-Z]{3}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}\$";

  :local shortDateTimeMask "^[a-zA-Z]{3}/[0-9]{2}[0-9]{2}:[0-9]{2}:[0-9]{2}\$";
  :local shortDateSpaceTimeMask "^[a-zA-Z]{3}/[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}\$";

  :if ($value~$iso8601DateOnlyMask) do={
#    :put "iso8601DateOnly";
##   20161231
##   01234567   index mod 10 for data (date portion only)
##           8  index mod 10 for separators
    :set $dateString [$dateToYYYYMMDDString value=$value];
  } else={
    :if ($value~$dateOnlyMask) do={
#      :put "dateOnly";
##   /log print where buffer=failedauth
##   oct/14/2016
##   012 45 7890   index mod 10 for data
##      3  6    1  index mod 10 for separators
      :set $dateString [$dateToYYYYMMDDString value=$value];
    } else={
      :if ($value~$shortDateOnlyMask) do={
#        :put "shortDateOnly";
##   /log print where buffer=failedauth
##   oct/14 system,error,critical login failure for user root from 201.217.248.217 via telnet
##   012 45   index mod 10 for data
##      3  6  index mod 10 for separators
        :local currentDate [/system clock get date]
        :local currentYear [:pick $currentDate 7 11]
        :set $dateString [$dateToYYYYMMDDString value=($value."/$currentYear")];
      } else={
        :if ($value~$iso8601TimeOnlyMask) do={
#          :put "iso8601TimeOnly";
##   012345
##   012345   index mod 10 for data (date portion only)
##         6  index mod 10 for separators
          :set $timeString $value;
        } else={
          :if ($value~$timeOnlyMask) do={
#            :put "timeOnly";
## 17:37:09
## 01 34 67  index mod 10 for data (time portion only)
##   2  5  8 index mod 10 for separators (time portion only)
            :set $timeString [$timeToHHMMSSString value=$value];
          } else={
            :if ($value~$iso8601DateTimeMask) do={
#              :put "iso8601DateTime";
##   20161231012345
##   01234567         index mod 10 for data (date portion only)
##           890123   index mod 10 for data (time portion only)
##                 4  index mod 10 for separators
              :set $dateString [:pick $value 0 8]
              :set $timeString [:pick $value 8 14]
            } else={
              :if ($value~$iso8601DateSpaceTimeMask) do={
#                :put "iso8601DateSpaceTime";
##   20161231 012345
##   01234567          index mod 10 for data (date portion only)
##            901234   index mod 10 for data (time portion only)
##           8      5  index mod 10 for separators
                :set $dateString [:pick $value 0 8]
                :set $timeString [:pick $value 9 15]
              } else={
                :if ($value~$dateTimeMask) do={
#                  :put "dateTime";
## oct/13/201617:37:09
## 012 45 7890          index mod 10 for data (date portion only)
##    3  6    1         index mod 10 for separators (date portion only)
##            12 45 78  index mod 10 for data (time portion only)
##              3  6  9 index mod 10 for separators (time portion only)
                  :set $dateString [$dateToYYYYMMDDString value=[:pick $value 0 11]];
                  :set $timeString [$timeToHHMMSSString value=[:pick $value 11 19]];
                } else={
                  :if ($value~$dateSpaceTimeMask) do={
#                    :put "dateSpaceTime";
## oct/13/2016 17:37:09
## 012 45 7890          index mod 10 for data (date portion only)
##    3  6    1         index mod 10 for separators (date portion only)
##             23 56 89  index mod 10 for data (time portion only)
##               4  7  0 index mod 10 for separators (time portion only)
                    :set $dateString [$dateToYYYYMMDDString value=[:pick $value 0 11]];
                    :set $timeString [$timeToHHMMSSString value=[:pick $value 12 20]];
                  } else={
                    :if ($value~$shortDateTimeMask) do={
#                      :put "shortDateTime";
## oct/1317:37:09
## 012 45          index mod 10 for data (date portion only)
##    3  6         index mod 10 for separators (date portion only)
##       67 90 23  index mod 10 for data (time portion only)
##         89 1  4 index mod 10 for separators (time portion only)
                      :local currentDate [/system clock get date]
                      :local currentYear [:pick $currentDate 7 11]
                      :set $dateString [$dateToYYYYMMDDString value=([:pick $value 0 6]."/$currentYear")];
                      :set $timeString [$timeToHHMMSSString value=[:pick $value 7 14]];
                    } else={
                      :if ($value~$shortDateSpaceTimeMask) do={
#                        :put "shortDateSpaceTime";
## oct/13 17:37:09
## 012 45           index mod 10 for data (date portion only)
##    3  6          index mod 10 for separators (date portion only)
##        78 01 34  index mod 10 for data (time portion only)
##          9  2  5 index mod 10 for separators (time portion only)
                        :local currentDate [/system clock get date]
                        :local currentYear [:pick $currentDate 7 11]
                        :set $dateString [$dateToYYYYMMDDString value=([:pick $value 0 6]."/$currentYear")];
                        :set $timeString [$timeToHHMMSSString value=[:pick $value 7 15]];
                      } else={
#                        :put "not any of iso8601DateOnly, dateOnly, shortDateOnly, iso8601TimeOnly, timeOnly, iso8601DateTime, iso8601DateSpaceTime, dateTime, dateSpaceTime, shortDateTime, shortDateSpaceTime"
## foo
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }

  :if ($dateString = "") do={
    :set $dateString [$dateToYYYYMMDDString value=[/system clock get date]];
  }
  :if ($timeString = "") do={
    :set $timeString [$timeToHHMMSSString value=[/system clock get time]];
  }
#:put "dateString=";
#$varDump value=$dateString;
#:put "timeString=";
#$varDump value=$timeString;

  :local result ($dateString.$timeString);
#:put "result=";
#$varDump value=$result;
  return $result;
}

## Examples:
## /import scripts/Function.dateTimeToYYYYMMDDhhmmssString.rsc
## :put [$dateTimeToYYYYMMDDhhmmssString value=([/system clock get date] . [/system clock get time])]
## :put [$dateTimeToYYYYMMDDhhmmssString value=([/system clock get time])]
## :put [$dateTimeToYYYYMMDDhhmmssString value=([/system clock get date])]
## :put [$dateTimeToYYYYMMDDhhmmssString value="oct/13/2016"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="oct/13"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="jan/03"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="jan/03/2016"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="jan/03/201607:06:09"]
## 20160103070609
## :put [$dateTimeToYYYYMMDDhhmmssString value="07:06:09"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="jan/03/2016"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="oct/14 00:19:51"]
## 20161014001951
## :put [$dateTimeToYYYYMMDDhhmmssString value="oct/14/2016 09:48:25"]
## 20161014094825
## :put [$dateTimeToYYYYMMDDhhmmssString value="20161231"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="oct/14/2016"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="oct/14"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="012345"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="17:37:09"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="20161231012345"]
## 20161231012345
## :put [$dateTimeToYYYYMMDDhhmmssString value="20161231 012345"]
## 20161231012345
## :put [$dateTimeToYYYYMMDDhhmmssString value="oct/13/201617:37:09"]
## 20161013173709
## :put [$dateTimeToYYYYMMDDhhmmssString value="oct/13/2016 17:37:09"]
## 20161013173709
## :put [$dateTimeToYYYYMMDDhhmmssString value="oct/1317:37:09"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="oct/13 17:37:09"]
## :put [$dateTimeToYYYYMMDDhhmmssString value="foo"]


File: /scripts\Function.dateToYYYYMMDDString.rsc
/system script environment remove [find where name="dateToYYYYMMDDString"];
:global dateToYYYYMMDDString do={
## returns a string YYYYMMDD representation of the Date string in $value
## $value can either be either in ISO-8601 (yyyymmdd) long (mmm/dd/yyyy) or short (mmm/dd) Mikrotik format. If short, then the current year is used in yyyy.
## if $value has an invalid date, then [/system clock get date] is used

## maybe TODO: ensure the various parts are valid:
## - month is valid
## - day of the month is valid (0..27 extended by max days in month)

#  /system script environment get varDump
#  :global varDump;

#:put "value=";
#$varDump value=$value;

## unlike POSIX, character classes like [:digit:] are not supported in regular expressions http://forum.mikrotik.com/viewtopic.php?f=9&t=113422
## unlike POSIX regex, you have to escape the $ here "because Mikrotik scripting language"
#  :local dateOnlyMask "^[a-zA-Z]{3}/[:digit:]{2}/[0-9]{4}\$";
  :local iso8601DateOnlyMask "^[0-9]{4}[0-9]{2}[0-9]{2}\$";
  :local dateOnlyMask "^[a-zA-Z]{3}/[0-9]{2}/[0-9]{4}\$";
  :local shortDateOnlyMask "^[a-zA-Z]{3}/[0-9]{2}\$";

  :local varDay;
  :local varMonth;
  :local varYear;

  :if ($value~$iso8601DateOnlyMask) do={
#    :put "iso8601DateOnly";
## now we have a valid date formatted like this:
##   20161013
##   012345678 index mod 10 for data
    :return $value;
## for future range checking:
##    :set $varYear [:pick $value 0 4];
##    :set $varMonth [:pick $value 4 6];
##    :set $varDay [:pick $value 6 8];
#:put "varYear=";
#$varDump value=$varYear;
#:put "varMonth=";
#$varDump value=$varMonth;
#:put "varDay=";
#$varDump value=$varDay;
  } else={
    :local date
    :if ($value~$dateOnlyMask) do={
#      :put "dateOnly";
      :set $date ($value);
    } else={
      :if ($value~$shortDateOnlyMask) do={
#          :put "shortDateOnly";
##       /log print where buffer=failedauth
##       oct/14 00:19:51 system,error,critical login failure for user root from 201.217.248.217 via telnet
##       012 45 78 01 34   index mod 10 for data
##          3  6  9  2  5  index mod 10 for separators
        :local currentDate [/system clock get date]
        :local currentYear [:pick $currentDate 7 11]
        :local shortDatePart [:pick $value 0 6]
        :set $date ($shortDatePart."/$currentYear");
      } else={
#        :put "not any of iso8601DateOnly, dateOnly, shortDateOnly"
        :set $date ([/system clock get date]);
      };
    };
#:put "date=";
#$varDump value=$date;
##   now we have a valid date formatted like this:
##   oct/13/2016
##   012 45 78901 index mod 10 for data
##      3  6      index mod 10 for separators
    :local months [:toarray "jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec"]
    :local varMonthString [:pick $date 0 3];
    :local varMonthPosition [:find $months $varMonthString -1];
    :set $varMonth ($varMonthPosition + 1);
#:put "months=";
#$varDump value=$months;
#:put "varMonthString=";
#$varDump value=$varMonthString;
#:put "varMonthPosition=";
#$varDump value=$varMonthPosition;
#:put "varMonth=";
#$varDump value=$varMonth;
    :if ($varMonth < 10) do={
      :set varMonth ("0" . $varMonth);
#:put "varMonth=";
#$varDump value=$varMonth;
    }
    :set $varDay [:pick $date 4 6];
    :set $varYear [:pick $date 7 11];
#:put "varDay=";
#$varDump value=$varDay;
#:put "varYear=";
#$varDump value=$varYear;
  };

  :local result ($varYear.$varMonth.$varDay);

#:put "result=";
#$varDump value=$result;
  :return $result;
};

## Examples:
## /import scripts/Function.dateToYYYYMMDDString.rsc
## :put [$dateToYYYYMMDDString value=([/system clock get date])]
## :put [$dateToYYYYMMDDString value="oct/13/2016"]
## 20161013
## :put [$dateToYYYYMMDDString value="oct/13"]
## 20161013
## :put [$dateToYYYYMMDDString value="foo"]
## :put [$dateToYYYYMMDDString value="jan/03"]
## 20160103
## :put [$dateToYYYYMMDDString value="jan/03/2016"]
## 20160103
## :put [$dateToYYYYMMDDString value="oct/14"]
## 20161014
## :put [$dateToYYYYMMDDString value="oct/14/2016"]
## 20161014


File: /scripts\Function.endsWithString.rsc
/system script environment remove [ find where name="endsWithString" ];
:global endsWithString do={
  ## returns true if $value ends with $subString

#global varDump

#:put "value="
#$varDump value=$value
#:put "subString="
#$varDump value=$subString

  :local result false
#:put "result="
#$varDump value=$result

  :if ([:typeof $value] = "str") do={
    :if ([:typeof $subString] = "str") do={
      :local valueLength [:len $value]
      :local subStringLength [:len $subString]
      :if ($valueLength > $subStringLength) do={
## strings start at position zero (0)!
## 01234
## ABCDE -> length 5
## DE -> length 2; positions 3..4

        :local valueStart ($valueLength - $subStringLength)
        ## bug that won't be fixed: :pick end parameter is 1-based, not 0-based http://forum.mikrotik.com/viewtopic.php?t=108311
        ## :local valueEnd ($valueLength - 1)
        :local valueEnd ($valueLength - 0)
        :local valuePick [:pick $value $valueStart $valueEnd]
#:put "valueStart="
#$varDump value=$valueStart
#:put "valueEnd="
#$varDump value=$valueEnd
#:put "valuePick="
#$varDump value=$valuePick
        :set $result ($subString = $valuePick)
      }
    }
  };

#:put "result="
#$varDump value=$result
  :return $result;
}

## Examples:
## /import scripts/Function.endsWithString.rsc
## :put [$endsWithString value="ABCDE"]
## false
## :put [$endsWithString value="ABCDE" subString=(7)]
## false
## :put [$endsWithString value="ABCDE" subString="DE"]
## true
## :put [$endsWithString value="ABCDE" subString="AB"]
## false


File: /scripts\Function.escapeString.rsc
/system script environment remove [ find where name="escapeString" ];
## First try at https://gist.github.com/jpluimers/f667af4696d2a6411be44df1eeda2c2f
:global escapeString do={
  ## convert non-printable characters in $value to HEX-escaped compatible with the Scripting Language
  ## string loop based on URL encoding in http://forum.mikrotik.com/viewtopic.php?t=84705
  :local result "";
## set empty associative array: http://forum.mikrotik.com/viewtopic.php?p=418796#p549154
  :local convert ({})
## special as this is non-printable as well
  :set ($convert->("\7F")) ("\\7F")
##generated >>
  :set ($convert->("\00")) ("\\00")
  :set ($convert->("\01")) ("\\01")
  :set ($convert->("\02")) ("\\02")
  :set ($convert->("\03")) ("\\03")
  :set ($convert->("\04")) ("\\04")
  :set ($convert->("\05")) ("\\05")
  :set ($convert->("\06")) ("\\06")
  :set ($convert->("\07")) ("\\07")
  :set ($convert->("\08")) ("\\08")
  :set ($convert->("\09")) ("\\09")
  :set ($convert->("\00")) ("\\00")
  :set ($convert->("\0A")) ("\\0A")
  :set ($convert->("\0B")) ("\\0B")
  :set ($convert->("\0C")) ("\\0C")
  :set ($convert->("\0D")) ("\\0D")
  :set ($convert->("\0E")) ("\\0E")
  :set ($convert->("\0F")) ("\\0F")
  :set ($convert->("\10")) ("\\10")
  :set ($convert->("\11")) ("\\11")
  :set ($convert->("\12")) ("\\12")
  :set ($convert->("\13")) ("\\13")
  :set ($convert->("\14")) ("\\14")
  :set ($convert->("\15")) ("\\15")
  :set ($convert->("\16")) ("\\16")
  :set ($convert->("\17")) ("\\17")
  :set ($convert->("\18")) ("\\18")
  :set ($convert->("\19")) ("\\19")
  :set ($convert->("\10")) ("\\10")
  :set ($convert->("\1A")) ("\\1A")
  :set ($convert->("\1B")) ("\\1B")
  :set ($convert->("\1C")) ("\\1C")
  :set ($convert->("\1D")) ("\\1D")
  :set ($convert->("\1E")) ("\\1E")
  :set ($convert->("\1F")) ("\\1F")
  :set ($convert->("\80")) ("\\80")
  :set ($convert->("\81")) ("\\81")
  :set ($convert->("\82")) ("\\82")
  :set ($convert->("\83")) ("\\83")
  :set ($convert->("\84")) ("\\84")
  :set ($convert->("\85")) ("\\85")
  :set ($convert->("\86")) ("\\86")
  :set ($convert->("\87")) ("\\87")
  :set ($convert->("\88")) ("\\88")
  :set ($convert->("\89")) ("\\89")
  :set ($convert->("\80")) ("\\80")
  :set ($convert->("\8A")) ("\\8A")
  :set ($convert->("\8B")) ("\\8B")
  :set ($convert->("\8C")) ("\\8C")
  :set ($convert->("\8D")) ("\\8D")
  :set ($convert->("\8E")) ("\\8E")
  :set ($convert->("\8F")) ("\\8F")
  :set ($convert->("\90")) ("\\90")
  :set ($convert->("\91")) ("\\91")
  :set ($convert->("\92")) ("\\92")
  :set ($convert->("\93")) ("\\93")
  :set ($convert->("\94")) ("\\94")
  :set ($convert->("\95")) ("\\95")
  :set ($convert->("\96")) ("\\96")
  :set ($convert->("\97")) ("\\97")
  :set ($convert->("\98")) ("\\98")
  :set ($convert->("\99")) ("\\99")
  :set ($convert->("\90")) ("\\90")
  :set ($convert->("\9A")) ("\\9A")
  :set ($convert->("\9B")) ("\\9B")
  :set ($convert->("\9C")) ("\\9C")
  :set ($convert->("\9D")) ("\\9D")
  :set ($convert->("\9E")) ("\\9E")
  :set ($convert->("\9F")) ("\\9F")
  :set ($convert->("\00")) ("\\00")
  :set ($convert->("\01")) ("\\01")
  :set ($convert->("\02")) ("\\02")
  :set ($convert->("\03")) ("\\03")
  :set ($convert->("\04")) ("\\04")
  :set ($convert->("\05")) ("\\05")
  :set ($convert->("\06")) ("\\06")
  :set ($convert->("\07")) ("\\07")
  :set ($convert->("\08")) ("\\08")
  :set ($convert->("\09")) ("\\09")
  :set ($convert->("\00")) ("\\00")
  :set ($convert->("\0A")) ("\\0A")
  :set ($convert->("\0B")) ("\\0B")
  :set ($convert->("\0C")) ("\\0C")
  :set ($convert->("\0D")) ("\\0D")
  :set ($convert->("\0E")) ("\\0E")
  :set ($convert->("\0F")) ("\\0F")
  :set ($convert->("\A0")) ("\\A0")
  :set ($convert->("\A1")) ("\\A1")
  :set ($convert->("\A2")) ("\\A2")
  :set ($convert->("\A3")) ("\\A3")
  :set ($convert->("\A4")) ("\\A4")
  :set ($convert->("\A5")) ("\\A5")
  :set ($convert->("\A6")) ("\\A6")
  :set ($convert->("\A7")) ("\\A7")
  :set ($convert->("\A8")) ("\\A8")
  :set ($convert->("\A9")) ("\\A9")
  :set ($convert->("\A0")) ("\\A0")
  :set ($convert->("\AA")) ("\\AA")
  :set ($convert->("\AB")) ("\\AB")
  :set ($convert->("\AC")) ("\\AC")
  :set ($convert->("\AD")) ("\\AD")
  :set ($convert->("\AE")) ("\\AE")
  :set ($convert->("\AF")) ("\\AF")
  :set ($convert->("\B0")) ("\\B0")
  :set ($convert->("\B1")) ("\\B1")
  :set ($convert->("\B2")) ("\\B2")
  :set ($convert->("\B3")) ("\\B3")
  :set ($convert->("\B4")) ("\\B4")
  :set ($convert->("\B5")) ("\\B5")
  :set ($convert->("\B6")) ("\\B6")
  :set ($convert->("\B7")) ("\\B7")
  :set ($convert->("\B8")) ("\\B8")
  :set ($convert->("\B9")) ("\\B9")
  :set ($convert->("\B0")) ("\\B0")
  :set ($convert->("\BA")) ("\\BA")
  :set ($convert->("\BB")) ("\\BB")
  :set ($convert->("\BC")) ("\\BC")
  :set ($convert->("\BD")) ("\\BD")
  :set ($convert->("\BE")) ("\\BE")
  :set ($convert->("\BF")) ("\\BF")
  :set ($convert->("\C0")) ("\\C0")
  :set ($convert->("\C1")) ("\\C1")
  :set ($convert->("\C2")) ("\\C2")
  :set ($convert->("\C3")) ("\\C3")
  :set ($convert->("\C4")) ("\\C4")
  :set ($convert->("\C5")) ("\\C5")
  :set ($convert->("\C6")) ("\\C6")
  :set ($convert->("\C7")) ("\\C7")
  :set ($convert->("\C8")) ("\\C8")
  :set ($convert->("\C9")) ("\\C9")
  :set ($convert->("\C0")) ("\\C0")
  :set ($convert->("\CA")) ("\\CA")
  :set ($convert->("\CB")) ("\\CB")
  :set ($convert->("\CC")) ("\\CC")
  :set ($convert->("\CD")) ("\\CD")
  :set ($convert->("\CE")) ("\\CE")
  :set ($convert->("\CF")) ("\\CF")
  :set ($convert->("\D0")) ("\\D0")
  :set ($convert->("\D1")) ("\\D1")
  :set ($convert->("\D2")) ("\\D2")
  :set ($convert->("\D3")) ("\\D3")
  :set ($convert->("\D4")) ("\\D4")
  :set ($convert->("\D5")) ("\\D5")
  :set ($convert->("\D6")) ("\\D6")
  :set ($convert->("\D7")) ("\\D7")
  :set ($convert->("\D8")) ("\\D8")
  :set ($convert->("\D9")) ("\\D9")
  :set ($convert->("\D0")) ("\\D0")
  :set ($convert->("\DA")) ("\\DA")
  :set ($convert->("\DB")) ("\\DB")
  :set ($convert->("\DC")) ("\\DC")
  :set ($convert->("\DD")) ("\\DD")
  :set ($convert->("\DE")) ("\\DE")
  :set ($convert->("\DF")) ("\\DF")
  :set ($convert->("\E0")) ("\\E0")
  :set ($convert->("\E1")) ("\\E1")
  :set ($convert->("\E2")) ("\\E2")
  :set ($convert->("\E3")) ("\\E3")
  :set ($convert->("\E4")) ("\\E4")
  :set ($convert->("\E5")) ("\\E5")
  :set ($convert->("\E6")) ("\\E6")
  :set ($convert->("\E7")) ("\\E7")
  :set ($convert->("\E8")) ("\\E8")
  :set ($convert->("\E9")) ("\\E9")
  :set ($convert->("\E0")) ("\\E0")
  :set ($convert->("\EA")) ("\\EA")
  :set ($convert->("\EB")) ("\\EB")
  :set ($convert->("\EC")) ("\\EC")
  :set ($convert->("\ED")) ("\\ED")
  :set ($convert->("\EE")) ("\\EE")
  :set ($convert->("\EF")) ("\\EF")
  :set ($convert->("\F0")) ("\\F0")
  :set ($convert->("\F1")) ("\\F1")
  :set ($convert->("\F2")) ("\\F2")
  :set ($convert->("\F3")) ("\\F3")
  :set ($convert->("\F4")) ("\\F4")
  :set ($convert->("\F5")) ("\\F5")
  :set ($convert->("\F6")) ("\\F6")
  :set ($convert->("\F7")) ("\\F7")
  :set ($convert->("\F8")) ("\\F8")
  :set ($convert->("\F9")) ("\\F9")
  :set ($convert->("\F0")) ("\\F0")
  :set ($convert->("\FA")) ("\\FA")
  :set ($convert->("\FB")) ("\\FB")
  :set ($convert->("\FC")) ("\\FC")
  :set ($convert->("\FD")) ("\\FD")
  :set ($convert->("\FE")) ("\\FE")
  :set ($convert->("\FF")) ("\\FF")
## generated <<
#  :put "$convert"
#  :put "value=$value"
  :for i from=0 to=([:len $value] - 1) do={
    :local char [:pick $value $i]
    :local converted ($convert->"$char")
    :local convertedType [:typeof $converted]
#    :put "$char $converted $convertedType"
    :if ($convertedType = "str") do={
      :set $char $converted
    }
    :set result ($result.$char)
  }
#  :put "result=$result"
  :return $result;
}

## Example:
## /import scripts/Function.escapeString.rsc
## :put [$escapeString value=("f o\00\01\7E\7F\80\81\FE\FFo")]
## f o\00\01~\7F\80\81\FE\FFo


File: /scripts\Function.isValidIPv4.rsc
/system script environment remove [ find where name="isValidIPv4" ];
:global isValidIPv4 do={
## returns true if $value is a valid quad-dotted IPv4 address without taking into account:
## - subnetting issues like https://en.wikipedia.org/wiki/IPv4#Addresses_ending_in_0_or_255
## - non-decimal parts in the quads (so a leading zero in a quad is allowed but does not mean an octal)
## - non-quad-dotted representations (like a full decimal or full octal representation)
## - other varieties that https://linux.die.net/man/3/inet_addr accepts.

## TODO: consider using the `:toip` function mentioned but not documented at http://wiki.mikrotik.com/wiki/Manual:Scripting
## as IPv4 isn't always quad-dotted decimal: http://forum.mikrotik.com/viewtopic.php?f=9&t=114099
## `:toip` example usage at:
## - http://wiki.mikrotik.com/wiki/Converting_network_and_gateway_from_routing_table_to_hexadecimal_string
## - http://wiki.mikrotik.com/wiki/Sync_Address_List_with_DNS_Cache
## - http://forum.mikrotik.com/viewtopic.php?t=85205
## Maybe do a parse as well to distinguish between `ip` and `ip-prefix`
## - http://forum.mikrotik.com/viewtopic.php?t=70574

#:global varDump;

#$varDump value=$value name="value";

  :local IPv4 ("$value");
# via https://stackoverflow.com/questions/106179/regular-expression-to-match-dns-hostname-or-ip-address/106223#106223
# note the backslash escapes so \\. escapes into \. which matches the . literal and \$ expands into $
  :local validIPv4RegularExpression "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\$";
## if you forget the \$ escape, then you get strange errors like on the below line "expected end of command (line 19 column 28)"

#$varDump value=$IPv4 name="IPv4";
#$varDump value=$validIPv4RegularExpression name="validIPv4RegularExpression";

  :local result ($IPv4 ~ $validIPv4RegularExpression);

#$varDump value=$result name="result";
  :return $result;
}

## Examples:
## /import scripts/Function.isValidIPv4.rsc
## :put [$isValidIPv4 value=1.2.3.4]
## true
## :put [$isValidIPv4 value="1.2.3.4"]
## true
## :put [$isValidIPv4 value="0"]
## :put [$isValidIPv4 value="0.0"]
## :put [$isValidIPv4 value="0.0.0"]
## :put [$isValidIPv4 value="0.0.0.0"]
## true
## :put [$isValidIPv4 value="1111"]
## :put [$isValidIPv4 value="1111.1111"]
## :put [$isValidIPv4 value="1111.1111.1111"]
## :put [$isValidIPv4 value="1111.1111.1111.1111"]
## :put [$isValidIPv4 value="255"]
## :put [$isValidIPv4 value="255.255"]
## :put [$isValidIPv4 value="255.255.255"]
## :put [$isValidIPv4 value="255.255.255.255"]
## true
## :put [$isValidIPv4 value="0255"]
## :put [$isValidIPv4 value="0255.0255"]
## :put [$isValidIPv4 value="0255.0255.0255"]
## :put [$isValidIPv4 value="0255.0255.0255.0255"]


File: /scripts\Function.padLeftString.rsc
:global padLeftString do={
  ## returns $value padded left with $padChar (space when left out) up to a $padLength length
  ## if $padLength is not defined or less than [:len $value], then returns $value

# :global varDump

# :put "value="
# $varDump value=$value
# :put "padChar="
# $varDump value=$padChar
# :put "padLength="
# $varDump value=$padLength

  :local result "$value"
  :local valueLength [:len $value]
  :local paddingCount 0
  :if ([:typeof $padLength] = "num") do={
    :if ($padLength > $valueLength) do={
      :set $paddingCount ($padLength - $valueLength)
    }
  };
  :local padding " "
  :if ([:typeof $padChar] = "str") do={
    :if ([:len $padChar] = 1) do={
      :set $padding $padChar
    }
  };

# :put "result="
# $varDump value=$result
# :put "valueLength="
# $varDump value=$valueLength
# :put "paddingCount="
# $varDump value=$paddingCount
# :put "padding="
# $varDump value=$padding

  :if ($paddingCount  > 0) do={
    :for i from=1 to=$paddingCount do={
# :put "$i"
      :set result ($padding.$result)
    }
  }
  :return $result;
}

## Examples: (note the parenthsis around the numbers!)
## /import scripts/Function.padLeftString.rsc
## :put [$padLeftString value="12345"]
## 12345
## :put [$padLeftString value="12345" padLength=(7)]
##   12345
## :put [$padLeftString value="12345" padLength=(7) padChar="."]
## ..12345


File: /scripts\Function.padRightString.rsc
:global padRightString do={
  ## returns $value padded right with $padChar (space when Right out) up to a $padLength length
  ## if $padLength is not defined or less than [:len $value], then returns $value

# :global varDump

# :put "value="
# $varDump value=$value
# :put "padChar="
# $varDump value=$padChar
# :put "padLength="
# $varDump value=$padLength

  :local result "$value"
  :local valueLength [:len $value]
  :local paddingCount 0
  :if ([:typeof $padLength] = "num") do={
    :if ($padLength > $valueLength) do={
      :set $paddingCount ($padLength - $valueLength)
    }
  };
  :local padding " "
  :if ([:typeof $padChar] = "str") do={
    :if ([:len $padChar] = 1) do={
      :set $padding $padChar
    }
  };

# :put "result="
# $varDump value=$result
# :put "valueLength="
# $varDump value=$valueLength
# :put "paddingCount="
# $varDump value=$paddingCount
# :put "padding="
# $varDump value=$padding

  :if ($paddingCount  > 0) do={
    :for i from=1 to=$paddingCount do={
# :put "$i"
      :set result ($result.$padding)
    }
  }
  :return $result;
}

## Examples: (note the parenthsis around the numbers!)
## /import scripts/Function.padRightString.rsc
## :put [$padRightString value="12345"]
## 12345
## :put [$padRightString value="12345" padLength=(7)]
## 12345
## :put [$padRightString value="12345" padLength=(7) padChar="."]
## 12345..


File: /scripts\Function.startsWithString.rsc
/system script environment remove [ find where name="startsWithString" ];
:global startsWithString do={
  ## returns true if $value starts with $subString

#global varDump

#:put "value="
#$varDump value=$value
#:put "subString="
#$varDump value=$subString

  :local result false
#:put "result="
#$varDump value=$result

  :if ([:typeof $value] = "str") do={
    :if ([:typeof $subString] = "str") do={
      :local valueLength [:len $value]
      :local subStringLength [:len $subString]
      :if ($valueLength > $subStringLength) do={
## strings start at position zero (0)!
## 01234
## ABCDE -> length 5
## AB -> length 2; positions 0..1

        :local valueStart (0)
        # bug that won't be fixed: :pick end parameter is 1-based, not 0-based http://forum.mikrotik.com/viewtopic.php?t=108311
        # :local valueEnd ($subStringLength - 1)
        :local valueEnd ($subStringLength - 0)
        :local valuePick [:pick $value $valueStart $valueEnd]
#:put "valueStart="
#$varDump value=$valueStart
#:put "valueEnd="
#$varDump value=$valueEnd
#:put "valuePick="
#$varDump value=$valuePick
        :set $result ($subString = $valuePick)
      }
    }
  };

#:put "result="
#$varDump value=$result
  :return $result;
}

## Examples:
## /import scripts/Function.startsWithString.rsc
## :put [$startsWithString value="ABCDE"]
## false
## :put [$startsWithString value="ABCDE" subString=(7)]
## false
## :put [$startsWithString value="ABCDE" subString="DE"]
## false
## :put [$startsWithString value="ABCDE" subString="AB"]
## true


File: /scripts\Function.stripInvalidHostNameCharactersFromString.rsc
/system script environment remove [ find where name="stripInvalidHostNameCharactersFromString" ];
:global stripInvalidHostNameCharactersFromString do={
  ## returns $value without invalid characters for a Hostname
  ## if $allowMultipleLabels is not nothing, then it also allows dots between labels
#  :put "$value"
#  :put "$allowMultipleLabels"
  ## https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_host_names
  ## valid: a..z A..Z 0..9 -
  ## for convenience, replace space and underscore with hyphen.
  ## string loop based on URL encoding in http://forum.mikrotik.com/viewtopic.php?t=84705
  :local result "";
  ## set empty associative array: http://forum.mikrotik.com/viewtopic.php?p=418796#p549154
  :local convert ({})
  :if ([:typeof $allowMultipleLabels] != "nothing") do={
    # allow multiple labels in a host name
    :set ($convert->(".")) (".")
  };
  :local validChars "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890-"
  :for validCharsIndex from=0 to=([:len $validChars] - 1) do={
    :local validChar [:pick $validChars $validCharsIndex]
    :set ($convert->($validChar)) ($validChar)
  }
  ## for convenience, translate space and underscore to hyphen
  :set ($convert->("_")) ("-")
  :set ($convert->(" ")) ("-")
#  :put "$convert"

  :for i from=0 to=([:len $value] - 1) do={
    :local char [:pick $value $i]
    :local converted ($convert->"$char")
    :local convertedType [:typeof $converted]
#    :put "$char $converted $convertedType"
    :if ($convertedType = "str") do={
      :set $char $converted
    } else={
      :set $char ""
    }
    :set result ($result.$char)
  }
  :return $result;
}

## Example:
## /import scripts/Function.stripInvalidHostNameCharactersFromString.rsc
## :put [$stripInvalidHostNameCharactersFromString value=("a#host#name")]
## ahostname
## :put [$stripInvalidHostNameCharactersFromString value=("a@host/name.domain name" ) allowMultipleLabels="yes"]
## ahostname.domainname


File: /scripts\Function.systemScriptJobCountTypeIsCommand.rsc
:local scriptName "Function.systemScriptJobCountTypeIsCommand.rsc"
/system script environment remove [ find where name="systemScriptJobCountTypeIsCommand" ];
## First try at https://gist.github.com/jpluimers/f667af4696d2a6411be44df1eeda2c2f
:global systemScriptJobCountTypeIsCommand do={
  :local result [:len [/system script job find where type=command]];
#  :put "result=$result"
  :return $result;
}

## Example:
## /import scripts/Function.systemScriptJobCountTypeIsCommand.rsc
## :put [$systemScriptJobCountTypeIsCommand];


File: /scripts\Function.timeToHHMMSSString.rsc
/system script environment remove [find where name="timeToHHMMSSString"];
:global timeToHHMMSSString do={
## returns a string hhmmss representation of the Time string in $value
## $value can either be either in ISO-8601 (hhmmss) Mikrotik (hh:mm:ss) format.
## if $value has an invalid time, then [/system clock get time] is used

## maybe TODO: ensure the various parts are valid:
## - hour in range 0..23
## - minute in range 0..59
## - second in range 0..59

#  /system script environment get varDump
#  :global varDump;

#:put "value=";
#$varDump value=$value;

  :local varHour;
  :local varMinute;
  :local varSecond;

## unlike POSIX, character classes like [:digit:] are not supported in regular expressions http://forum.mikrotik.com/viewtopic.php?f=9&t=113422
## unlike POSIX regex, you have to escape the $ here "because Mikrotik scripting language"
# :local timeOnlyMask "^[0-9]{2}:[:digit:]{2}:[0-9]{2}\$";
  :local timeOnlyMask "^[0-9]{2}:[0-9]{2}:[0-9]{2}\$";
  :local iso8601TimeOnlyMask "^[0-9]{2}[0-9]{2}[0-9]{2}\$";

  :if ($value~$iso8601TimeOnlyMask) do={
#    :put "iso8601TimeOnly";
## hhmmss
## 0123456 index mod 10 for data
##         index mod 10 for separators
    :return $value;
## for future range checking:
##    :set $varHour [:pick $value 0 2];
##    :set $varMinute [:pick $value 2 4];
##    :set $varSecond [:pick $value 4 6];
  } else={
    :local time;
    :if ($value~$timeOnlyMask) do={
#      :put "timeOnly";
      :set $time ($value);
    } else={
#        :put "not any of iso8601TimeOnly, timeOnly"
      :set $time ([/system clock get time]);
    };
#:put "time=";
#$varDump value=$time;
## hh:mm:ss
## 01 34 678 index mod 10 for data
##   2  5    index mod 10 for separators
    :set $varHour [:pick $time 0 2];
    :set $varMinute [:pick $time 3 5];
    :set $varSecond [:pick $time 6 8];
  };
#:put "varHour=";
#$varDump value=$varHour;
#:put "varMinute=";
#$varDump value=$varMinute;
#:put "varSecond=";
#$varDump value=$varSecond;

  :local result ($varHour.$varMinute.$varSecond);

#:put "result=";
#$varDump value=$result;
  :return $result;
};

## Examples:
## /import scripts/Function.timeToHHMMSSString.rsc
## :put [$timeToHHMMSSString value=([/system clock get time])]
## :put [$timeToHHMMSSString value="17:37:09"]
## 173709
## :put [$timeToHHMMSSString value="07:06:09"]
## 070609
## :put [$timeToHHMMSSString value="00:19:51"]
## 001951
## :put [$timeToHHMMSSString value="09:48:25"]
## 094825
## :put [$timeToHHMMSSString value="173709"]
## 173709
## :put [$timeToHHMMSSString value="070609"]
## 070609
## :put [$timeToHHMMSSString value="001951"]
## 001951
## :put [$timeToHHMMSSString value="094825"]
## 094825


File: /scripts\Function.timeToSecondsSinceMidnight.rsc
/system script environment remove [find where name="timeToSecondsSinceMidnight"];
:global timeToSecondsSinceMidnight do={

## $value can either be either in ISO-8601 (hhmmss) Mikrotik (hh:mm:ss) format.
## if $value has an invalid time, then [/system clock get time] is used

#  /system script environment get varDump
#  :global varDump;

#:put "value=";
#$varDump value=$value;

  :local varHour;
  :local varMinute;
  :local varSecond;

## unlike POSIX, character classes like [:digit:] are not supported in regular expressions http://forum.mikrotik.com/viewtopic.php?f=9&t=113422
## unlike POSIX regex, you have to escape the $ here "because Mikrotik scripting language"
# :local timeOnlyMask "^[0-9]{2}:[:digit:]{2}:[0-9]{2}\$";
  :local timeOnlyMask "^[0-9]{2}:[0-9]{2}:[0-9]{2}\$";
  :local iso8601TimeOnlyMask "^[0-9]{2}[0-9]{2}[0-9]{2}\$";

  :if ($value~$iso8601TimeOnlyMask) do={
#    :put "iso8601TimeOnly";
## hhmmss
## 0123456 index mod 10 for data
##         index mod 10 for separators
    :set $varHour [:pick $value 0 2];
    :set $varMinute [:pick $value 2 4];
    :set $varSecond [:pick $value 4 6];
  } else={
    :local time;
    :if ($value~$timeOnlyMask) do={
#      :put "timeOnly";
      :set $time ($value);
    } else={
#        :put "not any of iso8601TimeOnly, timeOnly"
      :set $time ([/system clock get time]);
    };
#:put "time=";
#$varDump value=$time;
## hh:mm:ss
## 01 34 678 index mod 10 for data
##   2  5    index mod 10 for separators
    :set $varHour [:pick $time 0 2];
    :set $varMinute [:pick $time 3 5];
    :set $varSecond [:pick $time 6 8];
  };
#:put "varHour=";
#$varDump value=$varHour;
#:put "varMinute=";
#$varDump value=$varMinute;
#:put "varSecond=";
#$varDump value=$varSecond;

  :local h [:tonum $varHour];
#:put "h=";
#$varDump value=$h;
  :local m [:tonum $varMinute];
#:put "m=";
#$varDump value=$m;
  :local s [:tonum $varSecond];
#:put "s=";
#$varDump value=$s;
  :local result (($h * 60 * 60) + ($m * 60) + $s);

#:put "result=";
#$varDump value=$result;
  :return $result;
};

## Examples:
## /import scripts/Function.timeToSecondsSinceMidnight.rsc
## :put [$timeToSecondsSinceMidnight value=([/system clock get time])]
## :put [$timeToSecondsSinceMidnight value="17:37:09"]
## 63429
## :put [$timeToSecondsSinceMidnight value="07:06:09"]
## 25569
## :put [$timeToSecondsSinceMidnight value="09:48:25"]
## 35305
## :put [$timeToSecondsSinceMidnight value="24:00:00"]
## 86400
## :put [$timeToSecondsSinceMidnight value="foo"]
## :put [$timeToSecondsSinceMidnight value="173709"]
## 63429
## :put [$timeToSecondsSinceMidnight value="070609"]
## 25569
## :put [$timeToSecondsSinceMidnight value="094825"]
## 35305
## :put [$timeToSecondsSinceMidnight value="240000"]
## 86400


File: /scripts\Function.toString.rsc
:local scriptName "Function.toString.rsc"
/system script environment remove [ find where name="toString" ];

:global toString do={
  ## for recursion
  :global toString;
  ## convert non-printable characters in $value to HEX-escaped compatible with the Scripting Language
  ## string loop based on URL encoding in http://forum.mikrotik.com/viewtopic.php?t=84705
  :local result "";
  :local infoMessage "$scriptName testing for function existence; if you get `no such item` then one or more dependencies fail; test with `/system script environment print` and `/system logging action print` if they are there."
#  :put "info: $infoMessage"

#  :put "$value"
  :local typeOfValue [:typeof $value]

  :if ($typeOfValue = "str") do={
    :set $result $value;
#    :put "str: $result"
  } else={
    :if ($typeOfValue = "array") do={
#      :put "$typeOfValue"
      :foreach key,element in=$value do={
        :if ($result != "") do={
          :set $result "$result,";
#          :put "comma: $result"
        }
        :local typeOfKey [:typeof $key];
        :if ($typeOfKey != "num") do={
          :local keyString [$toString value=$key];
          :set $result ($result."$keyString=");
#          :put "non-num key: $result"
        }
        :local elementString [$toString value=$element];
#        :put "element: $elementString=$element"
        :set $result ($result."$elementString");
#        :put "iteration: $result"
      };
    } else={
#      :put "typeOfValue: $typeOfValue"
      :if (($typeOfValue = "nothing") or ($typeOfValue = "nil")) do={
      } else={
        :set result "$value";
      }
    }
  }
#  :put "result=$result"
  :return $result;
}

## Example:
## /import scripts/Function.toString.rsc
##{
##  :global dateTimeToYYYYMMDDhhmmssNumber;
##  :global toString;
##  :foreach logEntry in=[/log print as-value where buffer="memory"] do={
##    :local logEntryTime ($logEntry->"time");
##    :local logEntryTopics ($logEntry->"topics");
##    :local logEntryMessage ($logEntry->"message");
##
##    :local logEntryDateTime [$dateTimeToYYYYMMDDhhmmssNumber value=$logEntryTime];
##    :local logEntryTopicsType [:typeof $logEntryTopics];
##    :local logEntryTopicsString [$toString value=$logEntryTopics];
##    :put "$logEntryDateTime;$logEntryTime;$logEntryMessage;$logEntryTopicsType;$logEntryTopicsString";
##  }
##}


File: /scripts\Generate-convert-set-statements-for.Function.escapeString.rsc
## initialise as empty array as the MikroTik RouterOS scripting language has a bug initialising
## assosiative arrays when they contain hex escapes like `:global convert {"\00"="\\00"}`
## see http://forum.mikrotik.com/viewtopic.php?f=9&t=108107&sid=74f5fd6f4b0e376b1eb6338ccb2f5ec2
:global convert ({})

## now add all the characters that need to be escaped:
#:set ($convert->"\00") "\\00"
:set ($convert->"\7F") "\\7F"
:set ($convert->"\81") "\\81"
:local hexChars "01234567890ABCDEF"
:local groupChars "01890ABCDEF"
:for groupCharsIndex from=0 to=([:len $groupChars] - 1) do={
  :local groupChar [:pick $groupChars $groupCharsIndex]
  :for hexCharsIndex from=0 to=([:len $hexChars] - 1) do={
    :local hexChar [:pick $hexChars $hexCharsIndex]
    ## the `:put` statements will output the formatted code for initialisation in `Function.escapeString.rsc`:
    :put ":set (\$convert->(\"\\$groupChar$hexChar\")) (\"\\\\$groupChar$hexChar\")"
  }
}

## for debugging/research purposes:
:put [/system script environment print]
:put [:typeof $convert]
:put "$convert"
:put ($convert->"\00")
:put ($convert->"\81")
:put ($convert->"f")
:put [:typeof ($convert->"\00")]
:put [:typeof ($convert->"\81")]
:put [:typeof ($convert->"f")]


File: /scripts\import.file-scripts-functions-procedures.rsc
## Imports all Function.*.rsc and Procedure.*.rsc files from the /scripts directory
## so they can be used and listed as `/system script environment print`

## Emit output to both console and log.

## inspired by http://forum.mikrotik.com/viewtopic.php?t=75081#p477543 (Re: Functions and function parameters)

## Match scripts in `scripts/` folder ending with `.rsc` and starting with `Function.` or `Procedure.`

## Run by copying this script into the `scripts/` folder then running this from the terminal:

## `/import scripts/import.file-scripts-functions-procedures.rsc`

## Note in order to call a `:local` method from another method, it needs to be `:local` inside that other method.

:local importScriptsInScriptsDirectoryStartingWith do={
  :local importScriptsByPattern do={
    # imports scripts matching $value pattern
    :local logLine "Importing scripts matching pattern '$value'"
    :put $logLine
    :log info $logLine

    :local count 0

    :foreach fileId in [/file find where name~"$value"] do={
      :local fileName [/file get $fileId name]
      :local fileType [/file get $fileId type]
      :local fileSize [/file get $fileId size]
      :local fileSizeType [:typeof $fileSize]
      :local logLine "Importing script: $fileSize bytes ($fileSizeType), type $fileType: '$fileName'"
      :put $logLine
      :log info $logLine
      /import $fileName
      :set $count ($count + 1)
    }
    :if ($count = 0) do={
      :local logLine "No scripts matching pattern '$value'"
      :put $logLine
      :log info $logLine
    }
  }

  $importScriptsByPattern value=("^scripts/$value.*\\.rsc\$")
}

## start in the root so the outer `eval` in each function doesn't include the full path to where we were.
/

$importScriptsInScriptsDirectoryStartingWith value=("Function\\.")
$importScriptsInScriptsDirectoryStartingWith value=("Procedure\\.")

# Example:
# /import scripts/import.file-scripts-functions-procedures.rsc


File: /scripts\list.systemScript.file-subdirectory-scripts.rsc
## can be executed as one-liner
## it lists size, typeof size, type and name of each file
#:foreach fileId in [/file find] do={ :local fileName [/file get $fileId name]; :local fileType [/file get $fileId type]; :local fileSize [/file get $fileId size]; :local fileSizeType [:typeof $fileSize]; :put "$fileSize bytes ($fileSizeType), type $fileType: '$fileName'" }

## Match anything
:foreach fileId in [/file find where name~".*"] do={ :local fileName [/file get $fileId name]; :local fileType [/file get $fileId type]; :local fileSize [/file get $fileId size]; :local fileSizeType [:typeof $fileSize]; :put "$fileSize bytes ($fileSizeType), type $fileType: '$fileName'" }

## Match starting with "scripts/Function."
:foreach fileId in [/file find where name~"^scripts\\/\\Function\\..*"] do={ :local fileName [/file get $fileId name]; :local fileType [/file get $fileId type]; :local fileSize [/file get $fileId size]; :local fileSizeType [:typeof $fileSize]; :put "$fileSize bytes ($fileSizeType), type $fileType: '$fileName'" }
## inspired by http://forum.mikrotik.com/viewtopic.php?t=75081#p477543 (Re: Functions and function parameters)

## Example:
## /import scripts/list.systemScript.file-subdirectory-scripts.rsc


File: /scripts\list.systemScript.lengthName.rsc
## can be executed as one-liner
## see http://forum.mikrotik.com/viewtopic.php?f=9&t=108405#p538221 (Is there a good way to sync a local directory from the scripts that a Mikrotik has? - MikroTik RouterOS)

## Match anything
:foreach scriptId in [/system script find] do={ :local scriptSource [/system script get $scriptId source]; :local scriptSourceLength [:len $scriptSource];  :local scriptName [/system script get $scriptId name]; :put "$scriptSourceLength bytes: '$scriptName'" }

## Example:
## /import scripts/list.systemScript.lengthName.rsc


File: /scripts\Procedure.outputError.rsc
/system script environment remove [ find where name="outputError" ];
:global outputError do={
  ## outputs $value using both :put and :log info
  :put "error: $value"
  :log error "$value"
}

## Examples:
## /import scripts/Procedure.outputError.rsc

## > $outputError value="12345"
## > $outputError value=12345
## > $outputError value=(12345)


File: /scripts\Procedure.outputInfo.rsc
/system script environment remove [ find where name="outputInfo" ];
:global outputInfo do={
  ## outputs $value using both :put and :log info
  :put "info: $value"
  :log info "$value"
}

## Examples:
## /import scripts/Procedure.outputInfo.rsc

## > $outputInfo value="12345"
## > $outputInfo value=12345
## > $outputInfo value=(12345)


File: /scripts\Procedure.varDump.rsc
:local scriptName "Procedure.varDump.rsc"
/system script environment remove [ find where name="varDump" ];
:global varDump do={
  ## for recursion
  :global varDump
  ## performs various :put with information of $value
  ## indents output with parameter $indent
  ## appends indent with parameter $name
  ## inspired by http://php.net/manual/en/function.var-dump.php but RouterOS does not allow underscores in variables and functions
  ## requires Function.escapeString.rsc with function escapeString

  ## TODO: expand and add more examples from http://forum.mikrotik.com/viewtopic.php?t=91480

  :local infoMessage "$scriptName testing for function existence; if you get `no such item` then one or more dependencies fail; test with `/system script environment print` if they are there."
#  :put "info: $infoMessage"

  /system script environment get escapeString
  :global escapeString

  :local typeOfValue [:typeof $value]
  :local prefix ("$indent$name:typeof=$typeOfValue")

  :if ($typeOfValue = "str") do={
    :local valueLen [:len $value]
    :put "$prefix;len=$valueLen;\$value=$value"
    :local escaped [$escapeString value=$value]
    :if ($value != $escaped) do={
      :put "$indent\$value escaped='$escaped'"
    }
  } else={
    :if ($typeOfValue = "array") do={
      :local valueLen [:len $value]
      :put "$prefix;len=$valueLen"
      :foreach key,element in=$value do={
         $varDump value=$key indent=("  $indent")
        :local escapedKey [$escapeString value=("$key")]
         $varDump value=$element indent=("  $indent[$escapedKey]")
      };
    } else={
      :if (($typeOfValue = "nothing") or ($typeOfValue = "nil")) do={
        :put "$prefix"
      } else={
        :put "$prefix;\$value=$value"
      }
    }
  }
}

## Examples:
## /import scripts/Procedure.varDump.rsc

## > $varDump value="12345" name="foo"
## foo:typeof=str;len=5;$value=12345

## > $varDump value="12345"
## :typeof=str;len=5;$value=12345

## > $varDump value="12345"
## :typeof=str;len=5;$value=12345

### (yes, a value without parenthesis is considered a string)
## > $varDump value=12345
## :typeof=str;len=5;$value=12345

## > $varDump value=(12345)
## :typeof=num;$value=12345

## > $varDump
## :typeof=nothing

## > $varDump value=$fooBar
## :typeof=nothing

## > $varDump value=[$fooBar]
## :typeof=nil

##> $varDump value=({1;2;3} , 5 )
##:typeof=array;len=4
##  :typeof=num;$value=0
##  [0]:typeof=num;$value=1
##  :typeof=num;$value=1
##  [1]:typeof=num;$value=2
##  :typeof=num;$value=2
##  [2]:typeof=num;$value=3
##  :typeof=num;$value=3
##  [3]:typeof=num;$value=5

##> :local convert ({}); :set ($convert->("a\00")) ("A"); :set ($convert->("b")) ("B\01"); $varDump value=$convert;
##:typeof=array;len=2
##  :typeof=str;len=2;$value=a
##  $value escaped='a\00'
##  [a\00]:typeof=str;len=1;$value=A
##  :typeof=str;len=1;$value=b
##  [b]:typeof=str;len=2;$value=B
##  [b]$value escaped='B\01'


File: /scripts\README.rst
scripts
=======

There are lots of gotchas writing RouterOS scripts. The ones I found are documented inside the scripts. Hopefully I will have time in the future to write that up into a proper document.

For now you will have to do with the below information.

Some conventions used:

- method names start with lower case and are `camelCase <https://en.wikipedia.org/wiki/CamelCase>`_ starting with a lowercase character.
- descriptive/explanatory comments start with a double ``##``
- comments used while debugging start with a single ``#``
- explanation of each script is usually at the end of it

``:global`` functions that assist in various operations:

- `Function.civilDateTimeToSecondsSince19700101.rsc               <Function.civilDateTimeToSecondsSince19700101.rsc>`_
- `Function.civilDateToDaysSince19700101.rsc                      <Function.civilDateToDaysSince19700101.rsc>`_
- `Function.dateTimeToYYYYMMDDhhmmssNumber.rsc                    <Function.dateTimeToYYYYMMDDhhmmssNumber.rsc>`_
- `Function.dateTimeToYYYYMMDDhhmmssString.rsc                    <Function.dateTimeToYYYYMMDDhhmmssString.rsc>`_
- `Function.dateToYYYYMMDDString.rsc                              <Function.dateToYYYYMMDDString.rsc>`_
- `Function.endsWithString.rsc                                    <Function.endsWithString.rsc>`_
- `Function.escapeString.rsc                                      <Function.escapeString.rsc>`_
- `Function.padLeftString.rsc                                     <Function.padLeftString.rsc>`_
- `Function.padRightString.rsc                                    <Function.padRightString.rsc>`_
- `Function.startsWithString.rsc                                  <Function.startsWithString.rsc>`_
- `Function.stripInvalidHostNameCharactersFromString.rsc          <Function.stripInvalidHostNameCharactersFromString.rsc>`_
- `Function.timeToHHMMSSString.rsc                                <Function.timeToHHMMSSString.rsc>`_
- `Function.timeToSecondsSinceMidnight.rsc                        <Function.timeToSecondsSinceMidnight.rsc>`_
- `Function.toString.rsc                                          <Function.toString.rsc>`_

Helper:

- `Generate-convert-set-statements.for.Function.escapeString.rsc  <Generate-convert-set-statements.for.Function.escapeString.rsc>`_

Imports all ``.rsc`` files starting with ``Function.`` or ``Procedure``; run like this::

  /import scripts/import.file-scripts-functions-procedures.rsc

- `import.file-scripts-functions-procedures.rsc                   <import.file-scripts-functions-procedures.rsc>`_

Various utilities (not procedures or functions, so just start with ``/import``):

- `list.systemScript.file-subdirectory-scripts.rsc                <list.systemScript.file-subdirectory-scripts.rsc>`_
- `list.systemScript.lengthName.rsc                               <list.systemScript.lengthName.rsc>`_


