# Repository Information
Name: mikrotik_swos_tools

# Directory Structure
Directory structure:
└── github_repos/mikrotik_swos_tools/
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
    │   │       ├── pack-b258f15496c7ad1cc46496ca22847bda77b3eadb.idx
    │   │       └── pack-b258f15496c7ad1cc46496ca22847bda77b3eadb.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── CHANGELOG.rst
    ├── CMakeLists.txt
    ├── LICENSE
    ├── msg/
    │   └── Statistics.msg
    ├── nodes/
    │   └── swos_api
    ├── package.xml
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
	url = https://github.com/ctu-vras/mikrotik_swos_tools.git
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
0000000000000000000000000000000000000000 c87667b33191258409efdab1aa71c1c826e48f06 vivek-dodia <vivek.dodia@icloud.com> 1738606070 -0500	clone: from https://github.com/ctu-vras/mikrotik_swos_tools.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 c87667b33191258409efdab1aa71c1c826e48f06 vivek-dodia <vivek.dodia@icloud.com> 1738606070 -0500	clone: from https://github.com/ctu-vras/mikrotik_swos_tools.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 c87667b33191258409efdab1aa71c1c826e48f06 vivek-dodia <vivek.dodia@icloud.com> 1738606070 -0500	clone: from https://github.com/ctu-vras/mikrotik_swos_tools.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
c87667b33191258409efdab1aa71c1c826e48f06 refs/remotes/origin/master
23481ed6e992d04650cc1269b85cf6d1a53640a1 refs/tags/1.0.1
4a74134fa65b6f557e0c9952b26866f877d29149 refs/tags/1.1.0
c87667b33191258409efdab1aa71c1c826e48f06 refs/tags/1.1.1
f8a42c0179d9e2bbbe5755f9d734504ad214759b refs/tags/cave_submission


File: /.git\refs\heads\master
c87667b33191258409efdab1aa71c1c826e48f06


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /CHANGELOG.rst
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package mikrotik_swos_tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.1.1 (2023-04-16)
------------------
* Noetic compatibility (2nd round).
* Contributors: Martin Pecka

1.1.0 (2022-06-08)
------------------
* Noetic compatibility
* Contributors: Martin Pecka

1.0.1 (2020-02-09)
------------------
* Initial commit.
* Contributors: Martin Pecka


File: /CMakeLists.txt
cmake_minimum_required(VERSION 3.10.2)
project(mikrotik_swos_tools)

find_package(catkin REQUIRED COMPONENTS message_generation std_msgs)

add_message_files(DIRECTORY msg)
generate_messages(DEPENDENCIES std_msgs)

catkin_package(CATKIN_DEPENDS message_runtime std_msgs)

catkin_install_python(PROGRAMS
  nodes/swos_api
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


File: /LICENSE
BSD 3-Clause License

Copyright (c) 2020, Martin Pecka
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
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


File: /msg\Statistics.msg
# Holds the data presented on the statistics tab of SwOS web interface
# All arrays have one entry per enabled port.

Header header
string[] port_names
uint8[] port_numbers
int64[] rx_rate_bytes
int64[] rx_rate_packets
int64[] tx_rate_bytes
int64[] tx_rate_packets
int64[] rx_bytes
int64[] rx_packets
int64[] rx_unicasts
int64[] rx_broadcasts
int64[] rx_multicasts
int64[] rx_64
int64[] rx_127
int64[] rx_255
int64[] rx_511
int64[] rx_1023
int64[] rx_1518
int64[] rx_jumbo
int64[] tx_bytes
int64[] tx_packets
int64[] tx_unicasts
int64[] tx_broadcasts
int64[] tx_multicasts
int64[] tx_64
int64[] tx_127
int64[] tx_255
int64[] tx_511
int64[] tx_1023
int64[] tx_1518
int64[] tx_jumbo

File: /nodes\swos_api
#!/usr/bin/env python

# For license see file LICENSE in the root of this repo.

from builtins import int

import json
import re
import requests

import rospy

from mikrotik_swos_tools.msg import Statistics


class SwOSAPI:
    def __init__(self):
        self._rate = rospy.Rate(rospy.get_param("~rate", 0.1))
        self._username = rospy.get_param("~username", "admin")
        self._password = rospy.get_param("~password", "")
        self._address = rospy.get_param("~address", "http://192.168.88.1/")
        if not self._address.startswith("http://"):
            self._address = "http://" + self._address
        if not self._address.endswith("/"):
            self._address += "/"

        self._identity = None
        self._port_names = None
        self._enabled_ports = None
        self._enabled_port_names = None
        self._enabled_port_numbers = None

        wait_for_switch = rospy.get_param("~wait_for_switch", False)
        if wait_for_switch:
            switch_ok = False
            while not rospy.is_shutdown() and not switch_ok:
                try:
                    self._collect_sys_tab_data()
                    switch_ok = True
                except requests.exceptions.RequestException as e:
                    rospy.logwarn("Waiting for switch management interface %s to become available." % self._address)
                    rospy.logdebug("Switch management interface error: " + str(e))
                    rospy.sleep(rospy.Duration(1, 0))
            if rospy.is_shutdown():
                return

        self._stats_pub = rospy.Publisher('~statistics', Statistics, queue_size=1)

        rospy.loginfo("Set up Mikrotik SwOS API on %s" % (self._address, ))

    def _request(self, url):
        response = requests.get(url, auth=requests.auth.HTTPDigestAuth(self._username, self._password))
        response.raise_for_status()
        return response

    def _api_request(self, url_command):
        response = self._request("%s%s" % (self._address, url_command))
        response = self._fix_broken_json(response.text)
        return json.loads(response)

    def _collect_sys_tab_data(self):
        response = self._api_request("sys.b")
        self._identity = self._decode_string(response["id"])
        rospy.loginfo("The connected switch is called '%s'" % self._identity)

    @property
    def identity(self):
        if self._identity is None:
            self._collect_sys_tab_data()
        return self._identity

    def _collect_link_tab_data(self):
        response = self._api_request("link.b")
        self._port_names = [self._decode_string(s) for s in response["nm"]]
        rospy.loginfo("The connected switch has ports '%r'" % self._port_names)

        enabled = int(response["en"], base=16)
        self._enabled_ports = list()
        port_bit = 1
        for _ in range(len(self._port_names)):
            self._enabled_ports.append((port_bit & enabled) != 0)
            port_bit = port_bit << 1

        self._enabled_port_names = list()
        self._enabled_port_numbers = list()
        all_i = 0
        for port_name in self._port_names:
            if self._enabled_ports[all_i]:
                self._enabled_port_names.append(port_name)
                self._enabled_port_numbers.append(all_i)
            all_i += 1

        rospy.loginfo("Ports %r with numbers %r are enabled" % (self._enabled_port_names, [i+1 for i in self._enabled_port_numbers]))

    @property
    def port_names(self):
        if self._port_names is None:
            self._collect_link_tab_data()
        return self._port_names

    @property
    def enabled_ports(self):
        if self._enabled_ports is None:
            self._collect_link_tab_data()
        return self._enabled_ports

    @property
    def enabled_port_names(self):
        if self._enabled_port_names is None:
            self._collect_link_tab_data()
        return self._enabled_port_names

    @property
    def enabled_port_numbers(self):
        if self._enabled_port_numbers is None:
            self._collect_link_tab_data()
        return self._enabled_port_numbers

    def _collect_statistics_tab_data(self):

        stats = self._api_request('!stats.b')
        for k, values in stats.items():
            stats[k] = [val for val, enabled in zip(values, self.enabled_ports) if enabled]

        result = Statistics()

        result.header.stamp = rospy.Time.now()
        result.header.frame_id = self.identity
        result.port_names = self.enabled_port_names
        result.port_numbers = self.enabled_port_numbers

        # rate
        result.rx_rate_bytes = [self._decode_byte_rate(d) / 8 for d in stats['rrb']]
        result.rx_rate_packets = [self._decode_packet_rate(d) for d in stats['rrp']]
        result.tx_rate_bytes = [self._decode_byte_rate(d) / 8 for d in stats['trb']]
        result.tx_rate_packets = [self._decode_packet_rate(d) for d in stats['trp']]

        # rx
        result.rx_bytes = self._get_long_stats(stats, 'rb')
        result.rx_packets = [self._decode_int(d) for d in stats['rtp']]
        result.rx_unicasts = self._get_long_stats(stats, 'rup')
        result.rx_broadcasts = self._get_long_stats(stats, 'rbp')
        result.rx_multicasts = self._get_long_stats(stats, 'rmp')
        result.rx_64 = [self._decode_int(d) for d in stats['r64']]
        result.rx_127 = [self._decode_int(d) for d in stats['r65']]
        result.rx_255 = [self._decode_int(d) for d in stats['r128']]
        result.rx_511 = [self._decode_int(d) for d in stats['r256']]
        result.rx_1023 = [self._decode_int(d) for d in stats['r512']]
        result.rx_1518 = [self._decode_int(d) for d in stats['r1k']]
        result.rx_jumbo = [self._decode_int(d) for d in stats['rmax']]

        # tx
        result.tx_bytes = self._get_long_stats(stats, 'tb')
        result.tx_packets = [self._decode_int(d) for d in stats['ttp']]
        result.tx_unicasts = self._get_long_stats(stats, 'tup')
        result.tx_broadcasts = self._get_long_stats(stats, 'tbp')
        result.tx_multicasts = self._get_long_stats(stats, 'tmp')
        result.tx_64 = [self._decode_int(d) for d in stats['t64']]
        result.tx_127 = [self._decode_int(d) for d in stats['t65']]
        result.tx_255 = [self._decode_int(d) for d in stats['t128']]
        result.tx_511 = [self._decode_int(d) for d in stats['t256']]
        result.tx_1023 = [self._decode_int(d) for d in stats['t512']]
        result.tx_1518 = [self._decode_int(d) for d in stats['t1k']]
        result.tx_jumbo = [self._decode_int(d) for d in stats['tmax']]

        return result

    def run(self):
        while not rospy.is_shutdown():
            try:
                self._stats_pub.publish(self._collect_statistics_tab_data())
            except requests.exceptions.RequestException as e:
                rospy.logerr("Error communicating with Mikrotik SwOS API: " + str(e))
            self._rate.sleep()

    @staticmethod
    def _decode_byte_rate(s):
        return int(s, base=16) * 10

    @staticmethod
    def _decode_packet_rate(s):
        return int(s, base=16)

    @staticmethod
    def _decode_int(s):
        return int(s, base=16)

    @staticmethod
    def _decode_long(s_low, s_high):
        return int("0x" + s_high[2:] + s_low[2:], base=16)

    def _get_long_stats(self, stats, param):
        return [self._decode_long(d, dh) for d, dh in zip(stats[param], stats[param + 'h'])]

    @staticmethod
    def _decode_string(s):
        result = ""
        for i in range(len(s) // 2):
            strnum = s[2 * i:(2 * i + 2)]
            num = int(strnum, base=16)
            ch = chr(num)
            result += ch
        return result

    @staticmethod
    def _fix_broken_json(broken_json):
        result = re.sub(r'([{,])([a-zA-Z][a-zA-Z0-9]+)', '\\1"\\2"', broken_json)
        result = re.sub(r'\'', '"', result)
        result = re.sub(r'(0x[0-9a-zA-Z]+)', '"\\1"', result)

        return result


if __name__ == '__main__':
    rospy.init_node("swos_api")
    api = SwOSAPI()

    try:
        api.run()
    except rospy.ROSInterruptException:
        pass


File: /package.xml
<?xml version="1.0"?>
<package format="3">
  <name>mikrotik_swos_tools</name>
  <version>1.1.1</version>
  <description>Integration between ROS (Robot Operating System) and Mikrotik SwOS</description>

  <license>BSD</license>

  <url type="website">https://github.com/peci1/mikrotik_swos_tools</url>
  <url type="issuetracker">https://github.com/peci1/mikrotik_swos_tools/issues</url>

  <maintainer email="peckama2@fel.cvut.cz">Martin Pecka</maintainer>
  <author email="peckama2@fel.cvut.cz">Martin Pecka</author>

  <buildtool_depend>catkin</buildtool_depend>

  <build_depend>message_generation</build_depend>
  <exec_depend>message_runtime</exec_depend>
  <depend>std_msgs</depend>

  <exec_depend>rospy</exec_depend>
  <exec_depend condition="$ROS_PYTHON_VERSION == 2">python-future</exec_depend>
  <exec_depend condition="$ROS_PYTHON_VERSION == 3">python3-future</exec_depend>
  <exec_depend condition="$ROS_PYTHON_VERSION == 2">python-requests</exec_depend>
  <exec_depend condition="$ROS_PYTHON_VERSION == 3">python3-requests</exec_depend>
</package>


File: /README.md
# mikrotik_swos_tools

Integration between ROS (Robot Operating System) and Mikrotik SwOS.

## Nodes

### swos_api

Gives access to the web management interface via ROS.

If connection to the switch fails, a `requests.exceptions.RequestException` python exception is thrown and the node exits - unless `wait_for_switch` is set to True.

#### Parameters

- `rate` (`double`): Rate at which to query the switch for updates (in Hz, default `0.1`).
- `username` (`string`): Username of the management user (default: `admin`).
- `password` (`string`): Password of the management user (default: empty string)
- `address` (`string`): URL of the management interface (default: `http://192.168.88.1/`)
- `wait_for_switch` (`bool`): If true, the script will wait for the switch management interface to become available before advertising its topics and services. If false, the script dies if the management interface is not accessible. Default is `False`.

#### Published topics

- `~statistics` (`mikrotik_swos_tools/Statistics`): Data from the Statistics tab as a ROS message. Published regularly on the given rate.

