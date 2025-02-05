# Repository Information
Name: mikrotik-config-generator

# Directory Structure
Directory structure:
└── github_repos/mikrotik-config-generator/
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
    │   │       ├── pack-621d7a1ebcfd966041e293c02d59718d984ac10e.idx
    │   │       └── pack-621d7a1ebcfd966041e293c02d59718d984ac10e.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── mikrotik-config/
    │   ├── app.rc
    │   ├── AssemblyInfo.cpp
    │   ├── CmdGen.cpp
    │   ├── CmdGen.h
    │   ├── Form1.h
    │   ├── Form1.resx
    │   ├── mikrotik-config.cpp
    │   ├── mikrotik-config.vcproj
    │   ├── resource.h
    │   ├── Result.cpp
    │   ├── Result.h
    │   ├── stdafx.cpp
    │   └── stdafx.h
    ├── mikrotik-config.sln
    └── mikrotik-config.suo


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
	url = https://github.com/EmelyS3/mikrotik-config-generator.git
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
0000000000000000000000000000000000000000 8d967549742a7c530dade87ca442efa7d9652829 vivek-dodia <vivek.dodia@icloud.com> 1738606384 -0500	clone: from https://github.com/EmelyS3/mikrotik-config-generator.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 8d967549742a7c530dade87ca442efa7d9652829 vivek-dodia <vivek.dodia@icloud.com> 1738606384 -0500	clone: from https://github.com/EmelyS3/mikrotik-config-generator.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 8d967549742a7c530dade87ca442efa7d9652829 vivek-dodia <vivek.dodia@icloud.com> 1738606384 -0500	clone: from https://github.com/EmelyS3/mikrotik-config-generator.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
8d967549742a7c530dade87ca442efa7d9652829 refs/remotes/origin/master


File: /.git\refs\heads\master
8d967549742a7c530dade87ca442efa7d9652829


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /mikrotik-config\app.rc
// Microsoft Visual C++ generated resource script.
//
#include "resource.h"

#define APSTUDIO_READONLY_SYMBOLS

/////////////////////////////////////////////////////////////////////////////
#undef APSTUDIO_READONLY_SYMBOLS

/////////////////////////////////////////////////////////////////////////////
// English (U.S.) resources


/////////////////////////////////////////////////////////////////////////////
//
// Icon
//

// Icon placed first or with lowest ID value becomes application icon

LANGUAGE 10, 2
#pragma code_page(1252)
1           ICON         "app.ico"

#ifdef APSTUDIO_INVOKED
/////////////////////////////////////////////////////////////////////////////
//
// TEXTINCLUDE
//

1 TEXTINCLUDE  
BEGIN
    "resource.h\0"
    "\0"
END

2 TEXTINCLUDE  
BEGIN
    "#include ""afxres.h""\r\n"
    "\0"
END

3 TEXTINCLUDE  
BEGIN
    "\0"
END

#endif    // APSTUDIO_INVOKED

/////////////////////////////////////////////////////////////////////////////



#ifndef APSTUDIO_INVOKED
/////////////////////////////////////////////////////////////////////////////
//
// Generated from the TEXTINCLUDE 3 resource.
//


/////////////////////////////////////////////////////////////////////////////
#endif    // not APSTUDIO_INVOKED



File: /mikrotik-config\AssemblyInfo.cpp
#include "stdafx.h"

using namespace System;
using namespace System::Reflection;
using namespace System::Runtime::CompilerServices;
using namespace System::Runtime::InteropServices;
using namespace System::Security::Permissions;

//
// General Information about an assembly is controlled through the following
// set of attributes. Change these attribute values to modify the information
// associated with an assembly.
//
[assembly:AssemblyTitleAttribute("mikrotikconfig")];
[assembly:AssemblyDescriptionAttribute("")];
[assembly:AssemblyConfigurationAttribute("")];
[assembly:AssemblyCompanyAttribute("")];
[assembly:AssemblyProductAttribute("mikrotikconfig")];
[assembly:AssemblyCopyrightAttribute("Copyright (c)  2019")];
[assembly:AssemblyTrademarkAttribute("")];
[assembly:AssemblyCultureAttribute("")];

//
// Version information for an assembly consists of the following four values:
//
//      Major Version
//      Minor Version
//      Build Number
//      Revision
//
// You can specify all the value or you can default the Revision and Build Numbers
// by using the '*' as shown below:

[assembly:AssemblyVersionAttribute("1.0.*")];

[assembly:ComVisible(false)];

[assembly:CLSCompliantAttribute(true)];

[assembly:SecurityPermission(SecurityAction::RequestMinimum, UnmanagedCode = true)];


File: /mikrotik-config\CmdGen.cpp
#include "StdAfx.h"
#include "CmdGen.h"


CCmdGen::CCmdGen(void)
{
}


int CCmdGen::GetPublicIpLines()
{
	return linesIpPublic;
}


int CCmdGen::GetClientLines()
{
	return linesClient;
}


int CCmdGen::SetOperation(String ^ value)
{

	operation = value;

	return 0;
}



String ^ CCmdGen::ParseIpPublics(String ^ input)
{

	return input;

}



int CCmdGen::SetAction(String ^ value)
{

	action = value;

	return 0;
}



int CCmdGen::SetComment(String ^ value)
{

	comment = value;

	return 0;
}


int CCmdGen::SetSrcAddress(String ^ value)
{
	srcAddress = value;

	return 0;
}


int CCmdGen::SetToAddress(String ^ value)
{

	toAdress = value;

	return 0;
}


int CCmdGen::SetChain(String ^ value)
{
	chain = value;

	return 0;
}


array<CResult ^>  ^ CCmdGen::Results()
{

	array<CResult ^>  ^ retResult;

	return retResult;
}


String ^ CCmdGen::ReadInputs(String ^ clientsList, String ^ ipList)
{

	TextReader ^clientRdr = gcnew StringReader(clientsList);
	TextReader ^ipRdr = gcnew StringReader(ipList);
	String ^lineClient;
	String ^lineIp;
	String ^ip;
	String ^cmdResult;
	array <String ^> ^arrayClients;
	arrayResult = gcnew array <CResult ^>(5000);
	int indexResult = 0;


	//Read line by line clientRdr ...
    while (lineClient = clientRdr->ReadLine())
    {

		//Read line by line ipRdr ...
	    lineIp = ipRdr->ReadLine();

		linesClient++;

		if(lineIp == nullptr)
			break;

			else
			{
				linesIpPublic++;
			}			


		if(lineIp->Length > 0 && lineClient->Length > 0)
		{

			arrayClients = ParseClients(lineClient);

			if(arrayClients[0]->Length > 0 && arrayClients[1]->Length > 0)
			{

				ip = ParseIpPublics(lineIp);

				SetOperation("add");
				SetAction("netmap");
				SetChain("srcnat");				
				SetComment(arrayClients[0]);				
				SetSrcAddress(arrayClients[1]);
				SetToAddress(ip);

				arrayResult[indexResult] = gcnew CResult();
				arrayResult[indexResult]->SetIpPublic(ip);
				arrayResult[indexResult]->SetClientComment(arrayClients[0]);
				arrayResult[indexResult]->SetClientIp(arrayClients[1]);				
				indexResult++;


				if(cmdResult != nullptr)
					cmdResult = cmdResult + "\r\n\r\n" + FwNat(true);

				else
					cmdResult = cmdResult + FwNat(true);

			}
		}
	}

	Array::Resize(arrayResult, indexResult);
	return cmdResult;

}



array<String ^ > ^ CCmdGen::ParseClients(String ^ input)
{


	//Split IP
	String ^ pattern = "(\\d{1,3}(\\.\\d{1,3}){3})";
	TextReader ^ txtReader = gcnew StringReader(input);
	String ^ line;
	Match ^ rExpr;
	Group ^ groupComment;
	int indexComment;
	array<String^>^ arrayReturn = gcnew array<String^> {"comment",  "ipPrivate"};


	//Read line by line ...
    while ((line = txtReader->ReadLine()))
    {

		// Evaluate regular expression
		rExpr = Regex::Match(line, pattern);

		groupComment = rExpr->Groups[0];
		indexComment = groupComment->Index;
		arrayReturn[0] = line->Substring(0, indexComment);
		arrayReturn[1] = rExpr->Value;


		Console::WriteLine(line);


    }


	return arrayReturn;
}



String ^ CCmdGen::FwNat(bool pair)
{	

	String ^ strResult;


    strResult = "/ip firewall nat " + operation +
				" action=" + action + " chain=" + chain +
                " comment=\"" + comment + "\"" +
                " src-address=" + srcAddress +
                " to-address=" + toAdress;

	strResult =  strResult + "\r\n";



	if(pair == true)
	{

		strResult = strResult + "/ip firewall nat " + operation +
					" action=" + action + " chain=dstnat" +
					" comment=\'" + comment + "\'" +
					" dst-address=\'" + toAdress + "\'" +
					" to-address=" + srcAddress;
	}


	return strResult;

}




File: /mikrotik-config\CmdGen.h
#pragma once

#include "result.h"

using namespace System;
using namespace Text::RegularExpressions;
using namespace IO;

ref class CCmdGen
{

private:

	 String ^ operation;
	 String ^ action;
	 String ^ chain;
	 String ^ comment;
	 String ^ ip;
	 String ^ srcAddress;
	 String ^ toAdress;
	 int linesClient;
	 int linesIpPublic;

public:

	array <CResult ^> ^arrayResult;

	CCmdGen(void);
	int GetPublicIpLines();
	String ^ ReadInputs(String ^ clientsList, String ^ ipList);
	array<String ^ > ^ ParseClients(String ^ input);
	String ^ ParseIpPublics(String ^ input);

	int SetOperation(String ^ value);
	int SetChain(String ^ value);
	int SetAction(String ^ value);
	int SetComment(String ^ value);
	int SetSrcAddress(String ^ value);
	int SetToAddress(String ^ value);
	int GetClientLines();
	array<CResult ^>  ^ Results();

	String ^ FwNat(bool pair);	

};


File: /mikrotik-config\Form1.h
#pragma once

#include <iostream>
#include "cmdgen.h"

using namespace std;



namespace mikrotikconfig {

	using namespace System::ComponentModel;
	using namespace System::Collections;
	using namespace System::Windows::Forms;
	using namespace System::Data;
	using namespace System::Drawing;

	/// <summary>
	/// Summary for Form1
	///
	/// WARNING: If you change the name of this class, you will need to change the
	///          'Resource File Name' property for the managed resource compiler tool
	///          associated with all .resx files this class depends on.  Otherwise,
	///          the designers will not be able to interact properly with localized
	///          resources associated with this form.
	/// </summary>
	public ref class Form1 : public System::Windows::Forms::Form
	{
	public:
		Form1(void)
		{
			InitializeComponent();
			//
			//TODO: Add the constructor code here
			//

		}

	protected:
		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		~Form1()
		{
			if (components)
			{
				delete components;
			}
		}

	protected: 






	private: System::Windows::Forms::Label^  label2;
	private: System::Windows::Forms::Label^  label3;
	private: System::Windows::Forms::TextBox^  txtbOuput;

	private: System::Windows::Forms::ListView^  listView1;



	private: System::Windows::Forms::ColumnHeader^  columnHeader3;
	private: System::Windows::Forms::ColumnHeader^  columnHeader4;
	private: System::Windows::Forms::ColumnHeader^  columnHeader1;






	private: System::Windows::Forms::ColumnHeader^  columnHeader5;
	private: System::Windows::Forms::ColumnHeader^  columnHeader2;

	private: System::Windows::Forms::TableLayoutPanel^  tableLayoutPanel2;
	private: System::Windows::Forms::Button^  button3;
	private: System::Windows::Forms::Label^  lblLinesClients;

	private: System::Windows::Forms::Label^  label1;
	private: System::Windows::Forms::TextBox^  textBox1;
	private: System::Windows::Forms::Label^  label4;
	private: System::Windows::Forms::Label^  lblIpPublic;

	private: System::Windows::Forms::TextBox^  textBox3;
	private: System::Windows::Forms::TableLayoutPanel^  tableLayoutPanel1;
	private: System::Windows::Forms::TableLayoutPanel^  tableLayoutPanel3;

















	private:
		/// <summary>
		/// Required designer variable.
		/// </summary>
		System::ComponentModel::Container ^components;

#pragma region Windows Form Designer generated code
		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		void InitializeComponent(void)
		{
			System::ComponentModel::ComponentResourceManager^  resources = (gcnew System::ComponentModel::ComponentResourceManager(Form1::typeid));
			this->label2 = (gcnew System::Windows::Forms::Label());
			this->label3 = (gcnew System::Windows::Forms::Label());
			this->txtbOuput = (gcnew System::Windows::Forms::TextBox());
			this->listView1 = (gcnew System::Windows::Forms::ListView());
			this->columnHeader3 = (gcnew System::Windows::Forms::ColumnHeader());
			this->columnHeader2 = (gcnew System::Windows::Forms::ColumnHeader());
			this->columnHeader5 = (gcnew System::Windows::Forms::ColumnHeader());
			this->columnHeader4 = (gcnew System::Windows::Forms::ColumnHeader());
			this->columnHeader1 = (gcnew System::Windows::Forms::ColumnHeader());
			this->tableLayoutPanel2 = (gcnew System::Windows::Forms::TableLayoutPanel());
			this->button3 = (gcnew System::Windows::Forms::Button());
			this->lblLinesClients = (gcnew System::Windows::Forms::Label());
			this->label1 = (gcnew System::Windows::Forms::Label());
			this->textBox1 = (gcnew System::Windows::Forms::TextBox());
			this->label4 = (gcnew System::Windows::Forms::Label());
			this->lblIpPublic = (gcnew System::Windows::Forms::Label());
			this->textBox3 = (gcnew System::Windows::Forms::TextBox());
			this->tableLayoutPanel1 = (gcnew System::Windows::Forms::TableLayoutPanel());
			this->tableLayoutPanel3 = (gcnew System::Windows::Forms::TableLayoutPanel());
			this->tableLayoutPanel2->SuspendLayout();
			this->tableLayoutPanel1->SuspendLayout();
			this->tableLayoutPanel3->SuspendLayout();
			this->SuspendLayout();
			// 
			// label2
			// 
			this->label2->AutoSize = true;
			this->label2->Font = (gcnew System::Drawing::Font(L"Lucida Sans Unicode", 11.25F, System::Drawing::FontStyle::Bold));
			this->label2->Location = System::Drawing::Point(3, 0);
			this->label2->Name = L"label2";
			this->label2->Size = System::Drawing::Size(111, 18);
			this->label2->TabIndex = 10;
			this->label2->Text = L"Info Preview";
			// 
			// label3
			// 
			this->label3->Anchor = static_cast<System::Windows::Forms::AnchorStyles>(((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Left) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->label3->AutoSize = true;
			this->label3->Font = (gcnew System::Drawing::Font(L"Lucida Sans Unicode", 11.25F, System::Drawing::FontStyle::Bold));
			this->label3->Location = System::Drawing::Point(3, 0);
			this->label3->Name = L"label3";
			this->label3->Size = System::Drawing::Size(1338, 18);
			this->label3->TabIndex = 12;
			this->label3->Text = L"Info Output";
			// 
			// txtbOuput
			// 
			this->txtbOuput->Anchor = static_cast<System::Windows::Forms::AnchorStyles>(((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Left) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->txtbOuput->Location = System::Drawing::Point(3, 21);
			this->txtbOuput->Multiline = true;
			this->txtbOuput->Name = L"txtbOuput";
			this->txtbOuput->ScrollBars = System::Windows::Forms::ScrollBars::Vertical;
			this->txtbOuput->Size = System::Drawing::Size(1338, 255);
			this->txtbOuput->TabIndex = 11;
			// 
			// listView1
			// 
			this->listView1->Columns->AddRange(gcnew cli::array< System::Windows::Forms::ColumnHeader^  >(5) {this->columnHeader3, this->columnHeader2, 
				this->columnHeader5, this->columnHeader4, this->columnHeader1});
			this->listView1->Location = System::Drawing::Point(3, 21);
			this->listView1->Name = L"listView1";
			this->listView1->Size = System::Drawing::Size(1337, 55);
			this->listView1->TabIndex = 13;
			this->listView1->UseCompatibleStateImageBehavior = false;
			this->listView1->View = System::Windows::Forms::View::Details;
			// 
			// columnHeader3
			// 
			this->columnHeader3->Text = L"#";
			this->columnHeader3->Width = 1;
			// 
			// columnHeader2
			// 
			this->columnHeader2->Text = L"Chain";
			// 
			// columnHeader5
			// 
			this->columnHeader5->Text = L"Comment";
			this->columnHeader5->Width = 200;
			// 
			// columnHeader4
			// 
			this->columnHeader4->Text = L"Source Address";
			this->columnHeader4->Width = 203;
			// 
			// columnHeader1
			// 
			this->columnHeader1->Text = L"Destination Address";
			this->columnHeader1->Width = 153;
			// 
			// tableLayoutPanel2
			// 
			this->tableLayoutPanel2->Anchor = static_cast<System::Windows::Forms::AnchorStyles>(((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Left) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->tableLayoutPanel2->ColumnCount = 1;
			this->tableLayoutPanel2->ColumnStyles->Add((gcnew System::Windows::Forms::ColumnStyle(System::Windows::Forms::SizeType::Percent, 
				100)));
			this->tableLayoutPanel2->Controls->Add(this->listView1, 0, 1);
			this->tableLayoutPanel2->Controls->Add(this->label2, 0, 0);
			this->tableLayoutPanel2->Location = System::Drawing::Point(13, 252);
			this->tableLayoutPanel2->Name = L"tableLayoutPanel2";
			this->tableLayoutPanel2->RowCount = 2;
			this->tableLayoutPanel2->RowStyles->Add((gcnew System::Windows::Forms::RowStyle(System::Windows::Forms::SizeType::Percent, 23.07692F)));
			this->tableLayoutPanel2->RowStyles->Add((gcnew System::Windows::Forms::RowStyle(System::Windows::Forms::SizeType::Percent, 76.92308F)));
			this->tableLayoutPanel2->Size = System::Drawing::Size(1343, 79);
			this->tableLayoutPanel2->TabIndex = 23;
			// 
			// button3
			// 
			this->button3->Anchor = static_cast<System::Windows::Forms::AnchorStyles>(((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Bottom) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->button3->BackColor = System::Drawing::SystemColors::ButtonFace;
			this->button3->Location = System::Drawing::Point(1232, 207);
			this->button3->Name = L"button3";
			this->button3->Size = System::Drawing::Size(109, 27);
			this->button3->TabIndex = 15;
			this->button3->Text = L"Parse";
			this->button3->UseVisualStyleBackColor = false;
			this->button3->Click += gcnew System::EventHandler(this, &Form1::button3_Click);
			// 
			// lblLinesClients
			// 
			this->lblLinesClients->Anchor = static_cast<System::Windows::Forms::AnchorStyles>((((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Bottom) 
				| System::Windows::Forms::AnchorStyles::Left) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->lblLinesClients->AutoSize = true;
			this->lblLinesClients->Location = System::Drawing::Point(3, 191);
			this->lblLinesClients->Name = L"lblLinesClients";
			this->lblLinesClients->Size = System::Drawing::Size(666, 13);
			this->lblLinesClients->TabIndex = 18;
			this->lblLinesClients->Text = L"Total Lines";
			// 
			// label1
			// 
			this->label1->Anchor = static_cast<System::Windows::Forms::AnchorStyles>((((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Bottom) 
				| System::Windows::Forms::AnchorStyles::Left) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->label1->AutoSize = true;
			this->label1->Font = (gcnew System::Drawing::Font(L"Lucida Sans Unicode", 11.25F, System::Drawing::FontStyle::Bold, System::Drawing::GraphicsUnit::Point, 
				static_cast<System::Byte>(0)));
			this->label1->Location = System::Drawing::Point(3, 0);
			this->label1->Name = L"label1";
			this->label1->Size = System::Drawing::Size(666, 18);
			this->label1->TabIndex = 8;
			this->label1->Text = L"Input Clients";
			// 
			// textBox1
			// 
			this->textBox1->Anchor = static_cast<System::Windows::Forms::AnchorStyles>((((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Bottom) 
				| System::Windows::Forms::AnchorStyles::Left) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->textBox1->Location = System::Drawing::Point(3, 21);
			this->textBox1->Multiline = true;
			this->textBox1->Name = L"textBox1";
			this->textBox1->ScrollBars = System::Windows::Forms::ScrollBars::Vertical;
			this->textBox1->Size = System::Drawing::Size(666, 167);
			this->textBox1->TabIndex = 4;
			this->textBox1->Text = resources->GetString(L"textBox1.Text");
			this->textBox1->TextChanged += gcnew System::EventHandler(this, &Form1::textBox1_TextChanged);
			// 
			// label4
			// 
			this->label4->Anchor = static_cast<System::Windows::Forms::AnchorStyles>((((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Bottom) 
				| System::Windows::Forms::AnchorStyles::Left) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->label4->AutoSize = true;
			this->label4->Font = (gcnew System::Drawing::Font(L"Lucida Sans Unicode", 11.25F, System::Drawing::FontStyle::Bold));
			this->label4->Location = System::Drawing::Point(675, 0);
			this->label4->Name = L"label4";
			this->label4->Size = System::Drawing::Size(666, 18);
			this->label4->TabIndex = 19;
			this->label4->Text = L"Input Public IP";
			// 
			// lblIpPublic
			// 
			this->lblIpPublic->Anchor = static_cast<System::Windows::Forms::AnchorStyles>((((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Bottom) 
				| System::Windows::Forms::AnchorStyles::Left) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->lblIpPublic->AutoSize = true;
			this->lblIpPublic->Location = System::Drawing::Point(675, 191);
			this->lblIpPublic->Name = L"lblIpPublic";
			this->lblIpPublic->Size = System::Drawing::Size(666, 13);
			this->lblIpPublic->TabIndex = 17;
			this->lblIpPublic->Text = L"Total Lines";
			// 
			// textBox3
			// 
			this->textBox3->Anchor = static_cast<System::Windows::Forms::AnchorStyles>((((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Bottom) 
				| System::Windows::Forms::AnchorStyles::Left) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->textBox3->Location = System::Drawing::Point(675, 21);
			this->textBox3->Multiline = true;
			this->textBox3->Name = L"textBox3";
			this->textBox3->ScrollBars = System::Windows::Forms::ScrollBars::Vertical;
			this->textBox3->Size = System::Drawing::Size(666, 167);
			this->textBox3->TabIndex = 14;
			this->textBox3->Text = L"77.151.767.10\r\n\r\n77.151.767.11\r\n\r\n77.151.767.12\r\n\r\n77.151.767.13\r\n\r\n77.151.767.14" 
				L"\r\n\r\n77.151.767.15\r\n\r\n77.151.767.16\r\n";
			// 
			// tableLayoutPanel1
			// 
			this->tableLayoutPanel1->Anchor = static_cast<System::Windows::Forms::AnchorStyles>(((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Left) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->tableLayoutPanel1->AutoSize = true;
			this->tableLayoutPanel1->ColumnCount = 2;
			this->tableLayoutPanel1->ColumnStyles->Add((gcnew System::Windows::Forms::ColumnStyle(System::Windows::Forms::SizeType::Percent, 
				50)));
			this->tableLayoutPanel1->ColumnStyles->Add((gcnew System::Windows::Forms::ColumnStyle(System::Windows::Forms::SizeType::Percent, 
				50)));
			this->tableLayoutPanel1->Controls->Add(this->textBox3, 1, 1);
			this->tableLayoutPanel1->Controls->Add(this->lblIpPublic, 1, 2);
			this->tableLayoutPanel1->Controls->Add(this->label4, 1, 0);
			this->tableLayoutPanel1->Controls->Add(this->textBox1, 0, 1);
			this->tableLayoutPanel1->Controls->Add(this->label1, 0, 0);
			this->tableLayoutPanel1->Controls->Add(this->lblLinesClients, 0, 2);
			this->tableLayoutPanel1->Controls->Add(this->button3, 1, 3);
			this->tableLayoutPanel1->Location = System::Drawing::Point(12, 12);
			this->tableLayoutPanel1->Name = L"tableLayoutPanel1";
			this->tableLayoutPanel1->RowCount = 4;
			this->tableLayoutPanel1->RowStyles->Add((gcnew System::Windows::Forms::RowStyle()));
			this->tableLayoutPanel1->RowStyles->Add((gcnew System::Windows::Forms::RowStyle(System::Windows::Forms::SizeType::Percent, 100)));
			this->tableLayoutPanel1->RowStyles->Add((gcnew System::Windows::Forms::RowStyle()));
			this->tableLayoutPanel1->RowStyles->Add((gcnew System::Windows::Forms::RowStyle()));
			this->tableLayoutPanel1->Size = System::Drawing::Size(1344, 237);
			this->tableLayoutPanel1->TabIndex = 22;
			// 
			// tableLayoutPanel3
			// 
			this->tableLayoutPanel3->Anchor = static_cast<System::Windows::Forms::AnchorStyles>(((System::Windows::Forms::AnchorStyles::Top | System::Windows::Forms::AnchorStyles::Left) 
				| System::Windows::Forms::AnchorStyles::Right));
			this->tableLayoutPanel3->ColumnCount = 1;
			this->tableLayoutPanel3->ColumnStyles->Add((gcnew System::Windows::Forms::ColumnStyle(System::Windows::Forms::SizeType::Percent, 
				100)));
			this->tableLayoutPanel3->Controls->Add(this->txtbOuput, 0, 1);
			this->tableLayoutPanel3->Controls->Add(this->label3, 0, 0);
			this->tableLayoutPanel3->Location = System::Drawing::Point(12, 341);
			this->tableLayoutPanel3->Name = L"tableLayoutPanel3";
			this->tableLayoutPanel3->RowCount = 2;
			this->tableLayoutPanel3->RowStyles->Add((gcnew System::Windows::Forms::RowStyle(System::Windows::Forms::SizeType::Percent, 6.593407F)));
			this->tableLayoutPanel3->RowStyles->Add((gcnew System::Windows::Forms::RowStyle(System::Windows::Forms::SizeType::Percent, 93.40659F)));
			this->tableLayoutPanel3->Size = System::Drawing::Size(1344, 287);
			this->tableLayoutPanel3->TabIndex = 24;
			// 
			// Form1
			// 
			this->AutoScaleDimensions = System::Drawing::SizeF(6, 13);
			this->AutoScaleMode = System::Windows::Forms::AutoScaleMode::Font;
			this->BackColor = System::Drawing::SystemColors::ButtonFace;
			this->ClientSize = System::Drawing::Size(1368, 669);
			this->Controls->Add(this->tableLayoutPanel3);
			this->Controls->Add(this->tableLayoutPanel2);
			this->Controls->Add(this->tableLayoutPanel1);
			this->Icon = (cli::safe_cast<System::Drawing::Icon^  >(resources->GetObject(L"$this.Icon")));
			this->Name = L"Form1";
			this->Text = L"Mikrotik Configuration Generator";
			this->Load += gcnew System::EventHandler(this, &Form1::Form1_Load);
			this->tableLayoutPanel2->ResumeLayout(false);
			this->tableLayoutPanel2->PerformLayout();
			this->tableLayoutPanel1->ResumeLayout(false);
			this->tableLayoutPanel1->PerformLayout();
			this->tableLayoutPanel3->ResumeLayout(false);
			this->tableLayoutPanel3->PerformLayout();
			this->ResumeLayout(false);
			this->PerformLayout();

		}
#pragma endregion


	private: System::Void Form1_Load(System::Object^  sender, System::EventArgs^  e)
	 {

		 CCmdGen ^cmd = gcnew CCmdGen();

	 }


	 private: System::Void button3_Click(System::Object^  sender, System::EventArgs^  e)
	 {

			if(this->listView1->Items->Count  > 2)
			{
				this->listView1->Items->Clear();
				
			}

		
			this->txtbOuput->Text = "";


			CCmdGen ^ cmd = gcnew CCmdGen();

			String ^ cmdResult = cmd->ReadInputs(this->textBox1->Text, this->textBox3->Text);
			int linesTxtClients = cmd->GetClientLines();			
			int linesTxtIpPublics = cmd->GetPublicIpLines();

			this->lblIpPublic->Text = "Total Lines: " + Convert::ToString(linesTxtIpPublics);
			this->lblLinesClients->Text = "Total Lines: " + Convert::ToString(linesTxtClients);


			// Set & Parse Input
			cmd->SetOperation("add");
			cmd->SetAction("netmap");
			cmd->SetChain("srcnat");
			cmd->SetComment("CustomerNumber");
			cmd->SetSrcAddress("10.10.77.43");
			cmd->SetToAddress("77.151.767.10");


			// Output to varible
			String ^ result = cmd->FwNat(true);



			// Variable to Preview (ListView)	
			for(int a = 0; a < cmd->arrayResult->Length; a++)
			{

				ListViewItem ^ items = gcnew ListViewItem();

				items->SubItems->Add("add");
				items->SubItems->Add(cmd->arrayResult[a]->GetClient());
				items->SubItems->Add(cmd->arrayResult[a]->GetIpClient());
				items->SubItems->Add(cmd->arrayResult[a]->GetIpPublic());
				this->listView1->Items->Add(items);

			}			




			// Variable to output (txtbOutput)
			this->txtbOuput->Text = cmdResult;


		}


private: System::Void textBox1_TextChanged(System::Object^  sender, System::EventArgs^  e)
		 {

		 }
};
}



File: /mikrotik-config\Form1.resx
﻿<?xml version="1.0" encoding="utf-8"?>
<root>
  <!-- 
    Microsoft ResX Schema 
    
    Version 2.0
    
    The primary goals of this format is to allow a simple XML format 
    that is mostly human readable. The generation and parsing of the 
    various data types are done through the TypeConverter classes 
    associated with the data types.
    
    Example:
    
    ... ado.net/XML headers & schema ...
    <resheader name="resmimetype">text/microsoft-resx</resheader>
    <resheader name="version">2.0</resheader>
    <resheader name="reader">System.Resources.ResXResourceReader, System.Windows.Forms, ...</resheader>
    <resheader name="writer">System.Resources.ResXResourceWriter, System.Windows.Forms, ...</resheader>
    <data name="Name1"><value>this is my long string</value><comment>this is a comment</comment></data>
    <data name="Color1" type="System.Drawing.Color, System.Drawing">Blue</data>
    <data name="Bitmap1" mimetype="application/x-microsoft.net.object.binary.base64">
        <value>[base64 mime encoded serialized .NET Framework object]</value>
    </data>
    <data name="Icon1" type="System.Drawing.Icon, System.Drawing" mimetype="application/x-microsoft.net.object.bytearray.base64">
        <value>[base64 mime encoded string representing a byte array form of the .NET Framework object]</value>
        <comment>This is a comment</comment>
    </data>
                
    There are any number of "resheader" rows that contain simple 
    name/value pairs.
    
    Each data row contains a name, and value. The row also contains a 
    type or mimetype. Type corresponds to a .NET class that support 
    text/value conversion through the TypeConverter architecture. 
    Classes that don't support this are serialized and stored with the 
    mimetype set.
    
    The mimetype is used for serialized objects, and tells the 
    ResXResourceReader how to depersist the object. This is currently not 
    extensible. For a given mimetype the value must be set accordingly:
    
    Note - application/x-microsoft.net.object.binary.base64 is the format 
    that the ResXResourceWriter will generate, however the reader can 
    read any of the formats listed below.
    
    mimetype: application/x-microsoft.net.object.binary.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Binary.BinaryFormatter
            : and then encoded with base64 encoding.
    
    mimetype: application/x-microsoft.net.object.soap.base64
    value   : The object must be serialized with 
            : System.Runtime.Serialization.Formatters.Soap.SoapFormatter
            : and then encoded with base64 encoding.

    mimetype: application/x-microsoft.net.object.bytearray.base64
    value   : The object must be serialized into a byte array 
            : using a System.ComponentModel.TypeConverter
            : and then encoded with base64 encoding.
    -->
  <xsd:schema id="root" xmlns="" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
    <xsd:import namespace="http://www.w3.org/XML/1998/namespace" />
    <xsd:element name="root" msdata:IsDataSet="true">
      <xsd:complexType>
        <xsd:choice maxOccurs="unbounded">
          <xsd:element name="metadata">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" />
              </xsd:sequence>
              <xsd:attribute name="name" use="required" type="xsd:string" />
              <xsd:attribute name="type" type="xsd:string" />
              <xsd:attribute name="mimetype" type="xsd:string" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="assembly">
            <xsd:complexType>
              <xsd:attribute name="alias" type="xsd:string" />
              <xsd:attribute name="name" type="xsd:string" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="data">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
                <xsd:element name="comment" type="xsd:string" minOccurs="0" msdata:Ordinal="2" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" msdata:Ordinal="1" />
              <xsd:attribute name="type" type="xsd:string" msdata:Ordinal="3" />
              <xsd:attribute name="mimetype" type="xsd:string" msdata:Ordinal="4" />
              <xsd:attribute ref="xml:space" />
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="resheader">
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="value" type="xsd:string" minOccurs="0" msdata:Ordinal="1" />
              </xsd:sequence>
              <xsd:attribute name="name" type="xsd:string" use="required" />
            </xsd:complexType>
          </xsd:element>
        </xsd:choice>
      </xsd:complexType>
    </xsd:element>
  </xsd:schema>
  <resheader name="resmimetype">
    <value>text/microsoft-resx</value>
  </resheader>
  <resheader name="version">
    <value>2.0</value>
  </resheader>
  <resheader name="reader">
    <value>System.Resources.ResXResourceReader, System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <resheader name="writer">
    <value>System.Resources.ResXResourceWriter, System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089</value>
  </resheader>
  <data name="textBox1.Text" xml:space="preserve">
    <value>"customername"

206-Fred Bloggs, Anytown 10.10.44.63

520-Sean Smith, BallyDuff Woods 10.10.48.65

223 - Pat Murphy, Kerry 10.10.49.66

140-Mary Flaherty, Tralee 10.10.77.10

658-Michael Kennedy - PortLaoise 10.10.66.14

452 - Joan O'Mahony, Kilmacow 10.10.44.16

759 - John &amp; Maria Kelly, Dublin 10.10.39.17

</value>
  </data>
  <assembly alias="System.Drawing" name="System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a" />
  <data name="$this.Icon" type="System.Drawing.Icon, System.Drawing" mimetype="application/x-microsoft.net.object.bytearray.base64">
    <value>
        AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AABNTU0ATU1NAE1NTQBNTU1KTU1Nn01NTdhNTU3eTU1NpU1NTVVNTU0ATU1NAE1NTQBNTU0ATU1NAE1N
        TQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAP//
        /wD///8A////AE1NTQBNTU0vTU1Nv01NTfJNTU3yTU1N8k1NTfJNTU3yTU1N8k1NTcRNTU01TU1NAE1N
        TQD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP//
        /wD///8A////AP///wD///8ATU1NAE1NTb9NTU3yTU1N8k1NTfJNTU3yTU1N8k1NTfJNTU3yTU1N8k1N
        TeZNTU01TU1NAP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP//
        /wD///8A////AP///wD///8A////AP///wBNTU1NTU1N8k1NTfJRUVHyr6+v+e3t7f7x8fH+uLi4+lZW
        VvNNTU3yTU1N8k1NTeZNTU01////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP//
        /wD///8A////AP///wD///8A////AP///wD///8A////AE1NTaVNTU3yTU1N8rKysvn/////+/v7//X1
        9f7/////2dnZ/FZWVvNNTU3yTU1N8k1NTeZNTU01////AP///wD///8A////AP///wD///8A////AP//
        /wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8ATU1N3k1NTfJNTU3y8fHx/vPz
        8/5hYWHzU1NT8t/f3/3/////2dnZ/FZWVvNNTU3yTU1N8k1NTeZNTU01////AP///wD///8A////AP//
        /wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wBNTU3nTU1N8k1N
        TfL39/f+8fHx/lNTU/JNTU3y1NTU/P//////////2dnZ/FZWVvNNTU3yTU1N8k1NTeZNTU01////AP//
        /wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AE1N
        Ta5NTU3yTU1N8rq6uvr/////7+/v/uHh4f3/////////////////////2dnZ/FZWVvNNTU3yTU1N8k1N
        TeZNTU01////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP//
        /wD///8ATU1NWE1NTfJNTU3yVlZW89LS0vz/////////////////////////////////////2dnZ/FZW
        VvNNTU3yTU1N8k1NTeZNTU01////AP///wD///8A////AP///wD///8A////AP///wD///8A////AP//
        /wD///8A////AP///wBNTU0ATU1NxE1NTfJNTU3yU1NT8tLS0vz/////////////////////////////
        ////////2dnZ/FZWVvNNTU3yTU1N8k1NTeZNTU2zTU1N501NTfJNTU3nTU1Ns01NTXpNTU05////AP//
        /wD///8A////AP///wD///8A////AE1NTQBNTU01TU1N3U1NTfJNTU3yU1NT8tTU1Pz/////////////
        ////////////////////////2dnZ/FZWVvNNTU3yTU1N8k1NTfJNTU3yTU1N8k1NTfJNTU3yTU1N8k1N
        TfJNTU3HTU1NR////wD///8A////AP///wD///8ATU1NAE1NTQBNTU0yTU1N3U1NTfJTU1Py0NDQ+///
        ////////////////////////////////////////2dnZ/FZWVvNNTU3yTU1N8k1NTfJNTU3yTU1N8k1N
        TfJNTU3yTU1N8k1NTfJNTU3yTU1Nhf///wD///8A////AP///wBNTU0ATU1NAE1NTQBNTU0yVFRU3s/P
        z/v/////////////////////////////////////////////////////2dnZ/KGhofjS0tL89/f3/v//
        ///39/f+0tLS/KOjo/hYWFjzTU1N8k1NTfJNTU3yTU1Nqv///wD///8A////AE1NTQBNTU0ATU1NAP//
        /wCtra1Z+Pj4/f////////////////39/f//////////////////////////////////////////////
        //////////////////////////////X19f6SkpL3TU1N8k1NTfJNTU3yTU1NiP///wD///8ATU1NAE1N
        TQBNTU0A////AP///wC6urpi+Pj4/f/////5+fn/hoaG9tLS0vz/////////////////////////////
        //////////////////////////////////////////////////+tra35TU1N8k1NTfJNTU3yTU1NRP//
        /wBNTU0ATU1NAE1NTQD///8A////AP///wC6urpi8vLy/IGBgfZNTU3yU1NT8tLS0vz/////////////
        //////////////////////////////////////////////////////////////////+UlJT3TU1N8k1N
        TfJNTU3K////AE1NTQBNTU0ATU1NAP///wD///8A////AP///wBxcXE8TU1N3U1NTfJNTU3yU1NT8tLS
        0vz///////////////////////////////////////////////////////////////////////////Pz
        8/5aWlrzTU1N8k1NTfJNTU05TU1NAE1NTQBNTU0A////AP///wD///8A////AP///wBNTU0yTU1N3U1N
        TfJNTU3ymJiY9///////////////////////////////////////////////////////////////////
        /////////////6Ojo/hNTU3yTU1N8k1NTYBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1N
        TQBNTU22TU1N8k1NTfLU1NT8//////////////////////////9NTU3yTU1N8k1NTfJNTU3yTU1N8k1N
        TfK0tLT5////////////////19fX/E1NTfJNTU3yTU1NuU1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1N
        TQBNTU0ATU1NAE1NTdtNTU3yTU1N8u/v7/7//////////////////////////01NTfJNTU3yTU1N8k1N
        TfJNTU3yTU1N8k1NTfK2trb5///////////z8/P+TU1N8k1NTfJNTU3hTU1NAE1NTQBNTU0ATU1NAE1N
        TQBNTU0ATU1NAE1NTQBNTU0ATU1N7E1NTfJNTU3y+/v7////////////////////////////TU1N8k1N
        TfJNTU3yTU1N8k1NTfJNTU3yTU1N8k1NTfK4uLj6//////////9PT0/yTU1N8k1NTfJNTU0ATU1NAE1N
        TQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU3bTU1N8k1NTfLv7+/+////////////////////////
        //9NTU3yTU1N8k1NTfL///8A////AE1NTbVNTU3yTU1N8k1NTfK8vLz68fHx/k1NTfJNTU3yTU1N3k1N
        TQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTbFNTU3yTU1N8tHR0fv/////////////
        /////////////01NTfJNTU3yTU1N8v///wD///8A////AE1NTbhNTU3yTU1N8k1NTfKYmJj3TU1N8k1N
        TfJNTU2lTU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NeE1NTfJNTU3ymJiY9///
        ////////////////////////TU1N8k1NTfJNTU3yTU1Nhf///wD///8A////AE1NTb5NTU3yTU1N8k1N
        TfJNTU3yTU1N8k1NTUFNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0rTU1N8k1N
        TfJWVlbz7e3t/v////////////////////+SkpL3TU1N8k1NTfJNTU3yTU1Nhf///wD///8A////AE1N
        TY1NTU3yTU1N8k1NTfJNTU2N////AE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1N
        TQBNTU3ETU1N8k1NTfKMjIz2//////////////////////////+SkpL3TU1N8k1NTfJNTU3yTU1Nhf//
        /wD///8A////AE1NTStNTU1kTU1NK////wD///8ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1N
        TQBNTU0ATU1NAE1NTTxNTU3yTU1N8k1NTfKjo6P4//////////////////////////+SkpL3TU1N8k1N
        TfJNTU3yTU1NY////wD///8A////AP///wD///8A////AP///wBNTU0ATU1NAE1NTQBNTU0ATU1NAE1N
        TQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTXxNTU3yTU1N8k1NTfKIiIj27+/v/v//////////////////
        //+SkpL3TU1N8k1NTfJNTU3y////AP///wD///8A////AP///wD///8A////AE1NTQBNTU0ATU1NAE1N
        TQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTZxNTU3yTU1N8k1NTfJWVlbzmpqa+M/P
        z/vr6+v9/////+vr6/14eHj1TU1N8k1NTfJNTU05////AP///wD///8A////AP///wD///8ATU1NAE1N
        TQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTXdNTU3yTU1N8k1N
        TfJNTU3yTU1N8k1NTfJNTU3yTU1N8k1NTfJNTU3yTU1N8v///wD///8A////AP///wD///8A////AP//
        /wBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0A////AE1N
        TT9NTU3ETU1N8k1NTfJNTU3yTU1N8k1NTfJNTU3yTU1N8k1NTfJNTU1j////AP///wD///8A////AP//
        /wD///8A////AE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1NTQBNTU0ATU1NAE1N
        TQD///8A////AP///wBNTU0uTU1NdU1NTa5NTU3WTU1N8k1NTdZNTU2dTU1NOf///wD///8A////AP//
        /wD///8A////AP///wD///8A4H///4Af//+AD///AAf//wAD//8AAf//AAD//wAAf/8AAD//gAAAf4AA
        AB/AAAAP4AAAB/AAAAP4AAAB/AAAAf4AAAD/AAAA/4AAAP+AAAD/gAAA/4AGAP+ABwD/gAOA/4ABwf/A
        AOP/wAB//+AAf//wAD//+AB///wAf///AP8=
</value>
  </data>
</root>

File: /mikrotik-config\mikrotik-config.cpp
// mikrotik-config.cpp : main project file.

#include "stdafx.h"
#include "Form1.h"

using namespace mikrotikconfig;


int main(array<System::String ^> ^args)
{

	// Enabling Windows XP visual effects before any controls are created
	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false); 



	// Create the main window and run it
	Application::Run(gcnew Form1());	

	return 0;
}


File: /mikrotik-config\mikrotik-config.vcproj
<?xml version="1.0" encoding="Windows-1252"?>
<VisualStudioProject
	ProjectType="Visual C++"
	Version="8,00"
	Name="mikrotik-config"
	ProjectGUID="{3A24367E-AB39-458A-B637-B00CB2EFAF8C}"
	RootNamespace="mikrotikconfig"
	Keyword="ManagedCProj"
	>
	<Platforms>
		<Platform
			Name="Win32"
		/>
	</Platforms>
	<ToolFiles>
	</ToolFiles>
	<Configurations>
		<Configuration
			Name="Debug|Win32"
			OutputDirectory="$(SolutionDir)$(ConfigurationName)"
			IntermediateDirectory="$(ConfigurationName)"
			ConfigurationType="1"
			CharacterSet="1"
			ManagedExtensions="2"
			>
			<Tool
				Name="VCPreBuildEventTool"
			/>
			<Tool
				Name="VCCustomBuildTool"
			/>
			<Tool
				Name="VCXMLDataGeneratorTool"
			/>
			<Tool
				Name="VCWebServiceProxyGeneratorTool"
			/>
			<Tool
				Name="VCMIDLTool"
			/>
			<Tool
				Name="VCCLCompilerTool"
				Optimization="0"
				PreprocessorDefinitions="WIN32;_DEBUG"
				RuntimeLibrary="3"
				UsePrecompiledHeader="2"
				WarningLevel="3"
				DebugInformationFormat="3"
			/>
			<Tool
				Name="VCManagedResourceCompilerTool"
			/>
			<Tool
				Name="VCResourceCompilerTool"
			/>
			<Tool
				Name="VCPreLinkEventTool"
			/>
			<Tool
				Name="VCLinkerTool"
				AdditionalDependencies="$(NoInherit)"
				LinkIncremental="2"
				GenerateDebugInformation="true"
				AssemblyDebug="1"
				SubSystem="2"
				EntryPointSymbol="main"
				TargetMachine="1"
			/>
			<Tool
				Name="VCALinkTool"
			/>
			<Tool
				Name="VCManifestTool"
			/>
			<Tool
				Name="VCXDCMakeTool"
			/>
			<Tool
				Name="VCBscMakeTool"
			/>
			<Tool
				Name="VCFxCopTool"
			/>
			<Tool
				Name="VCAppVerifierTool"
			/>
			<Tool
				Name="VCWebDeploymentTool"
			/>
			<Tool
				Name="VCPostBuildEventTool"
			/>
		</Configuration>
		<Configuration
			Name="Release|Win32"
			OutputDirectory="$(SolutionDir)$(ConfigurationName)"
			IntermediateDirectory="$(ConfigurationName)"
			ConfigurationType="1"
			CharacterSet="1"
			ManagedExtensions="2"
			WholeProgramOptimization="1"
			>
			<Tool
				Name="VCPreBuildEventTool"
			/>
			<Tool
				Name="VCCustomBuildTool"
			/>
			<Tool
				Name="VCXMLDataGeneratorTool"
			/>
			<Tool
				Name="VCWebServiceProxyGeneratorTool"
			/>
			<Tool
				Name="VCMIDLTool"
			/>
			<Tool
				Name="VCCLCompilerTool"
				PreprocessorDefinitions="WIN32;NDEBUG"
				RuntimeLibrary="2"
				UsePrecompiledHeader="2"
				WarningLevel="3"
				DebugInformationFormat="3"
			/>
			<Tool
				Name="VCManagedResourceCompilerTool"
			/>
			<Tool
				Name="VCResourceCompilerTool"
			/>
			<Tool
				Name="VCPreLinkEventTool"
			/>
			<Tool
				Name="VCLinkerTool"
				AdditionalDependencies="$(NoInherit)"
				LinkIncremental="1"
				GenerateDebugInformation="true"
				SubSystem="2"
				EntryPointSymbol="main"
				TargetMachine="1"
			/>
			<Tool
				Name="VCALinkTool"
			/>
			<Tool
				Name="VCManifestTool"
			/>
			<Tool
				Name="VCXDCMakeTool"
			/>
			<Tool
				Name="VCBscMakeTool"
			/>
			<Tool
				Name="VCFxCopTool"
			/>
			<Tool
				Name="VCAppVerifierTool"
			/>
			<Tool
				Name="VCWebDeploymentTool"
			/>
			<Tool
				Name="VCPostBuildEventTool"
			/>
		</Configuration>
	</Configurations>
	<References>
		<AssemblyReference
			RelativePath="System.dll"
			AssemblyName="System, Version=2.0.0.0, PublicKeyToken=b77a5c561934e089, processorArchitecture=MSIL"
		/>
		<AssemblyReference
			RelativePath="System.Data.dll"
			AssemblyName="System.Data, Version=2.0.0.0, PublicKeyToken=b77a5c561934e089, processorArchitecture=x86"
		/>
		<AssemblyReference
			RelativePath="System.Drawing.dll"
			AssemblyName="System.Drawing, Version=2.0.0.0, PublicKeyToken=b03f5f7f11d50a3a, processorArchitecture=MSIL"
		/>
		<AssemblyReference
			RelativePath="System.Windows.Forms.dll"
			AssemblyName="System.Windows.Forms, Version=2.0.0.0, PublicKeyToken=b77a5c561934e089, processorArchitecture=MSIL"
		/>
		<AssemblyReference
			RelativePath="System.XML.dll"
			AssemblyName="System.Xml, Version=2.0.0.0, PublicKeyToken=b77a5c561934e089, processorArchitecture=MSIL"
		/>
	</References>
	<Files>
		<Filter
			Name="Source Files"
			Filter="cpp;c;cc;cxx;def;odl;idl;hpj;bat;asm;asmx"
			UniqueIdentifier="{4FC737F1-C7A5-4376-A066-2A32D752A2FF}"
			>
			<File
				RelativePath=".\AssemblyInfo.cpp"
				>
			</File>
			<File
				RelativePath=".\CmdGen.cpp"
				>
			</File>
			<File
				RelativePath=".\mikrotik-config.cpp"
				>
			</File>
			<File
				RelativePath=".\Result.cpp"
				>
			</File>
			<File
				RelativePath=".\stdafx.cpp"
				>
				<FileConfiguration
					Name="Debug|Win32"
					>
					<Tool
						Name="VCCLCompilerTool"
						UsePrecompiledHeader="1"
					/>
				</FileConfiguration>
				<FileConfiguration
					Name="Release|Win32"
					>
					<Tool
						Name="VCCLCompilerTool"
						UsePrecompiledHeader="1"
					/>
				</FileConfiguration>
			</File>
		</Filter>
		<Filter
			Name="Header Files"
			Filter="h;hpp;hxx;hm;inl;inc;xsd"
			UniqueIdentifier="{93995380-89BD-4b04-88EB-625FBE52EBFB}"
			>
			<File
				RelativePath=".\CmdGen.h"
				>
			</File>
			<File
				RelativePath=".\Form1.h"
				FileType="3"
				>
				<File
					RelativePath=".\Form1.resX"
					SubType="Designer"
					>
				</File>
			</File>
			<File
				RelativePath=".\resource.h"
				>
			</File>
			<File
				RelativePath=".\Result.h"
				>
			</File>
			<File
				RelativePath=".\stdafx.h"
				>
			</File>
		</Filter>
		<Filter
			Name="Resource Files"
			Filter="rc;ico;cur;bmp;dlg;rc2;rct;bin;rgs;gif;jpg;jpeg;jpe;resx;tiff;tif;png;wav"
			UniqueIdentifier="{67DA6AB6-F800-4c08-8B7A-83BB121AAD01}"
			>
			<File
				RelativePath=".\app.ico"
				>
			</File>
			<File
				RelativePath=".\app.rc"
				>
			</File>
		</Filter>
		<File
			RelativePath=".\ReadMe.txt"
			>
		</File>
	</Files>
	<Globals>
	</Globals>
</VisualStudioProject>


File: /mikrotik-config\resource.h
//{{NO_DEPENDENCIES}}
// Microsoft Visual C++ generated include file.
// Used by app.rc


File: /mikrotik-config\Result.cpp
#include "StdAfx.h"
#include "Result.h"

CResult::CResult(void)
{
}


String ^ CResult::GetClient()
{
	return clientComment;
}


String ^ CResult::SetClientComment(String ^ comment)
{
	clientComment = comment;
	return clientComment;
}


String ^ CResult::SetIpPublic(String ^ ip)
{
	ipPublic = ip;
	return ipPublic;
}


String ^ CResult::GetIpPublic()
{
	return ipPublic;
}

String ^ CResult::GetIpClient()
{
	return clientIp;
}


String ^ CResult::SetClientIp(String ^ ip)
{

	clientIp = ip;
	return clientIp;
}


File: /mikrotik-config\Result.h
#pragma once

using namespace System;

ref class CResult
{

private:
	String ^clientComment;
	String ^clientIp;
	String ^ipPublic;


public:

	String ^ SetClientComment(String ^ comment);
	String ^ SetIpPublic(String ^ ip);
	String ^ SetClientIp(String ^ ip);

	String ^ GetClient();
	String ^ GetIpPublic();
	String ^ GetIpClient();


	CResult(void);

};


File: /mikrotik-config\stdafx.cpp
// stdafx.cpp : source file that includes just the standard includes
// mikrotik-config.pch will be the pre-compiled header
// stdafx.obj will contain the pre-compiled type information

#include "stdafx.h"




File: /mikrotik-config\stdafx.h
// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently, but
// are changed infrequently
#pragma once

// TODO: reference additional headers your program requires here


File: /mikrotik-config.sln
﻿
Microsoft Visual Studio Solution File, Format Version 9.00
# Visual C++ Express 2005
Project("{8BC9CEB8-8B4A-11D0-8D11-00A0C91BC942}") = "mikrotik-config", "mikrotik-config\mikrotik-config.vcproj", "{3A24367E-AB39-458A-B637-B00CB2EFAF8C}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Win32 = Debug|Win32
		Release|Win32 = Release|Win32
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{3A24367E-AB39-458A-B637-B00CB2EFAF8C}.Debug|Win32.ActiveCfg = Debug|Win32
		{3A24367E-AB39-458A-B637-B00CB2EFAF8C}.Debug|Win32.Build.0 = Debug|Win32
		{3A24367E-AB39-458A-B637-B00CB2EFAF8C}.Release|Win32.ActiveCfg = Release|Win32
		{3A24367E-AB39-458A-B637-B00CB2EFAF8C}.Release|Win32.Build.0 = Release|Win32
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
EndGlobal


