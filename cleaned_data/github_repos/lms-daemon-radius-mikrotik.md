# Repository Information
Name: lms-daemon-radius-mikrotik

# Directory Structure
Directory structure:
└── github_repos/lms-daemon-radius-mikrotik/
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
    │   │       ├── pack-34e81a3ff116f3963663eb31d98a4ed5f56eee93.idx
    │   │       └── pack-34e81a3ff116f3963663eb31d98a4ed5f56eee93.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── .project
    ├── .pydevproject
    ├── .settings/
    │   └── org.eclipse.core.resources.prefs
    ├── client_ldrm.py
    ├── conf/
    │   └── ldrm.conf
    ├── createVirtEnv.bash
    ├── install.txt
    ├── ldrm.py
    ├── LICENSE
    ├── log/
    │   └── .gitignore
    ├── README.md
    ├── Readme.pl
    └── requirements.txt


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
	url = https://github.com/noxgle/lms-daemon-radius-mikrotik.git
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
0000000000000000000000000000000000000000 7063041d54df42b00136bff9833540ec21e49c34 vivek-dodia <vivek.dodia@icloud.com> 1738606448 -0500	clone: from https://github.com/noxgle/lms-daemon-radius-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 7063041d54df42b00136bff9833540ec21e49c34 vivek-dodia <vivek.dodia@icloud.com> 1738606448 -0500	clone: from https://github.com/noxgle/lms-daemon-radius-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 7063041d54df42b00136bff9833540ec21e49c34 vivek-dodia <vivek.dodia@icloud.com> 1738606448 -0500	clone: from https://github.com/noxgle/lms-daemon-radius-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
98917efbbb521f4fbe4da6f51f368b8fed7acb9f refs/remotes/origin/dev
7063041d54df42b00136bff9833540ec21e49c34 refs/remotes/origin/master


File: /.git\refs\heads\master
7063041d54df42b00136bff9833540ec21e49c34


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
/venv/
/tmp/


File: /.project
<?xml version="1.0" encoding="UTF-8"?>
<projectDescription>
	<name>lms-daemon-radius-mikrotik</name>
	<comment></comment>
	<projects>
	</projects>
	<buildSpec>
		<buildCommand>
			<name>org.python.pydev.PyDevBuilder</name>
			<arguments>
			</arguments>
		</buildCommand>
	</buildSpec>
	<natures>
		<nature>org.python.pydev.pythonNature</nature>
	</natures>
</projectDescription>


File: /.pydevproject
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<?eclipse-pydev version="1.0"?><pydev_project>
<pydev_pathproperty name="org.python.pydev.PROJECT_SOURCE_PATH">
<path>/${PROJECT_DIR_NAME}</path>
</pydev_pathproperty>
<pydev_property name="org.python.pydev.PYTHON_PROJECT_VERSION">python interpreter</pydev_property>
<pydev_property name="org.python.pydev.PYTHON_PROJECT_INTERPRETER">ldrm</pydev_property>
</pydev_project>


File: /.settings\org.eclipse.core.resources.prefs
eclipse.preferences.version=1
encoding/client_ldrm.py=utf-8
encoding/ldrm.py=utf-8


File: /client_ldrm.py
#!venv/bin/python
# -*- coding: utf-8 -*-

import json
from socket import *
import sys

class clienttcp:
    
    def __init__(self,host,port):
        self.s=socket(AF_INET,SOCK_STREAM)
        self.host=host
        self.port=port
    
    def sendDATA(self,keyData,clientData):
        try:
            self.s.connect((self.host,self.port))
            self.s.settimeout(1)
            try:
                data=json.dumps(['DATA',keyData,clientData])
                self.s.send(data)
                try:
                    msg=json.loads(self.s.recv(1024))
                    self.s.close
                    if msg[0]=='OK':
                        return True
                    else:
                        return False
                except ValueError:
                    print 'Recived data is not json'
            except ValueError:
                print 'Send data is not json'
            except socket.timeout:
                print 'Connection Timeout'
            except socket.error:
                print 'Cant connect to server'
            self.s.close
            return False
        except:
            return False


if __name__ == "__main__":
    data={
        'NAS_Identifier':sys.argv[1],
        'NAS_IP_Address':sys.argv[2],
        'NAS_Port':sys.argv[3],
        'NAS_Port_Type':sys.argv[4],
        'Calling_Station_Id':sys.argv[5],
        'Framed_IP_Address':sys.argv[6],
        'Called_Station_Id':sys.argv[7],
        'User_Name':sys.argv[8],       
        'Password':sys.argv[9]
        }
        
    clienttcp('127.0.0.1',8888).sendDATA(sys.argv[8]+sys.argv[6],data)


File: /conf\ldrm.conf
[main]
# log: debug,info,warn,error,critical
log=debug
File: /createVirtEnv.bash
#!/bin/bash
# 
# Script start in project folder.
DIR=`pwd`

if ! [ -x "$(command -v pip)" ]; then
  echo 'Error: pip is not installed.' >&2
  exit 1
fi

if ! [ -x "$(command -v virtualenv)" ]; then
  echo 'Error: virtualenv is not installed.' >&2
  exit 1
fi

virtualenv --no-site-packages venv
#virtualenv --no-site-packages -p /home/ilusion/workspace/stuff/pypy/pypy2-v5.10.0-linux64/bin/pypy venv
source $DIR/venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
deactivate


File: /install.txt
HOW TO INSTALL
on freeradius server:
- create a directory lms-daemon-radius-mikrotik in /opt
- copy source files to /opt/lms-daemon-radius-mikrotik
- create virtual environment ./createVirtEnv.bash
- configure ldrm daemon file: conf/ldrm.conf
- in freeradius post-auth sections add:
	
		update control { 
        			Auth-Type := `/opt/lms-daemon-radius-mikrotik/venv/bin/python /opt/lms-daemon-radius-mikrotik/client_ldrm.py '%{NAS-Identifier}' '%{NAS-IP-Address}' '%{NAS-Port}' '%{NAS-Port-Type}' '%{Calling-Station-Id}' '%{Framed-IP-Address}' '%{Called-Station-Id}' '%{User-Name}' '%{Password}'`
		}
		
		
USAGE

- start daemon mode:
/opt/lms-daemon-radius-mikrotik/venv/bin/python ldrm.py start
- stop daemon mode:
/opt/lms-daemon-radius-mikrotik/venv/bin/python ldrm.py stop

If you want to run ldrm in debug mode then:
/opt/lms-daemon-radius-mikrotik/venv/bin/python ldrm.py debug
You can also increase the display level of messages by changing the configuration file ldrm.conf

File: /ldrm.py
#!venv/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
from collections import deque
import datetime
import hashlib
import json
import logging
import os.path
from signal import SIGTERM
import socket
import sys
import threading
import time

import daemon.pidfile
import memcache
import mysql.connector
import psycopg2
import ssh2
from ssh2.session import Session
#
# pylibmc
        
class conSQL:
    def __init__(self):
        self.basePath = basePath      
        self.loadConf()

    def loadConf(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open(self.basePath + '/conf/ldrm.conf'))
        self.type = config.get('db', 'type')
        self.ip = config.get('db', 'ip')
        self.port = int(config.get('db', 'port'))
        self.dbname = config.get('db', 'dbname')
        self.login = config.get('db', 'login')
        self.passwd = config.get('db', 'passwd')

    def getDataFromDB(self, mac):
        if self.type == 'mysql':
            results = self.selectMySQL("""SELECT n.id as id, inet_ntoa(n.ipaddr) as ip, n.name as nodename, access, warning
                            FROM nodes as n, macs as m
                            WHERE upper(m.mac) = '%s'
                            AND n.id = m.nodeid
                            ORDER by n.id""" % (mac))
            if results is False:
                return False
            dataMac = None
            if len(results) > 0:
                dataMac = {"id":results[0][0], "ip":results[0][1], "nodename":results[0][2], "access":results[0][3], "warning":results[0][4]}
                results = self.selectMySQL("""SELECT CONCAT(ROUND(COALESCE(x.upceil, y.upceil, z.upceil)),'k','/', ROUND(COALESCE(x.downceil, y.downceil, z.downceil)),'k') AS mrt
                            FROM (
                                SELECT n.id, MIN(n.name) AS name, SUM(t.downceil/o.cnt) AS downceil, SUM(t.upceil/o.cnt) AS upceil
                                FROM nodeassignments na
                                JOIN assignments a ON (na.assignmentid = a.id)
                                 JOIN tariffs t ON (a.tariffid = t.id)
                                JOIN nodes n ON (na.nodeid = n.id)
                                JOIN macs m ON (m.nodeid = n.id)
                                JOIN (
                                SELECT assignmentid, COUNT(*) AS cnt
                                    FROM nodeassignments
                                    GROUP BY assignmentid
                                ) o ON (o.assignmentid = na.assignmentid)
                                WHERE (a.datefrom <= unix_timestamp() OR a.datefrom = 0)
                                AND (a.dateto > unix_timestamp() OR a.dateto = 0)
                                AND upper(m.mac) = '%s'
                                GROUP BY n.id
                            ) x
                            LEFT JOIN (
                                SELECT SUM(t.downceil)/o.cnt AS downceil,
                                SUM(t.upceil)/o.cnt AS upceil
                                FROM assignments a
                                JOIN tariffs t ON (a.tariffid = t.id)
                                JOIN nodes n ON (a.customerid = n.ownerid)
                                JOIN macs m ON (m.nodeid = n.id)
                                JOIN (
                                SELECT COUNT(*) AS cnt, ownerid FROM vnodes
                                WHERE NOT EXISTS (
                                    SELECT 1 FROM nodeassignments, assignments a
                                    WHERE assignmentid = a.id AND nodeid = vnodes.id
                                    AND  (a.dateto > unix_timestamp() OR a.dateto = 0))
                                    GROUP BY ownerid
                                ) o ON (o.ownerid = n.ownerid)
                                WHERE (a.datefrom <= unix_timestamp() OR a.datefrom = 0)
                                AND (a.dateto > unix_timestamp() OR a.dateto = 0)
                                    AND NOT EXISTS (SELECT 1 FROM nodeassignments WHERE assignmentid = a.id)
                                    AND upper(m.mac) = '%s'
                                GROUP BY n.id
                            ) y ON (1=1)
                            RIGHT JOIN (
                                SELECT n.id, n.name, 64 AS downceil, 64 AS upceil
                                    FROM nodes as n,macs as m
                                    WHERE upper(m.mac) = '%s'
                                    AND m.nodeid = n.id
                            ) z ON (1=1)""" % (mac, mac, mac))
                if results is False:
                    return False
                if len(results) > 0:
                    dataMac.update({"mrt":results[0][0]})
                else:
                    logging.warn("conSQL: can't find tariff for %s" % (mac))
            else:
                logging.warn("conSQL: wrong mac address: %s, don't exist in DB" % (mac))
            return dataMac
        elif self.type == 'pgsql':
            results = self.selectPG("""SELECT n.id as id, inet_ntoa(n.ipaddr) as ip, n.name as nodename, access, warning
                            FROM nodes as n, macs as m
                            WHERE upper(m.mac) = '%s'
                            AND n.id = m.nodeid
                            ORDER by n.id""" % (mac))
            if results is False:
                return False
            dataMac = None
            if len(results) > 0:
                dataMac = {"id":results[0][0], "ip":results[0][1], "nodename":results[0][2], "access":results[0][3], "warning":results[0][4]}
                results = self.selectPG("""SELECT CONCAT(ROUND(COALESCE(x.upceil, y.upceil, z.upceil)),'k','/', ROUND(COALESCE(x.downceil, y.downceil, z.downceil)),'k') AS mrt
                            FROM (
                                SELECT n.id, MIN(n.name) AS name, SUM(t.downceil/o.cnt) AS downceil, SUM(t.upceil/o.cnt) AS upceil
                                FROM nodeassignments na
                                JOIN assignments a ON (na.assignmentid = a.id)
                                 JOIN tariffs t ON (a.tariffid = t.id)
                                JOIN nodes n ON (na.nodeid = n.id)
                                JOIN macs m ON (m.nodeid = n.id)
                                JOIN (
                                SELECT assignmentid, COUNT(*) AS cnt
                                    FROM nodeassignments
                                    GROUP BY assignmentid
                                ) o ON (o.assignmentid = na.assignmentid)
                                WHERE (a.datefrom <= extract(epoch from now()) OR a.datefrom = 0)
                                AND (a.dateto > extract(epoch from now()) OR a.dateto = 0)
                                AND upper(m.mac) = '%s'
                                GROUP BY n.id
                            ) x
                            LEFT JOIN (
                                SELECT SUM(t.downceil)/o.cnt AS downceil,
                                SUM(t.upceil)/o.cnt AS upceil
                                FROM assignments a
                                JOIN tariffs t ON (a.tariffid = t.id)
                                JOIN nodes n ON (a.customerid = n.ownerid)
                                JOIN macs m ON (m.nodeid = n.id)
                                JOIN (
                                SELECT COUNT(*) AS cnt, ownerid FROM vnodes
                                WHERE NOT EXISTS (
                                    SELECT 1 FROM nodeassignments, assignments a
                                    WHERE assignmentid = a.id AND nodeid = vnodes.id
                                    AND  (a.dateto > extract(epoch from now()) OR a.dateto = 0))
                                    GROUP BY ownerid
                                ) o ON (o.ownerid = n.ownerid)
                                WHERE (a.datefrom <= extract(epoch from now()) OR a.datefrom = 0)
                                AND (a.dateto > extract(epoch from now()) OR a.dateto = 0)
                                    AND NOT EXISTS (SELECT 1 FROM nodeassignments WHERE assignmentid = a.id)
                                    AND upper(m.mac) = '%s'
                                GROUP BY n.id, o.cnt
                            ) y ON (1=1)
                            RIGHT JOIN (
                                SELECT n.id, n.name, 64 AS downceil, 64 AS upceil
                                    FROM nodes as n,macs as m
                                    WHERE upper(m.mac) = '%s'
                                    AND m.nodeid = n.id
                            ) z ON (1=1)""" % (mac, mac, mac))

                if results is False:
                    return False
                if len(results) > 0:
                    dataMac.update({"mrt":results[0][0]})
                else:
                    logging.warn("conSQL: can't find tariff for %s" % (mac))
            else:
                logging.warn("conSQL: wrong mac address: %s, don't exist in DB" % (mac))
            return dataMac
        else:
            logging.error("conSQL: wrong type of db: %s, supported only mysql or pgslq" % (self.type))

    def selectMySQL(self, query):
        try:
            cnx = mysql.connector.connect(host=self.ip, database=self.dbname, user=self.login, password=self.passwd)
        except Exception as e:
            logging.error('conSQL: ' + str(e))
            return False
        else:
            cursor = cnx.cursor()
            try:
                cursor.execute(query)
            except Exception as e:
                logging.error('conSQL: ' + str(e))
                return False
            else:
                results = cursor.fetchall()
                return results
            finally:
                cnx.close()

    def selectPG(self, query):
        try:
            con = psycopg2.connect(host=self.ip, dbname=self.dbname, user=self.login, password=self.passwd)
        except Exception as e:
            logging.error('conSQL: ' + str(e))
            return False
        else:
            cur = con.cursor()
            try:
                cur.execute(query)
            except Exception as e:
                logging.error('conSQL: ' + str(e))
                return False
            else:
                results = cur.fetchall()
                return results
            finally:
                con.close()


class queueDrd:
    queueDrd = deque([])
    
    dataClient = {}
    
    size = 1000
    
    lock = threading.Lock()

    def fetch(self):
        if len(self.queueDrd) > 0:     
            self.lock.acquire()
            try:
                machash = self.queueDrd.popleft()
                data = self.dataClient.pop(machash)
            finally:
                self.lock.release()
            return [machash, data]
        else:
            return None
    
    def add(self, machash, data):
        if len(self.queueDrd) < self.size:
            
            self.lock.acquire()
            try:  
                if machash not in self.queueDrd:
                    self.queueDrd.append(machash)
                    self.dataClient.update({machash:data})
            finally:
                self.lock.release()
                
     
class deamonMT(threading.Thread):
        
    def __init__(self, QH):  
        threading.Thread.__init__(self)
        self.setDaemon(True)
        
        self.basePath = basePath      
        self.loadConf()
                
        self.cache = memcache.Client([self.ip + ':' + self.port], debug=0) 
    
        self.QH = QH
        
        self.SQL = conSQL()
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    def run(self):
        logging.info("deamonMT: ready and waiting..")
        ql=0
        while True:
            if ql > 0:
                data = self.QH.fetch()
                if data is not None:
                    if self.api == 'ssh':
                        MTCommands=self.createMTCommands(data)
                        if MTCommands is not False:
                            logging.info("deamonMT: sending commands to execute on Mikrotik :\n" + str(MTCommands))
                            self.executeMT(MTCommands[1],MTCommands[0])
                    else:
                        logging.error('deamonMT: incorrect api: %s' % (self.api))
            ql = len(self.QH.queueDrd)
            logging.info("deamonMT: size of queue: %s" % (ql))
            if ql == 0:
                time.sleep(60)
            elif ql == 1:
                time.sleep(30)
            elif ql < 10:
                time.sleep(15)
            elif ql > 0 and ql < 50:
                time.sleep(5)
            elif ql > 0 and ql < 100:
                time.sleep(1)
            elif ql > 0 and ql < 300:
                time.sleep(0.5)
            else:
                time.sleep(0.1)
                    
    
    def createMTCommands(self, data):
        if self.is_valid_ipv4_address(data[1]['Framed_IP_Address']):
            self.macData = self.cache.get(hashlib.sha1(data[0] + data[1]['Framed_IP_Address']).hexdigest())
            if self.macData is None:
                logging.info('deamonMT: miss cache for mac: %s ip: %s, extracting data from DB' % (data[1]['User_Name'], data[1]['Framed_IP_Address']))
                while True:
                    dataSQL = self.SQL.getDataFromDB(data[1]['User_Name'])
                    if dataSQL is False:
                        time.sleep(5)
                    else:
                        if dataSQL is not None:
                            data[1].update({"nodeId":dataSQL["id"]})
                            data[1].update({"access":dataSQL["access"]})
                            data[1].update({"warning":dataSQL["warning"]})
                            data[1].update({"nodename":dataSQL["nodename"]})
                            data[1].update({"mrt":dataSQL["mrt"]})
                            self.cache.set(hashlib.sha1(data[0] + data[1]['Framed_IP_Address']).hexdigest(), data[1], self.time)
                            self.macData = data[1]
                        else:
                            # cant find mac in db, send info?
                            data[1].update({"nodeId":None})
                            self.cache.set(hashlib.sha1(data[0] + data[1]['Framed_IP_Address']).hexdigest(), data[1], self.time)
                            self.macData = data[1]
                        break
            else:
                logging.info('deamonMT: hit cache for mac: %s ip: %s, extracting data from memcached' % (data[1]['User_Name'], data[1]['Framed_IP_Address']))
            execOnMT = None
            logging.debug(self.macData)                                    
            if self.macData['nodeId'] is not None and self.macData['nodename'] is not None and  self.macData['mrt'] is not None and self.is_valid_ipv4_address(self.macData['Framed_IP_Address']) and self.is_valid_ipv4_address(self.macData['NAS_IP_Address']):
                datenow = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
                execOnMT = '/queue simple remove [find target=' + str(self.macData['Framed_IP_Address']) + '/32]; '  
                execOnMT += '/queue simple remove [find name=%s]; ' % (str(self.macData['nodename']))                
                execOnMT += '/ip firewall nat remove [find src-address="' + str(self.macData['Framed_IP_Address']) + '" and chain="'+self.warnchainName+'"]; '
                execOnMT += '/ip firewall address-list remove [find address="' + str(self.macData['Framed_IP_Address']) + '" and list="'+self.blockListName+'"]; '
                if str(self.macData['mrt']) =='0k/0k': 
                    execOnMT += """/queue simple add name=""" + str(self.macData['nodename']) + """ target=""" + str(self.macData['Framed_IP_Address']) + """/32 parent=none packet-marks="" priority=8/8 queue=s100/s100 limit-at=64k/64k max-limit=64k/64k burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s comment=""" + str(datenow) + """; """    
                else:
                    execOnMT += """/queue simple add name=""" + str(self.macData['nodename']) + """ target=""" + str(self.macData['Framed_IP_Address']) + """/32 parent=none packet-marks="" priority=8/8 queue=s100/s100 limit-at=64k/64k max-limit=""" + str(self.macData['mrt']) + """ burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s comment=""" + str(datenow) + """; """ 
                if self.macData['access'] == 0:
                    execOnMT += """/ip firewall address-list add list="""+self.blockListName+""" address=""" + str(self.macData['Framed_IP_Address']) + """ comment=""" + str(self.macData['nodeId']) + """; """
                    if self.macData['warning'] == 1:
                        execOnMT += """/ip firewall nat add chain="""+self.warnchainName+""" action=dst-nat to-addresses=""" + self.lmswarn + """ to-ports=8001 protocol=tcp src-address=""" + str(self.macData['Framed_IP_Address']) + """ limit=10/1h,1:packet log=no log-prefix="" comment=""" + str(datenow) + """; """
                if self.macData['access'] == 1:  
                    if self.macData['warning'] == 1:
                        execOnMT += """/ip firewall nat add chain="""+self.warnchainName+""" action=dst-nat to-addresses=""" + self.lmswarn + """ to-ports=8001 protocol=tcp src-address=""" + str(self.macData['Framed_IP_Address']) + """ limit=10/1h,1:packet log=no log-prefix="" comment=""" + str(datenow) + """; """
                
                logging.debug("deamonMT: Mikrotik commands for ip %s:\n %s" % (self.macData['NAS_IP_Address'], execOnMT))
                
                return (self.macData['NAS_IP_Address'], execOnMT)
            else:
                logging.info('deamonMT: incorrect data: nodeId, access, warning, nodename, mtr, NAS_IP_Address or Framed_IP_Address')
                return False
        else:
            logging.info('deamonMT: incorrect Framed_IP_Address or null')
            return False
        
    def is_valid_ipv4_address(self, address):
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:  
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error: 
            return False
        return True
                    
    def loadConf(self):
        
        config = ConfigParser.ConfigParser()
        config.readfp(open(self.basePath + '/conf/ldrm.conf'))
        
        self.ip = config.get('memcached', 'ip')
        self.port = config.get('memcached', 'port')
        self.time = int(config.get('memcached', 'time'))
        
        self.lmswarn = config.get('lms', 'warnserver')
        
        self.api = config.get('mt', 'api')
        self.loginSsh = config.get('mt', 'login')
        self.passwdSsh = config.get('mt', 'pass')
        self.portSsh = int(config.get('mt', 'port'))
        self.timeoutSsh = int(config.get('mt', 'timeout'))
        
        self.warnchainName = config.get('mt', 'warnchainName')
        self.blockListName = config.get('mt', 'blockListName')
        
    def executeMT(self, execOnMT, ipToCon):
        host = ipToCon
        user = self.loginSsh
        passwd = self.passwdSsh
        port = int(self.portSsh)
        timeout = self.timeoutSsh
               
        i = 0
        while (True):
            if i < 3:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    sock.connect((host, port))
                    session = Session()
                    session.handshake(sock)
                    session.userauth_password(user, passwd)
                    channel = session.open_session()
                    channel.execute(execOnMT)
                    channel.wait_eof()
                    channel.close()
                    channel.wait_closed()
                except Exception as e:
                    logging.warn('deamonMT: %s', (e))
                else:
                    logging.info('deamonMT: ssh commands has been sent, SUCCESS')
                    break
                finally:
                    sock.close()
                time.sleep(1)    
                i += 1
            else:
                logging.info("deamonMT: ssh can't connect to host: %s", (host))
                break 

class servertcp(threading.Thread):
        
    def __init__(self, QH):  
        threading.Thread.__init__(self)
        self.setDaemon(True)
        
        self.basePath = basePath      
        self.loadConf()        
        
        self.QH = QH
        
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, int(self.port)))
        s.listen(5)
        logging.info("servertcp(on port %s): ready and waiting.." % (self.port))
        while True:
            client, ipPort = s.accept()
            client.settimeout(int(self.connectionTimeout))
            if ipPort[0] == '127.0.0.1':
                try:
                    data = json.loads(client.recv(1024))
                    if data[0] == 'DATA':
                        self.QH.add(hashlib.sha1(data[1]).hexdigest(), data[2])
                        client.send(json.dumps(['OK']))
                        logging.info("servertcp: new data, mac: %s from %s" % (data[2]['User_Name'], ipPort[0]))
                    else:
                        client.send(json.dumps(['BADCOMMAND']))
                    client.close    
                except ValueError as e:
                    logging.warn('servertcp: recived data is not json, %s' % (e))
                    client.close
                except socket.timeout as e:
                    logging.warn('servertcp: connection Timeout, %s' % (e))
                    client.close
            else:
                logging.warn("servertcp: dont't accept conections form %s, only localhost is accepted" % (ipPort[0]))
                client.close
            
    def loadConf(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open(self.basePath + '/conf/ldrm.conf'))
        self.host = config.get('tcpserver', 'host')
        self.port = config.get('tcpserver', 'port')
        self.connectionTimeout = config.get('tcpserver', 'connectionTimeout')

        
class ldrm:
        
    def __init__(self, basePath):
        self.basePath = basePath
        self.loadConf()
    
    def run(self):
        if 'debug' == sys.argv[1]:
            if self.log == 'debug':
                logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
            elif self.log == 'info':
                logging.basicConfig(level=logging.INFO, format='%(relativeCreated)6d %(threadName)s %(message)s')
            elif self.log == 'warn':
                logging.basicConfig(level=logging.WARN, format='%(relativeCreated)6d %(threadName)s %(message)s')
            elif self.log == 'error':
                logging.basicConfig(level=logging.ERROR, format='%(relativeCreated)6d %(threadName)s %(message)s')
            elif self.log == 'critical':
                logging.basicConfig(level=logging.CRITICAL, format='%(relativeCreated)6d %(threadName)s %(message)s')
            else:
                logging.basicConfig(level=logging.INFO, format='%(relativeCreated)6d %(threadName)s %(message)s')
        else:
            if self.log == 'debug':
                logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-1s %(levelname)-1s %(message)s',
                            datefmt='%d-%m-%d %H:%M',
                            filename=self.logFile,
                            filemode='w')
            elif self.log == 'info':
                logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-1s %(levelname)-1s %(message)s',
                            datefmt='%d-%m-%d %H:%M',
                            filename=self.logFile,
                            filemode='w')
            elif self.log == 'warn':
                logging.basicConfig(level=logging.WARN,
                            format='%(asctime)s %(name)-1s %(levelname)-1s %(message)s',
                            datefmt='%d-%m-%d %H:%M',
                            filename=self.logFile,
                            filemode='w')
            elif self.log == 'error':
                logging.basicConfig(level=logging.ERROR,
                            format='%(asctime)s %(name)-1s %(levelname)-1s %(message)s',
                            datefmt='%d-%m-%d %H:%M',
                            filename=self.logFile,
                            filemode='w')
            elif self.log == 'critical':
                logging.basicConfig(level=logging.CRITICAL,
                            format='%(asctime)s %(name)-1s %(levelname)-1s %(message)s',
                            datefmt='%d-%m-%d %H:%M',
                            filename=self.logFile,
                            filemode='w')
            else:
                logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-1s %(levelname)-1s %(message)s',
                            datefmt='%d-%m-%d %H:%M',
                            filename=self.logFile,
                            filemode='w')

        logging.info("ldrm: start main thread")

        QH = queueDrd()
        
        ST = servertcp(QH)
        ST.start()
        
        DMT = deamonMT(QH)
        DMT.start()

        while True:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                if 'debug' == sys.argv[1]:
                    break

            if ST.is_alive() is False:
                logging.error("ldrm: threads servertcp is down, starting new")
                ST = servertcp(QH)
                ST.start()

            if DMT.is_alive() is False:
                logging.error("ldrm: threads deamonMT is down, starting new")
                DMT = deamonMT(QH)
                DMT.start()
                    
        logging.info("ldrm: stop main thread")
                
    def loadConf(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open(self.basePath + '/conf/ldrm.conf'))
        self.log = config.get('main', 'log')
        self.logFile = config.get('main', 'logFile')

    def start(self):
        """
        Start the daemon
        """
        if os.path.isfile(self.basePath + '/conf/ldrm.conf') is False:
            print 'ldrm: Where is conf, should be in main directory\nfile: ldrm.conf'
            sys.exit(1)
        
        pidfile = '/tmp/ldrm.pid'
        try:
            pf = file(pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
    
        if pid:
            message = "ldrm: pidfile %s already exist. Daemon already running?"
            sys.stderr.write(message % pidfile)
            sys.exit(1)
        
        working_directory = self.basePath
        pidfile = daemon.pidfile.PIDLockFile(pidfile)

        with daemon.DaemonContext(working_directory=working_directory, pidfile=pidfile):
                self.run()

    def stop(self):
        """
        Stop the daemon
        """        

        pidfile = '/tmp/ldrm.pid'
        
        try:
            pf = file(pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
    
        if not pid:
            message = "pidfile %s does not exist. Daemon not running?"
            sys.stderr.write(message % pidfile)
            return 
           
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError, err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(pidfile):
                    os.remove(pidfile)
            else:
                print str(err)
                sys.exit(1)

    
if __name__ == "__main__":
    basePath = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) == 2:
        if 'debug' == sys.argv[1]:
            ldrm(basePath).run()
        elif 'start' == sys.argv[1]:            
            ldrm(basePath).start()
        elif 'stop' == sys.argv[1]:
            ldrm(basePath).stop()
        elif 'restart' == sys.argv[1]:
            ldrm(basePath).stop()
            ldrm(basePath).start()
        elif 'help' == sys.argv[1]:
            print "usage: %s \n\trestart \t\t-> restart deamon \n\tstart \t\t-> start deamon \n\tstop \t\t-> stop deamon \n\tdebug \t-> non-daemon mode \n\thelp \t-> show this" % sys.argv[0]
            sys.exit(2)
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s \n\tstart \t-> start deamon \n\tstop \t-> stop deamon \n\tdebug \t-> non-daemon mode \n\thelp \t-> show this" % sys.argv[0]
        sys.exit(2)

File: /LICENSE
MIT License

Copyright (c) 2018 noXgle system

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


File: /log\.gitignore
File: /README.md
# ldrm

# DESCRIPTIONS
ldrm (lms-daemon-radius-mikrotik) is a demon to the LMS system (http://www.lms.org.pl/) to perform tasks on Mikrotik after Freeradius authorization. It consists of two parts:
- demon: ldrm.py
- script: client_ldrm.py 

# REQUIREMENTS
- installed python 2.7
- installed pip and virtualenv
- you can install memcached services, on debian: apt-get install memcached for better performance

# HOW TO INSTALL
see install.txt

# USAGE
see install.txt



File: /Readme.pl
O  lms-daemon-radius-mikrotik 
Demon lms-daemon-radius-mikrotik umożliwia wykonywanie zadań zauotoryzowanym klientom zadań na mikrotiku:
- ustawia przepustowości dla klientów
- tworzy wpisy do firewall z przekierowaniem na winietkę z ostrzeżeniem dla klientów, którzy mają włączone ostrzeżenia
- tworzy listę osób, którzy mają status odłączony

Wszystkie zadania są kolejkowanie i wykonywane z kliku sekundowym poślizgiem żeby zapobiec przeciążaniu mikrotika i bazy danych przez klientów, którzy robią up-down. Połączania pomiędzy demonem a mikrotikiem wykonywane są po ssh.

Całość instalujemy na freeradiusie, obsługuje naraz wiele mikrotików. 

Skrócony opis instalacji:
z root zainstalować: pip i virtualenv
prze-logować się na użytkownika i wykonać rzeczy z pliku install.txt 


File: /requirements.txt
ConfigParser
mysql-connector
daemon
pidfile
python-daemon
python-memcached
#psycopg2
psycopg2-binary
ssh2-python

